# ComfyUI Load Image (File/URL)

A custom ComfyUI node that loads images from either local files or URLs with live preview.

## Features

- **Dual Source**: Switch between local files and URLs with a simple dropdown
- **Live Preview**: See image preview directly in the node for both sources
- **Upload Support**: Upload new images directly from the node
- **Responsive Preview**: Preview scales to fit node size

## Installation

### Via ComfyUI Manager (Recommended)
Search for "Load Image URL" in ComfyUI Manager and click Install.

### Manual Installation
1. Navigate to your ComfyUI's `custom_nodes` folder
2. Clone this repository:
   ```bash
   git clone https://github.com/Braeden90000/comfyui-load-image-url.git load_image_url
   ```
3. Restart ComfyUI

## Usage

1. Add the "Load Image (File/URL)" node from the `image` category
2. Select source: `file` or `url`
3. For files: Use the dropdown to select existing images or click "choose file to upload"
4. For URLs: Paste any direct image URL (supports jpg, png, webp, etc.)

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| source | dropdown | Choose between "file" or "url" |
| image | dropdown | Select from uploaded images |
| url | string | Direct URL to an image |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| IMAGE | IMAGE | The loaded image tensor |
| MASK | MASK | Alpha channel mask (white if no alpha) |

## License

MIT License
