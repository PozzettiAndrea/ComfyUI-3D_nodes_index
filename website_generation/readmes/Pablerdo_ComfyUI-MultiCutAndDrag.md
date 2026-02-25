# ComfyUI-MultiCutAndDrag

A ComfyUI extension that allows cutting and dragging multiple parts of an image along specified paths, with advanced masking capabilities.

## Features

### MultiCutAndDragOnPath

This node allows you to cut out parts of an image based on masks and then animate them along specified coordinate paths.

**Features:**
- Cut multiple regions from an image using masks
- Drag these regions along coordinate paths
- Optionally rotate the cut regions during animation
- Background inpainting for removed regions
- Supports custom background images
- Creates a batch of frames showing the animation

**Input Format:**
Coordinate paths should be provided as a JSON array of arrays containing coordinate objects:

```json
[
  [{"x": 100, "y": 100}, {"x": 200, "y": 200}, {"x": 300, "y": 100}],
  [{"x": 50, "y": 150}, {"x": 40, "y": 200}, {"x": 30, "y": 250}],
]
```

### BatchImageToMask

This node converts RGB images to binary masks using grayscale conversion and thresholding.

**Features:**
- Batch processing of multiple images
- Automatic handling of different tensor formats and dimensions
- Adjustable threshold for mask creation
- Optional morphological dilation to expand mask areas

### MapTrajectoriesToSegmentedMasks

This node aligns trajectory paths with mask centroids, allowing for more intuitive animation of segmented objects.

**Features:**
- Automatically calculates the centroid of each mask
- Translates trajectory paths to align with mask centroids
- Maintains the shape and relative positions within each path
- Handles multi-channel and single-channel masks
- Returns both transformed masks and the translated trajectory JSON

## Installation

### Method 1: Via ComfyUI Manager

1. Open ComfyUI Manager
2. Search for "MultiCutAndDrag"
3. Click Install

### Method 2: Manual Installation

```
WORKDIR /comfyui/custom_nodes
RUN git clone https://github.com/pablerdo/ComfyUI-MultiCutAndDrag.git --recursive
WORKDIR /comfyui/custom_nodes/ComfyUI-MultiCutAndDrag
RUN git reset --hard (latestcommit hash)
RUN if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi
RUN if [ -f install.py ]; then python install.py || echo "install script failed"; fi
```
3. Restart ComfyUI

## Example Workflow

1. Load an image and create masks for the areas you want to animate
2. Use BatchImageToMask to convert segmentation images to proper masks if needed
3. Define coordinate paths for each mask
4. Connect them to MultiCutAndDragOnPath to create an animation sequence
5. Alternatively, use MapTrajectoriesToSegmentedMasks to automatically align trajectories with mask centroids

## Requirements

- torch >= 2.0.0
- torchvision >= 0.15.0
- numpy >= 1.20.0
- Pillow >= 9.0.0
- scipy >= 1.8.0
- opencv-python
- Other dependencies as listed in requirements.txt

## License

This project is licensed under the GNU General Public License v3.0
