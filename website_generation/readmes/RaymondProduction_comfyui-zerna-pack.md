# Zerna Pack

Zerna Pack is a collection of custom nodes for ComfyUI designed to facilitate batch processing of text and images. It includes tools for dynamic prompt generation and other utilities to enhance your workflow.

## Features

- **Dynamic Prompt Injector**: Generate prompts dynamically by replacing placeholders with content from text files.
- **Batch Processing**: Process multiple prompts or images efficiently.

## Installation

1. Clone or download the repository into the `custom_nodes` directory of your ComfyUI installation:
   ```bash
   git clone https://github.com/RaymondProduction/comfyui-zerna-pack.git
   ```
2. Ensure that ComfyUI is installed and properly configured. No additional dependencies are required as this pack uses only the standard library and ComfyUI core.

## Usage

### Dynamic Prompt Injector

1. Place your `.txt` files containing prompt data in the `prompts` directory:
   ```
   comfyui-zerna-pack/prompts/
   ```
   Example files:
   - `test.txt`:
     ```
     hello
     ```
   - `example01.txt`:
     ```
     cat
     dog
     pig
     ```

2. Use the **Dynamic Prompt Injector** node in ComfyUI:
   - Set the `prompt_text` field with a template containing `[X]` as a placeholder.
   - Select a `.txt` file from the `prompt_file` dropdown.
   - Configure optional parameters like `reload`, `load_cap`, and `start_index` as needed.

3. The node will replace `[X]` in the `prompt_text` with each line from the selected file and output the processed prompts.

### Example

- **Input**:
  - `prompt_text`: `"A photo of [X] in the forest."`
  - `prompt_file`: `example01.txt`
- **Output**:
  ```
  A photo of cat in the forest.
  A photo of dog in the forest.
  A photo of pig in the forest.
  ```

## Development

### File Structure

- `zerna/`: Contains the core logic for the Zerna Pack.
  - `prompt_generators.py`: Implements the Dynamic Prompt Injector.
- `prompts/`: Directory for storing `.txt` files used in prompt generation.
- `__init__.py`: Initializes the Zerna Pack and registers its nodes with ComfyUI.

### Version

Current version: `0.0.1`

## Contributing

Feel free to submit issues or pull requests to improve the Zerna Pack. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Special thanks to the ComfyUI community for providing the tools and inspiration for this project.