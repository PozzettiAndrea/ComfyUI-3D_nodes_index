# ComfyUI Blind Watermark

[English](README.md) | [中文文档](README_cn.md)

A powerful blind watermark plugin for ComfyUI that allows you to embed and extract invisible watermarks in images using frequency domain techniques (DWT-DCT-SVD).

This project is based on https://github.com/guofei9987/blind_watermark.git Production, thank you for the big shot's open source



## Features

- 🔒 **Invisible Watermarks**: Embed watermarks that are imperceptible to the human eye
- 📝 **Text Watermarks**: Embed and extract text messages
- 🖼️ **Image Watermarks**: Embed and extract image watermarks
- 📲 **QR Code Support**: Generate and decode QR codes for advanced watermarking
- 🛡️ **Robust**: Resistant to common image manipulations (rotation, cropping, scaling, compression)
- ⚙️ **Advanced Controls**: Fine-tune embedding strength, DCT coefficients, and processing modes
- 🎨 **ComfyUI Integration**: Seamless workflow integration with native node support

## Installation

### 1. Install the Plugin

Navigate to your ComfyUI custom nodes directory and clone this repository:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/TianDongL/Blind_watermark_Comfyui.git
```

### 2. Install Dependencies

Install the required Python packages:

```bash
cd Comfyui_blind_watermark
pip install -r requirements.txt
```

**Required packages:**
- `blind-watermark` - Core watermarking library
- `qrcode` - QR code generation
- `pillow` - Image processing
- `pyzbar` (optional) - QR code decoding

### 3. Restart ComfyUI

Restart ComfyUI to load the new nodes.

## Available Nodes

### Watermark Nodes

1. **📝 Embed Text Watermark**
   - Embeds invisible text into images
   - Configurable embedding strength (d1, d2)
   - Supports multiple DCT coefficient modes

2. **📖 Extract Text Watermark**
   - Extracts embedded text from watermarked images
   - Requires matching password and length parameters
   - Provides detailed extraction info

3. **🖼️ Embed Image Watermark**
   - Embeds an invisible image watermark into another image
   - Supports PNG, JPEG, and other formats
   - Configurable alpha blending

4. **🔍 Extract Image Watermark**
   - Extracts embedded image watermarks
   - Requires watermark dimensions (width × height)
   - Outputs extracted watermark as image tensor

### QR Code Nodes

5. **📲 Generate QR Code**
   - Creates QR codes from text/URLs
   - Adjustable size and error correction levels
   - Outputs as image tensor for further processing

6. **🔍 Decode QR Code**
   - Decodes QR codes from images
   - Automatic detection and extraction
   - Returns decoded text/URL

## Quick Start Guide

### Example 1: Text Watermark Workflow

**Embed Text:**
1. Load your image using "Load Image" node
2. Add "📝 Embed Text Watermark" node
3. Connect the image and enter:
   - **Watermark Text**: "Copyright 2025"
   - **Password**: 12345
   - **d1/d2**: Use defaults (36/20) or adjust
4. Save the watermarked image

**Extract Text:**
1. Load the watermarked image
2. Add "📖 Extract Text Watermark" node
3. Enter the same password and text length
4. View extracted text in output

### Example 2: Image Watermark Workflow

**Embed Image:**
1. Load the original image
2. Load your watermark/logo image
3. Add "🖼️ Embed Image Watermark" node
4. Connect both images
5. Set password and embedding strength
6. Save the result

**Extract Image:**
1. Load the watermarked image
2. Add "🔍 Extract Image Watermark" node
3. Enter password and watermark dimensions
4. View extracted watermark

### Example 3: QR Code Watermark

1. Generate a QR code with "📲 Generate QR Code"
2. Use it as watermark with "🖼️ Embed Image Watermark"
3. Extract and decode with "🔍 Extract Image Watermark" → "🔍 Decode QR Code"

## Parameters Explained

### Password Parameters
- **password_img**: Password for image encryption (integer)
- **password_wm**: Password for watermark encryption (integer)
- Both passwords must match between embed and extract operations

### Embedding Strength (d1/d2)
- **d1**: Controls frequency coefficient range (default: 36)
- **d2**: Controls embedding strength (default: 20)
- **Higher values** = stronger watermark, more visible
- **Lower values** = weaker watermark, more invisible
- Recommended: d1=36, d2=20 for balanced results

### DCT Coefficient Modes
- **Mode 1**: Uses fewer coefficients (faster, less robust)
- **Mode 2**: Uses more coefficients (slower, more robust)
- **Mode 3**: Uses even more coefficients (slowest, most robust)

### Processing Modes
- **Single Process**: Standard processing
- **Multi-core**: Parallel processing for faster embedding
- **All Cores**: Uses all available CPU cores

## Watermark Robustness

This watermark technique is resistant to:

| Attack Type | Robustness | Notes |
|------------|-----------|--------|
| 🔄 Rotation | ⭐⭐⭐⭐ | Survives moderate rotation |
| ✂️ Cropping | ⭐⭐⭐⭐⭐ | Highly resistant |
| 📏 Scaling | ⭐⭐⭐⭐⭐ | Survives resize operations |
| 🎭 Masking | ⭐⭐⭐⭐ | Partial watermark still recoverable |
| 📦 Compression | ⭐⭐⭐⭐ | Survives JPEG compression |
| 🌈 Brightness/Contrast | ⭐⭐⭐⭐⭐ | Unaffected by color adjustments |
| 🔊 Noise | ⭐⭐⭐ | Moderate resistance |

## Tips & Best Practices

### For Best Results:

1. **Password Management**
   - Use the same passwords for embedding and extraction
   - Record passwords securely
   - Higher passwords = more security

2. **Watermark Length**
   - Keep text watermarks concise (< 100 characters)
   - Longer watermarks require larger images
   - Note the reported `wm_bit_length` after embedding

3. **Image Quality**
   - Use high-resolution images (minimum 512×512)
   - Avoid heavily compressed images as input
   - Save watermarked images in lossless formats (PNG)

4. **Embedding Strength**
   - Start with defaults (d1=36, d2=20)
   - Increase d2 if extraction fails
   - Decrease d2 if watermark is visible

5. **Image Watermarks**
   - Use simple, high-contrast watermark images
   - Recommended watermark size: 64×64 or 128×128
   - Black and white logos work best

## Troubleshooting

### Watermark Extraction Failed

**Problem**: Extracted text is garbled or empty

**Solutions:**
- ✅ Verify passwords match exactly
- ✅ Check `wm_bit_length` parameter
- ✅ Ensure image hasn't been re-encoded multiple times
- ✅ Try increasing embedding strength (d2)
- ✅ Use the same DCT mode for embed/extract

### Watermark Visible in Image

**Problem**: Watermark creates visible artifacts

**Solutions:**
- ✅ Reduce d2 parameter (e.g., from 20 to 15)
- ✅ Use a smaller watermark
- ✅ Ensure input image is high quality

### Node Not Appearing

**Problem**: Nodes don't show up in ComfyUI

**Solutions:**
- ✅ Check `requirements.txt` packages are installed
- ✅ Restart ComfyUI completely
- ✅ Check console for error messages
- ✅ Verify folder is in `ComfyUI/custom_nodes/`

## Technical Details

This plugin uses frequency domain watermarking based on:
- **DWT** (Discrete Wavelet Transform)
- **DCT** (Discrete Cosine Transform)
- **SVD** (Singular Value Decomposition)

The watermark is embedded in the frequency domain, making it invisible to the human eye while being detectable with the correct password.

## Credits

Based on the excellent [blind_watermark](https://github.com/guofei9987/blind_watermark) library by [@guofei9987](https://github.com/guofei9987).

## Related Projects

- **blind_watermark**: [https://github.com/guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)
- **Text Blind Watermark**: [https://github.com/guofei9987/text_blind_watermark](https://github.com/guofei9987/text_blind_watermark)
- **HideInfo**: [https://github.com/guofei9987/HideInfo](https://github.com/guofei9987/HideInfo)

## License

This project follows the original blind_watermark library license. Please refer to the LICENSE file for details.

## Support & Contribution

- 🐛 **Bug Reports**: Open an issue on GitHub
- 💡 **Feature Requests**: Open an issue with your suggestion
- 🔧 **Pull Requests**: Contributions are welcome!

---

**Happy Watermarking! 🎨🔒**
