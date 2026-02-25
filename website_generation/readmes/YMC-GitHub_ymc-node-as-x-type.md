<div align="center">
  <h1>ymc-node-as-x-type</h1>
  <p>
    <strong>🤖 some comfyui custom nodes to set it as known type.</strong>
  </p>

</div>

## Why

- it may be better to use to enhance [use cg-use-everywhere to link nodes in wifi](https://github.com/chrisgoringe/cg-use-everywhere) for some case.

## Features

- feat(core): node to set it as any type
- feat(core): node to set it as image type
- feat(core): node to set it as model type
- feat(core): node to set it as clip type
- feat(core): node to set it as vae type
- feat(core): node to set it as conditioning type
- feat(core): node to set it as latent type
- feat(core): node to set it as string type
- feat(core): node to set it as int type
- feat(core): node to set it as float type
- feat(core): node to set it as number type


## Nodes
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
git clone https://github.com/ymc-github/ymc-node-as-x-type
```

- **deps will be installed automatically** if deps in requirements.txt were not installed when comfyui up

## Usage

- you can find it in search box : double click + typing `set it as`
- you can find it in right mouse menu : `YMC/LINK`
- ~~you can find it in right mouse menu : `YMC/as_x_type` (as alias)~~

## Based-on

- pypi package [yors_comfyui_node_setup](https://pypi.org/project/yors_comfyui_node_setup/) -  setup comfyui custom nodes easily
- ~~pypi package [yors_comfyui_node_as_x_type](https://pypi.org/project/yors_comfyui_node_as_x_type/) - use its nodes~~
- pypi package [yors_pano_ansi_color](https://pypi.org/project/yors_pano_ansi_color/) - info msg in console with color in your comfyui custom nodes easily
- pypi package [yors_pano_zero_field](https://pypi.org/project/yors_pano_zero_field/) - set nodes input field to be HQ in your comfyui custom nodes easily 


## Published to Comfy registry

- get more details in [publish_to_comfy.yml](.github/workflows/publish_to_comfy.yml)

- [docs for publishing to comfy registey](https://docs.comfy.org/registry/overview)

- installed with comfy-cli ? `comfy node registry-install ymc-node-as-x-type`

## Author

ymc-github <ymc.github@gmail.com>

## License

MIT
