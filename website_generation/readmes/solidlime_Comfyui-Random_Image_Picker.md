# Random Image Picker - ComfyUI Custom Node

A ComfyUI custom node that provides flexible image loading with support for both single file picker and random folder selection.

## Features

✨ **Two Operation Modes**:
- **Single Mode**: Direct file picker with instant preview
- **Folder Mode**: Randomly select an image from a folder

🎯 **Key Features**:
- **📁 File Picker Button**: Browser-based file selection with instant preview
- **Auto Mode Switching**: Automatically switches to Single mode when using file picker
- **Real-time Preview**: See your image immediately without execution
- **Subfolder Support**: Option to include subfolders in folder search
- **Resolution Output**: Automatically outputs image width and height
- **Reproducible Random**: Seed control for consistent random selection
- **Clean UI**: Hidden internal widgets for better user experience

## Installation

### Via Git Clone (Manual)

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/solidlime/Comfyui-Random_Image_Picker.git
   ```

2. Restart ComfyUI

3. The node will appear in the "image" category as "Random Image Picker"

### Via ComfyUI-Manager (Coming Soon)

Once registered with ComfyUI-Manager, you'll be able to install directly from the manager UI.

## Usage

### Node Controls

- **folder_path** (STRING): 
  - Path to folder for random selection (Folder mode only)
  - Default: ComfyUI input directory
  
- **folder_mode** (BOOLEAN):
  - `Single` (OFF): Use file picker for direct selection
  - `Folder` (ON): Random selection from folder_path
  - **Note**: Automatically switches to `Single` when using file picker

- **include_subfolders** (BOOLEAN):
  - Only applies in Folder mode
  - `OFF`: Only scan the specified folder
  - `ON`: Include all subfolders in the search

- **seed** (INT): 
  - Random seed for reproducible selection in Folder mode
  - Range: 0 to 18446744073709551615

- **📁 Choose File** (Button):
  - Click to open browser file picker
  - Selected image shows instantly in preview
  - Automatically switches to Single mode

### Node Outputs

- **image**: The loaded image in ComfyUI tensor format
  - Includes real-time preview display
  - Works with all standard ComfyUI image processing nodes

## How It Works

### Single Mode (File Picker)
1. Click **📁 Choose File** button
2. Select an image from your file system
3. Image appears instantly in preview
4. Mode automatically switches to `Single`
5. Image is ready for use in workflow

### Folder Mode (Random Selection)
1. Set `folder_mode` to `Folder` (ON)
2. Enter folder path in `folder_path`
3. Optionally enable `include_subfolders`
4. Set `seed` for reproducible results
5. Execute workflow to select random image

### Supported Image Formats

- PNG (.png)
- JPEG (.jpg, .jpeg)
- WebP (.webp)
- BMP (.bmp)
- GIF (.gif)

## Examples

### Example 1: Quick File Selection
```
1. Set folder_mode: Single (default)
2. Click "📁 Choose File"
3. Select your image
4. Preview appears instantly!
```

### Example 2: Random from Folder
```
folder_path: D:/images/
folder_mode: Folder (ON)
include_subfolders: OFF
seed: 42
```
→ Randomly selects one image from `D:/images/` (excluding subfolders)

### Example 3: Random with Subfolders
```
folder_path: D:/images/
folder_mode: Folder (ON)
include_subfolders: ON
seed: 42
```
→ Randomly selects one image from `D:/images/` and all its subfolders

## Technical Details

### Architecture
- **Python Backend**: Image loading and processing using PIL/Pillow
- **JavaScript Frontend**: File picker with FileReader API for browser-based file access
- **Base64 Transfer**: Secure data transfer from browser to ComfyUI backend

### Browser Limitations
Due to browser security restrictions, the file picker:
- Cannot access full file system paths
- Uses FileReader API to read files directly in browser
- Transfers image data as base64-encoded strings
- Works completely client-side until execution

### Output Format
- Image tensor: `[batch, height, width, channels]`
- Color space: RGB
- Value range: 0.0 to 1.0 (float32)
- Batch size: Always 1

## Troubleshooting

### Preview not showing
- Ensure ComfyUI is restarted after installation
- Check browser console for JavaScript errors
- Verify WEB_DIRECTORY is correctly set in `__init__.py`

### File picker not working
- Modern browsers required (Chrome, Firefox, Edge)
- Check that JavaScript is enabled
- Clear browser cache and reload

### Folder mode errors
- Verify folder path exists and is accessible
- Check folder contains supported image formats
- Ensure proper path format for your OS

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - Feel free to use and modify as needed.

## Credits

Developed with ❤️ for the ComfyUI community
include_subfolders: ON
seed: 42
```
→ Randomly selects one image from `D:/images/` and all its subfolders

## Technical Details

- Images are converted to RGB format
- Output tensor format: `[batch, height, width, channels]`
- Pixel values normalized to 0.0-1.0 range
- Uses PyTorch tensors for ComfyUI compatibility
- Real-time preview in ComfyUI UI (OUTPUT_NODE enabled)
- Custom JavaScript widget for enhanced file selection

## License

MIT License

## Author

Created for ComfyUI
