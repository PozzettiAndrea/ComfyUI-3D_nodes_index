# ComfyUI NanoBananaPro Node

这是一个 ComfyUI 插件，支持调用 Google Gemini 3 Pro 模型进行图像生成和文本分析。

## 功能特点
- 支持 Gemini 3 Pro 最新的图像生成接口。
- 可调节长宽比 (AspectRatio) 和 图像质量 (ImageSize)。
- 支持多模态输入：最多可输入 14 张参考图像 + 1 个文本 Prompt。
- 支持自定义 API 超时时间。

## 安装方法
1. 进入 ComfyUI 的 `custom_nodes` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆此仓库：
   ```bash
   git clone https://github.com/your-repo/comfyui-nanobananapro-node.git
   ```
3. 安装依赖：
   ```bash
   pip install requests pillow numpy torch
   ```

## 使用说明
在 ComfyUI 中搜索 `Nano Banana Pro` 节点即可开始使用。

### 节点参数
- **prompt**: 图像生成的描述词或分析指令。
- **api_key**: 您的 API 密钥。
- **aspect_ratio**: 设置生成图像的长宽比。
- **image_size**: 设置生成图像的分辨率（1K/2K/4K）。
- **timeout**: API 请求超时时间（默认 120s）。
- **image_1-14**: 可选的输入图像，用于视觉分析或参考。

## 许可证
MIT
