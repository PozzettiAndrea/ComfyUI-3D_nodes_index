# ComfyUI Image Tools

A ComfyUI custom node for automatically fitting images to standard model dimensions.

## Installation

Clone or copy this folder into your ComfyUI `custom_nodes` directory:

```
ComfyUI/
  custom_nodes/
    comfyui_imgtools/
      __init__.py
      nodes.py
```

Restart ComfyUI to load the node.

## Nodes

### Image Dimension Fitter

**Category:** image/transform

Automatically crops images to the closest standard dimensions for your target model. Uses center cropping to preserve the most important part of the image.

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| image | IMAGE | Input image to process |
| model | dropdown | Target model: SD, Flux, or Z-Turbo |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| image | IMAGE | Center-cropped image at target dimensions |
| target_width | INT | Width of the output image |
| target_height | INT | Height of the output image |

#### Supported Dimensions

**SD (Stable Diffusion 1.5)**
- 512x512, 640x512, 512x640, 704x512, 512x704, 768x512, 512x768

**Flux**
- 1024x1024, 1152x896, 896x1152, 1216x832, 832x1216
- 1344x768, 768x1344, 1536x640, 640x1536, 1920x1080, 1080x1920

**Z-Turbo**
- 1024x1024, 1152x896, 896x1152, 1216x832, 832x1216
- 1344x768, 768x1344, 1536x640, 640x1536

## How It Works

1. Takes the input image dimensions and calculates its aspect ratio
2. Finds the closest matching standard dimension for the selected model
3. Center crops the image to those dimensions
4. Returns the cropped image along with the target dimensions

If the input image is smaller than the target dimensions, it is returned unchanged.

## Example Workflow

```
Load Image -> Image Dimension Fitter (model=Flux) -> VAE Encode -> KSampler -> ...
```

The `target_width` and `target_height` outputs can be connected to Empty Latent Image or other nodes that need dimension information.

## License

MIT
