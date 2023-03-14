<div align="center">

  <img src="static/volta-rounded.svg" alt="logo" width="200" height="auto" />
  <h1>VoltaML - Fast Stable Diffusion</h1>
  
  <p><b>
    Stable Diffusion WebUI and API accelerated by <a href="https://github.com/facebookincubator/AITemplate">AITemplate</a> 
  </b></p>
  
  
  <p>
    <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/graphs/contributors">
      <img src="https://img.shields.io/github/contributors/VoltaML/voltaML-fast-stable-diffusion" alt="contributors" />
    </a>
    <a href="">
      <img src="https://img.shields.io/github/last-commit/VoltaML/voltaML-fast-stable-diffusion" alt="last update" />
    </a>
    <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/network/members">
      <img src="https://img.shields.io/github/forks/VoltaML/voltaML-fast-stable-diffusion" alt="forks" />
    </a>
    <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/stargazers">
      <img src="https://img.shields.io/github/stars/VoltaML/voltaML-fast-stable-diffusion" alt="stars" />
    </a>
    <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/issues/">
      <img src="https://img.shields.io/github/issues/VoltaML/voltaML-fast-stable-diffusion" alt="open issues" />
    </a>
    <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/VoltaML/voltaML-fast-stable-diffusion.svg" alt="license" />
    </a>
    <a href="https://github.com/voltaML/voltaML-fast-stable-diffusion/tree/experimental">
      <img src="https://img.shields.io/github/commit-activity/m/VoltaML/voltaML-fast-stable-diffusion/experimental?label=commit%20activity%20-%20experimental" alt="commit activity on experimental" />
    </a>
    <a href="https://github.com/voltaML/voltaML-fast-stable-diffusion/tree/experimental">
      <img src="https://img.shields.io/github/last-commit/VoltaMl/voltaML-fast-stable-diffusion/experimental?label=last%20commit%20-%20experimental" alt="latest activity on experimental" />
    </a>
  </p>
  <a href="https://discord.gg/pY5SVyHmWm"> <img src="https://dcbadge.vercel.app/api/server/pY5SVyHmWm" /> </a> 
    
  <h4>
      <a href="https://stax124.github.io/voltaML-fast-stable-diffusion/">Documentation</a>
    <span> · </span>
      <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/issues/new/choose">Report Bug</a>
    <span> · </span>
      <a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/issues/new/choose">Request Feature</a>
  </h4>

</div>

<br />

<h1> Table of Contents</h1>

- [About the Project](#about-the-project)
  - [Screenshots](#screenshots)
  - [Tech Stack](#tech-stack)
  - [Features](#features)
  - [Speed comparison](#speed-comparison)
  - [Installation](#installation)
- [Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Contact](#contact)

# About the Project

## Screenshots

<div align="center"> 
  <img src="docs/static/frontend/frontend-txt2img.webp" alt="screenshot" />
  <img src="docs/static/frontend/frontend-img2img.webp" alt="screenshot" />
  <img src="docs/static/frontend/frontend-browser.webp" alt="screenshot" />
</div>

## Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://vuejs.org/">Vue.js</a></li>
    <li><a href="https://www.naiveui.com/en-US/dark">NaiveUI</a></li>
    <li><a href="https://ionic.io/ionicons">Ionicons</a></li>
  </ul>
</details>

<details>
  <summary>API</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://pytorch.org/">PyTorch</a></li>
    <li><a href="https://github.com/facebookincubator/AITemplate">AITemplate</a></li>
    <li><a href="https://github.com/facebookresearch/xformers">xFormers</a></li>
    <li><a href="https://websockets.readthedocs.io/en/stable/">WebSockets</a></li>
  </ul>
</details>

<details>
<summary>Discord Bot</summary>
  <ul>
    <li><a href="https://github.com/Rapptz/discord.py">Discord.py</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://github.com/features/actions">GitHub Actions</a></li>
    <li><a href="https://pages.github.com/">GitHub Pages</a></li>
    <li><a href="https://vitepress.vuejs.org/">VitePress</a></li>
  </ul>
</details>

## Features

- Easy install with Docker
- Clean and simple Web UI
- Supports PyTorch as well as TensorRT for fastest inference
- Support for Windows and Linux (TRT is not officialy supported on Windows if running locally)
- xFormers support
- GPU cluster support with load balancing
- Discord bot

## Speed comparison

The below benchmarks have been done for generating a 512x512 image, batch size 1 for 50 iterations.

| GPU (it/s) | T4  | A10  | A100 | 4090 | 3090 | 2080Ti | 3050 |
| ---------- | --- | ---- | ---- | ---- | ---- | ------ | ---- |
| PyTorch    | 4.3 | 8.8  | 15.1 | 19   | 11   | 8      | 4.1  |
| xFormers   | 5.5 | 15.6 | 27.5 | 28   | 15.7 | N/A    | 5.1  |
| AITemplate | N/A | 23   | N/A  | N/A  | N/A  | N/A    | 9.7  |

## Installation

Please see the [documentation](https://voltaml.github.io/voltaML-fast-stable-diffusion/installation/docker.html) for installation instructions.

# Contributing

<a href="https://github.com/VoltaML/voltaML-fast-stable-diffusion/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=VoltaML/voltaML-fast-stable-diffusion" />
</a>

Contributions are always welcome!

See `contributing.md` for ways to get started.

## Code of Conduct

Please read the [Code of Conduct](https://github.com/VoltaML/voltaML-fast-stable-diffusion/blob/master/CODE_OF_CONDUCT.md)

# License

Distributed under the <b>GPL v3</b>. See [License](https://github.com/VoltaML/voltaML-fast-stable-diffusion/blob/experimental/License) for more information.

# Contact

Feel free to contact us on discord: https://discord.gg/pY5SVyHmWm

Project Link: [https://github.com/VoltaML/voltaML-fast-stable-diffusion](https://github.com/VoltaML/voltaML-fast-stable-diffusion)
