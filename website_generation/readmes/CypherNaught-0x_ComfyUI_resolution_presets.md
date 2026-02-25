# ComfyUI Resolution Presets

A ComfyUI custom node extension that provides optimized resolution presets for various AI image generation models.

## Features

- Pre-configured resolution presets for multiple AI models
- Support for various aspect ratios
- Two node variants: Basic and Advanced
- Easily extensible architecture
- Automatic validation of model/aspect ratio combinations

## Supported Models

- **Qwen Image** - 7 aspect ratios
- **SDXL** - 9 aspect ratios
- **Flux** - 11 aspect ratios
- **SD 1.5** - 7 aspect ratios

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyUI_resolution_presets.git
   ```

3. Restart ComfyUI

## Nodes

### Resolution Presets

The basic node that outputs resolution presets for your selected model.

**Inputs:**
- `model` - Select the AI model (Qwen Image, SDXL, Flux, SD 1.5)
- `aspect_ratio` - Select the desired aspect ratio

**Outputs:**
- `ratio` (STRING) - The aspect ratio (e.g., "16:9")
- `width` (INT) - Image width in pixels
- `height` (INT) - Image height in pixels
- `model_name` (STRING) - The selected model name

### Resolution Presets (Advanced)

An enhanced version with scaling capabilities.

**Inputs:**
- `model` - Select the AI model
- `aspect_ratio` - Select the desired aspect ratio
- `scale_multiplier` - Scale the resolution (0.25x to 4.0x, default: 1.0)

**Outputs:**
- `ratio` (STRING) - The aspect ratio
- `width` (INT) - Scaled width (rounded to multiple of 8)
- `height` (INT) - Scaled height (rounded to multiple of 8)
- `model_name` (STRING) - The selected model name
- `total_pixels` (INT) - Total pixel count (width × height)

## Usage Example

1. Add the "Resolution Presets" node to your workflow
2. Select your target model (e.g., "Flux")
3. Choose an aspect ratio (e.g., "16:9")
4. Connect the width and height outputs to your image generation node
5. Use the model_name output for reference or routing

## Resolution Presets Reference

### Qwen Image
- 1:1 → 1328×1328
- 16:9 → 1664×928
- 9:16 → 928×1664
- 4:3 → 1472×1140
- 3:4 → 1140×1472
- 3:2 → 1584×1056
- 2:3 → 1056×1584

### SDXL
- 1:1 → 1024×1024
- 16:9 → 1344×768
- 9:16 → 768×1344
- 4:3 → 1152×896
- 3:4 → 896×1152
- 3:2 → 1216×832
- 2:3 → 832×1216
- 21:9 → 1536×640
- 9:21 → 640×1536

### Flux
- 1:1 → 1024×1024
- 16:9 → 1344×768
- 9:16 → 768×1344
- 4:3 → 1152×896
- 3:4 → 896×1152
- 3:2 → 1216×832
- 2:3 → 832×1216
- 21:9 → 1536×640
- 9:21 → 640×1536
- 2:1 → 1408×704
- 1:2 → 704×1408

### SD 1.5
- 1:1 → 512×512
- 16:9 → 682×384
- 9:16 → 384×682
- 4:3 → 608×456
- 3:4 → 456×608
- 3:2 → 624×416
- 2:3 → 416×624

## Extending the Node

To add new models or resolutions, edit `resolution_presets.py`:

```python
RESOLUTION_PRESETS = {
    "Your Model Name": {
        "1:1": (width, height),
        "16:9": (width, height),
        # Add more aspect ratios...
    },
    # Add more models...
}
```

The extension will automatically:
- Add the new model to the dropdown
- Include new aspect ratios in the sorted list
- Validate combinations at runtime

## Best Practices

1. **Model-specific ratios**: Not all aspect ratios are available for all models. The node will show an error with available options if an invalid combination is selected.

2. **Multiple of 8**: The Advanced node automatically rounds dimensions to multiples of 8, which is optimal for most diffusion models.

3. **Scale multiplier**: Use the Advanced node's scale multiplier for quick resolution adjustments while maintaining aspect ratios.

## Technical Details

- **Category**: `image/resolution`
- **Return types**: Strongly typed outputs (STRING, INT)
- **Validation**: Runtime validation with helpful error messages
- **Extensibility**: Simple dictionary-based configuration

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! To add support for new models:

1. Research the optimal resolutions for the model
2. Add the model to `RESOLUTION_PRESETS` dictionary
3. Test the presets
4. Submit a pull request

## Changelog

### Version 1.0.0
- Initial release
- Support for Qwen Image, SDXL, Flux, and SD 1.5
- Basic and Advanced node variants
- Automatic aspect ratio sorting
