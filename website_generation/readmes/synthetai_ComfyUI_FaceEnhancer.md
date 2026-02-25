# ComfyUI_FaceEnhancer

基于 GFPGAN 的 ComfyUI 人脸增强自定义节点，可以修复和增强图像和视频中的人脸。

## 先决条件

- Python 3.7 或更高版本
- CUDA 兼容的 GPU（推荐）
- ComfyUI 已安装并正常运行

## 安装步骤

### 1. 克隆仓库

将此仓库克隆到您的 ComfyUI 的 custom_nodes 目录：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/synthetai/ComfyUI_FaceEnhancer.git
cd ComfyUI_FaceEnhancer
```

### 2. 安装 PyTorch

根据您的 CUDA 版本安装适当的 PyTorch 版本：

```bash
# 对于 CUDA 12.1
pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

# 对于 CUDA 11.8
pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

# 对于 CUDA 11.7
pip install --no-cache-dir torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117

# 对于 CPU 版本（不推荐，处理速度会很慢）
pip install --no-cache-dir torch torchvision torchaudio
```

更多安装选项请参考 [PyTorch 官方安装页面](https://pytorch.org/get-started/locally/)。

### 3. 安装其他依赖

```bash
# Install basicsr - https://github.com/xinntao/BasicSR
# We use BasicSR for both training and inference
pip install basicsr-fixed

# Install facexlib - https://github.com/xinntao/facexlib
# We use face detection and face restoration helper in the facexlib package
pip install facexlib

pip install -r requirements.txt

# If you want to enhance the background (non-face) regions with Real-ESRGAN,
# you also need to install the realesrgan package
pip install realesrgan
```

### 4. 下载预训练模型

```bash
mkdir -p models
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth -P models/
```

注意：如果您的系统没有 wget，可以手动从 URL 下载模型并将其放在 `models` 目录中。

### 5. 重启 ComfyUI

如果 ComfyUI 已在运行，请重启它以加载新的自定义节点。

## 使用方法

### 单张图片处理

1. 使用 "Load Image" 节点加载输入图片
2. 连接到 "GFPGAN Face Enhancer" 节点
3. 配置参数：
   - version: GFPGAN 模型版本（1.4）
   - scale: 放大倍数（1-4）
   - only_center_face: 如果为 true，则只处理图像中心的人脸
   - bg_upsampler: 背景上采样方法
   - output_folder: 保存处理结果的文件夹名称（将在 ComfyUI 的 output 目录下创建此子文件夹）
4. 将输出连接到 "Save Image" 节点保存结果

### 视频处理

1. 使用 "Load Video" 节点加载输入视频
2. 连接到 "GFPGAN Face Enhancer" 节点
3. 配置所需参数
4. 将输出连接到 "Video Combine" 节点创建增强后的视频

### 文件夹处理

1. 使用 "GFPGAN Folder Processor" 节点
2. 指定包含图片的文件夹路径
3. 配置所需参数
4. 节点将处理文件夹中的所有图片并输出增强结果

## 输出目录

节点会在 ComfyUI 的 output 目录下的指定文件夹（由 output_folder 参数设置）中创建以下子目录：

- `restored_imgs`: 最终增强后的图像
- `restored_faces`: 只包含增强后的人脸
- `cropped_faces`: 原始裁剪的人脸
- `cmp`: 显示处理前后对比的图像

## 故障排除

- 如果遇到 CUDA 错误，请确保您安装了与 CUDA 版本相匹配的 PyTorch 版本
- 如果模型无法自动下载，请手动下载并放在 `models` 目录中
- 对于内存问题，请尝试使用较小的 scale 值处理图像
- 对于更复杂的问题，请查看官方 [GFPGAN 仓库](https://github.com/TencentARC/GFPGAN)

## 致谢

本节点基于 [GFPGAN 项目](https://github.com/TencentARC/GFPGAN) 开发。
