# ComfyUI-Utilitools

A collection of utility nodes for ComfyUI that I find handy. Nothing fancy, just stuff that makes workflows a bit easier when you need simple operations.

## What's in here?

These aren't the most sophisticated nodes out there, but they get the job done for basic operations:

### 🧮 Math Nodes
- **Add, Subtract, Multiply, Divide** - Basic math with both int and float outputs
- **Calculator** - Safely evaluate simple math expressions like "2 + 2 * 3"

### 📝 Text Utilities  
- **Text Concatenation** - Join two strings with optional separator
- **String Replace** - Find and replace text with optional count limit

### 🔄 Type Conversions
- **Float to Int / Int to Float** - Convert between number types
- **Whatever To String** - Convert any value (int, float, string) to string

### 🤔 Logic & Control
- **If Then Else** - Branch workflows based on boolean conditions
- **Switch** - Select from up to 8 inputs by index
- **Boolean Gates** - AND, OR, NOT operations

### 📋 Data Manipulation
- **Create List** - Make lists from up to 8 items
- **List Index** - Get item from list by index
- **Batch Controller** - Adjust tensor batch sizes

### ⚙️ Workflow Helpers
- **Passthrough** - For workflow organization (does nothing, just passes data through)
- **Counter** - Increment/decrement with optional reset
- **Date Timestamp** - Generate formatted date/time strings with toggles for components
- **Constants** - Int, Float, and String constant value nodes

### 🖼️ Image Utilities
- **Image Dimensions** - Get width, height, and batch size from images
- **Aspect Ratio** - Calculate ratio as decimal and simplified fraction (like "16:9")

## Installation

Just drop this folder into your ComfyUI `custom_nodes` directory and restart ComfyUI. That's it.

```
ComfyUI/custom_nodes/ComfyUI-Utilitools/
```

## Notes

- All nodes are organized under "Utilitools" categories in the node browser
- Most math operations work with both int and float inputs  
- The calculator node only accepts basic math expressions for safety
- These are utility nodes I made for myself - they're useful but not groundbreaking

## Structure

The code is organized by category for easier maintenance:

```
nodes/
├── math.py          # Arithmetic operations
├── text.py          # Text processing
├── conversion.py    # Type conversions  
├── logic.py         # Conditional logic
├── data.py          # Lists and batching
├── workflow.py      # Workflow helpers
├── constants.py     # Constant values
├── image.py         # Image utilities
└── main.py          # Central registry
```

Feel free to use, modify, or ignore as needed!
