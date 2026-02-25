# ComfyUI InSPyReNet

ComfyUI node for background removal, implementing InSPyReNet

## Updates
* (2024-08-16) add to comfy registry now you can install from registry.
* (2024-08-07) add RGB image output under the `Advanced` node, you can get a white or black background image without an alpha channel.
* (2024-08-06) add model path,load model from local path
* (2024-08-06) add model under the `Advanced` node, you can choose different models(You need to download and rename the model first).
## Installation

1. Go to your `custom_nodes` folder in ComfyUI, open the terminal and run the following command:

```
git clone https://github.com/ycyy/ComfyUI-YCYY-InSPyReNet.git
```

2. To install requirements, run the following commands:

```
cd ComfyUI-YCYY-InSPyReNet
pip install -r requirements.txt
```
3. Download the model and place it in the `models/transparent-background` directory.

|model name| download link|
|--|--|
|ckpt_base.pth|https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_base.pth|
|ckpt_fast.pth|https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_fast.pth|
|ckpt_base_nightly.pth|https://github.com/plemeri/transparent-background/releases/download/1.2.12/ckpt_base_nightly.pth|


## Thanks

[john-mnz](https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg)

[RGX650](https://github.com/RGX650/ComfyUI-Inspyrenet-Rembg)