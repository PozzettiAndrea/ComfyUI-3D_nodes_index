# ComfyUI-TripoSF

ComfyUI nodes for **TripoSF** - high-resolution 3D mesh encoding/decoding (up to 1024³) with arbitrary topology support including open surfaces.

## Nodes

- **Load TripoSF Model** - Download and load the TripoSF VAE model from HuggingFace
- **TripoSF Encode** - Encode a mesh into latent embeddings
- **TripoSF Decode** - Decode latents back to high-resolution mesh
- **TripoSF Interpolate** - Interpolate between mesh latents using optimal transport
- **Visualize TripoSF Latent** - Visualize the latent space

## Workflows

### Latent Embeddings
![Embeddings workflow](docs/embeddings.png)

### Surface Reconstruction
![Surface reconstruction workflow](docs/surface_reconstruction.png)

## Install

Via ComfyUI Manager or clone into `custom_nodes/`.

Requires GeometryPack for TRIMESH type support.

## Community

Questions or feature requests? Open a [Discussion](https://github.com/PozzettiAndrea/ComfyUI-TripoSF/discussions) on GitHub.

Join the [Comfy3D Discord](https://discord.gg/bcdQCUjnHE) for help, updates, and chat about 3D workflows in ComfyUI.
