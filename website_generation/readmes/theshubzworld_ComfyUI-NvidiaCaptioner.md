# NVIDIA Captioner for ComfyUI

A powerful ComfyUI node for generating rich, detailed captions for images using NVIDIA's vision models. This node allows batch processing of images with customizable prompts and supports various captioning styles.

![NVIDIA Captioner Node](https://img.shields.io/badge/ComfyUI-Node-important)
![License](https://img.shields.io/badge/License-MIT-blue)
[![GitHub stars](https://img.shields.io/github/stars/theshubzworld/ComfyUI-NvidiaCaptioner?style=social)](https://github.com/theshubzworld/ComfyUI-NvidiaCaptioner/stargazers)

## Features

- 🖼️ Batch process multiple images with a single click
- 🎨 Multiple captioning styles (detailed, concise, product-focused, etc.)
- ⚡ Optimized for performance with rate limiting
- 🔄 Built-in caching to avoid reprocessing the same images
- 📊 Progress tracking for batch operations
- 🔍 Case-insensitive image filtering
- 🎭 Support for custom system prompts

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/theshubzworld/ComfyUI-NvidiaCaptioner.git
   ```

3. Install the required dependencies:
   ```bash
   pip install -r ComfyUI-NvidiaCaptioner/requirements.txt
   ```

4. Restart ComfyUI.

## Usage

1. Add the **NVIDIA Captioner** node to your workflow from the `NVIDIA/Vision` category.
2. Configure the node settings:
   - **Image Directory**: Folder containing images to process
   - **API Key**: Your NVIDIA API key
   - **Model**: Select the vision model to use
   - **Prompt Style**: Choose from various captioning styles
   - **Use Cache**: Toggle to skip already processed images

3. Connect the output to any text node or save the captions to a file.

## Node Configuration

### Inputs
- `image_directory`: Path to directory containing images to process
- `api_key`: Your NVIDIA API key
- `model`: The vision model to use (default: "nvidia/vision")
- `system_prompt_preset`: Predefined prompt styles
- `custom_system_prompt`: Custom prompt (overrides preset if provided)
- `prompt`: Instruction for the model
- `use_cache`: Skip already processed images (default: True)
- `skip_existing_txt`: Skip images with existing .txt files (default: False)
- `max_tokens`: Maximum tokens in response (default: 300)
- `temperature`: Sampling temperature (default: 0.2)
- `top_p`: Nucleus sampling parameter (default: 0.7)
- `frequency_penalty`: Penalize frequent tokens (default: 0.0)
- `presence_penalty`: Penalize new tokens (default: 0.0)
- `max_retries`: Maximum retry attempts (default: 3)
- `retry_delay`: Delay between retries in seconds (default: 2.0)

### Outputs
- `all_captions`: Concatenated captions for all processed images
- `last_caption`: Caption for the most recently processed image

## Example Workflow

1. Load a batch of images using the **Load Batch** node
2. Connect to the **NVIDIA Captioner** node
3. Configure the captioning settings
4. Save or use the generated captions in your workflow

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues and feature requests, please [open an issue](https://github.com/theshubzworld/ComfyUI-NvidiaCaptioner/issues).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing node-based UI
- [NVIDIA](https://www.nvidia.com/) for their powerful vision models
