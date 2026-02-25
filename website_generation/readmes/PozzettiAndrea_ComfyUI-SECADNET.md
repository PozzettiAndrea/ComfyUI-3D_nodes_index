----------
Work in Progress! This node is not finished.
----------

# ComfyUI-SECADNET

Sketch-extrude CAD reconstruction from voxel representations.

**Originally from [ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)**

## Paper

**SECAD-Net: Self-Supervised CAD Reconstruction by Learning Sketch-Extrude Operations**

- GitHub: https://github.com/BunnySoCrazy/SECAD-Net

## Installation

### Via ComfyUI Manager
Search for "SECADNET" in ComfyUI Manager

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PozzettiAndrea/ComfyUI-SECADNET
pip install -r ComfyUI-SECADNET/requirements.txt
```

## Nodes

- **LoadSECADNetModel** - Load pretrained encoder/decoder/generator
- **MeshToVoxel** - Convert mesh to 64x64x64 voxel grid
- **SECADNetInference** - Initial reconstruction from voxels
- **SECADNetFinetune** - Per-shape optimization (200-500 epochs)
- **SECADNetLatentToMesh** - Generate mesh from latent codes

## Requirements

- torch>=2.0.0
- numpy>=1.24.0
- trimesh>=3.20.0
- PyMCubes>=0.1.4
- gdown>=4.7.0

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-SECADNET/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## Credits

- Original CADabra: [PozzettiAndrea/ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)
- SECAD-Net paper authors

## License

GPL-3.0
