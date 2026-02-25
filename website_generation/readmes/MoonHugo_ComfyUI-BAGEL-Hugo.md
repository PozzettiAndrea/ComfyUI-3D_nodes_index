<h1 align="center">ComfyUI-BAGEL-Hugo</h1>

<p align="center">
    <br> <font size=5>中文 | <a href="README_EN.md">English</a></font>
</p>


## 介绍

本仓库将BAGEL模型封装为ComfyUI节点来使用，包含图像编辑、图像反推功能，但是没有文生图功能。<br>

## 安装 

#### 方法1:

1. 进入节点目录, `ComfyUI/custom_nodes/`
2. `git clone https://github.com/MoonHugo/ComfyUI-BAGEL-Hugo.git`
3. `cd ComfyUI-BAGEL-Hugo`
4. `pip install -r requirements.txt`
5. 重启ComfyUI

#### 方法2:
直接下载节点源码包，然后解压到custom_nodes目录下，最后重启ComfyUI

#### 方法3：
通过ComfyUI-Manager安装，搜索“ComfyUI-BAGEL-Hugo”进行安装

## 节点参数说明

![plot](./assets/4.png)

**model_function**: 模型功能，分为图像编辑、提示词反推功能，即"imageEdit", "reverse"，但是没有文生图功能。<br>
**image**: 输入图片。<br>
**prompt**: 提示词。<br>
**seed**: 整数类型，设置种子值来确保结果的可重复性，取值范围在0到2**32 - 1之间。<br>
**cfg_text_scale**: 控制模型遵循文本提示词的强度。 1.0 表示禁用文本引导。典型范围： 4.0–8.0 。<br>
**cfg_img_scale**: 控制模型保留输入图像细节的程度。 1.0 表示禁用图像引导。典型范围： 1.0–2.0 。<br>
**cfg_interval_start**: CFG作用的起始时间步。0.0表示从第一步开始应用CFG。1.0表示在最后一步应用CFG，默认值：0.0。<br>
**cfg_interval_end**: CFG作用的结束时间步。0.0表示在第一步结束时应用CFG。1.0表示在最后一步结束时应用CFG，默认值：1.0。<br>
**timestep_shift**: 调整去噪步骤的分布比例。数值越高，初始阶段分配更多步骤（影响整体布局）；数值越低，后期阶段分配更多步骤（提升细节质量）。<br>
**num_timesteps**: 总去噪步数，默认值： 50 。<br>
**cfg_renorm_min**: CFG-Renorm 的最小值。设为 1.0 时禁用重归一化（renorm）。默认值：0。<br>
**cfg_renorm_type**: CFG-Renorm 的类型，有global、channel、text_channel三个选项。global 在所有标记（tokens）和通道（channels）上进行归一化（文本到图像 T2I 的默认方法）；channel 对每个标记（token）跨通道进行归一化。；text_channel 类似通道（channel）方式，但仅应用于文本条件（适合图像编辑，但可能导致模糊）。如果编辑后的图像显得模糊，请尝试使用全局（global）CFG-Renorm、降低 cfg_renorm_min 或降低 cfg_scale的值。<br>
**show_thinking**: 是否显示思考过程。启用此选项可以在推理过程中显示模型的思考过程。<br>
**text_temperature**: 控制文本生成中的随机性。较低的值会使输出更确定，较高的值会使输出更随机。<br>
**max_think_token_n**: 思考过程中生成的最大token数。较高的值可能会导致更长的思考过程，但也会增加计算负担。<br>
**do_sample**: 是否在文本生成中使用采样。启用此选项可以使生成的文本更加多样化。<br>
**precision**: 选择模型的精度。BFloat16 提供更高的精度，但需要更多的 GPU 内存。DFloat11 是一种更节省内存的精度，体积比原始 BFloat16 模型缩小 32%，却能生成完全一致的输出结果，并在 GPU 上高效运行。<br>
**offload_buffers**: 指将数据从GPU内存卸载到CPU内存或者硬盘。启用此选项可以节省GPU内存，但可能会导致推理速度变慢。<br>
**unload_model**: 是否在推理后卸载模型。启用此选项可以释放GPU内存，但会导致下次推理时重新加载模型。<br>
___

## 使用

首先需要手动下载模型放到models/bagel目录下，模型下载地址：[BAGEL-7B-MoT](https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT)、[BAGEL-7B-MoT-DF11](https://huggingface.co/DFloat11/BAGEL-7B-MoT-DF11)<br/>

![](./assets/3.png)


___
工作流imageEdit.json的使用<br/>

![plot](./assets/1.png)

___
工作流image2text.json的使用<br/>

![plot](./assets/2.png)

___
## 社交账号
- Bilibili：[我的B站主页](https://space.bilibili.com/1303099255)

## 感谢

感谢Bagel仓库的所有作者 [ByteDance-Seed/Bagel](https://github.com/ByteDance-Seed/Bagel)

## 关注历史

[![Star History Chart](https://api.star-history.com/svg?repos=MoonHugo/ComfyUI-BAGEL-Hugo&type=Date)](https://star-history.com/#MoonHugo/ComfyUI-BAGEL-Hugo&Date)