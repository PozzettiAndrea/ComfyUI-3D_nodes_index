# Azure Flux ComfyUI Nodes

Minimal, production-focused ComfyUI nodes for Azure OpenAI Images (Flux). Provides:

- FLUX.1-Kontext-ImageToImage: edit existing image (edits API)
- FLUX.1-Kontext-TextToImage: generate from text (generations API)
- FLUX-1.1-pro-TextToImage: generate from text (generations API)
- FLUX.2-pro-TextToImage: generate from text (generations API)

All nodes call the official Azure OpenAI Images endpoints. No extra services, wrappers, or local models.

## Overview

Four nodes with only the necessary fields for each mode. The API logic is unchanged and mirrors Azure’s Images Edits/Generations behavior.

## Installation

Manual install:

```
cd ComfyUI/custom_nodes/
git clone https://github.com/xpanceo-team/azure-flux-comfyui.git
cd azure-flux-comfyui
pip install -r requirements.txt
```

Restart ComfyUI after installation.

## Configuration

Set these fields in the node UI:

- azure_endpoint: `https://<your-resource>.services.ai.azure.com/` or `https://<your-resource>.cognitiveservices.azure.com/`
- api_version: `2025-04-01-preview` (or `preview` for FLUX.2-pro if required)
- api_key: your Azure OpenAI API key

Notes:
- Endpoint must end with `/`.
- Ensure the deployment name exists in your Azure resource:
  - Kontext nodes use `FLUX.1-Kontext-pro`
  - FLUX-1.1 node uses `FLUX-1.1-pro`
  - FLUX.2 node uses `FLUX.2-pro`

## Nodes

- FLUX.1-Kontext-ImageToImage
  - Mode: image-to-image (edits)
  - Inputs: azure_endpoint, api_version, api_key, editing_prompt, image_1
  - Optional: size (`WIDTHxHEIGHT`, default `1024x1024`), n (1–8), output_format (`png|jpeg|webp`)

- FLUX.1-Kontext-TextToImage
  - Mode: text-to-image (generations)
  - Inputs: azure_endpoint, api_version, api_key, editing_prompt
  - Optional: size, n, output_format

- FLUX-1.1-pro-TextToImage
  - Mode: text-to-image (generations)
  - Inputs: azure_endpoint, api_version, api_key, editing_prompt
  - Optional: size, n, output_format

- FLUX.2-pro-TextToImage
  - Mode: text-to-image (generations)
  - Inputs: azure_endpoint, api_version, api_key, editing_prompt
  - Optional: size, n, output_format

## Parameters

- editing_prompt: text description or edit instruction
- image_1: input image tensor (only for ImageToImage)
- size: `WIDTHxHEIGHT` (e.g. `1024x1024`)
- n: number of images to generate (1–8)
- output_format: `png`, `jpeg`, or `webp`

## Requirements

- Python >= 3.8
- ComfyUI (current version)
- Dependencies (from `requirements.txt`):
  - requests
  - Pillow
  - torch
  - numpy

## Troubleshooting

- 401/403: check `api_key`, resource/region, and endpoint URL.
- 404/400: verify the deployment name exists and supports the operation.
  - FLUX-1.1-pro supports generations; use TextToImage, not edits.
- Invalid size: use `WIDTHxHEIGHT` (e.g., `1024x1024`).
- Image-to-image: `image_1` is required.
- Timeouts: reduce `n` or try a smaller size.

## License

MIT — see `LICENSE`.
