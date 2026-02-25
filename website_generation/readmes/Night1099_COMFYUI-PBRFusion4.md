[![HuggingFace](https://img.shields.io/badge/🤗%20HuggingFace-Weights-blue)](https://huggingface.co/NightRaven109/PBRFusion4)

![teaser](assets/1.jpg)
# COMFYUI-PBRFusion4

ComfyUI custom nodes for generating depth maps and normal maps from images using the PBRFusion4 diffusion model. Designed for PBR texture workflows.

## Installation

Clone this repo into your ComfyUI `custom_nodes` folder:

```
cd ComfyUI/custom_nodes
git clone https://github.com/NightRaven109/COMFYUI-PBRFusion4.git
```

The model (`PBRFusion4.safetensors`, ~4.1 GB) is **automatically downloaded** on first use from HuggingFace and saved to `ComfyUI/models/pbrfusion4/`. No manual download required.

## Nodes

### PBRFusion4 Simple Depth & Normal Generator

Generates a depth map and normal map from an input image.

**Inputs:**
- `image` - Input image
- `intensity_blend` - Blend factor for mixing original image intensity into normal map generation (0.0 - 1.0)
- `opengl_normal` - When enabled, outputs OpenGL-format normals (Y up). When disabled, outputs DirectX-format (Y down)
- `optimize` - Limit processing resolution to 1024px max side for faster inference, then resize back to original
- `bilateral_d` / `bilateral_sigma_color` / `bilateral_sigma_space` - Bilateral filter settings for depth smoothing

**Outputs:**
- `depth` - Raw depth map
- `depth_filtered` - Bilateral-filtered depth map
- `normal` - Normal map generated from filtered depth
- `intensity` - Extracted intensity map from input

### Utility Nodes

- **Normal Map Flip Y** - Convert between OpenGL and DirectX normal map formats
- **Black Threshold Filter** - Set near-black pixels to pure black (clean up artifacts)
- **Smart Upscale Calculator** - Calculate target dimensions and scale factor for 1k/2k/4k output
- **Clamp Resolution** - Cap dimensions to a max size while preserving aspect ratio
- **Conditional Upscale** - Upscale using a model with a bypass toggle

## Requirements

- diffusers

## License

This model is licensed under the https://www.apache.org/licenses/LICENSE-2.0.
