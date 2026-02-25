# Floyo FLUX.2 [pro] Custom Node

Custom ComfyUI node for Floyo that wraps the Black Forest Labs FLUX.2 **[pro]** API. URL-first (no local file paths): you pass URLs and get back a signed output URL for downstream Floyo nodes to download.

## Features
- Text-to-image generation with width/height, seed, safety tolerance, and output format controls.
- Image editing with multi-reference support (`input_image` + up to 7 extra refs).
- Clear URL-only inputs/outputs to match Floyo’s storage pipeline.
- Configurable API key via `config.ini` or `BFL_API_KEY` env var.
- Built-in polling with basic error handling and timeouts.

## Installation
Repo layout (mirrors Floyo Seed API style):
- `nodes/` → node code and helpers
- `config.ini` → API key placeholder
- `requirements.txt`
- `README.md`, `__init__.py`

1. Place this repository folder (e.g., `Flux2-Pro`) into `ComfyUI/custom_nodes/`.
2. Install dependencies:
   ```bash
   cd Flux2-Pro   # or your folder name under custom_nodes
   pip install -r requirements.txt
   ```
3. Add your key to `config.ini` or export it:
   ```ini
   [API]
   BFL_API_KEY = <your_real_key>
   BFL_BASE_URL = https://api.bfl.ai/v1/flux-2-pro
   BFL_FLEX_BASE_URL = https://api.bfl.ai/v1/flux-2-flex
   ```
   ```bash
   export BFL_API_KEY=<your_real_key>
   export BFL_BASE_URL=https://api.bfl.ai/v1/flux-2-pro
   export BFL_FLEX_BASE_URL=https://api.bfl.ai/v1/flux-2-flex
   ```
4. Restart ComfyUI.

## Nodes and I/O
### FLUX.2 [pro] Text-to-Image (`Flux2ProTextToImage`)
- **Inputs (required):** `prompt`, `width`, `height`
- **Inputs (optional):** `seed` (`-1` = random), `safety_tolerance` (0-6), `output_format` (`jpeg`/`png`)
- **Output:** `image` (IMAGE tensor ready for Save Image)

### FLUX.2 [pro] Image Edit (`Flux2ProImageEdit`)
- **Inputs (required):** `prompt`, `input_image` (IMAGE tensor)
- **Inputs (optional):** `input_image_2` … `input_image_8` (IMAGE tensors, keep total refs <= 8). `width`, `height` (0 = match input), `seed` (`-1` = random), `safety_tolerance`, `output_format`
- **Output:** `image` (IMAGE tensor ready for Save Image)

### FLUX.2 [flex] Text-to-Image (`Flux2FlexTextToImage`)
- **Inputs (required):** `prompt`, `width`, `height`, `guidance` (1.5–10), `steps` (1–50)
- **Inputs (optional):** `seed` (`-1` = random), `safety_tolerance`, `output_format`
- **Output:** `image` (IMAGE tensor)

### FLUX.2 [flex] Image Edit (`Flux2FlexImageEdit`)
- **Inputs (required):** `prompt`, `input_image` (IMAGE tensor)
- **Inputs (optional):** `input_image_2` … `input_image_10` (IMAGE tensors, keep total refs <= 10), `width`, `height`, `seed`, `safety_tolerance`, `output_format`, `guidance`, `steps`
- **Output:** `image` (IMAGE tensor)

### FLUX.2 [pro] Image Edit (`Flux2ProImageEdit`)
- **Inputs (required):** `prompt`, `input_image` (IMAGE tensor)
- **Inputs (optional):** `input_image_2` … `input_image_8` (IMAGE tensors, keep total refs <= 8). `width`, `height` (0 = match input), `seed` (`-1` = random), `safety_tolerance`, `output_format`
- **Output:** `image` (IMAGE tensor ready for Save Image)

## Usage Notes
- The returned URL expires quickly; run your Floyo download/output node immediately after this node.
- API statuses handled: `Ready`, `Pending`, and error/moderation states. Failures return an error string in the node output.
- Keep total reference images within FLUX.2 [pro] limits (max 8 images, 9MP total). Width/height must be multiples of 16; `0` uses the input image dimensions for edits. Max resolution 4MP (e.g., 2048x2048).
- When connecting ComfyUI image tensors, the node auto-converts to base64. If you prefer URLs, fill the URL fields instead.

## API Reference
- Endpoint: `https://api.bfl.ai/v1/flux-2-pro`
- Docs: https://docs.bfl.ai/quick_start/introduction
