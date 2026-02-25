<div align="center">
  <h1>ymc_node_joy</h1>
  <p>
    <strong>🤖 comfyui custom nodes to caption image with joy </strong>
  </p>

</div>

<!-- inject desc here -->
<!-- inject-desc -->

## Why

<!-- inject why here -->

- use joy to caption image for aigc.
- use joy to caption image files in diretory to do sth. (eg. lora training) 


## Features

<!-- inject feat here -->
<!-- inject-features -->

## Nodes

<!-- inject node here -->
- nodes show in console:
<div style="text-align: center;">
  <img src="./shotscreen/nodes.console.png" alt="console" width="256">
  <!-- <img src="./shotscreen/nodes.right.menu.png" alt="right mouse menu" width="256"> -->
</div>

- nodes show in right mouse menu:

<div style="text-align: center;">
  <!-- <img src="./shotscreen/nodes.console.png" alt="console" width="256"> -->
  <img src="./shotscreen/nodes.right.menu.png" alt="right mouse menu" width="256">
</div>

## Install 

```bash
# cd to comfyui/custom_nodes
git clone https://github.com/ymc-github/ymc_node_joy
```
- **deps will be installed automatically** if deps in requirements.txt were not installed when comfyui up

<!-- inject model here -->

## Required Models

Essential components:
- `google/siglip-so400m-patch14-384` (Vision model)
- `unsloth/Meta-Llama-3.1-8B-bnb-4bit` or `meta-llama/Meta-Llama-3.1-8B` (LLM)
- `Joy_caption/image_adapter.pt` (Custom adapter)

```plaintext
<comfyui_root>/
├── models/
│   ├── clip/                    # SigLIP Vision Model
│   │   └── siglip-so400m-patch14-384/
│   ├── llm/                     # Llama Language Model
│   │   ├── Meta-Llama-3.1-8B-bnb-4bit/
│   │   └── Meta-Llama-3.1-8B/
│   └── Joy_caption/             # Custom Components
│       └── image_adapter.pt     # Dimension Adapter
```

### 1. SigLIP Vision Model (google/siglip-so400m-patch14-384)
**International**: https://huggingface.co/google/siglip-so400m-patch14-384  
**China Mirror**: https://hf-mirror.com/google/siglip-so400m-patch14-384

### 2. Llama Language Models
#### 4bit Quantized (unsloth/Meta-Llama-3.1-8B-bnb-4bit)
**International**: https://huggingface.co/unsloth/Meta-Llama-3.1-8B-bnb-4bit  
**China Mirror**: https://hf-mirror.com/unsloth/Meta-Llama-3.1-8B-bnb-4bit

#### Original (meta-llama/Meta-Llama-3.1-8B)
**International**: https://huggingface.co/meta-llama/Meta-Llama-3.1-8B (Access approval required)  
**China Mirror**: https://hf-mirror.com/meta-llama/Meta-Llama-3.1-8B

### 3. Image Adapter (Joy_caption/image_adapter.pt)
**International**: https://huggingface.co/spaces/fancyfeast/joy-caption-pre-alpha/tree/main/wpkklhc6  
**China Mirror**: https://www.modelscope.cn/models/fireicewolf/joy-caption-pre-alpha/files




## Usage

- you can find it in search box : double click + typing keywords (eg: `joy`, `caption`)
- you can find it in right mouse menu : `ymc/caption`
- ~~you can find it in right mouse menu : `utils/ymc/caption` (as alias)~~

## Demo

<!-- inject demo here -->
- workflow demo:
<div style="text-align: center;">
  <img src="./shotscreen/nodes.demo.png" alt="console" width="256">
</div>


## Based-on

- pypi package [yors_comfyui_node_setup](https://pypi.org/project/yors_comfyui_node_setup/) -  setup comfyui custom nodes easily
- pypi package [yors_pano_ansi_color](https://pypi.org/project/yors_pano_ansi_color/) - info msg in console with color in your comfyui custom nodes easily
- ~~pypi package [yors_pano_zero_field](https://pypi.org/project/yors_pano_zero_field/) - set nodes input field to be HQ in your comfyui custom nodes easily~~


## Published to Comfy registry

- get more details in [publish_to_comfy.yml](.github/workflows/publish_to_comfy.yml)

- [docs for publishing to comfy registey](https://docs.comfy.org/registry/overview)

- installed with comfy-cli ? `comfy node registry-install ymc_node_joy`

## Author

<!-- ymc-github <ymc.github@gmail.com> -->

name|email|desciption
:--|:--|:--
yemiancheng|<ymc.github@gmail.com>|Main developer and code maintainer|
chenxinghua|<455758525@qq.com>|Code reference from [StartHua/Comfyui_CXH_joy_caption](https://github.com/StartHua/Comfyui_CXH_joy_caption)|

## License

MIT