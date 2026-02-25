# ComfyUI Yellow Detection Plugin

这个插件为ComfyUI添加了检测图像中黄色调的功能，特别适用于皮肤色调分析和图像色彩评估。

## 功能

该插件包含两个主要节点：

1. **Detect Yellowish Image (IsYellowish)**
    - 分析图像中的黄色调
    - 使用LAB色彩空间进行准确的黄色检测
    - 提供多个分析结果：是否偏黄、黄色占比、b通道均值等

2. **Generate Yellow Heatmap (YellowHeatmap)**
    - 生成图像中黄色区域的热力图可视化
    - 支持调整阈值参数
    - 直观显示图像中黄色的分布情况

## 安装

### 方法1：通过ComfyUI Manager安装

1. 在ComfyUI中安装并启用ComfyUI Manager
2. 在Manager中搜索"Yellow Detection"并安装

### 方法2：手动安装

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/purewater2011/comfyui_color_detection.git