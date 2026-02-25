# UNet Downloader for ComfyUI

A custom node plugin that allows you to download, organize, and manage UNet/Diffusion models directly inside ComfyUI.

## Features

- Download UNet models from URLs (HuggingFace, Civitai and direct links supported)
- Manage local UNet model directories
- Support for FLUX, SD3, and other diffusion models
- Download existing models to local machine
- Batch download all models at once

## Supported Models

- FLUX.1 Dev/Schnell (FP8, FP16)
- Stable Diffusion 3
- Other UNet-based diffusion models

## Installation

### Using ComfyUI-Manager
Search for `UNet Downloader for ComfyUI` and install.

### Manual install
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/huihuihuiz/unet_downloader
```

## Usage

1. Open ComfyUI
2. Click the "UNet 下载器" button in the menu, or visit `http://your-comfyui-address/unet_downloader`
3. Enter the model name and download URL
4. Click "下载 UNet 模型" to start downloading

## Web Interface

Access the web interface at: `http://localhost:8188/unet_downloader`

## Note

UNet model files are typically very large (20GB-50GB). Make sure you have enough disk space and a stable internet connection.

## License

MIT License
