# ComfyUI- CCSR upscaler node
## Update:

Models now available here in safetensors format here, by default fp16 is used:

https://huggingface.co/Kijai/ccsr-safetensors/tree/main

There's also a new node that autodownloads them, in which case they go to `ComfyUI/models/CCSR`

![image](https://github.com/kijai/ComfyUI-CCSR/assets/40791699/f7301285-1753-49f7-9828-c8273ee06bb9)

Model loading is also twice as fast as before, and memory use should be bit lower.


The old node simply selects from checkpoints -folder, for backwards compatibility I won't change that.

https://github.com/kijai/ComfyUI-CCSR/assets/40791699/a22306f0-90a4-4a3e-97de-1f795fa8decd

![image](https://github.com/kijai/ComfyUI-CCSR/assets/40791699/5ea77221-441d-41b2-8ede-50c4fd1cfa4f)

This is a simple wrapper node for https://github.com/csslc/CCSR

As such, it's NOT a proper native ComfyUI implementation, so not very efficient and there might be memory issues, tested on 4090 and 4x upscale tiled worked well.



Original model:
The model (https://drive.google.com/drive/folders/1jM1mxDryPk9CTuFTvYcraP2XIVzbPiw_?usp=drive_link) goes to `ComfyUI/models/checkpoints`

I suggest installing with the comfyui-manager:
![image](https://github.com/kijai/ComfyUI-CCSR/assets/40791699/b7214913-4789-4da2-b05a-4ff18e6619b2)

