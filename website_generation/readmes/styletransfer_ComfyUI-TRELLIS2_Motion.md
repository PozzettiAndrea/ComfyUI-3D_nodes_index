# ComfyUI-TRELLIS2_Motion

A comprehensive ComfyUI node package that uses Microsoft's TRELLIS2 to transform video footage into 3D mesh reconstructions with advanced rendering effects.

![TRELLIS2 Motion](https://img.shields.io/badge/ComfyUI-Custom_Nodes-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![CUDA](https://img.shields.io/badge/CUDA-Required-red)

## Features

- **Image to 3D Mesh**: Convert single images to high-quality 3D meshes with PBR materials
- **Video Processing**: Batch process video frames through TRELLIS2
- **Multiple Rendering Modes**: PBR, wireframe, cel/toon shading, normal map, depth map
- **Onion Skinning**: Motion ghosting effect with configurable interval (every 5, 10, 30 frames)
- **Camera Control**: Orbit, dolly, pan trajectories with animation support
- **Lighting Presets**: Studio, outdoor, dramatic, flat lighting configurations
- **Post-Processing**: Bloom, depth of field, motion blur, outlines
- **Progress Bars**: Visual feedback on all long-running operations
- **Auto Model Download**: Automatically downloads TRELLIS2 model (~8GB) on first use

## Nodes

| Node | Description |
|------|-------------|
| **Trellis2Predict** | Convert single image to 3D mesh with PBR materials |
| **VideoToMeshes** | Batch process video frames through TRELLIS2 |
| **CameraTrajectory** | Define camera movement (orbit, dolly, pan, static) |
| **MultiAngleCamera** | Generate multiple viewing angles for grid preview |
| **MeshRenderer** | Render mesh from camera viewpoint with effects |
| **MeshSequenceRenderer** | Render video sequence with consistent camera |
| **OnionSkinning** | Add motion ghosting effect to rendered frames |
| **RenderingEffects** | Apply bloom, DoF, cel shading, outlines |
| **Trellis2VideoAngleShift** | All-in-one convenience node |

## Installation

### 1. Clone the Repository

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-TRELLIS2_Motion.git
cd ComfyUI-TRELLIS2_Motion
```

### 2. Install Dependencies

```bash
python install.py
```

### 3. Install TRELLIS2 (Required)

```bash
pip install git+https://github.com/microsoft/TRELLIS.git
```

### 4. Install nvdiffrast (Required for Rendering)

```bash
pip install git+https://github.com/NVlabs/nvdiffrast.git
```

### 5. Restart ComfyUI

The nodes will appear under the `TRELLIS2` category.

## Requirements

- **Python**: 3.10+
- **CUDA**: Required (tested on CUDA 11.8+)
- **GPU**: NVIDIA GPU with 24GB+ VRAM recommended (A100, RTX 4090)
- **ComfyUI**: Latest version

## Workflows

Pre-built workflows are included in the `workflows/` folder:

| Workflow | Description |
|----------|-------------|
| `single_image_novel_view.json` | Basic image to 3D with camera control |
| `video_angle_shift.json` | Full video processing pipeline |
| `onion_skinning_demo.json` | Motion ghosting showcase |
| `effects_showcase.json` | Cel shading and post-processing demo |
| `multiview_preview.json` | 8-angle grid preview |

## Usage Examples

### Single Image Novel View

```
LoadImage → Trellis2Predict → MeshRenderer → SaveImage
                                    ↑
                           CameraTrajectory
```

### Video Angle Shift

```
VHS_LoadVideo → VideoToMeshes → MeshSequenceRenderer → VHS_VideoCombine
                                        ↑
                               CameraTrajectory
```

### With Onion Skinning

```
VHS_LoadVideo → VideoToMeshes → MeshSequenceRenderer → OnionSkinning → VHS_VideoCombine
```

## Onion Skinning Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `ghost_count` | Number of ghost frames | 3 |
| `frame_interval` | Frames between ghosts | 5 |
| `ghost_opacity` | Base opacity of ghosts | 0.3 |
| `opacity_falloff` | linear, exponential, constant | linear |
| `ghost_color_mode` | original, tinted, silhouette | tinted |
| `past_tint` | Color for past frames | Blue (#0066FF) |
| `future_tint` | Color for future frames | Orange (#FF6600) |

## Rendering Modes

- **PBR**: Full physically-based rendering with materials
- **Wireframe**: Edge visualization
- **Cel/Toon**: Quantized shading with outlines
- **Normal**: RGB-encoded surface normals
- **Depth**: Grayscale depth visualization

## Lighting Presets

- **Studio**: Professional 3-point lighting
- **Outdoor**: HDR sky with sun
- **Dramatic**: High contrast single light
- **Flat**: Even lighting for cel shading

## Performance

| Resolution | TRELLIS2 Time | Render Time | Total/Frame |
|------------|---------------|-------------|-------------|
| 512x512 | ~3s | ~0.1s | ~3.1s |
| 1024x1024 | ~10s | ~0.2s | ~10.2s |

*Tested on NVIDIA A100 80GB*

## Comparison with SHARP

| Aspect | TRELLIS2 | SHARP |
|--------|----------|-------|
| Output | PBR Mesh + Materials | Gaussian Splats |
| Processing Time | 3-60s per frame | <1s per frame |
| Materials | Full PBR | SH coefficients |
| Rendering | nvdiffrast | gsplat |
| Quality | Higher fidelity meshes | Real-time splatting |

## Troubleshooting

### "CUDA out of memory"
- Reduce resolution from 1024 to 512
- Increase frame_skip to process fewer frames
- Use a GPU with more VRAM

### "nvdiffrast not found"
```bash
pip install git+https://github.com/NVlabs/nvdiffrast.git
```

### "TRELLIS not found"
```bash
pip install git+https://github.com/microsoft/TRELLIS.git
```

## Credits

- [Microsoft TRELLIS](https://github.com/microsoft/TRELLIS) - Core 3D reconstruction model
- [nvdiffrast](https://github.com/NVlabs/nvdiffrast) - CUDA mesh rendering
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based UI framework

## License

MIT License - See LICENSE file for details.
