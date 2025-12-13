# Awesome ComfyUI 3D

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated index of ComfyUI custom nodes for 3D generation, processing, and visualization.

## Categories

- [Image-to-3D](#image-to-3d)
- [Text-to-3D](#text-to-3d)
- [Multi-View Generation](#multi-view-generation)
- [Mesh Processing](#mesh-processing)
- [Texturing](#texturing)
- [Gaussian Splatting](#gaussian-splatting)
- [Rigging & Animation](#rigging--animation)
- [Depth & Normal](#depth--normal)
- [Visualization](#visualization)

---

## Image-to-3D

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Comprehensive suite: TripoSR, InstantMesh, CRM, LGM, Era3D, Wonder3D, Unique3D, StableFast3D, 3DGS, NeRF | `community` `image-to-3d` `glb` |
| [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper) | Kijai | Hunyuan3D 2.0 wrapper for high-quality image-to-3D mesh generation | `tencent` `hunyuan3d` `image-to-3d` |
| [Comfyui_Hunyuan3D_EX](https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX) | BIMer-99 | Simplified Hunyuan3D wrapper with streamlined workflow | `tencent` `hunyuan3d` |
| [ComfyUI-Flowty-TripoSR](https://github.com/flowtyone/ComfyUI-Flowty-TripoSR) | flowtyone | Standalone TripoSR implementation for fast image-to-3D | `stability` `triposr` `image-to-3d` |
| [ComfyUI-Flowty-CRM](https://github.com/flowtyone/ComfyUI-Flowty-CRM) | flowtyone | Convolutional Reconstruction Model for image-to-3D | `community` `crm` `image-to-3d` |
| [ComfyUI-TripoSG](https://github.com/fredconex/ComfyUI-TripoSG) | fredconex | TripoSG (Tripo Stable Gaussian) for high-quality 3D generation | `vast-ai` `triposg` `gaussian` |
| [ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS) | smthemex | Microsoft TRELLIS for structured latent 3D generation | `microsoft` `trellis` `image-to-3d` |
| [ComfyUI-IF_Trellis](https://github.com/if-ai/ComfyUI-IF_Trellis) | if-ai | Alternative TRELLIS wrapper with additional features | `microsoft` `trellis` |

## Text-to-3D

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-Tripo](https://github.com/VAST-AI-Research/ComfyUI-Tripo) | VAST-AI-Research | Official Tripo API integration for text/image-to-3D with rigging support | `vast-ai` `text-to-3d` `api` |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Text-to-3D via Score Distillation Sampling (SDS) with various models | `community` `text-to-3d` |

## Multi-View Generation

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Zero123++, Era3D, Wonder3D, SV3D for consistent multi-view image generation | `community` `multi-view` |
| [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper) | Kijai | Hunyuan3D multi-view diffusion for consistent view synthesis | `tencent` `multi-view` `hunyuan3d` |

## Mesh Processing

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-GeometryPack](https://github.com/MeshArt3D/ComfyUI-GeometryPack) | MeshArt3D | Remesh, boolean operations, UV unwrap, mesh simplification, and more | `community` `mesh-processing` |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Basic mesh operations, format conversion, and preprocessing | `community` `mesh-processing` |

## Texturing

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes) | N3rd00d | Texture inpainting and generation for 3D meshes | `community` `texturing` |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | UV texture baking and material assignment | `community` `texturing` |

## Gaussian Splatting

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | 3D Gaussian Splatting training and rendering | `community` `gaussian` |
| [ComfyUI-TripoSG](https://github.com/fredconex/ComfyUI-TripoSG) | fredconex | Tripo Stable Gaussian for high-quality Gaussian output | `vast-ai` `gaussian` `triposg` |
| [ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS) | smthemex | SLAT representation with Gaussian Splatting output | `microsoft` `gaussian` `trellis` |

## Rigging & Animation

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-Tripo](https://github.com/VAST-AI-Research/ComfyUI-Tripo) | VAST-AI-Research | UniRig auto-rigging and animation retargeting via Tripo API | `vast-ai` `rigging` `animation` |
| [ComfyUI-mesh2motion](https://github.com/jtydhr88/ComfyUI-mesh2motion) | jtydhr88 | Mesh to rigged animation workflows | `community` `rigging` `animation` |

## Depth & Normal

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-Marigold](https://github.com/kijai/ComfyUI-Marigold) | Kijai | Marigold diffusion-based depth and normal estimation | `community` `depth` |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Depth and normal map preprocessing for 3D reconstruction | `community` `depth` `normal` |

## Visualization

| Package | Author | Description | Tags |
|:--------|:-------|:------------|:-----|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | 3D mesh viewer with orbit camera controls | `community` `viewer` |
| [comfyUI-blender-wrapper](https://github.com/IRCSS/comfyUI-blender-wrapper) | IRCSS | Blender integration for rendering and scene manipulation | `community` `blender` |

---

## Tags Legend

**Creator Tags:**
- `tencent` - Tencent models (Hunyuan3D)
- `vast-ai` - VAST-AI models (Tripo, TripoSG, UniRig)
- `microsoft` - Microsoft models (TRELLIS)
- `stability` - Stability AI models (TripoSR)
- `community` - Community-developed packages

**Model Tags:**
- `hunyuan3d` `triposr` `triposg` `trellis` `crm` `instantmesh`

**I/O Tags:**
- `image-to-3d` `text-to-3d` `multi-view` `mesh-processing` `texturing` `rigging` `animation` `depth` `normal` `viewer`

**Format Tags:**
- `glb` `gaussian` `blender`

---

## Contributing

Contributions are welcome! Please submit a PR to add new packages or update existing entries.

## License

MIT License
