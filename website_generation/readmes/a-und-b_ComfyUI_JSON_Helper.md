# ComfyUI JSON Helper

This custom node for ComfyUI provides a simple way to convert JSON strings to JSON objects, bridging the gap between nodes that output JSON as strings and nodes that require JSON object inputs.

## Features

- Converts JSON strings to JSON objects
- Handles JSON parsing errors gracefully
- Easy to integrate into existing ComfyUI workflows

## Requirements

- ComfyUI
- Python 3.10+

## Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/a-und-b/ComfyUI-JSONHelper.git
   ```
3. Restart ComfyUI

## Usage

After installation, you'll find a new node called "JSON String to Object" in the node menu. 

1. Connect the output of a node that produces a JSON string to the input of this node.
2. The output of this node will be a JSON object, which can be connected to nodes that expect JSON input.

## Error Handling

If the input string is not valid JSON, the node will print an error message to the console and return None.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
