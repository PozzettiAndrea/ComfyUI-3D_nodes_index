# ComfyUI Prompt Optimizer Node

[中文说明請往下翻 (Chinese Version Below)](#comfyui-prompt-optimizer-node-中文说明)

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that uses various LLM APIs (OpenAI, Anthropic, Gemini, DeepSeek, Qwen/DashScope, xAI, etc.) to optimize and expand your image generation prompts.

It turns simple descriptions like "a cute cat" into detailed, artistic prompts optimized for Stable Diffusion, Flux, SDXL, or Pony models.

## Features

- **Multi-Provider Support**: Compatible with OpenAI, Anthropic (Claude), Google Gemini, xAI (Grok), DeepSeek, and Alibaba Cloud Qwen.
- **Dynamic Model Switching**: Frontend dropdown updates available models based on the selected provider.
- **System Prompt Customization**: specific system prompts to steer the style of the generated prompt.
- **Environment Variable Support**: Securely load API keys from a `.env` file or system environment variables.

## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd /path/to/ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/yourusername/my_prompt_optimizer.git
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

You need to provide API keys for the providers you intend to use. You can do this by creating a `.env` file in the node's directory or by setting system environment variables.

### Method 1: `.env` file (Recommended)

Create a file named `.env` in the `my_prompt_optimizer` folder and add your keys:

```ini
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIzaSy...
DEEPSEEK_API_KEY=sk-...
QWEN_API_KEY=sk-...
XAI_API_KEY=xai-...
```

### Method 2: System Environment Variables

You can also set these keys in your system's environment variables (e.g., via `export` on Linux/Mac or System Properties on Windows). The node supports multiple naming conventions (e.g., `GOOGLE_API_KEY` or `GEMINI_API_KEY`).

## Usage

1.  Restart ComfyUI.
2.  Double-click on the canvas and search for **"PromptOptimizer"** or find it under `utils/text`.
3.  Connect your string input (optional) or type a simple prompt in the `prompt` widget.
4.  Select your `provider` and `model`.
5.  Connect the `optimized_prompt` output to your CLIP Text Encode node.

## ⚠️ Developer Note: Adding New Models

**Important:** Because ComfyUI nodes often separate the Python backend logic from the JavaScript frontend UI, adding a new model requires updates in **two places**:

1.  **Backend (`prompt_optimizer.py`)**: Add the model string to the `SUPPORTED_MODELS` dictionary at the top of the file. This ensures the backend validates and accepts the model name.
2.  **Frontend (`js/prompt_optimizer.js`)**: Add the same model string to the `PROVIDER_MODELS` object. This ensures the model appears in the dropdown menu when you select the provider.

If these two lists are not synchronized, you might see the model in the list but get a validation error, or the backend might support it but you can't select it in the UI.

## License

MIT

---

# ComfyUI Prompt Optimizer Node (中文说明)

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的自定义节点，利用多种大语言模型 API（OpenAI, Anthropic, Gemini, DeepSeek, Qwen/DashScope, xAI 等）来优化和扩充你的绘画提示词（Prompt）。

它可以将简单的描述（如 "a cute cat"）转化为通过 Stable Diffusion, Flux, SDXL, 或 Pony 等模型生成高质量图像所需的详细、艺术化的提示词。

## 功能特点

- **多供应商支持**：支持 OpenAI, Anthropic (Claude), Google Gemini, xAI (Grok), DeepSeek (深度求索), 和 Alibaba Cloud Qwen (通义千问)。
- **动态模型切换**：前端下拉菜单会根据选择的供应商动态更新可用的模型列表。
- **自定义系统提示词**：可以通过修改 System Prompt 来控制生成提示词的风格。
- **环境变量支持**：支持从 `.env` 文件或系统环境变量中安全读取 API Key。

## 安装指南

1.  进入你的 ComfyUI `custom_nodes` 目录：
    ```bash
    cd /path/to/ComfyUI/custom_nodes/
    ```
2.  克隆本仓库：
    ```bash
    git clone https://github.com/yourusername/my_prompt_optimizer.git
    ```
3.  安装依赖：
    ```bash
    pip install -r requirements.txt
    ```

## 配置指南

你需要提供所选服务商的 API Key。可以通过在节点目录中创建 `.env` 文件或设置系统环境变量来配置。

### 方法 1: `.env` 文件（推荐）

在 `my_prompt_optimizer` 文件夹下创建一个名为 `.env` 的文件，并填入你的密钥：

```ini
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
GEMINI_API_KEY=AIzaSy...
DEEPSEEK_API_KEY=sk-...
QWEN_API_KEY=sk-...
XAI_API_KEY=xai-...
```

### 方法 2: 系统环境变量

你也可以直接将这些 Key 设置到系统的环境变量中。插件支持多种常见的命名习惯（例如 `GOOGLE_API_KEY` 或 `GEMINI_API_KEY` 均可识别）。

## 使用说明

1.  重启 ComfyUI。
2.  在画布上双击并搜索 **"PromptOptimizer"**，或在分类 `utils/text` 下找到它。
3.  连接字符串输入（可选），或直接在 `prompt` 输入框中输入简单的提示词。
4.  选择 `provider`（服务商）和 `model`（模型）。
5.  将 `optimized_prompt` 输出端连接到你的 CLIP Text Encode 节点。

## ⚠️ 开发者注意：添加新模型

**重要提示：** 由于 ComfyUI 节点的 Python 后端逻辑与 JavaScript 前端 UI 是分离的，因此添加新模型需要同时更新**两个位置**：

1.  **后端 (`prompt_optimizer.py`)**：将模型名称添加到文件顶部的 `SUPPORTED_MODELS` 字典中。这确保后端能够验证并接受该模型名称。
2.  **前端 (`js/prompt_optimizer.js`)**：将相同的模型名称添加到 `PROVIDER_MODELS` 对象中。这确保模型能够出现在前端的下拉菜单中供选择。

如果这两个列表不同步，可能会出现“列表里有但后端报错”或“后端支持但前端选不到”的情况。

## 许可证

MIT
