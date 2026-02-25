# ComfyUI-BiRefNet-TRT

## Introduction

This repository wraps the latest BiRefNet model as ComfyUI nodes. Compared to the previous model, the latest model offers higher and better matting accuracy.Support TensorRT.

## Installation

#### Method  1:

1. Go to comfyUI custom_nodes folder, `ComfyUI/custom_nodes/`
2. `https://github.com/jesenzhang/ComfyUI-BiRefNet-TRT.git`
3. `cd ComfyUI-BiRefNet-TRT`
4. `pip install -r requirements.txt`
5. restart ComfyUI

#### Method 2:

Directly download the node source package, then extract it into the custom_nodes directory, and finally restart ComfyUI.

#### Method 3：

Install through ComfyUI-Manager by searching for '`ComfyUI-BiRefNet-TRT`' and installing it.

### Requirements

Repository:https://github.com/pythongosssss/ComfyUI-Custom-Scripts

## Usage

The demo workflow placed in `ComfyUI-BiRefNet-TRT/workflow`

Choose a type of load_mode,the default is local,means models should have beed downloaded to the local,placed in ComdyUI/models/BiRefNet folder.

Use pretrained models will download from https://huggingface.co/ZhengPeng7/BiRefNet/tree/main

TRT weights should be converted with ComfyUI_TensorRT and placed in ComdyUI/models/BiRefNet folder.

![](workflow\local_trt.png)

## Thanks

Thanks to BiRefNet repo owner  [ZhengPeng7/BiRefNet](https://github.com/zhengpeng7/birefnet)

Some of the code references [MoonHugo/ComfyUI-BiRefNet-Hugo](https://github.com/MoonHugo/ComfyUI-BiRefNet-Hugo)
