# ComfyUI Checkpoint Extract

Extract CLIP and VAE models from a loaded checkpoint in ComfyUI.

## Intended use

The idea of this project is to be able to separately load the clip model(s) and vae model from a checkpoint once a [TensorRT engine](https://github.com/comfyanonymous/ComfyUI_TensorRT) has been built from it. Normaly, after the engine is built, you still need the clip model and the vae model and the simplest way to get them is to load the checkpoint again. But by doing so, it will also load the original model which you don't need because you will use the compiled TensortRT engine.

This project allows to build the TensorRT engine while extracting the clip model(s) and vae model on the same pass: this way you can load the builded TensorRT engine along side with the clip and vae models without having to load the original checkpoint.

## Installation

### Comfy Manager

I have not submited this project to Comfy Manager yet. To install it with the manager, go to `Custom Nodes Manager` and use the `Install via Git URL` button in the bottom right corner. Enter the following URL:
`https://github.com/hekmon/comfyui-checkpoint-extract.git`

### Manually

On the github interface, click the green `<> Code` button and then `Download ZIP`. Extract the root folder of the zip file into your `ComfyUI/custom_nodes` directory.

## Example

In this example we will build a TensorRT version of the [DreamShaper XL v2.1 Turbo](https://civitai.com/models/112902?modelVersionId=351306) model. Download the model to the `models/checkpoints` directory to get started.

### Build & Extract

First [download](res/TensorRT%20build.json) and import the extraction and build workflow. This workflows relies on custom nodes to work:

- ComfyUI Checkpoint Extract (this one obviously)
- [ComfyUI TensorRT](https://github.com/comfyanonymous/ComfyUI_TensorRT)
- [ComfyUI-Image-Saver](https://github.com/farizrifqi/ComfyUI-Image-Saver)
- [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

![TensorRT build workflow with clip and vae on the fly extraction](res/TensorRT%20build.png)

Once the workflow is executed, move the TensorRT engine output from `output/dreamshaperXL_v21TurboDPMSDE_$dyn-b-1-4-1-h-576-1152-1152-w-1024-2048-2048_00001_.engine` to `models/tensorrt/dreamshaperXL_v21TurboDPMSDE_$dyn-b-1-4-1-h-576-1152-1152-w-1024-2048-2048_00001_.engine`.

### Use models separately

Once the CLIP and VAE models have been extracted and the TensorRT engine put in the correct folder, you can use them separately in your workflows.

![Separately loading models](res/trt_split_loading.png)

### Full workflow

If you are interested in a complete workflow with HiRes fix + 4k upscale based on this example, you can find it [here](res/DreamShaper%20XL%20Turbo%20TRT%20HiRes.json). This workflow will additionnaly need:

- The `RealESRGAN x2plus` [upscale model](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth)
- [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials)

![full workflow screenshot](res/fullworkflow.png)

## Clip models compatibility

By default the clip model saver will simply take the clip model from the connection and save it as is. However, some models/architectures might need a pre processing step before being saved. For now the following models are supported:

- **SDXL**: `clip-g` and `clip-l` are separated into separate files in order to be properly loaded by the dual clip loader comfyui node. The layers keys names are also cleaned from checkpoint bundle prefixes.

Others models will probaly needs testing and code modification to be compatible with the simple or dual clip loader.
