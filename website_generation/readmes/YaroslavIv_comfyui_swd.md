# SwD Preset Selector for ComfyUI

The **SwD Preset Selector** is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that provides a simple way to select predefined SwD configurations. This node outputs three values:
- **Image Size (INT):** The base image resolution.
- **Upscale Values (STRING):** A comma-separated string representing the upscale factors.
- **Sigmas (SIGMAS):** A tensor containing sigma values (as a PyTorch tensor) used in custom sampling.

> **Note:** This node utilizes concepts from the [SwD module](https://github.com/yandex-research/swd) by Yandex Research.

## Features

- **Preset Options:** Choose between multiple presets:
  - *SwD 2B, 6 steps*
  - *SwD 2B, 4 steps*
  - *SwD 8B, 6 steps*
  - *SwD 8B, 4 steps*
  - *SwD FLUX, 4 steps*

## Installation

1. Clone this repo into `custom_nodes` folder.
2. **Restart ComfyUI.** The node should now appear in the **SwD** category as **SwD Preset Selector**.

## Dependency

This custom node relies on the methodology introduced in the [SwD module](https://github.com/yandex-research/swd) by Yandex Research. Please refer to that repository for further details and implementation guidelines.

## Contributing

Contributions and suggestions are welcome! If you have any improvements or bug fixes, please create an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for providing the base UI framework.
- [SwD module by Yandex Research](https://github.com/yandex-research/swd) for the core ideas and implementation details.