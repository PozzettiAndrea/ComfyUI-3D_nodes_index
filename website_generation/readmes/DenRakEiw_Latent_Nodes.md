# ComfyUI Latent Color Tools

A collection of powerful nodes for color manipulation and image adjustments directly in the latent space, providing faster and more efficient processing compared to traditional image-based operations.

## 🚀 Features

### 🎨 Latent Color Match
Advanced color matching between latents using multiple algorithms:
- **Cubiq-based methods** with kornia color space conversions (LAB, YCbCr, LUV, YUV, XYZ, RGB)
- **Advanced algorithms** using color-matcher library (hm-mkl-hm, mkl, hm, reinhard, mvgd, hm-mvgd-hm)
- **Real-time processing** directly in latent space
- **Batch processing** support for efficiency

### 🎛️ Latent Image Adjust
Complete image adjustment suite working in latent space:
- **Brightness** (-1.0 to 1.0) - Additive brightness adjustment
- **Contrast** (0.0 to 3.0) - Multiplicative contrast around mean
- **Hue** (-180° to 180°) - Color tone shifting with HSV conversion
- **Saturation** (0.0 to 3.0) - Color intensity adjustment
- **Sharpness** (0.0 to 3.0) - Unsharp masking and blur effects

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "Latent Color Tools" in the manager
3. Install and restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ComfyUI-Latent-Color-Tools.git
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-Latent-Color-Tools
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## 🎯 Usage

### Latent Color Match
1. Add the "🎨 Latent Color Match" node to your workflow
2. Connect your source and reference latents
3. Choose a color matching method:
   - **LAB**: Best for natural color matching
   - **hm-mkl-hm**: Highest quality (requires color-matcher)
   - **YCbCr**: Good for skin tones
   - **RGB**: Direct channel matching
4. Adjust the factor (0.0-3.0) to control the effect strength

### Latent Image Adjust
1. Add the "🎛️ Latent Image Adjust" node to your workflow
2. Connect your latent input
3. Adjust parameters as needed:
   - **Brightness**: Negative values darken, positive brighten
   - **Contrast**: Values < 1.0 reduce contrast, > 1.0 increase
   - **Hue**: Shift color tone in degrees
   - **Saturation**: 0.0 = grayscale, > 1.0 = more vibrant
   - **Sharpness**: < 1.0 = blur, > 1.0 = sharpen

## 🔧 Technical Details

### Dependencies
- **kornia** (>= 0.6.0) - For advanced color space conversions
- **color-matcher** (>= 0.2.0) - For professional color matching algorithms
- **torch** - PyTorch (included with ComfyUI)
- **numpy** - Numerical operations (included with ComfyUI)

### Performance Benefits
- **No VAE encoding/decoding** - Works directly with latents
- **GPU accelerated** - Full CUDA support
- **Batch processing** - Efficient handling of multiple samples
- **Memory efficient** - Lower VRAM usage compared to image operations

### Supported Tensor Shapes
- 4D tensors: `[batch, channels, height, width]`
- 5D tensors: `[batch, channels, 1, height, width]` (automatically handled)
- Any number of channels (RGB-like processing for first 3 channels)

## 📊 Comparison with Image-based Methods

| Feature | Latent Space | Image Space |
|---------|-------------|-------------|
| Speed | ⚡ Fast | 🐌 Slow |
| Memory Usage | 💾 Low | 📈 High |
| Quality Loss | ✅ None | ❌ VAE artifacts |
| Integration | 🔄 Seamless | 🔀 Requires conversion |

## 🎨 Color Matching Methods

### Cubiq-based (with kornia)
- **LAB**: Perceptually uniform color space, best for natural images
- **YCbCr**: Separates luminance from chrominance, good for skin tones
- **LUV**: Alternative perceptual color space
- **YUV**: Broadcast standard color space
- **XYZ**: CIE standard color space
- **RGB**: Direct RGB channel matching

### Advanced (with color-matcher)
- **hm-mkl-hm**: Histogram + Monge-Kantorovich + Histogram (highest quality)
- **mkl**: Monge-Kantorovich Linearization
- **hm**: Classical Histogram Matching
- **reinhard**: Reinhard et al. method
- **mvgd**: Multi-Variate Gaussian Distribution
- **hm-mvgd-hm**: HM + MVGD + HM compound

## 🐛 Troubleshooting

### Common Issues

**"Kornia not available" warning**
```bash
pip install kornia>=0.6.0
```

**"Color-matcher not available" warning**
```bash
pip install color-matcher>=0.2.0
```

**Tensor shape errors**
- The nodes automatically handle 4D and 5D tensors
- If you encounter shape issues, check your latent source

**Weak effects**
- Increase the factor parameter (try 1.5-3.0)
- Some methods work better with specific content types

## 📝 Changelog

### v1.0.0
- Initial release
- Latent Color Match with multiple algorithms
- Latent Image Adjust with 5 adjustment types
- Full kornia and color-matcher integration
- Automatic tensor shape handling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [cubiq](https://github.com/cubiq) for the original ImageColorMatch implementation
- [kornia](https://github.com/kornia/kornia) team for excellent computer vision library
- [color-matcher](https://github.com/hahnec/color-matcher) for professional color matching algorithms
- ComfyUI community for the amazing platform

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ComfyUI-Latent-Color-Tools/issues) page
2. Create a new issue with detailed description
3. Include your ComfyUI version and error logs

---

**Made with ❤️ for the ComfyUI community**
