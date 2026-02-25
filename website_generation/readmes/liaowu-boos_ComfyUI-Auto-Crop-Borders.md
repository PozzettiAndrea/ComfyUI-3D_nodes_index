# ComfyUI Auto Crop Borders

[English](#english) | [中文](#中文)

---

## English

### Overview

A ComfyUI custom node that automatically detects and crops continuous black borders from images. This plugin intelligently identifies the content area and removes unnecessary black edges, perfect for cleaning up screenshots, scanned documents, or any images with unwanted borders.

### Features

- 🎯 **Automatic Detection**: Intelligently detects black borders using grayscale analysis
- ✂️ **Precise Cropping**: Calculates the minimum bounding box of non-black content
- 🎛️ **Flexible Control**: Adjustable threshold and padding parameters
- 🔄 **Dual Output**: Returns both cropped image and corresponding mask
- 🛡️ **Safe Processing**: Handles edge cases like all-black images gracefully

### Node Information

**Node Name**: Auto Crop Black Borders  
**Category**: Design Tools/Image  
**Inputs**: IMAGE, threshold (INT), padding (INT)  
**Outputs**: IMAGE, BOX_MASK (MASK)

### Parameters

#### `image` (IMAGE)
- **Type**: IMAGE (ComfyUI image format)
- **Description**: The input image to be processed

#### `threshold` (INT)
- **Type**: Integer
- **Range**: 0 - 255
- **Default**: 10
- **Description**: Pixel brightness threshold for black detection. Pixels with values below this threshold are considered black. Lower values detect only pure black, while higher values include dark gray pixels.
  - `0`: Only pure black pixels (RGB: 0,0,0)
  - `10`: Near-black pixels (recommended for most cases)
  - `50`: Dark gray pixels
  - `100+`: Medium gray and darker

#### `padding` (INT)
- **Type**: Integer
- **Range**: -1000 to 1000
- **Default**: 0
- **Description**: Adjusts the crop boundary after detection
  - **Positive values** (e.g., `10`): Expand outward, keeping some black border
  - **Zero** (`0`): Crop exactly at the detected boundary
  - **Negative values** (e.g., `-10`): Shrink inward, removing edge noise/artifacts

**Use Cases for Padding**:
- Positive padding: Keep a small border for aesthetic purposes
- Negative padding: Remove residual noise or compression artifacts at edges

### Installation

#### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Auto Crop Borders"
3. Click Install

#### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/liaowu/comfyui-auto-crop-borders.git
   ```

3. Install dependencies:
   ```bash
   cd comfyui-auto-crop-borders
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

### Usage Example

1. Add the "Auto Crop Black Borders" node to your workflow
2. Connect an image to the `image` input
3. Adjust parameters:
   - Set `threshold` to define what counts as "black"
   - Set `padding` to fine-tune the crop boundary
4. The node outputs:
   - **IMAGE**: The cropped image
   - **BOX_MASK**: A mask showing the cropped region (white) vs removed area (black)

### Algorithm

1. **Grayscale Conversion**: Convert input image to grayscale for analysis
2. **Black Pixel Detection**: Identify all pixels with brightness > threshold
3. **Bounding Box Calculation**: Find the minimum rectangle containing all non-black pixels
4. **Padding Application**: Adjust boundaries based on padding value
5. **Cropping**: Extract the final region and generate corresponding mask

### Requirements

- ComfyUI
- PyTorch
- NumPy

### License

MIT License - See [LICENSE](LICENSE) file for details

### Contributing

Issues and pull requests are welcome!

### Author

**liaowu**

---

## 中文

### 概述

一个 ComfyUI 自定义节点，用于自动检测并裁切图片中的连续黑边。该插件能够智能识别图片内容区域，去除不必要的黑色边缘，非常适合清理截图、扫描文档或任何带有多余边框的图片。

### 功能特点

- 🎯 **自动检测**：使用灰度分析智能检测黑边
- ✂️ **精确裁切**：计算非黑色内容的最小外接矩形
- 🎛️ **灵活控制**：可调节阈值和边距参数
- 🔄 **双重输出**：同时返回裁切后的图片和对应遮罩
- 🛡️ **安全处理**：优雅处理全黑图片等边界情况

### 节点信息

**节点名称**：Auto Crop Black Borders  
**分类**：Design Tools/Image  
**输入**：IMAGE, threshold (INT), padding (INT)  
**输出**：IMAGE, BOX_MASK (MASK)

### 参数说明

#### `image` (IMAGE)
- **类型**：IMAGE（ComfyUI 图片格式）
- **说明**：待处理的输入图片

#### `threshold` (INT)
- **类型**：整数
- **范围**：0 - 255
- **默认值**：10
- **说明**：黑色检测的像素亮度阈值。低于此值的像素被视为黑色。较低的值只检测纯黑色，较高的值会包含深灰色像素。
  - `0`：仅纯黑色像素（RGB: 0,0,0）
  - `10`：接近黑色的像素（推荐用于大多数情况）
  - `50`：深灰色像素
  - `100+`：中灰色及更深的颜色

#### `padding` (INT)
- **类型**：整数
- **范围**：-1000 到 1000
- **默认值**：0
- **说明**：在检测后调整裁切边界
  - **正数**（如 `10`）：向外扩展，保留一些黑边
  - **零** (`0`)：精确在检测边界处裁切
  - **负数**（如 `-10`）：向内收缩，去除边缘噪点/伪影

**Padding 使用场景**：
- 正数边距：为美观保留小边框
- 负数边距：去除边缘残留噪点或压缩伪影

### 安装方法

#### 方法 1：ComfyUI Manager（推荐）
1. 打开 ComfyUI Manager
2. 搜索 "Auto Crop Borders"
3. 点击安装

#### 方法 2：手动安装
1. 进入 ComfyUI 自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. 克隆此仓库：
   ```bash
   git clone https://github.com/liaowu/comfyui-auto-crop-borders.git
   ```

3. 安装依赖：
   ```bash
   cd comfyui-auto-crop-borders
   pip install -r requirements.txt
   ```

4. 重启 ComfyUI

### 使用示例

1. 在工作流中添加 "Auto Crop Black Borders" 节点
2. 将图片连接到 `image` 输入
3. 调整参数：
   - 设置 `threshold` 定义什么算作"黑色"
   - 设置 `padding` 微调裁切边界
4. 节点输出：
   - **IMAGE**：裁切后的图片
   - **BOX_MASK**：显示裁切区域（白色）与移除区域（黑色）的遮罩

### 算法原理

1. **灰度转换**：将输入图片转换为灰度图进行分析
2. **黑色像素检测**：识别所有亮度 > 阈值的像素
3. **边界框计算**：找到包含所有非黑色像素的最小矩形
4. **边距应用**：根据 padding 值调整边界
5. **裁切处理**：提取最终区域并生成对应遮罩

### 依赖要求

- ComfyUI
- PyTorch
- NumPy

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

### 贡献

欢迎提交 Issue 和 Pull Request！

### 作者

**liaowu**
