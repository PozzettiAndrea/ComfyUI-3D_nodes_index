# ComfyUI_ACE-Step-zveroboy

I took the original source code from the repository [ComfyUI_ACE-Step](https://github.com/billwuhao/ComfyUI_ACE-Step) and modified it to make the model loading explicit instead of hidden.

For music generation, the original nodes from the package [ComfyUI_ACE-Step](https://github.com/billwuhao/ComfyUI_ACE-Step) are required.

This code has been imlemented to the original repository [ComfyUI_ACE-Step](https://github.com/billwuhao/ComfyUI_ACE-Step)

![comfy-ace-step](https://github.com/thezveroboy/ComfyUI_ACE-Step-zveroboy/blob/main/nodes.jpg)

# Description

This repository is an extension for ComfyUI that enables explicit loading of ACE-Step music generation models through a dedicated node. It allows flexible management of model paths and seamless integration with all generative nodes, providing enhanced control and customization for music generation workflows.

# Example Pipeline

![comfy-ace-step](https://github.com/thezveroboy/ComfyUI_ACE-Step-zveroboy/blob/main/flow.jpg)

# Quick Start

Copy the contents of this repository into the custom_nodes/ComfyUI_ACE-Step-zveroboy/ folder of your ComfyUI installation.

Ensure that the original ComfyUI_ACE-Step repository and all dependencies are properly installed.

In the ComfyUI interface, use the ACEModelLoaderZveroboy node to load your models explicitly.

Connect the output models from the loader node to the generative nodes such as ACEStepGenZveroboy, ACEStepRepaintZveroboy, and others.

Configure parameters as needed and start generating music.

