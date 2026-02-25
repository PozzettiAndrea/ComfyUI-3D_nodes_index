# ComfyUI Advanced Generation Pack (AGP)

Production-ready custom nodes for advanced diffusion workflows. Modular implementation grounded in proven techniques from leading ComfyUI repositories.

## Installation

Copy the repository into your ComfyUI `custom_nodes` directory:

\`\`\`bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/your-repo/ComfyUI-AdvGenPack.git
\`\`\`

Nodes will appear in ComfyUI UI under "AGP/" categories after restart.

## Module Overview

### WAN Multi-Expert Sampling
Automatic expert switching optimized for Wan2.2 models and Lightning LoRAs.

**Nodes:**
- **WAN Multi-Expert Sampler** - Switch between high-noise and low-noise experts at optimal diffusion boundaries
- **WAN Lightning Hybrid (3-Stage)** - Triple-stage sampling with per-stage LoRA strength optimization
- **WAN Boundary Optimizer** - Detect optimal expert transition points using gradient/entropy analysis
- **WAN Noise Expert Mixer** - Blend expert outputs with configurable interpolation modes

**Key Features:**
- Adaptive boundary detection
- Per-stage LoRA scaling (early: 0.8x, mid: 1.2x, late: 0.6x)
- Multiple blending modes (linear, sigmoid, cosine)

**Example Config:**
\`\`\`toml
[wan.multi_expert]
boundary_type = "adaptive"
cfg_scale = 7.5
expert_weights = "1.0,1.0"
noise_blend_mode = "sigmoid"
\`\`\`

### Frame Interpolation
RIFE/DAIN-style frame synthesis with optical flow and temporal consistency.

**Nodes:**
- **Optical Flow Frame Interpolator** - Generate intermediate frames using Lucas-Kanade or Horn-Schunck flow
- **Temporal Consistency Enforcer** - Maintain coherence across frame sequences
- **Keyframe Extractor** - Auto-extract critical frames from sequences
- **Motion Prediction Sampler** - Predict intermediate frames with easing functions

**Example Config:**
\`\`\`toml
[frame_interp.optical_flow]
flow_method = "lucas_kanade"
interpolation_mode = "flow_guided"
blend_strength = 1.0
\`\`\`

### Post-Processing FX
Real-time image effects for final rendering polish.

**Nodes:**
- **Bloom & Glow FX** - Threshold-based bloom with falloff (additive, screen, soft-light modes)
- **Denoise Suite** - NLM, bilateral, median, morphological denoising
- **Sharpening Filter** - Unsharp mask, high-pass, detail enhancement
- **Chromatic Aberration** - RGB channel offsets (radial, directional, swirl)
- **Film Grain & Noise** - Procedural grain (uniform, Gaussian, Perlin-style)

**Example Config:**
\`\`\`toml
[fx.bloom]
bloom_threshold = 0.8
bloom_intensity = 1.0
bloom_size = 15
glow_strength = 0.5
bloom_mode = "screen"
\`\`\`

### Color Correction
Professional color grading and correction tools.

**Nodes:**
- **Histogram Equalizer** - Adaptive/global histogram stretching
- **LUT 3D Loader** - Apply 3D LUT color grades
- **Curves & Levels** - Point-based curve adjustment
- **HSV Shifter** - Independent hue/saturation/value control
- **Color Grading Preset** - Pre-built cinematic grades (cinematic, vintage, cool, warm, noir)
- **White Balance Corrector** - Temperature/tint correction with auto-detection

**Example Config:**
\`\`\`toml
[color.grading]
preset = "cinematic"
intensity = 1.0
temperature = 6500
tint = 0.0
\`\`\`

### Model & LoRA Merging
Advanced checkpoint and LoRA merging techniques.

**Nodes:**
- **Checkpoint Merger (DARE)** - DARE-TIES merging with configurable sparsity
- **Checkpoint Merger (Block-wise MBW)** - Per-block weight blending for SD1.5/SDXL
- **Checkpoint Merger (Advanced Multi)** - Multi-model blending with layer schedules
- **LoRA Multi-Merger** - Batch merge N LoRAs with custom alphas
- **LoRA DARE Merger** - DARE-based LoRA combination
- **LoRA Strength Scheduler** - Dynamic LoRA weights across diffusion steps
- **Checkpoint Mask Generator** - Generate layer-wise weighting masks

**Example Config:**
\`\`\`toml
[merge.dare]
sparse_factor = 0.95
rescale_mode = "vector"

[merge.blockwise]
architecture = "sdxl"
input_blocks_weight = 0.6
middle_block_weight = 0.7
output_blocks_weight = 0.5

[merge.lora_scheduler]
schedule_type = "sigmoid"
start_strength = 1.0
end_strength = 0.5
\`\`\`

## Workflow Examples

### Example 1: Wan2.2 Multi-Expert Sampling

\`\`\`
ckpt_load("wan2.2-base.safetensors") 
  → wan_multi_expert(
      steps=20, 
      boundary_type="adaptive",
      cfg_scale=7.5
    )
  → wan_lightning_hybrid(
      early_lora_scale=0.8,
      mid_lora_scale=1.2,
      late_lora_scale=0.6
    )
  → vae_decode()
\`\`\`

### Example 2: Frame Interpolation + Post-FX

\`\`\`
load_frame_sequence("input/") 
  → optical_flow_interpolator(
      interpolation_factor=0.5,
      flow_method="lucas_kanade"
    )
  → temporal_consistency_enforcer(
      consistency_strength=0.7
    )
  → bloom_glow_fx(
      bloom_intensity=1.2,
      bloom_mode="screen"
    )
  → film_grain_noise(
      grain_amount=0.05,
      grain_type="gaussian"
    )
  → save_images()
\`\`\`

### Example 3: Model Merging + Grading

\`\`\`
ckpt_load("sd15-base.safetensors")
ckpt_load("style-a.safetensors")
ckpt_load("style-b.safetensors")
  → checkpoint_merger_blockwise(
      architecture="sd15",
      input_blocks_weight=0.6,
      middle_block_weight=0.7,
      output_blocks_weight=0.6
    )
  → lora_load("quality-lora.safetensors")
  → lora_strength_scheduler(
      steps=25,
      schedule_type="cosine",
      start_strength=1.0,
      end_strength=0.4
    )
  → ksampler(steps=25)
  → color_grading_preset(preset="cinematic", intensity=1.0)
  → vae_decode()
\`\`\`

## Technical Details

### Architecture
- **Modular Design**: 7 separate node modules (WAN, Frame Interp, FX, Color, Merging, Utils)
- **Utilities**: Common functions, color space conversion, merge algorithms in `utils/`
- **Type Hints**: Full Python 3.8+ type annotations for IDE support

### Performance Notes
- Optical flow operations CPU-optimized for speed (Lucas-Kanade, Horn-Schunck simplified implementations)
- Bloom/denoise operations support batched tensor operations
- Merging operations designed for efficient state dict manipulation

### Compatibility
- **ComfyUI**: Latest versions (tested on 0.1.x+)
- **Python**: 3.8+
- **PyTorch**: 2.0+
- **Models**: SD1.5, SDXL, Wan2.2

## Node Reference

### Input/Output Types
- `MODEL` - Diffusion model checkpoint
- `LORA` - LoRA checkpoint dictionary
- `IMAGE` - Tensor [batch, height, width, channels] in [0, 1] range
- `LATENT` - Latent space tensor
- `CONDITIONING` - Prompt conditioning from CLIP encoders
- `SIGMAS` - Noise schedule for diffusion steps
- `INT`, `FLOAT`, `STRING`, `BOOLEAN` - Standard types

### Common Parameters
- **steps** - Number of diffusion steps (1-500)
- **cfg_scale** - Classifier-free guidance scale (0-30)
- **strength** - Effect intensity (0-1 or 0-2 depending on context)
- **schedule_type** - Interpolation mode (linear, sigmoid, cosine, step)
- **blend_mode** - Blending operation (additive, screen, soft_light, overlay, etc.)

## Troubleshooting

**Nodes not appearing in UI:**
- Ensure repo is in `custom_nodes` directory
- Restart ComfyUI completely
- Check console for import errors

**Out of memory errors:**
- Reduce `bloom_size` in Bloom FX
- Lower frame interpolation search area
- Split large frame sequences into batches

**Inconsistent results with frame interpolation:**
- Increase `consistency_strength` in Temporal Enforcer
- Use `flow_guided` interpolation mode
- Extract keyframes first with Keyframe Extractor

## Citation & References

Grounded in techniques from:
- WanMoeKSampler (Wan2.2 expert routing)
- TripleKSampler (3-stage Lightning optimization)
- DareMerge (DARE-TIES merging)
- LoRA-Merger-ComfyUI (LoRA combination)
- RES4LYF (frame and image processing)
- ComfyUI-Extra-Samplers (additional sampling methods)

## License

MIT License - See LICENSE file for details
