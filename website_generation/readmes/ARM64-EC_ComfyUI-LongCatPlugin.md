# ComfyUI-LongCatPlugin

[简体中文](README_CN.md)

> Third-party implementation of LongCat for ComfyUI.

## Overview
ComfyUI nodes wrapping LongCat image generation and editing pipelines (diffusers-based). Includes text-to-image and multi-image edit flows with prompt rewriting, aspect-aware sizing, and latent decoding for ComfyUI.

## Features
 - **LongCatPipelineLoader**: Loads the LongCat pipeline and exposes Model/CLIP/VAE components.
 - **TextEncodeLongCatImage / TextEncodeLongCatImageEdit**: Encodes text prompts and reference images (for editing) into conditioning.
 - **LongCatSizePicker**: Selects the target supported resolutions and produces empty latents of the correct size.
 - **LongCatImageResizer**: Resize input images to the nearest LongCat supported resolution using several strategies.
 - **LongCatSampler**: Handles the sampling process (denoising) using the LongCat transformer.
 - **LongCatImageSizeScale**: Scales images to a target pixel area and rounds dimensions to multiples of 16.

## Implemented (What works today)
- LongCat transformer: `LongCatImageTransformer2DModel` implemented and used by the pipelines.
- Pipelines:
    - `LongCatImagePipeline` (text-to-image): prompt rewrite, tokenizer usage, latent packing, denoising loop, and VAE decode implemented.
    - `LongCatImageEditPipeline` (image editing): implemented with VL prompt handling, image latents, and edit-aware denoising.
- Nodes (ComfyUI):
    - `LongCatPipelineLoader` (basic loader for pipelines; returns (model, pipeline, vae) so other nodes can reference them).
    - `TextEncodeLongCatImage` (T2I text encoding; uses CLIP tokenizer/encoder)
    - `TextEncodeLongCatImageEdit` (Edit text & image encoding — partially implemented; some behavior remains to be fully wired to CLIP/VL models)
    - `LongCatSizePicker` (picks supported resolutions and returns empty latents)
    - `LongCatImageResizer` (resize/pad/crop strategies to fit LongCat resolutions)
    - `LongCatSampler` (wraps ComfyUI-supported sampler calls into the LongCat denoising loop)
    - `LongCatImageSizeScale` (image scaling node)
- Utilities: `longcat_image/utils/model_utils.py` provides functions like `pack_latents`/`unpack_latents`, `prepare_pos_ids`, `split_quotation`, `retrieve_timesteps`, and optimized scaling helpers.
- Training examples: scripts and example configs for LoRA, SFT, Edit, and DPO training under `train_examples/`.
- Tests: Minimal unit tests for nodes (`tests/test_nodes.py`) for CI / smoke check.

## Installation
1.  **Copy Folder**: Copy the `comfyui_longcat` folder into your ComfyUI `custom_nodes` directory.
    *   Example: `ComfyUI/custom_nodes/comfyui_longcat`
2.  **Install Dependencies**: Ensure your ComfyUI environment has the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    (Note: `requirements.txt` is in the root of this repo, or check `setup.py` for list).
3.  **Model Weights**: Place LongCat model weights in a directory accessible to ComfyUI.

## Usage in ComfyUI
- Put this plugin folder into ComfyUI `custom_nodes`, then restart.
- Nodes appear under category `LongCat`.
- **Workflow**:
    1. Load the model/pipeline with `LongCatPipelineLoader` (returns `model`, `clip` (pipeline), and `vae`).
    2. Use `TextEncodeLongCatImage` for text-to-image or `TextEncodeLongCatImageEdit` when editing or using reference images; connect the `clip`/pipeline node to these encoders.
    3. Use `LongCatSizePicker` to pick a supported resolution and create an empty latent (or use your own latents).
    4. Use `LongCatImageResizer` to resize reference images to the nearest supported LongCat resolution (if needed).
    5. Connect the `MODEL`, `CONDITIONING` (Positive/Negative), and `LATENT` to `LongCatSampler` to run the LongCat denoising process.
- Set `model_path` to your downloaded LongCat checkpoint; on CUDA you may enable `cpu_offload` to save VRAM.

## Development
- Tests: `pytest tests/test_nodes.py`
- Key modules: `nodes.py`, `longcat_image/pipelines/*`, `longcat_image/models/longcat_image_dit.py`.

## To-Do
### Completed / in-progress items
- Implemented core transformer and pipelines for text-to-image and edit flows.
- Node wrappers for basic operation and VAE/text encoding/decoding.
- Training example scripts for LoRA, SFT, DPO, and Edit training flows.

### Planned / Roadmap
 - [ ] Finalize `LongCatPipelineLoader` to robustly load:
    - Diffusers-style directory checkpoints (separate transformer, vae, tokenizer, scheduler subfolders)
    - Single-file safetensors checkpoints and mapping to model components
    - CLIP and VAE loading and correct device placement
- [ ] Implement `TextEncodeLongCatImageEdit` fully (support multi-image & VL inputs and correct token/image merging).
- [ ] Add documentation: step-by-step ComfyUI usage, example flow screenshots, and a model download/prepare helper script.
- [ ] Add automated pipeline tests, including smoke tests and tests across dtype/device combos.
- [ ] Add Git LFS support for model weights and an example of safe weight handling.
- [ ] Add GitHub Actions CI to run linting and tests for PRs.
- [ ] Add `pre-commit` config to avoid accidental commits of binary or cache files.
- [ ] Add examples showing how to run training scripts for LoRA/SFT/DPO and how to apply saved checkpoints to the ComfyUI nodes.

If you'd like, I can implement the `LongCatCheckpointLoader` improvements and the `TextEncodeLongCatImageEdit` node next, and add GitHub Actions for CI. 

## Credits
- LongCat base model & pipelines: original LongCat project (LongCat team).
- **diffusers** (Hugging Face) for pipeline scaffolding.
- **transformers** (Hugging Face) for text and vision encoders.
- **accelerate** for optional CPU/GPU offload helpers.
- **PyTorch** for core tensor and model runtime.
- **Pillow (PIL)** and **NumPy** for image/tensor conversions.
