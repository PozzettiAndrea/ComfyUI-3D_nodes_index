# ComfyUI-SendToDiscord

ComfyUI-SendToDiscord is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that simplifies sending preview images to Discord via webhooks. It supports both single-image uploads and batch mode with intelligent fallback, automatic compression, and workflow preservation, making it an efficient and robust tool for sharing your generated images directly with your Discord server.

![Node Preview](examples/workflow.png "Node Example")
- Workflow included in the image

## Features
- **Smart Image Delivery**: Send individual or batches of images with intelligent fallback (individual sending if batch fails)
- **Automatic Compression**: WebP compression with configurable quality to optimize file sizes
- **Workflow Preservation**: Automatically preserves ComfyUI workflow JSON when compressing images
- **Metadata Support**: Includes prompts and additional PNG information in saved images
- **Advanced Configuration**: Extensive configuration options for compression, fallback, and file size limits
- **Visual Status Indicators**: Real-time progress indicators with emoji feedback
- **Robust Error Handling**: Graceful handling of network issues and Discord API limits
- **Output Node Compatibility**: Functions as both preview and output node for flexible workflow integration

## Requirements
- Python 3.10+
- `Pillow`, `requests`, and `numpy` libraries (automatically installed via `requirements.txt`).

## Installation
- [Find it at ComfyUI Registry](https://registry.comfy.org/publishers/gmorks/nodes/comfyui-sendtodiscord) 
- Or using [comfy-cli](https://docs.comfy.org/comfy-cli/getting-started):

```bash
comfy node registry-install comfyui-sendtodiscord
```

## Manual Install
1. Clone the repository into your ComfyUI custom nodes directory:
    ```bash
    git clone https://github.com/gmorks/ComfyUI-SendToDiscord.git
    ```
2. Install dependencies:
    ```bash
    cd ComfyUI-SendToDiscord
    pip install -r requirements.txt
    ```
3. Configure the `config.ini` file:
    - Locate the `config.ini.template` file in the root directory.
    - Copy it and rename it to `config.ini`:
        ```bash
        cp config.ini.template config.ini
        ```
    - Open the `config.ini` file and replace the placeholder with your Discord webhook URL:
        ```ini
        ; Configuration file for ComfyUI-SendToDiscord
        ; Replace 'your-webhook-url-here' with your Discord webhook URL.
        ; You can get a webhook URL by going to your Discord server settings, then Integrations, then Webhooks, then New Webhook.

        [Discord]
        webhook_url = your-webhook-url-here
        ```
### Dependencies
This node has been tested with the following Python packages:

- `Pillow>=11.0.0` (updated for better WebP support and performance)
- `requests>=2.32.0` (updated for security improvements)
- `numpy>=1.26.0` (updated for compatibility)

If you encounter issues, please ensure these versions or higher are installed, or consult the official ComfyUI documentation for compatible dependencies.

## Usage

1. Open ComfyUI.
2. Add the "Preview Image (with Discord option)" node to your workflow.
3. Configure the node parameters:
    - **Send to Discord**: Enable or disable image uploads to Discord.
    - **Batch Mode**: Enable to accumulate images and send them in a single batch.
    - **Passthrough Image** (optional): Input for passing images through to other nodes.
4. Generate your images, and they will be uploaded automatically to the specified Discord channel.

## Configuration

### Node Parameters

- **images**: The list of images to process.
- **send_to_discord**: Enable or disable sending images to Discord (enable/disable).
- **batch_mode**: Accumulate images and send them as a batch (enable/disable).
- **passthrough_image** (optional): Input for chaining with other nodes.

### Advanced Configuration (config.ini)

The node supports extensive configuration options in your `config.ini` file:

```ini
[Discord]
webhook_url = your-webhook-url-here

[Fallback]
# Enable automatic fallback (individual sending if batch fails)
enable_fallback = true

# Enable automatic image compression
enable_compression = true

# Compression quality (0-100, higher = better quality)
compression_quality = 80

# Maximum file size before compression (MB)
max_file_size_mb = 8
```

### Key Features

- **Intelligent Fallback**: If batch sending fails, automatically attempts individual sending
- **WebP Compression**: Automatically compresses large images while preserving quality
- **Workflow Preservation**: When images are compressed, the original ComfyUI workflow JSON is automatically sent alongside
- **Visual Feedback**: Console messages with emoji indicators show upload progress and status
- **Flexible Integration**: Works as both a preview node and output node for maximum workflow compatibility

## Example Workflow

You can add this node after your image generation process to preview and share your results directly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
