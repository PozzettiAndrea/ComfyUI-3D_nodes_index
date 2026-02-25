----------
Work in Progress! This node is not finished.
----------

# ComfyUI-HunyuanX

**Hunyuan 3D 2.1 generation package for ComfyUI**

Integrates Tencent's Hunyuan 3D 2.1 for image-to-3D generation with PBR texturing, featuring both standard and modular pipelines.

## Features

### 3D Generation
- **Hunyuan 3D 2.1**: Image-to-3D with PBR texturing, model caching (5-10x speedup)
- **Standard Pipeline**: Quick generation with all-in-one nodes
- **Modular Pipeline**: Memory-efficient split DiT/VAE loading (andrea_nodes)

### Texture Generation
- **PBR Multiview**: Albedo + metallic-roughness textures
- **Conditioning Maps**: Normal/position map rendering
- **Inpainting**: Fill UV texture holes
- **Baking**: Multi-view texture baking

### Mesh Operations
- **Post-Processing**: Built-in mesh cleaning and optimization
- **UV Unwrapping**: Custom Hunyuan UV unwrapper
- **Export**: GLB, OBJ, STL, PLY, 3MF, DAE, FBX

### Interpolation
- **Latent Blending**: Hunyuan3D latents, DINO embeddings
- **SLERP/LERP**: Smooth transitions between meshes/images

## Installation

### Quick Install
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/YOUR_USERNAME/ComfyUI-HunyuanX
cd ComfyUI-HunyuanX
pip install -r requirements.txt
```

### Via ComfyUI-Manager
1. Open ComfyUI Manager
2. Search for "ComfyUI-HunyuanX"
3. Click Install

**Requirements**: Python 3.10+, PyTorch 2.5-2.8, NVIDIA GPU with CUDA (recommended 24GB+ VRAM)

---

## All Nodes (~24 total)

### Hunyuan 3D 2.1 - Standard Pipeline (13 nodes)

**Model Loaders**
| Node | Purpose |
|------|---------|
| `HunyuanX_VAELoader` | Load Hunyuan VAE model |
| `HunyuanX_CameraConfig` | Configure camera parameters |

**Input Nodes**
| Node | Purpose |
|------|---------|
| `HunyuanX_LoadImageWithTransparency` | Load RGBA image |
| `HunyuanX_ImageWithAlphaInput` | Direct RGBA input |

**Core Pipeline**
| Node | Purpose |
|------|---------|
| `HunyuanX_MeshGenerator` | Generate 3D mesh from image (DiT Flow Matching) |
| `HunyuanX_VAEDecode` | Decode latents to mesh |
| `HunyuanX_PostprocessMesh` | Clean and optimize mesh |

**Texture Generation**
| Node | Purpose |
|------|---------|
| `HunyuanX_MultiViewsGenerator` | Generate multi-view textures |
| `HunyuanX_BakeMultiViews` | Bake textures onto mesh |
| `HunyuanX_InPaint` | Inpaint/complete textures |

**Mesh Operations**
| Node | Purpose |
|------|---------|
| `HunyuanX_MeshUVWrap` | UV unwrap mesh |
| `HunyuanX_LoadMesh` | Load mesh from file |
| `HunyuanX_ExportMesh` | Export to various formats |

---

### Hunyuan 3D 2.1 - Modular Pipeline (9 nodes)

For fine-grained control over the generation process:

**Image Preprocessing**
| Node | Purpose |
|------|---------|
| `HunyuanX_PrepareImageForDINO` | Preprocess images for DINO encoder |

**Model Loaders**
| Node | Purpose |
|------|---------|
| `HunyuanX_LoadDinoModel` | Load DINO v2 vision encoder |
| `HunyuanX_LoadDiT` | Load Hunyuan DiT (diffusion transformer) |
| `HunyuanX_LoadVAE` | Load Hunyuan VAE |

**Modular Pipeline**
| Node | Purpose |
|------|---------|
| `HunyuanX_EncodeDINO` | Encode image to DINO embeddings |
| `HunyuanX_GenerateLatents` | Generate mesh latents from embeddings |
| `HunyuanX_DecodeLatents` | Decode latents to mesh |
| `HunyuanX_ImageToLatents` | All-in-one convenience node |

**Visualization**
| Node | Purpose |
|------|---------|
| `HunyuanX_PreviewTrimesh` | Interactive 3D mesh preview |

---

### Texture Generation / Rendering (~2 nodes)

| Node | Purpose |
|------|---------|
| `LoadHunyuanMultiViewModel` | Load Hunyuan multi-view diffusion model |
| Additional texture generation nodes... |

---

## Key Features

### ✅ Model Caching
- **5-10x faster reloads**: Models stay in memory between generations
- **Smart memory management**: Only loads models when needed

### ✅ Lazy Loading
- **Faster startup**: Models load on first use, not at ComfyUI startup
- **Lower memory footprint**: Only loaded models consume memory

### ✅ Granular Pipelines
- **Standard pipeline**: Simple all-in-one nodes for quick generation
- **Modular pipeline**: Split DiT/VAE loading for research and fine control
- **Memory efficient**: Load only the components you need

---

## Example Workflows

Workflows are included in the `workflows/` directory:
- `hunyuan-i2m.json` - Hunyuan image-to-3D with texture generation

These workflows are automatically copied to ComfyUI's workflow directory on first run.

---

## Documentation

- **Installation Guide**: See above
- **Requirements**: See `requirements.txt`
- **Testing**: See `tests/README.md`

---

## System Requirements

### Minimum
- **GPU**: NVIDIA with 16GB+ VRAM
- **RAM**: 32GB+
- **Python**: 3.10+
- **PyTorch**: 2.5.0 - 2.8.0
- **CUDA**: 12.x

### Recommended
- **GPU**: NVIDIA with 24GB+ VRAM (A5000, RTX 4090, A6000)
- **RAM**: 64GB+
- **Storage**: 50GB+ for models

---

## Dependencies

### Core (Required)
- PyTorch 2.5.0-2.8.0
- trimesh, pymeshlab, pygltflib, xatlas
- transformers, diffusers, timm, einops
- opencv-python, Pillow, rembg

### Optional
- **Kaolin**: For advanced mesh operations (auto-installs)
- **flash-attn**: 10-20% faster inference (auto-installs)
- **spconv**: For sparse convolutions (auto-installs)
- **Blender**: For RGB multiview rendering

All dependencies are automatically installed by `install.py`.

---

## License

- **Hunyuan 3D 2.1**: Tencent License
- **HunyuanX code**: MIT License

---

## Contributing

Issues and PRs welcome at: https://github.com/YOUR_USERNAME/ComfyUI-HunyuanX

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-HunyuanX/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## Credits

- Tencent Hunyuan Team for Hunyuan 3D 2.1
- ComfyUI community
