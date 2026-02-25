[https://tryon.fewbox.com/](https://tryon.fewbox.com/)

- [Web App](https://github.com/FewBox/fewbox-outfit-web)

- [Comfy Gateway](https://github.com/FewBox/fewbox-comfy-gateway)

- [Comfy Node](https://github.com/FewBox/fewbox-outfit-comfyui)

# ComfyUI Workflow
> try-on.json
> Suggest use https://tryon.fewbox.com/ opensource UI and gateway
# Basic
- B: Batch Size，批次大小，一次处理的图像数量。
- H: Height，图像的垂直分辨率。
- W: Width，图像的水平分辨率。
- C: Channels, 通道数，图像的颜色通道（RGB为3，灰度为1）。
# Shape
- Image的torch.Tensor Shape是[B,H,W,C]（C=3）。保存或加载图像，需要和PIL.Image格式转换。**NOTE：出于计算效率的原因，某些pytorch使用[B,C,H,W]**
    > from PIL import Image, ImageOps
- Mask的torch.Tensor Shape是[B,H,W]。
- Latent的torch.Tensor Shape是[B,C,H,W] (C=4)。
# Mask
LoadImage节点使用图像Alpha通道（"RGBA"中的"A"）来创建Mask。Alpha通道的值被标准化为\[0,1\](torch.float32)。许多图像（如：JPEG）没有Alpha通道。LoadImage会创建一个Shape的默认蒙版[1,64,64]
Mask的Shape[B,H,W]，C是被隐藏的。经常会遇到B维度被隐藏的压缩蒙版张量[H,W]。**NOTE：要使用MASK，需要[B,H,W,C]，压缩C=1执行unsqueeze(-1)，压缩B执行unsqueeze(0)，要检查len（mask.shape）**

**sponsor**
https://www.paypal.com/paypalme/fewbox/1
