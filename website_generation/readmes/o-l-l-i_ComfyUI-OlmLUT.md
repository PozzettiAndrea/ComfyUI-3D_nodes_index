# Olm LUT Node for ComfyUI

![Olm LUT ComfyUI splash image](images/olmLUT_splash.png)


The **Olm LUT** is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to apply `.cube` LUT (Look-Up Table) files to images within your generative workflows. It supports creative workflows including film emulation, color grading, and aesthetic stylization using LUTs.

This node supports adjustable LUT blending strength, gamma correction, and includes several built-in test and debug modes for validating and inspection of  the results.

You can easily create your own LUTs using my [LUT Maker](https://o-l-l-i.github.io/lut-maker/), a free, GPU-accelerated LUT generator that runs entirely in your browser. It's a great companion tool for Olm LUT, letting you quickly design custom .cube LUTs without the need for expensive software.

![Olm LUT ComfyUI node UI](images/olmLUT_ui.png)

---

## Why Use This Node?

Many ComfyUI nodes are buried inside large, complex node packs that introduce unnecessary bloat and overhead. Often, you end up installing dozens of nodes just to use the one you actually need.

This node is different — it’s a focused, lightweight, and standalone solution built specifically for one task: applying LUTs cleanly and efficiently.

If you’re looking to add color grading to your images without pulling in a ton of unrelated functionality, this node offers a simple, clean, and effective alternative.

---

## Features

- Apply industry-standard `.cube` LUTs to images
  - 17,32,64 tested
- Adjustable blending strength (0.0-1.0)
- Optional sRGB gamma correction
- Multiple test modes and patterns:
  - Passthrough (no effect)
  - Test b/w gradient
  - HSV map
  - Test RGB color swatches (horizontal/vertical)
  - Mid-gray box mode
- Supports 3D LUT interpolation with high accuracy
- Auto-loads LUTs from local `luts/` directory
- A few example LUTs included, by yours truly.

**Test patterns:**

![Test patterns illustration](images/olmLUT_test_patterns_image.png)

---

## Installation

1. **Clone this repository to your ComfyUI/custom_nodes folder.**

2. **Check/install dependencies.**

You should already have all of the dependencies installed if you have ComfyUI up and running.
Remember to always active the virtual environment (venv) before installing anything.

```bash
# Most likely you don't need to do this:
pip install -r requirements.txt
```


3. **Ensure your folder contains a `luts/` directory** with your `.cube` LUT files:

```
ComfyUI-OlmLUT/
├── init.py
├── olm_lut.py # <-- this is the node
└── luts/ (put your LUTs here)
    ├── life_is_a_lemon.cube
    ├── bubblegum_dream.cube
    └── ...
```

4. **Restart ComfyUI** to load the new node.

---

## Usage

1. Add the **Olm LUT** node into your ComfyUI workflow.
2. Connect an image input (e.g. from a VAE Decode or Load Image node).
3. Choose a LUT from the dropdown — these are automatically listed from the `luts/` subfolder.
4. Adjust the **strength** slider (0.0 = no effect, 1.0 = full LUT).
5. (Optional) Enable **gamma correction** if your images are in sRGB space.
6. Use the **operation mode** dropdown to:
   - Apply LUT normally (`normal`)
   - Output test patterns (`test_colors_horizontal`, `test_gradient`, etc.)
   - View passthrough (`passthrough`)

---

## Parameters

| Name              | Type      | Description                                                   |
| ------------------|-----------|---------------------------------------------------------------|
| `image`           | Image     | Input image tensor                                            |
| `lut_file`        | Choice    | LUT to apply, loaded from `luts/` folder                      |
| `strength`        | Float     | Blend between original and LUT-mapped image (0.0 to 1.0)      |
| `gamma_correction`| Boolean   | Convert sRGB to linear before LUT and back after              |
| `debug_logging`   | Boolean   | Print LUT and mode info to console                            |
| `operation_mode`  | Enum      | Choose from `normal`, `passthrough`, or several test patterns |

---

## Operation Modes

| Mode                     | Description                                        |
|--------------------------|----------------------------------------------------|
| `normal`                 | Apply selected LUT with blending                   |
| `passthrough`            | Output original image (useful for comparison etc.) |
| `test_colors_horizontal` | Horizontal RGB color bars                          |
| `test_colors_vertical`   | Vertical RGB color bars                            |
| `test_gradient`          | Horizontal grayscale linear gradient               |
| `test_hsv`               | Horizontal HSV color gradient                      |
| `mid_gray_box`           | Centered gray box against black background         |

---

## Notes

- `.cube` files must be properly formatted and contain valid LUT data (3D cube format).
- If LUT resolution is incorrect or data is missing, the script may throw an error.
- Strength interpolation uses smooth linear blending.
- Check the debug mode output (when enabled), it might give you clues what is going on.
- Expect bugs and such, this is the first version.

---

## Author

Developed by [@o-l-l-i](https://github.com/o-l-l-i).


## Thanks

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) — the foundation that made this node possible.
- Suzie1 for the excellent [Guide To Making Custom Nodes in ComfyUI](https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes).