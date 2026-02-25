# ComfyUI Stability AI API

**ComfyUI Stability AI API** is a collection of custom nodes that integrate the Stability AI API with ComfyUI. These nodes enable you to perform a variety of creative tasks—from image generation and editing to upscaling, video generation, and even 3D asset creation and preview.

## Features

- **Image Generation**
  - *StabilityImageCore*: Generate images using Stability Core.
  - *StabilityImageSD3*: Generate images with Stability SD3.
  - *StabilityImageUltra*: Generate images using Stability Ultra.

- **Image Editing**
  - *StabilityEdit*: Edit images (e.g., erase, inpaint, outpaint, search-and-replace, search-and-recolor, and remove background).
  - *StabilityControlSketch*: Create images from sketches or outlines.
  - *StabilityControlStructure*: Generate images while preserving the structure of the input.
  - *StabilityControlStyle*: Generate images with style control.

- **Image Upscaling**
  - *StabilityUpscaleFast*: Fast image upscaling.
  - *StabilityUpscaleConservative*: Conservative upscaling for minimal artifacts.
  - *StabilityUpscaleCreative*: Creative upscaling with adjustable creativity.

- **3D Asset Creation & Preview**
  - *StableFast3D*: Generate 3D assets from a single 2D image quickly.
  - *StablePointAware3D*: Generate detailed 3D models using point-aware diffusion.
  - *Preview3DModel*: Preview 3D models using a built-in Three.js viewer.
  - *Save3DModel*: Save 3D models to disk.

- **Video Generation**
  - *StabilityImageToVideo*: Create videos from images by combining frames.

## Installation

You can install this custom nodes via ComfyUI Manager, or clone the repository and install the dependencies:

```bash
git clone https://github.com/yhayano-ponotech/comfyui-stability-ai-api.git
cd comfyui-stability-ai-api
pip install -r requirements.txt

```

## API Key Configuration

There are two methods for providing your Stability AI API key:

1.  **Via config.ini**  
    On the first run, a `config.ini` file is automatically generated in the project directory. You can open this file and set your API key under the appropriate section. The nodes will use this API key by default.
    
2.  **Directly via Node Input**  
    Each node has an optional `api_key` input. You can directly provide your API key in this field when building your workflow. This method overrides any API key set in `config.ini` for that node.
    

## Usage

After installation, load the nodes into ComfyUI to start building your workflows. For example:

-   **Image Generation Workflow:** Use the _StabilityImageCore_, _StabilityImageSD3_, or _StabilityImageUltra_ node to generate images from text prompts.
-   **Image Editing Workflow:** Use the _StabilityEdit_ node to modify images using techniques like inpainting or outpainting.
-   **Upscaling Workflow:** Use one of the upscale nodes (_Fast_, _Conservative_, or _Creative_) to enhance image resolution.
-   **3D Workflows:** Combine the _StableFast3D_ or _StablePointAware3D_ nodes with _Preview3DModel_ and _Save3DModel_ for 3D asset generation and preview.
-   **Video Workflow:** Use the _StabilityImageToVideo_ node to convert images into video sequences.

Example workflow JSON files are provided in the `examples/` directory. Import these files into ComfyUI to see sample setups.

## Development & Publishing

To update or publish a new version:

1.  Update the version number in `pyproject.toml`.
2.  Push changes to the `main` or `master` branch.
3.  The GitHub Actions workflow defined in `.github/workflows/publish.yml` will automatically publish the new version to the Comfy Registry.

## License

This project is licensed under the terms specified in the [LICENSE](https://chatgpt.com/c/LICENSE) file.

## Contact & Support

For questions, issues, or further support, please open an issue in the [GitHub repository](https://github.com/yhayano-ponotech/comfyui-stability-ai-api).

----------

Happy creating with ComfyUI and Stability AI!

