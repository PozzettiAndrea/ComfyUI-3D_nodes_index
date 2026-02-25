# ComfyUI Seed Wildcard & Tools

ComfyUI custom nodes for advanced wildcard control and utilities.

## Features

### 1. Seed Based Wildcard Selector
- Selects a specific line from a wildcard file based on the Seed value.
- Supports Impact Pack syntax (`__tag__`, `{a|b}`, `{1::a|9::b}`).
- **Seed 1** = First line of the file.

### 2. Seed Based Wildcard (Lora Stack Output)
- Automatically parses `<lora:name:strength>` tags from the selected line.
- Outputs `LORA_STACK` for direct use with Impact Pack or similar nodes.
- Auto-matches filenames even if the extension or path separator differs.

### 3. Seed Generator (Min Limit)
- Generates a seed that never goes below a specified minimum value (e.g., 1).
- Useful for preventing errors in 1-based indexing logic.

### 4. Utilities
- **Resize Image by Base + Scale + Crop**: Handy image resizing tool.
- **Dynamic Text Concatenate**: Joins multiple text inputs with a delimiter.

## Installation

1. Install via ComfyUI Manager (Search for `Seed Wildcard`).
2. Or clone this repo into `custom_nodes` folder:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ComfyUI-Seed-Wildcard-Pack.git](https://github.com/YOUR_USERNAME/ComfyUI-Seed-Wildcard-Pack.git)