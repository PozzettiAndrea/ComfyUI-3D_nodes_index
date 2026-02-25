# DDM Bundle - ComfyUI Custom Nodes

Clean workflow routing nodes for ComfyUI. Say goodbye to spaghetti connections!

## Features

- **Set Node**: Store any value with a unique identifier
- **Get Node**: Retrieve stored values anywhere in your workflow
- Works with all data types (images, latents, models, text, etc.)
- No more messy connection lines across your canvas

## Installation

### Method 1: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
```bash
   cd ComfyUI/custom_nodes/
```

2. Clone or download this repository:
```bash
   git clone https://github.com/yourusername/DDM_Bundle.git
```
   
   Or manually create a folder called `DDM_Bundle` and copy all files into it.

3. Restart ComfyUI

### Method 2: ComfyUI Manager
*Coming soon - install directly through ComfyUI Manager*

## Usage

### Basic Example

1. **Set a Value**
   - Add a "DDM Set Value" node
   - Connect any output to it (image, latent, model, etc.)
   - Give it an ID like `"my_image"`

2. **Get the Value**
   - Add a "DDM Get Value" node anywhere else in your workflow
   - Type the same ID: `"my_image"`
   - The value will be retrieved automatically

### Advanced Features

- **Optional Default**: Get Node has an optional default input if the value isn't found
- **Pass-through**: Set Node outputs the same value it receives, so you can chain them
- **Any Type**: Works with any ComfyUI data type automatically

## Nodes

### DDM Set Value
- **Inputs**:
  - `value`: Any type - the value to store
  - `id`: String - unique identifier for this value
- **Outputs**:
  - `value`: The same value (pass-through)

### DDM Get Value
- **Inputs**:
  - `id`: String - identifier to retrieve
  - `default` (optional): Any type - fallback if ID not found
- **Outputs**:
  - `value`: The retrieved value

## Tips

- Use descriptive IDs like `"prompt_text"`, `"final_image"`, `"lora_model"`
- Set nodes must execute before Get nodes (ComfyUI handles this automatically)
- IDs are case-sensitive
- Use the same ID in Set and Get nodes to connect them

## Troubleshooting

**Get node shows validation error?**
- Make sure there's a Set node with the same ID somewhere in the workflow
- The validation should pass automatically with this version

**Getting None values?**
- Check that the Set node is actually executing (not disabled)
- Verify the ID matches exactly (case-sensitive)
- Make sure the Set node runs before the Get node

## Version History

- **v1.0.0** - Initial release
  - Set and Get nodes with proper validation
  - Support for all data types
  - Optional default values

## License

MIT License - See LICENSE file for details

## Credits

Created for the ComfyUI community to make workflows cleaner and more manageable.

## Support

If you encounter issues or have suggestions:
- Open an issue on GitHub
- Join the discussion in the ComfyUI Discord

---

**Enjoy cleaner workflows!** 🎨
```

### 4. `LICENSE` (MIT License)
```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 5. `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# ComfyUI specific
*.safetensors
*.ckpt
*.pt
*.pth
