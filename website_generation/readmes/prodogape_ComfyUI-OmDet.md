# ComfyUI-OmDet
This node is mainly based on [OmDet](https://github.com/om-ai-lab/OmDet) for object detection, and it outputs related images, masks, and Labelme JSON information.

![image](/docs/workflow.png)

# README
- [English](README.md)
- [简体中文](readme/README.zh_CN.md)

# NODES
|name                          |description                                        |
|------------------------------|---------------------------------------------------|
|Apply OmDet                   |Apply OmDer model, supports automatic download     |

# INSTALL
you need to install the following dependencies:

```
pip install -r requirements.txt
```

# MODEL
This node supports automatic model downloads.

```
ComfyUI
    models
        OmDet
            OmDet-Turbo_tiny_SWIN_T.pth
            ViT-B-16.pt
```
