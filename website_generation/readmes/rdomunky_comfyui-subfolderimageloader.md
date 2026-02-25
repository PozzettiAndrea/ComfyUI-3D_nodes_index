# ComfyUI Subfolder Image Loader

A ComfyUI custom node that enhances image loading with subfolder organization and dynamic filtering.

## Features

- **Subfolder Navigation**: Organize your input images into subfolders and select them easily
- **Dynamic Image Filtering**: Image list automatically updates when you change subfolder selection
- **Two-Stage Selection**: First select a subfolder, then choose an image from within it
- **Format Support**: PNG, JPG, JPEG, WebP, BMP, TIFF formats
- **Transparency Support**: Automatic alpha channel/mask extraction from RGBA images
- **Refresh Functionality**: Right-click menu option to refresh file listings
- **Security**: Path validation prevents directory traversal attacks

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Subfolder Image Loader"
3. Install the node

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/rdomunky/comfyui-subfolderimageloader.git
   ```
3. Restart ComfyUI

## Usage

1. **Organize Images**: Place your images in subfolders within ComfyUI's `input/` directory:
   ```
   ComfyUI/input/
   ├── portraits/
   │   ├── person1.jpg
   │   └── person2.png
   ├── landscapes/
   │   ├── mountain.jpg
   │   └── beach.png
   └── textures/
       ├── wood.jpg
       └── metal.png
   ```

2. **Add Node**: In ComfyUI, add the "Subfolder Image Loader" node (found in `image/loaders` category)

3. **Select Subfolder**: Choose a subfolder from the dropdown (or leave empty for root folder)

4. **Choose Image**: The image dropdown will automatically filter to show only images from the selected subfolder

5. **Load Image**: The node outputs the same data as the standard Load Image node:
   - `IMAGE`: The loaded image tensor
   - `MASK`: Alpha channel mask (if present)
   - `STRING`: Filename
   - `INT`: Width
   - `INT`: Height

## Tips

- **Refresh Files**: Right-click the node → "🔄 Refresh Files" to update file listings without restarting
- **UI Quirk**: Due to ComfyUI limitations, the image dropdown display may require a mouse movement to visually update (functionality works correctly)
- **Empty Folders**: Subfolders with no images will still appear in the subfolder list
- **Nested Folders**: Only direct subfolders are supported (no nested subfolder navigation)

## Technical Details

- **Path Security**: All file paths are validated to prevent directory traversal
- **API Endpoint**: Provides `/subfolder_loader/refresh` for dynamic file listing updates
- **Error Handling**: Graceful fallback to empty image tensors on errors
- **Performance**: Includes optional file caching for improved performance

## Comparison with Standard Load Image

| Feature | Standard Load Image | Subfolder Image Loader |
|---------|-------------------|----------------------|
| Subfolder support | ❌ | ✅ |
| Dynamic filtering | ❌ | ✅ |
| File organization | ❌ | ✅ |
| Transparency masks | ✅ | ✅ |
| Same outputs | ✅ | ✅ |

## Troubleshooting

**Images not appearing**: Ensure images are in supported formats and located in ComfyUI's input directory or its subfolders.

**Subfolder not updating**: Try the refresh option or restart ComfyUI if subfolders don't appear.

**JavaScript not loading**: Make sure the `web/` directory and `WEB_DIRECTORY` in `__init__.py` are properly configured.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.