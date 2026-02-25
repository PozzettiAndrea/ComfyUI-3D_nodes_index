# ComfyUI OmniSVG Nodes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)
[![OmniSVG](https://img.shields.io/badge/OmniSVG-3B-orange.svg)](https://github.com/OmniSVG/OmniSVG)

Generate high-quality SVG graphics from text descriptions and images using OmniSVG in ComfyUI.


## 🎯 Features

- **🔧 OmniSVG Model Loader**: Load and manage OmniSVG models
- **📝 Text to SVG**: Generate SVG graphics from text descriptions
- **🖼️ Image to SVG**: Convert images to SVG format
- **🔄 SVG to Image**: Convert SVG strings to ComfyUI IMAGE tensors
- **💾 SVG Saver**: Save SVG files to disk

## 🚀 Quick Start

```bash
# Clone to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-OmniSVG.git
cd ComfyUI-OmniSVG

# Install dependencies and setup
python install.py

# Restart ComfyUI
```

## 📋 Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Node Reference](#node-reference)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 📦 Installation

### Method 1: Automated Installation (Recommended)

```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes/

# Clone the repository
git clone https://github.com/yourusername/ComfyUI-OmniSVG.git
cd ComfyUI-OmniSVG

# Run automated installer
python install.py

# Restart ComfyUI
```

The installer will:
- ✅ Install all Python dependencies
- ✅ Set up the models directory
- ✅ Verify the installation
- ✅ Provide next steps

### Method 2: Manual Installation

<details>
<summary>Click to expand manual installation steps</summary>

1. **Clone Repository**
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/yourusername/ComfyUI-OmniSVG.git
   cd ComfyUI-OmniSVG
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Model Weights**
   ```bash
   # Create models directory
   mkdir -p ../../models/omnisvg/

   # Download model (requires huggingface-cli)
   huggingface-cli download OmniSVG/OmniSVG --local-dir ../../models/omnisvg/OmniSVG-3B
   ```

4. **Restart ComfyUI**

</details>

### Method 3: Using Existing OmniSVG Installation

If you already have OmniSVG installed (e.g., in `/mnt/storage/OmniSVG-3B`), the nodes will automatically detect and use it.

## Requirements

- **GPU Memory**: 17GB+ VRAM for optimal performance
- **Python**: 3.8+
- **PyTorch**: 2.3.0+
- **CUDA**: 12.1+ (recommended)

## Usage

### Basic Workflow

1. **Load Model**: Use "OmniSVG Model Loader" to load the model
2. **Generate SVG**: 
   - Use "OmniSVG Text to SVG" for text-based generation
   - Use "OmniSVG Image to SVG" for image conversion
3. **Process Output**:
   - Use "SVG to Image" to convert SVG to ComfyUI images
   - Use "SVG Saver" to save SVG files

### Node Parameters

#### OmniSVG Text to SVG
- **text_prompt**: Description of the SVG to generate
- **temperature**: Controls randomness (0.1-2.0)
- **top_p**: Nucleus sampling parameter (0.1-1.0)
- **top_k**: Top-k sampling parameter (1-100)
- **repetition_penalty**: Prevents repetition (1.0-2.0)

#### OmniSVG Image to SVG
- **image**: Input image to convert
- **target_size**: Resize image before processing (64-512px)
- **temperature**: Lower values for more faithful conversion (0.01-1.0)
- **top_p**: Nucleus sampling (0.001-1.0)

## Model Storage

Models should be placed in:
```
ComfyUI/models/omnisvg/
└── OmniSVG-3B/
    ├── config.yaml
    ├── config.json
    ├── pytorch_model.bin
    └── README.md
```

## Performance Tips

- **GPU**: Use CUDA for 10-50x faster generation
- **Memory**: Ensure 17GB+ VRAM available
- **Batch Size**: Process one image at a time for stability
- **Temperature**: Lower values (0.1-0.3) for more consistent results

## Troubleshooting

### Common Issues

1. **"Download Required" in model list**
   - Download OmniSVG models to `ComfyUI/models/omnisvg/`
   - Or ensure existing installation is accessible

2. **CUDA Out of Memory**
   - Free up GPU memory from other processes
   - Use CPU mode (slower but functional)

3. **Import Errors**
   - Install all requirements: `pip install -r requirements.txt`
   - Ensure OmniSVG core files are copied correctly

### Error Messages

- **"Model not found"**: Check model path and file permissions
- **"Generation error"**: Check GPU memory and model loading
- **"SVG conversion failed"**: Verify CairoSVG installation

## Examples

### Text to SVG
```
Input: "A minimalist icon of a coffee cup with steam"
Output: Clean SVG icon suitable for web use
```

### Image to SVG
```
Input: Photo of a simple logo or icon
Output: Vector SVG representation
```

## License

This project follows the same license as OmniSVG. Please refer to the original OmniSVG repository for licensing details.

## Credits

- **OmniSVG**: Original model and implementation
- **ComfyUI**: Node framework and integration
- **Qwen2.5-VL**: Base vision-language model

## Support

For issues and questions:
1. Check this README and troubleshooting section
2. Review ComfyUI console output for error details
3. Open an issue on GitHub with error logs
