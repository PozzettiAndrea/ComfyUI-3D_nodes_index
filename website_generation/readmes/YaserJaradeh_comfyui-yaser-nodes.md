# Yaser-nodes for ComfyUI

A collection of custom nodes for ComfyUI that provide dynamic input selection and intelligent upscaling functionality.

## Features

### 🔮 Conditional Selection Node
- **Dynamic Inputs**: Automatically adds new input slots as you connect cables
- **Index-based Selection**: Choose which input to pass through using an integer index
- **Any Type Support**: Works with any ComfyUI data type (images, latents, text, etc.)

### 🔮 Iterative Upscale with Models Node
- **Multi-Scale Support**: Choose from 1x, 2x, 4x, or 8x upscaling
- **Model Selection**: Use different upscale models for different scale factors
- **Optimized Performance**: Uses ComfyUI's tiled scaling for memory efficiency
- **OOM Protection**: Automatically reduces tile size if GPU memory is insufficient

## Installation

### Method 1: Git Clone (Recommended)

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/YaserJaradeh/comfyui-yaser-nodes.git
   ```

3. Restart ComfyUI

### Method 2: Manual Download

1. Download this repository as a ZIP file
2. Extract it to your ComfyUI `custom_nodes` directory
3. Ensure the folder is named `Yaser-nodes` or `comfyui-yaser-nodes`
4. Restart ComfyUI

### Method 3: ComfyUI Manager

1. Open ComfyUI Manager in your ComfyUI interface
2. Search for "Yaser-nodes" 
3. Click Install
4. Restart ComfyUI

## Usage

### Conditional Selection Node

1. **Add the node**: Search for "Conditional Selection Node" in the node menu
2. **Connect inputs**: 
   - The node starts with one input slot
   - As you connect cables to existing slots, new input slots automatically appear
   - Connect as many inputs as you need (any data type)
3. **Set selection index**: Use the `selection_index` parameter to choose which input to output (0-based indexing)
4. **Output**: The selected input will be passed through to the output

**Example Use Cases:**
- Switch between different prompts based on conditions
- Select different models dynamically
- Choose between processed and original images
- Route different data types conditionally

### Iterative Upscale with Models Node

1. **Add the node**: Search for "Iterative Upscale with Models Node" in the node menu
2. **Connect inputs**:
   - `image`: The input image to upscale
   - `model1x`, `model2x`, `model4x`, `model8x`: Different upscale models for each scale factor
3. **Select scale factor**: Choose from the dropdown (1, 2, 4, or 8)
4. **Output**: The upscaled image using the appropriate model

**Tips:**
- Use models that match their intended scale factor for best results
- For 1x scale, you can use any model (output will match the model's native scale)
- Ensure you have upscale models loaded in ComfyUI's `models/upscale_models/` directory

## File Structure

```
Yaser-nodes/
├── __init__.py              # Node registration
├── nodes.py                 # Main node definitions
├── types.py                 # Custom type definitions
├── upscale_utils.py         # Upscaling utility functions
├── web/                     # Frontend JavaScript
│   └── js/
│       └── dynamicInputs.js # Dynamic input handling
├── requirements.txt         # Python dependencies
```

## Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- PyTorch
- Standard ComfyUI dependencies

No additional Python packages are required beyond what ComfyUI already uses.

## Troubleshooting

### Nodes Not Appearing
- Ensure the folder is in the correct `custom_nodes` directory
- Check that all Python files are present and not corrupted
- Restart ComfyUI completely
- Check the ComfyUI console for any error messages

### Dynamic Inputs Not Working
- Make sure the `web` directory and JavaScript files are present
- Clear your browser cache
- Ensure ComfyUI is serving the web directory correctly

### Upscaling Errors
- Verify that your upscale models are compatible with ComfyUI
- Check that you have sufficient GPU memory
- Try reducing image size if getting out-of-memory errors
- Ensure the upscale models are in the correct format (.pth, .safetensors)

### Performance Issues
- Use smaller tile sizes for large images
- Close other GPU-intensive applications
- Consider using CPU upscaling for very large images

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs by opening an issue
- Suggest new features
- Submit pull requests with improvements
- Share your workflow examples

## License

This project is open source. Please check the license file for details.

## Acknowledgments

- Built for the amazing [ComfyUI](https://github.com/comfyanonymous/ComfyUI) by comfyanonymous
- Upscaling functionality based on ComfyUI's core upscale implementation
- Dynamic input system inspired by community custom nodes

## Support

If you find these nodes useful, please:
- ⭐ Star this repository
- 🐛 Report any bugs you encounter
- 💡 Suggest improvements or new features
- 📺 Share your workflows using these nodes

For support, please open an issue on GitHub with:
- Your ComfyUI version
- Steps to reproduce any problems
- Screenshots if applicable
- Console error messages (if any)
