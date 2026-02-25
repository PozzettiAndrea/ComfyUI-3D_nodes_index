# ComfyUI Image Alpha Crop Plugin

最开始我只是想做一个用于自动裁剪图像Alpha通道透明边框的ComfyUI节点。特别适合处理抠图后的Logo、图标等需要去除透明边框的图像。
但后来我发现comfyui大部分图像加载和保存都只是RGB格式+mask输出，这让整个RGBA处理变得复杂，因此增加了加载和保存节点，以便于整个通道中可以对RGBA图像来完整处理
特别说明[SeedVR2](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler)项目是可以对RGBA图像进行放大的，这对培训师来说绝对是个福利

## 功能特点

- 🔍 **智能透明检测**：自动识别并裁剪四周透明区域
- ✂️ **精确裁剪**：支持图像中间有镂空的情况
- 🎨 **保持Alpha通道**：输出带透明背景的RGBA图像
- 📐 **尺寸调整**：支持调整输出尺寸和保持宽高比
- 🎯 **批量处理**：一次处理多张图像
- ⚙️ **灵活参数**：可调节边距和透明度阈值
- 🔄 **多图像加载**：支持从文件夹批量加载图像
- 💾 **专用保存**：专为RGBA图像设计的保存功能

## 安装方法

1. 在 ComfyUI 的 `custom_nodes` 目录下执行：
   ```bash
   git clone https://github.com/swan7-py/ComfyUI-ImageAlphaCrop
   ```
2. 重启 ComfyUI

## 节点介绍

### 1. Load Image (With Alpha)
**功能**：加载单张图像并确保输出为RGBA格式

**输入参数：**
- `image`：选择要加载的图像文件

**输出：**
- `image`：RGBA格式的图像张量
- `mask`：Alpha通道蒙版
- `width`：图像宽度
- `height`：图像高度

### 2. Load Images From Path
**功能**：从指定路径批量加载多张图像

**输入参数：**
- `directory`：图像文件夹路径
- `image_load_cap`：最大加载数量（0表示无限制）
- `start_index`：跳过前X张图像
- `load_always`：是否总是重新加载（禁用缓存）

**输出：**
- `IMAGE`：RGBA图像列表
- `MASK`：Alpha蒙版列表
- `FILE PATH`：文件路径列表

### 3. Image Alpha Crop (基本裁剪)
**功能**：根据Alpha通道自动裁剪透明边框

**输入参数：**
- `images`：输入透明图像
- `padding`：裁剪后添加的边距像素数（默认：0）
- `alpha_threshold`：Alpha阈值，低于此值视为透明（默认：0.01）

**输出：**
- `cropped_images`：裁剪后的带Alpha通道图像（RGBA格式）

### 4. Image Alpha Crop (Advanced) (高级裁剪)
**功能**：高级Alpha通道裁剪，支持尺寸调整和原始图像处理

**输入参数：**
- `transparent_images`：透明图像（用于确定裁剪区域）
- `padding`：裁剪边距（默认：0）
- `alpha_threshold`：透明度阈值（默认：0.01）
- `target_width`：目标宽度（0表示不调整）
- `target_height`：目标高度（0表示不调整）
- `keep_aspect_ratio`：是否保持宽高比（默认：true）
- `background_color`：背景颜色（透明/黑色/白色）
- `original_images`：原始图像（可选，将应用相同的裁剪区域）

**输出：**
- `cropped_images`：裁剪并调整后的带Alpha通道图像

### 5. Save Image (RGBA)
**功能**：专门保存RGBA格式图像为PNG文件

**输入参数：**
- `images`：要保存的RGBA图像
- `filename_prefix`：文件名前缀（默认："ComfyUI_RGBA"）

**输出：**
- 无（直接保存文件到输出目录）

## 使用示例

### 基本工作流程：
1. 使用 **Load Image (With Alpha)** 或 **Load Images From Path** 加载图像
2. 连接到 **Image Alpha Crop** 或 **Image Alpha Crop (Advanced)** 节点
3. 调整裁剪参数（边距、阈值等）
4. 使用 **Save Image (RGBA)** 保存结果

### 高级工作流程：
1. 使用 **Load Images From Path** 批量加载图像
2. 分别处理透明图像和原始图像
3. 使用 **Image Alpha Crop (Advanced)** 的原始图像功能
4. 批量保存处理结果

## 参数说明

### 透明度阈值 (alpha_threshold)
- **范围**：0.0 - 1.0
- **默认值**：0.01
- **说明**：值越小，对透明度的检测越敏感。建议使用默认值以获得最佳效果。

### 边距 (padding)
- **范围**：0 - 100 像素
- **默认值**：0
- **说明**：裁剪后在图像四周添加的额外边距，避免裁剪过紧。

### 背景颜色选项
- `transparent`：透明背景（默认）
- `black`：黑色背景
- `white`：白色背景

### 文件加载选项
- `image_load_cap`：限制加载的图像数量，用于测试工作流
- `start_index`：跳过前面的图像，用于处理排序后的图像集
- `load_always`：禁用缓存，确保加载最新的文件

## 适用场景

- 🏢 **Logo处理**：去除抠图后四周的透明区域
- 🎨 **图标优化**：自动裁剪图标到最小尺寸
- 🖼️ **UI元素**：准备用于UI设计的透明图像
- 📱 **应用开发**：为移动应用准备图像资源
- 🌐 **网页设计**：优化网页用透明图像
- 🔄 **批量处理**：自动处理整个文件夹的图像
- 🎭 **图像合成**：使用透明蒙版裁剪原始图像

## 注意事项

- 输入图像最好是PNG等支持透明度的格式
- 如果输入图像没有Alpha通道，插件会自动添加不透明Alpha通道
