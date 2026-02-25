** This is untested as I have no access to runninghub. It might work, It might not. 

# ComfyUI RunningHub Integration

Custom ComfyUI nodes for integrating RunningHub's AI image and video generation services into your workflows.

This package is a conversion of the [freeqwenimage](https://github.com/rockyandtom/freeqwenimage) web application into ComfyUI custom nodes, allowing you to use RunningHub's AI capabilities directly in ComfyUI.

## Features

- **Text to Image Generation** - Generate images from text prompts
- **Image to Image Transformation** - Transform images using text prompts
- **Image Enhancement** - Enhance image quality and resolution
- **Image to Video Conversion** - Convert static images into videos
- **URL Image Loading** - Load images from URLs into workflows

## Installation

### 1. Install to ComfyUI Custom Nodes

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/marduk191/comfyui_qwen_runninghub.git
cd comfyui_qwen_runninghub
pip install -r requirements.txt
```

### 2. Configure RunningHub API Credentials

You need to obtain API credentials from [RunningHub](https://www.runninghub.cn):

1. Sign up for a RunningHub account
2. Get your `WEBAPP_ID` and `API_KEY` from the dashboard

Set them as environment variables:

```bash
export RUNNINGHUB_WEBAPP_ID="your_webapp_id_here"
export RUNNINGHUB_API_KEY="your_api_key_here"
```

Or on Windows:

```cmd
set RUNNINGHUB_WEBAPP_ID=your_webapp_id_here
set RUNNINGHUB_API_KEY=your_api_key_here
```

Alternatively, you can enter them directly in the node parameters in ComfyUI.

### 3. Restart ComfyUI

Restart ComfyUI to load the new nodes. You should see them under the "RunningHub" category.

## Available Nodes

### RunningHub Text to Image

Generate images from text prompts.

**Inputs:**
- `prompt` (string, required) - Text description of the image to generate
- `negative_prompt` (string, optional) - Things to avoid in the image
- `webapp_id` (string, required) - Your RunningHub webapp ID
- `api_key` (string, required) - Your RunningHub API key
- `timeout` (int, optional) - Maximum wait time in seconds (default: 600)

**Outputs:**
- `IMAGE` - Generated image

### RunningHub Image to Image

Transform an existing image using a text prompt.

**Inputs:**
- `image` (IMAGE, required) - Source image to transform
- `prompt` (string, required) - Description of how to transform the image
- `webapp_id` (string, required) - Your RunningHub webapp ID
- `api_key` (string, required) - Your RunningHub API key
- `timeout` (int, optional) - Maximum wait time in seconds (default: 600)

**Outputs:**
- `IMAGE` - Transformed image

### RunningHub Image Enhancer

Enhance the quality and resolution of an image.

**Inputs:**
- `image` (IMAGE, required) - Image to enhance
- `webapp_id` (string, required) - Your RunningHub webapp ID
- `api_key` (string, required) - Your RunningHub API key
- `timeout` (int, optional) - Maximum wait time in seconds (default: 600)

**Outputs:**
- `IMAGE` - Enhanced image

### RunningHub Image to Video

Convert a static image into a video.

**Inputs:**
- `image` (IMAGE, required) - Source image
- `prompt` (string, optional) - Description for video generation
- `webapp_id` (string, required) - Your RunningHub webapp ID
- `api_key` (string, required) - Your RunningHub API key
- `timeout` (int, optional) - Maximum wait time in seconds (default: 600)

**Outputs:**
- `video_url` (STRING) - URL of the generated video

### RunningHub Load Image

Load an image from a URL.

**Inputs:**
- `url` (string, required) - URL of the image to load

**Outputs:**
- `IMAGE` - Loaded image

## Example Workflows

### Basic Text to Image

1. Add a "RunningHub Text to Image" node
2. Enter your prompt: "A beautiful sunset over mountains"
3. Enter your API credentials
4. Connect to a "Save Image" node
5. Queue the workflow

### Image Enhancement Pipeline

1. Add a "Load Image" node with your source image
2. Connect to "RunningHub Image Enhancer" node
3. Enter your API credentials
4. Connect to "Save Image" node
5. Queue the workflow

### Image to Video

1. Add a "Load Image" node with your source image
2. Connect to "RunningHub Image to Video" node
3. Optionally add a prompt for video generation
4. The output will be a video URL that you can download

## API Information

This integration uses the RunningHub API which provides:

- **Base URL**: `https://www.runninghub.cn`
- **Async Processing**: Tasks are submitted and polled for completion
- **Typical Processing Time**: 30 seconds to 5 minutes depending on the operation
- **Default Timeout**: 10 minutes (600 seconds)

### Node IDs

The RunningHub API uses different node IDs for different operations:
- Text to Image: Node ID 1
- Image Enhancer: Node ID 2
- Image to Image: Node ID 3
- Image to Video: Node ID 4

## Troubleshooting

### "RunningHub credentials are required" Error

Make sure you've set the environment variables or entered the credentials in the node parameters:
```bash
export RUNNINGHUB_WEBAPP_ID="your_webapp_id"
export RUNNINGHUB_API_KEY="your_api_key"
```

### Timeout Errors

If tasks are timing out, try increasing the `timeout` parameter to 900 or 1200 seconds (15-20 minutes).

### Task Failed Errors

Check the console output for detailed error messages from the RunningHub API. Common issues:
- Invalid API credentials
- Insufficient credits in your RunningHub account
- Invalid image URLs or formats

### Import Errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## Source Project

This ComfyUI integration is based on the [freeqwenimage](https://github.com/rockyandtom/freeqwenimage) web application, which provides a Next.js-based interface to RunningHub's AI services.

## License

MIT License

## Credits

- Original web app: [freeqwenimage](https://github.com/rockyandtom/freeqwenimage)
- API Provider: [RunningHub](https://www.runninghub.cn)
- ComfyUI: [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Support

For issues or questions:
- Open an issue on GitHub
- Check RunningHub documentation at https://www.runninghub.cn
- Refer to the original freeqwenimage project for API usage examples
