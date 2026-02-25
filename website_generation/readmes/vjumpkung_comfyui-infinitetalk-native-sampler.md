# InfiniteTalk Native Sampler for ComfyUI

A ComfyUI custom node package for generating lip-sync videos from audio using WAN 2.1 models with automatic frame extension for long audio.

## Features

- 🎵 **Automatic Frame Extension** — Seamlessly handles long audio by automatically extending video generation using motion frames
- 🗣️ **Lip-Sync Generation** — Produces realistic talking head videos synchronized to input audio
- 👥 **Multi-Speaker Support** — Supports two speakers with separate masks for advanced scenarios
- 🎛️ **Two Sampler Variants** — Choose between standard KSampler or advanced custom sampler interfaces
- 🎬 **Motion Frame Conditioning** — Uses motion frames to maintain temporal consistency across extended generations

## Nodes

### 1. InfiniteTalk Auto Sampler

Standard KSampler interface with familiar parameters:
- `seed`, `steps`, `cfg`, `sampler_name`, `scheduler`, `denoise`

**Inputs:**
| Name                     | Type                 | Description                                 |
| ------------------------ | -------------------- | ------------------------------------------- |
| `model`                  | MODEL                | Base WAN 2.1 model                          |
| `model_patch`            | MODEL_PATCH          | InfiniteTalk model patch                    |
| `positive`               | CONDITIONING         | Positive conditioning                       |
| `negative`               | CONDITIONING         | Negative conditioning                       |
| `vae`                    | VAE                  | VAE for encoding/decoding                   |
| `audio_encoder_output_1` | AUDIO_ENCODER_OUTPUT | Primary audio encoder features              |
| `audio`                  | AUDIO                | Input audio                                 |
| `width`                  | INT                  | Video width (default: 832)                  |
| `height`                 | INT                  | Video height (default: 480)                 |
| `length`                 | INT                  | Frames per pass (default: 81)               |
| `motion_frame_count`     | INT                  | Motion frames for conditioning (default: 9) |
| `audio_scale`            | FLOAT                | Audio conditioning scale (default: 1.0)     |
| `start_image`            | IMAGE                | Optional starting image                     |
| `clip_vision_output`     | CLIP_VISION_OUTPUT   | Optional CLIP vision conditioning           |
| `audio_encoder_output_2` | AUDIO_ENCODER_OUTPUT | Optional second speaker audio               |
| `mask_1`, `mask_2`       | MASK                 | Speaker reference masks                     |

### 2. InfiniteTalk Auto Sampler (Advanced)

Custom sampler interface accepting NOISE/SAMPLER/SIGMAS objects for advanced workflows:
- Use with custom noise generators, samplers, and sigma schedules

**Additional Inputs:**
| Name      | Type    | Description           |
| --------- | ------- | --------------------- |
| `noise`   | NOISE   | Custom noise object   |
| `sampler` | SAMPLER | Custom sampler object |
| `sigmas`  | SIGMAS  | Custom sigma schedule |

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/vjumpkung/comfyui-infinitalk-native-sampler.git
```

2. Restart ComfyUI — the nodes will be automatically loaded.

or 

Install from ComfyUI Manager search `infinitetalk-native-sampler`

## Requirements

- ComfyUI with WAN 2.1 model support
- Compatible audio encoder (e.g., wav2vec2-base)
- `comfy.ldm.wan.model_multitalk` module (included in recent ComfyUI versions)

## Workflow

A sample workflow is included in [`workflows/infinitetalk_native_loop_sampler_by_vjumpkung.json`](workflows/infinitetalk_native_loop_sampler_by_vjumpkung.json).

### Basic Usage

1. Load your WAN 2.1 model and InfiniteTalk model patch
2. Encode your audio using a compatible audio encoder (wav2vec2-base recommended)
3. Connect the audio encoder output and audio to the InfiniteTalk sampler
4. Configure dimensions (`width`, `height`, `length`)
5. Set `motion_frame_count` for temporal consistency (default: 9)
6. Run the sampler — it will automatically calculate and execute multiple passes for long audio

### Multi-Speaker Setup

1. Provide two audio encoder outputs (`audio_encoder_output_1` and `audio_encoder_output_2`)
2. Provide corresponding reference masks (`mask_1` and `mask_2`)
3. The system will combine audio features using "add" mode

## How It Works

### Frame Extension Algorithm

The sampler automatically handles long audio through multiple passes:

1. **Base Pass**: Generates initial `length` frames from motion frame (start image or zeros)
2. **Extend Passes**: Chains generation using last `motion_frame_count` frames as motion conditioning

Pass count calculation:
```
extend_frames = length - motion_frame_count
total_passes = 1 + ceil((total_frames - length) / extend_frames)
```

### Audio Processing

- Linear interpolation from 50fps to 25fps
- Audio encoder output validated against model patch dimensions
- Compatible encoders: wav2vec2-base (blocks=12, channels=768)

### Model Patching

The sampler applies patches to the model for each pass:
- `attn2_patch`: Cross-attention patch for audio conditioning
- `attn1_patch`: Self-attention patch for reference masks (when provided)
- `InfiniteTalkOuterSampleWrapper`: Handles motion frame conditioning

## Parameters Guide

| Parameter            | Default | Range             | Description                                        |
| -------------------- | ------- | ----------------- | -------------------------------------------------- |
| `length`             | 81      | 1-4096 (step 4)   | Frames generated per pass. Higher = more VRAM      |
| `motion_frame_count` | 9       | 1-33              | Frames used for motion conditioning between passes |
| `audio_scale`        | 1.0     | -10.0 to 10.0     | Strength of audio conditioning                     |
| `width`              | 832     | 16-4096 (step 16) | Output video width                                 |
| `height`             | 480     | 16-4096 (step 16) | Output video height                                |

### Tuning Tips

- **Longer Audio**: Reduce `length` or increase `motion_frame_count` to use fewer passes
- **Better Consistency**: Increase `motion_frame_count` for smoother transitions
- **VRAM Management**: Lower `length` if running out of memory
- **Audio Strength**: Adjust `audio_scale` to control lip-sync intensity

## Technical Details

### Latent Shape Convention

Shape format: `[batch, channels, temporal, height//8, width//8]`
- Channels: 16 (for WAN)
- Temporal: `((length - 1) // 4) + 1` (4x temporal compression)

### Audio Feature Validation

Audio encoder dimensions must match:
- `model_patch.model.audio_proj.blocks` (e.g., 12)
- `model_patch.model.audio_proj.channels` (e.g., 768)

## Troubleshooting

### "Audio encoder output dimensions do not match"
Ensure you're using a compatible audio encoder (wav2vec2-base for standard models).

### Out of Memory
Reduce `length` parameter to generate fewer frames per pass.

### "Both mask_1 and mask_2 are required"
When using two audio encoders, both masks must be provided.

## License

- Some codebase are from ComfyUI 

## Credits

- Based on WAN 2.1 model architecture
- InfiniteTalk implementation for lip-sync generation

**The entire codebase is generate from Claude Code.**
