# Snap Style Nodes for ComfyUI

A collection of custom nodes for ComfyUI designed to replicate certain visual elements and effects reminiscent of Snap and early digital aesthetics. These nodes are ideal for image processing tasks and are fully compatible with ComfyUI.

## Metadata

- **Keywords**: ComfyUI, Custom Nodes, Image Processing, Snap Effects, Filters, Overlays
- **Repository Name**: comfyui-ComfySnap

## Installation

**Manual Installation**

Since this repository is not yet listed in the ComfyUI Manager, you can install it manually:

1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
    ```bash
    git clone https://github.com/SignalCha1n/comfyui-ComfySnap
    ```
3. Restart ComfyUI.

Once the repository is added to the ComfyUI Manager, you will be able to install it directly from the manager.

## Included Nodes

This package currently includes the following nodes, which will appear under the **"ComfySnap"** category when adding nodes:

---

### 1. Snap Text (`SnapTextOverlay`)

Adds a Snap-style semi-transparent text bar overlay to an image. Supports automatic text wrapping based on pixel width and various placement options.

**Inputs:**

* `image` (IMAGE): The input image.
* `text` (STRING): The text content to display in the bar.
* `vertical_placement` (COMBO): Selects the general vertical position of the text bar.
    * Options: "top", "middle", "bottom", "custom"
    * Default: "middle"
* `custom_vertical_percentage` (FLOAT): Sets the vertical position when `vertical_placement` is "custom". Uses a 0-100 scale where 0 = Bottom edge placement, 100 = Top edge placement for the bar's top edge. Default: 0.0.
* `text_color` (COLOR): The color of the text. Default: White (#FFFFFF).
* `font_name` (STRING): The filename of the font to use (e.g., `arial.ttf`, `segoeui.ttf`). 
* `font_size_ratio` (FLOAT): Sets the font size relative to the image width. Default: 0.05 (5% of width).
* `vertical_padding_ratio_of_size` (FLOAT): Defines the total vertical padding (space above + below text) relative to the calculated font size. A value of 0.7 means padding is 70% of the font size. Adjusts bar height dynamically. Default: 0.7.
* `line_spacing` (INT): Pixel spacing between lines if the text wraps. Default: 4.
* `bar_color` (COLOR): The color of the semi-transparent background bar. Default: Black (#000000).
* `bar_alpha` (FLOAT): The opacity of the background bar (0.0 = fully transparent, 1.0 = fully opaque). Default: 0.5.

**Outputs:**

* `image` (IMAGE): The image with the text bar overlay applied.

---

### 2. Face Avoid (`FaceAvoidRandomY`)

Calculates the vertical center of a face mask and generates a random vertical position (0-100 scale, 100=Top) that avoids a defined zone around the face. Optionally avoids a second user-defined vertical zone. Useful for positioning overlays like text or stamps away from faces.

**Inputs:**

* `mask` (MASK): The input face mask (white pixels indicate the face). Processes only the first mask in a batch.
* `centroid_threshold` (FLOAT): Threshold (0.01-1.0) to determine which mask pixels are considered 'active' for centroid calculation. Default: 0.5.
* `vertical_adjustment` (FLOAT): Manually shift the detected vertical face center (-100 to 100) before calculating the avoidance zone. 100=Top, 0=Bottom. Default: 0.0.
* `avoid_threshold` (FLOAT): Defines the size (+/- this value) of the zone to avoid around the adjusted face center (0-50). Default: 15.0.
* `seed` (INT): Seed for the random number generator.
* `generate_random` (BOOLEAN): If True, generates a random position outside the avoidance zone(s). If False, outputs the adjusted face center position directly. Default: True.
* `avoid_zone2_y_bottom` (FLOAT, Optional): The bottom boundary (0-100, 0=Bottom) of an optional second vertical zone to avoid (e.g., where a text bar is placed). Default: -1.0 (disabled).
* `avoid_zone2_y_top` (FLOAT, Optional): The top boundary (0-100, 100=Top) of the optional second vertical zone to avoid. Default: -1.0 (disabled).

**Outputs:**

* `vertical_pos_100_top` (FLOAT): The calculated vertical position (0-100 scale, 100=Top). Either random (if enabled) or the adjusted face center.

---

### 3. Basic Filters (`BasicFilters`)

Applies simple color grading filters reminiscent of basic Snap swipe filters. Allows randomization of filter type and strength.

**Inputs:**

* `image` (IMAGE): The input image.
* `filter_type` (COMBO): Select the desired filter effect.
    * Options: "original", "grayscale", "vivid", "cooler", "warmer", "brighter", "darker"
    * Default: "original"
* `strength` (FLOAT): Blends the filtered image with the original (0.0 = original, 1.0 = full filter effect). Default: 1.0.
* `randomize_filter` (BOOLEAN): If True, ignores `filter_type` and randomly selects an actual filter (excludes "original"). Default: False.
* `randomize_strength` (BOOLEAN): If True, ignores `strength` slider and uses a random value between the min/max settings below. Default: False.
* `random_strength_min` (FLOAT): Minimum value for randomized strength (0.0-1.0). Default: 0.5.
* `random_strength_max` (FLOAT): Maximum value for randomized strength (0.0-1.0). Default: 1.0.
* `seed` (INT): Seed for randomization.

**Outputs:**

* `image` (IMAGE): The image with the filter applied and blended.

---

### 4. Low Quality Digital Look (`LowQualityDigitalLook`)

Simulates the artifacts and noise typical of early digital cameras or low-light photos. Applies JPEG compression and Gaussian noise.

**Inputs:**

* `image` (IMAGE): The input image.
* `preset` (COMBO): Choose a predefined set of parameters.
    * Options: "Standard Snap Low Light", "Early 2000s Digital"
    * Default: "Standard Snap Low Light"
* `effect_level` (FLOAT): Controls the overall intensity of the effect.
    * 0.0 = No effect (original image).
    * 0.5 = The standard effect defined by the chosen `preset`.
    * 1.0 = A stronger version of the effect (more artifacts/noise).
    * Default: 0.5
* `seed` (INT): Seed for the random noise generation.

**Outputs:**

* `image` (IMAGE): The image with low-quality effects applied.

---

## Dependencies

These nodes rely on standard Python libraries (`os`, `datetime`, `random`, `io`) and libraries typically included with ComfyUI (`torch`, `numpy`, `PIL`/`Pillow`). No external installation should be required beyond having a standard ComfyUI setup.

## Testing

To run tests, ensure you have `pytest` installed. If not, install it using:
```bash
pip install pytest
```

Navigate to the `tests/` directory and execute:
```bash
pytest
```

This will run all unit tests and provide a summary of the results. Ensure all dependencies listed in `requirements.txt` are installed before running the tests.

## Known Limitations

1. The nodes assume valid input formats (e.g., 4D tensors for images, 3D tensors for masks). Invalid inputs may result in errors.
2. Font availability depends on the system. Ensure the specified font file exists or use a fallback font.
3. Randomized outputs may vary depending on the seed value.
4. Processing large images or batches may lead to performance issues.

## Best Practices

1. Use the provided `requirements.txt` to install dependencies with compatible versions.
2. Test the nodes with a variety of inputs to ensure expected behavior.
3. Profile the code for performance bottlenecks if processing large datasets.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
