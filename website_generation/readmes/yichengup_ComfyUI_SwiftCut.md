# ComfyUI_YC_VideoCutHelper

A simple ComfyUI plugin that Its purpose and function is to replicate some of the editing effects of capcut,jianying and pr.

## 📦 Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/ComfyUI_SwiftCut.git
```

2. Install required dependencies:
```bash
pip install torch numpy pillow
```

3. Restart ComfyUI



https://github.com/user-attachments/assets/d353c911-2364-4d81-b6d8-7a28b06c8ce4



## 🛠️ Available Nodes

### Image Processing Nodes

#### 🎬 ImagePushPullLens
**Category:** `SwiftCut/Image`

Creates cinematic push-pull lens effects (dolly zoom) from single or multiple images.

**Features:**
- **Single to Multi Mode**: Generate multiple frames from a single image
- **Multi to Multi Mode**: Apply different crop ratios to existing frame sequences
- **Three-stage Animation**: Customizable start, middle, and end crop ratios
- **Center-based Cropping**: Maintains subject focus during zoom effects

**Inputs:**
- `image`: Input image(s)
- `frames`: Number of output frames (2-120)
- `start_crop_ratio`: Initial crop ratio (0.1-1.0)
- `middle_crop_ratio`: Middle point crop ratio (0.1-1.0)
- `end_crop_ratio`: Final crop ratio (0.1-1.0)
- `middle_frame`: Frame where middle ratio is reached
- `input_mode`: Processing mode selection

**Outputs:**
- `frames`: Processed image sequence
- `masks`: Corresponding crop masks

#### 🎨 ImageOverlayBlend
**Category:** `SwiftCut/Image`

Advanced multi-frame blending with background overlay and transparency control.

**Features:**
- **Dynamic Alpha Control**: Three-stage transparency animation
- **Multiple Blend Modes**: Normal, Multiply, Screen, Overlay, Soft Light
- **Custom Background**: Hex color background support
- **Professional Color Mixing**: Industry-standard blend algorithms

**Inputs:**
- `frames`: Input frame sequence
- `background_color`: Hex color (e.g., "#000000")
- `start_alpha_ratio`: Initial transparency (0.0-1.0)
- `middle_alpha_ratio`: Middle transparency (0.0-1.0)
- `end_alpha_ratio`: Final transparency (0.0-1.0)
- `middle_frame`: Transition point frame
- `blend_mode`: Blending algorithm selection

**Outputs:**
- `blended_frames`: Processed frame sequence
- `alpha_masks`: Transparency masks

#### 🔀 ImageBatchBlend
**Category:** `SwiftCut/Image`

High-performance batch image blending for complex compositions.

**Features:**
- **Automatic Channel Matching**: RGB/RGBA/Grayscale compatibility
- **Frame Synchronization**: Automatic length matching
- **Professional Blend Modes**: 7 industry-standard modes
- **Batch Processing**: Optimized for large sequences

**Inputs:**
- `image1`: First image batch
- `image2`: Second image batch
- `blend_factor`: Blend strength (0.0-1.0)
- `blend_mode`: Blending algorithm

**Outputs:**
- `blended_images`: Final composited sequence

### Utility Nodes

#### 📋 SelectImages
**Category:** `SwiftCut/Utils`

Precise image selection from batches with advanced indexing.

**Features:**
- **Flexible Indexing**: Single, range, and step selections
- **Negative Indexing**: Reverse selection support
- **Error Handling**: Configurable bounds checking

#### 📋 SelectImagesAdvanced
**Category:** `SwiftCut/Utils`

Extended selection capabilities with complex pattern support.

**Features:**
- **Complex Patterns**: Mixed index formats
- **Batch Processing**: Multiple selection operations
- **Safety Controls**: Comprehensive error handling

#### If you benefit from this project, please buy the author a cup of coffee.
<img width="1536" height="841" alt="未标题-2" src="https://github.com/user-attachments/assets/a562fcfd-cb65-4695-a2a8-ca3eb6a6db67" />


