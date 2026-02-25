# ComfyUI VPype Nodes

<a href="https://www.buymeacoffee.com/gcode.pro" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

This custom node suite for ComfyUI uses `vpype` to process SVG files and generate G-code for plotting. It provides two main nodes: one for processing SVGs (merging, simplifying, rotating, layout) and another for generating G-code with customizable plotting parameters.

![Example Workflow](screen.jpg)

_Note: The example workflow above uses [z-image](https://github.com/Z-Image/ComfyUI-Z-Image) (or similar image loader) and [ComfyUI-ToSVG-Potracer](https://github.com/ImagineerNL/ComfyUI-ToSVG-Potracer) to generate the initial SVG from an image._

## Features

- **VPype SVG Processor**:
  - `linemerge`: Merges nearby lines to optimize plotting paths.
  - `linesimplify`: Simplifies paths by reducing the number of nodes.
  - `linesort`: Sorts lines to minimize travel distance.
  - `min_length`: Filters out paths shorter than a specified threshold.
  - `multipass`: Duplicate geometries for multiple passes.
  - `rotate`: Rotates the geometry.
  - `layout`: Scales and centers the design on a specified page size (A4, etc.) within margins.
- **VPype G-Code Generator**:
  - Generates G-code from an SVG input.
  - Customizable Pen Up/Down positions.
  - Adjustable plotting speed.
  - Option to invert the Y-axis.

## Nodes

### 1. VPype SVG Processor

This node performs geometric operations on an input SVG file.

**Inputs:**

- **`svg_input`** (STRING): The SVG content or file path. Usually comes from a previous node.
- **`merge_tolerance`** (FLOAT, default: 0.1): Tolerance for merging lines (mm).
- **`simplify_tolerance`** (FLOAT, default: 0.05): Tolerance for path simplification (mm).
- **`min_length`** (FLOAT, default: 0.0): Filter out paths shorter than this length (mm). Set to 0 to disable.
- **`multipass_count`** (INT, default: 0): Duplicate geometries to draw them multiple times. Set to 0 to disable.
- **`rotation`** (FLOAT, default: 90.0): Angle to rotate the design (degrees).
- **`perform_layout`** (BOOLEAN, default: True): If enabled, scales and aligns the SVG to the specified page dimensions. Disable if you want to keep the original SVG coordinates/size.
- **`margin`** (FLOAT, default: 10.0): Page margin when layout is enabled (mm).
- **`width`** (FLOAT, default: 210.0): Target page width (mm). Default is A4 width.
- **`height`** (FLOAT, default: 297.0): Target page height (mm). Default is A4 height.

**Outputs:**

- **`svg_output`** (STRING): The processed SVG content.

### 2. VPype G-Code Generator

This node takes an SVG string and converts it into G-code formatted for plotters/CNC machines.

**Inputs:**

- **`svg_input`** (STRING): The SVG content (usually from _VPype SVG Processor_).
- **`pen_up`** (FLOAT, default: 5.0): Z-axis position when the pen is up (mm).
- **`pen_down`** (FLOAT, default: 0.0): Z-axis position when the pen is down/writing (mm).
- **`speed`** (FLOAT, default: 1000.0): Movement speed (Feed rate) in mm/min.
- **`invert_y`** (BOOLEAN, default: False): Invert the Y-axis coordinates (useful for some CNC coordinate systems).

**Outputs:**

- **`gcode_output`** (STRING): The generated G-code.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory.

    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/boardmain/ComfyUI-Svg2Gcode.git
    ```

    _(Or simply copy the folder if you are developing locally)_

2.  Install the required Python packages for the ComfyUI environment:

    ```bash
    pip install -r requirements.txt
    ```

    This will install `vpype`, `vpype-occult`, and `vpype-gcode`.

3.  Restart ComfyUI.

## Requirements

- `vpype`
- `vpype-occult`
- `vpype-gcode`

Make sure `vpype` is correctly installed and accessible in the system path or the virtual environment used by ComfyUI.
