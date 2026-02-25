# Niutonian Smart Image Suite

A comprehensive ComfyUI custom node suite for intelligent image stitching, processing, and manipulation with automatic handling of empty/bypassed inputs.

## Nodes Included

### 1. Smart Image Stitch
Linear image stitching with intelligent input handling.
- **Features**: 4-direction stitching, aspect ratio preservation, smart resizing
- **Inputs**: Up to 6 images
- **Use Case**: Creating panoramas, contact sheets, before/after comparisons

### 2. Smart Grid Stitch  
Automatic grid arrangement with flexible sizing.
- **Features**: Auto/manual grid sizing, uniform cell sizing, gap control
- **Inputs**: Up to 9 images
- **Use Case**: Photo grids, comparison matrices, thumbnail sheets

### 3. Smart Panorama Stitch
Advanced panoramic stitching with feature detection.
- **Features**: Auto overlap detection, feature matching, seamless blending
- **Inputs**: Up to 6 images
- **Use Case**: Landscape panoramas, 360° views, wide-angle compositions

### 4. Smart Collage Maker
Artistic collage creation with varied layouts.
- **Features**: Multiple layout styles, size variation, rotation, overlapping
- **Inputs**: Up to 9 images  
- **Use Case**: Artistic compositions, mood boards, creative layouts

### 5. Smart Image Splitter
Intelligent image splitting into multiple parts.
- **Features**: Grid splitting, overlap control, multiple output formats
- **Inputs**: Single image
- **Use Case**: Tiling for printing, creating puzzle pieces, detail extraction

### 6. Smart Border & Frame
Professional framing with multiple styles.
- **Features**: 7 frame styles, shadows, rounded corners, custom colors
- **Inputs**: Single image
- **Use Case**: Photo finishing, presentation, artistic effects

### 7. Smart Batch Processor
Batch operations with template saving.
- **Features**: Multiple operations, template system, progress logging
- **Inputs**: Up to 9 images
- **Use Case**: Workflow automation, consistent processing, batch jobs

## Common Features

- **Smart Input Handling**: Automatically ignores empty or bypassed image inputs
- **Aspect Ratio Preservation**: Multiple handling modes (pad, crop, stretch)
- **High-Quality Resizing**: Lanczos, bilinear, bicubic, nearest neighbor options
- **Flexible Alignment**: Start, center, end positioning
- **Background Control**: Transparent, white, black, custom colors
- **Professional Quality**: Optimized for print and digital use

## Installation

Copy this folder to your ComfyUI custom_nodes directory and restart ComfyUI.

```
ComfyUI/custom_nodes/comfyui_niutonian_smart_image/
```

All nodes will appear under the "Niutonian/Image Processing" category.

## Quick Start Examples

### Basic Linear Stitching
1. Add "Smart Image Stitch" node
2. Connect 2-6 images
3. Set direction (right/left/top/bottom)
4. Choose resize mode and aspect handling
5. Result: Seamlessly stitched image

### Photo Grid Creation  
1. Add "Smart Grid Stitch" node
2. Connect multiple images
3. Select grid size (2x2, 3x3, etc.)
4. Set cell sizing mode
5. Result: Professional photo grid

### Panorama Creation
1. Add "Smart Panorama Stitch" node  
2. Connect overlapping images in sequence
3. Choose auto or manual overlap detection
4. Set feature detector and confidence
5. Result: Seamless panoramic image

### Artistic Collage
1. Add "Smart Collage Maker" node
2. Connect images for collage
3. Choose layout style (magazine, scattered, spiral)
4. Enable rotation and size variation
5. Result: Creative artistic composition

## Advanced Usage

### Template System (Batch Processor)
Save frequently used settings as templates for consistent processing across projects.

### Chaining Nodes
Combine multiple nodes for complex workflows:
- Split → Process → Grid → Frame
- Stitch → Collage → Border
- Panorama → Split → Batch Process

### Quality Settings
- Use Lanczos resizing for best quality
- Choose "pad" aspect handling to preserve content
- Enable shadows and borders for professional finish