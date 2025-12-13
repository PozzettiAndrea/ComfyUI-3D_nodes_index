# Awesome ComfyUI 3D

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated index of ComfyUI nodes for 3D generation, processing, and visualization.

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

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Extensive suite with 20+ models: InstantMesh, CRM, TripoSR, Era3D, Zero123++, Unique3D, 3DGS training/rendering, FlexiCubes, mesh fitting |
| [ComfyUI-Hunyuan3d-2-1](https://github.com/visualbruno/ComfyUI-Hunyuan3d-2-1) | visualbruno | Tencent | 228 | Two-stage pipeline: shape generation, then texture baking with differentiable renderer and xAtlas UV |
| [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper) | Kijai | Tencent | 921 | DiT Flow Matching for shape, then texture refinement with custom rasterizer and xatlas UV unwrapping |
| [ComfyUI-HunyuanX](https://github.com/PozzettiAndrea/ComfyUI-HunyuanX) | PozzettiAndrea | Tencent | 5 | Standard/modular pipelines with PBR multiview texturing, inpainting, latent blending, multi-format export |
| [ComfyUI-Hunyuan3D-Part](https://github.com/PozzettiAndrea/ComfyUI-Hunyuan3D-Part) | PozzettiAndrea | Tencent | 32 | P3-SAM for 3D mesh segmentation and X-Part diffusion for part mesh generation |
| [Comfyui_Hunyuan3D_EX](https://github.com/BIMer-99/Comfyui_Hunyuan3D_EX) | BIMer-99 | Tencent | 7 | Six-view generation, TriMeshViewer, background removal, trimesh optimization without pytorch3d |
| [ComfyUI-Flowty-TripoSR](https://github.com/flowtyone/ComfyUI-Flowty-TripoSR) | flowtyone | Stability AI | 526 | Fast feedforward 3D reconstruction from single image |
| [ComfyUI-Flowty-CRM](https://github.com/flowtyone/ComfyUI-Flowty-CRM) | flowtyone | Tsinghua Univ | 156 | Convolutional Reconstruction Model for image-to-3D |
| [ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS) | smthemex | Microsoft | 174 | TRELLIS for structured latent 3D generation |
| [ComfyUI-IF_Trellis](https://github.com/if-ai/ComfyUI-IF_Trellis) | if-ai | Microsoft | 441 | TRELLIS with SLAT representation |
| [ComfyUI-SAM3DBody](https://github.com/PozzettiAndrea/ComfyUI-SAM3DBody) | PozzettiAndrea | Meta AI | 199 | Full-body 3D human mesh recovery with body/hand detection modes, visualization, and OBJ/PLY export |

## Text-to-3D

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-Tripo](https://github.com/VAST-AI-Research/ComfyUI-Tripo) | VAST-AI-Research | VAST-AI | 315 | Official Tripo API for text/image/multiview-to-3D, texture with PBR, refinement, rigging, animation |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Text-to-3D via Score Distillation Sampling |

## Multi-View Generation

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Zero123++, Era3D, Wonder3D, SV3D for multi-view generation |
| [ComfyUI-Hunyuan3DWrapper](https://github.com/kijai/ComfyUI-Hunyuan3DWrapper) | Kijai | Tencent | 921 | Hunyuan3D multi-view diffusion |

## Mesh Processing

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-GeometryPack](https://github.com/PozzettiAndrea/ComfyUI-GeometryPack) | PozzettiAndrea | Community | 33 | Mesh I/O, remeshing, UV unwrap, booleans using libigl, CGAL |
| [ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra) | PozzettiAndrea | Community | 9 | CAD file processing (STEP, IGES, BREP) with OpenCASCADE |
| [ComfyUI-Direct3D-S2](https://github.com/visualbruno/ComfyUI-Direct3D-S2) | visualbruno | Direct3D | 36 | Image-to-dense-mesh or mesh refinement for Hunyuan3D outputs using v1.0/1.1 models |
| [ComfyUI-CuMesh](https://github.com/visualbruno/ComfyUI-CuMesh) | visualbruno | Community | 1 | CuMesh operations integration |
| [ComfyUI-QRemeshify](https://github.com/visualbruno/ComfyUI-QRemeshify) | visualbruno | Community | 6 | Mesh remeshing operations |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Basic mesh operations and format conversion |

## Texturing

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-Paint3D-Nodes](https://github.com/N3rd00d/ComfyUI-Paint3D-Nodes) | N3rd00d | OpenTexture | 72 | 3D model texture inpainting |
| [ComfyUI-DetailGen3D](https://github.com/PozzettiAndrea/ComfyUI-DetailGen3D) | PozzettiAndrea | VAST-AI | 0 | Enhance coarse meshes with geometric detail via diffusion-based SDF and marching cubes |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | UV texture baking and materials |

## Gaussian Splatting

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | 3DGS training and rendering |
| [ComfyUI_TRELLIS](https://github.com/smthemex/ComfyUI_TRELLIS) | smthemex | Microsoft | 174 | SLAT with Gaussian output |
| [ComfyUI-SAM3DObjects](https://github.com/PozzettiAndrea/ComfyUI-SAM3DObjects) | PozzettiAndrea | Meta AI | 113 | Single-image to 3D Gaussian Splats and textured GLB meshes with batch processing |

## Rigging & Animation

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-UniRig](https://github.com/PozzettiAndrea/ComfyUI-UniRig) | PozzettiAndrea | SIGGRAPH 2025 | 231 | ML-based skeleton extraction and skinning for any mesh with pose manipulation and FBX/GLB export |
| [ComfyUI-Tripo](https://github.com/VAST-AI-Research/ComfyUI-Tripo) | VAST-AI-Research | VAST-AI | 315 | Tripo API for skeleton rigging and animation retargeting |
| [ComfyUI-mesh2motion](https://github.com/jtydhr88/ComfyUI-mesh2motion) | jtydhr88 | Mesh2Motion | 35 | Full editor with skeleton fitting, weight painting for humanoid/quadruped/bird/dragon, animation library |

## Depth & Normal

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-DepthAnythingV3](https://github.com/PozzettiAndrea/ComfyUI-DepthAnythingV3) | PozzettiAndrea | DepthAnything | 210 | State-of-the-art monocular depth estimation |
| [ComfyUI-Marigold](https://github.com/kijai/ComfyUI-Marigold) | Kijai | ETH Zurich | 557 | Diffusion-based depth/normal with ensemble iterations, fp16 support, and OpenEXR export |
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Depth/normal preprocessing |

## Visualization

| Package | Node Author | Model Author | Stars | Description |
|:--------|:------------|:-------------|:-----:|:------------|
| [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) | MrForExample | Multiple | 3.5k | Built-in 3D mesh and Gaussian viewer with orbit camera for previewing assets |
| [comfyUI-blender-wrapper](https://github.com/IRCSS/comfyUI-blender-wrapper) | IRCSS | Blender | 5 | Headless Blender for cleanup, UV unwrapping, baking, and rigging tasks |

---

## Model Authors

| Organization | Models |
|:-------------|:-------|
| **Tencent** | Hunyuan3D, Hunyuan3D-Part, Hunyuan3D-Omni |
| **Microsoft** | TRELLIS (Structured Latent) |
| **Meta AI** | SAM 3D Body, SAM 3D Objects |
| **VAST-AI** | Tripo, TripoSG, UniRig, DetailGen3D |
| **Stability AI** | TripoSR |
| **ETH Zurich** | Marigold |
| **Tsinghua University** | CRM |
| **Community** | Various mesh processing tools |

---

## Contributing

Contributions welcome! Please submit a PR to add new packages or update existing entries.

## License

MIT License
