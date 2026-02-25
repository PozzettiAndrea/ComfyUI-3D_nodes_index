# ComfyUI PK Load Image Paste

A ComfyUI custom node that extends the standard Load Image functionality with a convenient "Paste from clipboard" button. This allows you to directly paste images from your clipboard without workflow conflicts, ensuring only images are pasted.

## Features

- **Enhanced Load Image Node**: All standard Load Image functionality
- **Clipboard Integration**: Direct paste from clipboard with a single button click
- **Conflict Prevention**: Avoids workflow pasting conflicts by specifically handling images

## Requirements

- ComfyUI
- Modern web browser with Clipboard API support (Chrome, Firefox, Safari, Edge)

## Installation

### Manual Installation via Git

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/smbdsbrain/ComfyUI-PK_load_image_paste.git
   ```

3. Restart ComfyUI

The node will appear in your node menu under the "image" category as **"Paste Image (Load) — PK"**.

## Usage

### Basic Usage

1. Add the **"Paste Image (Load) — PK"** node to your workflow
2. You can use it in two ways:
   - **Manual path entry**: Type or paste an image path in the text field
   - **Clipboard paste**: Click the "Paste from clipboard" button

### Clipboard Paste Feature

1. Copy an image to your clipboard (from any application, screenshot tool, etc.)
2. In ComfyUI, click the **"Paste from clipboard"** button on the node
3. The image will be automatically:
   - Uploaded to the `ComfyUI/input/pasted/` directory
   - Named with timestamp (e.g., `paste_1634567890123.png`)
   - Loaded into the node automatically

### Path Formats

The node accepts various path formats:

- **Relative to input directory**: `image.png` or `subfolder/image.png`
- **Input directory explicit**: `input/image.png`
- **Pasted images**: `pasted/paste_1634567890123.png` (automatically set when using clipboard)
- **Absolute paths**: `/full/path/to/image.png` (advanced usage)

## Output

The node provides two outputs:
- **IMAGE**: The loaded image tensor
- **MASK**: Alpha channel mask (if present) or empty mask

## Browser Compatibility

The clipboard paste feature requires a modern browser with Clipboard API support:

- ✅ Chrome 76+
- ✅ Firefox 90+
- ✅ Safari 13.1+
- ✅ Edge 79+

## Troubleshooting

### "Clipboard API not available" Error
- Check if your browser supports the Clipboard API
- Try refreshing the page

### "No image in clipboard" Error
- Make sure you've copied an image (not text or other content)
- Try copying the image again
- Some applications may not properly copy images to clipboard

### "Upload failed" Error
- Check ComfyUI server logs for detailed error information
- Ensure ComfyUI has write permissions to the input directory
- Verify disk space availability

### Image Not Found
- Check the file path is correct
- Ensure the image file exists in the specified location
- For relative paths, files should be in the `ComfyUI/input/` directory

## Technical Details

- **Backend**: Python node that extends standard image loading with flexible path handling
- **Frontend**: JavaScript extension that adds clipboard functionality via Clipboard API
- **File Storage**: Pasted images are stored in `ComfyUI/input/pasted/` directory
- **Supported Formats**: All formats supported by PIL/Pillow (PNG, JPEG, GIF, BMP, etc.)

## License

This project is licensed under the WTFPL (Do What The F*ck You Want To Public License).

## Contributing

Feel free to submit issues, feature requests, or pull requests on GitHub.

## Version

Current version: v7