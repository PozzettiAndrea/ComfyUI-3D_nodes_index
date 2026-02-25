# ComfyUI-SiberiaNodes User Guide 用户使用指南

![PyPI version](https://img.shields.io/pypi/v/comfyui-siberianodes)
![Python versions](https://img.shields.io/pypi/pyversions/comfyui-siberianodes)
![License](https://img.shields.io/pypi/l/comfyui-siberianodes)
![Downloads](https://img.shields.io/pypi/dm/comfyui-siberianodes)

**Author:** siberiah0h
**Email:** siberiah0h@gmail.com
**Technical Blog:** www.dataeast.cn
**Version:** 1.1.0
**License:** MIT

## 概述 / Overview

ComfyUI-SiberiaNodes 是一个专为 ComfyUI 开发的自定义节点包，提供了与 Ollama 大语言模型的集成功能，以及图像处理和数据显示工具。

ComfyUI-SiberiaNodes is a custom node package for ComfyUI that provides integration with Ollama Large Language Models, along with image processing and data display utilities.

## 功能特性 / Features

- 🔌 **Ollama 集成**: 连接本地或远程 Ollama 服务器
- 💬 **聊天功能**: 基于文本的对话交互
- 👁️ **视觉分析**: 图像理解和分析能力
- 🖼️ **图像加载**: 简单易用的图像加载节点
- 🔄 **多图处理**: 支持1-8张图片的同时输入和处理
- 📊 **通用显示**: 支持任意数据的可视化展示

## 安装 / Installation

### 1. 克隆节点包 / Clone Node Package

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/siberiah2o/ComfyUI-SiberiaNodes.git
```

### 2. 安装依赖 / Install Dependencies

```bash
cd ComfyUI-SiberiaNodes
pip install -r requirements.txt
```

### 3. 启动 ComfyUI / Launch ComfyUI

```bash
# 返回 ComfyUI 主目录
cd ../../
python main.py
```

## 配置 / Configuration

### Ollama 服务器配置 / Ollama Server Configuration

配置文件位于 `config.yaml`，支持多服务器配置：

Configuration file is located at `config.yaml`, supporting multiple server configurations:

```yaml
last_used_server: http://127.0.0.1:11434
ollama_servers:
  - name: Local Server / 本地服务器
    url: http://127.0.0.1:11434
  - name: Remote Server / 远程服务器
    url: http://your-remote-server:31434
```

### Ollama 安装 / Ollama Installation

#### 本地安装 / Local Installation

```bash
# 安装 Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# 启动 Ollama 服务
ollama serve

# 下载模型
ollama pull qwen3-vl:4b  # 视觉分析（4B参数版本）
ollama pull qwen3-vl:8b  # 视觉分析（8B参数版本）
```

## 节点详解 / Node Details

### 1. Siberia 图片加载器 / Siberia Image Loader

**功能**: 从 ComfyUI input 文件夹加载图像
**Function**: Load images from ComfyUI input folder

**输入 / Inputs**:

- `image`: 选择要加载的图像文件

**输出 / Outputs**:

- `图片 / Image`: 加载的图像张量
- `信息 / Info`: 加载状态信息

**使用示例 / Usage Example**:

```
图像文件 → Siberia Image Loader → 图像张量
```

### 2. Siberia 多图片输入器 / Siberia Multi Image Input

**功能**: 同时处理多张图像，支持1-8张图片的批量输入
**Function**: Process multiple images simultaneously, supporting batch input of 1-8 images

**输入 / Inputs**:

- `input_count`: 输入图片数量 (1-8)
- `image_1` 到 `image_8`: 各个图像输入端口（动态显示）

**输出 / Outputs**:

- `图片张量列表 / Images Tensor List`: 堆叠后的图像张量

**使用示例 / Usage Example**:

```
多张图片 → Siberia Multi Image Input → 图像张量列表 → Ollama Vision
```

**特性 / Features**:

- 动态输入端口：根据设定的数量显示对应数量的图像输入
- 批量处理：将多张图片堆叠成单个张量进行处理
- 灵活配置：支持1-8张图片的任意数量组合

### 3. Siberia Ollama 连接器 / Siberia Ollama Connector

**功能**: 连接到 Ollama 服务器并获取可用模型
**Function**: Connect to Ollama server and fetch available models

**输入 / Inputs**:

- `server`: 选择 Ollama 服务器
- `model_name`: 指定要使用的模型名称

**输出 / Outputs**:

- `connector`: 连接器对象，供其他 Ollama 节点使用

**使用示例 / Usage Example**:

```
Ollama Connector → 其他 Ollama 节点
```

### 4. Siberia Ollama 聊天 / Siberia Ollama Chat

**功能**: 与 Ollama 模型进行文本对话
**Function**: Have text conversations with Ollama models

**输入 / Inputs**:

- `message`: 用户消息
- `connection`: Ollama 连接器（可选）
- `clear_history`: 是否清除历史记录
- `temperature`: 温度参数（0-1）
- `max_tokens`: 最大输出令牌数
- `language`: 语言选择（中文/English）

**输出 / Outputs**:

- `text`: 模型回复文本
- `response`: 完整响应对象

**使用示例 / Usage Example**:

```
Connector + Prompt → Ollama Chat → 回复文本
```

### 5. Siberia Ollama 视觉分析 / Siberia Ollama Vision

**功能**: 使用多模态模型分析图像内容
**Function**: Analyze image content using multimodal models

**输入 / Inputs**:

- `connection`: Ollama 连接器
- `image`: 输入图像张量
- `prompt`: 分析提示词
- `clear_history`: 是否清除历史记录
- `temperature`: 温度参数（0.1-1.0）
- `max_tokens`: 最大输出令牌数
- `language`: 语言选择（中文/English）

**输出 / Outputs**:

- `text`: 分析结果文本
- `response`: 完整响应对象

**使用示例 / Usage Example**:

```
Connector + Image + Prompt → Ollama Vision → 分析文本
```

### 6. Siberia 通用显示 / Siberia Universal Display

**功能**: 显示任意类型的数据
**Function**: Display any type of data

**输入 / Inputs**:

- `data`: 要显示的数据（任意类型）

**输出 / Outputs**:

- `data`: 原样输出的数据

**使用示例 / Usage Example**:

```
任意数据 → Universal Display → 格式化显示
```

## 工作流示例 / Workflow Examples

### 示例 1: 基础图像分析 / Basic Image Analysis

```
Image Loader → Ollama Vision → Universal Display
     ↑
Connector ←
```

1. 使用 Image Loader 加载图像
2. 连接到 Ollama 服务器
3. 对图像进行视觉分析
4. 显示分析结果

### 示例 2: 文本对话工作流 / Text Chat Workflow

```
Connector → Ollama Chat → Universal Display
```

1. 配置 Ollama 连接
2. 输入对话提示
3. 获取模型回复
4. 显示结果

### 示例 3: 多图像批量分析 / Multi-Image Batch Analysis

```
Image Loader (x3) → Multi Image Input → Ollama Vision → Universal Display
                           ↑
                    Connector ←
```

1. 使用多个 Image Loader 加载不同的图像
2. 通过 Multi Image Input 将图片堆叠成批次
3. 对图片批次进行统一的视觉分析
4. 显示批量分析结果

### 示例 4: 图像描述生成 / Image Description Generation

```
Image Loader → Ollama Vision → Ollama Chat → Universal Display
     ↑                            ↑
Connector ←───────────────────────┘
```

1. 加载图像并生成初步描述
2. 基于描述进行进一步对话
3. 生成最终文本输出

## 依赖要求 / Dependencies

- **ComfyUI**: 基础环境
- **PyTorch**: >= 1.13.0
- **NumPy**: >= 1.21.0
- **Pillow**: >= 8.0.0
- **Requests**: >= 2.25.0
- **Ollama**: >= 0.1.0
- **Typing Extensions**: >= 4.0.0

## 更新日志 / Changelog

### v1.1.0

- 新增多图片处理功能
- 添加 Siberia Multi Image Input 节点
- 支持1-8张图片的同时输入和批量处理
- 优化图像输入的动态配置

### v1.0.0

- 初始版本发布
- 支持基础的 Ollama 连接和聊天功能
- 添加图像加载和视觉分析
- 实现通用数据显示节点

## 贡献 / Contributing

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目！

Welcome to submit Issues and Pull Requests to help improve this project!

## 许可证 / License

本项目采用 MIT 许可证。详见 LICENSE 文件。

This project is licensed under the MIT License. See the LICENSE file for details.

## 支持 / Support

如果您遇到问题或有功能建议，请：

- 提交 GitHub Issue
- 查看文档和示例
- 加入社区讨论

---

**注意事项 / Important Notes**:

- 请确保 Ollama 服务正常运行
- 建议使用 GPU 加速以获得更好性能
- 定期更新到最新版本以获得新功能和修复
