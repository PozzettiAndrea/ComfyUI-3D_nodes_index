# Kaizen Package

A collection of high-quality custom nodes for ComfyUI focused on image processing and compositing.

## Features

-   **Image Composite**: Professional mask-based image compositing with precise positioning
    -   Overlay images with pixel-perfect positioning (supports negative coordinates)
    -   Alpha blending using masks for smooth transitions
    -   Automatic size matching between mask and source images
    -   Handles edge cases and out-of-bounds positioning gracefully

## Installation

### Via ComfyUI Manager (Recommended)

1. Install [ComfyUI](https://docs.comfy.org/get_started)
2. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. Search for "Kaizen Package" in ComfyUI-Manager and install
4. Restart ComfyUI

### Manual Installation

1. Clone this repository to `ComfyUI/custom_nodes/`:
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/aleolidev/kaizen_package.git
    ```
2. Install dependencies:
    ```bash
    cd kaizen_package
    pip install -r requirements.txt
    ```
3. Restart ComfyUI

## Usage

After installation, you'll find the following nodes under the `kaizen/image` category:

### Image Composite

Composite two images using a mask for alpha blending.

**Inputs:**

-   `background`: Background image that will receive the overlay
-   `foreground`: Image to be overlaid onto the background
-   `mask`: Alpha mask controlling opacity (1.0=opaque, 0.0=transparent)
-   `x`: Horizontal position (supports negative values)
-   `y`: Vertical position (supports negative values)

**Output:**

-   `composite`: The final composited image

## Development

To set up for development:

```bash
cd kaizen_package
pip install -e .[dev]
pre-commit install
```

The `-e` flag creates a "live" install where changes are automatically picked up when you restart ComfyUI.

## Testing

Run the test suite:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the GNU General Public License v3 - see the [LICENSE](LICENSE) file for details.

## Support

-   Report bugs: [GitHub Issues](https://github.com/aleolidev/kaizen_package/issues)
-   Join our community: [ComfyUI Discord](https://discord.com/invite/comfyorg)
