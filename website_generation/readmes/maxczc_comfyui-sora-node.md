# Sora Custom Node for ComfyUI

This repository contains a comprehensive set of ComfyUI custom nodes for interacting
with a Sora-compatible REST API. The nodes support the full range of Sora capabilities:

- **Text-to-Video**: Generate videos from text prompts
- **Image-to-Video**: Generate videos from images
- **Video-to-Video**: Edit, extend, or transform existing videos

All nodes use only Python's standard library (with optional PIL/numpy support for image processing).

## Installation

1. Clone or copy this folder into the `ComfyUI/custom_nodes/` directory:

   ```bash
   cd ComfyUI/custom_nodes
   git clone <this repo> sora
   ```

   **重要**: 确保文件夹结构如下：

   ```
   ComfyUI/custom_nodes/sora/
   ├── __init__.py          ← 必需！
   ├── sora_node.py         ← 必需！
   └── ...
   ```

2. **完全重启 ComfyUI**（关闭所有进程，然后重新启动）

   - 不是刷新浏览器页面
   - 需要完全关闭并重新启动 ComfyUI 服务器

3. **Optional dependencies** (for better image handling):

   - `Pillow` (PIL): For processing PIL Image objects
   - `numpy`: For processing numpy array inputs

   These are optional - the nodes will work with file paths and base64 strings without them.

### Verification

After installation, verify the nodes are loaded:

```bash
cd ComfyUI/custom_nodes/sora
python test_comfyui_load.py
```

If nodes don't appear in ComfyUI, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for help.

## Available Nodes

### 1. Sora Text-To-Video

Generates videos from text prompts.

**Inputs:**

- `prompt` (required): Text description of the video
- `negative_prompt`: What to avoid in the video
- `duration_seconds`: Video length (default: 5.0)
- `aspect_ratio`: Video aspect ratio (default: "16:9")
- `fps`: Frames per second (default: 24)
- `guidance_scale`: Generation guidance (default: 7.5)
- `seed`: Random seed for reproducibility
- And more...

### 2. Sora Image-To-Video

Generates videos from images. Accepts ComfyUI image inputs (PIL Image, numpy arrays, or file paths).

**Inputs:**

- `image` (required): Image input (from ComfyUI image nodes)
- `prompt` (required): Text description for video generation
- All the same optional parameters as Text-To-Video

**Image Input Support:**

- PIL Image objects
- Numpy arrays (various shapes supported)
- File paths (PNG, JPG, WebP)
- Base64 encoded strings

### 3. Sora Video-To-Video

Edits or extends existing videos. Supports multiple operations:

- **extend**: Extend video duration
- **edit**: Edit video content based on prompt
- **inpaint**: Fill masked regions
- **style_transfer**: Apply style to video

**Inputs:**

- `video` (required): Video file path or base64 string
- `prompt` (required): Description of desired changes
- `operation`: Type of video operation (default: "extend")
- `extension_seconds`: For extend operation (default: 5.0)
- All the same optional parameters as other nodes

## Configuration

All nodes look for an API key using the following priority:

1. The `api_key` input field on the node.
2. The `SORA_API_KEY` environment variable.
3. The `OPENAI_API_KEY` environment variable.

You can also configure:

- `base_url`: defaults to `https://api.openai.com/v1/sora`.
- `endpoint`: defaults to `/videos`, change it if your backend uses another path.
- `download_path`: optional local directory or file path for saving the video.
- `wait_for_result`: Whether to poll until completion (default: True)
- `poll_interval`: Seconds between status checks (default: 3.0)
- `max_wait_seconds`: Maximum wait time (default: 120.0)

## Outputs

All nodes return three strings:

1. **Job ID**: Unique identifier for the generation job
2. **Status**: Current status (`submitted`, `processing`, `succeeded`, `failed`, etc.)
3. **Result JSON**: Contains the raw API response and downloaded file path (if any)

## Local Testing

You can test the custom node locally without running ComfyUI:

### 1. Basic Functionality Test

Run the test script to verify node functionality:

```bash
# Run basic tests (no API calls)
python test_sora_node.py

# Run full unittest suite
python test_sora_node.py --unittest

# Test with real API (requires API key)
python test_sora_node.py --test-client --api-key YOUR_KEY
```

### 2. Test in ComfyUI

1. Copy this folder to `ComfyUI/custom_nodes/sora/`
2. Start ComfyUI
3. The node should appear in the node menu under "Sora" category
4. You can test it directly in the ComfyUI interface

### 3. Mock Testing

The test script uses mocks to test API interactions without making real network calls. This is useful for:

- Testing error handling
- Testing response parsing
- Validating node logic

## Features

### Full Sora Capability Support

- ✅ Text-to-Video generation
- ✅ Image-to-Video generation
- ✅ Video-to-Video editing and extension
- ✅ Multiple video operations (extend, edit, inpaint, style transfer)

### ComfyUI Integration

- Seamless integration with ComfyUI image nodes
- Supports all ComfyUI image formats (PIL, numpy, file paths)
- Automatic format conversion and handling

### Robust Error Handling

- Clear error messages for API failures
- Timeout protection
- Automatic retry logic for polling

### Flexible Configuration

- Environment variable support for API keys
- Customizable endpoints and base URLs
- Optional result downloading
- Webhook support for async operations

## Notes

- Nodes poll the job until completion when `wait_for_result` is enabled.
- If `download_path` is a folder, videos are saved as `<job_id>.mp4`.
- The nodes automatically search for video URLs in various response formats:
  - `result_url` or `video_url` (direct)
  - `outputs[0].url` or `outputs[0].download_url` (nested)
  - `videos` array
- Image inputs are automatically converted to the format required by the API.
- Video inputs support file paths and base64 encoded strings.
