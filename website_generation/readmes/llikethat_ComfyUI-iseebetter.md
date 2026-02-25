# ComfyUI-iSeeBetter

ComfyUI custom nodes for **iSeeBetter** video super-resolution with **BasicVSR/BasicVSR++** learned flow, **SRGAN enhancement**, and **water-specific optimization**.

Based on [iSeeBetter: Spatio-Temporal Video Super Resolution](https://github.com/amanchadha/iSeeBetter) using Recurrent-Generative Back-Projection Networks.

## Features

### Core Video Super-Resolution
- **RBPN Generator** - Recurrent Back-Projection Network for temporal video SR
- **Optical Flow Integration** - Temporal alignment using DIS, Farneback, or simple flow
- **Multi-frame Processing** - Leverages neighboring frames for better quality
- **Tiled Processing** - Handle large images without running out of memory

### BasicVSR / BasicVSR++ (NEW!)
State-of-the-art video super-resolution with **learned optical flow**:
- **SpyNet** - Lightweight learned optical flow network (no external flow needed)
- **Bidirectional Propagation** - Uses both past and future frames
- **Second-order Grid Propagation** (BasicVSR++) - Enhanced temporal modeling
- **Artifact-free** - Avoids "golf ball" artifacts from external flow estimation

### SRGAN Enhancement
- **Discriminator** - SRGAN discriminator for GAN-based quality assessment
- **Perceptual Loss** - VGG-based perceptual similarity scoring
- **Generator Loss** - Combined MSE + Perceptual + Adversarial + TV loss

### Water-Specific Enhancement
Optimized for water bodies: **sea, ocean, waterfall, splash, swell, wake**

- **Water Detail Enhancer** - Neural network trained for water textures
- **Frequency Attention** - Enhances wave patterns, ripples, reflections
- **Water Post-Processing** - Highlight enhancement, local contrast, blue boost

## Nodes

### Video Upscaling Nodes

| Node | Description |
|------|-------------|
| **iSeeBetter Model Loader** | Load RBPN/iSeeBetter model weights |
| **iSeeBetter Video Upscale** | Full temporal upscaling with optical flow (supports SpyNet) |
| **iSeeBetter Clean Upscale** | Artifact-free upscaling (recommended if seeing artifacts) |
| **iSeeBetter Simple Upscale** | Simplified upscaling (no explicit optical flow) |
| **iSeeBetter Frame Buffer** | Buffer frames for temporal processing |

### BasicVSR Nodes (NEW!)

| Node | Description |
|------|-------------|
| **BasicVSR Model Loader** | Load/create BasicVSR or BasicVSR++ model |
| **BasicVSR Video Upscale** | Upscale using learned optical flow (best quality) |

### Water Enhancement Nodes

| Node | Description |
|------|-------------|
| **Water Detail Enhance** | Neural network enhancement for water textures |
| **Water Post Process** | CPU-based post-processing (highlights, contrast, color) |
| **Water Enhancer Model Loader** | Load custom water enhancer weights |

### Quality & Utility Nodes

| Node | Description |
|------|-------------|
| **SRGAN Discriminator Loader** | Load discriminator for quality assessment |
| **Perceptual Quality Score** | Calculate VGG-based perceptual similarity |
| **Image Sharpener** | Unsharp masking for detail enhancement |
| **iSeeBetter Debug Test** | Test single frame to isolate issues |

## Troubleshooting

### "Golf ball" / Pixelated Artifacts

If you see golf-balling or bad pixel artifacts:

#### Quick Fix Options

1. **Use the Clean Upscale Node**: The new "iSeeBetter Clean Upscale (No Artifacts)" node is designed to avoid artifacts:
   - Uses optimized flow estimation that won't cause artifacts
   - Doesn't use tiling (processes full frames)
   - Has `use_temporal_info` toggle - try setting to `False` if artifacts persist
   - Has `blend_factor` to mix with bicubic for smoother results

2. **Adjust Flow Settings** in standard iSeeBetter Video Upscale:
   - Set `optical_flow_method` to `zero` - this disables motion compensation entirely
   - Set `smooth_flow` to `True` (default)
   - Set `flow_scale` to `0.5` or lower - reduces motion compensation strength

3. **Disable Tiling**: Set `tile_size=0` to process full frames (requires more VRAM)

#### Diagnostic Steps

1. **Test with Debug Node**: Use the "iSeeBetter Debug Test" node to isolate:
   - Set `use_zero_flow=True` and `force_no_tiling=True`
   - If artifacts persist, the issue is with the model weights
   - If artifacts disappear, the issue is with flow/tiling

2. **Check console output**: Look for these stats:
   ```
   [iSeeBetter] Output stats (before clamp on future frames):
     - min=0.0000, max=1.0000  <- Good
     - mean=0.4500, std=0.2000 <- Normal range
   ```
   - Very low std (<0.01) = model may be producing flat output
   - Very high std (>0.5) = may indicate artifacts

3. **Check flow statistics**:
   ```
   [iSeeBetter] Flow stats (after scale): min=-X, max=X, mean=~0
   ```
   - If values are very large (>50), try reducing `flow_scale`
   - If you see NaN or Inf, there's a computation error

4. **Verify model compatibility**:
   - Model should output values in [0, 1] range after processing
   - Check that nFrames matches (usually 7 for iSeeBetter)
   - Scale factor should match (2x, 4x, or 8x)

## Installation

1. Clone or download this repository to your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI-iSeeBetter.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download model weights and place them in `ComfyUI/models/iseebetter/`:
   - Get the iSeeBetter checkpoint from the [original repository](https://github.com/amanchadha/iSeeBetter)
   - Trained for 4 epochs: `RBPN_4x.pth`

4. Restart ComfyUI

## Usage

### Basic Video Upscaling (iSeeBetter)

```
Load Video → iSeeBetter Model Loader → iSeeBetter Video Upscale → Save Video
```

### BasicVSR Pipeline (Best Quality, No Artifacts)

```
Load Video → BasicVSR Model Loader → BasicVSR Video Upscale → Save Video
```

### Hybrid: iSeeBetter with SpyNet Flow

Use iSeeBetter model but with learned optical flow:

```
Load Video → iSeeBetter Model Loader → iSeeBetter Video Upscale (optical_flow_method=spynet) → Save Video
```

### Water Enhancement Pipeline

For optimal water body upscaling:

```
Load Video 
    ↓
BasicVSR Model Loader → BasicVSR Video Upscale
    ↓
Water Detail Enhance (strength: 0.5)
    ↓
Water Post Process (highlight: 0.2, contrast: 0.3, blue_boost: 1.1)
    ↓
Image Sharpener (amount: 0.3)
    ↓
Save Video
```

### Quality Assessment

Compare your upscaled results:
```
Original HR → Perceptual Quality Score ← Upscaled SR
                      ↓
              Quality Report (loss value + assessment)
```

## Model Files

Place models in `ComfyUI/models/iseebetter/`:

| File Pattern | Type |
|--------------|------|
| `*.pth`, `*rbpn*` | RBPN generator weights |
| `*discriminator*`, `*netD*` | SRGAN discriminator |
| `*water*` | Water enhancer weights |

## Parameters Guide

### BasicVSR Model Loader (Recommended)
- **variant**: `basicvsr` (faster) or `basicvsr_plusplus` (better quality)
- **scale_factor**: 2x or 4x upscaling
- **num_features**: Feature channels (64 default, higher = better quality but more VRAM)
- **num_blocks**: Residual blocks (15 default)

### BasicVSR Video Upscale
- **chunk_size**: Process frames in chunks (10 default, reduce if OOM)

### iSeeBetter Video Upscale
- **optical_flow_method**: 
  - `spynet` (recommended) - Learned optical flow, best quality
  - `dis` - Dense Inverse Search (OpenCV)
  - `farneback` - Classical Farneback (OpenCV)
  - `simple` - Gradient-based, fastest
  - `zero` - No motion compensation (use if seeing artifacts)
- **tile_size**: 0 = auto (no tiling for high VRAM), or 256/384 for large images
- **tile_overlap**: 32 recommended for seamless tiles
- **smooth_flow**: Enable Gaussian smoothing on flow (reduces artifacts)
- **flow_scale**: Scale factor for optical flow magnitude (lower = less motion compensation)

### iSeeBetter Clean Upscale
- **use_temporal_info**: Use neighbor frames for temporal consistency. Disable if seeing artifacts
- **blend_factor**: Blend between model output (1.0) and bicubic fallback (0.0)

### Water Detail Enhance
- **strength**: 0.0-1.0, blend with original
- **use_frequency_attention**: Enable for wave/ripple enhancement

### Water Post Process
- **highlight_strength**: 0.1-0.3 for subtle reflection enhancement
- **contrast_strength**: 0.2-0.5 for texture detail
- **saturation**: 1.0-1.3 for color vibrancy
- **blue_boost**: 1.0-1.2 for ocean/water color

## Technical Details

### BasicVSR/BasicVSR++ Architecture
- **SpyNet**: 6-level spatial pyramid for learned optical flow
- **Bidirectional Propagation**: Forward and backward temporal features
- **Second-order Propagation** (++): Two-stage propagation in each direction
- **Pixel Shuffle Upsampler**: Sub-pixel convolution for upscaling

### iSeeBetter Architecture
- **Generator**: RBPN with DBPN-S modules
- **Discriminator**: SRGAN-style with LeakyReLU
- **Loss Function**: MSE + Perceptual (VGG) + Adversarial + TV

### Water Enhancement
- **Frequency Attention**: Separates low/mid/high frequency for targeted enhancement
- **Multi-scale Processing**: 3x3, 5x5, 7x7 kernels for different pattern sizes
- **Residual Learning**: Learns enhancement residuals, not full reconstruction

## Requirements

```
torch>=1.9.0
torchvision>=0.10.0
numpy>=1.19.0
opencv-python>=4.5.0
```

## Citation

If you use this in your research:

```bibtex
@article{iseebetter2020,
  title={iSeeBetter: Spatio-temporal video super-resolution using recurrent generative back-projection networks},
  author={Chadha, Aman and Britto, John and Roja, M Mani},
  journal={Computational Visual Media},
  year={2020},
  publisher={Springer}
}
```

## License

This project is for research purposes. See the original [iSeeBetter repository](https://github.com/amanchadha/iSeeBetter) for licensing details.

## Acknowledgments

- [iSeeBetter](https://github.com/amanchadha/iSeeBetter) by Aman Chadha
- [SRGAN](https://github.com/leftthomas/SRGAN) by LeftThomas
- [RBPN-PyTorch](https://github.com/alterzero/RBPN-PyTorch) baseline
