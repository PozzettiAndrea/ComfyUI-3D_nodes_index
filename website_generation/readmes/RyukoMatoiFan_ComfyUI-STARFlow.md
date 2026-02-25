# ComfyUI-STARFlow

Custom nodes for STARFlow text-to-image generation in ComfyUI.

## Install
1) Clone into `ComfyUI/custom_nodes/ComfyUI-STARFlow`.
2) Restart ComfyUI.

No extra Python installs are required beyond a standard ComfyUI setup.

## Models
- T5-XL text encoder (required): download the encoder weights from
  https://huggingface.co/QQGYLab/ELLA/tree/main/models--google--flan-t5-xl--text_encoder
  and place the `.safetensors` file in `ComfyUI/models/text_encoders/`.
- VAE: load any SD VAE in ComfyUI via `VAELoader` (e.g. `sd-vae-ft-ema.safetensors`).
- STARFlow checkpoint: place your `.pth` or `.safetensors` file in `ComfyUI/models/starflow/`.

## Nodes
- `STARFlowCheckpointLoader`: loads the STARFlow checkpoint and preset config.
- `STARFlowT5TextEncode`: takes a STRING prompt input and produces STARFlow conditioning.
- `STARFlowSampler`: runs STARFlow sampling (supports optional image conditioning).
- `STARFlowVAEDecode`: decodes latents to images with ComfyUI VAE.

## Basic Workflow
1) Add a `String (Multiline)` node and connect it to `STARFlowT5TextEncode.text`.
2) Load a STARFlow checkpoint with `STARFlowCheckpointLoader`.
3) Load a VAE with `VAELoader`.
4) Connect `STARFlowSampler` (model + conditioning + vae), then `STARFlowVAEDecode`, then `SaveImage`.

An example is included at `workflows/starflow_basic_t2i.json`.

![Workflow](workflow.png)
