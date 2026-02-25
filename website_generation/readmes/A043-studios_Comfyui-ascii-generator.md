# ComfyUI ASCII Generator Node

A powerful ComfyUI custom node that converts images to ASCII art with multi-language character set support. Based on the excellent [ASCII-generator](https://github.com/vietnh1009/ASCII-generator) by vietnh1009.

![ASCII Generator Demo](assets/demo.png)

## Features

🎨 **Multi-Language ASCII Art**
- English, Chinese, Japanese, Korean, Russian, German character sets
- Simple and complex ASCII character mappings
- Customizable output density and style

🖼️ **Dual Output Format**
- ASCII Art Image: Visual representation with customizable background
- ASCII Text: Raw text output for further processing

⚙️ **Flexible Parameters**
- Adjustable column count (10-500)
- Multiple character sets
- Black/white background options
- Configurable font sizes

🔧 **ComfyUI Integration**
- Native tensor support
- Batch processing capability
- Error handling and fallbacks

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "ASCII Generator"
3. Click Install

### Method 2: Manual Installation
1. Clone this repository to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/YOUR_USERNAME/comfyui-ascii-generator.git
```

2. Install dependencies:
```bash
cd comfyui-ascii-generator
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

### Basic Workflow
1. **Load Image**: Connect any image source to the ASCII Generator node
2. **Configure Parameters**:
   - `num_cols`: Number of ASCII columns (affects detail level)
   - `language`: Character set to use
   - `background`: Black or white background
   - `font_size`: Size of characters in output image
3. **Generate**: The node outputs both an ASCII image and text

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image` | IMAGE | - | Input image to convert |
| `num_cols` | INT | 100 | Number of ASCII columns (10-500) |
| `language` | COMBO | simple | Character set selection |
| `background` | COMBO | black | Background color (black/white) |
| `font_size` | INT | 12 | Font size for ASCII image (6-48) |

### Character Sets

- **simple**: `@%#*+=-:. ` - Basic ASCII characters
- **complex**: Full ASCII character set with symbols
- **english**: `AaBbCc...` - English alphabet
- **chinese**: Chinese characters for unique artistic effects
- **korean**: Korean Hangul characters
- **japanese**: Japanese Hiragana characters
- **russian**: Cyrillic alphabet
- **german**: German alphabet with umlauts

## Examples

### Simple ASCII Art
```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@####################%@@@@@@@@@
@@@@@@@@@@                    +@@@@@@@@@
@@@@@@@@@@                    +@@@@@@@@@
```

### Complex ASCII Art
```
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$wU\<l     <[rU*$$$$$$$$$$$$
$$$$$$$$$$Z{                :rW$$$$$$$$$
$$$$$$$$n"    !_)\nnnnj\[<^    <k$$$$$$$
```

### Gradient Mapping
```
.....::::-----====++++*****####%%%%%@@@@
.`^,;l!>~+-]}{)|/tjxnvzYUCQOZwpdka*#W8B@
```

## Technical Details

### Algorithm
The node uses brightness-based character mapping:
1. **Image Processing**: Converts input to grayscale
2. **Cell Division**: Divides image into character-sized cells
3. **Brightness Analysis**: Calculates average brightness per cell
4. **Character Mapping**: Maps brightness to character density
5. **Output Generation**: Creates both image and text outputs

### Character Sorting
Characters are automatically sorted by visual density using PIL font rendering to ensure optimal brightness-to-character mapping.

## Compatibility

- **ComfyUI**: Latest version
- **Python**: 3.8+
- **Dependencies**: torch, numpy, Pillow

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
```bash
git clone https://github.com/YOUR_USERNAME/comfyui-ascii-generator.git
cd comfyui-ascii-generator
pip install -r requirements.txt
python test_ascii_generator.py
```

## Credits

- Original ASCII generation algorithm by [vietnh1009](https://github.com/vietnh1009/ASCII-generator)
- ComfyUI integration and enhancements
- Generated using the [MCP ComfyUI Framework](https://github.com/A043-studios/mcp-comfyui-framework)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0
- Initial release
- Multi-language character set support
- Dual output format (image + text)
- ComfyUI tensor compatibility
- Configurable parameters

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/comfyui-ascii-generator/issues) page
2. Create a new issue with detailed description
3. Include your ComfyUI version and error logs

---

**Made with ❤️ for the ComfyUI community**
