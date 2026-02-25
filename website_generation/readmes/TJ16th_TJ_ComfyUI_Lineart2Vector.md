# TJ ComfyUI Lineart to Vector

ComfyUI custom nodes for line art centerline extraction and SVG manipulation with advanced editing and visualization capabilities.

## Overview

Complete pipeline from line art images to editable SVG vectors: line detection → centerline extraction → SVG generation → style editing → visualization → raster output.

## Features

### Core Extraction & Conversion

- **Line Region Detector**: Extract centerlines from line art images using skeletonization
- **Centerline to SVG**: Convert extracted centerlines to clean SVG vector paths with Douglas-Peucker simplification
- **Mask Cleanup**: Remove noise and small regions from masks
- **SVG Path Cleanup**: Remove duplicate/overlapping paths based on distance threshold
- **SVG File Saver**: Save SVG strings to files with customizable paths

### Visualization & Layout

- **SVG Group Layout**: XY plot visualization with automatic tiling
  - Auto-layout mode: tile all paths/groups in a grid
  - Manual placement via JSON configuration
  - Grid lines and labels for easy identification
  - Background preview showing all paths at low opacity
  - Global fill/stroke color overrides
  - Per-tile color/style customization

- **SVG To Image**: Render SVG to raster images using Pillow
  - Custom resolution and scaling
  - Background color control
  - Global fill/stroke overrides
  - Control point visualization

### Style Editing

- **SVG Style Editor**: Modify styles using CSS selectors
  - Supports ID (`#path0`), class (`.hair`), attribute (`[id*=eye]`) selectors
  - Change stroke, fill, stroke-width, and opacity

- **SVG Style Editor (Simple)**: Path index-based style editing
  - Simple syntax: `0,2-5,10` for path selection
  - Direct parameter inputs (no JSON required)

- **SVG Color Picker**: Generate normalized #RRGGBBAA color strings
  - Preset colors + custom RGB/Alpha overrides
  - Outputs consistent hex format for downstream nodes

### Path Management

- **SVG Auto Reorder**: Automatic path ordering for optimal rendering
  - Sort modes: area-based, proximity-based, hybrid (area tiers + proximity)
  - Reverse option
  - Optional ID renumbering (`path0`, `path1`, ...)

- **SVG Reorder**: Manual path ordering via priority rules
  - Specify exact order with selector-based rules

- **SVG Visibility**: Show/hide paths by selector
  - Display control per element
  - Optional deletion mode

## Interactive UI Features

**Live Color Picker Widget** (JavaScript extension)
- Appears automatically on all color fields
- Color swatch + alpha slider + live preview
- No node execution needed - updates immediately
- Transparent background checker pattern

Supported nodes:
- SVG To Image
- SVG Group Layout
- SVG Style Editor (Simple)
- SVG Color Picker

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/TJ16th/TJ_ComfyUI_Lineart2Vector.git
# Restart ComfyUI
```

### Requirements

All dependencies are listed in `requirements.txt`:
- torch
- numpy
- Pillow
- opencv-python
- scikit-image
- scipy

These are typically already installed with ComfyUI. If you encounter issues:

```bash
pip install -r requirements.txt
```

### SVG To Image Note

The `SVG To Image` node provides **basic SVG path rendering**:
- ✅ **No additional dependencies**: Works with Pillow alone (already in ComfyUI)
- ✅ **Windows compatible**: No native DLLs required
- ⚠️ **Limitations**: Complex SVG features (gradients, filters, advanced paths) not supported

**Supported:**
- Basic path commands (M, L, H, V, C, Z)
- Stroke/fill colors
- Simple line/polygon drawing

**For high-quality rendering:**
- Use `SVG File Saver` then render in Inkscape/Illustrator/browser
- On Linux/macOS, consider CairoSVG for advanced features

## Usage Examples

### Basic Workflow: Line Art → SVG

1. **Line Region Detector**: Input your line art image
2. **Centerline to SVG**: Convert detected lines to SVG paths
3. **SVG Path Cleanup**: Remove duplicate paths (optional)
4. **SVG File Saver**: Save the result

### XY Plot Visualization

1. Extract centerlines and convert to SVG
2. **SVG Group Layout**:
   - Set `auto_layout = true`
   - Adjust `tile_cols` and `tile_spacing`
   - Use `override_fill_color` for consistent coloring
   - Enable `show_all_background` to see context

### Style Customization

**Method 1: Global Override**
```
SVG Group Layout:
├─ override_fill_color: "#FF0000FF"  (all paths red)
└─ override_stroke_color: "#000000FF" (all strokes black)
```

**Method 2: Per-Path Control**
```
SVG Style Editor (Simple):
├─ path_indices: "0,2-5,10"
├─ stroke_color: "#FF0000"
└─ stroke_width: 3.0
```

**Method 3: Selector-Based**
```json
SVG Style Editor:
[
  {"selector": "#hair", "stroke": "#000000", "fill": "#FFFF00"},
  {"selector": ".shadow", "opacity": 0.5}
]
```

### Automatic Path Ordering

```
SVG Auto Reorder:
├─ sort_mode: "area_then_proximity"
├─ area_tiers: 3  (group by size, then sort by proximity)
├─ renumber_ids: true  (rename as path0, path1, ...)
└─ reverse: false
```

## JSON Configuration Examples

### SVG Group Layout: Manual Placement

```json
[
  {
    "selector": "#path0",
    "x": 100,
    "y": 100,
    "scale": 1.5,
    "stroke": "#FF0000FF",
    "fill": "none",
    "stroke_width": 2.0
  },
  {
    "selector": "#path1",
    "x": 400,
    "y": 100,
    "fill": "#00FF00FF",
    "opacity": 0.8
  }
]
```

### SVG Reorder: Priority Rules

```json
[
  {"selector": "#background", "priority": 0},
  {"selector": ".shadow", "priority": 1},
  {"selector": ".main", "priority": 2},
  {"selector": "#highlights", "priority": 3}
]
```

## Node Reference

### Line Region Detector
Extract line regions from line art images.

**Inputs:**
- `image`: Input image
- `background_mode`: Background detection (auto/white/black)
- `line_detection_method`: Detection method (edge/morphology/hybrid)
- Additional threshold parameters

**Outputs:**
- `line_mask`: Line region mask
- `fill_mask`: Fill region mask
- `preview_image`: Preview with overlays
- `color_info`: Detected colors (JSON)

### Centerline to SVG
Convert line masks to SVG paths via centerline extraction.

**Inputs:**
- `line_mask`: Line region mask
- `algorithm`: Extraction algorithm (ridge/skeleton/medial_axis)
- `smoothing`: Path smoothing level
- `simplification`: Douglas-Peucker tolerance

**Outputs:**
- `svg_string`: SVG path string
- `centerline_image`: Centerline preview
- `statistics`: Path statistics (JSON)

### SVG Group Layout
Visualize SVG paths in a tiled layout with styling options.

**Inputs:**
- `svg_string`: Input SVG
- `canvas_width`/`canvas_height`: Output dimensions
- `auto_layout`: Enable automatic tiling
- `tile_cols`/`tile_spacing`: Grid layout parameters
- `override_fill_color`/`override_stroke_color`: Global color overrides
- `show_all_background`: Show all paths at low opacity
- `show_grid_lines`/`show_labels`: Visual aids
- `group_positions_json`: Manual placement rules (JSON)

**Outputs:**
- `image`: Rendered composite
- `meta`: Layout statistics (JSON)

### SVG Style Editor
Apply style changes using CSS selectors.

**Inputs:**
- `svg_string`: Input SVG
- `style_rules_json`: Style rules (JSON array)

**Outputs:**
- `svg`: Modified SVG
- `meta`: Applied changes (JSON)

### SVG Style Editor (Simple)
Apply styles using path index ranges.

**Inputs:**
- `svg_string`: Input SVG
- `path_indices`: Path selection (e.g., "0,2-5,10")
- `stroke_color`/`fill_color`: Color overrides
- `stroke_width`/`opacity`: Style parameters

**Outputs:**
- `svg`: Modified SVG
- `meta`: Modification stats (JSON)

### SVG Auto Reorder
Automatically reorder paths for optimal rendering.

**Inputs:**
- `svg_string`: Input SVG
- `sort_mode`: Sorting algorithm (area/proximity/area_then_proximity)
- `reverse`: Reverse final order
- `area_tiers`: Number of size tiers (for hybrid mode)
- `renumber_ids`: Renumber paths as path0, path1, ...

**Outputs:**
- `svg`: Reordered SVG
- `meta`: Sorting statistics (JSON)

### SVG Color Picker
Generate normalized color strings.

**Inputs:**
- `base_color`: Input color (any format)
- `preset`: Color preset
- `r_override`/`g_override`/`b_override`/`a_override`: Component overrides

**Outputs:**
- `color_hex`: Normalized #RRGGBBAA string
- `meta`: Parsed components (JSON)

## Tips

- **Performance**: For large SVGs, use `SVG Path Cleanup` to reduce path count
- **Color Workflow**: Use `SVG Color Picker` to generate consistent color strings
- **Debugging**: Enable `show_labels` in SVG Group Layout to see path IDs
- **Path Order**: Use `SVG Auto Reorder` with `renumber_ids=true` before using index-based editing

## Development

### Structure
- **Python nodes**: `*.py` files for backend processing
- **JavaScript extension**: `web/tj_color_picker.js` for UI enhancements
- **WEB_DIRECTORY export**: Enables custom UI widgets

### Adding Color Fields
Edit `web/tj_color_picker.js`:
```javascript
const colorFields = new Set([
  "your_field_name",  // Add here
  // ...existing fields
]);
```

## License

MIT License

## Links

- GitHub: https://github.com/TJ16th/TJ_ComfyUI_Lineart2Vector
- Issues: https://github.com/TJ16th/TJ_ComfyUI_Lineart2Vector/issues

## Changelog

### Latest (2025-11-09)
- Added fill/stroke color override to SVG Group Layout (global + per-placement)
- Added `renumber_ids` option to SVG Auto Reorder
- Fixed JavaScript extension loading (WEB_DIRECTORY export + correct directory structure)
- Added live color picker UI widget with alpha control
- Added SVG Color Picker node for consistent #RRGGBBAA output

### Initial Release
- Line art centerline extraction
- SVG conversion and path simplification
- Multi-mode auto reorder (area/proximity/hybrid)
- CSS selector-based and index-based style editing
- XY plot layout with auto-tiling
- SVG visibility control

---

[日本語版 README](README_ja.md)
