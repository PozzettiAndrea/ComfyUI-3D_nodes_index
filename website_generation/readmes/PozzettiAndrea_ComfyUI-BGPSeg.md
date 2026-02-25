----------
Work in Progress! This node is not finished.
----------

# ComfyUI-BGPSeg

Boundary-guided primitive segmentation for point clouds.

**Originally from [ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)**

## Paper

**BGPSeg: Boundary-Guided Primitive Segmentation for Point Clouds** (IEEE TIP 2025)

## Installation

### Via ComfyUI Manager
Search for "BGPSeg" in ComfyUI Manager

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PozzettiAndrea/ComfyUI-BGPSeg
pip install -r ComfyUI-BGPSeg/requirements.txt
```

## Nodes

- **LoadBGPSegModels** - Load BGFE and BoundaryNet models
- **BGPSegSegmentation** - Segment point cloud with boundary guidance

## Requirements

- torch>=2.0.0
- numpy>=1.24.0
- trimesh>=3.20.0
- gdown>=4.7.0
- CUDA toolkit (for JIT-compiled extensions)

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-BGPSeg/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## Credits

- Original CADabra: [PozzettiAndrea/ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)
- BGPSeg paper authors

## License

GPL-3.0