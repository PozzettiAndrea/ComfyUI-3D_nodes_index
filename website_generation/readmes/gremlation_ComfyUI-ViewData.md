# ComfyUI-ViewData

A ComfyUI node that displays the type and contents of whatever is connected to the input.  In the case of a Tensor object, it shows the shape instead of its value.

![A screenshot showing usage of the node.](docs/workflow.png)

## Installation

### ComfyUI-Manager

- Open the Manager
- Pick "Custom Nodes Manager"
- Search for "ComfyUI-ViewData"
- Install the latest version
- Restart ComfyUI

### Comfy-Cli

- Run `comfy node install comfyui-viewdata`
- Restart ComfyUI

### Manual

Run the following commands in the terminal:

```shell
cd custom_nodes
git clone https://github.com/Gremlation/ComfyUI-ViewData
```

Then restart ComfyUI.

Note that due to an issue with case-sensitivity, you may have to rename the `ComfyUI-ViewData` directory to the
lowercase `comfyui-viewdata` before styles and syntax highlighting work.

## Options

You can change the indentation level for dictionaries by going to Settings > View Data ~🅖
