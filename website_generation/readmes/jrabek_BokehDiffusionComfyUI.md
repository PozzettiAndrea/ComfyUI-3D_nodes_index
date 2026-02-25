# ComfyUI Bokeh Diffusion

ComfyUI custom nodes for Bokeh Diffusion - Defocus Blur Control in Text-to-Image Diffusion Models.

This package provides ComfyUI nodes to add bokeh (defocus blur) control to FLUX models.

## Installation

1. Copy this directory (`ComfyUI_BokehDiffusion`) to your ComfyUI `custom_nodes` folder:
   ```
   cp -r ComfyUI_BokehDiffusion /path/to/ComfyUI/custom_nodes/
   ```

2. Install dependencies (if not already installed):
   ```bash
   pip install diffusers transformers huggingface_hub
   ```

## Usage

### Basic Workflow

1. **Load FLUX Model** - Use ComfyUI's standard model loading nodes to load a FLUX model
2. **Load Bokeh Adapter** - Use the `Load Bokeh Adapter` node to load the adapter from HuggingFace
3. **Apply Bokeh Adapter** - Connect your FLUX model and adapter to `Apply Bokeh Adapter`
4. **Set Bokeh Level** - Use `Bokeh Level` node to set the desired bokeh level (0-30)
5. **Generate** - Use `Bokeh KSampler` instead of the standard KSampler for generation

### Node Descriptions

#### Load Bokeh Adapter
- **adapter_name**: HuggingFace model ID (default: "atfortes/BokehDiffusion")
- **bokeh_scale**: Scale factor for bokeh effect (default: 1.0)
- **lora_scale**: Scale factor for LoRA components (default: 1.0)

#### Apply Bokeh Adapter
- **model**: FLUX model from ComfyUI's model loader
- **adapter**: Adapter from `Load Bokeh Adapter` node

#### Bokeh Level
- **bokeh_level**: Bokeh level from 0 (sharp) to 30 (maximum blur)
- **bokeh_pivot**: (Optional) Pivot bokeh level for grounded generation
- **num_grounding_steps**: (Optional) Number of grounding steps for scene consistency (0 = disabled, 18-24 recommended)

#### Bokeh KSampler
- **model**: Model with bokeh adapter applied
- **positive**: Positive conditioning
- **negative**: Negative conditioning
- **latent_image**: Initial latent image
- **seed**: Random seed
- **steps**: Number of inference steps
- **cfg**: Guidance scale
- **sampler_name**: Sampler name (e.g., "euler")
- **scheduler**: Scheduler name (e.g., "normal")
- **bokeh_control**: Bokeh control from `Bokeh Level` node
- **true_cfg**: (Optional) True CFG scale for negative prompt

### Example Workflow

```
[Load Checkpoint] -> [Apply Bokeh Adapter] -> [Bokeh KSampler]
                              ^
                              |
                    [Load Bokeh Adapter]

[CLIP Text Encode] -> [Bokeh KSampler]
                              ^
                              |
                    [Bokeh Level] -> [Bokeh KSampler]
```

## Features

- **Unbounded Generation**: Control bokeh level from 0 to 30
- **Grounded Generation**: Scene-consistent bokeh transitions using grounding steps
- **Standard ComfyUI Integration**: Works with standard ComfyUI nodes (model loading, VAE, CLIP, etc.)

## Notes

- This node requires a FLUX model (e.g., FLUX.1-dev)
- The adapter modifies the model's attention processors, so the model must support this
- For best results with grounded generation, use 18-24 grounding steps
- Bokeh level is normalized from 0-30 range to 0-1 internally

## License

This project is licensed under [NTU S-Lab License 1.0](https://github.com/atfortes/BokehDiffusion/blob/main/LICENSE).

## Credits

Based on the work by:
- Armando Fortes, Tianyi Wei, Shangchen Zhou, Xingang Pan
- Original repository: https://github.com/atfortes/BokehDiffusion

