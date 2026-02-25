# ComfyUI-JM-Gemini-API

Custom nodes for ComfyUI that generate images and videos using Google's Gemini API, supporting text-to-image, image-to-image, text-to-video, and image-to-video generation.

English | [简体中文](README_CN.md)

## Features

### Image Generation
- Support for multiple Gemini image models:
  - `gemini-3-pro-image-preview` (default, with 2K resolution)
  - `gemini-2.5-flash-image`
- Text-to-image generation
- Image-to-image generation (single or multiple input images)
- Image editing mode (single image input)
- Configurable aspect ratios (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
- Resolution control (1K, 2K, 4K) - only for gemini-3-pro-image-preview
- Support up to 10 input images
- Automatic image saving to ComfyUI output directory

### Video Generation
- Support for Gemini Veo video models:
  - `veo-3.1-generate-preview` (default)
  - `veo-3.1-fast-generate-preview`
  - `veo-3.0-generate-001`
  - `veo-3.0-fast-generate-001`
- Text-to-video generation
- Image-to-video generation (animate a single image)
- First-last frame interpolation (Veo 3.1 only)
- Negative prompt support
- Configurable aspect ratios (16:9, 9:16)
- Resolution control (720p, 1080p)
- Duration control (4, 6, 8 seconds)
- Automatic video saving to ComfyUI output directory

**Important Limitations:**
- **1080p resolution**: Only supports 8-second duration for Veo 3.1 models
- **First-last frame interpolation**: Only available for Veo 3.1 models with 8-second duration

### Watermark Removal
- Automatically detects and removes Gemini watermarks from generated images
- Supports both 48×48 and 96×96 watermark sizes
- Uses reverse alpha blending algorithm for clean removal
- Simple one-click operation - just pass the image through the node

## Installation

1. Clone or download this repository to your ComfyUI custom_nodes directory:

```bash
cd custom_nodes
git clone https://github.com/synthetai/ComfyUI-JM-Gemini-API.git
```

2. Install required dependencies:

```bash
cd ComfyUI-JM-Gemini-API
pip install -r requirements.txt
```

3. Restart ComfyUI

## Requirements

- Python 3.8+
- ComfyUI
- google-genai >= 0.2.0
- Pillow >= 10.0.0
- torch
- torchvision
- numpy
- httpx[socks] (for proxy support)

## Proxy Configuration (Optional)

If you need to use a proxy to access the Gemini API (common for users in China), you can set environment variables:

### HTTP/HTTPS Proxy

```bash
export HTTP_PROXY="http://your-proxy:port"
export HTTPS_PROXY="http://your-proxy:port"
```

### SOCKS5 Proxy

```bash
export HTTP_PROXY="socks5://your-proxy:port"
export HTTPS_PROXY="socks5://your-proxy:port"
```

Or set them before starting ComfyUI:

```bash
HTTP_PROXY="socks5://127.0.0.1:1080" HTTPS_PROXY="socks5://127.0.0.1:1080" python main.py
```

## Usage

### Getting Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for use in the node

### Node Parameters

#### Required Inputs:

- **gemini_api_key**: Your Gemini API key (string)
- **prompt**: Text prompt describing the image you want to generate (multiline text)
- **model**: Choose between:
  - `gemini-3-pro-image-preview` (default, supports 1K/2K/4K resolution)
  - `gemini-2.5-flash-image` (faster, aspect ratio only)
- **aspect_ratio**: Image aspect ratio (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
- **resolution**: Image resolution (1K, 2K, 4K)
  - Note: Only effective for `gemini-3-pro-image-preview` model
  - Default: 2K

#### Optional Inputs:

- **image1 ~ image10**: Up to 10 optional image inputs for image-to-image generation
  - Connect output from Load Image node
  - Can be left empty for text-to-image generation

#### Outputs:

- **image**: Generated image (ComfyUI IMAGE tensor format)
  - Can be connected to Preview Image or Save Image nodes
  - Automatically saved to ComfyUI output directory

### Usage Examples

#### 1. Text-to-Image Generation

1. Add "JM Gemini Image Generator" node to your workflow
2. Enter your Gemini API key
3. Write your prompt
4. Select model and aspect ratio
5. Leave all image inputs empty
6. Connect output to Preview Image node
7. Run the workflow

#### 2. Image Editing (Single Image)

1. Add Load Image node and load your image
2. Add "JM Gemini Image Generator" node
3. Connect Load Image output to image1 input
4. Enter editing instructions in prompt (e.g., "Add a sunset background")
5. Configure model and parameters
6. Run the workflow

#### 3. Image-to-Image (Multiple Images)

1. Add multiple Load Image nodes
2. Connect them to image1, image2, etc.
3. Enter a prompt describing how to combine/transform the images
4. Run the workflow

## Model Differences

### gemini-3-pro-image-preview
- Supports resolution parameter (1K, 2K, 4K)
- Default resolution: 2K
- Supports single image editing
- Higher quality output

### gemini-2.5-flash-image
- Faster generation
- Uses aspect ratio only (no resolution parameter)
- Good for quick iterations

## Troubleshooting

### Common Issues

1. **"Gemini API key is required"**
   - Make sure you've entered a valid API key

2. **"No images were generated"**
   - Check your prompt is clear and descriptive
   - Try a different aspect ratio or resolution
   - Verify your API key is valid and has sufficient quota

3. **"Failed to generate image"**
   - Check your internet connection
   - Verify API key permissions
   - Check Gemini API service status

4. **Image quality issues**
   - For gemini-3-pro-image-preview, try using different resolutions (1K, 2K, or 4K)
   - Make your prompt more detailed and specific

## Output Directory

Generated images are automatically saved to:
- `ComfyUI/output/` directory
- Filename format: `{model}_{mode}_{timestamp}.png`
  - Example: `gemini3pro_text2img_1234567890.png`

## License

MIT License

## Credits

Developed by JM

Based on Google's Gemini API

## Support

For issues and feature requests, please visit the [GitHub repository](https://github.com/yourusername/ComfyUI-JM-Gemini-API/issues)

## Video Node Usage

### Node: JM Gemini Video Generator

#### Required Inputs:
- **gemini_api_key**: Your Gemini API key (string, encrypted input)
- **prompt**: Text prompt describing the video you want to generate (multiline text)

#### Optional Inputs:
- **negative_prompt**: Describe what you don't want in the video (multiline text)
- **model**: Choose video model:
  - `veo-3.1-generate-preview` (default, highest quality)
  - `veo-3.1-fast-generate-preview` (faster generation)
  - `veo-3.0-generate-001` (stable version)
  - `veo-3.0-fast-generate-001` (stable + fast)
- **aspect_ratio**: Video aspect ratio (16:9 or 9:16, default: 16:9)
- **resolution**: Video resolution (720p or 1080p, default: 720p)
- **duration**: Video duration in seconds (4, 6, or 8, default: 8)
- **first_image**: First frame image (optional, for image-to-video or interpolation)
- **last_image**: Last frame image (optional, only for Veo 3.1 interpolation)

#### Output:
- **video_path**: Path to the generated video file (STRING)

### Video Generation Modes

#### 1. Text-to-Video
1. Add "JM Gemini Video Generator" node
2. Enter API key and prompt
3. Leave both image inputs empty
4. Configure model and parameters
5. Run workflow - video will be saved to output directory

#### 2. Image-to-Video
1. Add Load Image node and load your image
2. Connect it to **first_image** input
3. Enter prompt describing the motion/animation
4. Run workflow

#### 3. First-Last Frame Interpolation (Veo 3.1 only)
1. Add two Load Image nodes
2. Connect first image to **first_image** input
3. Connect last image to **last_image** input
4. Select a Veo 3.1 model (veo-3.1-generate-preview or veo-3.1-fast-generate-preview)
5. **Set duration to 8 seconds** (required for interpolation mode)
6. Enter prompt describing the transition
7. Run workflow - the model will generate smooth interpolation between frames

**Important Notes**:
- Video generation can take several minutes. The node will poll the API every 10 seconds with a 20-minute timeout.
- **1080p resolution** is only supported with **8-second duration** for Veo 3.1 models
- **First-last frame interpolation** requires **Veo 3.1 models** and **8-second duration only**

## Watermark Remover Node Usage

### Node: JM Gemini Watermark Remover

This node removes the Gemini watermark that appears on generated images.

#### Input:
- **image**: The Gemini-generated image with watermark (IMAGE tensor)

#### Output:
- **image**: The same image with watermark removed (IMAGE tensor)

#### Usage:

1. Add "JM Gemini Watermark Remover" node to your workflow
2. Connect the output from "JM Gemini Image Generator" (or any Load Image node with a Gemini image) to the image input
3. Connect the output to Preview Image or Save Image node
4. Run the workflow

The node will:
- Automatically detect the watermark size (48×48 or 96×96) based on image dimensions
- Calculate the watermark position (bottom-right corner)
- Remove the watermark using reverse alpha blending algorithm
- Save the cleaned image to the ComfyUI output directory

**How it works:**
- Gemini adds watermarks to images larger than 512×512 pixels
- Images larger than 1024×1024 use a 96×96 watermark
- Smaller images use a 48×48 watermark
- The node uses pre-calculated alpha maps from background captures to reverse the watermark blending

## Changelog

### Version 1.2.0
- Added JM Gemini Watermark Remover node
- Automatically removes Gemini watermarks from generated images
- Supports both 48×48 and 96×96 watermark sizes
- Uses reverse alpha blending algorithm for clean removal

### Version 1.1.0
- Added video generation support with JM Gemini Video Generator node
- Support for Veo 3.1 and Veo 3.0 models
- Text-to-video generation
- Image-to-video animation
- First-last frame interpolation (Veo 3.1 only)
- Refactored code structure with separate node files and shared utilities

### Version 1.0.0
- Initial release
- Support for gemini-3-pro-image-preview and gemini-2.5-flash-image
- Text-to-image generation
- Image-to-image generation (up to 10 images)
- Configurable aspect ratios and resolutions
