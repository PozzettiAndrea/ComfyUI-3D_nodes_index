# ComfyUI Qwen VL Nodes

This repository provides ComfyUI nodes that wrap the latest vision-language and language-only checkpoints from the Qwen family. Both **Qwen3 VL** and **Qwen2.5 VL** models are supported for multimodal reasoning, alongside text-only Qwen2.5 models for prompt generation.

## What's New

- Added support for the Qwen3 VL family (`Qwen3-VL-4B-Thinking`, `Qwen3-VL-8B-Thinking`, etc.).
- Retained compatibility with existing Qwen2.5 VL models.
- Text-only workflows continue to use the Qwen2.5 instruct checkpoints.

## Sample Workflows

- Multimodal workflow example: [`workflow/Qwen2VL.json`](workflow/Qwen2VL.json)
- Text generation workflow example: [`workflow/qwen25.json`](workflow/qwen25.json)

![Qwen VL workflow](workflow/comfy_workflow.png)
![Qwen text workflow](workflow/comfy_workflow2.png)

## Installation

You can install through ComfyUI Manager (search for `Qwen-VL wrapper for ComfyUI`) or manually:

1. Clone the repository:

   ```bash
   git clone https://github.com/alexcong/ComfyUI_QwenVL.git
   ```

2. Change into the project directory:

   ```bash
   cd ComfyUI_QwenVL
   ```

3. Install dependencies (ensure you are inside your ComfyUI virtual environment if you use one):

   ```bash
   pip install -r requirements.txt
   ```

## Supported Nodes

- **Qwen2VL node** – Multimodal generation with Qwen3 VL and Qwen2.5 VL checkpoints. Accepts images or videos as optional inputs alongside text prompts.
- **Qwen2 node** – Text-only generation backed by Qwen2.5 instruct models, with optional quantization for lower memory usage.

Both nodes expose parameters for temperature, maximum token count, quantization (none/4-bit/8-bit), and manual seeding. Set `keep_model_loaded` to `True` to cache models between runs.

## Model Storage

Downloaded models are stored under `ComfyUI/models/LLM/`.
