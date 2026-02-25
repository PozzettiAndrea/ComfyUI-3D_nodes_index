# Draw Tools for ComfyUI

一组针对图像处理的ComfyUI自定义节点集合。

## 功能节点

### Detect Inner Box

- 检测掩码中不与边缘相连的白色区域
- 返回区域最小外接矩形的宽度和高度
- 支持设置阈值和连通性参数
- 适用于检测图像中孤立区域的尺寸

### Paste Into Frame

- 根据掩码中央矩形尺寸缩放内容图像
- 使用原始掩码将内容贴进框架图像
- 支持保持内容图像的原始宽高比
- 自动处理透明度（如果框架图像有alpha通道）

## 安装

```bash
cd custom_nodes
git clone https://github.com/Ky11le/draw_tools
cd draw_tools
pip install -r requirements.txt
```

## 依赖要求

本插件需要以下依赖项：
- opencv-python >= 4.5.0
- torch >= 1.7.0
- numpy >= 1.19.0

## 使用方法

节点会在ComfyUI的"DrawTools"类别下出现。

### Detect Inner Box 参数

- `mask_image`: 输入掩码图像
- `threshold`: 二值化阈值（0.0-1.0）
- `connectivity`: 连通性（4或8）

### Paste Into Frame 参数

- `frame_image`: 框架图像（将作为背景）
- `content_image`: 内容图像（将被贴入框架）
- `mask_image`: 掩码图像（决定贴图区域）
- `threshold`: 二值化阈值（0.0-1.0）
- `connectivity`: 连通性（4或8）
- `keep_aspect`: 是否保持内容图像的原始宽高比 