# ComfyUI Marigold + PaGeR TensorRT (RT-Only)

This pack is RT-only and exposes exactly four nodes:

1. `Load UNet -> TensorRT Engine` (`LoadUNetTensorRTEngine`)
2. `Load Marigold IID Appearance Model (TensorRT)` (`DownloadAndLoadMarigoldIIDAppearanceModelRT`)
3. `Load Marigold IID Lighting Model (TensorRT)` (`DownloadAndLoadMarigoldIIDLightingModelRT`)
4. `Load PaGeR Model (TensorRT)` (`DownloadAndLoadPaGeRModelRT`)

## Scope

- This pack only builds/loads TensorRT UNet backends.
- Inference/postprocess nodes are expected from [Comfyui-marigold-intrinsics-PaGeR](https://github.com/Apache0ne/Comfyui-marigold-intrinsics-PaGeR) node pack.
- `IIDMODEL` and `PAGERMODEL` payloads are kept compatible so external nodes can run unchanged.

## Install

```bash
pip install -r requirements.txt
```

## Notes

- Engine selection supports `.engine` and `.trt` files.
- Model files are stored under `models/marigold_intrinsics/...`.
- PaGeR RT loader keeps optional Comfy TAESD VAE support.

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
- [ONNX Documentation](https://onnx.ai/onnx/), for the Open Neural Network Exchange model format and ecosystem.
- [NVIDIA TensorRT Documentation](https://docs.nvidia.com/deeplearning/tensorrt/latest/), for engine building, optimization profiles, and runtime APIs.

We thank the authors and maintainers for making their code publicly available.
