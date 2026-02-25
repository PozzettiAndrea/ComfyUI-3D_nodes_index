# ComfyUI IO Helpers

A custom nodes package for ComfyUI that enhances workflow flexibility by providing specialized nodes for saving and loading intermediate data. This package makes it easy to store and retrieve encoded prompts and sampled latents in multiple formats, with support for compression to optimize storage space.

![banner](assets/banner.png)

## Features

-   Save and load encoded prompts and sampled latents in multiple formats (pt, pth, npy)
-   Gzip compression support for efficient storage
-   Progress bar integration for better user feedback during operations
-   Clean, modular design with helper classes for file I/O
-   Seamless integration with ComfyUI workflows

## Installation

### Using ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Find and install 'ComfyUI-IO-Helpers' through the manager interface
3. Restart ComfyUI

### Manual Installation

Clone this repository into your ComfyUI custom_nodes directory:

```bash
cd custom_nodes
git clone https://github.com/austinbrown34/comfyui-io-helpers.git
```

## Available Nodes

### Encoded Prompt Nodes

1. **EncodedPromptToFile**

    - Save encoded prompts to file with optional compression
    - Supports multiple output formats (pt, pth, npy)
    - Includes progress tracking

2. **EncodedPromptFromFile**
    - Load encoded prompts from saved files
    - Automatic handling of compressed and uncompressed files
    - Progress tracking during load operations

### Sampled Latents Nodes

1. **SampledLatentsToFile**

    - Save sampled latents to file with optional compression
    - Multiple format support
    - Built-in progress tracking

2. **SampledLatentsFromFile**
    - Load sampled latents from saved files
    - Handles both compressed and uncompressed formats
    - Progress feedback during loading

## Usage Examples

### Saving Encoded Prompts

```python
# Example workflow using EncodedPromptToFile
encoded_prompt_node = EncodedPromptToFile(
    conditioning=your_conditioning,
    filename_prefix="my_prompt",
    output_format="pt",
    compress=True
)
```

### Loading Sampled Latents

```python
# Example workflow using SampledLatentsFromFile
latents_node = SampledLatentsFromFile(
    filepath="path/to/your/latents.pt.gz"
)
```

## Technical Details

### Supported File Formats

-   PyTorch formats (.pt, .pth)
-   NumPy format (.npy)
-   All formats support gzip compression (.gz)

### Dependencies

-   Python 3.x
-   PyTorch >= 1.7
-   NumPy >= 1.19
-   ComfyUI (latest version recommended)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

-   [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - The powerful and modular stable diffusion GUI that makes this project possible
-   Inspired by the needs of the ComfyUI community for better intermediate data handling

## Contact

Austin Brown - austinbrown34@gmail.com

For bugs and feature requests, please open an issue on the GitHub repository.
