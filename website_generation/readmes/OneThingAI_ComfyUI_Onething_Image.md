# ComfyUI OneThing AI Node

A custom node for ComfyUI that integrates with OneThing AI's image generation API.

## Features
- Generate images using OneThing AI's models
- Control image dimensions (512x512 to 2048x2048)
- Multiple images per request (1-10)
- Built-in retry mechanism for API stability
- Configurable timeout settings
- Reference image support for guided image generation

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/OneThingAI/ComfyUI_Onething_Image.git
```

2. Install required dependencies:
```bash
pip install Pillow requests
```

## Usage

1. Get your API key from OneThing AI
2. In ComfyUI, find the "OneThingAI Image Generator" node
3. Configure the parameters:
   - API Key: Your OneThing AI API key
   - Prompt: Text description of the image you want to generate
   - Model: Select the model (default: gpt4o)
   - Number of Images: How many images to generate (1-10)
   - Width/Height: Image dimensions (512-2048, step 64)
   - Retries: Number of retry attempts (0-5)
   - Timeout: Request timeout in seconds (5-100)
   - Reference Image (optional): Input image to guide the generation
   - Reference Image Weight (optional): Control how much the reference image influences the result (0.0-1.0)

## Requirements
- Python 3.x
- ComfyUI
- Pillow (PIL)
- requests


