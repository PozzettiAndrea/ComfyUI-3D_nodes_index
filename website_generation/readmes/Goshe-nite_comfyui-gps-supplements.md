# comfyui-gps-supplements
Nodes to make [ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver) and [rgthree-comfy](https://github.com/rgthree/rgthree-comfy) more compatible. Allowing Power Lora Loader node to be used with Image Saver node. Also adding nodes to extract Image Saver compatible strings to simplify workflows.

## Nodes
**Lora to String**: connect Power Lora Loader (rgthree) as input to get lora strings in the format: \<lora:strength\>

**Lora Prompt Concatenation**: connect Power Lora Loader (rgthree) and positive prompt string as input to get formatted positive prompt compatible with Image Saver (comfyui-image-saver).

**Model to String**: connect checkpoint loader as input to get checkpoint name as string output.

**KSampler to Image Saver**: connect to KSampler or nodes alike to extract data compatible with Image Saver (comfyui-image-saver), data includes seed, steps, cfg, sampler name, scheduler, denoise. Can retrieve data even if KSampler takes input from other nodes. Input boxes are provided as fallback options if other nodes missing some options are connected as input. 

## Installation
1. Installation with ComfyUI Manager:
  - In ComfyUI Manager, open custom nodes manager
  - Search for 'GPS' Supplements for ComfyUI'
  - Install the custom nodes
  - Restart ComfyUI

2. Installation with git:
  Open a terminal from ComfyUI folder, in the terminal, do:
  - `cd custom_nodes`
  - `git clone https://github.com/Goshe-nite/comfyui-gps-supplements.git`
  - Restart ComfyUI

## Example Workflow
Example workflow provided in examples folder.
![example workflow](https://github.com/user-attachments/assets/95cee8e1-f8d5-4e07-942d-384f23dffe83)

## Credit
- [kijai\ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes): for the Widget To String node which this project's nodes heavily derived from.
- [rgthree\rgthree-comfy](https://github.com/rgthree/rgthree-comfy): for the wonderful Power Lora Loader node.
- [ alexopus\ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver.git): for the fantastic Civitai compatible Image Saver.
