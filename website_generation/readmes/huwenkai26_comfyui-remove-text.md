# ComfyUI Text Remove Node

这是一个ComfyUI自定义节点，用于自动检测和移除图像中的文本。

## 功能特性

- 自动检测图像中的文本区域
- 使用图像修复技术移除文本
- 支持批量处理
- 可调节检测精度和修复参数

## 安装方法

### 方法1：直接复制到ComfyUI

1. 将整个项目文件夹复制到ComfyUI的`custom_nodes`目录下
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 重启ComfyUI

### 方法2：使用ComfyUI Manager

如果你使用ComfyUI Manager，可以通过以下方式安装：
1. 在ComfyUI Manager中搜索"Text Remove Node"
2. 点击安装

## 使用方法

1. 在ComfyUI中，在节点菜单的`image/processing`分类下找到"Text Remove Node"
2. 连接图像输入
3. 调整参数：
   - `short_size`: 检测时的短边尺寸（默认960，越大检测越精确但速度越慢）
   - `inpaint_radius`: 修复半径（默认3，影响修复效果）
4. 连接输出到后续节点

## 参数说明

- **image**: 输入图像
- **short_size**: 文本检测时图像的短边尺寸，范围320-1920，步长32
- **inpaint_radius**: 图像修复的半径，范围1-10

## 技术原理

本节点使用DBNet进行文本检测，然后使用OpenCV的图像修复算法移除检测到的文本区域。

## 注意事项

- 确保`models/dbnet.onnx`模型文件存在
- 首次使用时可能需要下载模型文件
- 处理大图像时可能需要较长时间

## 依赖项

- torch>=1.9.0
- onnxruntime>=1.8.0
- opencv-python>=4.5.0
- numpy>=1.21.0
- Pillow>=8.0.0
- pyclipper>=1.3.0
- shapely>=1.7.0