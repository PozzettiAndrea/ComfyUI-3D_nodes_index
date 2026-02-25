# ComfyUI-QwenCameraSelector

**Custom node for ComfyUI** to generate Qwen-Multiple-Angle camera prompts.

You are like me and you are tired to copy/paste, copy/paste, copy/paste, copy/paste, copy/paste, copy/paste,...?
I got you covered!

This node allows you to select **azimuth, elevation, and distance** for the camera, and outputs a properly formatted `<sks>` prompt. It is designed for use with the [Qwen Multiple Angles LoRA model](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA).

---

## Installation

1. Clone or download this repository:

```
cd Comfyui/custom_nodes
git clone https://github.com/TheMadDoctor007/ComfyUI-QwenCameraSelector.git

Launch or restart ComfyUI. The node will appear under: Camera > Qwen

Usage

Inputs:
azimuth – Horizontal rotation (0° front, 45° front-right, …, 315° front-left)
elevation – Vertical angle (-30° low-angle, 0° eye-level, 30° elevated, 60° high-angle)
distance – Camera distance (close, medium, wide)

Outputs:
prompt – Full prompt string for the model
prompt_preview – Same string for connecting to a Text Display node for preview

Note: The node automatically generates the correct Qwen-Multiple-Angle prompt; no additional descriptors are required.

Version
1.0.0 (first node ever)
