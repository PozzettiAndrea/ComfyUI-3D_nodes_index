# ComfyUI - fal.ai Nano Banana Pro Nodes 🍌

Custom ComfyUI nodes for **Nano Banana Pro** (a.k.a. Nano Banana 2 / Gemini 3 Pro Image) via the [fal.ai](https://fal.ai) API.

Two nodes included:

| Node | Description |
|------|-------------|
| **Nano Banana Pro (Text to Image) 🍌** | Generate images from text prompts |
| **Nano Banana Pro (Image Edit) 🍌** | Edit existing images with natural language |

## Installation

1. Clone or copy this folder into your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone <this-repo> comfyui-fal-nano-banana-pro
   ```

2. Install the dependency (only `requests` — `PIL`/`torch`/`numpy` are already in ComfyUI):
   ```
   pip install requests
   ```

3. Set your fal.ai API key as an environment variable **before** launching ComfyUI:
   ```bash
   export FAL_KEY="your-fal-api-key-here"
   ```
   Get a key at: https://fal.ai/dashboard/keys

4. Restart ComfyUI. The nodes will appear under **fal.ai/Nano Banana Pro**.

---

## Safety Tolerance / Censorship — How It Works

This is likely the reason you're here, so here's the full picture:

### Text-to-Image (`fal-ai/nano-banana-pro`)
- **No `safety_tolerance` parameter is exposed** on this endpoint.
- Content filtering is applied server-side by a combination of Google's Gemini model safety systems and fal.ai's infrastructure.
- You **cannot** reduce or disable filtering for text-to-image via the API.
- If a prompt is filtered, you'll typically get an empty `images` array or an error.

### Image Editing (`fal-ai/nano-banana-pro/edit`)
- **Exposes `safety_tolerance`** as an API-only parameter (not in fal.ai's playground UI).
- Scale of **1 to 6**:
  - `1` = Most strict (blocks the most content)
  - `6` = Least strict (blocks the least content)
  - Default = `4`
- This is included as a dropdown in the ComfyUI node.
- **Important:** Even at level 6, the underlying Gemini model still has Google's built-in safety filters. The `safety_tolerance` parameter adjusts fal.ai's additional filtering layer on top of the model — it does not remove the model's own refusals.

### What this means in practice
- Setting `safety_tolerance` to `6` on the edit node will let more borderline content through fal.ai's filter, but Google's model-level safety can still refuse to generate certain content.
- The text-to-image node has no equivalent knob — you're subject to whatever the default filtering is.
- If you get empty results, check the `description` output — it sometimes contains the model's refusal reason.

---

## Node Parameters

### Text to Image
| Parameter | Type | Default | Notes |
|-----------|------|---------|-------|
| prompt | string | — | Required |
| num_images | int | 1 | 1–4 |
| aspect_ratio | enum | 1:1 | 10 options |
| output_format | enum | png | png/jpeg/webp |
| resolution | enum | 1K | 1K/2K/4K (4K costs 2x) |
| seed | int | -1 | -1 = random |
| limit_generations | bool | false | Force exactly 1 image per generation round |
| enable_web_search | bool | false | Let the model search the web (+$0.015) |
| timeout | int | 300 | Max seconds to wait |

### Image Edit
All of the above, plus:
| Parameter | Type | Default | Notes |
|-----------|------|---------|-------|
| image | IMAGE | — | Required, primary input image |
| image_2 | IMAGE | — | Optional second reference image |
| image_3 | IMAGE | — | Optional third reference image |
| safety_tolerance | enum | 4 | 1 (strict) → 6 (permissive). API-only. |

---

## Pricing (fal.ai)
- **$0.15 per image** at 1K/2K
- **$0.30 per image** at 4K
- **+$0.015** if web search is enabled

---

## License
MIT
