# ComfyUI Razv WaveSpeed Nodes

Custom ComfyUI nodes for integrating WaveSpeed AI API for image and video generation.

## Features

- Multiple AI model integrations (Qwen, Google Nano Banana, etc.)
- Image generation, editing, and upscaling capabilities
- Video generation support
- Sync and async processing modes
- Automatic retry logic for network issues

## Installation

### Option 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "razv-wavespeed"
3. Click Install

### Option 2: Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/razvanmatei-sf/razv-wavespeed.git
cd razv-wavespeed/comfyui-razv-wavespeed-custom
pip install -r requirements.txt
```

## Configuration

1. Copy `config.ini.tmp` to `config.ini`
2. Add your WaveSpeed API key to `config.ini`:
```ini
[api]
key = your_wavespeed_api_key_here
```

Or provide the API key directly in the WaveSpeedAI Client node.

## Available Nodes

### Core Nodes
- **WaveSpeedAI Client**: Connection node for API authentication
- **WaveSpeedAI Upload Image**: Upload images and get URLs for processing

### Generation Nodes
- **Qwen Image Text to Image**: Generate images from text prompts
- **Qwen Image Edit**: Edit existing images with prompts
- **Google Nano Banana Edit**: Advanced image editing
- **Image Upscaler**: Upscale images with AI

### Workflow Pattern

```
Load Image → WaveSpeedAI Upload Image → WaveSpeedAI [Processing Node] → Preview Image
            ↓                           ↑
            WaveSpeedAI Client ←←←←←←←←←
```

## Node Development

To add new WaveSpeed API models:
1. Create a new `.py` file in `comfyui-razv-wavespeed-custom/py/`
2. Follow the template structure in existing nodes
3. Register the node with `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`

## Requirements

- ComfyUI
- Python 3.8+
- See `requirements.txt` for Python dependencies

## Troubleshooting

- **SSL Errors**: The client includes automatic retry logic with progressive backoff
- **Missing Nodes**: Restart ComfyUI after installation
- **API Key Issues**: Verify key in config.ini or node settings

## License

MIT