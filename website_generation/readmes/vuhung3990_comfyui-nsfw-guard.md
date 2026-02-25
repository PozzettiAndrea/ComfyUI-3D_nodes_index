# ComfyUI NSFW Guard

Block NSFW content in ComfyUI workflows.

✅ **Zero Config** - Model auto-downloads on first use  
✅ **Fast** - ~0.1s per image, even on CPU  
✅ **Accurate** - 95%+ detection rate

## Why?

I needed a fast NSFW detector that doesn't slow down my workflow. Other solutions either:
- Use large models (accurate but slow)
- Replace NSFW with censored images (still wastes GPU resources)

I just want to **stop immediately** when NSFW is detected — no wasted compute on unacceptable content.

## Installation

**ComfyUI Manager:** Search "NSFW Guard" and install.

**Manual:**
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/vuhung3990/comfyui-nsfw-guard.git
pip install -r comfyui-nsfw-guard/requirements.txt
```

## Usage

Add **NSFW Check (YOLO)** node → Connect image → Done.

```
[Image] → [NSFW Check] → [Save/Preview]
```

- **Safe**: Image passes through
- **NSFW**: Workflow stops

![Demo](screenshot.jpg)

## Threshold

| Value | Effect |
|-------|--------|
| 0.3 | Strict |
| 0.5 | Balanced (default) |
| 0.7 | Lenient |

## API

NSFW blocks return structured JSON via `/history`:

```json
{"error": {"type": "nsfw_content_detected", "details": {"confidence": 0.95}}}
```

## Manual Model Download

If auto-download fails, manually download and place in `ComfyUI/models/nsfw/`:

- [Model](https://huggingface.co/Falconsai/nsfw_image_detection/resolve/main/falconsai_yolov9_nsfw_model_quantized.pt)
- [Labels](https://huggingface.co/Falconsai/nsfw_image_detection/resolve/main/labels.json)

## Credits

Model: [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection)
