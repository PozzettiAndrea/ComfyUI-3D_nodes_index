<a id="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">ComfyUI Ollama VL Prompt Generator</h3>
  <p align="center">
    A custom ComfyUI node that uses Ollama vision-language models to generate or refine prompts from multiple input images and text.
    <br />
    <br />
    <a href="https://github.com/JuanBerta/comfyui_ollama_vl_prompt/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/JuanBerta/comfyui_ollama_vl_prompt/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This project provides a **ComfyUI custom node** that connects to **Ollama** and lets the user choose *any* local vision-language (VL) model to generate or refine prompts based on:

* Up to 3 input images (supporting individual batch processing or combined context).
* Configurable presets via an external JSON file.
* An optional user hint or base text prompt.

The node is **model-agnostic**: if the model is installed in Ollama, you can select it.

### Key Features
* **Editable Presets**: Customize system prompts easily via `presets.json`.
* **Multi-Image Support**: Process images separately or as a single combined context.
* **Local Execution**: Zero cloud dependency — everything runs on your machine.

## Getting Started

### Prerequisites
* **ComfyUI** installed.
* **Ollama** running locally.
* A **VL-capable model** (e.g., `llava`, `moondream`, `qwen2-vl`).

Verify Ollama status:
`ollama list`

### Installation

1. Clone inside `custom_nodes`:
   `git clone https://github.com/JuanBerta/comfyui_ollama_vl_prompt.git`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Restart ComfyUI.

## Usage

1. Add the **Ollama VL -> Prompt** node.
2. **Inputs**:
   * `image1` (Required), `image2`, `image3`: Input image tensors.
   * `preset`: Choose a template from `presets.json`.
   * `combine_all_images`: `True` for combined context, `False` for individual prompts.
   * `user_hint`: Additional text instructions.
3. **Settings**:
   * `model`: Select your auto-detected Ollama model.
   * `keep_alive`: Model VRAM duration in minutes.

## Roadmap
* [x] Ollama model auto-detection.
* [x] Multi-image input support.
* [x] Custom presets via JSON.
* [ ] Streaming token output.

## License
Distributed under the MIT License.

## Contact
Juan - GitHub: [https://github.com/JuanBerta](https://github.com/JuanBerta)
Project: [https://github.com/JuanBerta/comfyui_ollama_vl_prompt](https://github.com/JuanBerta/comfyui_ollama_vl_prompt)

## Acknowledgments
* ComfyUI community.
* Ollama team.
