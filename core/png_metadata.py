import copy
import json
import logging
from dataclasses import fields
from io import BytesIO
from os import makedirs
from pathlib import Path
from typing import List, Union

import piexif
import piexif.helper
from PIL import Image
from PIL.PngImagePlugin import PngInfo

from core.config import config
from core.types import (
    ControlNetQueueEntry,
    Img2ImgQueueEntry,
    InpaintQueueEntry,
    Txt2ImgQueueEntry,
    UpscaleQueueEntry,
)
from core.utils import unwrap_enum_name

logger = logging.getLogger(__name__)


def create_metadata(
    job: Union[
        Txt2ImgQueueEntry,
        Img2ImgQueueEntry,
        InpaintQueueEntry,
        ControlNetQueueEntry,
        UpscaleQueueEntry,
    ],
    index: int,
):
    "Return image with metadata burned into it"

    data = copy.copy(job.data)

    text_metadata = PngInfo()
    exif_meta_dict = {}

    if not isinstance(job, UpscaleQueueEntry):
        data.seed = str(job.data.seed) + (f"({index})" if index > 0 else "")  # type: ignore Overwrite for sequencialy generated images

    def write_metadata_text(key: str):
        text_metadata.add_text(key, str(unwrap_enum_name(data.__dict__.get(key, ""))))

    def write_metadata_exif(key: str):
        exif_meta_dict[key] = str(unwrap_enum_name(data.__dict__.get(key, "")))

    if config.api.image_extension == "png":
        for key in fields(data):
            if key.name not in ("image", "mask_image"):
                write_metadata_text(key.name)
    else:
        for key in fields(data):
            if key.name not in ("image", "mask_image"):
                write_metadata_exif(key.name)

    if isinstance(job, Txt2ImgQueueEntry):
        procedure = "txt2img"
    elif isinstance(job, Img2ImgQueueEntry):
        procedure = "img2img"
    elif isinstance(job, InpaintQueueEntry):
        procedure = "inpaint"
    elif isinstance(job, ControlNetQueueEntry):
        procedure = "control_net"
    elif isinstance(job, UpscaleQueueEntry):
        procedure = "upscale"
    else:
        procedure = "unknown"

    if config.api.image_extension == "png":
        text_metadata.add_text("procedure", procedure)
        text_metadata.add_text("model", job.model)
        user_comment: bytes = b""  # for type checking
    else:
        exif_meta_dict["procedure"] = procedure
        exif_meta_dict["model"] = job.model

        user_comment = piexif.helper.UserComment.dump(
            json.dumps(exif_meta_dict, ensure_ascii=False), encoding="unicode"
        )

    return text_metadata if config.api.image_extension == "png" else user_comment


def save_images(
    images: List[Image.Image],
    job: Union[
        Txt2ImgQueueEntry,
        Img2ImgQueueEntry,
        InpaintQueueEntry,
        ControlNetQueueEntry,
        UpscaleQueueEntry,
    ],
):
    "Save image to disk or r2"

    if isinstance(
        job,
        (
            Txt2ImgQueueEntry,
            Img2ImgQueueEntry,
            InpaintQueueEntry,
        ),
    ):
        prompt = (
            job.data.prompt[:30]
            .strip()
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
            .replace("[", "")
            .replace("]", "")
            .replace("?", "")
            .replace("!", "")
            .replace(":", "")
            .replace(";", "")
            .replace("'", "")
            .replace('"', "")
            .replace(" ", "_")
            .replace("<", "")
            .replace(">", "")
        )
    else:
        prompt = ""

    urls: List[str] = []
    for i, image in enumerate(images):
        if isinstance(job, UpscaleQueueEntry):
            folder = "extra"
        elif isinstance(job, Txt2ImgQueueEntry):
            folder = "txt2img"
        else:
            folder = "img2img"

        metadata = create_metadata(job, i)

        if job.save_image == "r2":
            # Save into Cloudflare R2 bucket
            from core.shared_dependent import r2

            assert r2 is not None, "R2 is not configured, enable debug mode to see why"

            filename = f"{job.data.id}-{i}.png"
            image_bytes = BytesIO()
            image.save(image_bytes, pnginfo=metadata, format=config.api.image_extension)
            image_bytes.seek(0)

            url = r2.upload_file(file=image_bytes, filename=filename)
            if url:
                logger.debug(f"Saved image to R2: {filename}")
                urls.append(url)
            else:
                logger.debug("No provided Dev R2 URL, uploaded but returning empty URL")
        else:
            base_dir = Path("data/outputs")
            extra_path = config.api.save_path_template.format(
                **{
                    "prompt": prompt,
                    "id": job.data.id,
                    "folder": folder,
                    "seed": job.data.seed
                    if not isinstance(job, UpscaleQueueEntry)
                    else "0",
                    "index": i,
                    "extension": config.api.image_extension,
                }
            )

            path = base_dir / extra_path

            makedirs(path.parent, exist_ok=True)

            with path.open("wb") as f:
                logger.debug(f"Saving image to {path.as_posix()}")

                if config.api.image_extension == "png":
                    image.save(f, pnginfo=metadata)
                else:
                    # ! This is using 2 filesystem calls, find a way to save directly to disk with metadata properly inserted

                    # Save the image
                    image.save(f, quality=config.api.image_quality)

                    # Insert metadata
                    exif_metadata = {
                        "0th": {},
                        "Exif": Image.Exif(),
                        "GPS": {},
                        "Interop": {},
                        "1st": {},
                    }
                    exif_metadata["Exif"][piexif.ExifIFD.UserComment] = metadata
                    exif_bytes = piexif.dump(exif_metadata)
                    piexif.insert(exif_bytes, path.as_posix())

    return urls
