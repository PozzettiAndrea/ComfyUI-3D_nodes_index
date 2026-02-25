# Candlehead Nodez - ComfyUI Custom Node Collection

A comprehensive suite of utility nodes for ComfyUI image processing workflows.

## Nodes Included

### AspectToRes
Converts input aspect ratio or aspect ratio from image to fixed width and height values for standard QWEN resolutions.

**Input:** 
Aspect ratio string (e.g., "16:9", "4:3", "1:1")
Image input pipe

**Output:**
- `width` (INT)
- `height` (INT)

**Supported Ratios:**
- 1:1 → 1328×1328
- 16:9 → 1664×928
- 9:16 → 928×1664
- 4:3 → 1472×1140
- 3:4 → 1140×1472
- 3:2 → 1584×1056
- 2:3 → 1056×1584
- Default (unsupported) → 1328×1328

### ImageInfo
Extracts and displays dimension and format information from image tensors.

**Input:** Image tensor

**Output:**
- `width` (INT)
- `height` (INT)
- `channels` (INT)
- `info` (STRING) - Formatted info string

### TextProcessor
Simple text processing node for string manipulation.

**Input:** Text string and processing mode

**Output:** Processed text string

**Modes:**
- uppercase
- lowercase
- capitalize
- reverse

## Installation

1. Copy this folder to your ComfyUI `custom_nodes` directory:
   ```bash
   cp -r Candlehead-Nodez /path/to/ComfyUI/custom_nodes/
   ```

2. Restart ComfyUI

## Usage

1. In ComfyUI UI, right-click to open the node menu
2. Search for node name (e.g., "Aspect Ratio to Resolution")
3. Click to add to workflow
4. Connect inputs and outputs as needed

## Project Structure

```
candlehead-nodez/
├── __init__.py           # Main node registration
├── nodes/
│   ├── __init__.py
│   ├── aspect_converter.py
│   ├── image_info.py
│   └── text_processor.py
└── README.md
```

## License

MIT License
