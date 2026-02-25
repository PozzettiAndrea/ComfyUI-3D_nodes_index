# ComfyPoe

Custom ComfyUI nodes for image generation and editing via [Poe's](https://poe.com) OpenAI-compatible API.

## Features

- **PoeImageEdit** - Edit images with text prompts (img2img)
- **PoeImageGenerate** - Generate images from text prompts
- **PoeImageVariation** - Create variations of existing images
- **PoeMultiImageEdit** - Edit using multiple reference images

Supports multiple image models through Poe:
- GPT-Image-1
- DALL-E-3
- Imagen-4
- FLUX-pro-1.1 / FLUX-schnell
- Playground-v3
- Recraft-V3
- Ideogram-v2
- SD3.5-Large / SD3.5-Large-Turbo

## Installation

### Via ComfyUI Manager (Recommended)

Search for "ComfyPoe" in ComfyUI Manager and click Install.

### Manual Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/mrf/ComfyPoe.git
   ```

2. Restart ComfyUI. Dependencies (`openai`, `requests`) will be installed automatically on first load.

## Usage

1. Get your API key from https://poe.com/api_key
2. Add a Poe node to your workflow (found under **api/poe** category)
3. Enter your API key and configure settings
4. Connect to other ComfyUI nodes

### Node Parameters

| Parameter | Description |
|-----------|-------------|
| `image` | Input image tensor (for edit/variation nodes) |
| `prompt` | Text description of desired output |
| `api_key` | Your Poe API key |
| `model` | Image model to use |
| `aspect` | Aspect ratio (1:1, 3:2, 2:3, 4:3, 16:9, etc.) |
| `quality` | Output quality (low, medium, high) |
| `seed` | Random seed (-1 for random) |

### Example Workflows

**Basic Image Edit:**
```
LoadImage → PoeImageEdit → PreviewImage
```

**Text to Image:**
```
PoeImageGenerate → PreviewImage
```

**Image Variation with Style:**
```
LoadImage → PoeImageVariation → PreviewImage
```

## Outputs

Each node returns:
- `image` - Output image tensor (compatible with all ComfyUI image nodes)
- `raw_response` - Full API response text (useful for debugging)

## Security Note

**Do not share workflow files (.json) that contain your API key.** The key is stored in plain text within the workflow. Remove it before sharing or use environment variables in your setup.

## Requirements

- ComfyUI
- Python 3.10+
- Poe API subscription with API access

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
