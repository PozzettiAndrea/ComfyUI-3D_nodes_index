# ComfyUI Load Image From URL

A ComfyUI custom node that allows you to load images directly from URLs or local file paths. This node provides a convenient way to import images into your ComfyUI workflows without manually downloading them first.

## Features

- Load images from HTTP/HTTPS URLs
- Load images from local file paths
- Supports multiple image formats (PNG, JPG, JPEG, GIF, etc.)
- Returns both image and mask outputs
- Handles animated images (GIF) by extracting frames
- Automatic EXIF orientation correction
- Alpha channel support with mask extraction

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/papcorns/ComfyUI-load-image-from-url.git
```

2. Install the required dependencies:
```bash
cd ComfyUI-load-image-from-url
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

You can find this node in the **"🍿PapcornsNodes"** category in ComfyUI.

### Node Inputs
- **url_or_path**: A string input that accepts either:
  - HTTP/HTTPS URLs (e.g., `https://example.com/image.png`)
  - Local file paths (e.g., `/path/to/your/image.jpg`)

### Node Outputs
- **IMAGE**: The loaded image as a tensor
- **MASK**: Alpha channel mask (if present) or empty mask

### Example Workflow

![Node Example](https://i.postimg.cc/XY0CLx3Q/image.png)

```json
{
  "1": {
    "inputs": {
      "url_or_path": "https://i.postimg.cc/TYbdk63X/test.png"
    },
    "class_type": "LoadImageFromUrlOrPath",
    "_meta": {
      "title": "LoadImageFromUrlOrPath"
    }
  },
  "2": {
    "inputs": {
      "images": [
        "1",
        0
      ]
    },
    "class_type": "PreviewImage",
    "_meta": {
      "title": "Preview Image"
    }
  }
}
```

## Requirements

- ComfyUI
- Python 3.7+
- See `requirements.txt` for Python package dependencies

## Supported Image Formats

- PNG
- JPEG/JPG
- GIF (animated and static)
- BMP
- TIFF
- WebP
- And other formats supported by PIL/Pillow

## Error Handling

The node will handle common errors gracefully:
- Invalid URLs
- Network timeouts
- Unsupported file formats
- Missing local files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source. Please check the license file for more details.

## Changelog

### v1.0.0
- Initial release
- Support for URL and local path loading
- Basic image processing and mask extraction
