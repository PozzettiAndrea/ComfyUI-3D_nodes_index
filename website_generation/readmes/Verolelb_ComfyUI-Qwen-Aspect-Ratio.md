# Qwen Aspect Ratio Selector (Latent) - ComfyUI Node

A simple ComfyUI custom node to select aspect ratios optimized for Qwen Image, calculate the correct resolution, and output a ready-to-use empty latent.

## Features
- 24 predefined aspect ratios (portrait, landscape, cinematic, ultrawide…)
- Native Qwen resolution (1328 px longest side)
- Scale output size by percentage
- Outputs both width/height and a ready-to-use `LATENT`

## Installation
### Manual
1. Copy `qwen_aspect_ratio_latent.py` into your `ComfyUI/custom_nodes` folder.
2. Restart ComfyUI.
3. Look for **"Qwen Aspect Ratio Selector (Latent)"** in the **Qwen Utils** category.

### With ComfyUI Manager
1. Open ComfyUI.
2. Go to **Manager** → **Install Custom Node**.
3. Paste this repo URL:

https://github.com/Verolelb/ComfyUI-Qwen-Aspect-Ratio

4. Install and restart.

## Parameters
- **aspect_ratio** : Choose from 1:1, 16:9, 21:9, etc.
- **scale_percent** : Increase or decrease the resolution while keeping the ratio.
- **batch_size** : Number of images in the latent.

## License
MIT License
# No extra dependencies required
