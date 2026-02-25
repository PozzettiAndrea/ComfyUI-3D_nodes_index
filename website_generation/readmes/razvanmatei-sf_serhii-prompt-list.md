# Dynamic Prompt List Node for ComfyUI

A custom node for ComfyUI that allows you to create lists of prompts with **dynamic input count**. Add or remove prompt inputs on the fly without creating multiple nodes.

![Node Icon](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)

## Features

✨ **Dynamic Inputs** - Adjust the number of prompt inputs from 2 to 50
🔄 **Easy Updates** - Click "Update inputs" button to add/remove fields
📝 **Clean Interface** - Multiline text support for each prompt
🎯 **List Output** - Returns a proper list structure for use with other nodes

## Installation

### Method 1: Clone to ComfyUI custom_nodes

```bash
cd ComfyUI/custom_nodes
git clone <your-repo-url> serhii-prompt-list
```

### Method 2: Manual Installation

1. Download this repository
2. Extract to `ComfyUI/custom_nodes/serhii-prompt-list`
3. Restart ComfyUI

## Usage

### Basic Workflow

1. **Add Node**: Search for "Dynamic Prompt List" in ComfyUI node menu
2. **Set Input Count**: Adjust the `inputcount` parameter (default: 5)
3. **Update Inputs**: Click the "Update inputs" button
4. **Fill Prompts**: Enter your prompts in the multiline text fields
5. **Connect**: Connect the output to any node that accepts lists

### Node Parameters

- **inputcount** (INT): Number of prompt inputs (2-50, default: 5)
- **prompt_1** to **prompt_N** (STRING): Multiline text inputs for prompts

### Example

```
┌─────────────────────────────┐
│ Dynamic Prompt List         │
├─────────────────────────────┤
│ inputcount: 6               │
│ [Update inputs]             │
├─────────────────────────────┤
│ prompt_1: "A sunny beach"   │
│ prompt_2: "Mountain sunset" │
│ prompt_3: "City at night"   │
│ prompt_4: "Forest path"     │
│ prompt_5: "Desert landscape"│
│ prompt_6: "Ocean waves"     │
└─────────────────────────────┘
         ↓
    prompt_list (LIST)
```

## File Structure

```
serhii-prompt-list/
├── __init__.py              # Node registration
├── prompt_list_node.py      # Main node logic
├── README.md                # This file
└── web/
    └── js/
        └── dynamic_inputs.js # Dynamic input UI logic
```

## How It Works

### Python Backend (`prompt_list_node.py`)
- Defines the node class with dynamic `**kwargs` support
- Processes inputs dynamically based on `inputcount`
- Returns a list of non-empty prompts

### JavaScript Frontend (`dynamic_inputs.js`)
- Adds "Update inputs" button to the node
- Dynamically creates/removes input slots in the UI
- Handles input counting and name management

## Troubleshooting

### Node doesn't appear in menu
- Restart ComfyUI completely
- Check console for error messages
- Verify files are in the correct directory structure

### "Update inputs" button doesn't work
- Make sure JavaScript file is in `web/js/` folder
- Clear browser cache and refresh ComfyUI
- Check browser console for JavaScript errors

### Inputs not connecting
- Ensure you clicked "Update inputs" after changing count
- Verify the input type matches (STRING)

## Technical Details

**Category**: Serhii/Prompts
**Return Type**: STRING (list)
**Input Range**: 2-50 prompts
**Compatible With**: Any node accepting list inputs

## Credits

Based on the dynamic input pattern from:
- **KJNodes** by @kijai - JoinStringMulti implementation
- **Comfyroll Custom Nodes** - CR Simple Prompt List concept

## License

MIT License - Feel free to use, modify, and distribute

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check ComfyUI community forums

---

Made with ❤️ for the ComfyUI community
