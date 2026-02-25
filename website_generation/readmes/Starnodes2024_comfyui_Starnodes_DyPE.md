# ComfyUI Star DyPE

**Dynamic Position Extrapolation for Ultra High Resolution FLUX Image Generation**

This custom node enables FLUX models in ComfyUI to generate ultra-high resolution images (4K and beyond) using DyPE (Dynamic Position Extrapolation) technology.

## Features

- 🚀 **Ultra-High Resolution**: Generate 4096×4096 and larger images
- 🎯 **Multiple Methods**: YARN (recommended), NTK, and Base position encoding
- ⚡ **Dynamic Scaling**: Timestep-aware position encoding for better results
- 📐 **Preset Aspect Ratios**: 7 optimized aspect ratios (1:1, 3:4, 4:3, 5:7, 7:5, 16:9, 9:16)
- 🔌 **Easy Integration**: Works with any FLUX model in ComfyUI
- 🎨 **Workflow Compatible**: Outputs ready-to-use MODEL and LATENT

## What is DyPE?

DyPE (Dynamic Position Extrapolation) is a technique that enables pre-trained diffusion transformers to generate images at resolutions far beyond their training scale. It dynamically adjusts positional encodings during the denoising process to match evolving frequency content—achieving faithful 4K results without retraining or extra sampling cost.

**Reference**: [DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion](https://arxiv.org/abs/2510.20766)

## Installation

1. Clone or download this repository into your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone <repository-url> comfyui_star_DyPE
   ```

2. Restart ComfyUI

3. The node will appear under **⭐StarNodes/DyPE** category

## Usage

### Node: ⭐ Star DyPE Model Patcher

**Inputs:**
- `model` (MODEL): Any FLUX model loaded in ComfyUI
- `method` (dropdown): Position encoding method
  - **yarn** (recommended): Combines NTK and linear interpolation for best results
  - **ntk**: Neural Tangent Kernel scaling
  - **base**: Standard position encoding (no extrapolation)
- `enable_dype` (boolean): Enable dynamic timestep-aware scaling (recommended: True)
- `aspect_ratio` (dropdown): Select from 7 preset aspect ratios
- `scale` (float): Latent scale factor (default: 0.5)
  - **0.5**: Creates latent at half the chosen resolution (e.g., 2048×2048 for 4096×4096 selection)
  - **1.0**: Creates full-size latent matching the chosen resolution
  - Range: 0.1 to 2.0

**Outputs:**
- `MODEL`: Patched FLUX model with DyPE support
- `empty_latent`: Pre-configured empty latent at selected resolution
- `width` (INT): Image width in pixels
- `height` (INT): Image height in pixels

### Aspect Ratio Presets

All presets are optimized for approximately 16 megapixels total resolution:

| Aspect Ratio | Resolution | Use Case |
|--------------|------------|----------|
| 1:1 | 4096×4096 | Square images, social media |
| 3:4 | 3552×4736 | Portrait orientation |
| 4:3 | 4736×3552 | Landscape orientation |
| 5:7 | 3456×4838 | Tall portrait |
| 7:5 | 4838×3456 | Wide landscape |
| 16:9 | 5440×3060 | Widescreen, cinematic |
| 9:16 | 3060×5440 | Vertical video format |

### Example Workflow

```
Load Checkpoint (FLUX) → DyPE Model Patcher → KSampler → VAE Decode → Save Image
                              ↓
                         empty_latent
```

**Step-by-step:**
1. Load your FLUX model using a checkpoint loader
2. Connect the MODEL to **DyPE Model Patcher**
3. Select your preferred method (start with "yarn")
4. Enable DyPE (recommended)
5. Choose your aspect ratio
6. Connect the patched MODEL to KSampler
7. Connect the empty_latent to KSampler's latent input
8. Use your normal workflow (CLIP Text Encode, VAE Decode, etc.)

### Recommended Settings

**For best results:**
- **Method**: yarn
- **Enable DyPE**: True
- **Steps**: 28-50 (FLUX typically needs fewer steps)
- **CFG Scale**: 3.5-4.5 for FLUX
- **Sampler**: euler or flowmatch schedulers

## Technical Details

### How It Works

DyPE modifies the rotary position embeddings (RoPE) in FLUX's transformer blocks:

1. **YARN Method**: Combines Neural Tangent Kernel (NTK) scaling with linear interpolation, using a frequency-dependent mask to blend different scaling strategies
2. **Dynamic Timestep Scaling**: Adjusts position encoding based on the current denoising timestep, with stronger extrapolation during early (noisy) steps
3. **Frequency-Aware**: Different frequency components are scaled differently to preserve both low and high-frequency details

### Position Encoding Methods

- **YARN (YaRN)**: "Yet another RoPE extensioN" - combines multiple interpolation strategies with dynamic masking. Best for ultra-high resolutions.
- **NTK**: Neural Tangent Kernel scaling - adjusts the base frequency of position encodings. Good balance of quality and simplicity.
- **Base**: Standard position encoding without extrapolation. Use for debugging or comparison.

### Memory Considerations

Ultra-high resolution generation requires significant VRAM:
- **4096×4096**: ~16-24GB VRAM (depending on model)
- **5440×3060**: ~18-26GB VRAM
- Enable VAE tiling if you encounter memory issues during decoding
- Consider using model offloading for lower VRAM systems

## Compatibility

- **Models**: 
  - All FLUX variants (FLUX.1-dev, FLUX.1-schnell, FLUX.1-Krea-dev, etc.)
  - WAN (Wuerstchen Architecture Network)
  - Qwen Image models
- **ComfyUI**: Tested with recent ComfyUI versions
- **Hardware**: CUDA-compatible GPU recommended (16GB+ VRAM for 4K)

## Troubleshooting

**Issue**: "Model does not have pos_embed attribute"
- **Solution**: Ensure you're using a FLUX model, not SD1.5/SDXL

**Issue**: Out of memory errors
- **Solution**: 
  - Use a smaller aspect ratio
  - Enable VAE tiling
  - Use model CPU offloading
  - Reduce batch size to 1

**Issue**: Image quality degradation at high resolutions
- **Solution**:
  - Try switching between yarn/ntk methods
  - Ensure enable_dype is True
  - Increase inference steps (30-50)
  - Adjust CFG scale (3.5-5.0)

## Credits

- **DyPE Paper**: Noam Issachar, Guy Yariv, Sagie Benaim, Yossi Adi, Dani Lischinski, and Raanan Fattal (2025)
  - [Paper](https://arxiv.org/abs/2510.20766) | [Project Page](https://noamissachar.github.io/DyPE/)
- **Original DyPE Implementation**: Guy Yariv
  - [GitHub Repository](https://github.com/NoamIssachar/DyPE)
- **ComfyUI Integration**: Starnodes

## License

MIT License
- ComfyUI Integration: Copyright (c) 2025 Starnodes
- Original DyPE Implementation: Copyright (c) 2025 Guy Yariv

This ComfyUI integration is based on the original DyPE implementation by Guy Yariv and the DyPE research paper.

**Note**: The original DyPE work is patent pending. For commercial use or licensing inquiries regarding the DyPE method, please contact the [original authors](mailto:noam.issachar@mail.huji.ac.il).

See LICENSE file for full details.

## Citation

If you use this in your research or projects, please cite the original DyPE paper:

```bibtex
@misc{issachar2025dypedynamicpositionextrapolation,
      title={DyPE: Dynamic Position Extrapolation for Ultra High Resolution Diffusion}, 
      author={Noam Issachar and Guy Yariv and Sagie Benaim and Yossi Adi and Dani Lischinski and Raanan Fattal},
      year={2025},
      eprint={2510.20766},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2510.20766}, 
}
```

## More StarNodes Custom Nodes

Check out our other custom nodes for ComfyUI:

### ⭐ [ComfyUI StarNodes](https://github.com/Starnodes2024/ComfyUI_StarNodes)
Our main collection of production-ready custom nodes featuring:
- **InfiniteYou Patch Loader**: Memory-optimized character consistency patches with CPU/GPU device selection
- **Advanced Image Processing**: Professional-grade tools for image manipulation
- **Workflow Utilities**: Essential nodes to streamline your ComfyUI workflows
- Optimized for performance and memory efficiency

### ⭐ [ComfyUI StarBetaNodes](https://github.com/Starnodes2024/ComfyUI_StarBetaNodes)
Experimental and cutting-edge features:
- **Latest Research Implementations**: Early access to new AI techniques
- **Experimental Tools**: Test upcoming features before official release
- **Community-Driven**: Feedback-driven development and rapid iteration
- Perfect for users who want to explore the bleeding edge of ComfyUI capabilities

All StarNodes projects are actively maintained and designed to work seamlessly together!

## Support

For issues, questions, or feature requests, please open an issue on the GitHub repository.

---

**Enjoy creating ultra-high resolution images with FLUX! 🚀**
