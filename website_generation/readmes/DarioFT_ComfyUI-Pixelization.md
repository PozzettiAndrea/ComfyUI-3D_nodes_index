# ComfyUI Pixelization

A ComfyUI node that converts images to pixel art using the neural network from the SIGGRAPH Asia paper ["Make Your Own Sprites: Aliasing-Aware and Cell-Controllable Pixelization"](https://github.com/WuZongWei6/Pixelization).

## Examples

| Original | Pixelized |
|----------|-----------|
| ![](preview-original.png) | ![](preview.png) |

## Installation

### ComfyUI Manager (Recommended)

Search for "Pixelization" in ComfyUI Manager and install.

### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DarioFT/ComfyUI-Pixelization
cd ComfyUI-Pixelization
pip install -r requirements.txt
```

Restart ComfyUI after installation.

### Models

Models are **downloaded automatically** on first use from [HuggingFace](https://huggingface.co/ashleykleynhans/pixelization) to:
```
ComfyUI/models/Pixelization/
├── pixelart_vgg19.pth   (558 MB)
├── 160_net_G_A.pth      (151 MB)
└── alias_net.pth        (35 MB)
```

## Usage

Find the node at: **postprocessing/Effects > Pixelization**

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `pixel_size` | 4 | Size of pixels in output (1-32). Higher = larger pixels |
| `upscale_after` | true | Upscale output to match input resolution using nearest-neighbor |
| `copy_hue` | false | Preserve original image hue (color tone) |
| `copy_sat` | false | Preserve original image saturation (color intensity) |
| `copy_val` | false | Preserve original image value (brightness) |
| `restore_dark` | 15 | Blend dark areas with original (0-100%) |
| `restore_bright` | 1 | Blend bright areas with original (0-100%) |

### Tips

- **Best results**: Use with regular photos or digital artwork, not existing pixel art
- **Color preservation**: Enable `copy_hue` and `copy_sat` to keep original colors while applying pixel art style
- **Larger pixels**: Increase `pixel_size` for a more retro look
- **Input size**: Works best with images 256px+ in size

### Limitations

- Not designed for enhancing existing pixel art (may introduce artifacts)
- Very small images may lack detail for good pixelization

## Credits

- **Original Paper**: [Make Your Own Sprites](https://github.com/WuZongWei6/Pixelization) (SIGGRAPH Asia)
- **Reference Implementation**: https://github.com/arenatemp/pixelization_inference
- **Model Hosting**: https://huggingface.co/ashleykleynhans/pixelization

## License

This node wrapper is provided as-is. The underlying model is released under a non-commercial research license by the original authors.
