# ruucm-comfy

## Node List

### Load External Lora Model Only

Load external lora by URL.

Tested with Flux Dev model.

### Share Screen

Share screen with ComfyUI.

Base codes from [ComfyUI_zfkun](https://github.com/zfkun/ComfyUI_zfkun).

## Dev

1. Clone ComfyUI
   `git clone https://github.com/comfyanonymous/ComfyUI`
   follow the install and setup instructions of ComfyUI README
2. Clone ruucm-comfy
   in /ComfyUI folder

```
cd custom_nodes && git clone https://github.com/ruucm/ruucm-comfy.git
```

3. npm install
   inside `/ComfyUI/custom_nodes/ruucm-comfy`
   do `cd ui && npm install`
   this will install all node dependencies
4. build and run
   inside `/ComfyUI/custom_nodes/ruucm-comfy/ui`
   `npm run build --watch`
   this command will watch for your file changes and automatically rebuild, you just need to refresh to see your changes in browser everyting you change some code
5. run ComfyUI server
   inside `/ComfyUI`
   do `python main.py` or `python3 main.py` depending on your version
