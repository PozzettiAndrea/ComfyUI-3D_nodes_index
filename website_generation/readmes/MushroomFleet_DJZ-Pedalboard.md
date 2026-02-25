# DJZ Pedalboard Custom Nodes for ComfyUI
![node-preview](https://raw.githubusercontent.com/MushroomFleet/DJZ-Pedalboard/refs/heads/main/images/node.png)

This project provides a collection of custom nodes designed for enhanced audio effects in ComfyUI. With an intuitive pedalboard interface, users can easily integrate and manipulate various audio effects within their workflows.

## Installation

### General Installation
1. Copy all custom node files into your ComfyUI custom nodes directory.
2. Restart ComfyUI to load the new nodes.

### Windows Users (ComfyUI Portable)
- Run the `install_portable.bat` script provided in this repository. This script automates the setup of the custom nodes specifically for ComfyUI Portable on Windows.

## How to Use the Nodes

Once installed, the custom nodes will be available within the ComfyUI interface:
- Add the nodes into your workflow.
- Select your audio effect requirements.
- Refer to the example workflows in the `example-workflow/` directory for practical guidance on integrating and using these nodes.

## The .pdl Format

The repository includes several `.pdl` files that define audio effect plugins for the pedalboard. These files specify the configuration, parameters, and chains for various audio effects. For more detailed documentation on the effect plugins, please refer to [PDL Information](https://github.com/MushroomFleet/DJZ-Pedalboard/blob/main/pedalboard/pedalboard.md). Check the /pedalboard/ folder to see the current list of PDL effects.

## Gradio Effect Designer
![designer-ui](https://raw.githubusercontent.com/MushroomFleet/DJZ-Pedalboard/refs/heads/main/images/gradio-designer.png)

This project also features a Gradio-based effect designer tool that enables you to create and test custom `.pdl` files through an interactive web interface. For more information and updates regarding the Gradio effect designer, visit [PDL Designer](https://github.com/MushroomFleet/Pedalboard-Gradio).

## Additional Notes

- Ensure that ComfyUI is set up correctly before installing the custom nodes.
- For troubleshooting and additional documentation, review the project logs and inline comments.
