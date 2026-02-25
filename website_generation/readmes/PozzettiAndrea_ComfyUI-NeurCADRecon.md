----------
Work in Progress! This node is not finished.
----------

# ComfyUI-NeurCADRecon

Neural implicit CAD reconstruction with Morse loss.

**Originally from [ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)**

## Paper

**NeurCADRecon: Neural Representation for Reconstructing CAD Surfaces** (SIGGRAPH 2024)

## Installation

### Via ComfyUI Manager
Search for "NeurCADRecon" in ComfyUI Manager

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PozzettiAndrea/ComfyUI-NeurCADRecon
pip install -r ComfyUI-NeurCADRecon/requirements.txt
```

## Nodes

- **LoadNeurCADReconModel** - Initialize neural implicit model
- **NeurCADReconTrain** - Train model on point cloud
- **NeurCADReconInference** - Extract mesh from trained model
- **NeurCADReconLoadCheckpoint** - Load trained checkpoint

## Requirements

- torch>=2.0.0
- numpy>=1.24.0
- trimesh>=3.20.0
- scipy>=1.11.0
- PyMCubes>=0.1.4

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-NeurCADRecon/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## Credits

- Original CADabra: [PozzettiAndrea/ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)
- NeurCADRecon paper authors

## License

GPL-3.0
