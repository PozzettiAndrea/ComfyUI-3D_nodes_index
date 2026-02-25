# ComfyUI Comparison Grid

A custom ComfyUI node that generates comparison grids in a single node. Compare any two parameters (LoRA, strength, seed, steps, CFG, sampler, scheduler, denoise) across rows and columns, with labeled cell images and an assembled grid output.

## Installation

Clone this repo into your ComfyUI `custom_nodes` directory:

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/evandcoleman/comfyui-comparison-grid.git
```

Restart ComfyUI. The node will appear under **image/comparison** as **Comparison Grid**.

## How It Works

The Comparison Grid node replaces what would normally be a large multi-node workflow (100+ nodes for a 4x4 grid) with a single node. Internally it:

1. Parses row and column axis values
2. Pre-loads all needed LoRA weights
3. Iterates over every row/col combination, running the full pipeline per cell:
   - Applies LoRA (if applicable)
   - Samples (KSampler equivalent)
   - Decodes via VAE
   - Overlays a text label ("row_label | col_label")
4. Assembles all cells into a labeled grid image with row/column headers

## Node Inputs

### Required

| Input | Type | Description |
|-------|------|-------------|
| `model` | MODEL | Base diffusion model |
| `clip` | CLIP | CLIP model |
| `vae` | VAE | VAE for decoding |
| `positive` | CONDITIONING | Positive prompt conditioning |
| `negative` | CONDITIONING | Negative prompt conditioning |
| `latent_image` | LATENT | Starting latent (e.g. from EmptyLatentImage) |
| `row_axis` | COMBO | Parameter to vary across rows |
| `row_values` | STRING | One value per line for the row axis |
| `col_axis` | COMBO | Parameter to vary across columns |
| `col_values` | STRING | One value per line for the column axis |
| `default_lora` | COMBO | Default LoRA file (used when lora is not an axis) |
| `default_strength` | FLOAT | Default LoRA strength |
| `default_seed` | INT | Default seed |
| `default_steps` | INT | Default sampling steps |
| `default_cfg` | FLOAT | Default CFG scale |
| `default_sampler` | COMBO | Default sampler algorithm |
| `default_scheduler` | COMBO | Default scheduler |
| `default_denoise` | FLOAT | Default denoise strength |
| `font_size` | INT | Label font size |
| `font_color` | STRING | Label text color (hex, e.g. `#FFFFFF`) |
| `bg_color` | STRING | Label background color (hex, e.g. `#000000`) |

### Optional

| Input | Type | Description |
|-------|------|-------------|
| `font_path` | STRING | Path to a .ttf font file |
| `lora_name` | * | LoRA filename from an upstream download node |
| `lora_N` | * | Additional LoRA filenames (dynamic inputs: `lora_1`, `lora_2`, ...) |

### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `cell_images` | IMAGE | Batch of all labeled cell images (R*C images, row-major) |
| `grid_image` | IMAGE | Single assembled grid image with row/column headers |
| `num_rows` | INT | Number of rows in the grid |
| `num_cols` | INT | Number of columns in the grid |

## Axis Parameters

Any two of these can be used as row/column axes:

| Parameter | Value Format | Example |
|-----------|-------------|---------|
| `lora` | Filename (from `loras/` folder) | `my_lora.safetensors` |
| `strength` | Float | `0.5`, `0.75`, `1.0` |
| `seed` | Integer | `12345`, `67890` |
| `steps` | Integer | `10`, `20`, `30` |
| `cfg` | Float | `1.5`, `4.0`, `7.0` |
| `sampler` | Sampler name | `euler`, `dpmpp_2m_sde` |
| `scheduler` | Scheduler name | `normal`, `karras` |
| `denoise` | Float (0-1) | `0.5`, `0.75`, `1.0` |

Values are entered one per line in the multiline text inputs.

## LoRA Integration

LoRA files are loaded from ComfyUI's standard `loras/` folder via `folder_paths`. There are two ways to provide LoRAs:

### From the dropdown (non-axis default)

Select a LoRA from the `default_lora` dropdown. This is used when lora is not one of the axes.

### From upstream download nodes (axis or default)

Connect one or more `lora_name` / `lora_N` inputs from upstream nodes that output filenames (e.g. [comfyui-model-manager](https://github.com/evandcoleman/comfyui-model-manager)'s `ModelManagerLoRADownload` node).

When lora is an axis, the linked LoRA inputs become the axis values automatically, replacing whatever is in the multiline text field. The label for each LoRA is derived from its filename (extracting "Epoch N" patterns when present).

## Example Workflow

A minimal workflow with this node:

```
UNETLoader ─────────────┐
CLIPLoader ──┬──────────┤
             |          |
CLIPTextEncode(+) ──────┤
CLIPTextEncode(-) ──────┤
VAELoader ──────────────┤
EmptyLatentImage ───────┤
                        |
ModelManagerLoRADownload ──┐
ModelManagerLoRADownload ──┤
ModelManagerLoRADownload ──┤
ModelManagerLoRADownload ──┤
                           ▼
                   ComparisonGrid
                           |
                           ▼
                     SaveImage
```

A companion workflow generator script (`generate_workflow.py`) is available in the [LoRA-Testing](https://github.com/evandcoleman/ComfyUI-Workflows) project that builds this workflow from a simple config.

## License

MIT
