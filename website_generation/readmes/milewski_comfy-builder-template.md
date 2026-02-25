# Comfy Builder Template

This is a template repository that you can use as a starting point for building your own custom nodes for ComfyUI.

## Setup Instructions

Follow these steps to get started with building your custom node:

1. Clone the repository or [click here](https://github.com/new?template_name=comfy-builder-template&template_owner=milewski).
2. Rename Your Custom Node
   - Modify the name of your custom node. It must be unique
   - Change the `package.name` and `lib.name` in `Cargo.toml` to your desired node name.
3. Install Prerequisites:
   - Install [Rust](https://rust-lang.org/tools/install/)
   - Install [Maturin](https://www.maturin.rs/installation.html) to build Python extensions.
4. Build Your Node
   Run the following command to generate a `.whl` file:
   ```bash
   maturin build --release
   ```
   This will generate a `.whl` file located at `./target/wheels`
5. Install the Wheel in Your ComfyUI Environment:
   Install the generated .whl file into your ComfyUI environment:
   ```bash
   pip install ./target/wheels/your_custom_node.whl
   ```
6. Add the `__init__.py` File
   At the root of your custom node directory, create an __init__.py file with the following content:
   ```python
   from name_of_your_custom_node import *
   ```
7. Restart your ComfyUI installation. Your custom node should now appear and be ready for use!

---

## Publishing Your Custom Node

To share your custom node with the ComfyUI community and make it available on the registry, follow these steps:

1. Create an Account:
   Sign up and create a username at the [ComfyUI Registry](https://registry.comfy.org/).
2. Install ComfyUI CLI:
   Download and install the ComfyUI CLI:
   ```bash
   pip install comfy-cli
   ```
3. Update `pyproject.toml`:
Open `pyproject.toml`, ensure your custom node details are correct and update the `PublisherId` with your username from the ComfyUI registry.

4. Publish Your Node: `comfy node publish`.

--- 

## Customizing the Installation Script

Take a look at the `install.py` script. This is the first script that runs when your node is installed. 
It ensures that your node compiles successfully by:

- Installing Rust if it's not already installed.
- Running `maturin build --release`.
- Installing the generated wheel using `pip`.

Feel free to customize this script to fit your specific needs.