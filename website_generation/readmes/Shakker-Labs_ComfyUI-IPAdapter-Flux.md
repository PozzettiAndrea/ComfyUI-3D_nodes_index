# ComfyUI-IPAdapter-Flux

[阅读中文版](./README_zh.md)

<div align="center">
<img src=logo.jpeg width="25%"/>
</div>
<p align="center">
 👋 Join our <a href="https://discord.gg/5TuxSjJya6" target="_blank">Discord</a> 
</p>
<p align="center">
 📍 Visit <a href="https://www.shakker.ai/shakker-generator">shakker-generator</a> and <a href="https://www.shakker.ai/online-comfyui">Online ComfyUI</a> to experience the online FLUX.1-dev-IP-Adapter.
</p>

## Highlight

Please update your ComfyUI to commit `bda1482`.

## Project Updates

- **update**: ```2024/12/10```: Support multiple ipadapter, thanks to <a href="https://github.com/Slickytail">Slickytail.
- **Update**: ```2024/11/25```: Adapted to the latest version of ComfyUI. Tested on ComfyUI commit `2fd9c13`, weights can now be successfully loaded and unloaded.  
- 🌱 **Source**: ```2024/11/22```: We have open-sourced FLUX.1-dev-IP-Adapter, an IPAdapter model based on FLUX.1 dev. You can access the [ipadapter weights](https://huggingface.co/InstantX/FLUX.1-dev-IP-Adapter).

## Quick Start

### Installation

1. Navigate to `ComfyUI/custom_nodes`.  
2. Clone this repository, and the path should be `ComfyUI/custom_nodes/comfyui-ipadapter-flux/*`, where `*` represents all the files in this repository.  
3. Go to `ComfyUI/custom_nodes/comfyui-ipadapter-flux/` and run `pip install -r requirements.txt`.  
4. Download [ipadapter weights](https://huggingface.co/InstantX/FLUX.1-dev-IP-Adapter) to `ComfyUI/models/ipadapter-flux`. You can also download [google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384) to `ComfyUI/models/clip_vision` or use huggingface cache by default. 
5. Run ComfyUI after installation is complete!  

### Running the Workflow

[Reference Workflow](./workflows/ipadapter_example.json)

<div align="center">
<img src=./workflows/ipadapter_example.png width="100%"/>
</div>

[Adjust start step and end step](./workflows/ipadapter_example_start_end_percent.json)

<div align="center">
<img src=./workflows/ipadapter_example_start_end_percent.png width="100%"/>
</div>

[Use multiple ipadapter with multiple images](./workflows/multi-ipadapter_example.json)

<div align="center">
<img src=./workflows/multi-ipadapter_example.png width="100%"/>
</div>

### Online Experience

You can try the online FLUX.1-dev-IP-Adapter using [shakker-generator](https://www.shakker.ai/shakker-generator) and [Online ComfyUI](https://www.shakker.ai/online-comfyui).

## Model License

The code in this repository is released under the [Apache 2.0 License](./LICENSE).

The FLUX.1-dev-IP-Adapter model is released under the [FLUX.1 [dev] Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).
