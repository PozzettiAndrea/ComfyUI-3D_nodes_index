# ComfyUI-Koala

A collection of custom nodes for ComfyUI focused on aspect ratio management and other utilities.

## Installation

### Manual Installation
1. Clone this repository into your `ComfyUI/custom_nodes` folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/cloudkoala/comfyui-koala.git
```
2. Restart ComfyUI

### ComfyUI Manager
Coming soon!

## Nodes

### Koala Aspect Ratio Empty Latent
Creates empty latents that match predefined aspect ratios from training hyperparameters.

**Inputs:**
- `batch_size`: Number of latents to create (1-64)
- `image` (optional): Image to extract dimensions from
- `width` (optional): Manual width input
- `height` (optional): Manual height input

**Outputs:**
- `latent`: Empty latent tensor with matched dimensions
- `width`: The matched width value
- `height`: The matched height value
- `aspect_ratio`: The matched aspect ratio value
- `info`: String showing input → matched dimensions

**Usage:**
The node will automatically find the closest matching aspect ratio from a predefined set of training-optimized ratios, ensuring your generations use optimal dimensions.

## Supported Aspect Ratios
The node supports 40 different aspect ratios ranging from 0.25 (512×2048) to 4.0 (2048×512), including common ratios like 1:1, 16:9, 9:16, etc.

## Credits
Created by Cloud Koala

## License
MIT License