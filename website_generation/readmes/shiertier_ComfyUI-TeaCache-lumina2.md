# ComfyUI TeaCache for Lumina

Professional ComfyUI nodes for accelerating Lumina diffusion models using TeaCache technology.

## Overview

This package provides optimized ComfyUI nodes that implement TeaCache (Timestep Embedding Aware Cache) specifically for Lumina model series. TeaCache is a training-free acceleration technique that can significantly speed up inference while maintaining generation quality.

## Features

- **Zero Training Required**: Direct acceleration for existing Lumina models
- **Intelligent Caching**: Advanced timestep-aware caching mechanism
- **Multiple Model Support**: Compatible with Lumina2 and LuminaNext architectures
- **Automatic Detection**: Smart model type recognition
- **Quality Preservation**: Configurable trade-off between speed and quality
- **Easy Integration**: Standard ComfyUI node interface

## Supported Models

| Model Type | Description | Status |
|------------|-------------|---------|
| Lumina2 | Lumina-Image-2.0 models | ✅ Fully Supported |
| LuminaNext | Lumina-T2X (Next generation) | ✅ Fully Supported |
| Auto Mode | Automatic model detection | ✅ Recommended |

## Installation

### Prerequisites
- ComfyUI installation
- Python 3.8 or higher
- PyTorch 2.0 or higher

### Setup
1. Clone or download this repository to your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone <repository-url> ComfyUI-TeaCache-lumina
```

2. Install dependencies:
```bash
cd ComfyUI-TeaCache-lumina
pip install -r requirements.txt
```

3. Restart ComfyUI

## Node Reference

### TeaCache for Lumina (Auto)
**Location**: `TeaCache/Lumina` → `TeaCache for Lumina (Auto)`

Automatically detects Lumina model type and applies appropriate TeaCache optimization.

**Inputs**:
- `model` (MODEL): Input Lumina model
- `enable_teacache` (BOOLEAN): Enable/disable acceleration (default: True)
- `rel_l1_thresh` (FLOAT): Cache threshold controlling acceleration strength (default: 0.3)
- `num_inference_steps` (INT): Number of inference steps (default: 30)

**Outputs**:
- `model` (MODEL): Optimized model with TeaCache applied

### TeaCache for Lumina2
**Location**: `TeaCache/Lumina` → `TeaCache for Lumina2`

Specialized optimization for Lumina2 transformer models.

### TeaCache for LuminaNext
**Location**: `TeaCache/Lumina` → `TeaCache for LuminaNext`

Specialized optimization for LuminaNext DiT models.

## Performance Tuning

### Cache Threshold (`rel_l1_thresh`)

Controls the trade-off between speed and quality:

| Threshold | Speed Gain | Quality Impact | Use Case |
|-----------|------------|----------------|----------|
| 0.2 | ~1.5x | Minimal | High quality priority |
| 0.3 | ~1.9x | Slight | **Recommended balance** |
| 0.4 | ~2.4x | Moderate | Speed priority |
| 0.5 | ~2.8x | Noticeable | Maximum speed |

### Best Practices

1. **Start with Auto Mode**: Use automatic detection for new models
2. **Tune Gradually**: Begin with default threshold (0.3) and adjust as needed
3. **Monitor Quality**: Check output quality when increasing threshold
4. **Match Steps**: Ensure `num_inference_steps` matches your sampler settings

## Technical Details

### TeaCache Algorithm

The TeaCache mechanism works by:

1. **Timestep Analysis**: Monitoring changes in timestep embeddings
2. **Smart Caching**: Using L1 distance metrics to determine cache validity
3. **Residual Preservation**: Storing computation residuals for efficient reuse
4. **Adaptive Decision**: Dynamic switching between computation and cache retrieval

### Architecture Integration

```
Input → Timestep Embedding → [TeaCache Decision Engine] → Output
                                    ↓
                              Cache Store/Retrieve
```

The system integrates seamlessly with existing Lumina model pipelines without requiring model modifications.

## Troubleshooting

### Common Issues

**ImportError: diffusers is required**
- Install diffusers: `pip install diffusers>=0.25.0`

**Model type not supported**
- Ensure you're using a compatible Lumina model
- Try the Auto detection mode
- Check model loading in ComfyUI logs

**Unexpected quality degradation**
- Lower the `rel_l1_thresh` value
- Verify `num_inference_steps` matches your workflow
- Ensure model compatibility

### Performance Issues

If acceleration is not as expected:
1. Verify model type compatibility
2. Check that TeaCache is enabled
3. Monitor cache hit rates in console output
4. Adjust threshold parameters

## Compatibility

- **ComfyUI**: Latest stable version
- **Python**: 3.8, 3.9, 3.10, 3.11
- **PyTorch**: 2.0+
- **Platform**: Windows, Linux, macOS

## License

Licensed under the Apache License, Version 2.0. See `LICENSE` file for details.

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests for any improvements.

## Changelog

### Version 1.0.0
- Initial release
- Support for Lumina2 and LuminaNext models
- Automatic model detection
- Configurable caching parameters
- Standard ComfyUI node interface