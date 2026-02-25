# ComfyUI Batch Name Loop

A ComfyUI custom node package for batch image processing with filename preservation.

## Features

- **Batch Image Loader**: Load multiple images from a folder
- **Batch Image Iterator**: Process images individually in a loop
- **Batch Image Saver**: Save processed images with preserved filenames
- **Filename Preservation**: Maintain original filenames through the processing pipeline

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-BatchNameLoop.git
```

2. Restart ComfyUI

## Nodes

### Batch Image Loader
- **Input**: Folder path, file patterns (e.g., "*.png,*.jpg,*.jpeg")
- **Output**: Batch of images, filenames array, count
- Loads all matching images from the specified folder

### Batch Image Iterator
- **Input**: Batch images, filenames, index
- **Output**: Single image, corresponding filename
- Extracts a single image and filename by index for individual processing

### Batch Image Saver
- **Input**: Batch images, filename prefix, output folder
- **Output**: Array of saved file paths
- Saves entire batch with optional filename preservation

### Batch Image Single Saver
- **Input**: Single image, original filename, output folder
- **Output**: Saved file path
- Saves one image with preserved original filename

## Usage Example

1. Use **Batch Image Loader** to load a folder of images
2. Connect to your image processing nodes
3. Use **Batch Image Iterator** in a loop to process each image
4. Use **Batch Image Single Saver** to save with original filenames

## Requirements

- ComfyUI
- PIL (Pillow)
- PyTorch
- NumPy

## License

MIT License