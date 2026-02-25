# Eses Composition Golden Ratio

![Eses Composition Golden Ratio Node Screenshot](docs/composition_golden_ratio.png)


> [!CAUTION]
> Before downloading and using the contents of this repository, please review the LICENSE.txt and the disclaimer.
> I kindly ask that you respect the licensing terms and the effort put into these tools to ensure their 
> continued availability for everyone. Thank you!


## Description

The 'Eses Composition Golden Ratio' node is a non-destructive visualization / exploration tool for ComfyUI. Overlay a customizable golden ratio pattern (Fibonacci spiral) onto a preview image. Analyze and create compositions with harmonious balance. 


💡 **The overlay is purely for guidance and does not alter the final output image!**

💡 No other requirements than having ComfyUI installed.

## Features

🧠 This tool works best on image that has 1:1618 aspect ratio, but it can also be used like a ruler, overlayed over your image, simply move, rotate and scale the pattern to analyze your target image!

* **Pattern Generation**:
    * **Orientation**: Sets the starting direction of the pattern (Up, Right, Down, Left). An 'auto' mode adapts to the image dimensions.
    * **Steps**: Controls the number of recursive divisions within the pattern.
    * **Draw Spiral**: Toggles the visibility of the spiral curve.

* **Fitting & Sizing**:
    * **Fit Mode**: 'Crop' maintains the golden ratio, potentially leaving empty space, while 'Stretch' fits the pattern to the image's aspect ratio.
    * **Crop Offset**: When in 'Crop' mode, this adjusts the pattern's position within the image frame.
    * **Axial Stretch**: Allows for manual stretching or squashing of the pattern along its main axis for artistic adjustments.

* **Projection & Transforms**:
    * **Offset X/Y**: Moves the entire pattern across the image.
    * **Rotation**: Rotates the pattern from -360 to 360 degrees.
    * **Scale**: Uniformly zooms the pattern in or out from its center.
    * **Flip Horizontal/Vertical**: Flips the pattern's orientation.

* **Line & Style Settings**:
    * **Line Color**: Sets the color of the overlay pattern.
    * **Line Thickness**: Controls the base thickness of the lines.
    * **Uniform Line Width**: When enabled, prevents line thickness from changing during uniform scaling.
    * **Blend Mode**: Sets the canvas blend mode for the overlay effect.


## Requirements

* PyTorch – (you should have this if you have ComfyUI installed).


## Installation

1.  **Navigate to your ComfyUI custom nodes directory:**
    ```
    ComfyUI/custom_nodes/
    ```

2.  **Clone this repository:**
    ```
    git clone https://github.com/quasiblob/EsesCompositionGoldenRatio.git
    ```

3.  **Restart ComfyUI:**
    * After restarting, the "Eses Composition Golden Ratio" node will be available in the "Eses Nodes/Visualization" category.



## Folder Structure

```
ComfyUI-EsesImageLoader/
├── init.py                      # Main module defining the custom node.
├── composition_golden_ratio.py  # The Python file containing the node logic.
└── README.md                    # This file.
```


## Usage

* Connect an image to the 'image' input. 
* The golden ratio guide will appear as an overlay on the preview image within the node itself. 
* Adjust the various parameters to manipulate the guide's position, size, and appearance in real-time. 
* The output 'image' tensor remains unaltered.


## Category

Eses Nodes/Visualization


## Contributing

* Feel free to report bugs and improvement ideas in issues, but I may not have time to do anything.


## License

* See LICENSE.txt


## About

-

## Update History

* 2025.6.30 Version 1.0.2 public version

* 2025.6.28 Version 1.0.1 fixed node collapse related issue (node JS elements visible on canvas)

* 2025.6.28 Version 1.0.0 released


## ⚠️Disclaimer⚠️

This custom node for ComfyUI is provided "as is," without warranty of any kind, express or implied. By using this node, you agree that you are solely responsible for any outcomes or issues that may arise. Use at your own risk.


## Acknowledgements

Thanks to the ComfyUI team and community for their ongoing work!