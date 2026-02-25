# K3NK ComfyUI Nodes

A collection of ComfyUI nodes for advanced video workflows and latent management.

---

## K3NK Image Loader with Blending

Advanced ComfyUI node for loading image sequences with intelligent frame blending for seamless video transitions.

This node is specifically designed for **multi-sequence video workflows**, automatically blending overlapping frames between sequences to create smooth transitions without visible cuts. Uses **smootherstep interpolation** for professional-grade blending quality.

### Features
- **Intelligent sequence detection**: Automatically calculates complete sequences and remaining frames
- **Smootherstep blending**: Professional non-linear interpolation eliminates ghosting artifacts
- **Interpolation-aware**: Automatically scales overlap for frame-interpolated sequences (RIFE, etc.)
- **Incomplete sequence handling**: Properly processes remaining frames even when they don't form a complete sequence
- **Flexible file patterns**: Support for multiple image formats via glob patterns
- **Sequential numbering**: Detects and sorts files by numeric sequence in filenames
- **Frame stride compatibility**: Works seamlessly with interpolated sequences (2x, 4x, etc.)
- **Debug output**: Detailed console logging for monitoring blend operations

### Key Concepts

#### Sequence-Based Processing
The node divides your image directory into sequences of N frames (e.g., 81 frames per sequence). When you have multiple sequences, it automatically blends the overlapping frames at sequence boundaries to create smooth transitions.

#### Smootherstep Blending Algorithm
Unlike basic linear blending, this node uses **smootherstep** (quintic hermite interpolation):
- **S-curve transition**: Slow at start/end, fast in middle
- **Eliminates ghosting**: Especially crucial with RIFE ensemble interpolation
- **Professional quality**: Industry-standard method for video crossfades
- **Handles micro-variations**: Compensates for interpolation artifacts

#### Frame Blending Mechanism
- **Overlap frames**: The last N frames of one sequence blend with the first N frames of the next
- **Smootherstep interpolation**: Uses quintic curve for natural transitions
- **Frame replacement**: Blended frames replace the original overlapping frames (no duplication)
- **Incomplete sequences**: Automatically handles leftover frames with adaptive blending

#### Output Frame Count
**Important**: The output will have FEWER frames than input due to blending:
- Input: 162 frames (2 sequences of 81)
- Overlap: 5 frames
- Output: 162 - 5 = **157 frames** (blending replaces, doesn't add)
- Formula: `total_frames - (overlap_frames × number_of_transitions)`

### Inputs
| Name | Type | Description |
|------|------|-------------|
| `directory_path` | STRING | Path to folder containing image sequence |
| `sequence_frames` | INT | Number of frames per sequence (1-10000, default: 81) |
| `overlap_frames` | INT | Number of frames to blend at sequence boundaries (1-20, default: 5) |
| `file_pattern` | STRING | Glob pattern for image files (default: *.png) |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| `images` | IMAGE | Blended image tensor in format `[total_frames, H, W, 3]` for ComfyUI processing |

### Usage Examples

#### Example 1: Standard Two-Sequence Workflow (No Interpolation)
**Scenario**: 162 frames total (2 sequences of 81 frames each)

Settings:
```
sequence_frames: 81
overlap_frames: 5
```

Processing:
- Sequence 1: Frames 0-80 (added complete)
- Sequence 2: Frames 81-161
  - Blend: Last 5 frames of Seq1 (76-80) with first 5 of Seq2 (81-85)
  - Add: Remaining frames 86-161
- **Output**: 157 frames total (162 - 5 blended frames)

#### Example 2: Two-Sequence Workflow with 2× Interpolation (RIFE)
**Scenario**: 324 frames total (2 sequences × 162 interpolated frames)

Settings:
```
sequence_frames: 162  # 81 × 2 (interpolated)
overlap_frames: 10    # 5 × 2 (scaled for interpolation)
```

Processing:
- Uses smootherstep to handle RIFE ensemble micro-variations
- Eliminates ghosting artifacts from interpolation
- Blend: Last 10 frames of Seq1 (152-161) with first 10 of Seq2 (162-171)
- **Output**: 314 frames total (324 - 10 blended frames)

**Critical**: When using RIFE with `ensemble=true`, the 10-frame overlap with smootherstep is essential to prevent visible ghosting.

#### Example 3: Incomplete Final Sequence
**Scenario**: 161 frames total (81 + 80 frames)

Settings:
```
sequence_frames: 81
overlap_frames: 5
```

Processing:
- Sequence 1: Frames 0-80 (complete)
- Remaining: 80 frames (not a complete sequence)
  - Adaptive blend: Uses min(5, 80) = 5 frames for blending
  - Blend: Frames 76-80 with frames 81-85
  - Add: Remaining frames 86-160
- **Output**: 156 frames total

#### Example 4: Three Sequences with Interpolation
**Scenario**: 486 frames (3 sequences × 162 interpolated frames)

Settings:
```
sequence_frames: 162  # 81 × 2 (interpolated)
overlap_frames: 10    # 5 × 2 (scaled for interpolation)
```

Processing:
- Creates 2 blend transitions (between 3 sequences)
- Total blended frames: 10 × 2 = 20 frames
- **Output**: 486 - 20 = **466 frames**

#### Example 5: Single Sequence (No Blending)
**Scenario**: 81 frames total

Settings:
```
sequence_frames: 81
overlap_frames: 5
```

Processing:
- Only one complete sequence detected
- No blending needed
- **Output**: 81 frames (unchanged)

### Interpolation Guidelines

When working with interpolated sequences (RIFE, FILM, etc.), **always scale the overlap proportionally**:

| Original | 2× Interpolation | 4× Interpolation |
|----------|------------------|------------------|
| 81 frames, 5 blend | 162 frames, 10 blend | 324 frames, 20 blend |
| 121 frames, 5 blend | 242 frames, 10 blend | 484 frames, 20 blend |

**Formula**: `interpolated_overlap = original_overlap × interpolation_factor`

**Why This Matters:**
- Video generation models often duplicate the last 5 frames to prevent color shift
- With 2× interpolation, these become 10 duplicated frames
- Overlap must cover ALL duplicated frames for smooth transitions
- Smootherstep handles micro-variations from RIFE ensemble mode

### File Naming Convention

The node extracts numeric sequences from filenames for proper ordering:
- `frame_0001.png` → number `1`
- `output_00138.png` → number `138`
- `render_050_final.png` → number `50`

Files are sorted by the **last number found** in the filename.

### Supported File Formats

Default pattern `*.png` includes PNG files. Customize with:
- `*.jpg` - JPEG files only
- `*.{png,jpg}` - Multiple formats (requires bash-style brace expansion support)
- `frame_*.png` - Specific prefix
- `*_final.png` - Specific suffix

The node automatically converts all images to RGB and normalizes to float32 [0-1] range.

### Technical Details

#### Smootherstep Blending Algorithm
```python
smooth_alpha = alpha³ × (alpha × (alpha × 6 - 15) + 10)
blended_frame = frame1 × (1 - smooth_alpha) + frame2 × smooth_alpha
```

**Alpha progression** across 5 overlap frames:
- Frame 1: alpha = 1/6 = 0.167 → smooth = 0.009 (0.9% new, 99.1% old)
- Frame 2: alpha = 2/6 = 0.333 → smooth = 0.132 (13.2% new, 86.8% old)
- Frame 3: alpha = 3/6 = 0.500 → smooth = 0.500 (50% new, 50% old)
- Frame 4: alpha = 4/6 = 0.667 → smooth = 0.868 (86.8% new, 13.2% old)
- Frame 5: alpha = 5/6 = 0.833 → smooth = 0.991 (99.1% new, 0.9% old)

**Comparison with Linear**:
- **Linear**: Constant blend rate → visible ghosting with many frames
- **Smootherstep**: S-curve → imperceptible transitions, eliminates ghosting

### Processing Order
1. **File discovery**: Glob pattern matching in directory
2. **Sequential sorting**: Extract and sort by numeric values
3. **Image loading**: Load all images, convert to RGB tensors
4. **Sequence calculation**: Determine complete sequences and remainders
5. **First sequence**: Add all frames without modification
6. **Subsequent sequences**: Smootherstep blend overlap, add remaining frames
7. **Incomplete sequences**: Adaptive blending with available frames
8. **Output stacking**: Concatenate all frames into single tensor

### Memory Considerations
- All images are loaded into memory simultaneously
- Output tensor size: `[total_frames, height, width, 3]` in float32
- Example: 500 frames at 1280×768 = ~4.7GB RAM
- Consider batch processing for very long sequences

### Console Output Example
```
📁 Found 324 images
✅ Loaded 324 images
🎯 162 frames per sequence, 10 overlap frames

🔧 Processing sequences...
  Complete sequences: 2
  Remaining frames: 0

  Added first sequence: frames 0-161

  Sequence 2:
    Start index: 162
    Blending frames 152-161 with 162-171
    Added frames 172-323

📊 Final: 314 frames (original: 324)

🔍 Checking for actual blending...
   10/10 first frames were modified
```

### Best Practices

#### Sequence Planning
- Plan your renders in multiples of `sequence_frames` when possible
- Account for lost frames in blending: `output = input - (overlap × transitions)`
- For 3 sequences: expect to lose `overlap_frames × 2` frames total

#### Overlap Selection
- **Without interpolation**: 5 frames (default, handles 5 duplicated frames)
- **With 2× interpolation**: 10 frames (handles 10 duplicated frames)
- **With 4× interpolation**: 20 frames (handles 20 duplicated frames)
- **General rule**: Scale overlap with interpolation factor

#### Interpolation-Specific Tips
- **RIFE with ensemble=true**: ALWAYS use smootherstep (this node's default)
- **Duplicated frames**: Video models duplicate last 5 frames to prevent color shift
- **After interpolation**: These duplicates become 10, 20, etc. frames
- **Overlap must cover duplicates**: Otherwise you'll see hard cuts

#### Quality Tips
- Use consistent lighting across sequences for better blending
- Avoid drastic scene changes at sequence boundaries
- Smootherstep compensates for RIFE ensemble micro-variations
- Higher overlap values needed for interpolated content
- Test with a small sequence first to verify settings

#### Workflow Integration
- Use with RIFE/FILM interpolation nodes for smooth slow-motion
- Pair with VHS Video Combine for final video output
- Compatible with any ComfyUI node accepting IMAGE input
- Works seamlessly with AnimateDiff, Wan Video, and other video models
- Essential for multi-batch WanVideoWrapper workflows

### Troubleshooting

#### Ghosting visible in transitions (interpolated sequences)
- **Cause**: RIFE ensemble mode creates micro-variations between frames
- **Solution**: Already solved with smootherstep - ensure you're using latest version
- **Verify**: Check code uses `smooth_alpha = alpha * alpha * alpha * (alpha * (alpha * 6.0 - 15.0) + 10.0)`
- **If persists**: Reduce overlap by 2-4 frames (e.g., 10 → 6-8)

#### Hard cuts visible between sequences
- **Cause**: Overlap doesn't cover all duplicated frames
- **Solution**: Increase overlap to match interpolation factor (5 → 10 for 2×)
- **Verify**: Check that `overlap_frames = original_overlap × interpolation_factor`

#### No blending visible in output
- Check console for "X/10 first frames were modified"
- Verify you have multiple sequences (more than `sequence_frames` total)
- Ensure `overlap_frames > 0`
- Check that images actually differ at sequence boundaries

#### Unexpected output frame count
- Remember: blending REPLACES frames, doesn't add them
- Formula: `total_input - (overlap_frames × number_of_transitions)`
- Example: 486 frames (3 sequences) with 10 overlap = 486 - 20 = 466 output

#### "No files found" error
- Verify `directory_path` is correct and absolute
- Check `file_pattern` matches your files
- Ensure files have proper extensions
- Verify file permissions

#### Images in wrong order
- Check filename numbering is sequential
- The node uses the LAST number found in each filename
- Rename files if necessary: `frame_001.png`, `frame_002.png`, etc.

#### Out of memory
- Reduce total frame count
- Process in smaller batches
- Lower image resolution before processing
- Use a machine with more RAM

### Performance Notes
- **Loading speed**: ~0.1-0.5s per image depending on resolution and disk speed
- **Blending speed**: Nearly instant (GPU tensor operations)
- **Smootherstep overhead**: Negligible compared to linear
- **Bottleneck**: Usually file I/O, not computation
- **Optimization**: Use SSD storage for faster loading

---

## K3NK Find Nearest Bucket

Utility node that finds the nearest resolution bucket for a given image, matching the bucketing logic used by video generation models like FramePack/HunyuanVideo.

Useful for ensuring your image dimensions are compatible with the model before encoding, avoiding aspect ratio mismatches or padding artifacts.

### Features
- **Model-compatible resolutions**: Uses the same bucketing logic as FramePack/HunyuanVideo
- **Aspect ratio preservation**: Finds the closest bucket while respecting the original proportions
- **Lightweight**: Reads image dimensions only, no pixel processing

### Inputs
| Name | Type | Description |
|------|------|-------------|
| `image` | IMAGE | Input image to analyze |
| `base_resolution` | INT | Target base resolution in pixels (default: 640, min: 64, max: 2048, step: 16) |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| `width` | INT | Nearest bucket width |
| `height` | INT | Nearest bucket height |

### Usage Example

Connect this node between your image loader and VAE encoder to ensure compatible dimensions:

```
[Load Image] → [K3NK Find Nearest Bucket] → [Image Resize] → [VAE Encode]
```

### Notes
- Requires `bucket_tools` from FramePackWrapper to be available in your ComfyUI installation
- Output dimensions can be fed directly into any resize or crop node
- Default `base_resolution: 640` matches FramePack's recommended setting

---

## Save Latent (Pass-Through)

A utility node for saving latents to disk mid-workflow **without interrupting the pipeline**. The latent passes through unchanged, making it ideal for checkpointing long generation processes.

### Features
- **Pass-through design**: Outputs the input latent unmodified — workflow continues normally
- **Absolute path support**: `filename_prefix` can include subdirectories relative to ComfyUI's output folder
- **Auto-incrementing filenames**: Automatically finds the next available `_XXXXX_` counter to avoid overwriting
- **Safetensors format**: Saves as `.latent` using the `safetensors` format, including tensor metadata
- **Auto directory creation**: Creates subdirectories automatically if they don't exist

### Inputs
| Name | Type | Description |
|------|------|-------------|
| `samples` | LATENT | The latent to save and pass through |
| `filename_prefix` | STRING | Filename prefix, optionally including subdirectory (e.g. `subdir/mylatent`) |

### Outputs
| Name | Type | Description |
|------|------|-------------|
| `samples` | LATENT | The original latent, unchanged |

### File Naming

Files are saved as `{prefix}_{counter:05d}_.latent` inside ComfyUI's output directory. The counter auto-increments to avoid collisions:

```
outputs/
└── mylatent_00000_.latent
└── mylatent_00001_.latent
```

With a subdirectory prefix (`subdir/mylatent`):
```
outputs/
└── subdir/
    └── mylatent_00000_.latent
```

### Usage Example

Insert this node anywhere in your latent pipeline to save a checkpoint:

```
[KSampler] → [Save Latent (Pass-Through)] → [VAE Decode] → [Save Image]
```

The latent is saved to disk and the workflow continues without interruption.

### Use Cases
- **Checkpointing**: Save intermediate latents during multi-stage workflows
- **Debugging**: Inspect latents at different pipeline stages
- **Reuse**: Save latents to reload later, skipping expensive re-generation
- **Multi-batch WanVideo**: Persist latents between batches for continuation workflows

---

## Version History
- **v1.5**: Added K3NK Find Nearest Bucket node for model-compatible resolution matching
- **v1.4**: Added Save Latent (Pass-Through) node for mid-workflow latent checkpointing
- **v1.3**: Switched to smootherstep blending, updated defaults (5 overlap), added interpolation guidelines
- **v1.2**: Improved incomplete sequence handling with adaptive blending
- **v1.1**: Fixed edge cases with remaining frames, enhanced debug output
- **v1.0**: Initial release with multi-sequence blending support

## Credits

Built for ComfyUI video workflows. Designed to work seamlessly with:
- WanVideoWrapper (multi-batch workflows)
- FramePackWrapper (bucketing, LoRA loading)
- RIFE interpolation (especially ensemble mode)
- AnimateDiff
- VHS Video Combine
- Frame interpolation nodes (FILM, RIFE, etc.)

## License

MIT License - Free to use and modify

---

**Note**: This node pack is optimized for multi-sequence video generation workflows where smooth transitions between generated segments are critical. The smootherstep algorithm is specifically tuned to handle RIFE ensemble interpolation artifacts. For single-sequence workflows or when transitions aren't needed, consider using standard image loader nodes.
