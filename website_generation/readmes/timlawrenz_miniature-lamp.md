# DINO-Guided Image Upscaler

A semantic-aware image upscaling tool that uses DINOv2 vision transformer embeddings to guide diffusion models, maintaining object identity and characteristics during upscaling.

## Overview

This project combines tiled upscaling with DINO semantic embeddings to maintain object identity and characteristics during the upscaling process, preventing common hallucination artifacts that occur with standard upscaling.

**Key Features:**
- 🎯 Semantic-aware upscaling using DINOv2 embeddings
- 🚀 **Model-agnostic** - Works with ANY ComfyUI diffusion model (SD 1.5, SDXL, FLUX, etc.)
- 🧩 Tiled processing for large images with seamless blending
- 💾 Uses external models from your workflow (no internal model loading)
- ⚙️ Configurable parameters for quality vs speed tradeoffs
- 🎨 Lightweight - No FLUX dependencies

## Current Status

- ✅ **ComfyUI Node v2.0:** Model-agnostic upscaling via ComfyUI's native samplers
- ✅ **Works with any model:** SD 1.5, SDXL, FLUX, and future models
- 📋 **Available on ComfyUI Registry:** Install via ComfyUI Manager

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "DINO Upscale"
3. Click Install
4. Restart ComfyUI

### Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/timlawrenz/miniature-lamp.git comfyui-dino-upscale
cd comfyui-dino-upscale
pip install -r requirements.txt
# Restart ComfyUI
```

**Requirements:**
- Python 3.8+
- ComfyUI
- CUDA-capable GPU (4GB+ VRAM recommended)
- Any ComfyUI-compatible diffusion model

## Quick Start

The node will appear under: `Add Node` → `image` → `upscaling` → `DINO Upscale`

See [ComfyUI Usage](#comfyui-node-usage) below for parameter details.

### Standalone Usage (Legacy)

For development or standalone testing:

```bash
# Simple bicubic upscaling (no diffusion model)
python examples/simple_poc.py image.jpg
```

## Parameter Reference (Legacy Standalone)

These parameters apply to the standalone scripts in `examples/`:

### Core Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `image` | str | *required* | Path to input image |
| `--scale` | float | `2.0` | Upscale factor (e.g., 2.0 = 2x, 1.5 = 1.5x) |

For ComfyUI usage, see [ComfyUI Node Usage](#comfyui-node-usage) section below.

## Usage Examples (ComfyUI)

### Conservative Enhancement
For subtle improvements that stay close to the original:

**Parameters:**
- `denoise`: 0.1-0.2
- `dino_strength`: 0.7-0.9
- `steps`: 15-20

**When to use:** Product photos, portraits, archival images

### Balanced Upscaling
Good balance of enhancement and preservation:

**Parameters:**
- `denoise`: 0.2-0.3
- `dino_strength`: 0.5
- `steps`: 20

**When to use:** General purpose upscaling, photography

### Creative Enhancement
More freedom for the diffusion model to add details:

**Parameters:**
- `denoise`: 0.4-0.6
- `dino_strength`: 0.3-0.5
- `steps`: 25-30

**When to use:** Artistic images, low-quality sources, creative projects

## Parameter Guide

### `denoise` (Denoising Strength)

Controls how much the diffusion model modifies the image:

| Value | Effect | Use Case |
|-------|--------|----------|
| `0.01-0.1` | Minimal changes, mostly upscaling | Preserve original exactly |
| `0.15-0.25` | Subtle enhancement | Product photos, documentation |
| `0.3` (default) | Moderate enhancement | General purpose |
| `0.4-0.6` | Significant changes | Creative work, quality improvement |
| `0.7+` | Heavy modification | Artistic interpretation |

### `dino_strength` (Semantic Conditioning)

Controls influence of DINO semantic features:

| Value | Effect | Use Case |
|-------|--------|----------|
| `0.0` | No DINO guidance | Test diffusion model alone |
| `0.1-0.3` | Light semantic guidance | Subtle preservation |
| `0.5` (default) | Moderate guidance | Balanced |
| `0.7-0.9` | Strong guidance | Maximum preservation |

### `tile_size` (Processing Tiles)

Different models work best at different resolutions:

| Model Type | Recommended tile_size | Why |
|------------|---------------------|-----|
| Stable Diffusion 1.5 | 512 | Trained on 512×512 images |
| FLUX | 1024 | Optimal at higher resolutions |
| SDXL | 1024 | Trained on 1024×1024 images |

## Programmatic Usage (Legacy Standalone)

```python
from src.dino_extractor import DINOFeatureExtractor
from src.upscaler import BasicUpscaler
from PIL import Image

# Initialize components
extractor = DINOFeatureExtractor()
upscaler = BasicUpscaler(
    dino_extractor=extractor,
    scale_factor=2.0
)

# Load and upscale
image = Image.open("photo.jpg")
result = upscaler.upscale(image)
result.save("upscaled.jpg")
```

For ComfyUI workflows, use the node directly in the visual editor.

## Troubleshooting

### Out of Memory Errors

- Reduce `tile_size` (e.g., from 1024 to 512)
- Use lower `denoise` values
- Process smaller images

### Output Looks Different Than Expected

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for:
- Parameter tuning guide
- Common issues and solutions
- Quality troubleshooting
- Systematic debugging approach

## Documentation

- **[ComfyUI Installation](docs/INSTALLATION.md)** - ComfyUI node installation and troubleshooting
- **[ComfyUI Usage](docs/COMFYUI_NODE_README.md)** - ComfyUI node parameters and examples
- **[TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[DEBUG_PLAN.md](docs/DEBUG_PLAN.md)** - Systematic debugging approach
- **[DINO_CONDITIONING.md](docs/DINO_CONDITIONING.md)** - DINO parameter guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development guidelines
- **[IMPLEMENTATION_SUMMARY.md](docs/IMPLEMENTATION_SUMMARY.md)** - Technical details

## ComfyUI Integration

A ComfyUI custom node is included in this repository:

```bash
# Install the repository to ComfyUI
cd ComfyUI/custom_nodes/
git clone https://github.com/timlawrenz/miniature-lamp.git
cd miniature-lamp
pip install -r requirements.txt
# Restart ComfyUI
```

The node will appear under: `Add Node` → `image` → `upscaling` → `DINO Upscale`

**Files**: `__init__.py`, `nodes.py`, `utils.py` in repository root.

See [docs/INSTALLATION.md](docs/INSTALLATION.md) for detailed installation and troubleshooting.

## How It Works

1. **DINO Feature Extraction** - DINOv2 extracts semantic patch embeddings (768-dim vectors for each 14×14 pixel patch)
2. **Feature Projection** - DINO features are projected to the diffusion model's latent space
3. **Tiled Processing** - Large images are split into overlapping tiles with configurable size
4. **Diffusion Enhancement** - Each tile is upscaled using img2img with DINO guidance
5. **Seamless Stitching** - Tiles are blended with gradient masks for smooth transitions

## Performance

Performance varies based on the diffusion model used:

| Image Size | Method | Typical Time | VRAM | Quality |
|------------|--------|--------------|------|---------|
| 512×512 | Bicubic | <1s | Minimal | Basic |
| 512×512 | SD 1.5 (20 steps) | ~5-10s | 6GB | Good |
| 512×512 | SD 1.5 (20 steps) | ~5-10s | 6GB | Good |
| 512×512 | SDXL (20 steps) | ~15s | 10GB | Excellent |
| 1024×1024 | Tiled processing | 2-4x longer | Same | Good |

*Times are approximate and depend on GPU hardware. First run includes model loading overhead.*

## Known Limitations

1. **DINO Conditioning** - Features are prepared but full cross-attention integration is WIP
2. **Speed** - Diffusion processing is significantly slower than simple upscaling (quality tradeoff)
3. **VRAM** - Requires 6-12GB GPU memory depending on model
4. **Tile Size** - Configurable but larger tiles require more VRAM

## Development

```bash
# Run tests
pytest tests/ -v

# Run with debug logging
python examples/simple_poc.py image.jpg 2>&1 | tee debug.log

```

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## Project Status & Roadmap

### ✅ Completed
- DINO feature extraction
- Diffusion model integration (model-agnostic)
- DINO conditioning adapter
- Tiled processing with seamless blending
- Memory optimizations (offloading, fp16)
- ComfyUI custom node
- Published on ComfyUI Registry

### 🚧 In Progress
- Full cross-attention DINO injection
- Documentation improvements
- Performance profiling

### 📋 Planned
- Batch processing support
- Additional upscaling strategies
- Model-specific optimizations

## References

- [DINOv2 Paper](https://arxiv.org/abs/2304.07193) - Self-supervised vision transformers
- [Ultimate SD Upscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale) - Tiled upscaling inspiration

## License

MIT License - See [LICENSE.txt](LICENSE.txt) for details

## Acknowledgments

- DINOv2 by Meta AI Research
- Diffusers library by Hugging Face
- ComfyUI community

## Citing DINOv2

If you use this tool in your research or projects, please cite the original DINOv2 work:

```bibtex
@misc{oquab2023dinov2,
  title={DINOv2: Learning Robust Visual Features without Supervision},
  author={Oquab, Maxime and Darcet, Timothée and Moutakanni, Theo and Vo, Huy V. and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and Howes, Russell and Huang, Po-Yao and Xu, Hu and Sharma, Vasu and Li, Shang-Wen and Galuba, Wojciech and Rabbat, Mike and Assran, Mido and Ballas, Nicolas and Synnaeve, Gabriel and Misra, Ishan and Jegou, Herve and Mairal, Julien and Labatut, Patrick and Joulin, Armand and Bojanowski, Piotr},
  journal={arXiv:2304.07193},
  year={2023}
}

@misc{darcet2023vitneedreg,
  title={Vision Transformers Need Registers},
  author={Darcet, Timothée and Oquab, Maxime and Mairal, Julien and Bojanowski, Piotr},
  journal={arXiv:2309.16588},
  year={2023}
}

@misc{jose2024dinov2meetstextunified,
  title={DINOv2 Meets Text: A Unified Framework for Image- and Pixel-Level Vision-Language Alignment}, 
  author={Cijo Jose and Théo Moutakanni and Dahyun Kang and Federico Baldassarre and Timothée Darcet and Hu Xu and Daniel Li and Marc Szafraniec and Michaël Ramamonjisoa and Maxime Oquab and Oriane Siméoni and Huy V. Vo and Patrick Labatut and Piotr Bojanowski},
  journal={arXiv:2412.16334},
  year={2024}
}
```

## ComfyUI Node Usage

The DINO Upscale node can be used in ComfyUI workflows with the following parameters:

### Required Parameters

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| `image` | IMAGE | - | - | Input image to upscale |
| `scale_factor` | FLOAT | 2.0 | 1.0-4.0 | Upscaling factor |
| `denoise` | FLOAT | 0.2 | 0.0-1.0 | Img2img denoising strength |
| `tile_size` | INT | 1024 | 512-2048 | Output tile dimensions (SD: 512, FLUX: 1024, SDXL: 1024) |
| `sampler_name` | DROPDOWN | euler | - | Sampling algorithm (euler, dpmpp_2m, etc.) |
| `scheduler` | DROPDOWN | normal | - | Noise schedule (normal, karras, exponential, etc.) **¹** |
| `steps` | INT | 20 | 1-100 | Number of inference steps |
| `dino_enabled` | BOOLEAN | True | - | Enable DINO semantic guidance |
| `dino_strength` | FLOAT | 0.5 | 0.0-1.0 | DINO conditioning weight |
| `seed` | INT | 0 | - | Random seed for reproducibility |
| `model` | MODEL | - | - | Diffusion model from Load Checkpoint node |
| `vae` | VAE | - | - | VAE from Load Checkpoint node |

### Optional Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `prompt` | STRING | Text prompt for guidance |

**¹ Scheduler and Sampler Discovery:** The node automatically detects all available schedulers and samplers from ComfyUI, including any custom ones installed via custom nodes. This means if you install a custom scheduler (like FlowMatchEulerDiscreteScheduler), it will automatically appear in the dropdown without needing to update the node code.

### Parameter Guide

#### `denoise` vs `dino_strength`

These are two **independent** controls:

- **`denoise`**: Controls how much the diffusion model modifies the image
  - `0.0` = No changes, pure upscale
  - `0.2` = Subtle enhancement (recommended for most cases)
  - `1.0` = Complete regeneration

- **`dino_strength`**: Controls how strongly DINO semantic features guide the process
  - `0.0` = No DINO guidance
  - `0.5` = Balanced semantic preservation
  - `1.0` = Maximum semantic consistency

**Example combinations:**
- Low denoise (0.2) + High DINO (0.8) = Minimal changes, strong semantic preservation
- High denoise (0.5) + Low DINO (0.2) = More creative freedom, less semantic constraint

#### `tile_size` Recommendations

Different models work best at different resolutions:

| Model Type | Recommended tile_size | Why |
|------------|---------------------|-----|
| Stable Diffusion 1.5 | 512 | Trained on 512×512 images |
| SDXL | 1024 | Trained on 1024×1024 images |
| FLUX | 1024 | Optimal at higher resolutions |
| Custom models | Varies | Check model documentation |

**Note:** Larger tiles use more VRAM but may produce better coherence.

#### Using External Models (Memory Optimization)

Connect a `Load Checkpoint` node to the `model` input to share models across multiple nodes:

```
[Load Checkpoint] → model → [DINO Upscale]
                  → vae   ↗
```

Benefits:
- Reduces memory usage (no duplicate model loading)
- Faster workflow execution
- Use any FLUX-compatible model from your workflow

### Migration Notes

**For users of previous versions:**

- Parameter `strength` has been renamed to `denoise` to match ComfyUI conventions
- New parameter `tile_size` replaces hardcoded 512 value (default now 1024 for FLUX)
- New parameters `sampler_name` and `scheduler` provide full sampling control
- Optional `model` and `vae` inputs allow memory-efficient workflows

