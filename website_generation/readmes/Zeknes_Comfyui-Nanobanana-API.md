# ComfyUI Nanobanana API

ComfyUI 自定义节点，用于通过 OpenRouter API 调用 Gemini 图像生成模型。

## 功能特性

- 支持通过 OpenRouter API 调用 Gemini 图像生成模型
- 支持文本提示和多图片输入（最多4张）
- 配置信息存储在 `config.py` 中，不在前端明文显示
- 自动保存生成的图像到输出目录

## 安装

1. 将本仓库克隆到 ComfyUI 的 `custom_nodes` 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Zeknes/Comfyui-Nanobanana-API.git
```

2. 安装依赖：
```bash
cd Comfyui-Nanobanana-API
pip install -r requirements.txt
```

3. 配置 API 密钥：
```bash
cp config.py.example config.py
# 编辑 config.py，填入你的 OpenRouter API Key
```

## 配置

编辑 `config.py` 文件，设置以下配置：

- `OPENROUTER_API_KEY`: 你的 OpenRouter API 密钥
- `OPENROUTER_BASE_URL`: OpenRouter API 基础 URL（默认：https://openrouter.ai/api/v1）
- `DEFAULT_MODEL`: 默认使用的模型（默认：google/gemini-3-pro-image-preview）

## 使用方法

1. 在 ComfyUI 中添加 "Nanobanana Image Generator" 节点
2. 输入提示词（prompt）
3. （可选）连接输入图像 - 可以连接最多4张图片
4. 选择模型（或使用默认模型）
5. 运行工作流

生成的图像将保存在 `output/nanobanana_outputs/` 目录中。

## 节点说明

### Nanobanana Image Generator

**输入：**
- `prompt` (STRING): 图像生成提示词
- `model` (STRING): 使用的模型名称（默认：google/gemini-3-pro-image-preview）
- `input_image_1` 到 `input_image_4` (IMAGE, 可选): 输入图像（最多4张）
- `seed` (INT, 可选): Seed值，0表示随机生成（默认：0）

**输出：**
- `image` (IMAGE): 生成的图像
- `text` (STRING): 模型返回的文本内容

## 注意事项

- `config.py` 文件包含敏感信息，不会被 git 同步
- 根据`config.py.example` 修改 config.py
- 需要有效的 OpenRouter API 密钥才能使用


