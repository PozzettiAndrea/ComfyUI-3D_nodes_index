# ComfyUI-VariationLab

A collection of experimental nodes for ComfyUI that enable systematic exploration of generation parameters.

## Features

This custom node collection provides specialized variation nodes for ComfyUI:

### VariationLab: CFG Explorer
- Generate a batch of images with different CFG (Classifier-Free Guidance) values
- Useful for finding the ideal CFG value for your prompt

### VariationLab: Step Explorer
- Generate a batch of images with different step counts
- Perfect for comparing how many steps are needed for good results

### VariationLab: Checkpoint Explorer
- Generate images using multiple checkpoints in a single workflow
- Supports up to 5 different checkpoints with customization for each:
  - Model-specific prompts (suffixes)
  - Clip skip values
  - Samplers, schedulers, CFG values, and step counts

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-VariationLab.git
```

2. Restart ComfyUI

## Usage

### CFG Explorer
Connect model, conditioning (positive/negative), VAE, and latent inputs, then specify:
- Seed value
- Step count
- CFG range (start, end, and number of steps)
- Sampler and scheduler

### Step Explorer
Connect model, conditioning, VAE, and latent inputs, then specify:
- Seed value
- Step range (start, end, and number of steps)
- CFG value
- Sampler and scheduler

### Checkpoint Explorer
Connect a latent input and specify:
- Base prompts (positive/negative)
- Seed value
- Default values for steps, CFG, sampler, etc.
- Up to 5 checkpoints with per-checkpoint customization

## Example Workflows

Example workflows can be found in the `example_workflows` directory:
- `batch_cfg_demo.json`: Demonstrates the CFG Explorer (CFG variation)
- `batch_steps_demo.json`: Demonstrates the Step Explorer (step count variation)
- `batch_checkpoint_demo.json`: Demonstrates the Checkpoint Explorer (model comparison)

> **Note:** If you experience validation errors when loading example workflows, try creating a new workflow from scratch by adding the nodes manually. Ensure you're using valid samplers (like "euler", "euler_ancestral", etc.) and schedulers ("normal", "karras", etc.).

## Future Development

- Improved parameter handling
- Support for more parameter types (sampler exploration, prompt exploration)
- Integration with ComfyUI's queue system
- Modular design for extensible parameter types
- Visual grid layout enhancements

## License

[MIT License](LICENSE) 