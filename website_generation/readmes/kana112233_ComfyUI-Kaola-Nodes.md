# ComfyUI-Kaola-Nodes

[English](#english) | [中文](#中文)

---

## English

A collection of ComfyUI custom nodes for image manipulation.

### Included Nodes

1. **Kaola Image Expand**: Image expansion (outpainting) with real-time preview.
2. **Kaola Image Scale By Aspect Ratio**: Advanced scaling with aspect ratio control, letterboxing, and cropping.
3. **Kaola Color Constant**: Helper node to provide hex color values using a color picker.

### Features

#### Kaola Image Expand
- **Real-time Preview**: Instant preview when adjusting expansion parameters.
- **Directional Control**: Independent control for 4 directions.
- **Fill Modes**: Solid color, edge color, mirror, blur.

#### Kaola Image Scale By Aspect Ratio
- **Aspect Ratio Control**: Scale images to common ratios (16:9, 4:3, etc.) or custom ones.
- **Fit Modes**:
    - `stretch`: Force resize.
    - `crop`: Center crop to target AR.
    - `letterbox`: Fit within target AR (black bars).
- **Background Color**: Customizable letterbox padding color.
- **Round to Multiple**: Ensure output dimensions are multiples of 8, 64, etc. (useful for Diffusion).

#### Kaola Color Constant
- **Color Picker**: Visual color selector to generate Hex strings.

### Installation

1. Navigate to your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/kana112233/ComfyUI-Kaola-Nodes.git
```

3. Restart ComfyUI

---

## 中文

ComfyUI 图像处理自定义节点合集。

### 包含节点

1. **Kaola Image Expand (考拉扩图)**: 带实时预览的图像扩展节点。
2. **Kaola Image Scale By Aspect Ratio (考拉比例缩放)**: 支持高级比例控制的缩放节点。
3. **Kaola Color Constant (考拉颜色选择器)**: 提供颜色选择功能的辅助节点。

### 功能特性

#### Kaola Image Expand (扩图)
- **实时预览**: 调整参数时立即查看效果。
- **方向控制**: 上下左右独立控制。
- **填充模式**: 纯色、边缘色、镜像、模糊。

#### Kaola Image Scale By Aspect Ratio (比例缩放)
- **比例控制**: 支持常用比例 (16:9, 4:3 等) 和自定义比例。
- **适配模式**:
    - `stretch` (拉伸): 强制缩放到目标尺寸。
    - `crop` (裁剪): 保持比例中心裁剪。
    - `letterbox` (信箱): 保持比例留黑边（支持自定义背景色）。
- **背景颜色**: Letterbox 模式下的填充颜色。
- **倍数取整**: 确保输出尺寸是 8, 64 等倍数（SD 模型必备）。

#### Kaola Color Constant (颜色选择)
- **颜色选择器**: 可视化选择颜色并输出 HEX 代码。

### 安装方法

1. 进入 ComfyUI 自定义节点目录：
```bash
cd ComfyUI/custom_nodes/
```

2. 克隆本仓库：
```bash
git clone https://github.com/kana112233/ComfyUI-Kaola-Nodes.git
```
*(注意：如果之前的文件夹是 kaola_nodes，建议重命名为 ComfyUI-Kaola-Nodes)*

3. 重启 ComfyUI

## Version History

- v1.0 - Basic expansion functionality
- v1.1 - Added real-time preview
- v1.2 - Added Kaola Image Scale By Aspect Ratio & Color Constant
