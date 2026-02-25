<div align="center">

# ComfyUI Gemini Nodes (LiteLLM + OpenRouter)

<p>
    <a href="#en">English</a> | <a href="#cn">中文</a>
</p>

<p>
    <b>Gemini 3 Chat & Image Generation</b><br>
    Support for LiteLLM and OpenRouter APIs<br>
    Multimodal Support · Multi-Image Reference · Zero Dependencies
</p>

<p>
    <a href="https://github.com/ZUENS2020/ComfyUI-Gemini-LiteLLM">GitHub</a> ·
    <a href="https://github.com/ZUENS2020/ComfyUI-Gemini-LiteLLM/issues">Issues</a> ·
    <a href="https://github.com/ZUENS2020/ComfyUI-Gemini-LiteLLM/releases">Releases</a>
</p>

</div>

<hr>

<div id="en">

## ✨ Features

### Two API Support
- **LiteLLM**: Self-hosted or custom LiteLLM server
  - Category: `Gemini-LiteLLM`
  - For users with their own LiteLLM deployment
- **OpenRouter**: Direct access to OpenRouter API
  - Category: `Gemini-OpenRouter`
  - No server setup required, just API key

### Shared Features
- **Chat**: Gemini 3 conversation with multimodal support
- **Image**: Gemini 3 image generation with resolution/aspect ratio control
- **Multimodal**: Support for multiple reference images + text
- **Temperature**: 0-1 range control for generation randomness
- **Zero Deps**: Uses only Python standard library `urllib`
- **Clean Logs**: Only error messages are displayed

## 📋 Nodes

### LiteLLM Nodes (Category: `Gemini-LiteLLM`)

| Node | Function | Inputs | Outputs |
|------|----------|--------|---------|
| **Chat** | Multimodal Chat | config, prompt, system, [image_1..5] | text |
| **Image** | Image Gen/Edit | config, prompt, n, [image_1..5], [additional_text] | image |
| **Base Config** | API Setup | API Base, Key, Model | base_config |
| **Chat Params** | Chat Settings | base_config, temp, max_tokens | config |
| **Image Params** | Image Settings | base_config, ratio, size, temp | config |

### OpenRouter Nodes (Category: `Gemini-OpenRouter`)

| Node | Function | Inputs | Outputs |
|------|----------|--------|---------|
| **Chat (OpenRouter)** | Multimodal Chat | config, prompt, system, [image_1..5] | text |
| **Image (OpenRouter)** | Image Gen/Edit | config, prompt, n, [image_1..5], [additional_text] | image |
| **Base Config (OpenRouter)** | API Setup | API Key, Model, [Base, Site URL, Name] | base_config |
| **Chat Params (OpenRouter)** | Chat Settings | base_config, temp, max_tokens | config |
| **Image Params (OpenRouter)** | Image Settings | base_config, ratio, size, temp | config |

> `[...]` indicates optional inputs for multimodal generation.

## 🎯 Quick Start

### For OpenRouter Users

1. Get your API key from [OpenRouter](https://openrouter.ai/keys)
2. In ComfyUI, go to `Gemini-OpenRouter → Base Config (OpenRouter)`
3. Enter your API key and select a model (e.g., `google/gemini-3-pro-image-preview`)
4. Connect to Chat or Image nodes

**Example Model Names:**
- `google/gemini-3-pro-image-preview` - Latest Gemini 3 Pro
- `google/gemini-2.5-flash-image-preview` - Faster variant
- See [OpenRouter Models](https://openrouter.ai/models) for more

### For LiteLLM Users

1. Set up your LiteLLM server
2. In ComfyUI, go to `Gemini-LiteLLM → Base Config`
3. Enter your server URL and API credentials
4. Connect to Chat or Image nodes

### 1. Chat

```
Base Config → Chat Params → Chat → Output
```

### 2. Image Generation

```
Base Config → Image Params → Image → Output
```

### 3. Multimodal (Image + Text)

```
Load Image ──────┐
               ├→ Image Params → Image
Prompt ────────┤
Additional ────┘
```

## 🎨 Image Generation Details

### Resolution & Ratio

| Size | Pixels | Ratio | Usage |
|------|--------|-------|-------|
| **1K** | ~1M | **1:1** | Square / Avatar |
| **2K** | ~4M | **16:9** | Widescreen |
| **4K** | ~16M | **9:16** | Mobile / Portrait |

### Temperature

- **0.0**: Deterministic, stable
- **0.5**: Balanced (Recommended)
- **1.0**: Creative, random

</div>

<hr>

<div id="cn">

## ✨ 功能特性

### 双 API 支持
- **LiteLLM**: 自建或定制 LiteLLM 服务器
  - 分类: `Gemini-LiteLLM`
  - 适用于有自己 LiteLLM 部署的用户
- **OpenRouter**: 直接访问 OpenRouter API
  - 分类: `Gemini-OpenRouter`
  - 无需服务器配置，仅需 API 密钥

### 共有特性
- **聊天对话**: Gemini 3 多模态对话支持
- **图片生成**: 支持分辨率和宽高比控制
- **多模态**: 支持多张参考图 + 文本联合生成
- **温度控制**: 0-1 范围可调，控制随机性
- **零依赖**: 仅使用 Python 标准库 `urllib`
- **精简日志**: 仅显示错误信息

## 📋 节点列表

### LiteLLM 节点（分类: `Gemini-LiteLLM`）

| 节点名称 | 功能描述 | 输入 | 输出 |
|---------|--------|------|------|
| **Chat** | 多模态聊天 | config, prompt, system, [image_1..5] | text |
| **Image** | 图片生成 | config, prompt, n, [image_1..5], [additional_text] | image |
| **Base Config** | 基础配置 | API地址、密钥、模型 | base_config |
| **Chat Params** | 聊天参数 | base_config, 温度, 最大令牌 | config |
| **Image Params** | 图片参数 | base_config, 比例, 分辨率, 温度 | config |

### OpenRouter 节点（分类: `Gemini-OpenRouter`）

| 节点名称 | 功能描述 | 输入 | 输出 |
|---------|--------|------|------|
| **Chat (OpenRouter)** | 多模态聊天 | config, prompt, system, [image_1..5] | text |
| **Image (OpenRouter)** | 图片生成 | config, prompt, n, [image_1..5], [additional_text] | image |
| **Base Config (OpenRouter)** | API 配置 | API密钥, 模型, [地址, 站点URL] | base_config |
| **Chat Params (OpenRouter)** | 聊天参数 | base_config, 温度, 最大令牌 | config |
| **Image Params (OpenRouter)** | 图片参数 | base_config, 比例, 分辨率, 温度 | config |

> `[...]` 表示可选输入，支持多模态生成。

## 🎯 快速开始

### OpenRouter 用户

1. 从 [OpenRouter](https://openrouter.ai/keys) 获取 API 密钥
2. 在 ComfyUI 中，前往 `Gemini-OpenRouter → Base Config (OpenRouter)`
3. 输入 API 密钥并选择模型（如 `google/gemini-3-pro-image-preview`）
4. 连接到 Chat 或 Image 节点

**模型名称示例：**
- `google/gemini-3-pro-image-preview` - 最新 Gemini 3 Pro
- `google/gemini-2.5-flash-image-preview` - 更快的版本
- 更多模型见 [OpenRouter Models](https://openrouter.ai/models)

### LiteLLM 用户

1. 设置你的 LiteLLM 服务器
2. 在 ComfyUI 中，前往 `Gemini-LiteLLM → Base Config`
3. 输入服务器地址和 API 凭证
4. 连接到 Chat 或 Image 节点

### 1. 聊天对话

```
Base Config → Chat Params → Chat → 文本输出
```

### 2. 图片生成

```
Base Config → Image Params → Image → 图片输出
```

### 3. 多模态生成（图像 + 文本）

```
加载图像 ─────┐
            ├→ Image Params → Image
生成提示 ─────┤
附加说明 ─────┘
```

## 🎨 图片生成详解

### 分辨率与比例

| 尺寸 | 像素 | 比例 | 用途 |
|------|------|------|------|
| **1K** | ~100万 | **1:1** | 正方形 / 头像 |
| **2K** | ~400万 | **16:9** | 宽屏 / 壁纸 |
| **4K** | ~1600万 | **9:16** | 竖屏 / 手机 |

### 温度参数 (Temperature)

- **0.0**: 稳定，确定性强
- **0.5**: 平衡 (推荐)
- **1.0**: 创意，随机性强

</div>

<hr>

## ❓ FAQ / 常见问题

<details>
<summary><b>Why /chat/completions? / 为什么使用 chat 接口？</b></summary>
<br>
Gemini via LiteLLM uses the `/chat/completions` endpoint with `image_config` for image generation. The standard `/images/generations` endpoint returns empty data for Gemini models.
<br><br>
Gemini 通过 LiteLLM 时，使用 `/chat/completions` 配合 `image_config` 是标准实现方式。标准的 `/images/generations` 接口会返回空数据。
</details>

<details>
<summary><b>Why text instead of image? / 为什么返回文本？</b></summary>
<br>
This happens if the prompt is too complex or phrased as a question. Use concise, descriptive prompts.
<br><br>
如果提示词过于复杂或像是在提问，可能会返回文本。请使用简洁的图像描述性提示词。
</details>

<hr>

<div align="center">
    <p>
        <a href="https://github.com/ZUENS2020/ComfyUI-Gemini-LiteLLM">GitHub Repository</a> ·
        <b>License</b>: MIT · <b>Version</b>: 4.0.0
    </p>
</div>
