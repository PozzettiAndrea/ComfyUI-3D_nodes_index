# ComfyUI Universal Image Loader

A powerful and versatile custom node for ComfyUI that provides multiple ways to load images into your workflows.

## 🌟 Features

### Multiple Input Methods
- **📁 File Path**: Load images from your local file system using ComfyUI's file picker
- **📋 Base64**: Paste base64-encoded image strings directly into the node

### Smart Input Handling
- **Input Precedence**: When multiple inputs are provided (especially via API), the node follows a clear precedence order
- **Auto-clearing**: When you use one input method, other inputs are automatically cleared for clarity
- **Visual Feedback**: Real-time preview and status indicators for loaded images
- **Error Recovery**: Robust error handling with informative logging

### Advanced Features
- **EXIF Rotation**: Automatically applies correct image orientation based on EXIF data
- **Alpha Channel Support**: Properly extracts and processes alpha channels as masks
- **Memory Management**: Efficient GPU memory handling with automatic cleanup
- **Format Support**: Works with PNG, JPEG, GIF, WebP, BMP, and other common formats

## 📦 Installation

### Method 1: Git Clone (Recommended)
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/comfyui-imgloader.git
```

### Method 2: Manual Download
1. Download this repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/comfyui-imgloader/`
3. Restart ComfyUI

### Method 3: ComfyUI Manager
Search for "Universal Image Loader" in ComfyUI Manager and install.

## 🚀 Usage

### Basic Usage
1. Add the node to your workflow: `Add Node` → `image` → `loaders` → `Image Loader (Universal)`
2. Choose your preferred input method:
   - **File Path**: Click the file selector and choose an image
   - **Base64**: Paste a base64 string into the text area

### Input Methods Details

#### 📁 File Path Input
- Uses ComfyUI's standard file picker
- Supports relative paths (resolved to `ComfyUI/input/` directory)
- Validates file existence and readability

#### 📋 Base64 Input
- Accepts both raw base64 strings and data URLs
- Supports format: `data:image/png;base64,iVBORw0KGgo...`
- Or raw base64: `iVBORw0KGgoAAAANSUhEUgAA...`
- Validates base64 format before processing

### API Usage

When using the ComfyUI API, you can provide multiple inputs. The node follows this precedence order:

1. **File Path** (highest priority)  
2. **Base64 String** (lowest priority)

Example API payload:
```json
{
  "inputs": {
    "filepath": "my_image.png",
    "base64": "iVBORw0KGgoAAAANSUhEUgA..."
  }
}
```

In this case, the `filepath` input would be used.

## 🔧 Output

The node provides two outputs:
- **IMAGE**: Standard ComfyUI image tensor (NHWC format, float32, range 0-1)
- **MASK**: Alpha channel mask or fully opaque mask if no alpha is present

## ⚙️ Configuration

### Environment Variables
You can set these environment variables to customize behavior:

```bash
# Enable debug logging
export COMFYUI_IMGLOADER_DEBUG=1

# Set custom input directory (overrides ComfyUI default)
export COMFYUI_IMGLOADER_INPUT_DIR="/path/to/custom/input"
```

### Node Settings
The node automatically detects and handles:
- Image format and color space
- EXIF orientation data
- Alpha channel presence
- File path resolution

## 🛠️ Development

### Project Structure
```
comfyui-imgloader/
├── __init__.py              # Node registration
├── imgloader_node.py        # Main Python implementation
├── js/
│   └── imgloader.js         # Frontend JavaScript
├── .github/
│   └── copilot-instructions.md
├── .vscode/
│   └── tasks.json
└── README.md
```

### Key Components

#### Python Backend (`imgloader_node.py`)
- Image loading and processing logic
- Tensor format conversion
- Error handling and validation
- Memory management

#### JavaScript Frontend (`js/imgloader.js`)
- UI state management
- Visual feedback

### Adding Features
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Test with ComfyUI
5. Submit a pull request

## 🐛 Troubleshooting

### Common Issues

#### "No valid image source found"
- Ensure your image file exists and is readable
- Check that base64 strings are properly formatted

#### Large images causing memory issues
- The node automatically manages GPU memory
- For very large images, consider resizing before input
- Monitor ComfyUI console for memory warnings

#### File path not found
- Relative paths are resolved to `ComfyUI/input/` directory
- Use absolute paths for files outside the input directory
- Check file permissions and accessibility

### Debug Mode
Enable debug logging by setting the environment variable:
```bash
export COMFYUI_IMGLOADER_DEBUG=1
```

This will provide detailed information about:
- Image loading operations
- Input precedence decisions
- Error details and stack traces
- Memory usage information

## 📋 Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- PIL/Pillow
- PyTorch
- NumPy

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Clone the repository
2. Install in development mode: `pip install -e .`
3. Make your changes
4. Test with ComfyUI
5. Submit a pull request

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/comfyui-imgloader/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/comfyui-imgloader/discussions)
- **ComfyUI Discord**: Find us in the #custom-nodes channel

## 🔄 Changelog

### v1.0.0
- Initial release
- File path and base64 support
- Visual feedback and preview
- Robust error handling
- Memory management
- EXIF rotation support
- Alpha channel processing

---

Made with ❤️ for the ComfyUI community
