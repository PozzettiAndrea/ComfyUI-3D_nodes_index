# ComfyUI-ATk-Nodes

**Ambrosinus ToolKit** - A streamlined workflow export plugin for ComfyUI

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-orange.svg)

> **📢 Status Update**: ATk-Nodes is currently pending approval in ComfyUI Manager. 
> For now, please use **git clone** or **manual installation**. We'll update this notice once it's available in the Manager!

## ✨ Features

### 🎯 **Streamlined Workflow Export**
- **Simple Context Menu Access**: Right-click → "⚗️ ATk Menu" → "🎨 Workflow Export"
- **Intuitive Modal Dialog**: Clean, modern interface with all options in one place
- **Multiple Export Formats**: PNG, JPG, WebP with embedded workflow metadata
- **Smart Scaling**: 1x, 2x, 3x, 4x resolution options with perfect text rendering
- **Professional Results**: Clean, scalable workflow images for documentation and sharing

### 🎨 **Built-in Professional Themes**
- **ATk Dark (Transparent)**: Modern dark theme optimized for transparent exports
- **ATk Light (Transparent)**: Clean light theme with transparency support
- **Auto-Installation**: Themes are automatically installed and registered in ComfyUI
- **Smart Theme Detection**: Automatically finds and applies existing transparent themes

### 📐 **Export Capabilities**
- **Custom Resolution**: Choose from 1x to 4x zoom levels for high-DPI displays
- **Transparent Background**: Professional transparent exports with theme support
- **Custom Filenames**: Set meaningful names for your exported files
- **Workflow Embedding**: Workflow data automatically embedded in PNG files for easy sharing
- **Format Optimization**: Each format optimized for its best use case

### 💡 **Technical Highlights**
- **Perfect Text Rendering**: Renders at native resolution then scales for crisp text at any size
- **Non-Destructive**: Temporarily applies export settings without affecting your workspace
- **Zero Dependencies**: No external requirements, works out of the box
- **Universal Compatibility**: Works with all ComfyUI distributions and modern browsers

## 🚀 Installation

### Method 1: ComfyUI Manager (Coming Soon)
*ATk-Nodes is currently pending approval in ComfyUI Manager. Check back in a few days!*

1. **Open ComfyUI Manager**
2. **Search for "ATk-Nodes"**
3. **Click Install**
4. **Restart ComfyUI**

### Method 2: Git Clone (Recommended - Available Now)

**📋 Quick Copy-Paste Commands:**

**For Windows:**
```cmd
cd C:\path\to\ComfyUI\custom_nodes
git clone https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes.git
```

**For Mac/Linux:**
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes.git
```

**Step-by-step:**

1. **Navigate to your ComfyUI custom_nodes directory:**
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes.git
   ```

3. **Restart ComfyUI**
   - The plugin will automatically install and register ATk themes

### Method 3: Manual Download

1. **Download the ZIP file** from the [Releases page](https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes/releases)

2. **Extract to your ComfyUI custom_nodes folder:**
   ```
   ComfyUI/
   └── custom_nodes/
       └── ComfyUI-ATk-Nodes/
           ├── __init__.py
           ├── install.py
           ├── web/
           │   └── atk_workflow_export.js
           └── themes/
               ├── ATk_dark_theme.json
               └── ATk_light_theme.json
   ```

3. **Restart ComfyUI**

## 📖 Usage

### Basic Workflow Export

1. **Right-click** anywhere on the ComfyUI canvas (not on a node)
2. **Select** "⚗️ ATk Menu" → "🎨 Workflow Export"
3. **Configure your export options:**
   - **Format**: Choose PNG, JPG, or WebP
   - **Filename**: Enter your desired filename
   - **Resolution**: Select zoom level (1x-4x)
   - **Transparent Background**: Check for transparency support
4. **Click Export**

### Advanced Features

#### **Transparent Background Export**
- ✅ Enable "Transparent Background" checkbox
- 🎨 Choose your ATk theme:
  - **Auto-detect**: Finds existing transparent themes in your ComfyUI
  - **ATk Dark**: Uses built-in dark transparent theme
  - **ATk Light**: Uses built-in light transparent theme
- 🖼️ Export with professional transparent background

#### **High-Resolution Export**
- 📐 Select 2x, 3x, or 4x for presentations and high-DPI displays
- 🔤 Text remains perfectly crisp at all resolutions
- 📊 Ideal for documentation, tutorials, and professional presentations

#### **Format Selection Guide**
- **PNG**: Best for transparency, includes embedded workflow data, highest quality
- **JPG**: Smaller file sizes, no transparency (automatically converts to white background)
- **WebP**: Modern format with good compression and transparency support

## 🎨 ATk Themes

ATk-Nodes includes two professionally designed themes optimized for clean workflow exports:

### ATk Dark (Transparent)
- 🌙 Modern dark color scheme with high contrast
- 🔍 Transparent background for flexible integration
- 📖 Optimized for readability and professional appearance
- 🎯 Perfect for light backgrounds in presentations

### ATk Light (Transparent)
- ☀️ Clean, minimalist light interface
- 📋 Transparent background for versatile use
- 💼 Professional appearance for business contexts
- 🎯 Ideal for technical documentation and tutorials

**Note**: Themes are automatically installed to `ComfyUI/user/color_palettes/` and registered in ComfyUI settings on first launch.

## 🔧 Technical Details

### Requirements
- ComfyUI (any recent version)
- Modern web browser with HTML5 Canvas support
- No additional dependencies required

### Compatibility
- ✅ ComfyUI Standard
- ✅ ComfyUI Portable
- ✅ All major operating systems (Windows, macOS, Linux)
- ✅ All modern browsers (Chrome, Firefox, Safari, Edge)

### File Structure
```
ComfyUI-ATk-Nodes/
├── __init__.py                 # Main plugin initialization
├── install.py                  # Automatic theme installation
├── requirements.txt            # Dependencies (empty - no requirements)
├── README.md                   # This documentation
├── LICENSE                     # MIT License
├── web/
│   └── atk_workflow_export.js  # Main export functionality
└── themes/
    ├── ATk_dark_theme.json     # Dark transparent theme
    └── ATk_light_theme.json    # Light transparent theme
```

## 🔍 Troubleshooting

### Common Issues

**Q: I don't see "ATk Menu" when I right-click**
- **A**: Make sure to right-click on the canvas background, not on a node. The menu appears in the context menu.

**Q: Themes not appearing in ComfyUI**
- **A**: Restart ComfyUI after installation. Themes auto-install on first load.

**Q: Export dialog not opening**
- **A**: Check the browser console (F12) for any JavaScript errors and report them in the Issues section.

**Q: Transparent background not working**
- **A**: Enable the "Transparent Background" checkbox and select an ATk theme. PNG format is recommended for best transparency support.

**Q: Text looks blurry in high-resolution exports**
- **A**: This is the intended behavior - ATk-Nodes renders at native resolution then scales to maintain text sharpness.

### Debug Information
Enable browser console (F12) to see detailed logging:
- Theme registration status
- Export process steps  
- Error messages with details

## 🤝 Contributing

Contributions are welcome! This is my first ComfyUI plugin, so I appreciate feedback from the community.

### How to Contribute
1. **Fork** the repository
2. **Clone** your fork to `ComfyUI/custom_nodes/`
3. **Make** your changes
4. **Test** thoroughly with different ComfyUI setups
5. **Submit** a pull request with a clear description

### Reporting Issues
When reporting bugs, please include:
- ComfyUI version and distribution (standard/portable)
- Browser information (Chrome, Firefox, etc.)
- Operating system
- Steps to reproduce the issue
- Console error messages (F12 → Console)
- Screenshots if applicable

### Feature Requests
Have ideas for improvements? Open an issue with the `enhancement` label and describe:
- What problem it would solve
- How you envision it working
- Any technical considerations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ComfyUI Team** for creating an amazing and extensible platform
- **ComfyUI Community** for inspiration, feedback, and support
- **Early Testers** who provided valuable feedback during development
- **Open Source Contributors** who make projects like this possible

## 💬 Support & Community

- **🐛 Bug Reports**: [GitHub Issues](https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes/issues)
- **💡 Feature Requests**: [GitHub Issues](https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes/issues) with `enhancement` label
- **🗣️ General Discussion**: [GitHub Discussions](https://github.com/lucianoambrosini/ComfyUI-ATk-Nodes/discussions)
- **📖 Documentation**: This README and inline code comments

### Stay Connected
- **🏷️ Tag your exports**: Use `#ATkNodes` when sharing your workflow exports
- **⭐ Star the repo**: If you find this plugin useful, please consider giving it a star
- **🔄 Share feedback**: Your experience helps improve the plugin for everyone

---

**Created with ❤️ by Luciano Ambrosini (Ambrosinus)**

*ATk-Nodes is my first contribution to the ComfyUI ecosystem. It started as a simple tool to create clean workflow documentation and evolved into something the community might find useful. Thank you for trying it out!*

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/lucianoambrosini/ComfyUI-ATk-Nodes)
![GitHub issues](https://img.shields.io/github/issues/lucianoambrosini/ComfyUI-ATk-Nodes)
![GitHub forks](https://img.shields.io/github/forks/lucianoambrosini/ComfyUI-ATk-Nodes)
![GitHub last commit](https://img.shields.io/github/last-commit/lucianoambrosini/ComfyUI-ATk-Nodes)
