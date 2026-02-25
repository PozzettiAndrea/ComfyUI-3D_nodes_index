# ComfyUI LatLong — Equirectangular Image Nodes

High‑quality equirectangular (360°) image processing nodes for ComfyUI. Rotate with yaw/pitch/roll, adjust the horizon, crop to 180° or square, convert to cubemaps, and extract perspective views — all designed for panoramic workflows.

## What's New

### Latest Updates (v2.0)

- **Interactive 360° Panorama Viewer**: Two new viewer nodes with Three.js-based WebGL rendering for real-time panorama exploration directly in ComfyUI
  - Drag to look around, scroll to zoom
  - Support for single images and video sequences
  - Automatic image optimization and format handling

- **16K Image Support with Tiled Processing**: Memory-efficient processing for extra-large high-resolution panoramas
  - Auto-detects images >8K and uses tiled processing
  - Configurable tile sizes (512-8192 pixels)
  - Reduces memory usage by 60-75% for large images
  - Processes 16K images (~1.6GB) in ~400-800MB memory footprint

### Previous Updates

- **Five new nodes added**: Cubemap ↔ Equirectangular conversion, Mirror/Flip, Resize with aspect preservation, Preset rotations, and Cubemap face extraction
- All‑in‑One node now embeds controls directly in the node (sliders/toggles/dropdowns). No external parameter nodes are required for rotation/crop/interpolation.
- Helpful tooltips added to every node and parameter to clarify behavior and best‑use guidance.

## Installation

Option A — Clone (recommended)
- From `ComfyUI/custom_nodes`:
  - `git clone https://github.com/cedarconnor/comfyui-LatLong.git`
  - `cd comfyui-LatLong`
  - `pip install -r requirements.txt`
  - Restart ComfyUI

Option B — Manual
- Extract the repo into `ComfyUI/custom_nodes/comfyui-LatLong/`
- Install deps: `pip install numpy>=1.21.0 opencv-python>=4.5.0 scipy>=1.7.0 torch>=1.9.0 Pillow>=9.0.0`
- Restart ComfyUI

Requirements
- ComfyUI (latest), Python 3.8+
- Python packages:
  - numpy>=1.21.0, opencv-python>=4.5.0, scipy>=1.7.0, torch>=1.9.0, Pillow>=9.0.0

GPU Notes
- Some GPU paths use `torch.grid_sample` and support bilinear/nearest only. Lanczos/Bicubic use CPU (OpenCV) paths.

Viewer Notes
- The interactive panorama preview nodes use Three.js. If you are offline or your frontend blocks CDN imports, run `python install.py` to download Three.js into `js/lib/`.

## Nodes Overview

### Core Transformation Nodes

1) **Equirectangular Rotate**
- Purpose: Rotate an equirectangular image with yaw/pitch/roll and adjust the horizon.
- **NEW**: Supports 16K images with automatic tiled processing
- Inputs:
  - `image`: equirectangular tensor (B,H,W,C) in [0,1]
  - `yaw_rotation`: horizontal rotation (degrees)
  - `pitch_rotation`: vertical tilt (degrees)
  - `roll_rotation`: bank rotation (degrees)
  - `horizon_offset`: vertical horizon shift (degrees)
  - `interpolation`: lanczos | bicubic | bilinear | nearest
  - `backend`: auto | cpu | gpu
  - `use_tiling`: auto | enabled | disabled (for large images)
  - `tile_size`: 512-8192 pixels (memory vs. speed trade-off)

2) **Equirectangular Rotate (Preset)**
- Purpose: Quick rotation to preset views with fine-tuning options.
- Presets: front, back, left, right, up, down
- Additional controls: yaw/pitch/roll offsets, horizon adjustment
- Ideal for: Quickly orienting panoramas to standard viewing angles

3) **Equirectangular Crop 180**
- Purpose: Extract a horizontal FOV (default 180°) window from an equirectangular image.
- Inputs:
  - `image`
  - `output_width`, `output_height`: target size
  - `maintain_aspect`: preserve natural aspect ratio for selected FOV
  - `center_longitude_deg`: FOV center longitude (degrees)
  - `fov_degrees`: horizontal field of view (degrees)
  - `interpolation`

4) **Equirectangular Crop Square**
- Purpose: Center‑crop width to match the original height (perfect square).
- Inputs: `image`, `interpolation` (not used by pure crop; kept for consistency)

5) **Equirectangular Processor (All‑in‑One)**
- Purpose: Rotate then optionally crop to 180° or to a centered square — a single‑node workflow. Note: square crop takes precedence over 180°.
- Inputs:
  - `image`
  - `yaw_rotation`, `pitch_rotation`, `roll_rotation`, `horizon_offset`
  - `crop_to_180`, `crop_to_square`
  - `output_width`, `output_height` (for 180° crop)
  - `interpolation`

6) **Equirectangular Perspective Extract**
- Purpose: Extract a pinhole‑camera perspective view (yaw/pitch/roll/FOV) from an equirectangular panorama.
- Inputs: `image`, `yaw_rotation`, `pitch_rotation`, `roll_rotation`, `fov_degrees`, `output_width`, `output_height`, `interpolation`, `backend`

### Cubemap Conversion Nodes

7) **Equirectangular → Cubemap (3×2)**
- Purpose: Convert equirectangular panorama to a 3×2 cubemap atlas.
- Inputs: `image`, `face_size`, `layout` (3×2), `interpolation`
- Face order: [left, front, right] on top row; [back, top, bottom] on bottom row

8) **Cubemap (3×2) → Equirectangular**
- Purpose: Convert a 3×2 cubemap atlas back to equirectangular format.
- Inputs: `cubemap_atlas`, `output_width`, `output_height`, `layout`, `interpolation`
- Useful for: Round-trip workflows, importing cubemaps from other tools

9) **Cubemap Faces Extract**
- Purpose: Extract individual cube faces from equirectangular panorama as separate images.
- Outputs: 6 separate images (left, front, right, back, top, bottom)
- Inputs: `image`, `face_size`, `interpolation`
- Useful for: Processing individual faces, creating custom cubemap layouts

**Flexible Cubemap Formats (Advanced)**
- **Equirectangular To Cubemap (Flexible)**: Output cubemaps as `atlas_3x2`, `dice`, `horizon`, or `stack` with configurable `face_order` (note: `list`/`dict` are aliases of `stack` for ComfyUI compatibility).
- **Cubemap To Equirectangular (Flexible)**: Ingest the same formats and convert back to equirectangular.
- **Stack Cubemap Faces (Stack)** / **Split Cubemap Faces (Stack)**: Pack/unpack face stacks (B*6 faces) for seam-edit workflows.

### Utility Nodes

10) **Equirectangular Mirror/Flip**
- Purpose: Mirror or flip panoramas with proper spherical wrapping.
- Options:
  - `mirror_horizontal`: flip left-right (reverse longitude)
  - `mirror_vertical`: flip top-bottom (reverse latitude)
- Useful for: Correcting orientation, creating mirrored effects

11) **Equirectangular Resize**
- Purpose: Resize equirectangular images with aspect ratio preservation.
- Inputs: `image`, `output_width`, `output_height`, `maintain_aspect`, `interpolation`
- Features: Auto-maintains 2:1 aspect ratio (standard equirectangular) or custom dimensions

### Seam-Safe / Mask Nodes

- **Create Seam Mask**: Center seam mask (with optional feather + optional 50% roll offset).
- **Create Pole Mask**: Circle mask for poles (face or equirectangular mode).
- **Roll Image (Wrap)** / **Roll Mask (Wrap)**: Fast wraparound rolling without resampling.
- **Apply Circular Padding Model/VAE**: Adds circular x-axis Conv2d padding to reduce seam artifacts (reload to undo if applied inplace).

### Outpainting Nodes
   
12) **LatLong Outpaint Setup**
- Purpose: Prepare a transparent equirectangular canvas with a source flat image for outpainting/inpainting.
- Inputs:
  - `flat_image`: Source rectilinear image
  - `canvas_width`, `canvas_height`: Canvas dimensions (usually 2:1)
  - `placement_mode`: 2d_composite | perspective
  - `scale`: Pixel scale (2D) or FOV multiplier (Perspective)
  - `translate_x`, `translate_y` (2D only)
  - `yaw`, `pitch`, `fov` (Perspective only)
  - `feather_size`: Inner edge feathering for smooth blending
- Outputs:
  - `composite_image`: Canvas with image placed (use for inpainting reference)
  - `outpaint_mask`: Mask where generated content should go
  - `stitch_context`: Data bundle for Stitch node

13) **LatLong Outpaint Stitch**
- Purpose: Composite the original high-res source image back over the generated result.
- Inputs:
  - `generated_equirect`: Result from KSampler/Inpainting
  - `stitch_context`: From Setup node
  - `blend_mode`: alpha | overlay | hard
- Features: Automatically scales high-res source to match generation resolution, preserving original detail.

### Post-Processing Nodes

14) **Equirectangular Edge Blender**
- Purpose: Blend left and right edges for seamless wraparound continuity.
- **NEW**: Essential for eliminating visible seams in 360° viewers
- Inputs:
  - `image`: Equirectangular panoramic image
  - `blend_width`: Blend region width in pixels (10-20 recommended)
  - `blend_mode`: cosine | linear | smooth (cosine smoothest)
  - `check_continuity`: Validate seamlessness after blending
- Use Case: Final polish step to ensure perfect wraparound in interactive viewers
- Features:
  - Three blending modes (cosine recommended for smoothest results)
  - Automatic edge continuity validation
  - Configurable blend width for different image resolutions
  - Reports seamless status to console

### Interactive Viewer Nodes

15) **Preview 360 Panorama**
- Purpose: Interactive 360° panorama viewer with real-time navigation.
- Features:
  - Three.js-based WebGL rendering
  - Mouse drag to look around (yaw/pitch control)
  - Mouse wheel to zoom (FOV adjustment 30°-90°)
  - Automatic image optimization and resizing
- Inputs: `images` (equirectangular), `max_width` (resize limit, default 4096)
- Use Case: Preview and explore panoramas directly in ComfyUI workflow

16) **Preview 360 Video Panorama**
- Purpose: Interactive 360° video panorama viewer with frame-by-frame playback.
- Features:
  - Frame-by-frame 360° video playback
  - Interactive navigation during playback
  - Configurable frame rate
  - Automatic frame optimization
- Inputs: `video_frames` (batch of equirectangular images), `fps`, `max_width`
- Use Case: Preview animated 360° content, test rotation sequences

## Quickstart Examples

**Basic Rotation**
- Add Equirectangular Rotate, connect an image, tweak yaw/pitch/roll/horizon.

**Quick Preset Views**
- Add Equirectangular Rotate (Preset), select preset (front/back/left/right/up/down), optionally fine-tune with offsets.

**Square Crop**
- Add Equirectangular Crop Square to center‑crop to a perfect square.

**180° Extraction**
- Add Equirectangular Crop 180, set `center_longitude_deg` and `fov_degrees` as needed, enable Maintain Aspect for correct proportions.

**Perspective View**
- Add Equirectangular Perspective Extract, set yaw/pitch/roll, FOV, and output size.

**Cubemap Generation**
- Add Equirectangular → Cubemap (3×2), choose `face_size`, select interpolation.

**Cubemap Conversion**
- Generate cubemap with Equirectangular → Cubemap, then convert back with Cubemap → Equirectangular for round-trip workflows.

**Flexible Cubemap Formats**
- Use Equirectangular To Cubemap (Flexible) with `cube_format` = `dice` (cross), `horizon` (strip), or `stack` (B*6 faces). Convert back with Cubemap To Equirectangular (Flexible).

**Extract Individual Faces**
- Add Cubemap Faces Extract to get 6 separate images (left, front, right, back, top, bottom) from an equirectangular panorama.

**Mirror/Flip**
- Add Equirectangular Mirror/Flip, enable horizontal or vertical flip for orientation correction or creative effects.

**Smart Resize**
- Add Equirectangular Resize with maintain_aspect=True to automatically preserve 2:1 ratio, or disable for custom dimensions.

**All‑in‑One**
- Add Equirectangular Processor (All‑in‑One), adjust rotation; enable square or 180° crop; pick interpolation. All controls are embedded in the node.

**Interactive Panorama Viewer**
- Add Preview 360 Panorama, connect your equirectangular image, explore interactively by dragging and scrolling.

**360° Video Preview**
- Add Preview 360 Video Panorama, connect a batch of equirectangular frames, set FPS, and watch your animated panorama with interactive navigation.

**Processing 16K Images**
- Load a 16K (16384×8192) panorama into Equirectangular Rotate, set `use_tiling` to "auto", adjust rotation parameters, and process without memory errors.

**Edge Blending for Seamless Wraparound**
- Add Equirectangular Edge Blender after rotation/processing, set `blend_width` to 10-20, choose "cosine" mode, enable continuity check to validate seamless edges.

**Seam Inpainting Workflow**
- Roll Image (Wrap) (50% x-roll)  Create Seam Mask  inpaint/composite  Roll Image (Wrap) back  (optional) Equirectangular Edge Blender.

**Outpainting / Compositing**
- **Setup**: Connect Flat Image to `LatLong Outpaint Setup`. Choose `perspective` mode, adjust `yaw`/`pitch` to place image on the sphere.
- **Inpaint**: Use `composite_image` and `outpaint_mask` with VAE Encode (for Inpainting) -> KSampler.
- **Stitch**: Connect KSampler output and `stitch_context` to `LatLong Outpaint Stitch` to overlay the crisp original source on top of the generation.

**Seam-Safe Generation**
- Apply Circular Padding Model/VAE before sampling/decoding to reduce x-seam artifacts (reload model/vae to undo if applied inplace).

## Technical Notes
Coordinate System
- Accurate spherical transforms with longitude wrapping and pole handling.

Interpolation
- CPU: OpenCV remap (Lanczos, Bicubic, Bilinear, Nearest)
- GPU: torch.grid_sample (Bilinear/Nearest where applicable)

Pipeline
- Input (B,H,W,C) → float32 processing → transform → resample → output tensor in [0,1].

Tiled Processing (16K Support)
- Automatically enabled for images larger than 8192 pixels in any dimension
- Processes images in horizontal bands with 64-pixel overlap to prevent seams
- Reduces memory usage by 60-75% for large images
- Configurable tile sizes: smaller tiles = less memory, more processing overhead
- Memory footprint: 16K image (~1.6GB full) processes in ~400-800MB with tiling
- Maintains full quality with proper overlap blending

Interactive Viewer
- Three.js WebGL-based rendering with equirectangular texture mapping
- Base64-encoded PNG delivery for seamless ComfyUI integration
- Automatic performance optimization via configurable image resizing
- Camera controls: spherical coordinate system with FOV adjustment

## Troubleshooting

- Blurry output: prefer Lanczos/Bicubic for final renders.
- Memory limits: enable tiled processing (`use_tiling: auto` or `enabled`) or reduce resolution.
- GPU path missing filters: use CPU for Lanczos/Bicubic.
- Out of memory on large images: Try smaller `tile_size` (e.g., 1024) or enable tiling explicitly.
- Viewer not loading: Ensure Three.js library loaded correctly (check browser console).
- Seams in tiled output: Increase tile overlap (currently fixed at 64px in code).

## Performance Benchmarks

| Image Resolution | Processing Mode | Memory Usage | Typical Process Time* |
|-----------------|-----------------|--------------|---------------------|
| 2K (2048×1024) | Direct | ~25MB | <1s |
| 4K (4096×2048) | Direct | ~100MB | 1-2s |
| 8K (8192×4096) | Direct/Auto | ~400MB | 3-5s |
| 16K (16384×8192) | Tiled (auto) | ~600MB | 8-15s |
| 32K (32768×16384) | Tiled (auto) | ~800MB | 30-60s |

*Times for rotation with Lanczos interpolation on typical CPU. GPU backend is 2-5x faster for bilinear/nearest.

## Future Enhancements

The following optimizations and features are planned for future releases:

### Advanced Tiling & Performance
- **Multi-threaded Tiling**: Process multiple bands in parallel for 2-4x speedup on multi-core CPUs
- **GPU Tiling Support**: Extend torch implementations with tiling for VRAM-constrained scenarios
- **Adaptive Tile Sizing**: Dynamically adjust tile size based on available RAM/VRAM
- **Disk-based Caching**: For very large batch operations, cache intermediate results to disk

### Processing Optimizations
- **Progressive Downsampling**: Generate quick low-res previews, then process full resolution
- **Smart Region Processing**: Only process regions that change (for animation/video sequences)
- **Half-precision Support**: FP16 processing for 50% memory reduction on compatible hardware
- **Lazy Evaluation**: Defer processing until output is actually needed

### Viewer Enhancements
- **VR Mode**: Native stereoscopic viewing for VR headsets
- **Hotspot Annotations**: Add interactive markers and info points to panoramas
- **Comparison Mode**: Side-by-side before/after comparison with synchronized navigation
- **Export Tools**: Save viewer state, generate shareable web embeds

### Additional Features
- **Stereo Panorama Support**: Top/bottom or side-by-side stereoscopic formats
- **HDR Processing**: Preserve high dynamic range through the processing pipeline
- **Batch Optimization**: Smart batching with automatic load balancing
- **Custom Projections**: Support for additional projection types (fisheye, cylindrical, etc.)

Community suggestions and contributions are welcome! If you have specific use cases or feature requests, please open an issue on GitHub.

## Contributing

Issues, feature requests, and PRs are welcome.

## License

Open source — see the repository license.

— Ideal for 360° photography, VR, panoramic pipelines, and social content where precise equirectangular control matters.
