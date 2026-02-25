# ComfyUI-MaxTools

A small collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## Install

Clone into your ComfyUI `custom_nodes` folder:

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/maximilianwicen/ComfyUI-MaxTools.git
```

Restart ComfyUI.

## Nodes

- **Max Quick Image Size** (`MaxQuickImageSize`): useful for Image-to-Image or Image-to-Video workflows; outputs `new_width`/`new_height` by selecting square/landscape/portrait presets based on aspect ratio. Provide `width`/`height`, or connect an `IMAGE` to infer dimensions.
