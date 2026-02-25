# ComfyUI-LZNodes

ComfyUI-LZNodes is a collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to simplify complex node workflows and enhance the image generation process. 

Created by Liz.

[日本語版 (Japanese Version)](README_ja.md)

## Features

This extension provides several quality-of-life nodes that condense common workflows:

*   **LZ Pipe System (`LZPipePack` / `LZPipeUnpack`)**: Simplifies "spaghetti" node connections by bundling `MODEL`, `CLIP`, `VAE`, `CONDITIONING`, `LATENT`, and generation parameters into a single `lz_pipe` connection.
*   **Smart Loaders**:
    *   `EZCheckpointLoader`: Loads a checkpoint and automatically encodes positive/negative prompts in a single node.
    *   `LZSimpleCheckpointLoader`: A lightweight loader strictly for extracting model components.
    *   `LZLoRAStacker`: Easily stack up to 10 LoRAs with built-in caching for faster generation.
*   **Prompt Management**:
    *   `AdvancedPositivePrompt` / `AdvancedNegativePrompt`: Cleanly separate base prompts, artist tags, and quality tags. Automatically concatenates and encodes them.
    *   `DualCLIPTextEncode`: Encodes both positive and negative prompts simultaneously.
*   **All-In-One Sampling (`LZKSamplerDecode`)**: Combines KSampler and VAEDecode into a single step, pulling directly from the `lz_pipe` routing. It can also accept raw text and perform CLIP encoding dynamically if conditioning isn't explicitly provided.
*   **Comprehensive Image Saving & Logging (`LZSaveImageAndLog`)**: Saves generated images (PNG/WEBP/JPG) alongside a highly detailed `.txt` log file capturing everything from Seed and Steps to Checkpoint Hash and full Prompt text. It also injects this data into PNG metadata invisibly.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/liz-ils/ComfyUI-LZNodes
   ```
3. Restart ComfyUI.

## Usage

Once installed, the nodes can be found in the ComfyUI add-node menu under the `MyCustomNodes` category (e.g., `MyCustomNodes/Loaders`, `MyCustomNodes/Prompt`, `MyCustomNodes/Sampling`, etc.). 

*Tip: A great starting point is connecting an `EZCheckpointLoader` through an `LZPipePack` to an `LZKSamplerDecode`, and finishing with `LZSaveImageAndLog`.*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
