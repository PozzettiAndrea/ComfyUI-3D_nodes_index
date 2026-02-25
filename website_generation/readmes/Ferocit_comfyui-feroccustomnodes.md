# ComfyUI-Feroc Custom Nodes

This repository contains custom nodes for ComfyUI, designed to enhance your workflow with text-based operations, particularly for managing and utilizing descriptive texts.

## Installation

1.  **Clone this repository** into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/YOUR_USERNAME/comfyui-feroc.git # Replace with your actual repository URL
    ```
2.  **Restart ComfyUI** to load the new nodes.

## Nodes Included

### 1. `LoadDescriptionNode` (Category: Feroc)

This node allows you to load text files from a designated `descriptions` folder within the `comfyui-feroc` directory. It's ideal for managing character descriptions, lore, or any other text snippets you frequently use in your ComfyUI workflows.

**Inputs:**

*   `subdirectory` (Dropdown): A dynamic list of subdirectories found within the `descriptions` folder. An empty string represents the root `descriptions` folder.
*   `file_name` (Dropdown): A dynamic list of `.txt` files found within the selected `subdirectory`.

**Outputs:**

*   `description_text` (STRING): The full content of the selected text file.
*   `description_name` (STRING): The base name of the selected description file (e.g., `Tabea`).

**Usage:**

Place your `.txt` description files inside the `ComfyUI/custom_nodes/comfyui-feroc/descriptions/` folder. You can organize them into subdirectories (e.g., `descriptions/characters/my_character.txt`).

First, select a `subdirectory` from the dropdown. Then, the `file_name` dropdown will populate with the `.txt` files available in that subdirectory.

If the `descriptions` folder or a selected subdirectory is empty, an example file `descriptions/examples/example.txt` will be created to guide you.

### 2. `RandomLineFromText` (Category: Feroc)

This node selects a random line from one or more specified text files. It's useful for injecting variability into your prompts or other text inputs by drawing from a pool of predefined lines.

**Inputs:**

*   `seed` (INT): A seed value for reproducibility of the random selection.
*   `file_path_1` to `file_path_5` (STRING, Optional): Absolute paths to text files from which a random line will be selected. You can provide up to 5 different file paths.

**Outputs:**

*   (STRING): A concatenated string of randomly selected lines, one from each provided file path. Each line is separated by a newline character.

**Usage:**

Provide the full absolute path to your text files (e.g., `C:\Users\YourUser\Documents\my_lines.txt`). The node will read each file, pick a random non-empty line, and combine them into a single output string. Warnings will be printed to the console if a file is not found or an error occurs during reading.

## Example Workflow

(Consider adding a screenshot or a brief description of a typical workflow here, e.g., connecting `LoadDescriptionNode` to a `CLIPTextEncode` node, or `RandomLineFromText` to inject dynamic elements into prompts.)

## Contributing

Feel free to open issues or pull requests if you have suggestions or improvements.
