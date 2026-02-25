# ComfyUI DeepStereo Nodes

A comprehensive set of ComfyUI nodes for generating AI-powered autostereograms (Magic Eye images) with procedural texture generation. This project brings the power of [DeepStereo](https://github.com/SanDiegoDude/DeepStereo/tree/main) into the ComfyUI node-based workflow environment.

## Overview

Transform any image into mesmerizing autostereograms using AI-generated depth maps and procedurally created textures. These nodes break down the complex stereogram generation process into modular, interconnected components that can be mixed and matched for endless creative possibilities.

## Features

### 🧠 AI Depth Estimation & Processing
- **Enhanced MiDaS Integration**: State-of-the-art depth estimation with built-in processing
- **Multiple Models**: MiDaS_small, DPT_Large, and DPT_Hybrid
- **Smart Model Management**: Automatic model handling in ComfyUI's controlnet directory
- **Advanced Depth Controls**:
  - Contrast and brightness adjustment
  - Gamma correction
  - Min/Max depth range control
  - Optional depth normalization
  - Blur for smoothing
  - Process width control

### 🎨 Pattern & Texture Generation
- **Procedural Texture Methods**:
  - Content-driven color dots with multiple modes
  - Advanced pattern generation with seamless tiling
  - Optimized for stereogram use
- **Pattern Width Control**: Matches stereogram separation for optimal results
- **12 Noise Types**:
  - RGB: Random color noise
  - Grayscale: Monochrome noise
  - Colored Dots: Random dot patterns
  - Perlin: Enhanced Perlin-like noise
  - Voronoi: Cell-based patterns
  - Kaleidoscope: Symmetric radial patterns
  - Waves: Wave interference patterns
  - Cellular: Organic cell-like patterns
  - Fractal: Complex self-similar patterns
  - Spiral: Spiral-based patterns
  - Interference: Wave interference effects
  - Crystalline: Geometric crystal-like patterns
- **Advanced Pattern Controls**:
  - Frequency control
  - Color variation
  - Multiple octaves
  - Symmetry points
  - Seamless tiling
  - Pattern width optimization

### ✨ Enhanced Stereogram Generation
- **Multiple Algorithms**: 
  - Standard: Basic stereogram generation
  - Improved: Better texture distribution
  - Layered: Advanced with texture preprocessing
  - Central: Enhanced pattern variation
- **Reference Types**:
  - Left to right
  - Right to left
  - Center out (recommended)
- **Depth Control**:
  - Up to 50 distinct depth layers
  - Layer smoothing control
  - Min/Max separation adjustment
- **Random Dot Stereograms**: 
  - Traditional RDS with depth layer support
  - Customizable dot density
  - Color control

### 🎨 Image Effects
- **Enhanced Image Processing**:
  - Advanced sharpening
  - Multiple blend modes:
    - Multiply/Screen
    - Overlay
    - Darken/Lighten
    - Color Dodge/Burn
    - Hard/Soft Light
    - Difference/Exclusion
  - Brightness preservation
  - Strength control
  - Color blending

### 🔧 Utility Features
- **Smart Image Resizing**: 
  - Megapixel-based
  - Dimension-based
  - Aspect ratio preservation
- **Texture Transformation**:
  - Rotation with multiple modes
  - Grid pattern generation
  - Color inversion
  - Size control
- **Color Management**:
  - RGB sliders
  - Preset colors
  - Hex input
  - Format options

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-DeepStereo-Nodes.git
```

2. Install the required dependencies:
```bash
cd ComfyUI-DeepStereo-Nodes
pip install -r requirements.txt
```

3. Restart ComfyUI

**Note**: This extension requires PyTorch, which should already be installed with ComfyUI. If you encounter torch-related issues, ensure your ComfyUI installation includes proper CUDA support for GPU acceleration.

## Quick Start

### Recommended Workflow
1. **Depth Map Creation**:
   - **Load Image** → **MiDaS Depth Estimator**
   - Use DPT_Large model for best quality
   - Adjust contrast, brightness, and depth range
   - Enable depth normalization for optimal results

2. **Texture Generation** (choose one):
   - **Random Noise Generator**:
     - Set pattern_width to match max_separation (default 100)
     - Try kaleidoscope, crystalline, or interference patterns
     - Enable seamless tiling
   - **Procedural Texture Generator**:
     - Use content-driven patterns
     - Apply texture transformation if needed

3. **Stereogram Creation**:
   - Use **Stereogram Generator** with:
     - Algorithm: "central"
     - Reference type: "center_out"
     - Depth layers: 50
     - Layer smoothing: 1.0
   - Or try **Random Dot Stereogram Generator** for classic effects

### Advanced Techniques
- **Pattern Enhancement**:
  - Use Image Effects for sharper, more defined patterns
  - Try different blend modes for unique effects
  - Adjust pattern frequency and color variation

- **Depth Optimization**:
  - Fine-tune depth layers for desired 3D effect
  - Use gamma correction for depth emphasis
  - Apply subtle blur for smoother transitions

- **Texture Tips**:
  - Avoid blurry or overly complex patterns
  - Use high contrast for better depth perception
  - Keep pattern size consistent with separation values

## Node Categories

### DeepStereo/Depth
- **MiDaS Depth Estimator**: AI-powered depth map generation with integrated processing

### DeepStereo/Texture
- **Procedural Texture Generator**: Multi-method texture creation
- **Random Noise Generator**: Advanced pattern generation with 12 noise types
- **Texture Transformer**: Rotation, grid, and transform effects

### DeepStereo/Effects
- **Image Effects**: Advanced image processing and blending

### DeepStereo/Generation
- **Stereogram Generator**: Create sophisticated autostereograms
  - Multiple algorithms and reference types
  - Depth layer control
  - Advanced smoothing
- **Random Dot Stereogram**: Enhanced RDS generation
  - Depth layer support
  - Advanced controls
  - Color customization

### DeepStereo/Utility
- **Image Resizer**: Smart dimension control
- **Color Picker**: Advanced color selection

## Requirements

- ComfyUI (with PyTorch)
- OpenCV (`opencv-python>=4.5.0`)
- NumPy (`numpy>=1.19.0`)
- tqdm (`tqdm>=4.50.0`)
- PIL/Pillow (usually included with ComfyUI)

## Credits and Inspiration

This ComfyUI node collection is based on my [DeepStereo](https://github.com/SanDiegoDude/DeepStereo/tree/main) standalone utility. DeepStereo is an integration of AI depth estimation with procedural texture generation for easy and fun autostereogram creation.

**Original DeepStereo Features Translated to Nodes:**
- Complete CLI functionality broken into modular nodes
- All texture generation methods (M1-M4) available
- Multiple stereogram algorithms implemented
- Advanced texture transformation and blending capabilities

If you prefer command-line usage or need batch processing capabilities, check out the original [DeepStereo repository](https://github.com/SanDiegoDude/DeepStereo/tree/main).

## License

This project is open source. See LICENSE file for details.

## Contributing

Issues and pull requests welcome! This project aims to make autostereogram generation accessible to everyone through ComfyUI's intuitive interface.

---

*Create mesmerizing Magic Eye images with the power of AI and procedural generation!*
