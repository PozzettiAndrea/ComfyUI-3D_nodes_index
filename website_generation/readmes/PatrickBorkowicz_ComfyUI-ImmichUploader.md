# ComfyUI-ImmichUploader

Upload images (directly from your graph) and files (e.g., videos written to disk) to **Immich**.  
Optionally create or reuse an **album** and add the uploaded assets to it.

- **Node name:** `Immich Upload (Image/File)`
- **Category:** `Save/Network`
- **ComfyUI compatibility:** Standard custom node (no extra server needed)

## Features

- 🚀 Upload `IMAGE` tensors from ComfyUI without saving first
- 🎞️ Upload arbitrary files by **path** (great for MP4s rendered to disk)
- 🗂️ Album support: create/find by **name**, or target a known **album ID**
- 🔐 Uses Immich **API Key** (no password sharing)

## Requirements

- ComfyUI (current rev)
- Immich server reachable from your ComfyUI host
- Immich **API Key** (Immich  → user menu → **API Keys**)
- Python packages: `requests` (and `pillow` if your build lacks it)

If you use ComfyUI’s embedded Python on Windows:

```powershell
<path-to>\ComfyUI\python_embeded\python.exe -m pip install --upgrade pip
<path-to>\ComfyUI\python_embeded\python.exe -m pip install requests
