# ComfyUI-ClownSampler

A standalone ComfyUI node for loading `RES4LYF` samplers and providing their names as string outputs.

## Installation

1. Clone this repository into your `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/YOUR_GITHUB_USERNAME/ComfyUI-ClownSampler.git
   ```
2. Restart ComfyUI.

## Usage

Find the **Clown Sampler Loader 🐉** node in the **ClownNodes** category.

- **sampler**: Regular ComfyUI samplers.
- **clownsampler**: Dropdown with `RES4LYF` samplers. If selected (not 'none'), it takes precedence.
- **scheduler**: Regular ComfyUI schedulers.

Outputs:
- **sampler_name**: The name of the selected sampler (string).
- **Sampler**: The sampler object.
- **schedular_name**: The name of the selected scheduler (string).
- **Schedular**: The scheduler object.
