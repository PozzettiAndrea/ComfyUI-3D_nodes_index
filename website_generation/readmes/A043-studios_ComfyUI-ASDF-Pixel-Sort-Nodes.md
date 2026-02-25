# ComfyUI ASDF Pixel Sort Nodes

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen)](https://github.com/comfyanonymous/ComfyUI)
[![Processing](https://img.shields.io/badge/Processing-4.3-blue)](https://processing.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](CHANGELOG.md)

A ComfyUI integration of Kim Asendorf's iconic **ASDFPixelSort** algorithm, bringing classic pixel sorting effects directly into your ComfyUI workflows.

## ✨ Features

- 🎨 **Authentic Algorithm**: Uses original Kim Asendorf ASDFPixelSort Processing script
- 🔄 **Four Sorting Modes**: White, Black, Bright, and Dark threshold-based sorting
- 🔗 **Seamless Integration**: Native ComfyUI tensor handling and workflow compatibility
- ⚙️ **Full Control**: Complete parameter customization for all sorting thresholds
- 🖥️ **Headless Ready**: Virtual display support for server environments
- 📦 **Easy Install**: Automated setup script for all dependencies

## 🚀 Quick Start

### Installation

1. **Clone this repository** into your ComfyUI custom_nodes directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/your-username/ComfyUI-ASDF-PixelSort.git
```

2. **Install dependencies** (automated):
```bash
cd ComfyUI-ASDF-PixelSort
chmod +x scripts/install.sh
sudo ./scripts/install.sh
```

3. **Restart ComfyUI** to load the new nodes

### Basic Usage

1. Add **LoadImage** node → **Pixel Sort (ASDF)** → **SaveImage**
2. Configure sorting mode and thresholds
3. Queue prompt to process

## 🎛️ Available Nodes

### Pixel Sort (ASDF)
**Location**: `Add Node` → `image` → `effects` → `Pixel Sort (ASDF)`

**Parameters**:
- **Mode**: `white` | `black` | `bright` | `dark`
- **White Threshold**: `-16777216` to `0` (default: `-12345678`)
- **Black Threshold**: `-16777216` to `0` (default: `-3456789`)
- **Bright Threshold**: `0` to `255` (default: `127`)
- **Dark Threshold**: `0` to `255` (default: `223`)

### Pixel Sort Advanced (ASDF)
**Location**: `Add Node` → `image` → `effects` → `Pixel Sort Advanced (ASDF)`

Additional features:
- Optional parameter inputs
- Custom Processing sketch path support
- Extended configuration options

## 🎨 Sorting Modes Explained

| Mode | Description | Effect |
|------|-------------|--------|
| **White** | Sorts pixels based on white threshold | Flowing, organic distortions |
| **Black** | Sorts pixels based on black threshold | Emphasizes shadows and dark regions |
| **Bright** | Sorts pixels based on brightness values | Smooth luminance gradients |
| **Dark** | Sorts pixels based on darkness values | High-contrast dramatic effects |

## 📖 Documentation

- 📋 [Installation Guide](docs/INSTALLATION.md) - Detailed setup instructions
- 🔧 [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions
- 📚 [API Reference](docs/API.md) - Complete technical documentation
- 🎯 [Examples](examples/) - Ready-to-use workflow files

## 🛠️ System Requirements

**Minimum**:
- Linux (Ubuntu 20.04+, CentOS 8+, Arch Linux)
- 4GB RAM, 2GB free storage
- Python 3.8+, Java 17+
- ComfyUI v0.3.40+

**Recommended**:
- 8GB+ RAM, SSD storage
- Multi-core processor
- GPU for ComfyUI acceleration

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md).

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### Attribution

- **Original Algorithm**: [ASDFPixelSort](http://kimasendorf.com) by Kim Asendorf (2010)
- **ComfyUI Integration**: This repository
- **Processing**: [Processing Foundation](https://processing.org)

## 🙏 Acknowledgments

- **Kim Asendorf** for the original ASDFPixelSort algorithm
- **ComfyUI Community** for the excellent framework
- **Processing Foundation** for the creative coding platform
- **Contributors** who help improve this project

---

<div align="center">

**Made with ❤️ for the ComfyUI community**

[⭐ Star this repo](https://github.com/your-username/ComfyUI-ASDF-PixelSort) • [🐛 Report Bug](https://github.com/your-username/ComfyUI-ASDF-PixelSort/issues) • [💡 Request Feature](https://github.com/your-username/ComfyUI-ASDF-PixelSort/issues)

</div>
