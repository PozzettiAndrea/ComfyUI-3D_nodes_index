# FL Path Animator

A standalone ComfyUI custom node for creating animated shapes that follow user-drawn paths.

## Features

- **Interactive Path Editor** - Visual modal interface for drawing motion paths and static anchor points
- **Two Path Types**:
  - **Motion Paths** - Draw continuous paths for shapes to follow over time
  - **Static Anchors** - Single-point paths for stationary shapes
- **Background Image Support** - Load or paste reference images to draw paths on
- **WAN ATI Compatible** - Outputs 121-point resampled coordinates for stable AI video generation
- **Visual Effects** - Blur, trails, rotation, borders, and custom colors
- **Multiple Shapes** - Circle, square, triangle, hexagon, and star

## Installation

1. Clone or download this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/machinedelusions/ComfyUI_FL-Path-Animator.git
```

2. Restart ComfyUI

## Usage

### Basic Workflow

1. Add the "FL Path Animator" node to your workflow
2. Click the **"Edit Paths"** button to open the path editor
3. Use the toolbar to:
   - **✏️ Pencil** - Draw motion paths (hold SHIFT for straight lines)
   - **📍 Point** - Add static anchor points
   - **🗑️ Eraser** - Delete paths by clicking
   - **↖️ Select** - Select and inspect paths
   - **🔒 Lock Perimeter** - Auto-generate static points around border
4. Optionally load a background image with **🖼️** or paste with **Ctrl+V**
5. Press **ESC** to save and close
6. Configure shape properties in the node
7. Connect outputs to your workflow

### Keyboard Shortcuts

- **ESC** - Save paths and close editor
- **SHIFT (hold)** - Draw straight lines (horizontal/vertical/45° diagonal)
- **Ctrl+V** - Paste background image from clipboard

### Node Parameters

#### Required
- `frame_width` / `frame_height` - Output frame dimensions
- `frame_count` - Number of frames to generate
- `shape` - Shape type (circle, square, triangle, hexagon, star)
- `shape_size` - Size in pixels
- `shape_color` - Color as hex (#FFFFFF) or RGB (255,255,255)
- `bg_color` - Background color

#### Optional
- `blur_radius` - Gaussian blur strength
- `trail_length` - Motion trail effect (0.0-1.0)
- `rotation_speed` - Shape rotation over time
- `border_width` - Border thickness
- `border_color` - Border color
- `paths_data` - JSON data from path editor (auto-managed)

### Outputs

1. **IMAGE** - Batch of rendered frames (shape following paths)
2. **MASK** - Alpha masks extracted from red channel
3. **STRING** - WAN ATI-compatible coordinate data (121 points per path)

## WAN ATI Integration

The coordinate output is specifically formatted for WAN (Warp and Noise) ATI video generation:

- Each path is resampled to exactly 121 points
- Arc-length parameterization ensures smooth motion
- Static points are repeated 121 times for stable anchors
- Output format: `[[{x, y}, ...], [{x, y}, ...]]` (array of tracks)

This prevents jitter and warping in AI-generated video by providing consistent tracking data.

## Path Editor Tools

### ✏️ Pencil Tool
Draw continuous motion paths by clicking and dragging. Shapes will smoothly follow these paths over the animation duration.

- Minimum 3px spacing between points for smoothing
- Hold SHIFT to constrain to straight lines

### 📍 Point Tool
Click once to create a static anchor point. Shapes at these positions won't move, useful for border stability in video generation.

### 🗑️ Eraser Tool
Click on any path to delete it.

### ↖️ Select Tool
Click paths to inspect details:
- Neon green highlight
- Point count and numbering
- Path type indicator

### 🔒 Lock Perimeter
Automatically distributes N static anchor points evenly around the canvas border. Useful for WAN video generation to stabilize frame edges.

## Technical Details

- **Path Resampling**: Arc-length parameterization for constant-speed motion
- **Canvas Scaling**: Paths automatically scale from editor coordinates to output frame size
- **Background Cache**: Uploaded/pasted images persist across editor sessions
- **Animated Preview**: Directional flow indicators show path direction in real-time

## Requirements

- Python 3.8+
- PIL (Pillow)
- NumPy
- PyTorch
- ComfyUI

## License

MIT License - See LICENSE file for details

## Credits

Created by Machine Delusions for the Fill-Nodes pack.
Extracted as standalone node for easier distribution.

## Support

For issues, feature requests, or questions:
- GitHub Issues: https://github.com/machinedelusions/ComfyUI_FL-Path-Animator/issues
- Patreon: https://www.patreon.com/c/Machinedelusions
