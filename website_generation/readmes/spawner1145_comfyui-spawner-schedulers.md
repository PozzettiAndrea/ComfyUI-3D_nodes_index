# comfyui-schedulers

<p align="center">
    <img src="https://github.com/user-attachments/assets/e23eed4a-58c0-49bd-8444-ab9520a88a9f" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/aace9408-b29e-4962-b5b9-275308f86e58" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/35284db9-93e2-4a13-8660-4b5886e50877" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/39a00d69-bf9e-4bf2-909d-73baa0e5a8f6" width="150" style="margin: 5px;">
</p>

这个插件为 ComfyUI 提供了额外的调度器选项，目前包含一个smooth调度器，旨在优化生成图像的质量和一致性。
## 测试结果
使用 Neta Lumina 模型在 2048x2048 分辨率下（上方图片已压缩）对以下调度器进行了测试：

- normal（标准）
- linear_quadratic（线性二次）
- sgm_uniform（SGGM 均匀）
- smooth（本插件提供）

提示词：
```
draw by @rafaelaaa,@jvn,@nixeu,(liang xing:0.45),(atdan:0.85),(@piromizu:1.1),fov ps,tokkyu,omone hokoma agm,yoneyama mai,void 0,
1girl in a maid dress is smiling towards the viewer.her left eye is purple and her right eye is blue.she has long white hair.
极致的细节, 精彩的光影, 动态光影,
超高对比度，明暗对比
厚涂3d质感,极致的细节,精彩的光影, 动态光影,极致的景深效果,高对比度,色彩丰富,精细光线,漏光效果,焦外虚化,前景模糊,光线追踪,镜头光晕,电影级打光，超写实背景,光晕，线条清晰,明暗对比,超高清,最高画质,强光,细腻渲染,丰富的细节,高质量,写实逼真,超清晰,
masterpiece, best quality
```

反向提示词：
```
ai generated image.blurry, worst quality, low quality
```

- 步骤：28
- CFG：4.0
- 采样器：Euler A
## 安装方法
- 克隆本仓库到 ComfyUI 的custom_nodes目录下
- 重启 ComfyUI
- 在k采样器节点中找到 "调度器" 类别，即可使用新增的调度器
----------------------------------------------------------------------------------------
This plugin provides additional scheduler options for ComfyUI, currently including a smooth scheduler designed to optimize the quality and consistency of generated images.
## Test Results
I tested the following schedulers using the Neta Lumina model at 2048x2048 resolution (images above are compressed):

- normal
- linear_quadratic
- sgm_uniform
- smooth (provided by this repo)

Prompt:
```
draw by @rafaelaaa,@jvn,@nixeu,(liang xing:0.45),(atdan:0.85),(@piromizu:1.1),fov ps,tokkyu,omone hokoma agm,yoneyama mai,void 0,
1girl in a maid dress is smiling towards the viewer.her left eye is purple and her right eye is blue.she has long white hair.
极致的细节, 精彩的光影, 动态光影,
超高对比度，明暗对比
厚涂3d质感,极致的细节,精彩的光影, 动态光影,极致的景深效果,高对比度,色彩丰富,精细光线,漏光效果,焦外虚化,前景模糊,光线追踪,镜头光晕,电影级打光，超写实背景,光晕，线条清晰,明暗对比,超高清,最高画质,强光,细腻渲染,丰富的细节,高质量,写实逼真,超清晰,
masterpiece, best quality
```

Negative prompt:
```
ai generated image.blurry, worst quality, low quality
```

- Steps: 28
- CFG: 4.0
- Sampler: Euler A
## Installation
- Clone this repository into the custom_nodes directory of ComfyUI
- Restart ComfyUI
- Find the "Schedulers" category in the KSampler node to use the new schedulers
