# Eses Image Effect Levels

![Eses Image Effect Levels Node Screenshot](docs/image_levels.png)


> [!CAUTION]
> Before downloading and using the contents of this repository, please review the LICENSE.txt and the disclaimer.
> I kindly ask that you respect the licensing terms and the effort put into these tools to ensure their 
> continued availability for everyone. Thank you!


## Description

The 'Eses Image Effect Levels' is a ComfyUI custom node that provides a real-time levels adjustment tool directly within the user interface. It allows for interactive control over the tonal range of both images and masks, using a GPU-accelerated PyTorch backend for near instant feedback.

This node is a single tool for tonal adjustments without the need to chain multiple nodes together. All level settings are saved with your workflow and are restored when you reload the page, ensuring a seamless and non-destructive workflow.

💡 No other requirements than having ComfyUI installed.

💡 NEW - Output black and white points adjustment

💡 NEW - Auto Levels and Auto Colors buttons


## Features

* **Interactive Level Sliders**:
    * Adjust input levels with live feedback using Black, Mid, and White point sliders.
    * Control the final output range with Output Black and Output White settings.
    * A live histogram is displayed directly on the node, updating as you change channels.

* **Multi-Channel Adjustments**:
    * Apply levels to the combined RGB channels for overall tonal control.
    * Isolate adjustments to individual Red, Green, or Blue channels for precise color grading.
    * Apply a separate, dedicated level adjustment directly to an input mask!

* **State Serialization**:
    * All level adjustments for all channels are saved with your workflow.
    * The node's state, including manually resized dimensions, persists even after refreshing the browser page.

* **Quality of Life Features**:
    * Automatic resizing of the node to best fit the aspect ratio of the input image.
    * "Set Auto Levels" and "Set Auto Color" buttons to automatically find optimal black and white points.
    * "Reset All Levels" button to instantly revert all channels to their default state.

* **Save Presets Feature**:
    * Adjust settings and then enter your preset name in the field, then press the `Save Preset` button.
    * Next time you reload ComfyUI or its webpage, the new preset can be found in the `Preset` -dropdown.



## Requirements

* PyTorch – you should have this if you have ComfyUI installed.


## Installation

1.  **Navigate to your ComfyUI custom nodes directory:**
    ```
    ComfyUI/custom_nodes/
    ```
2.  **Clone this repository:**
    ```
    git clone https://github.com/quasiblob/ComfyUI-EsesImageEffectLevels.git
    ```
3.  **Restart ComfyUI:**
    * After restarting, the "Eses Image Effect Levels" node will be available in the "Eses Nodes/Image Adjustments" category.


## Folder Structure

```
ComfyUI-EsesImageEffectLevels/
├── init.py                      # Main module defining the custom nodes.
├── image_effect_levels.py       # The Python file containing the node logic.
├── js/                          # Folder for JavaScript files.
│   └── image_effect_levels.js   # Frontend logic for the interactive node.
├── README.md                    # This file.
└── LICENSE.txt                  # You should read this before using this node.
```


## Usage

* Connect an `image` and/or a `mask` tensor to the corresponding inputs.
* Select the `channel` you wish to adjust from the dropdown menu inside the node.
* Use the sliders to modify the image or mask tones.
* The node outputs both the original and the adjusted image/mask for flexible workflow routing.


## Inputs

* **image** (`IMAGE`, *optional*): The input image to be adjusted.
* **mask** (`MASK`, *optional*): The input mask to be adjusted.


## Outputs

* **image** (`IMAGE`): A passthrough of the original input image.
* **mask** (`MASK`): A passthrough of the original input mask.
* **adjusted_image** (`IMAGE`): The image after the level adjustments have been applied.
* **adjusted_mask** (`MASK`): The mask after the level adjustments have been applied.


## Category

Eses Nodes/Image Adjustments


## Contributing

- Feel free to report bugs and improvement ideas in issues, but I may not have time to do anything.


## License

- See LICENSE.txt


## About

-


## Version History

**2025.7.24 Version 1.3.1** Auto levels and auto color functionality, with adjustable sensitivity control

**2025.7.10 Version 1.2.0** Added per channel black and white point adjustments, save name and save button for presets

**2025.7.10 Version 1.1.0** Released public version

**2025.7.3 Version 1.0.0** Added histogram display



## ⚠️Disclaimer⚠️

This custom node for ComfyUI is provided "as is," without warranty of any kind, express or implied. By using this node, you agree that you are solely responsible for any outcomes or issues that may arise. Use at your own risk.


## Acknowledgements

Thanks to the ComfyUI team and community for their ongoing work!