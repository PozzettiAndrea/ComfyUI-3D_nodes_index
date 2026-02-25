# ComfyUI_Detonate

**Professional compositing nodes for ComfyUI** - bringing Nuke and DaVinci Fusion workflows to AI-powered image generation.

[![Version](https://img.shields.io/badge/version-0.10.0-blue.svg)](DEVLOG.md)
[![Nodes](https://img.shields.io/badge/nodes-45-green.svg)](#node-categories)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

## 🎯 What is This?

ComfyUI_Detonate provides **45 professional compositing nodes** familiar to VFX artists, enabling traditional compositing workflows alongside AI image generation. All nodes support 32-bit float images with full precision, just like professional compositing software.

**Perfect for:**
- Compositors transitioning from Nuke/Fusion to AI workflows
- AI artists who need professional-grade image manipulation
- Anyone who wants industry-standard compositing tools in ComfyUI

## ✨ Features

- **AI inpainting helpers** - TriMap Generator, Seam Blender for perfect AI integration
- **Bridge tools for GenAI workflows** - Edge defringing, displacement mapping, mesh warping
- **Professional keying tools** - ChromaKeyer & LumaKeyer for greenscreen workflows
- **Mask refinement tools** - Professional edge smoothing and feathering (see [masking workflow guide](DOCS/MASKING_WORKFLOW.md))
- **Professional-grade algorithms** based on Nuke and Fusion

> **Note:** RotoBezier is experimental only - use ComfyUI's MaskEditor + Mask Smoother for practical masking workflows. See [deprecation notice](nodes/matte/ROTOBEZIER_DEPRECATED.md) for details.
- **Full float image support** (0-∞ range, not limited to 0-1)
- **User-friendly EXR loading** - File selector dropdown for easy EXR file access (see [EXR workflow guide](DOCS/EXR_WORKFLOW.md))
- **Multi-channel EXR support** for CG render passes with AOV selection
- **Cryptomatte ID mattes** for object/material extraction with dropdown file selection
- **Depth-based compositing** (ZDefocus, ZMerge) for CG workflows
- **Visual effects** (Glow, Defocus, Sharpen) for professional finishing
- **Professional color grading** with Bezier curves
- **Procedural generators** (Ramp, Noise with 10 algorithms) for masks and textures
- **Premultiplied alpha workflow** for accurate compositing
- **GPU-accelerated** operations using PyTorch
- **Batch processing** support for efficient workflows
- **Industry-standard** blend modes and color operations

## 📦 Installation

### Standard Installation (Recommended)

1. **Navigate to your ComfyUI custom nodes directory:**
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. **Clone this repository:**
   ```bash
   git clone https://github.com/aTanguay/ComfyUI_Detonate.git
   ```

3. **Install dependencies:**
   ```bash
   cd ComfyUI_Detonate
   pip install -r requirements.txt
   ```

4. **Restart ComfyUI**

The nodes will appear in the **Add Node → detonate/** category.

### Requirements

ComfyUI_Detonate requires the following Python packages:

- **torch** >= 2.0.0 (usually already installed with ComfyUI)
- **numpy** >= 1.23.5, < 2.0.0 (IMPORTANT: Must be < 2.0 for ComfyUI compatibility)
- **pillow** >= 9.0.0, < 11.0.0 (IMPORTANT: Must be < 11.0 for gradio compatibility)
- **opencv-python** >= 4.5.0 (for advanced image processing)
- **OpenImageIO** >= 2.4.0 (optional, for multi-channel EXR support)

**⚠️ Windows Users:** The version constraints on numpy (<2.0) and pillow (<11.0) are critical for ComfyUI compatibility. Do not remove these constraints.

### Manual Installation

If you prefer not to use git:

1. Download the repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/ComfyUI_Detonate/`
3. Install dependencies: `pip install -r requirements.txt`
4. Restart ComfyUI

### Troubleshooting

**Nodes not appearing?**
- Check the ComfyUI console for error messages
- Ensure all dependencies are installed: `pip list | grep -E "torch|numpy|pillow|opencv"`
- Try reinstalling: `pip install -r requirements.txt --force-reinstall`

**Import errors on Windows?**
- Verify numpy version is < 2.0: `pip show numpy`
- Verify pillow version is < 11.0: `pip show pillow`
- If needed, downgrade: `pip install "numpy<2.0" "pillow<11.0"`

---

## 🎨 Node Categories

### Compositing & Blending
- **Merge** - 16 blend modes (Over, Screen, Multiply, Overlay, etc.)
- **Premultiply/Unpremultiply** - Alpha channel workflows
- **SeamBlender** - Remove AI tiling seams

### Color Grading
- **Grade** - Lift/Gamma/Gain (Nuke-style)
- **ColorCorrect** - Quick adjustments (saturation, contrast, gamma, hue shift)
- **ColorCurves** - Bezier RGB curves
- **HueSatVal** - HSV manipulation
- **Saturation** - Saturation control
- **Exposure** - Photographic exposure (f-stops)
- **LUT** - 1D/3D LUT support
- **Clamp** - Value range limiting
- **Invert** - Color/channel inversion

### Keying & Matting
- **ChromaKeyer** - Greenscreen/bluescreen keying
- **LumaKeyer** - Brightness-based keying
- **LumaKeyer Simple** - Quick luma keying
- **RotoBezier** - Interactive Bezier spline drawing
- **RotoBezier From Image** - Roto with image reference
- **EdgeDefringe** - Remove edge artifacts
- **MatteControl** - All-in-one matte refinement
- **Erode/Dilate** - Matte expansion/contraction
- **TriMap Generator** - Generate trimaps for AI inpainting

### Transforms & Warping
- **Transform** - Translate, rotate, scale, skew
- **CornerPin** - 4-point perspective
- **DisplacementMap** - UV displacement warping
- **GridWarp** - Mesh-based warping
- **Crop** - Aspect ratio cropping with soft edges

### Filters & Effects
- **Blur** - Gaussian blur
- **Sharpen** - Image sharpening
- **EdgeDetect** - 4 edge detection algorithms
- **Defocus** - Lens-style defocus blur
- **ZDefocus** - Depth-based defocus
- **Glow** - Highlight blooming
- **Vignette** - Edge darkening
- **Grain** - Film grain simulation
- **Denoise** - Noise reduction

### Generators
- **Constant** - Solid colors and gradients
- **Ramp** - Linear/radial gradients
- **Noise** - 10 noise algorithms (Perlin, Simplex, Worley, Turbulence, Ridged, Gaussian, Voronoi, etc.)

### Channel Operations
- **Shuffle** - Channel reordering
- **ChannelCopy** - Copy channels between layers

### 3D & Depth
- **ZMerge** - Depth-based compositing
- **Cryptomatte** - ID matte extraction

### I/O
- **LoadEXR** - Multi-channel EXR loading

**Total: 45 nodes** across all professional compositing workflows.

---

## 📖 Documentation

- **[DEVLOG.md](DEVLOG.md)** - Version history and release notes
- **[PLANNING.md](PLANNING.md)** - Project vision and architecture
- **[CLAUDE.md](CLAUDE.md)** - Development guide for AI assistants
- **[DOCS/](DOCS/)** - Detailed technical documentation
  - [NODE_PRIORITIES.md](DOCS/NODE_PRIORITIES.md) - Node priority rankings
  - [NODE_SPECIFICATIONS.md](DOCS/NODE_SPECIFICATIONS.md) - Detailed node specs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

This project follows professional VFX industry standards. When contributing:
- Follow existing code structure and style
- Add comprehensive docstrings
- Test with various image sizes and formats
- Ensure compatibility with numpy <2.0 and pillow <11.0

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by **Nuke** (Foundry) and **DaVinci Fusion** (Blackmagic Design)
- Built for the **ComfyUI** community
- References implementation details from **Natron** (open-source compositor)

## 📬 Support

- **Issues:** [GitHub Issues](https://github.com/aTanguay/ComfyUI_Detonate/issues)
- **Discussions:** [GitHub Discussions](https://github.com/aTanguay/ComfyUI_Detonate/discussions)

---

**Made with ❤️ for compositors and AI artists**
