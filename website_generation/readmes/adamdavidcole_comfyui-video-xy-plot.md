# ComfyUI XY Video Plot Suite

A suite of ComfyUI nodes for generating parameter sweep video matrices with labeled grids. Create comprehensive visual comparisons of how different parameter combinations affect your video generation results.

## Example Output

![Example Grid](examples/wan_grid_steps_cfg.jpg)
![Example Setup](examples/example_setup.png)


**To load the example workflow:** Download and drag [`examples/wan_xy_plot.json`](examples/wan_xy_plot.json) into ComfyUI

[▶️ View Full Video Output](examples/wan_grid_steps_cfg.mp4)


A suite of ComfyUI nodes for generating parameter sweep video matrices with labeled grids. Create comprehensive visual comparisons of how different parameter combinations affect your video generation results.


## Features

- **Parameter Sweep Automation**: Test multiple parameter combinations automatically
- **Labeled Grid Output**: Clear X/Y axis labels showing which parameters generated each video
- **For Loop Integration**: Works seamlessly with `comfyui-easy-use` For Loop nodes
- **Customizable Layout**: Adjust cell sizes, fonts, and colors
- **Batch Organization**: Optional batch IDs for organized file management
- **Auto Cleanup**: Optionally delete source videos after grid assembly

## Installation

### 1. Install Dependencies

```bash
cd ComfyUI/custom_nodes/comfyui-xyvideoplot2
pip install -r requirements.txt
```

Or manually:
```bash
pip install moviepy
```

### 2. Clone Repository

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-xyvideoplot2
```

### 3. Restart ComfyUI

## Quick Start

### Basic Workflow Structure

```
XY Plot Setup
    ↓ initial_collection_data → For Loop Start (initial_value1)
    ↓ total_iterations → For Loop Start (iterations)
    ↓ xy_config (pass through)
    ↓ batch_id (optional - use in filename_prefix)

For Loop Start
    ↓ loop_index → XY Plot Get Values
    ↓ value1 (collection_data) → XY Plot Collect Video

XY Plot Get Values
    ↓ x_value → KSampler (or other parameter)
    ↓ y_value → KSampler (or other parameter)
    ↓ x_label, y_label → XY Plot Collect Video

[Your Generation Workflow]
    KSampler → Images → VHS Video Combine
    ↓ video_filepath → XY Plot Collect Video

XY Plot Collect Video
    ↓ collection_data → For Loop End (value1)

For Loop End
    ↓ final_value1 → XY Plot Video Grid

XY Plot Video Grid
    ↓ video_grid (IMAGE tensor) → Save Image/Video
```

### Example Setup

**XY Plot Setup:**
- X-axis: `seed` (type: INT, values: `1, 3, 5`)
- Y-axis: `cfg` (type: FLOAT, values: `2.0, 7.5`)

This creates a 3×2 grid testing all 6 combinations.

## Node Reference

### 1. XY Plot Setup

Initialize parameter sweep configuration.

**Inputs:**
- `x_axis_name` (STRING): Display name for X-axis (e.g., "seed")
- `x_axis_type` (ENUM): Data type - INT, FLOAT, or STRING
- `x_values` (STRING): Comma-separated values (e.g., "1, 2, 3")
- `y_axis_name` (STRING): Display name for Y-axis (e.g., "cfg")
- `y_axis_type` (ENUM): Data type - INT, FLOAT, or STRING
- `y_values` (STRING): Comma-separated values (e.g., "7.0, 8.0, 9.0")

**Outputs:**
- `initial_collection_data` (STRING): Empty array `"[]"` for For Loop Start
- `total_iterations` (INT): Number of iterations (len(x) × len(y))
- `xy_config` (STRING): JSON configuration (pass through workflow)
- `batch_id` (STRING): Unique timestamp ID (YYYYMMDD_HHMMSS) for organizing outputs

**Note:** Connect `batch_id` to your video generation node's `filename_prefix` for organized file naming.

### 2. XY Plot Get Values

Extract current X/Y parameter values for the loop iteration.

**Inputs:**
- `xy_config` (STRING): From XY Plot Setup
- `loop_index` (INT): From For Loop Start

**Outputs:**
- `x_value` (INT/FLOAT/STRING): Current X value (dynamically typed)
- `y_value` (INT/FLOAT/STRING): Current Y value (dynamically typed)
- `x_label` (STRING): Display label (e.g., "seed: 1")
- `y_label` (STRING): Display label (e.g., "cfg: 7.5")
- `xy_config` (STRING): Pass-through

**Important:** Connect `x_value`/`y_value` directly to your parameter inputs (e.g., KSampler seed, cfg). ComfyUI handles type conversion automatically.

### 3. XY Plot Collect Video

Accumulate video paths and labels during loop execution.

**Inputs:**
- `video_filepath` (STRING): Path from video generation node (e.g., VHS Video Combine)
- `x_label` (STRING): From XY Plot Get Values
- `y_label` (STRING): From XY Plot Get Values
- `xy_config` (STRING): Pass-through
- `collection_data` (STRING, optional): From For Loop Start `value1`

**Outputs:**
- `collection_data` (STRING): Updated JSON array → For Loop End `value1`
- `xy_config` (STRING): Pass-through

### 4. XY Plot Video Grid

Assemble all collected videos into a labeled grid.

**Inputs:**
- `collection_data` (STRING): From For Loop End `final_value1`
- `xy_config` (STRING): Pass-through from workflow
- `max_cell_width` (INT, default: 512): Maximum width per cell (maintains aspect ratio)
- `banner_font_size` (INT, default: 20): Title text size
- `label_font_size` (INT, default: 14): Axis label text size
- `font_color` (STRING, default: "white"): Text color
- `bg_color` (STRING, default: "black"): Background color
- `cleanup_files` (BOOLEAN, default: True): Delete source videos after assembly

**Outputs:**
- `video_grid` (IMAGE): Assembled grid as tensor (connect to Save Image/Video)
- `metadata` (STRING): JSON with grid info (shape, labels, fps, duration)

## Connection Guide

### Critical Connections

1. **For Loop Start Configuration:**
   - `initial_value1` ← XY Plot Setup: `initial_collection_data`
   - `iterations` ← XY Plot Setup: `total_iterations`

2. **Collection Data Flow (through loop):**
   - For Loop Start: `value1` → XY Plot Collect Video: `collection_data`
   - XY Plot Collect Video: `collection_data` → For Loop End: `value1`
   - For Loop End: `final_value1` → XY Plot Video Grid: `collection_data`

3. **Config Pass-Through (direct connections):**
   - XY Plot Setup: `xy_config` → XY Plot Get Values: `xy_config`
   - XY Plot Get Values: `xy_config` → XY Plot Collect Video: `xy_config`
   - XY Plot Collect Video: `xy_config` → XY Plot Video Grid: `xy_config`

### Common Mistakes

❌ **DON'T** manually type `"[]"` into For Loop Start - use `initial_collection_data` output  
❌ **DON'T** connect `collection_data` directly between nodes - it must flow through For Loop ports  
❌ **DON'T** forget to connect both `x_label` and `y_label` to XY Plot Collect Video  

## Troubleshooting

### Videos not in correct grid positions
- Check that your Y/X value ordering matches your expectations
- Grid is row-major: iterates Y values (outer) then X values (inner)

### Type mismatch errors
- Verify `x_axis_type`/`y_axis_type` match your parameter requirements
- Most ComfyUI nodes auto-convert STRING to INT/FLOAT when possible

### Missing videos in grid (black cells)
- Check video generation is completing successfully
- Verify video file paths are valid
- Check console for "Video file not found" warnings

### Text clipping or alignment issues
- Increase `max_cell_width` for larger grid
- Adjust `label_font_size` if text is too large/small
- Ensure all source videos have the same aspect ratio

### For Loop not completing
- Verify `total_iterations` connects to For Loop Start `iterations`
- Check loop isn't set to "Pause" mode in For Loop settings

## Advanced Usage

### Using Batch ID for Organization

Connect `batch_id` output from XY Plot Setup to your video node's `filename_prefix`:

```
XY Plot Setup: batch_id → [VHS Video Combine] filename_prefix
```

Result: Videos named like `20251003_143052_00001.mp4`, `20251003_143052_00002.mp4`, etc.

### Custom Video Dimensions

The grid automatically detects aspect ratio from the first video. For best results:
- Keep all videos at the same resolution
- Adjust `max_cell_width` based on your source video size (e.g., 512 for 512×512, 1024 for 1024×1024)

### Preserving Source Videos

Set `cleanup_files` to `False` in XY Plot Video Grid if you want to keep individual videos after grid assembly.

## Example Workflow

See `examples/wan_xy_plot.json` for a complete working example. Load it in ComfyUI to see the full node setup.

View `examples/wan_vace_xy_plot.mp4` to see the output grid format.

## Requirements

- ComfyUI (latest version recommended)
- `comfyui-easy-use` custom nodes (for For Loop)
- Python packages:
  - `moviepy>=1.0.3`
  - `torch` (included with ComfyUI)
  - `numpy` (included with ComfyUI)
  - `pillow` (included with ComfyUI)

## Example Workflow

See `example_workflow.json` for a complete working example.

## License

[Your License Here - e.g., MIT]

## Credits

Created for the ComfyUI community. Built with:
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [comfyui-easy-use](https://github.com/yolain/ComfyUI-Easy-Use)
- [MoviePy](https://zulko.github.io/moviepy/)

## Support

- Report issues: [GitHub Issues](https://github.com/yourusername/comfyui-xyvideoplot2/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/comfyui-xyvideoplot2/discussions)
