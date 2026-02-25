# ComfyUI-FString

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to format strings using Python's string formatting syntax.

## Features

- **Dynamic Inputs**: The node accepts dynamic inputs. You can connect outputs from other nodes, and they will be available for formatting.
- **String Formatting**: Use standard Python `.format()` syntax `{variable_name}` in your template to substitute values.
- **Tensor Support**: Automatically converts Tensor inputs to a string representation of their shape (e.g., `Tensor torch.Size([1, 512, 512, 3])`).

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/danielwolber-wood/ComfyUI-FString.git
   ```
3. Restart ComfyUI.

## Usage

1. Add the **Simple F-String** node to your workflow (Category: `Learning/Text`).
2. Connect any inputs you want to use in your string. The node handles dynamic inputs, so you can connect multiple values.
3. In the `template` text box, write your string using placeholders that match the input names.
   - **Example**: If you connect an input named `model` and another named `seed`, you can write:
     ```
     Processing with {model} using seed {seed}
     ```
4. The output `formatted_string` will contain the result.

## Error Handling

- If a placeholder in the template does not match any connected input, the node will output an error message indicating the missing key.
- General exceptions during formatting are caught and returned as error strings.

## AI Disclosure

The first draft of this README was written with AI, but was manually edited and checked for correctness.