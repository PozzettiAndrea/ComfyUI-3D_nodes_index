# USO Nodes for ComfyUI

Custom nodes to integrate the **USO** image generation model (based on FLUX.1 by ByteDance) into ComfyUI.

This project is an implementation based on the official source code from the [ByteDance/USO repository](https://github.com/bytedance/USO).

## Implemented Features

*   **`USO Model Loader`**:
    *   Loads all required models (FLUX.1, VAE, LoRA, Projector).
    *   Integrates encoders (T5-XXL, CLIP, SigLIP) with auto-downloading.
*   **`USO Sampler`**:
    *   Text-to-image pipeline supporting **content** and **style** references.

## Status: Implementation Blocked by Hardware Limitations

**The entire logical pipeline has been implemented, but I cannot validate its functionality on consumer-grade hardware due to excessive VRAM consumption.**

Loading the models or starting the sampling process systematically triggers a `torch.OutOfMemoryError`. Therefore, I cannot confirm that the full pipeline works as intended.

This project should be considered a **theoretical proof-of-concept that requires memory optimization expertise** to become testable and usable.

## Call for Contributions

I am looking for contributors with experience in PyTorch model optimization and memory management to tackle this bottleneck. The main goal is to reduce the VRAM footprint and make these nodes accessible.

Any help, suggestions, or Pull Requests are welcome.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    git clone https://github.com/Juste-Leo2/USO_ComfyUI.git
    ```
2.  Restart ComfyUI.

## Acknowledgments

This project is built upon the work of ByteDance on the original **USO** model. All credit for the model's architecture goes to the original authors.