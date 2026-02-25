# Flux Pro Nodes for ComfyUI

This plugin adds a new node to ComfyUI. The node uses the FLUX.1 Fill API to fill in parts of an image.

## Installation

1. Clone this repository to your ComfyUI `custom_nodes` directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   git clone https://github.com/Altair200333/ComfyUI_Flux_1.1_PRO
   ```

2. Open the `config.ini` file in the extension folder and add your API key:
   ```ini
   [API]
   API_KEY=your_api_key_here
   BASE_URL=https://api.us1.bfl.ai
   ```

3. Restart ComfyUI.

## Usage

After installation, you will see 3 new nodes in the "BFL" category.

### Provided Nodes
- **Flux Generate 1.1 [Pro, Ultra, Raw]**: This node generates images using the Flux API. Can also accept image input
- **Flux Pro 1.0 Fill [Inpaint]**: This node fills parts of an image based on a text prompt for inpainting and mask.
- **Flux Pro 1.0 Extend [Outpaint]**: This node extends images from the edges to produce outpainting results.


## API Information

For more details, see the API documentation.

```
https://api.us1.bfl.ai/scalar#tag/tasks/POST/v1/flux-pro-1.1
```

Examples:

## Image Examples

Below are image examples demonstrating the inpaint and outpaint functionalities:

|Source | Inpaint | Outpaint
|-------|-------|-------|
|![Inpaint Before](imgs/ref_1.png) | ![Inpaint After](imgs/inpaint_1.png) | ![Outpaint After](imgs/outpaint_1.png) |