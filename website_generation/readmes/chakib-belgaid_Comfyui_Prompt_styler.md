# ComfyUI Style Plugin

This is a simple plugin for ComfyUI that allows you to import A1111 CSV styles into ComfyUI prompts.

## Installation

To install the plugin, clone this repository into the `custom_nodes` folder in ComfyUI.

## Adding New Styles

To add new styles, place the CSV or JSON file into the `styles` folder in this repository.

**Note:** Ensure that the positive prompt in the style contains **"{prompt}"**. If it doesn't, the prompt will be appended at the end of the style.

## Nodes

The plugin includes the following node:

- `promot_styler`

## Example

Here's an example of how to use the plugin:

![Example scenario](https://raw.githubusercontent.com/chakib-belgaid/Comfyui_Prompt_styler/main/example.png)

## Known Issues

There is a visual bug where not all buttons are visible. To fix this, simply resize the box.

## Credits

The styles are downloaded from the [Dice repository](https://civitai.com/user/DiceAiDevelopment).