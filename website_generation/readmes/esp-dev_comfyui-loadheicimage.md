# ComfyUI Load Image (HEIC)

Custom node for ComfyUI that behaves like the standard **Load Image** node, but also supports `.heic` / `.heif`.

## Install

1. Copy this folder into: `D:\ComfyUI\custom_nodes\ComfyUI_LoadHEICImage\`
2. Install dependency in the same Python env as ComfyUI:

`pip install -r requirements.txt`

1. Restart ComfyUI.

## Node

- Category: **image**
- Node: **Load Image (HEIC)**
- Outputs: `IMAGE`, `MASK`

The dropdown lists images from ComfyUI `input/` folder (upload/drag&drop saves files there automatically), including `.heic`/`.heif`.

### Drag & drop note

If dropping a `.heic` shows **"Unable to find workflow..."**, it means the frontend treated the file as a workflow drop.
This extension intercepts `.heic/.heif` drops and uploads them to `input/`. For best results, drop onto the node widget, or select the **Load Image (HEIC)** node first and then drop.

## Known issues

### HEIC upload via file picker does not work

- The **"Choose file to upload"** (system file picker) is filtered to standard image extensions.
- Even if you manually pick a `.heic` (e.g. by switching the filter to *All files*), ComfyUI currently does not upload the HEIC file via that path.
- **Workaround:** upload HEIC/HEIF via **drag & drop**.

## License

MIT — see [LICENSE.txt](LICENSE.txt).
