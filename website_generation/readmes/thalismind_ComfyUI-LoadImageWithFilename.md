# ComfyUI LoadImageWithFilename

This custom node extends ComfyUI's image loading functionality with filename output and folder loading capabilities.

## Features

### LoadImageWithFilename
- **Enhanced Load Image Node**: Based on the original ComfyUI LoadImage node
- **Filename Output**: Returns the filename of the loaded image as a STRING output
- **Compatible**: Maintains all original functionality (IMAGE and MASK outputs)

### LoadImageFolder
- **Folder Loading**: Load all images from a specified folder path
- **Batch Processing**: Returns all images concatenated as a single tensor
- **Filename Tracking**: Returns a list of all loaded filenames
- **Error Handling**: Gracefully handles corrupted or unsupported image files

### SaveImageWithFilename
- **Enhanced Save Image Node**: Based on the original ComfyUI SaveImage node
- **Custom Filenames**: Accepts single filenames or comma-separated lists of filenames
- **Flexible Naming**: Can use provided filenames or fall back to default naming
- **Batch Support**: Handles multiple images with corresponding filenames

## Installation

1. Place `nodes.py` in your ComfyUI `custom_nodes` directory
2. Restart ComfyUI
3. The new nodes will appear in the "image" category

## Usage

### LoadImageWithFilename
- **Input**: Select an image file from the dropdown
- **Outputs**:
  - `image`: The loaded image tensor
  - `mask`: The image mask (if available)
  - `filename`: The filename of the loaded image

### LoadImageFolder
- **Input**: Enter a folder path as a string
- **Outputs**:
  - `image`: All images from the folder concatenated as a single tensor
  - `mask`: All masks concatenated as a single tensor
  - `filenames`: List of all loaded filenames

### SaveImageWithFilename
- **Inputs**:
  - `images`: The images to save (IMAGE tensor)
  - `filenames`: Single filename or comma-separated list of filenames (optional)
  - `filename_prefix`: Prefix for default naming (optional)
- **Behavior**:
  - If filenames are provided, uses them for the corresponding images
  - If no filenames or fewer filenames than images, uses default naming for remaining images
  - Automatically adds .png extension to filenames
  - Saves to ComfyUI output directory

## Requirements

- ComfyUI
- PIL (Pillow)
- PyTorch
- NumPy

## Notes

- The LoadImageFolder node will skip any non-image files in the selected folder
- If no valid images are found in a folder, empty tensors will be returned
- All images in a folder must have the same dimensions for proper concatenation
- Error messages are printed to console for any files that fail to load
- The SaveImageWithFilename node preserves original filenames when possible
- If filenames contain extensions, they will be replaced with .png

## Based On

- [ComfyUI LoadImage Node](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)
- [ComfyUI SaveImage Node](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)
- [Issue #8699](https://github.com/comfyanonymous/ComfyUI/issues/8699) - Request for filename output functionality