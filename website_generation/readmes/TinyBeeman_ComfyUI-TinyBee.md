# ComfyUI-TinyBee

A collection of custom nodes for ComfyUI, designed to provide utility functions for list processing, file management, and more.

## Features
- List counting, random entry selection, and indexed entry selection
- List randomization with seed support
- Incrementer node for generating sequences
- File listing with glob and extension filtering
- Path processing utilities

## Installation
1. Clone or copy this folder into your ComfyUI `custom_nodes` directory.
2. (Optional) Install any dependencies listed in `requirements.txt` (all current dependencies are from the Python standard library).

## Usage
Add the nodes to your ComfyUI workflow as needed. Each node is documented with its input and output types in the UI.

## Nodes
- **List Count**: Counts the number of items in a list.
- **Random Entry**: Selects a random entry from a list, with optional seed.
- **Indexed Entry**: Selects an entry by index, with wrap-around.
- **Randomize List**: Shuffles a list with a given seed.
- **Incrementer**: Generates incrementing numbers with optional reset.
- **Get File List**: Lists files in a directory matching a glob pattern and extensions.
- **Process Path Name**: Splits a path into components.

## License
MIT License
