# ComfyUI-PanoTools - Panorama Generation Tools

Professional panorama generation tools for ComfyUI. Converts perspective images/video to equirectangular 360° panoramas with automatic camera calibration. Supports multiple output resolutions (3840×1920, 4096×2048, 5760×2880, 7680×3840) and accepts any reasonable aspect ratio (portrait to landscape, 1:2 to 2:1).

> **Credits:** Based on the [original perspective-to-panorama method](https://old.reddit.com/r/StableDiffusion/comments/1p4nax9/a_method_to_turn_a_video_into_a_360_3d_vr/) by [hybridworkflow](https://www.patreon.com/cw/hybridworkflow).

> **Note:** Includes [GeoCalib](https://github.com/cvg/GeoCalib) (ECCV 2024) by ETH Zurich under Apache-2.0 license. See [NOTICE](NOTICE) and [LICENSE-GeoCalib](LICENSE-GeoCalib).

## Features

- **Flexible Input**: Accepts any aspect ratio between 1:2 (portrait) and 2:1 (landscape)
- **Configurable Output**: Choose from 4 resolutions (3840×1920, 4096×2048, 5760×2880, 7680×3840) to balance quality, memory usage, and processing speed
- **Automatic Calibration**: AI-based (GeoCalib), horizon detection, or vertical line detection. Caution: Horizon and vertical detection mostly untested.
- **Manual Control**: Fine-tune roll, pitch, and vFoV parameters

## Installation

**Via ComfyUI Manager (Coming soon):**
1. Search for "PanoTools"
2. Install

**Via Git:**
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/9nate-drake/ComfyUI-PanoTools.git
```

**Dependencies:**
```bash
pip install -r requirements.txt
```

Required: `torch`, `torchvision`, `opencv-python`, `kornia`, `matplotlib`, `numpy`

**GeoCalib**: Bundled with the package. Model weights (~110-220 MB) download automatically on first use.

## Usage

### Node Locations

**Camera Calibration**: `Add Node > PanoTools > Camera Calibration`
**Perspective to Panorama**: `Add Node > PanoTools > Perspective to Panorama`

## Camera Calibration Node

Estimates camera parameters (roll, pitch, vFoV) from a single image.

### Calibration Methods

| Method | Best For | Technology |
|--------|----------|------------|
| **GeoCalib Auto**  | Any scene, most accurate | Deep learning (ECCV 2024) |
| **Horizon Detection** | Outdoor scenes with visible horizon | Edge detection + Hough transform |
| **Vertical Lines** | Architectural/urban scenes | Edge detection + Hough transform |
| **Manual** | Known camera parameters | Direct input |

### Inputs

- **image** (IMAGE): Single image or first frame to analyze
- **calibration_method**: Choose method (geocalib_auto recommended, horizon_detection, vertical_lines, manual)
  - **geocalib_auto** : AI-based, works for all scenes (recommended)
  - **horizon_detection**: For outdoor/ocean scenes with visible horizon
  - **vertical_lines**: For architecture/buildings with vertical structures
  - **manual**: Specify values manually
- **manual_roll/pitch/vfov** (optional): Manual override values (only used when method is 'manual')
- **horizon_roi_top/bottom** (optional): Region of interest for horizon detection
- **min_line_length/angle_threshold** (optional): Parameters for vertical line detection

### Outputs

1. **roll** (FLOAT): Camera roll in degrees
2. **pitch** (FLOAT): Camera pitch in degrees
3. **vfov** (FLOAT): Vertical field of view in degrees
4. **focal_length** (FLOAT): Focal length in pixels
5. **focal_length_mm** (FLOAT): 35mm equivalent focal length (e.g., 24mm, 50mm)
6. **calibration_info** (STRING): Diagnostic information

## Perspective to Panorama Node

Converts perspective images/video to 360° equirectangular panoramas.

### Inputs

- **images** (IMAGE): Input frames (any aspect ratio from 1:2 portrait to 2:1 landscape)
- **output_resolution** (DROPDOWN): Output panorama resolution (default: 5760×2880)
  - **3840×1920**: Lower quality, faster processing, less VRAM
  - **4096×2048**: Medium-low quality, good for quick previews
  - **5760×2880**: Balanced quality/performance (recommended)
  - **7680×3840**: Highest quality, requires more VRAM and processing time
- **interpolation** (DROPDOWN): Interpolation method (default: lanczos)
  - **lanczos** : Best quality, sharpest edges, reduces jagged artifacts (recommended)
  - **cubic**: High quality, smooth results, faster than lanczos
  - **bilinear**: Basic quality, fastest processing
- **roll** (FLOAT): Camera roll in degrees (tilt left/right, default: 0.53)
- **pitch** (FLOAT): Camera pitch in degrees (tilt up/down, default: -9.47)
- **vfov** (FLOAT): Vertical field of view in degrees (default: 52.14)
  - Typical values: 40-60° (standard lens), 70-90° (wide angle), 10-30° (telephoto)
- **focal_length** (FLOAT): Focal length in pixels (0 = auto-calculate from vfov)

### Outputs

1. **panorama** (IMAGE): Equirectangular panorama at selected resolution
2. **mask_single** (IMAGE): Valid projection area mask (white=valid, black=invalid)
3. **info** (STRING): Processing information

## Example Workflow

Example workflows available in the /workflows folder.

**Automatic Calibration (Recommended):**

```
[Load Video] → [Get Frame 0] → [Camera Calibration (Auto)] → roll/pitch/vfov
                                                                      ↓
[Load Video] ────────────────────→ [Perspective to Panorama] ← ──────┘
                                              ↓
                                        [Save Image]
```

1. Load video/images
2. Extract one frame for calibration
3. Run Camera Calibration (use `geocalib_auto` for best results)
4. Connect calibration outputs to Perspective to Panorama node
5. Process all frames


## Troubleshooting

**Node doesn't appear:**
- Restart ComfyUI
- Check for Python errors in console

**"ERROR: Input must be between portrait(1:2) and landscape(2:1)":**
- Input aspect ratio too extreme (must be 0.5 ≤ width/height ≤ 2.0)

**Panorama rotated/off-center:**
- Use Camera Calibration node for automatic detection
- Manually adjust roll (horizon level) and pitch (vertical centering)

**"ERROR: OpenCV not available" or "ERROR: GeoCalib failed to load":**
- Run: `pip install -r requirements.txt`
- Restart ComfyUI

**"WARNING: No horizon/lines detected":**
- Try `geocalib_auto` method instead
- Adjust detection parameters (ROI, min_line_length, angle_threshold)

**Jagged edges or aliasing artifacts in panorama:**
- Switch from `bilinear` to `cubic` or `lanczos` interpolation
- Lanczos provides the best quality but is slower
- Increase output resolution for better quality at FOV edges

## Technical Details

**Projection:** Reverse equirectangular projection using spherical coordinates and pinhole camera model
**Coordinate System:** X=Right, Y=Up, Z=Forward, ZYX Euler angles
**Interpolation:** OpenCV remap with configurable methods (Lanczos4, Cubic, Bilinear)
  - Lanczos4: 8×8 pixel kernel, sharp and artifact-free
  - Cubic: 4×4 pixel kernel, smooth and balanced
  - Bilinear: 2×2 pixel kernel, fast but basic
**Optimization:** Mask computed once per batch, vectorized NumPy operations, GPU-accelerated interpolation (if OpenCV built with CUDA)

## Version History

- **v1.0** Initial release

## Credits

**Original Method**: [hybridworkflow](https://www.patreon.com/cw/hybridworkflow) - [Reddit post](https://old.reddit.com/r/StableDiffusion/comments/1p4nax9/a_method_to_turn_a_video_into_a_360_3d_vr/)

**GeoCalib (ECCV 2024)**: ETH Zurich - [Paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05636.pdf) | [GitHub](https://github.com/cvg/GeoCalib) | [Demo](https://veichta-geocalib.hf.space/)

## Contributing

Contributions welcome! Submit pull requests or open issues for bugs and feature requests.
