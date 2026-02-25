# ComfyUI-DreamCube

**360° Panoramic Depth Estimation with Multi-plane Synchronization for ComfyUI**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen)](https://github.com/comfyanonymous/ComfyUI)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

A ComfyUI custom node pack implementing [DreamCube](https://github.com/yukun-huang/DreamCube)'s multi-plane synchronization framework for consistent depth estimation on 360° panoramic images.

## 🌟 Features

- **📐 Projection Conversion**: Seamless equirectangular ↔ cubemap transformations
- **🎯 Depth Estimation**: Compatible with any ComfyUI depth node (Depth Anything, DA3, MiDaS, Marigold)
- **🔄 Multi-plane Synchronization**: Cross-face consistency for depth maps
- **✨ Boundary Blending**: Eliminates visible seams at cubemap edges
- **🪟 Windows Compatible**: Pure Python with no platform-specific dependencies
- **⚡ GPU Accelerated**: Optimized with PyTorch and vectorized operations

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "DreamCube"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/cedarconnor/ComfyUI-DreamCube.git
cd ComfyUI-DreamCube
pip install -r requirements.txt
```

Then restart ComfyUI.

### Method 3: Development Mode

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/cedarconnor/ComfyUI-DreamCube.git
cd ComfyUI-DreamCube
pip install -e .
```

---

## 🚀 Quick Start

### Basic Workflow: Equirect → Depth → Equirect

```
[Load Image] (360° panorama)
    ↓
[Equirect to Cubemap]
    ↓
[Extract Face: Front] → [Depth Anything] ┐
[Extract Face: Back]  → [Depth Anything] ├→ [Batch Cubemap Depth]
[Extract Face: Left]  → [Depth Anything] │         ↓
[Extract Face: Right] → [Depth Anything] │   [Cubemap to Equirect]
[Extract Face: Top]   → [Depth Anything] │         ↓
[Extract Face: Bottom]→ [Depth Anything] ┘    [Save Image]
```

---

## 📚 Node Reference

### Projection Nodes

#### `Equirect to Cubemap`
Convert 360° equirectangular panorama to 6-face cubemap.

**Inputs:**
- `image` (IMAGE): Equirectangular input (2:1 aspect ratio)
- `cube_resolution` (INT): Resolution per face (256-4096)

**Outputs:**
- `CUBEMAP`: 6-face cubemap data structure

---

#### `Cubemap to Equirect`
Convert cubemap back to equirectangular format.

**Inputs:**
- `cubemap` (CUBEMAP): Input cubemap
- `output_width` (INT): Output width (512-8192)
- `output_height` (INT): Output height (256-4096)
- `output_type` (ENUM): `rgb`, `depth`, or `rgbd`

**Outputs:**
- `IMAGE`: Equirectangular panorama

---

#### `Extract Cubemap Face`
Extract single face as IMAGE for processing.

**Inputs:**
- `cubemap` (CUBEMAP): Source cubemap
- `face` (ENUM): Face to extract (`front`, `back`, `left`, `right`, `top`, `bottom`)

**Outputs:**
- `IMAGE`: Extracted face as standard image

---

#### `Insert Cubemap Face`
Insert/update a face in cubemap.

**Inputs:**
- `cubemap` (CUBEMAP): Target cubemap
- `image` (IMAGE): Face image to insert
- `face` (ENUM): Face to update

**Outputs:**
- `CUBEMAP`: Updated cubemap

---

### Depth Processing Nodes

#### `Apply Depth to Cubemap Face`
Apply depth map to single cubemap face.

**Inputs:**
- `cubemap` (CUBEMAP): Target cubemap
- `depth_map` (IMAGE): Depth from any depth node
- `face` (ENUM): Face to apply depth to

**Outputs:**
- `CUBEMAP`: Cubemap with depth applied

---

#### `Batch Cubemap Depth`
Apply depth maps to all 6 faces at once.

**Inputs:**
- `cubemap_rgb` (CUBEMAP): RGB cubemap
- `depth_front/back/left/right/top/bottom` (IMAGE): Depth for each face
- `enforce_consistency` (BOOL): Enable boundary blending (default: True)
- `normalization` (ENUM): `global`, `per_face`, or `adaptive`

**Outputs:**
- `CUBEMAP`: Cubemap with depth and consistency

---

#### `Merge Cubemap Depth`
Combine RGB and depth cubemaps into RGBD.

**Inputs:**
- `cubemap_rgb` (CUBEMAP): RGB data
- `cubemap_depth` (CUBEMAP): Depth data

**Outputs:**
- `CUBEMAP`: Merged RGBD cubemap

---

#### `Extract Depth Channel`
Extract depth as separate cubemap for visualization.

**Inputs:**
- `cubemap` (CUBEMAP): Source cubemap with depth

**Outputs:**
- `CUBEMAP`: Depth as RGB cubemap

---

#### `Normalize Cubemap Depth`
Normalize depth values across faces.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap with depth
- `method` (ENUM): `global`, `per_face`, or `align_scales`

**Outputs:**
- `CUBEMAP`: Normalized cubemap

---

### Utility Nodes

#### `Cubemap Preview`
Visualize all 6 faces in various layouts.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap to preview
- `layout` (ENUM): `horizontal`, `cross`, `vertical`, or `grid`
- `show_depth` (BOOL): Show depth instead of RGB

**Outputs:**
- `IMAGE`: Preview visualization

---

#### `Validate Cubemap Seams`
Check depth continuity at face boundaries.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap with depth
- `threshold` (FLOAT): Max acceptable error (0.0-1.0)

**Outputs:**
- `is_valid` (BOOL): Whether seams are acceptable
- `max_error` (FLOAT): Maximum seam error
- `report` (STRING): Detailed validation report

---

#### `Cubemap Info`
Display cubemap properties and statistics.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap to inspect

**Outputs:**
- `info` (STRING): Information text

---

#### `Enforce Depth Consistency`
Manually apply boundary blending.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap with depth
- `boundary_width` (INT): Blending region width (4-64)
- `iterations` (INT): Number of smoothing passes (1-10)

**Outputs:**
- `CUBEMAP`: Smoothed cubemap

---

#### `Smooth Cubemap Depth`
Apply Gaussian smoothing to reduce noise.

**Inputs:**
- `cubemap` (CUBEMAP): Cubemap with depth
- `sigma` (FLOAT): Gaussian kernel sigma (0.1-5.0)

**Outputs:**
- `CUBEMAP`: Smoothed cubemap

---

#### `Create Empty Cubemap`
Create empty cubemap for manual workflows.

**Inputs:**
- `resolution` (INT): Face resolution (256-4096)

**Outputs:**
- `CUBEMAP`: Empty cubemap

---

## 🎨 Example Workflows

### 1. Basic Depth Estimation

Load 360° image → Equirect to Cubemap → Extract 6 faces → Apply Depth Anything to each → Batch Cubemap Depth → Cubemap to Equirect → Save
Sample JSON prompts:
- `examples/workflows/basic_projection.json` – minimal RGB round-trip plus preview save
- `examples/workflows/depth_batch_example.json` – apply precomputed per-face depth maps, blend seams, and export depth

### 2. High Quality with Consistency

Same as above, but:
- Enable `enforce_consistency` in Batch Cubemap Depth
- Add `Enforce Depth Consistency` node with `boundary_width=24`
- Use `Validate Cubemap Seams` to check quality

### 3. Depth Visualization

Load 360° → Equirect to Cubemap → Process depth → Extract Depth Channel → Cubemap Preview (cross layout) → Save

---

## 🔧 Advanced Usage

### Custom Depth Models

Any ComfyUI depth node that outputs `IMAGE` type can be used:
- ✅ Depth Anything V2
- ✅ Depth Anything V1
- ✅ DA3 (Depth Anything 3)
- ✅ MiDaS
- ✅ Marigold
- ✅ ZoeDepth
- ✅ Your custom depth model

### Manual Face Processing

For fine control:
1. Create Empty Cubemap
2. Extract each face
3. Process individually (depth, upscale, enhance)
4. Insert back into cubemap
5. Enforce consistency
6. Convert to equirect

### Batch Processing

Process multiple panoramas:
- Use Loop nodes (if available)
- Process faces in parallel
- Cache intermediate results

---

## ⚙️ Configuration

### Performance Settings

**Memory Management:**
- 1024² faces: ~4GB VRAM
- 2048² faces: ~12GB VRAM
- 4096² faces: ~40GB VRAM

**Speed Optimization:**
- Use `global` normalization for speed
- Reduce `boundary_width` for faster blending
- Lower `iterations` for consistency enforcement

### Quality Settings

**High Quality:**
- `cube_resolution` = 2048
- `enforce_consistency` = True
- `boundary_width` = 24
- `iterations` = 3

**Balanced:**
- `cube_resolution` = 1024
- `enforce_consistency` = True
- `boundary_width` = 16
- `iterations` = 2

**Fast:**
- `cube_resolution` = 512
- `enforce_consistency` = True
- `boundary_width` = 8
- `iterations` = 1

---

## 🐛 Troubleshooting

### Issue: "Invalid aspect ratio" error

**Solution**: Equirectangular images must be 2:1 ratio (e.g., 2048×1024). Resize your image first.

### Issue: Visible seams in output

**Solutions**:
1. Enable `enforce_consistency` in Batch Cubemap Depth
2. Increase `boundary_width` (try 24-32)
3. Add `Enforce Depth Consistency` node
4. Use `Smooth Cubemap Depth` with sigma=1.5
5. Check depth maps are consistent (use Validate Cubemap Seams)

### Issue: Out of memory

**Solutions**:
1. Reduce `cube_resolution` (try 512 or 768)
2. Process faces sequentially instead of batch
3. Close other applications
4. Use CPU fallback (slower but no VRAM limit)

### Issue: Depth maps look wrong

**Solutions**:
1. Check input images are correct faces
2. Try different `normalization` methods
3. Use `Normalize Cubemap Depth` node
4. Verify depth node is working correctly (test on single image)

---

## 📖 Technical Details

### Coordinate Systems

**Equirectangular:**
- Longitude: -180° to +180° (left to right)
- Latitude: +90° to -90° (top to bottom)
- Aspect ratio: 2:1

**Cubemap:**
- 6 faces: front, back, left, right, top, bottom
- Each face: square (N×N pixels)
- Coordinate system: Right-handed, Z-forward

### Face Adjacency

```
         [top]
    [left][front][right][back]
        [bottom]
```

### Depth Consistency

Boundary blending uses weighted average:
- Weight = 1.0 at face center
- Weight = 0.5 at boundary
- Linear interpolation in between

### Performance Benchmarks

| Operation | 1024² | 2048² | Hardware |
|-----------|-------|-------|----------|
| Equirect→Cubemap | 80ms | 250ms | RTX 3060 |
| Cubemap→Equirect | 75ms | 240ms | RTX 3060 |
| Depth Consistency | 120ms | 450ms | RTX 3060 |
| Full Pipeline | ~500ms | ~2000ms | RTX 3060 |

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This project is based on:
- **DreamCube** (ICCV 2025) by Yukun Huang, Yanning Zhou, Jianan Wang, Kaiyi Huang, Xihui Liu
- Paper: [arXiv:2506.17206](https://arxiv.org/abs/2506.17206)
- Code: [github.com/yukun-huang/DreamCube](https://github.com/yukun-huang/DreamCube)

Special thanks to:
- ComfyUI developers for the extensible framework
- Depth Anything team for excellent depth estimation models
- The open-source computer vision community

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/cedarconnor/ComfyUI-DreamCube/issues)
- **Discussions**: [GitHub Discussions](https://github.com/cedarconnor/ComfyUI-DreamCube/discussions)
- **ComfyUI Discord**: #custom-nodes channel

---

## 🗺️ Roadmap

### v1.1.0 (Planned)
- [ ] Video support with temporal consistency
- [ ] Normal map generation from depth
- [ ] 3D mesh export (OBJ, PLY, GLTF)
- [ ] LoRA integration for style-specific depth
- [ ] Outpainting from partial FOV to 360°

### v1.2.0 (Future)
- [ ] Multi-resolution processing
- [ ] Depth refinement with diffusion
- [ ] 3D Gaussian Splatting integration
- [ ] Real-time preview mode
- [ ] Batch video processing

---

## 📊 Citation

If you use this node pack in your research or project, please cite:

```bibtex
@inproceedings{huang2025dreamcube,
  title={DreamCube: 3D Panorama Generation via Multi-plane Synchronization},
  author={Huang, Yukun and Zhou, Yanning and Wang, Jianan and Huang, Kaiyi and Liu, Xihui},
  booktitle={ICCV},
  year={2025}
}
```

---

**Made with ❤️ for the ComfyUI community**
