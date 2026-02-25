# ComfyUI-fal-Image

Full-featured ComfyUI custom-node pack for [fal.ai](https://fal.ai) image generation (FLUX Dev / Pro / Schnell / Kontext / Redux / Schnell-Redux) with queue polling, automatic retry, timeout handling, safety toggles and native ComfyUI image I/O.

## Features
- **Text-to-Image**: FLUX Dev, FLUX Pro v1.1, FLUX Pro New, FLUX Schnell
- **Image-to-Image**: FLUX Pro Kontext, FLUX Kontext Dev, FLUX Pro Kontext Multi, FLUX Schnell Redux (`fal-ai/flux/schnell/redux`)
- **Model Select Drop-down**: automatic model-id mapping
- **Queue Polling**: non-blocking requests with configurable timeout & retry
- **Safety Controls**: enable/disable checker + tolerance per request
- **Context Store**: pass request-ids between nodes for Kontext workflows
- **Native I/O**: transparent URL ↔ numpy array conversion (HWC, 0-1)
- **Config File**: optional INI or ENV variable for API key

## Installation
1. Clone or download this repository **into** ComfyUI's `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/Paddel87/ComfyUI_fal_image.git
   ```
2. Install Python dependencies:
   ```bash
   pip install -r ComfyUI_fal_image/requirements.txt
   ```
3. Provide your fal.ai key:
   - **Environment** (recommended):  
     Windows PowerShell: `$env:FAL_KEY="YOUR_KEY"`  
     Linux/macOS: `export FAL_KEY="YOUR_KEY"`
   - **Config file**: copy `config.example.ini` to `config.ini` and add your key.
4. Restart ComfyUI – new nodes appear under `fal.ai/Image`.

### Windows Portable / python_embeded
If you use the ComfyUI standalone build, use its bundled interpreter:
```powershell
# in ComfyUI root
cd python_embeded
python.exe -m pip install -r ../custom_nodes/ComfyUI_fal_image/requirements.txt
```

## Node Overview
| Node | Description |
|------|-------------|
| **FAL Model Select (Image)** | Pick model from drop-down; outputs model-id string. |
| **FAL Text2Image** | Prompt + size + seed + safety → IMAGE + URL + context_id. |
| **FAL Image2Image** | Reference image + prompt + strength → edited IMAGE + URL. |
| **FAL Context Store** | Stores/returns a context_id for multi-step Kontext workflows. |

## Minimal Workflows
- **T2I**: Model Select → Text2Image → Save Image  
- **I2I**: Load Image → Image2Image → Save Image  
- **Kontext**: T2I → Context Store → (optional) I2I with same context

Ready-made JSON: [`workflows/minimal_kontext_img2img.json`](workflows/minimal_kontext_img2img.json) – import via ComfyUI "Load" button.

Example workflows: [`example_workflows/`](example_workflows/)

## Advanced Settings (Text2Image / Image2Image)
| Socket | Type | Default | Note |
|--------|------|---------|------|
| `timeout_sec` | INT | 60 | Queue polling timeout (10-600). |
| `retries` | INT | 2 | Max retry attempts on transient errors. |
| `safety_mode` | ENUM | auto | `enabled` / `disabled` / `auto` (model decides). |
| `context_id` | STRING | optional | Feed previous request-id for Kontext models. |
| `seed` | INT | 0 | 0 = random. |
| `guidance` | FLOAT | 3.5 | Guidance scale (FLUX: 2-5). |
| `steps` | INT | 28 | Inference steps (FLUX Dev: 20-40). |
| `num_images` | INT | 1 | Batch size (1-4). |
| `width/height` | INT | 1024 | Output resolution (64-2048). |
| `strength` | FLOAT | 0.75 | I2I denoise strength. |

## Safety Configuration
The node exposes three safety modes: `auto`, `enabled`, `disabled`.  
- `auto` (default): lets the fal endpoint decide.  
- `enabled`: always requests safety filtering.  
- `disabled`: requests no filtering; maximum `safety_tolerance` is used.

Server-side enforcement: certain endpoints ignore the client flag and always enable filtering. When this happens the node continues generation and reports the effective mode via the `safety_applied` output field.

## Testing / Verification
Verified behaviour:
- Context-ID reuse maintains identity across runs
- Img2Img low-strength (0.2-0.4) preserves core features
- `model_id`, `seed`, `safety_applied` logged for every request

Run: `python ComfyUI_fal_image/tests/demo_flux.py` (requires `FAL_KEY`)

## Examples
### Environment Launch (Windows)
```powershell
$env:FAL_KEY="fal-..."; python main.py
```
### Python Test (outside ComfyUI)
```python
import os, sys, ComfyUI_fal_image as m
os.environ["FAL_KEY"] = "fal-..."
from ComfyUI_fal_image.fal_client import FalClient
client = FalClient(os.environ["FAL_KEY"])
payload = {"prompt":"cyberpunk cat","image_size":{"width":768,"height":512}}
result, request_id, status = client.run_with_polling("fal-ai/flux/dev", payload, 90, 2)
# request_id can be used as context_id for Kontext workflows
print(result["images"][0]["url"])
```
### Config File (`config.ini`)
```ini
[fal]
key = fal-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
timeout_sec = 120
retries = 3
```

## Troubleshooting
- **"FAL_KEY missing"** → set environment variable or create `config.ini`.  
- **Timeout errors** → increase `timeout_sec` (slow models / large batches).  
- **Queue status ERROR** → retry count exhausted; check prompt / safety flags.  
- **ImportError** → re-run `pip install -r requirements.txt` inside ComfyUI's python env.

## Links
[fal.ai – get your key](https://fal.ai/dashboard/keys)  
[ComfyUI](https://github.com/comfyanonymous/ComfyUI)  
[Repository](https://github.com/Paddel87/ComfyUI_fal_image)

Happy generating!