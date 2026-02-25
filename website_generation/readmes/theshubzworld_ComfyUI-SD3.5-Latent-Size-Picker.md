
# 🔧 Universal Empty Latent Size Picker

A versatile node for generating empty latent tensors with support for SD3.5, SDXL, and Flux models. This node offers extensive aspect ratio support, batch processing, and flexible dimension overrides, ensuring optimal performance across different model types.

## Features

- **Wide Range of Resolutions**: Extensive list of predefined resolutions covering various aspect ratios
- **Model Agnostic**: Works with SD3.5, SDXL, and Flux models
- **Aspect Ratio Control**: Built-in aspect ratio locking for consistent results
- **Flexible Overrides**: Custom width/height overrides with aspect ratio preservation
- **Performance Optimized**: Efficient tensor creation with minimal overhead
- **Batch Processing**: Generate multiple latent tensors in a single operation
- **Downsample Control**: Adjustable downsample factor for different model requirements

## Parameters

- **resolution**: Dropdown list of pre-configured resolutions (default: `"1024x1024 (1:1)"`)
- **batch_size**: Number of latent tensors to generate (default: `1`)
- **width_override** / **height_override**: Custom dimensions (0 = use preset)
- **aspect_ratio_lock**: Lock aspect ratio to width, height, or unlocked
- **latent_channels**: Number of channels in latent space (default: `4`)
- **downsample_factor**: Model scaling factor (auto/4/8)
- **invert_ratios**: Swap width and height dimensions

## Output

The node returns:
- **LATENT**: A tensor with dimensions `[batch_size, 4, height // 8, width // 8]`, representing empty latent samples ready for further processing.
- **width**: Effective width, accounting for overrides and constraints.
- **height**: Effective height, accounting for overrides and constraints.

## Example Code

Here’s an example of how to use this node programmatically:

```python
import torch
from ComfyUI-SD3.5-Latent-Size-Picker.sd3_5_empty_latent import SD3_5EmptyLatent

# Initialize the SD3_5EmptyLatent node
latent_picker = SD3_5EmptyLatent()

# Set parameters
resolution = "1024x1024 (1.0)"
batch_size = 2
width_override = 768
height_override = 0
invert_ratios = "No"

# Execute to generate the latent tensor
latent_output, width, height = latent_picker.execute(
    resolution=resolution,
    batch_size=batch_size,
    width_override=width_override,
    height_override=height_override,
    invert_ratios=invert_ratios
)

print(f"Latent Shape: {latent_output['samples'].shape}, Width: {width}, Height: {height}")
```

## Installation

To use this node in ComfyUI:
1. Clone the repository into the `custom_nodes` folder in ComfyUI:

    ```bash
    git clone https://github.com/mithamunda/ComfyUI-SD3.5-Latent-Size-Picker.git
    ```

2. Restart ComfyUI to enable the node in the interface.

## License

This code is released under the MIT License, allowing for free use, distribution, and modification. See the `LICENSE` file for more details.
