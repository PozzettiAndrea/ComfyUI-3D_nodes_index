# ComfyUI FOV Estimator

A ComfyUI custom node collection that estimates the **Field of View (FOV)** and **tilt angle (horizon angle)** of images using computer vision techniques.

## Features

- **Two Analysis Methods**:
  - **RGB-based**: Analyzes images directly using edge detection and line detection
  - **Depth-based**: Uses depth maps for more robust geometric analysis (recommended)
- **FOV Estimation**: Estimates the camera's field of view in degrees by detecting vanishing points
- **Tilt Detection**: Detects the horizon angle and tilt of the camera in degrees
- **Visual Debugging**: Optionally overlays detected lines, vanishing points, and measurements on the output image
- **Configurable Parameters**: Adjust thresholds for different image types and depth estimation models

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/gitcapoom/comfyui_fovestimator.git
   ```

3. Install dependencies:
   ```bash
   cd comfyui_fovestimator
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Usage

Two nodes are available under the **image/analysis** category:

### 1. FOV & Tilt Estimator (Depth) - **Recommended**

Uses depth maps for more accurate and robust estimation.

**Workflow:**
```
Load Image → Depth Estimation (MiDaS/Depth Anything) → FOV & Tilt Estimator (Depth)
                                ↓
                          Original Image (for visualization)
```

**Inputs:**
- **depth_map** (required): Depth map from a depth estimation node (MiDaS, Depth Anything, etc.)
- **image** (required): Original RGB image for visualization overlay
- **depth_edge_threshold** (optional, default: 0.1): Threshold for depth discontinuities (0.01-1.0)
- **line_threshold** (optional, default: 50): Threshold for Hough line detection (10-300)
- **visualize** (optional, default: True): Whether to draw detected features

**Outputs:**
- **annotated_image**: RGB image with visualization overlays
- **fov_degrees**: Estimated horizontal field of view (float)
- **tilt_degrees**: Estimated tilt angle (float)
- **info**: Formatted text with results

**Example Workflow:**
1. Load your image
2. Pass it through a depth estimation node (MiDaS, Depth Anything, etc.)
3. Connect both the depth map and original image to the Depth FOV Estimator
4. The node will analyze depth discontinuities (3D edges) for more accurate results

### 2. FOV & Tilt Estimator (RGB)

Analyzes RGB images directly without requiring depth estimation.

**Inputs:**
- **image** (required): The input image to analyze
- **edge_threshold_low** (optional, default: 50): Lower threshold for Canny edge detection (0-255)
- **edge_threshold_high** (optional, default: 150): Upper threshold for Canny edge detection (0-255)
- **line_threshold** (optional, default: 100): Threshold for Hough line detection (10-500)
- **visualize** (optional, default: True): Whether to draw detected features

**Outputs:**
- **annotated_image**: The input image with visualization overlays
- **fov_degrees**: Estimated field of view in degrees (float)
- **tilt_degrees**: Estimated tilt/horizon angle in degrees (float)
- **info**: Text string with formatted results

**Example Workflow:**
1. Load an image
2. Connect it directly to the FOV & Tilt Estimator (RGB) node
3. View the results with detected features

## How It Works

### Depth-Based Method (Recommended)

**FOV Estimation from Depth:**
1. Detects **depth discontinuities** (3D edges) using Sobel gradients on the depth map
2. Applies bilateral filtering to preserve edges while smoothing
3. Detects lines from depth discontinuities using Hough transform
4. Filters for non-horizontal lines (converging building edges, roads, etc.)
5. Finds dominant vanishing point using RANSAC-like clustering
6. Calculates focal length from vanishing point position
7. Converts to horizontal FOV: `hfov = 2 × arctan(width / (2 × focal_length))`

**Tilt Estimation from Depth:**
1. Detects depth discontinuities (horizon appears as depth transition)
2. Finds horizontal lines in depth edges
3. Calculates horizon position relative to frame center
4. Converts to tilt angle using vertical FOV
5. Falls back to depth gradient analysis if no clear horizon found

**Advantages:**
- Depth discontinuities represent **real 3D geometry**, independent of texture/lighting
- More robust to shadows, reflections, and complex textures
- Cleaner edge detection from structural boundaries
- Can analyze depth gradients when lines aren't clear

### RGB-Based Method

**FOV Estimation:**
Uses the pinhole camera model and vanishing point analysis:

1. Applies Canny edge detection to find edges in RGB image
2. Uses Hough transform to detect lines
3. Filters for non-horizontal converging lines
4. Finds dominant vanishing point through intersection clustering
5. Calculates focal length from vanishing point distance to image center
6. Converts to FOV: `hfov = 2 × arctan(width / (2 × focal_length))`

**Tilt Estimation:**
1. Detects edges using Canny
2. Finds horizontal lines (potential horizons)
3. Calculates horizon position relative to frame center
4. Converts to tilt angle using vertical FOV
5. Tilt = 0° when horizon is centered

**Key Principle:** The distance from the image center to a vanishing point approximates the camera's focal length in pixels, enabling FOV calculation from pure geometry.

## Tips

### For Depth-Based Estimation (Recommended)
- **Use high-quality depth maps**: MiDaS v3.1 or Depth Anything v2 work best
- **Adjust depth_edge_threshold**:
  - Lower (0.05-0.08) for subtle depth changes
  - Higher (0.15-0.25) for noisy depth maps
- **For outdoor scenes**: Works well even without strong architectural features
- **For indoor scenes**: Excellent with depth - detects walls, furniture edges clearly

### For RGB-Based Estimation
- **For architecture/buildings**: Default settings work well
- **For outdoor landscapes**: Reduce line_threshold to 50-70
- **For noisy images**: Increase edge_threshold_low to 70-100
- **For subtle edges**: Decrease edge_threshold_high to 100-120

### General Recommendations
- **Use depth-based method whenever possible** - it's significantly more robust
- Images with clear geometric features (buildings, roads) work best for both methods
- For organic scenes (forests, clouds), depth-based method has better fallback behavior

## Limitations

### Depth-Based Method
- Requires depth estimation preprocessing (adds computational cost)
- Accuracy depends on depth map quality
- Very noisy depth maps (from poor lighting) may produce unreliable results
- Still assumes pinhole camera model (no fisheye correction)

### RGB-Based Method
- **FOV estimation** requires clear converging lines (buildings, roads, railroad tracks)
- **Tilt estimation** requires visible horizons
- Sensitive to texture, lighting, and shadows
- May struggle with:
  - Very cluttered scenes with few clear lines
  - Organic/natural scenes without geometric features
  - Low contrast images

### Both Methods
- Assume linear perspective (pinhole camera model)
- Not designed for extreme wide-angle or fisheye distortion
- Accuracy degrades with severe lens distortion

## Technical Details

- **Computer Vision**: Uses OpenCV for all image processing operations
- **Depth Processing** (Depth-based node):
  - Sobel gradient computation for depth discontinuities
  - Bilateral filtering for edge-preserving smoothing
  - Depth gradient analysis for fallback tilt estimation
  - Handles various depth map formats (1-channel, 3-channel, normalized/unnormalized)
- **Edge Detection**:
  - RGB: Canny edge detection with configurable thresholds
  - Depth: Gradient-based depth discontinuity detection
- **Line Detection**: Hough line transform (both standard and probabilistic)
- **FOV Estimation**:
  - RANSAC-like clustering for robust vanishing point detection
  - Pinhole camera model: `focal_length ≈ distance(principal_point, vanishing_point)`
  - FOV calculation: `hfov = 2 × arctan(width / (2 × f))`
  - Intelligent fallbacks based on aspect ratio
- **Tilt Estimation**:
  - Horizon line detection from horizontal edges
  - Position analysis relative to frame center
  - Vertical FOV conversion: `vfov = 2 × arctan(tan(hfov/2) / aspect_ratio)`
  - Median-based robust estimation resistant to outliers
  - Depth gradient analysis for scenes without clear horizons

## Recommended Depth Estimation Nodes

For best results with the depth-based estimator, use these ComfyUI depth estimation nodes:

- **MiDaS** (v3.0, v3.1) - Good general-purpose depth estimation
- **Depth Anything** (v1, v2) - State-of-the-art depth estimation, recommended
- **ZoeDepth** - Metric depth estimation
- **LeReS** - High-quality depth for indoor scenes

Install these through ComfyUI Manager or manually from their respective repositories.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
