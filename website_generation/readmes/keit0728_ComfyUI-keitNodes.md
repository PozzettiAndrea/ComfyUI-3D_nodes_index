# ComfyUI-keitNodes

**Languages:** [English](README.md) | [日本語](README.ja.md)

Custom nodes for ComfyUI by keit.

## Features

### 🌍 M2M-100 Translator

A powerful multilingual translation node powered by Meta's M2M-100 (Many-to-Many 100) model, supporting translation between 100+ languages.

**Key Features:**
- **Automatic Language Detection**: Automatically detects the source language when set to "auto_detect"
- **100+ Language Support**: Supports major world languages including Asian, European, African, and more
- **Multiple Model Sizes**: Choose between 418M and 1.2B parameter models based on your needs
- **GPU Acceleration**: Automatically utilizes CUDA if available for faster translation
- **Beam Search**: Configurable beam search for improved translation quality
- **Memory Efficient**: Models are shared across multiple node instances

**Supported Languages Include:**
- Asian: Japanese (ja), Chinese (zh), Korean (ko), Thai (th), Vietnamese (vi), Hindi (hi), etc.
- European: English (en), French (fr), German (de), Spanish (es), Russian (ru), Italian (it), etc.
- African: Arabic (ar), Swahili (sw), Amharica (am), Hausa (ha), etc.
- And many more...

### 🎯 Pixel Limit Resizer (16×)

An intelligent image resizing node that maintains aspect ratio while constraining pixel count and optimizing for 16-pixel multiple resolutions. Designed for 3D VAE spatiotemporal compression compatibility.

**Key Features:**
- **Pixel Count Limiting**: Calculates optimal resolution within specified pixel count constraints
- **Aspect Ratio Preservation**: Maintains original image aspect ratio as closely as possible
- **16-Pixel Multiple Constraint**: Adjusts width and height to be multiples of 16 (3D VAE compatible)
- **Multiple Upscale Methods**: Supports nearest-exact, bilinear, area, bicubic, lanczos interpolation methods
- **Detailed Output Information**: Provides resized image along with resolution metrics and aspect ratio data

**Technical Specifications:**
- **Default Max Pixels**: 589,824 (equivalent to 1024×576)
- **Minimum Resolution**: 16×16
- **Maximum Resolution**: 2048×2048
- **3D VAE Optimization**: Compatible with spatiotemporal compression (256× compression ready)

### 📺 WanVideo Optimal Resizer

A preset resolution conversion node optimized for the WanVideo platform. Analyzes input image aspect ratios and automatically selects the most suitable resolution from predefined presets for resizing.

**Key Features:**
- **Preset Resolutions**: Supports two presets - 480p and 720p
- **Multiple Aspect Ratio Support**: Each preset supports 5 different aspect ratios:
  - 16:9 vertical & horizontal
  - 1:1 square
  - Landscape (1.29:1 / 1.31:1)
  - Portrait (1:1.29 / 1:1.31)
- **Intelligent Selection**: Two-stage selection algorithm considering aspect ratio similarity and pixel count difference
- **Detailed Analysis**: Outputs comprehensive statistics before and after resizing

**Preset Resolutions:**

**480p Preset:**
- 480×832 (16:9 vertical)
- 832×480 (16:9 horizontal)
- 624×624 (1:1 square)
- 704×544 (1.29:1 landscape)
- 544×704 (1:1.29 portrait)

**720p Preset:**
- 720×1280 (16:9 vertical)
- 1280×720 (16:9 horizontal)
- 960×960 (1:1 square)
- 1088×832 (1.31:1 landscape)
- 832×1088 (1:1.31 portrait)

**Selection Algorithm:**
1. **Aspect Ratio Priority**: Identifies candidates with aspect ratios closest to the original image
2. **Resolution Optimization**: Selects the candidate with pixel count closest to the original among optimal aspect ratio matches

### 🔍 WanVideo Resolution Finder

An optimal resolution calculation node for the WanVideo platform. Uses the same algorithm as WanVideo Optimal Resizer but only returns the optimal resolution values without performing the actual resize.

**Key Features:**
- **Resolution Calculation Only**: Outputs optimal width and height values without resizing the image
- **Identical Algorithm**: Uses the same selection logic as WanVideo Optimal Resizer
- **Preset Support**: Choose between 480p and 720p presets
- **Lightweight Processing**: Fast operation as no image processing is performed

**Use Cases:**
- When you need to check optimal resolution before resizing
- When you want to use resolution information in other nodes
- When determining unified resolution for batch processing

**Output:**
- width (INT): Optimal width in pixels
- height (INT): Optimal height in pixels

### 📐 Aspect Ratio Resolution Finder

A resolution calculation node that maintains the original aspect ratio while adjusting to a specified height preset. This node only calculates the optimal width and height values without performing actual image resizing.

**Key Features:**
- **Height Preset Support**: Supports various height presets from 144p to 2160p
- **Aspect Ratio Preservation**: Calculates width automatically to maintain the original aspect ratio
- **No Image Processing**: Only returns resolution values, making it extremely fast
- **Precise Calculations**: Provides exact pixel dimensions based on aspect ratio

**Available Height Presets:**
- 144p (144 pixels)
- 240p (240 pixels)
- 360p (360 pixels)
- 480p (480 pixels)
- 540p (540 pixels)
- 576p (576 pixels)
- 720p (720 pixels)
- 900p (900 pixels)
- 1080p (1080 pixels)
- 1200p (1200 pixels)
- 1440p (1440 pixels)
- 1600p (1600 pixels)
- 2160p (2160 pixels)

**Use Cases:**
- When you need to calculate resolution maintaining aspect ratio before processing
- When standardizing multiple images to the same height while preserving their aspect ratios
- When planning resolution requirements for video processing pipelines
- When you need resolution information for other nodes without actual resizing

**Output:**
- width (INT): Calculated width in pixels (maintaining aspect ratio)
- height (INT): Selected height preset in pixels

## Installation

### Prerequisites
- ComfyUI installed and working

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "ComfyUI-keitNodes"
3. Click Install

### Method 2: Manual Installation
1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-keitNodes.git
```

2. Install required dependencies:
```bash
cd ComfyUI-keitNodes
pip install -r requirements.txt
```

3. Restart ComfyUI
