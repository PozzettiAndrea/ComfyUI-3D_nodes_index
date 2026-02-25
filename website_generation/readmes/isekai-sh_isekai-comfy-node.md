# Isekai ComfyUI Custom Node

[![Latest Release](https://img.shields.io/github/v/release/isekai-sh/isekai-comfy-node)](https://github.com/isekai-sh/isekai-comfy-node/releases/latest)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/isekai-sh/isekai-comfy-node)](LICENSE)

A comprehensive collection of custom nodes for ComfyUI featuring **22 image manipulation nodes**, multiple **LLM integrations** (Claude, OpenAI, Gemini, Ollama), **string utilities**, and **cloud upload** capabilities. Designed to integrate seamlessly with your Isekai Core deployment and enhance your ComfyUI workflows.

[Access the documentation here](https://isekai.sh/comfyui)

## Features

### Image Manipulation (22 Nodes)
Transform and enhance your images with professional-grade effects and transformations using only PIL/Pillow - no additional dependencies required.

- **Blend Operations**: Blend images, adjust colors, apply color ramps, modify levels, split toning
- **Effects**: Blur, sharpen, grain, vignette, chromatic aberration, glare, edge enhancement, color filters, invert, posterize, pixelate
- **Transformations**: Rotate, scale, crop, flip, translate, combined transforms

### LLM Integrations (4 Nodes)
Generate captions, titles, and descriptions using your preferred AI model.

- **Ollama**: Local LLM integration
- **Claude**: Anthropic's Claude API
- **OpenAI**: GPT models via OpenAI API
- **Gemini**: Google's Gemini API

### Dataset & String Utilities (4 Nodes)
Powerful text manipulation for dynamic prompts and batch processing.

- Dynamic string selection with variables
- String concatenation
- Tag selection and management
- Round-robin item cycling for batch workflows

### Cloud Upload (2 Nodes)
Upload your generated images to cloud storage.

- **Isekai Upload**: Direct integration with Isekai platform
- **S3 Upload**: AWS S3 and Cloudflare R2 support

### I/O Utilities (3 Nodes)
File operations for workflows.

- Compress and save images with quality control
- Load text from files
- Random line selection from text files

## Node Categories

All nodes are organized alphabetically in the ComfyUI menu under the **Isekai** category:

### Dataset (4 nodes)
- **Concatenate String**: Join multiple strings together
- **Dynamic String**: Select strings with variable support
- **Round Robin**: Cycle through items in batch workflows
- **Tag Selector**: Manage and select tags

### Image/Blend (5 nodes)
- **Blend Images**: Combine two images with various blend modes (Normal, Multiply, Screen, Add, Subtract, Difference, Lighten, Darken)
- **Color Adjust**: Adjust brightness, contrast, saturation, and sharpness
- **Color Ramp**: Apply gradient mapping for color grading
- **Levels**: Adjust black and white points
- **Split Toning**: Apply separate colors to highlights and shadows

### Image/Effects (11 nodes)
- **Blur**: Gaussian and Box blur effects
- **Chromatic Aberration**: RGB channel offset for lens effects
- **Color Filter**: Apply Sepia, Grayscale, or Black & White filters
- **Edge Enhance**: Enhance or detect edges
- **Glare**: Add bloom/glare effects to bright areas
- **Grain**: Add film grain or noise
- **Invert**: Invert image colors
- **Pixelate**: Create mosaic/pixel art effects
- **Posterize**: Reduce color levels for poster effects
- **Sharpen**: Sharpen images with Unsharp Mask
- **Vignette**: Darken edges with customizable radius and softness

### Image/Transform (6 nodes)
- **Crop**: Crop images to specified dimensions
- **Flip**: Flip images horizontally, vertically, or both
- **Rotate**: Rotate images by any angle
- **Scale**: Resize images with various resampling methods
- **Transform**: Combined rotate, scale, and translate operations
- **Translate**: Move/shift images

### IO (3 nodes)
- **Compress and Save**: Save images with quality control
- **Load Text**: Load text content from files
- **Random Line From File**: Select random lines from text files

### LLMs (4 nodes)
- **Claude**: Generate text using Anthropic's Claude API
- **Gemini**: Generate text using Google's Gemini API
- **Ollama**: Generate text using local Ollama models
- **OpenAI**: Generate text using OpenAI's GPT models

### Upload (2 nodes)
- **Upload to Isekai**: Upload images to Isekai platform
- **Upload to S3**: Upload to AWS S3 or Cloudflare R2

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "isekai"
3. Click Install
4. Restart ComfyUI

### Manual Installation
1. Clone or download this repository
2. Place it in `ComfyUI/custom_nodes/isekai-comfy-node`
3. Install dependencies:
   ```bash
   cd ComfyUI/custom_nodes/isekai-comfy-node
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

## Support

- **Issues:** Report bugs on [GitHub Issues](https://github.com/isekai-sh/isekai-comfy-node/issues)

## Development

### Project Structure

```
isekai-comfy-node/
├── __init__.py              # Package entry point
├── config.py                # Configuration management
├── pyproject.toml           # Package metadata for ComfyUI registry
├── README.md                # This file
├── requirements.txt         # Dependencies
│
├── nodes/                   # Node implementations
│   ├── __init__.py
│   ├── base.py              # Base classes and exceptions
│   │
│   ├── image/               # Image manipulation nodes (22 nodes)
│   │   ├── blend/           # Blend operations (5 nodes)
│   │   ├── effects/         # Visual effects (11 nodes)
│   │   └── transform/       # Geometric transforms (6 nodes)
│   │
│   ├── claude_node.py       # Claude API integration
│   ├── gemini_node.py       # Gemini API integration
│   ├── openai_node.py       # OpenAI API integration
│   ├── ollama_summarizer_node.py
│   │
│   ├── dynamic_string_node.py
│   ├── concatenate_string_node.py
│   ├── tag_selector_node.py
│   ├── round_robin_node.py
│   │
│   ├── upload_node.py       # Isekai upload
│   ├── s3_upload_node.py    # S3/R2 upload
│   │
│   ├── compress_and_save_node.py
│   ├── load_text_node.py
│   └── random_from_file_node.py
│
└── utils/                   # Shared utilities
    ├── __init__.py
    ├── validation.py        # Input validation
    ├── image_utils.py       # Image tensor/PIL conversion
    ├── cloud_llm_client.py  # Claude/OpenAI/Gemini client
    ├── ollama_client.py     # Ollama API client
    └── s3_client.py         # AWS S3/R2 client
```

### Requirements

- Python 3.8+
- ComfyUI
- Pillow >= 10.0.0
- torch >= 2.0.0 (typically included with ComfyUI)
- numpy >= 1.24.0 (typically included with ComfyUI)
- requests >= 2.31.0

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
