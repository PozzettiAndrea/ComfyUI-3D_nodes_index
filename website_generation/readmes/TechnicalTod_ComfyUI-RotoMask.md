# ComfyUI Roto Mask

A rotoscoping tool for ComfyUI that allows you to create animated masks using polygon curves with keyframe interpolation.

## Features

### 🎨 Interactive Canvas Editor
- **Draw Mode**: Click to create polygon curves on the canvas
- **Edit Mode**: Select and drag control points to modify curves
- **Soften/Sharpen Points**: Toggle individual points between smooth (curved) and sharp (angular)
- **Visual Feedback**: Selected curves highlighted in blue with semi-transparent overlays
- **Auto-Resize**: Canvas automatically matches loaded image dimensions (up to 2048px)

### 🎬 Animation & Timeline
- **Keyframe Animation**: Each curve has its own independent keyframe timeline
- **Automatic Interpolation**: Frames between keyframes are automatically interpolated
- **Frame Playback**: Play/Pause controls with 24fps playback
- **Frame Slider**: Scrub through frames to preview animation
- **Batch Frame Loading**: Upload multiple images to create frame sequences
- **Output Frame Range**: Set custom start and end frames for rendering

### 🛠️ Advanced Tools
- **Feather Amount**: Adjustable Gaussian blur for smooth mask edges (0-100)
- **Background Color**: Customizable mask background color
- **Mask Visualization**: Adjustable mask color and opacity for preview
- **Curve List Panel**: Manage all curves with per-curve keyframe navigation
- **Multi-Curve Support**: Combine multiple curves into a single mask
- **Per-Curve Keyframes**: Each curve interpolates independently
- **Add Point**: Add new points to existing curves by clicking on edges

### 📤 Multiple Outputs
- **Mask as Image**: RGB mask tensor for preview
- **Mask**: Single-channel mask for compositing
- **Masked Image**: Original image with mask overlay applied
- **Loaded Image**: Original loaded image

## Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` directory:
   ```
   ComfyUI/custom_nodes/ComfyUI_Roto/
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

## Quick Start

1. **Add the Node**: Search for "Roto Mask" in the node menu and add it to your workflow

2. **Load Frames** (optional):
   - Click "Load Frames" button
   - Select multiple images (Ctrl+Click or Shift+Click)
   - Images will be uploaded and the frame slider will update automatically

3. **Draw Curves**:
   - Press `B` or click "Draw (B)" to enter Draw mode
   - Click on the canvas to create a polygon curve
   - Curves are automatically closed for filled masks

4. **Edit Curves**:
   - Press `V` or click "Edit (V)" to enter Edit mode
   - Click and drag control points to modify curves
   - Use Shift+Click to select multiple points
   - Click "Soften Point" to make selected points smooth (curved)
   - Click "Sharpen Point" to make selected points angular

5. **Add Points**:
   - Select a curve in Edit mode
   - Click "Add Point" button
   - Click on a curve edge to add a new point at that location

6. **Animate**:
   - Move the frame slider to a different frame
   - Edit curves on that frame (automatically creates keyframes)
   - Frames between keyframes will interpolate automatically

6. **Adjust Settings**:
   - **Feather Amount**: Use the slider to control edge softness (0 = sharp, 100 = very soft)
   - **Mask Color**: Choose the background color for masked areas

7. **Render**: Set frame range (set to full range by default) to render a specific range of the total loaded clip

## Advanced Usage

### Independent Curve Interpolation

Each curve maintains its own keyframe timeline. This means:
- Curve A can have keyframes at frames 1, 10, 20
- Curve B can have keyframes at frames 1, 15, 30
- They interpolate independently without interfering with each other

### Keyframe Management

- **Creating Keyframes**: Edit a curve on a non-keyframe frame - only that curve gets a keyframe
- **Navigating Keyframes**: Use ◀/▶ buttons in the curve list to jump between keyframes for each curve
- **Deleting Keyframes**: Click 🔑✕ button to remove a keyframe for a specific curve on the current frame
- **Deleting Curves**: Click ✕ button to remove a curve from all frames

The value is stored in the curve metadata and persists with your workflow.

## UI Controls

### Toolbar
- **Load Frames**: Upload multiple images for frame sequences
- **Draw (B)**: Switch to draw mode
- **Edit (V)**: Switch to edit mode
- **Add Point**: Click to enable, then click on curve edge to add point
- **Soften/Sharpen Point**: Toggle selected points between smooth and angular

### Timeline
- **Frame Counter**: Shows current frame / total frames
- **Frame Slider**: Scrub through frames
- **Play/Pause**: Toggle animation playback at 24fps

### Settings Panel
- **Mask Visualization Settings**:
  - **Mask Color**: Color picker for preview overlay color
  - **Mask Opacity**: Slider to control preview overlay transparency (0-100%)
- **Image Output Settings**:
  - **Feather Amount**: Slider to control edge softness (0-100)
  - **Background Color**: Color picker for mask background
- **Output Frame Range**:
  - **Start Frame**: First frame to render
  - **End Frame**: Last frame to render

### Curve List Panel
- Shows all curves with their IDs
- **Red dot**: Indicates curve has a keyframe on current frame
- **◀**: Jump to previous keyframe for this curve
- **▶**: Jump to next keyframe for this curve
- **🔑✕**: Delete keyframe for this curve on current frame
- **✕**: Delete curve from all frames
- **Click curve name**: Select curve on canvas


## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.