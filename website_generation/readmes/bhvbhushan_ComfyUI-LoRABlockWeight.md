# ComfyUI LoRA Block Weight Loader

A production-ready ComfyUI custom node that provides per-block weight control for LoRA loading. Apply different LoRA strengths to specific transformer blocks for fine-grained control over model behavior. Compatible with Flux, Nunchaku, and standard Stable Diffusion models.

## 🎯 Key Features

- **Per-Block Weight Control**: Apply different LoRA strengths to specific transformer blocks
- **Universal Compatibility**: Works with Flux, Nunchaku, SDXL, and SD 1.5 models
- **Multiple Weight Modes**: Uniform, linear interpolation, exponential, gaussian, and custom curves
- **Block Range Selection**: Target specific block ranges (e.g., 0-6, 7-12, 13-18)
- **Advanced Presets**: Mathematical weight distributions (bell curve, U-shape, emphasis patterns)
- **Weight Visualization**: Built-in weight editor with ASCII visualization
- **Custom Presets**: Save and load your own weight configurations
- **Production Ready**: Fully compatible with ComfyUI Manager

## 📦 Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "LoRA Block Weight"
3. Click Install

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/bhvbhushan/ComfyUI-LoRABlockWeight.git
# Restart ComfyUI
```

## 🚀 Quick Start

### Basic Usage
1. Add the "LoRA Block Weight Loader" node to your workflow
2. Connect your model and CLIP
3. Select a LoRA file
4. Choose a weight mode or preset
5. Adjust strengths and connect to sampling nodes

### Example Workflows

#### Uniform Application (Traditional)
- Weight Mode: `uniform`
- Block Weights: `1.0`
- Result: Standard LoRA application across all blocks

#### Targeted Enhancement
- Weight Mode: `block_specific`
- Block Range: `0-6`  
- Block Weights: `1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9`
- Result: Stronger influence on early blocks

#### Smooth Transition
- Weight Mode: `linear_interpolation`
- Interpolation Start: `1.5`
- Interpolation End: `0.5`
- Result: Gradual decrease from early to late blocks

## 🎛️ Node Parameters

### LoRA Block Weight Loader

#### Required Inputs
- **model**: The base model (Nunchaku/Flux/SD)
- **clip**: CLIP model
- **lora_name**: LoRA checkpoint file
- **strength_model**: Overall LoRA strength for model (−20.0 to 20.0)
- **strength_clip**: Overall LoRA strength for CLIP (−20.0 to 20.0)

#### Optional Inputs
- **block_weights**: Custom weight values (multiple formats supported)
- **weight_mode**: How weights are applied
  - `uniform`: Same weight for all blocks
  - `block_specific`: Custom weights per block
  - `linear_interpolation`: Linear gradient
  - `exponential`: Exponential curve
  - `gaussian`: Bell curve distribution
  - `custom_curve`: User-defined pattern
- **interpolation_start/end**: Start and end values for interpolation modes
- **interpolation_curve**: Curve factor for non-linear interpolations
- **block_range**: Which blocks to target (e.g., "all", "0-6", "7-12,15-18")
- **normalize_weights**: Normalize to maintain average strength
- **preserve_mean**: Keep mean value when normalizing
- **verbose**: Show detailed weight information
- **preset**: Use predefined weight patterns

### LoRA Block Weight Editor

A companion node for generating and visualizing weight patterns.

#### Parameters
- **total_blocks**: Number of blocks in your model
- **pattern**: Mathematical pattern to generate
- **amplitude**: Pattern amplitude
- **offset**: Base offset value
- **frequency**: Pattern frequency
- **phase**: Phase shift
- **custom_expression**: Mathematical expression for custom patterns

## 📊 Weight Input Formats

The node accepts multiple weight formats for maximum flexibility:

```python
# Single value (applies to all blocks)
"1.5"

# Space-separated
"1.0 1.2 1.4 1.2 1.0 0.8"

# Comma-separated
"1.0, 1.2, 1.4, 1.2, 1.0, 0.8"

# JSON array
"[1.0, 1.2, 1.4, 1.2, 1.0, 0.8]"

# JSON object with indices
'{"0": 1.5, "5": 1.2, "10": 0.8}'

# Multi-line block-specific (for Flux models)
"""
double_blocks: 1.0, 1.2, 1.4
single_blocks: 0.8, 0.9, 1.0
"""
```

## 🎨 Built-in Presets

- **linear_decay**: Gradual decrease from 1.5 to 0.5
- **linear_growth**: Gradual increase from 0.5 to 1.5
- **bell_curve**: Peak in middle blocks
- **u_shape**: Peak at extremes, trough in middle
- **emphasis_early**: Strong early blocks (first third)
- **emphasis_middle**: Strong middle blocks
- **emphasis_late**: Strong late blocks (last third)

## 🔧 Advanced Features

### Custom Presets

Create your own presets by adding JSON files to the `presets/` directory:

```json
{
  "name": "my_custom_preset",
  "description": "My custom weight distribution",
  "weights": [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, ...]
}
```

For Flux-specific presets:
```json
{
  "name": "flux_custom",
  "description": "Custom Flux weights",
  "weights": {
    "double_blocks": [1.0, 1.1, 1.2, ...],
    "single_blocks": [0.9, 1.0, 1.1, ...]
  }
}
```

### Weight Visualization

The LoRA Block Weight Editor provides ASCII visualization:
```
Weight Distribution (blocks: 57)
Range: [0.500, 1.500]
Mean: 1.000, Std: 0.289

          ████████
       ███        ███
     ██              ██
   ██                  ██
 ██                      ██
─────────────────────────────
```

### Mathematical Expressions

Use custom expressions with the Weight Editor:
```python
# Sine wave
"1.0 + 0.5 * sin(2 * pi * i / n)"

# Exponential decay
"2.0 * exp(-i / (n / 3))"

# Step function
"1.5 if i < n/2 else 0.5"
```

## 🏗️ Architecture Support

### Flux Models
- Automatically detects double_blocks (19) and single_blocks (38)
- Proper weight mapping for Flux transformer architecture
- Native support for Nunchaku quantized models

### Stable Diffusion Models
- Compatible with SD 1.5, SDXL, and variants
- Detects input/output/middle blocks
- Falls back gracefully for unsupported architectures

## 🎯 Use Cases

### Creative Control
- **Composition Control**: Strengthen early blocks for layout/pose
- **Style Transfer**: Adjust middle blocks for artistic style
- **Detail Enhancement**: Boost late blocks for fine details
- **Character Consistency**: Target specific blocks for facial features

### Technical Applications
- **LoRA Merging**: Different strengths for different LoRA aspects
- **Fine-tuning**: Selective layer updates
- **A/B Testing**: Compare different weight distributions
- **Research**: Analyze block contributions to generation

## 🐛 Troubleshooting

### LoRA Not Loading
- Ensure LoRA file is in `ComfyUI/models/loras/`
- Check console for specific error messages
- Verify model compatibility

### Unexpected Results
- Enable verbose mode to see actual weights applied
- Start with uniform weights as baseline
- Check if normalization is affecting results

### Performance Issues
- Hierarchical weighting adds minimal overhead
- Weight calculations are cached
- Consider reducing block range for testing

## 📈 Performance

- **Memory**: Minimal additional memory usage
- **Speed**: < 1% overhead vs standard LoRA loading
- **Compatibility**: Works with all ComfyUI samplers

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Additional mathematical presets
- Model architecture detection improvements
- Weight optimization algorithms
- Integration with other ComfyUI nodes

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- ComfyUI community for the framework
- Nunchaku and Flux model developers
- Contributors and testers

## 📚 References

- [ComfyUI Documentation](https://github.com/comfyanonymous/ComfyUI)
- [Flux Architecture](https://github.com/black-forest-labs/flux)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/bhvbhushan/ComfyUI-LoRABlockWeight/issues)
- **Discussions**: [GitHub Discussions](https://github.com/bhvbhushan/ComfyUI-LoRABlockWeight/discussions)
- **Discord**: ComfyUI Discord #custom-nodes channel

---

**Note**: This node provides a general-purpose solution for per-block LoRA weight control. It works with any ComfyUI-compatible model that benefits from block-level weight control, including Flux, Nunchaku, SDXL, and SD 1.5 models.