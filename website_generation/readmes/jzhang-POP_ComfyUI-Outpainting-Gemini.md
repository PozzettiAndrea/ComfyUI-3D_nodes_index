# ComfyUI-Outpainting-Gemini

ComfyUI custom nodes for Gemini image generation and Nano Banana Pro outpainting workflows.

## Nodes

### Gemini Image Generate

Generate or transform images using Gemini 3 API.

**Inputs:**
- `image`: Input image
- `prompt`: Text prompt
- `api_key`: Gemini API key
- `model`: `gemini-3-pro-image-preview` or `gemini-3-nano-image-preview`
- `aspect_ratio`: Target aspect ratio (STRING, wirable)
- `resolution`: Target resolution (STRING, wirable)

### Nano Banana Pad Calculator

Calculate optimal padding to reach a supported Nano Banana Pro dimension.

**Inputs:**
- `image`: Input image
- `aspect_ratio`: Target aspect ratio or `"auto"` (finds smallest fit)
- `resolution`: `"1K"`, `"2K"`, `"4K"`, or `"auto"`

**Outputs:**
- `pad_left`, `pad_right`, `pad_top`, `pad_bottom`: Padding values
- `target_w`, `target_h`: Target dimensions
- `aspect_ratio`, `resolution`: Resolved values (for wiring to Gemini node)

## Supported Dimensions

| API Param | 1K | 2K | 4K |
|-----------|-----|------|------|
| 21:9 | 1584x672 | 3168x1344 | 6336x2688 |
| 16:9 | 1376x768 | 2752x1536 | 5504x3072 |
| 3:2 | 1264x848 | 2528x1696 | 5056x3392 |
| 4:3 | 1200x896 | 2400x1792 | 4800x3584 |
| 5:4 | 1152x928 | 2304x1856 | 4608x3712 |
| 1:1 | 1024x1024 | 2048x2048 | 4096x4096 |
| 4:5 | 928x1152 | 1856x2304 | 3712x4608 |
| 3:4 | 896x1200 | 1792x2400 | 3584x4800 |
| 2:3 | 848x1264 | 1696x2528 | 3392x5056 |
| 9:16 | 768x1376 | 1536x2752 | 3072x5504 |

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/Vermeer-Gemini.git
```

Restart ComfyUI.

## Outpainting Workflow

```
Load Image
    │
    ▼
Nano Banana Pad Calculator (auto/auto)
    │
    ├── pad values ──► ImagePadForOutpaint (feather=0)
    │                        │
    │                        ├── padded image ──► Gemini Image Generate
    │                        │                           │
    │                        │                           ▼
    │                        │                    ┌──────────────────┐
    │                        │                    │ImageCompositeMasked│
    │                        │                    │ destination = J    │
    │                        └── mask (inverted) ─│ mask              │
    │                                             │ x = pad_left      │
    │                                             │ y = pad_top       │
    └── aspect_ratio, resolution ──► Gemini      └──────────────────┘
                                                          │
Original Image ──► SolidMask (white) ────────────────────►│ source + mask
                                                          ▼
                                                     Save Image
```

## License

MIT