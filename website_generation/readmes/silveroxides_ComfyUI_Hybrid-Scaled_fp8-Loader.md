# ComfyUI_Hybrid-Scaled_fp8-Loader
Custom Loader for scaled_fp8 models with hybrid precision layers

### In order to load Chroma1-HD-fp8_scaled_original_hybrid large or small models you will need to use 
### this custom node in place of "Load Diffusion Model" node.
### I currently recommend using "small_rev3". large model can only use the pruned flash-heun LoRAs.
### Note: The visuals of the node has changed. But it is intuitive enough to understand still.
<img src="https://huggingface.co/silveroxides/Chroma1-HD-fp8-scaled/resolve/main/scaled_fp8_hybrid_loader.png" height=341 width=692>

### The fp8_scaled model without hybrid in name can be loaded normally without issue. 
