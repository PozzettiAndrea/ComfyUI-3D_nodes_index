# Fat Mex Nodes for ComfyUI

All-in-one node pack that collapses complex ComfyUI workflows into single nodes. Built for AI influencer content creation but useful for any image generation pipeline.

## Nodes

| Node | What it replaces | Description |
|------|-----------------|-------------|
| **Model Loader** | UNETLoader + CLIPLoader + VAELoader + LoraLoader x2 | Pick a preset, get MODEL + CLIP + VAE. Supports LoRA stacking, sage attention, model sampling shift. |
| **Content Sampler** | EmptyLatentImage + CLIPTextEncode x2 + KSampler + VAEDecode | All-in-one text-to-image. Prompt in, image out. |
| **Reference Sampler** | VAEEncode + ReferenceLatent + CLIPTextEncode x2 + KSampler + VAEDecode | Reference-guided generation. Feed a face photo, get consistent identity across poses. |
| **Image Edit Sampler** | TextEncodeQwenImageEditPlus + CLIPTextEncode + EmptyQwenImageLayeredLatent + KSampler + VAEDecode | Qwen image editing in one node. Feed reference images + edit prompt. |
| **Inpaint Sampler** | VAEEncode + SetLatentNoiseMask + TextEncodeQwenImageEditPlus + CLIPTextEncode + KSampler + VAEDecode | Masked inpainting with Qwen Edit conditioning. Perfect for head swaps. |
| **Head Mask** | LoadSAM3Model + SAM3Grounding + MaskGrow | SAM3-based head/object masking in one node. |
| **Upscaler** | Multiple upscale nodes | All-in-one image upscaling. |
| **Face Swap** | InsightFace + multiple detection/swap nodes | One-click face swap with InsightFace. |
| **Prompt Batch** | CR Prompt List + CLIPTextEncode | Enter multiple prompts (one per line), get them all encoded for batch generation. |
| **Prompt Template** | Manual prompt writing | AI influencer prompt generator with style presets. |
| **Dataset Saver** | SaveImage + manual folder management | Save images to structured dataset folders with captions. |
| **Image Compare** | Manual side-by-side comparison | Side-by-side image comparison output. |

## Supported Model Presets

| Preset | Steps | Use Case |
|--------|-------|----------|
| Klein 9B | 6 | Fast reference-based generation |
| Klein 9B True | 20 | High-quality reference generation |
| Qwen Image Edit 2509 | 8 | Image editing, face swap, multi-angle |
| Qwen Image Edit 2511 | 4* | Image editing (*with Lightning LoRA) |
| Qwen Image 2512 | 8 | Text-to-image with shift 0.6 |
| Z-Image Turbo | 6 | Fast text-to-image, detail pass |
| Chroma HD | 3 | Fast high-quality generation |

## Install

### ComfyUI Manager (recommended)
Search for **Fat Mex Nodes** in ComfyUI Manager and click Install.

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/FatMex/ComfyUI-FatMex-Nodes.git FatMex-Nodes
pip install -r FatMex-Nodes/requirements.txt
```

### Dependencies
Some nodes require additional custom node packs:
- **Head Mask** needs [ComfyUI-SAM3](https://github.com/neverbiasu/ComfyUI-SAM3)
- **Face Swap** needs InsightFace models (auto-downloaded on first use)

Restart ComfyUI after installation.

## Workflows

Example workflows are included in the `workflows/` folder. Load them directly in ComfyUI.

## License

MIT License - see [LICENSE](LICENSE)
