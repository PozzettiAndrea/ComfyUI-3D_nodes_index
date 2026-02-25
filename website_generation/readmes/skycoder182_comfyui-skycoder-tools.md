# 🛠️ ComfyUI Skycoder Tools

[![GitHub release](https://img.shields.io/github/release/skycoder/comfyui-skycoder-tools.svg)](https://github.com/skycoder/comfyui-skycoder-tools/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive collection of useful custom nodes for ComfyUI workflows. Designed to enhance productivity and extend ComfyUI's capabilities with practical, everyday tools.

## 🚀 Current Tools

### 📁 Tools
- **DirectoryImageLoader**: Load images from a directory by index
- **DirectoryImageInfo**: Get detailed information about images in a directory
- **Aspect Ratio and Tile size calculator**: Calculates the aspect ratio of an image and determines optimal tile dimensions based on a target megapixel value, upscale factor, and optional padding. Useful for tiled image processing workflows.
- **BLIP2 Image Caption**: Automatically generates a descriptive caption for an input image using Salesforce’s BLIP image captioning model. Ideal for semantic image analysis or annotation tasks.
- **Boolean Toggle**: Returns a boolean value from a toggle input. Useful for conditionally controlling workflow branches.
- **Concatenate and Test if Empty**: Concatenates up to four text inputs and checks whether the result is empty. Outputs both the combined string and a boolean indicating if it's empty.
- **ImageBasicNode**: Perform basic image operations such as resizing (with optional aspect ratio preservation) and grayscale conversion. Returns the processed image along with useful metadata like width, height, aspect ratio, color mode, and format. Ideal for simple preprocessing tasks within your ComfyUI workflows.

*More tools coming soon! This is just the beginning of the Skycoder Tools collection.*

## 🎯 Features

- **Modular Design**: Each tool category is organized in separate modules
- **Easy Extension**: Simple structure for adding new tools
- **Robust Error Handling**: Graceful fallbacks and detailed error messages
- **Professional Quality**: Production-ready code with comprehensive testing
- **Community Focused**: Built for and by the ComfyUI community

## 📦 Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Go to "Install Custom Nodes"
3. Search for "Skycoder Tools"
4. Click Install and restart ComfyUI

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/skycoder/comfyui-skycoder-tools.git
# Restart ComfyUI
### 🧠 Image Analysis & Utilities

