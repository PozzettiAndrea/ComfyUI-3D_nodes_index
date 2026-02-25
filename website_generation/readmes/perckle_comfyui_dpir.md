# ComfyUI-DPIR

A dpir/DRUnet inference node for ComfyUI (https://github.com/cszn/DPIR). Runs DRUnet models loaded from the load upscale model node. 
The key difference this node has to the vanilla upscale via model node, is an added strength variable passed to the model, and handling of grayscale images for the DRUnet-gray model.

Works for these models:
drunet_color
drunet_deblocking_color
drunet_deblocking_grayscale
drunet_gray

Models can be found at: https://github.com/cszn/KAIR/releases/tag/v1.0
Safetensor conversions at: https://huggingface.co/perckle/DPIR
The sample workflow will prompt to download the safetensor conversions.

<img src="workflow.png">


## Installation
Add via manage extensions menu or ComfyUI Manager. Open the example workflow for a prompt to download the models.

or

Download this project as zip and add the unzipped folder to ComfyUI/Custom_nodes. Put drunet models in ComfyUI/models/upscale_models
