# ComfyUI LatentGC_Aggressive

Contains a single node for ComfyUI (https://github.com/comfyanonymous/ComfyUI) that on being hit empties cache, runs GC and unloads models from VRAM. Useful to put between different stages of the workflow in low VRAM scenarios. Suggested use is before/after sampler, before VFI, etc. The performance impact of unloading models from VRAM and, in some cases, forcing an immediate re-load for the next node use, appears negligible on this system.

Thanks to:
https://github.com/ntdviet/comfyui-ext
https://github.com/yolain/ComfyUI-Easy-Use