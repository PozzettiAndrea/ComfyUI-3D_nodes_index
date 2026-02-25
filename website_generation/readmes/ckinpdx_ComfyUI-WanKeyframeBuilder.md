[README(1).md](https://github.com/user-attachments/files/24040452/README.1.md)
# WanKeyframeBuilder

ComfyUI custom nodes for building keyframe timelines for Wan video generation workflows.

## Nodes

### WanKeyframeBuilder
Basic keyframe timeline builder for single-pass video generation.

**Inputs:**
- `image1-8`: Up to 8 keyframe images
- `num_frames`: Total timeline length (default 81, should be 4n+1)
- `spacing_mode`: Even distribution or manual positioning
- `first_strength`, `last_strength`, `middle_strength`: Mask strengths for keyframes

**Outputs:**
- `images`: Full timeline [T, H, W, C] with keyframes placed and gray (0.5) fill
- `masks`: Strength masks [T, H, W] for each position
- `keyframes`: Just the keyframe images [N, H, W, C]

### WanKeyframeBuilderContinuation
Advanced keyframe builder for multi-segment video generation with continuation support.

**Key Features:**
- Continuation frames from previous video segment for smooth transitions
- First keyframe can be placed immediately after continuation frames
- Multiple reference images for scene transitions
- SVI-specific outputs for experimental SVI 2.0 workflows

**Inputs:**
- `image1`: Reference image for HuMo/quality 
- `image2-8`: Timeline keyframes (optional, placed on timeline)
- `continuation_image`: Last N frames from previous generation
- `continuation_frames`: Number of frames to use (default 3)
- `place_first_keyframe`: Place image2 immediately after continuation frames (default True)
- `first_keyframe_strength`: Mask strength for placed first keyframe (default 1.0)

**Continuation Frame Handling:**
- **IMPORTANT**: Continuation frames are now in **chronological order** (reversal logic removed)
- Takes last N frames from previous video in order: oldest → newest
- Position 0 = oldest continuation frame
- Position N-1 = newest continuation frame
- This matches standard video continuation expectations

**Mask Strength Modes:**
- `uniform`: All continuation frames use same strength
- `decay`: Exponential decay from start strength to end strength
  - `continuation_strength_start`: Strength for first/oldest frame (default 0.8)
  - `continuation_strength_end`: Strength for last/newest frame (default 0.2)
  - `continuation_decay_rate`: Decay curve (3.0 = moderate, 5.0+ = aggressive)

**Outputs:**
- `images`: Standard timeline with continuation + keyframes + gray fill
- `masks`: Strength masks
- `keyframes`: All reference images [image1, image2, ...] for HuMo/multi-reference
- `svi_reference_only`: **EXPERIMENTAL** - Timeline with image1 padding for SVI-Shot
- `svi_keyframe_segments`: **EXPERIMENTAL** - Each keyframe fills equal segments for SVI 2.0

## SVI Outputs (Experimental)

The `svi_reference_only` and `svi_keyframe_segments` outputs are designed for use with Stable Video Infinity (SVI) 2.0 LoRAs. 

**⚠️ WARNING: These outputs are experimental and NOT confirmed to work with SVI workflows.**

The SVI outputs were designed based on documentation from the [Stable-Video-Infinity](https://github.com/vita-epfl/Stable-Video-Infinity) repository, but have not been tested with actual SVI LoRAs in Kijai's WanVideoWrapper.

### svi_reference_only
Timeline filled entirely with `image1` (except continuation frames).

**Intended for:** SVI-Shot style reference padding where a single reference image persists throughout generation.

```
[0-2]: Continuation frames
[3-80]: image1 duplicated
```

### svi_keyframe_segments
Timeline where each keyframe fills its segment equally.

**Intended for:** SVI 2.0 multi-reference workflows with smooth transitions between different reference images.

```
With 3 continuation frames + 3 timeline keyframes (image2, image3, image4):

[0-2]: Continuation frames
[3-28]: image2 padding (segment 1)
[29-54]: image3 padding (segment 2)
[55-80]: image4 padding (segment 3)
```

**If you test these outputs:** Please report back whether they work with SVI LoRAs!

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/WanKeyframeBuilder
# Restart ComfyUI
```

## Example Workflow

### Basic Single-Pass Generation
```
WanKeyframeBuilder
├─ image1-5: Your keyframe images
├─ num_frames: 81
├─ spacing_mode: even
└─ Outputs → WanVideoImageToVideoEncode → WanVideoSampler
```

### Multi-Segment Generation with Continuation
```
Segment 1:
├─ WanKeyframeBuilderContinuation
│  ├─ image1: Reference face
│  ├─ image2-4: First segment keyframes
│  └─ continuation_image: None
└─ Generate 81 frames

Segment 2:
├─ WanKeyframeBuilderContinuation
│  ├─ image1: Same or new reference
│  ├─ image2-4: Second segment keyframes  
│  └─ continuation_image: Last 10-20 frames from Segment 1
└─ Generate 81 frames (uses last 3 frames for motion continuity)
```

## Technical Notes

### Frame Position Calculation

**Standard output (`images`):**
- Continuation frames: positions 0 to N-1
- First keyframe (if `place_first_keyframe=True`): position N
- Remaining keyframes: distributed via spacing mode
- Empty positions: gray fill (0.5)

**SVI outputs:**
- Both start with image1 as base padding
- Continuation frames overwrite positions 0 to N-1
- `svi_reference_only`: Rest stays as image1
- `svi_keyframe_segments`: Rest divided into equal segments per keyframe

### Mask Strength Behavior

Masks control how strongly each position is "locked" to its image:
- **1.0**: Fully locked (no model freedom)
- **0.8**: Strong guidance (recommended for middle keyframes)
- **0.5**: Balanced
- **0.2-0.3**: Light guidance (good for decay endpoints)
- **0.0**: Free generation (gray areas)

### Resolution Requirements

All connected images must match resolution. The node will raise an error if dimensions don't match. This is intentional - mismatched resolutions indicate a workflow error.

## Changelog

### Current Version
- **BREAKING CHANGE**: Removed continuation frame reversal logic
  - Frames now in chronological order (oldest → newest)
  - Matches standard video continuation expectations
  - Update workflows that relied on reversed order
- Added `place_first_keyframe` option for explicit first keyframe control
- Renamed continuation strength parameters for clarity (`start`/`end` instead of `ceiling`/`floor`)
- Added experimental SVI-specific outputs
- Improved mask strength calculation with clearer decay semantics

### Previous Versions
- Initial release with basic keyframe building
- Added continuation support
- Added SVI experimental outputs

## Credits

Designed for use with:
- [Kijai's WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [Stable Video Infinity](https://github.com/vita-epfl/Stable-Video-Infinity) (experimental)
- Wan 2.1/2.2 video generation models

## License

[Your License Here]

