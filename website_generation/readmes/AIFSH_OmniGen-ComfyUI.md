# OmniGen-ComfyUI

A custom node for [OmniGen](https://github.com/VectorSpaceLab/OmniGen), you can find [workflow here](./doc/)

Automatic downloading of the model is no longer performed, since now you have a loader node which will allow for finetunes, merges, as well as fp8 dtypes.

## How to Install

1. Create an OmniGen folder the models directory in /ComfyUI/models/Omnigen (this has moved from the older folder location)
2. Within the /ComfyUI/models/Omnigen download all of the files from https://huggingface.co/Shitao/OmniGen-v1 into its own folder.

You can also download the models with GIT. First do **GIT LFS** and afterwards do **git clone https://huggingface.co/Shitao/OmniGen-v1**. This can take awhile, and may appear as if it is doing nothing for a bit.

3. Install **OmniGen-ComfyUI** by **AIFSH** in Comfy Manager. Be sure to select the correct one. Many clones with less functionality have appeared since.

## Example
In the prompt text, you only need to use `image_1` (for image 1), instead of needing to use `<img><|image_1|></img>`.
|text|image_1|image_2|image_3|out_img|
|--|--|--|--|--|
|`A curly-haired man in a red shirt is drinking tea.`|--|--|--|![](./doc/ComfyUI_temp_mdplu_00001_.png)|
|`The woman in image_1 waves her hand happily in the crowd`|![](./doc/zhang.png)|--|--|![](./doc/ComfyUI_temp_pphmf_00001_.png)|

## Tips
For out of memory or time cost, you can refer to [inference.md#requiremented-resources](https://github.com/VectorSpaceLab/OmniGen/blob/main/docs/inference.md#requiremented-resources) to select a appropriate setting.

```
text2img Example Prompt: "A white cat resting on a picnic table."
Image Editing Example Prompt: "image_1 The umbrella should be red."
Segmentation Example Prompt: "Find lamp in the picture image_1 and color them blue."
Try-On Example Prompt:"image_1 wears image_2."
Pose Example Prompt: "Detect the skeleton of human in image_1."
```
## Disclaimer / 免责声明
We do not hold any responsibility for any illegal usage of the codebase. Please refer to your local laws about DMCA and other related laws. 我们不对代码库的任何非法使用承担任何责任. 请参阅您当地关于 DMCA (数字千年法案) 和其他相关法律法规.
