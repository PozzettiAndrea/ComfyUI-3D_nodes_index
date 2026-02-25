# ComfyUI-HappNodeSet

Custom nodes for ComfyUI

## Installation

### Method 1: ComfyUI Manager
Search for "HappNodeSet" in ComfyUI Manager and install.

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mikemojen/ComfyUI-HappNodeSet.git
```

## Requirements

If you have specific Python dependencies, install them:
```bash
pip install -r requirements.txt
```

## Nodes

# ComfyUI Line Counter & Measurer

A ComfyUI custom node package that detects, counts, and measures straight/dashed lines in images.

## Features

- **Line Detection**: Automatically detects all straight and dashed lines in an image
- **Line Counting**: Counts the total number of distinct lines
- **Length Measurement**: Measures each line's length in pixels
- **4-Way Junction Resolution**: Intelligently handles crossing lines by pairing collinear segments
- **Visualization**: Creates a stitched image showing each line separately with its length

## Algorithm

The node uses a sophisticated 7-step algorithm:

1. **Preprocessing**: Grayscale → Binary threshold → Noise cleanup
2. **Skeletonization**: Thin all lines to 1-pixel width
3. **Graph Building**: Identify junction points and endpoints
4. **Junction Classification**: Count connections at each junction
5. **4-Way Junction Resolution**: Pair collinear segments at crossings
6. **Line Extraction**: Trace through graph following pairing rules
7. **Measurement & Export**: Calculate lengths and generate visualizations

## Installation

1. Clone or copy this folder to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone <repo_url> comfyui_line_counter
   # OR
   cp -r /path/to/comfyui_line_counter ./
   ```

2. Install dependencies:
   ```bash
   pip install -r comfyui_line_counter/requirements.txt
   ```

3. Restart ComfyUI

## Nodes

### LineCounter (Basic)

**Inputs:**
- `image`: Input image (IMAGE)
- `threshold` (0-255, default: 128): Binary threshold value
- `min_line_length` (1-1000, default: 10): Minimum line length to include
- `noise_removal_kernel` (1-11, default: 3): Kernel size for noise removal
- `angle_tolerance` (5-90°, default: 30°): Tolerance for collinearity at junctions

**Outputs:**
- `line_count` (INT): Number of detected lines
- `line_lengths` (STRING): Comma-separated lengths in pixels
- `visualization` (IMAGE): Stitched image of individual lines

### LineCounterAdvanced

Same as basic, plus:

**Additional Inputs:**
- `dashed_line_gap` (0-50, default: 10): Gap size to close for dashed lines
- `line_thickness` (1-10, default: 2): Line thickness in visualization

**Additional Outputs:**
- `skeleton_debug` (IMAGE): Debug view showing skeleton with junctions (red) and endpoints (green)

## Usage Example

1. Add a "Load Image" node
2. Connect it to "Line Counter & Measurer"
3. Adjust parameters as needed:
   - Lower `threshold` if lines are light colored
   - Increase `dashed_line_gap` for dashed lines with larger gaps
   - Adjust `angle_tolerance` if lines at small angles should be separate
4. Connect outputs to preview nodes or save nodes

## Input Requirements

- Image should have dark lines on a white/light background
- Lines should be relatively straight (not curved)
- Works best with clean, high-contrast images

## Tips

- For dashed lines: Increase `dashed_line_gap` to connect the dashes
- For noisy images: Increase `noise_removal_kernel`
- For crossing lines: Adjust `angle_tolerance` - lower values require more exact alignment
- For thin/faint lines: Lower the `threshold` value

## Example Workflow

```
[Load Image] → [LineCounter] → [Preview Image (visualization)]
                            ↘ [Show Text (line_count)]
                            ↘ [Show Text (line_lengths)]
```

## License

MIT License

## Usage

[Add usage examples]