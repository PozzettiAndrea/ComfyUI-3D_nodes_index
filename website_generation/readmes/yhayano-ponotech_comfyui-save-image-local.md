English | [日本語](./README_ja.md)

# ComfyUI Local Save Node

This is a custom node for ComfyUI that allows you to directly download generated images to your local PC.

## Features

- Directly save images generated in ComfyUI to your local PC
- Supports downloading in PNG or JPEG format
- Customizable file name prefix
- Automatic generation of file names including timestamps and serial numbers
- Batch processing for downloading multiple images at once
- Feedback display when saving is complete

## Installation

1. Navigate to the ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/your-username/comfyui_local_save.git
```

3. Restart ComfyUI

## How to Use

1. Search for "Local Save Image" in the ComfyUI node browser
2. Add the node and set the following parameters:
   - `prefix`: Prefix for the file name to be saved (default: "generated")
   - `file_format`: Select the save format (PNG/JPEG)
3. Connect the output of the image generation node to the input of the "Local Save Image" node
4. When you run the workflow, the generated image will be downloaded automatically

## File Name Format

The file name of the saved image is generated in the following format:
```
{prefix}_{timestamp}_{number}.{ext}
```

Example:
```
generated_20250115_112814_001.png
generated_20250115_112814_002.png
```

- `prefix`: Prefix specified by the user
- `timestamp`: Timestamp in YYYYMMdd_HHmmss format
- `number`: 3-digit serial number starting from 001
- `ext`: Selected format (png/jpeg)

## Notes

- Depending on your browser settings, downloading multiple files may be restricted
- Please be aware of memory usage when processing a large number of images at once
- If you select JPEG format, the quality is set to 95%

## License

[MIT License](LICENSE)

## Information for Developers

Dependencies:
```
torch>=2.0.0
Pillow>=9.0.0
numpy>=1.22.0
```

These packages are included in the standard ComfyUI installation.

## Contact

Please submit bug reports and feature requests via GitHub Issues.