# ComfyUI Marigold Intrinsics PaGeR

This custom node pack provides Marigold IID nodes and PaGeR ERP geometry nodes.
![pack](https://github.com/Apache0ne/Comfyui-marigold-intrinsics-PaGeR/blob/main/examples/workflows.png)

## Included Nodes

TODO: missing PaGeR-Normals
PaGeR models 5/6

### Marigold IID Loaders

1. `Load Marigold IID Appearance Model` (`DownloadAndLoadMarigoldIIDAppearanceModel`)
- Downloads and loads the Marigold appearance pipeline as `IIDMODEL`.
- Uses hardcoded in-memory empty conditioning (no precomputed `.safetensors` path).

2. `Load Marigold IID Lighting Model` (`DownloadAndLoadMarigoldIIDLightingModel`)
- Downloads and loads the Marigold lighting pipeline as `IIDMODEL`.
- Uses hardcoded in-memory empty conditioning (no precomputed `.safetensors` path).

3. `Load Marigold IID Split (UNet/CLIP/VAE)` (`MarigoldIIDSplitLoader`)
- Loads split components as Comfy `MODEL`, `CLIP`, `VAE`.
- Uses runtime-minimal base files by default (scheduler + VAE); text assets are only fetched if `load_comfy_model_clip` is enabled.
- Supports tiny VAEs, including TAESD-style VAE choices.

4. `Translate Marigold Split -> IIDMODEL` (`MarigoldIIDSplitToIIDModel`)
- Converts split-loaded `MODEL` + `CLIP` + `VAE` into `IIDMODEL`.
- Uses hardcoded in-memory empty conditioning and TAESD-compatible VAE adapters.

### Marigold IID Inference

1. `Marigold IID Appearance` (`MarigoldIIDAppearance`)
- Runs appearance inference and returns `albedo`, `roughness`, `metallicity`.

2. `Marigold IID Appearance (with Material)` (`MarigoldIIDAppearanceExtended`)
- Same as above, plus `material`.

3. `Marigold IID Lighting (HyperSim)` (`MarigoldIIDLighting`)
- Runs lighting inference and returns `albedo`, `shading`, `residual`.

### PaGeR

1. `Load PaGeR Model` (`DownloadAndLoadPaGeRModel`)
- Loads PaGeR depth or normal model.
- Uses hardcoded in-memory empty conditioning (no tokenizer/text encoder stage in loader runtime path).
- Includes optional Comfy TAESD VAE backend (`use_comfy_taesd_vae`).

2. `PaGeR Infer Cubemap (ERP)` (`PaGeRInferCubemap`)
- Node A in the PaGeR pipeline.
- Runs encode + UNet + decode and returns decoded cubemap predictions.

3. `PaGeR Depth Postprocess (ERP)` (`PaGeRDepthPostprocess`)
- Node B depth postprocess.
- Converts cubemap prediction to ERP outputs:
  - `depth`
  - `edge_mask`
  - `depth_color`

4. `PaGeR Normal Postprocess (ERP)` (`PaGeRNormalPostprocess`)
- Node B normal postprocess.
- Converts cubemap prediction to ERP normal visualization.

5. `PaGeR Save Point Cloud (GLB/PLY)` (`PaGeRSavePointCloud`)
- Exports point cloud from `color` + `depth` as `.glb` or `.ply`.
- Supports `depth_mode` auto logic, optional masks, and optional edge filtering.

## Recommended PaGeR Pipeline

For depth:
1. `Load PaGeR Model` with a depth checkpoint.
2. `PaGeR Infer Cubemap (ERP)`.
3. `PaGeR Depth Postprocess (ERP)`.
4. Optional: `PaGeR Save Point Cloud (GLB/PLY)`.

For normals:
1. `Load PaGeR Model` with a normals checkpoint.
2. `PaGeR Infer Cubemap (ERP)`.
3. `PaGeR Normal Postprocess (ERP)`.

## Hardcoded Empty Conditioning

All active loaders now use hardcoded in-memory zero embeddings for empty conditioning:
1. No `.safetensors` empty-conditioning file is required.
2. No precomputed-conditioning inputs are exposed on loader nodes.
3. Marigold uses shape `[1, 2, C]`, where `C` is inferred from UNet `cross_attention_dim`.
4. PaGeR uses shape `[1, T, C]`, where `T` defaults to SD2-style context length and `C` is inferred from UNet config.

## TAESD VAE Option

`Load PaGeR Model` supports an optional Comfy TAESD VAE backend.

Why use it:
1. Lower VRAM usage.
2. Faster VAE encode/decode on constrained GPUs.
3. Useful when fitting PaGeR workflows on smaller cards.

Tradeoff:
1. TAESD is a tiny/approximate VAE.
2. Output quality can degrade in fine details, smooth gradients, and sharp depth edges.
3. In many scenes it is still usable, especially when speed and memory are priority.

## 8GB VRAM Note

This setup has been tested on an 8GB GPU with practical settings:
1. Prefer `fp16` precision.
2. Use hardcoded in-memory empty conditioning (default).
3. Enable TAESD VAE when memory is tight.
4. Keep PaGeR as `Infer Cubemap -> Postprocess` (current default workflow).

## Dependencies

Install with:

```bash
pip install -r requirements.txt
```

## Citation

Please cite our paper: (Waiting for citation)

```bibtex
Put citations here
```

## License

This code of this work is licensed under the Apache License, Version 2.0 (as defined in the [LICENSE](LICENSE)).

The models are licensed under RAIL++-M License (as defined in the [LICENSE-MODEL](LICENSE-MODEL))

By downloading and using the code and model you agree to the terms in [LICENSE](LICENSE) and [LICENSE-MODEL](LICENSE-MODEL) respectively.

## Acknowledgements

This project builds upon and is inspired by the following repositories and works:

- [Marigold-e2e-ft](https://github.com/VisualComputingInstitute/diffusion-e2e-ft), based on paper [Fine-Tuning Image-Conditional Diffusion Models is Easier than You Think](https://arxiv.org/abs/2409.11355).
- [Marigold](https://github.com/prs-eth/Marigold/tree/main), based on paper [Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://arxiv.org/abs/2312.02145).

We thank the authors and maintainers for making their code publicly available.
