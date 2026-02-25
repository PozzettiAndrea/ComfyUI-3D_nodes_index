# ComfyUI Int and Float Conversion Nodes

A simple ComfyUI custom node extension that provides utility nodes for converting between integer and float values.

## Overview

This extension adds two custom nodes to ComfyUI:
- **IntToFloat**: Converts integer values to float values
- **FloatToInt**: Converts float values to integer values with configurable rounding

## Installation

1. Clone or download this repository
2. Place the entire folder in your ComfyUI `custom_nodes` directory
3. Restart ComfyUI

The nodes will automatically be available in the node menu under the "Custom" category.

## Nodes

### IntToFloat Node

Converts an integer input to a float output.

**Inputs:**
- `int_value` (INT): The integer value to convert

**Outputs:**
- `float_value` (FLOAT): The converted float value

**Example:**
- Input: `42` → Output: `42.0`

### FloatToInt Node

Converts a float input to an integer output with configurable rounding.

**Inputs:**
- `float_value` (FLOAT): The float value to convert
- `rounding_mode` (SELECT): Rounding method
  - `down (floor)`: Rounds down to the nearest integer (default)
  - `up (ceil)`: Rounds up to the nearest integer

**Outputs:**
- `int_value` (INT): The converted integer value

**Examples:**
- Input: `3.7` with "down (floor)" → Output: `3`
- Input: `3.2` with "up (ceil)" → Output: `4`

## Use Cases

These nodes are particularly useful when:
- Working with nodes that require specific data types
- Converting between different parameter types in your workflow
- Ensuring compatibility between different node outputs and inputs
- Implementing custom logic that requires type conversion

## File Structure

```
comfyui-int-and-float/
├── __init__.py              # Main extension entry point
├── int_to_float_node.py     # IntToFloat node implementation
├── float_to_int_node.py     # FloatToInt node implementation
└── README.md               # This file
```

## Requirements

- ComfyUI
- Python 3.7+

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements or bug fixes. 