[中文说明](https://github.com/leizingyiu/yiu_comfy_nodes/blob/main/README.md) | [English Version readme](https://github.com/leizingyiu/yiu_comfy_nodes/blob/main/README_en.md)


# yiu_comfy_nodes

这是我在用comfyUI的过程中，频繁用到的小工具，希望对你也有用。

## 介绍

当前几个节点组合起来最常见的引用场景：
- 使用产品图以及环境结构参考图，在生成电商图片时，更可控的调整产品位置
- 使用产品图，以及模特图，合并产品到模特手上或身上，喂给kontext生图

## 节点列表

- **yiu_fit_itm_2_msk**

    将图1物品放置在图2的遮罩中。<BR>
    输入：物品图片、遮罩，背景图片，背景图片上指示物品位置尺寸的遮罩（可在加载图像节点中手动绘制）<BR>
    输出：缩放移动在背景遮罩中的：物品图片（透明背景）、物品图片的遮罩、物品图片（背景色）、物品图片（原背景）


- **yiu_img_cnv_placer**

    将图片放置在指定分辨率的画布中，可自定义图片在画布中的缩放以及位置。<BR>
    输入：图片，以及图片的遮罩<BR>
    输出：放置在画布中的图片、放置在画布中的原遮罩，用于扩图的遮罩

- **yiu_itm_cropper**

    将图片以及遮罩，按照抠图结果，进行裁切。<BR>
    输入：原图图片、原图遮罩，抠图结果图片，抠图结果遮罩<BR>
    输出：根据抠图结果遮罩，并根据padding、x_pos、y_pos调整，得到的裁切图片、遮罩

## 安装方法

### 方法 1 

直接在 comfyUI 的 manager 中搜索 yiu_comfy_nodes 安装

### 方法 2

下载本仓库中的 yiu_comfy_nodes 文件夹，将文件夹复制到 comfyUI 的 custom_nodes 文件夹中。

## 使用说明

请参考仓库中的 DEMO 工作流
![yiu_comfy_nodes_demo](https://raw.githubusercontent.com/leizingyiu/yiu_comfy_nodes/refs/heads/main/yiu_demo_workflow.png "这是一个 Demo 工作流图")


## 许可协议

本项目遵循 AGPL 协议，详情请参阅 LICENSE 文件。

## 致谢

感谢 ComfyUI 团队及社区的支持！
