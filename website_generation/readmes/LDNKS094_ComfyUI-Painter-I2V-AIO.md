[English](README.md) | [中文](README_zh.md)

# ComfyUI-PainterAIO

All-in-One collection of Painter's ComfyUI nodes for Wan 2.1/2.2 video generation.

This project consolidates and refactors multiple ComfyUI video node projects with unified API and optimized code structure.

---

## Based On

| Project | Author | Feature |
|---------|--------|---------|
| [ComfyUI-PainterI2V](https://github.com/princepainter/ComfyUI-PainterI2V) | princepainter | I2V with motion enhancement |
| [ComfyUI-PainterI2Vadvanced](https://github.com/princepainter/ComfyUI-PainterI2Vadvanced) | princepainter | Dual sampler + color protection |
| [ComfyUI-PainterLongVideo](https://github.com/princepainter/ComfyUI-PainterLongVideo) | princepainter | Long video extension |
| [Comfyui-PainterFLF2V](https://github.com/princepainter/Comfyui-PainterFLF2V) | princepainter | First-last frame interpolation |
| [ComfyUI-Wan22FMLF](https://github.com/wallen0322/ComfyUI-Wan22FMLF) | wallen0322 | Multi-frame reference conditioning |

---

## Nodes

| Node | Description |
|------|-------------|
| **PainterI2V** | Image-to-video with I2V / FLF2V modes, motion enhancement |
| **PainterI2VAdvanced** | Dual-phase sampler (high/low noise separation), supports loop continuation |
| **PainterI2VExtend** | Video extension for long video generation |
| **PainterSampler** | Sampler with motion enhancement |
| **PainterSamplerAdvanced** | Dual-phase sampler for PainterI2VAdvanced |

---

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/LDNKS094/ComfyUI-PainterAIO.git
```

---

## Features

- **Motion Enhancement**: Fix slow-motion issues with 4-step LoRAs (e.g., lightx2v)
- **Color Protection**: Prevent green/dark color drift after motion enhancement
- **Dual-Phase Sampling**: High noise for motion, low noise for semantic reference (Advanced only)
- **First-Last Frame Interpolation**: FLF2V mode with start and end frame anchoring
- **Long Video Extension**: Seamless continuation from previous video segment
- **SVI LoRA Compatible**: Supports latents_mean padding for SVI mode
- **Loop Support**: Auto-conversion between latent/image for ComfyUI loop workflows

---

## Node Details

### PainterI2V

Basic I2V node with motion enhancement.

| Parameter | Description |
|-----------|-------------|
| motion_amplitude | 4-step LoRA fix. 1.1-1.2 normal, 1.2-1.5 fast motion |
| color_protect | Prevents color drift from motion enhancement |
| svi_mode | SVI LoRA mode with latents_mean padding |
| start_image | First frame reference |
| end_image | Last frame for FLF2V mode |
| clip_vision | Semantic guidance |

### PainterI2VAdvanced

Advanced node with dual-phase sampling (high/low noise separation).

**Outputs 4 conditionings**: `high_positive`, `high_negative`, `low_positive`, `low_negative`

Use with **PainterSamplerAdvanced** for dual-phase sampling.

#### High Noise Phase (Motion)
- `motion_amplitude` - Motion enhancement strength
- `color_protect` - Color drift prevention
- `end_image` - End frame anchoring

#### Low Noise Phase (Semantics)
- `reference_latent` - From start_image (automatic)
- `clip_vision` - Semantic guidance
- `correct_strength` - Reference correction strength (0.01-0.05 recommended)

#### Continuation Parameters (Standard Mode Only)
- `overlap_frames` - Frame overlap count (4-8 recommended)
- `continuity_strength` - Motion lock strength (0.1-0.2 recommended)
- `previous_latent` or `previous_image` - Previous segment for continuation

#### Mode Differences

| Feature | Standard Mode | SVI Mode |
|---------|---------------|----------|
| Continuation source | previous_image | previous_latent |
| overlap_frames | Used (4-8) | Fixed (1 latent) |
| Concat padding | Grey (0.5) encoded | latents_mean (zero) |

### PainterI2VExtend

Video extension node for long video generation.

| Parameter | Description |
|-----------|-------------|
| overlap_frames | Frame overlap for continuity (4-8 recommended, standard mode only) |
| motion_amplitude | 4-step LoRA fix (both modes) |
| color_protect | Color drift prevention (both modes) |
| svi_mode | SVI LoRA mode with anchor + last latent |
| previous_video | Previous video segment to continue from |
| anchor_image | Anchor frame (defaults to previous_video[0]) |
| end_image | Target end frame |
| clip_vision | Semantic guidance |

---

## Parameter Guide

### motion_amplitude

| Motion Type | Recommended Value |
|-------------|-------------------|
| Subtle motion (talking, blinking) | 1.0 - 1.1 |
| Moderate motion (walking, gestures) | 1.1 - 1.2 |
| Large motion (running, jumping) | 1.2 - 1.5 |

### color_protect

Keep enabled (default: True) to prevent color drift after motion enhancement.

### overlap_frames (Advanced/Extend)

Number of pixel frames to overlap for continuity. Internally converted to latent index (`overlap_frames // 4`).

| Use Case | Recommended Value |
|----------|-------------------|
| Standard continuation | 4 |
| Smoother transition | 8 |

### continuity_strength (Advanced Only)

Controls motion lock strength between segments.

| Use Case | Recommended Value |
|----------|-------------------|
| Normal continuation | 0.1 |
| Stronger motion lock | 0.2 |

### correct_strength (Advanced Only)

Reference latent correction strength for low noise phase.

| Use Case | Recommended Value |
|----------|-------------------|
| Normal | 0.01 - 0.03 |
| Stronger reference | 0.03 - 0.05 |

---

## Acknowledgements

- **[princepainter](https://github.com/princepainter)**
- **[wallen0322](https://github.com/wallen0322)**
- **Wan2.1/2.2 Team**
- **ComfyUI Community**

---

## License

MIT License
