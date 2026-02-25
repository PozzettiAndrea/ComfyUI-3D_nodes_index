# ComfyUI-Torch-Compile

ComfyUI-Torch-Compile is a set of [ComfyUI](https://www.comfy.org/) nodes for running torch.compile.

These nodes are based off of the ones found in [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes/blob/8c590fd5a023ee14b5617347567752bf62ea4cd6/nodes/model_optimization_nodes.py), but are standalone to separate torch.compile functionality from other nodes found in that pack and also fixes torch.compile for TAESD.

--- 

- [ComfyUI-Torch-Compile](#comfyui-torch-compile)
- [Install](#install)
  - [Comfy Registry](#comfy-registry)
  - [ComfyUI-Manager](#comfyui-manager)
  - [Manual](#manual)
- [Nodes](#nodes)

# Install

**Prererquisites**

- Install [comfy-cli](https://docs.comfy.org/comfy-cli/getting-started)

The recommended installation method is to use the Comfy Registry.

## Comfy Registry

These nodes can be installed via the [Comfy Registry](https://registry.comfy.org/nodes/comfyui-torch-compile).

```
comfy node registry-install comfyui-torch-compile
```

## ComfyUI-Manager

These nodes can be installed via ComfyUI-Manager in the UI or via the CLI:

```
comfy node install comfyui-torch-compile
```

## Manual

These nodes can also be installed manually by copying them into your `custom_nodes` folder and then installing dependencies:

```
cd custom_nodes
git clone https://github.com/yondonfu/ComfyUI-Torch-Compile
cd ComfyUI-Torch-Compile
pip install -r requirements.txt
```

# Nodes

| Node                       | Description                                                                                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- |
| TorchCompileLoadVAE        | Creates an optimized version of the VAE using torch.compile that will be JIT compiled during inference.        |
| TorchCompileLoadControlNet | Creates an optimized version of the ControlNet using torch.compile that will be JIT compiled during inference. |