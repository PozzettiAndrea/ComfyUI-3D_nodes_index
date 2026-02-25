# ComfyUI Custom ASCII Art Node

A powerful and enhanced ASCII art node for ComfyUI, based on FL_Ascii from ComfyUI_Fill-Nodes but completely rewritten with improved features and better usability.

![ASCII Art Examples](examples/demo_showcase.png)

## 🌟 Features

- **Multiple Character Sets**: Classic, blocks, dots, braille, minimal, extended, and custom
- **Color Preservation**: Maintain original image colors or use monochrome output
- **Advanced Controls**: Spacing, font size, contrast enhancement, and brightness inversion
- **Smart Font System**: Automatic monospace font detection with cross-platform fallbacks
- **Batch Processing**: Efficient handling of multiple images
- **Background Customization**: Configurable background colors
- **Robust Error Handling**: Graceful fallbacks and error recovery

## 🚀 Quick Start

### Installation

1. Download the latest release or clone this repository
2. Copy the `custom_ascii_node.py` file to your ComfyUI `custom_nodes` directory
3. Restart ComfyUI
4. Find the node under **"image/effects"** → **"Custom ASCII Art"**

### Basic Usage

1. Load an image using the **LoadImage** node
2. Connect it to the **Custom ASCII Art** node
3. Adjust parameters as desired
4. Connect output to **SaveImage** or **PreviewImage**

## 📋 Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **character_set** | Dropdown | "classic" | Predefined character sets |
| **custom_characters** | String | " .:-=+*#%@" | Custom character string |
| **spacing** | Integer | 8 | Distance between characters (1-50) |
| **font_size** | Integer | 12 | Size of ASCII characters (6-72) |
| **invert** | Boolean | False | Reverse brightness mapping |
| **preserve_color** | Boolean | True | Keep original image colors |
| **background_color** | String | "#000000" | Background color (hex format) |
| **contrast** | Float | 1.0 | Contrast multiplier (0.1-3.0) |

## 🎨 Character Sets

- **Classic**: ` .:-=+*#%@` - Traditional ASCII art
- **Blocks**: ` ░▒▓█` - Unicode block characters
- **Dots**: ` .·•●` - Dot-based patterns
- **Minimal**: ` .-+#` - Clean, simple characters
- **Extended**: ` .:-=+*#%@$&` - More detailed mapping
- **Braille**: ` ⠁⠃⠇⠏⠟⠿⡿⣿` - Unique braille texture
- **Custom**: User-defined character strings

## 📖 Examples

### Classic Black & White ASCII
```
Character Set: classic
Preserve Color: False
Spacing: 8
Font Size: 12
```

### Colored Unicode Blocks
```
Character Set: blocks
Preserve Color: True
Spacing: 6
Font Size: 14
Contrast: 1.5
```

### Matrix-Style Binary
```
Character Set: custom
Custom Characters: "01"
Invert: True
Background Color: "#000000"
Preserve Color: False
```

## 🔧 Technical Details

### Font Handling
The node automatically searches for monospace fonts in this order:
1. DejaVuSansMono.ttf
2. Courier.ttf
3. consola.ttf
4. System-specific paths (macOS, Linux, Windows)
5. Default PIL font (fallback)

### Performance
- Efficient tensor operations for batch processing
- Memory-optimized image handling
- Smart font caching
- Cross-platform compatibility

## 🧪 Testing

Run the included test scripts to verify functionality:

```bash
# Basic functionality test
python test_ascii_node.py

# Comprehensive feature demonstration
python ascii_comparison_demo.py
```

## 📁 Project Structure

```
comfyui-custom-ascii-node/
├── custom_nodes/
│   ├── __init__.py
│   └── custom_ascii_node.py
├── examples/
│   ├── ascii_workflow_example.json
│   └── demo_images/
├── tests/
│   ├── test_ascii_node.py
│   └── ascii_comparison_demo.py
├── docs/
│   ├── README_ASCII_NODE.md
│   └── CUSTOM_ASCII_NODE_SUMMARY.md
├── README.md
├── LICENSE_ASCII_NODE
└── setup.py
```

## 🆚 Comparison with FL_Ascii

### Improvements
✅ Simplified parameter interface  
✅ Better font fallback system  
✅ Added contrast control  
✅ More character set options  
✅ Enhanced error handling  
✅ Comprehensive documentation  
✅ Optimized code structure  

### Retained Features
✅ Color preservation  
✅ Batch processing  
✅ Spacing control  
✅ Font size control  
✅ ComfyUI compatibility  

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE_ASCII_NODE](LICENSE_ASCII_NODE) file for details.

## 🙏 Acknowledgments

- Based on FL_Ascii from [ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes)
- Inspired by the ComfyUI community
- Built for educational and creative purposes

## 📞 Support

If you encounter any issues or have questions:
1. Check the [documentation](docs/)
2. Run the test scripts to verify installation
3. Open an issue on GitHub with details about your problem

---

**Made with ❤️ for the ComfyUI community**
