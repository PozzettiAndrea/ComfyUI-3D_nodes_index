# Upscaler Downloader for ComfyUI

A custom node plugin that allows you to download, organize, and manage upscaler/super-resolution models directly inside ComfyUI.

## Features

- Download upscaler models from URLs
- Manage local upscaler model directories
- Support for various upscaler formats (.pth, .pt, .safetensors)
- Download existing models to local machine
- Batch download all models at once

## Supported Models

- RealESRGAN (x2, x4, x8)
- ESRGAN
- SwinIR
- Other upscaler models

## Installation

### Using ComfyUI-Manager
Search for `Upscaler Downloader for ComfyUI` and install.

### Manual install
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/huihuihuiz/upscaler_downloader
```

## Usage

1. Open ComfyUI
2. Click the "放大模型下载器" button in the menu, or visit `http://your-comfyui-address/upscaler_downloader`
3. Enter the model name and download URL
4. Click "下载放大模型" to start downloading

## Web Interface

Access the web interface at: `http://localhost:8188/upscaler_downloader`

## License

MIT License
