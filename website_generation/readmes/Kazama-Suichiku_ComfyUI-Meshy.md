# ComfyUI-Meshy

**ComfyUI-Meshy** is a 3D generation extension based on [Meshy AI](https://www.meshy.ai/) API. It provides Text-to-3D and Image-to-3D capabilities within ComfyUI, allowing you to generate 3D models directly from text prompts or images.

## Features

- **Text to 3D (Preview)**: Generate preview 3D models from text descriptions
- **Text to 3D (Refine)**: Refine preview models with textures and details
- **Image to 3D**: Convert images into 3D models
- **Multiple AI Models**: Support for Meshy-4, Meshy-5, and Meshy-6
- **Customizable Output**: Control topology (triangle/quad), polygon count, and PBR settings
- **Multiple Art Styles**: realistic, cartoon, low-poly, sculpture, pbr

## Installation

### Method 1: Manual Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-Meshy.git
```

2. Install dependencies:

```bash
pip install -r ComfyUI-Meshy/requirements.txt
```

3. Restart ComfyUI

### Method 2: ComfyUI-Manager

Search for "ComfyUI-Meshy" in ComfyUI-Manager and click Install.

## Getting Started

### 1. Get Your API Key

1. Visit [Meshy AI](https://www.meshy.ai/)
2. Create an account or sign in
3. Go to API settings and generate an API key

### 2. Basic Usage

1. Add **"Meshy - API Key"** node and enter your API key
2. Add **"Meshy - Text to 3D (Preview)"** or **"Meshy - Image to 3D"** node
3. Connect the API key to the generation node
4. Configure your parameters and run!

## Nodes

### Meshy - API Key
Input node for your Meshy API key. All generation nodes require this connection.

### Meshy - Text to 3D (Preview)
Generate a preview 3D model from text description.

**Parameters:**
- `prompt`: Text description of the 3D model
- `art_style`: Visual style (realistic, cartoon, low-poly, sculpture, pbr)
- `ai_model`: Model version (meshy-4, meshy-5, meshy-6)
- `topology`: Mesh topology (triangle, quad)
- `target_polycount`: Target polygon count (100-300,000)
- `seed`: Random seed (-1 for random)
- `enable_pbr`: Enable PBR textures

### Meshy - Text to 3D (Refine)
Refine a preview model with textures.

**Parameters:**
- `preview_task_id`: Task ID from the preview stage
- `texture_prompt`: Additional prompt for texturing
- `enable_pbr`: Enable PBR textures

### Meshy - Image to 3D
Generate a 3D model from an input image.

**Parameters:**
- `image`: Input image
- `ai_model`: Model version
- `topology`: Mesh topology
- `target_polycount`: Target polygon count
- `enable_pbr`: Enable PBR textures
- `should_remesh`: Enable remeshing
- `should_texture`: Generate textures for the model

## Output

Generated models are saved to `ComfyUI/output/YYYY-MM-DD_HH-MM-SS/` with:
- 3D model files (GLB, FBX, OBJ, USDZ)
- Texture maps (base color, normal, metallic, roughness)
- Thumbnail image

## Outputs from Nodes

| Output | Description |
|--------|-------------|
| thumbnail | Preview thumbnail of the generated model |
| base_color | Base color texture map |
| normal | Normal map |
| metallic_roughness | Metallic/Roughness map |
| model_path | File path to the downloaded 3D model |

## API Pricing

Refer to [Meshy Pricing](https://www.meshy.ai/pricing) for current API costs:
- Text to 3D Preview: ~20 credits (Meshy-6) / ~5 credits (others)
- Text to 3D Refine: Additional credits
- Image to 3D: Varies by model

## Requirements

- ComfyUI
- Python 3.8+
- Valid Meshy API key

## Dependencies

- numpy
- Pillow
- requests
- torch
- pyhocon

## License

GPL-3.0 License

## Links

- [Meshy AI](https://www.meshy.ai/)
- [Meshy API Documentation](https://docs.meshy.ai/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Troubleshooting

### API Key Issues
- Ensure your API key is valid and has sufficient credits
- Check that the key is entered correctly without extra spaces

### Generation Failures
- Check your internet connection
- Verify your prompt doesn't contain restricted content
- Ensure you have sufficient API credits

### Model Not Downloading
- Check the output directory permissions
- Ensure sufficient disk space

