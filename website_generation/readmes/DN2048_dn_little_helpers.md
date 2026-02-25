# DN Little Helpers

A collection of little custom nodes for ComfyUI to help in simple/specific tasks.

# Features

- ### **[NODE] Boolean to Other**
  - Converts a boolean input to int or string.
  - For the int output it has an optional toggle to add +1 to the number. Useful for selectors that start on 1. So FALSE becomes 1 and TRUE becomes 2.


- ### **[NODE] Is Group Active**
  - Outputs a boolean is the selected group (via combobox) is active.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, git clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

> [NOTE]
> This projected was created with a [cookiecutter](https://github.com/Comfy-Org/cookiecutter-comfy-extension) template. It helps you start writing custom nodes without worrying about the Python setup.

