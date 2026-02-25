# ComfyUI-S4Tool-Image

**Version: 1.6.0**

A comprehensive image processing toolkit for ComfyUI, providing 23 professional-grade image manipulation nodes with production-ready quality and reliability, including advanced AI-powered segmentation capabilities with SAM2.1 and GroundingDINO.

## 🚀 Features

### Core Image Processing
- **💀Image Color Picker** - Extract colors from images with precision
- **💀Image Combine** - Merge multiple images with advanced blending options
- **💀Image Resize** - High-quality image resizing with multiple algorithms
- **💀Image Crop To Fit** - Smart cropping to fit specific dimensions
- **💀Image Adjustment** - Professional color and tone adjustments

### Advanced Effects
- **💀Image Blend With Alpha** - Advanced alpha blending with multiple modes
- **💀Image Remove Alpha** - Convert RGBA images to RGB with customizable background color
- **💀Image Overlay** - Layer images with positioning and transformation controls
- **💀Image Board** - Create image grids and layouts
- **💀Image Tiling Pattern** - Generate seamless tiling patterns
- **💀Image RMBG** - Background removal with AI-powered precision
- **💀Image SAM** - Segment Anything Model with GroundingDINO for intelligent object segmentation
- **💀Image SAM2** ⭐ NEW - Enhanced SAM2.1 with advanced features:
  - 8 SAM2 models (tiny to large)
  - NMS duplicate detection removal
  - Adjustable detection box padding
  - Minimum object size filtering
  - Adjustable edge smoothing strength (0-5)
  - Smart output quantity control
  - Quality-based filtering
  - 20-38% performance boost in complex scenes

### Color & Palette Tools
- **💀Image Color** - Generate solid color images
- **💀Image Palette** - Extract and analyze color palettes
- **💀Image Palette 6-3-1** - Specialized 6-3-1 color palette extraction
- **💀Image Primary Color** - Identify dominant colors in images
- **💀Image Get Color** - Sample colors from specific image coordinates

### File & Data Operations
- **💀Image from Base64** - Convert Base64 strings to images
- **💀Image from URL** - Load images directly from URLs
- **💀Image from Folder** - Batch load images from directories
- **💀Image from Folder by Index** - Load specific images by index
- **💀Image To Base64** - Convert images to Base64 format

### Mask Operations
- **💀Image Mask Expand** - Expand and contract image masks

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "S4Tool-Image" 
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/S4MUEL-404/ComfyUI-S4Tool-Image.git
   ```
3. Install dependencies:
   ```
   pip install -r ComfyUI-S4Tool-Image/requirements.txt
   ```
4. **⚠️ CRITICAL: Install BERT Model for SAM Node**
   
   Navigate to your ComfyUI models directory and install BERT model:
   ```bash
   cd ComfyUI/models/
   git clone https://huggingface.co/google-bert/bert-base-uncased
   ```
   
   **This step is REQUIRED for the 💀Image SAM node to function properly!**
   
   Without this model, the SAM functionality will fail. The BERT model is needed for GroundingDINO's text processing capabilities.
   
5. Restart ComfyUI

## 🔧 Dependencies

The plugin automatically manages its dependencies and provides detailed startup logging:
- **Pillow** (PIL) - Core image processing
- **NumPy** - Numerical operations
- **Requests** - URL image loading
- **AI Model Libraries** - Background removal, SAM segmentation, and GroundingDINO
- **Segment Anything** - Advanced object segmentation
- **Transformers** - BERT and neural network support

### ⚠️ **CRITICAL REQUIREMENT: BERT Model for SAM**

For the **💀Image SAM** node to work, you **MUST** install the BERT model manually:

```bash
cd ComfyUI/models/
git clone https://huggingface.co/google-bert/bert-base-uncased
```

**Why is this required?**
- GroundingDINO (used by SAM) requires BERT for natural language processing
- The model enables text-based object detection and segmentation
- Without it, SAM functionality will completely fail

All other dependencies are automatically checked at startup with production-quality validation.

## 📖 Usage

1. **Find Nodes**: All S4Tool-Image nodes are prefixed with 💀 in the ComfyUI node browser
2. **Categories**: Look under "💀S4Tool-Image" category
3. **Production Ready**: All nodes include comprehensive error handling and logging
4. **Examples**: Check the `examples/` folder for usage documentation

### Quick Start Example
1. Add any S4Tool-Image node to your workflow
2. Connect your image input
3. Configure node parameters
4. Execute workflow

## 🎯 Key Features

- ✅ **Production Quality** - Enterprise-grade error handling and validation
- ✅ **Comprehensive Logging** - Detailed operation tracking and debugging
- ✅ **Automatic Dependencies** - Smart dependency management and validation
- ✅ **Professional Tools** - 23 specialized image processing nodes
- ✅ **High Performance** - Optimized algorithms for speed and quality
- ✅ **User Friendly** - Intuitive node interfaces with helpful defaults

## 🆕 What's New in v1.6.0

### New Node: Image Remove Alpha
- Convert RGBA images to RGB format
- Remove alpha channel from images or image sequences
- Customizable background color for transparent areas (hex color format)
- Proper alpha blending with background
- Batch processing support

## 🆕 What's New in v1.5.0

### ImageSAM2 - Major Enhancement
Completely upgraded SAM2 node with production-grade features:

**Model Support**
- 8 SAM2 models: SAM2.1 and SAM2 series (tiny/small/base_plus/large)
- Support for 2 GroundingDINO models (SwinT/SwinB)

**Detection Optimization** (4 new parameters)
- `nms_threshold` - Remove duplicate detections (IoU-based NMS)
- `box_padding` - Adjust detection box size (-50 to +50 pixels)
- `min_box_size` - Filter out small noise detections
- `max_detections` - Limit output quantity with quality priority

**Edge Enhancement**
- `smooth_strength` - Adjustable edge smoothing (0.0-5.0)
- Natural to feathered edge effects

**Performance**
- 20-38% faster processing in complex scenes
- Smart filtering pipeline reduces redundant computations

**Total Parameters**: 16 (12 basic + 4 new advanced)

### Documentation
- Complete parameter guide with visual examples
- Quick reference table for all 16 parameters
- 5 preset configurations for common scenarios
- Troubleshooting guide and FAQ

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues.

## 📜 License

This project is open source. Please respect the licensing terms.

---

**Author:** S4MUEL  
**Website:** [s4muel.com](https://s4muel.com)  
**GitHub:** [S4MUEL-404/ComfyUI-S4Tool-Image](https://github.com/S4MUEL-404/ComfyUI-S4Tool-Image)  
**Version:** 1.6.0
