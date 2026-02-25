# ComfyUI — Compressed Metadata

Load & save ComfyUI workflows embedded in image metadata — with optional zlib+base64 compression for JPEG/WEBP — and batch convert folders.  
PNG drops still work natively; JPEG/WEBP with compressed workflows are handled by this extension.

## Features
- **Drag & Drop to Canvas**
  - If a dropped **JPEG/WEBP** contains `UserComment="COMPRESSED:<base64>"`, the workflow is decompressed and loaded.
  - If a dropped **PNG** contains the standard ComfyUI workflow text chunk, ComfyUI’s **native** loader handles it (we do not block it).
- **Nodes**
  - **SaveImageCompressed** — save images embedding compressed workflow to EXIF (JPEG) or alongside (WEBP).
  - **ConvertToCompressed** — batch convert a folder to JPEG/WEBP and embed compressed workflow where available.
  - **ExtractWorkflowsToJSON** — scan a folder and dump embedded workflows to `.json` files.
- **Frontend script**
  - Installs a minimal drop handler that only intercepts when a compressed EXIF workflow is detected; otherwise it defers to ComfyUI’s native behavior.

## Install
```bash
cd <Your ComfyUI folder>/custom_nodes
git clone https://github.com/<YOUR_GH_USER>/comfyui-compressed-metadata.git
```

Dependencies (installed automatically by most managers):
```bash
pip install -r comfyui-compressed-metadata/requirements.txt
```

## Usage
- **Saving**: use the “Save Compressed Image” node to save JPEG/WEBP with compressed workflow data.
- **Loading (drop)**:
  - Drop a **JPEG/WEBP** you saved with this node → workflow opens from compressed EXIF.
  - Drop a **standard PNG** created by core ComfyUI → workflow opens via native loader (unchanged).
- **Batch**: use “Convert to Compressed Image” to process folders; use “Extract Workflows to JSON” to export embedded workflows.

## Known Notes
- Some viewers strip EXIF; keep the original files if you rely on embedded workflows.
- For very large workflows, prefer **WEBP** or lower compression levels to stay within metadata limits on certain apps.

## License
MIT (see `LICENSE`)

## Credits
- Built for ComfyUI.
- Uses `piexif`, `Pillow` and a tiny frontend script (no bundler required).
