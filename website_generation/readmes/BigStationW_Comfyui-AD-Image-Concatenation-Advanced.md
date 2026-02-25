# Comfyui-AD-Image-Concatenation-Advanced

## Intro

This is a modified node of [this script](https://github.com/Eagle-CN/ComfyUI-Addoor/blob/d51659f66696e9a89c7f6adbf159c1f074742b7a/nodes/AddPaddingAdvanced.py#L170).

## Modifications

- **5 image inputs** instead of 2 (image1 is required, images (2->5) are optional)
- **New `output_all_concatenations` parameter**: When enabled, outputs all progressive concatenation steps as a list
 
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/caaedf91-d6df-4c66-a1af-f7687436db45" />

## Installation

Navigate to the **ComfyUI/custom_nodes** folder, [open cmd](https://www.youtube.com/watch?v=bgSSJQolR0E&t=47s) and run:

```bash
git clone https://github.com/BigStationW/Comfyui-AD-Image-Concatenation-Advanced
```

Restart ComfyUI after installation.
