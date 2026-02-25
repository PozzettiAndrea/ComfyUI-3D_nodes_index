----------
Work in Progress! This node is not finished.
----------

# ComfyUI-Cadrille

Multi-modal CAD reconstruction from point clouds, images, or text. Includes CAD-Recode for code generation.

**Originally from [ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)**

## Paper

**Cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning**

- GitHub: https://github.com/col14m/cadrille

## Installation

### Via ComfyUI Manager
Search for "Cadrille" in ComfyUI Manager

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PozzettiAndrea/ComfyUI-Cadrille
pip install -r ComfyUI-Cadrille/requirements.txt

# CadQuery (required for code execution)
conda install -c conda-forge cadquery
```

## Nodes

### Cadrille
- **LoadCadrilleModel** - Load Cadrille model from HuggingFace
- **CadrilleInference** - Generate CadQuery code from point cloud
- **CadrilleImageInference** - Generate CadQuery code from images
- **CadrilleTextInference** - Generate CadQuery code from text description

### CAD-Recode
- **LoadCADRecodeModel** - Load CAD-Recode model
- **CADRecodeInference** - Point cloud to CadQuery code
- **CadQueryExecute** - Safely execute generated CadQuery code

## Requirements

- torch>=2.0.0
- numpy>=1.24.0
- trimesh>=3.20.0
- transformers>=4.30.0
- accelerate
- Pillow
- cadquery (via conda)

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-Cadrille/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.

## Credits

- Original CADabra: [PozzettiAndrea/ComfyUI-CADabra](https://github.com/PozzettiAndrea/ComfyUI-CADabra)
- Cadrille and CAD-Recode paper authors

## License

GPL-3.0
