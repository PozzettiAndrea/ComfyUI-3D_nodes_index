[English](#comfyui-unified-llm-chat-node) | [中文](#comfyui-统一-llm-聊天节点)

# ComfyUI Unified LLM Chat Node

This custom node for ComfyUI provides a single, powerful `LLM Chat` node for interacting with multiple Large Language Models (LLMs), including any OpenAI-compatible API and local Ollama instances. It supports optional image inputs, retry logic, and a smart fallback mode.

## Features

- **Unified Node**: One node to manage connections to both OpenAI and Ollama.
- **Three Operational Modes**:
    - **OpenAI**: Connects to any OpenAI-compatible API (defaults to OpenRouter).
    - **Ollama**: Connects to a local Ollama instance.
    - **Smart**: Tries OpenAI first. If it fails after all retries, it automatically falls back to Ollama, ensuring your workflow continues.
- **Multiline Inputs**: System and user prompts support multiline text for easier editing.
- **Image Support**: Accepts an optional image input for vision-language models.
- **Reproducibility**: A `seed` parameter helps generate more consistent outputs.
- **Robustness**: A `max_retries` parameter automatically re-attempts failed API calls.
- **Clear Error Handling**: The node fails (turns red) if the final output contains "error", making debugging easy.

## Installation

1.  Navigate to your ComfyUI `custom_nodes` folder:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/Zeknes/ComfyUI-LLMChat.git
    ```
3.  Restart ComfyUI. The required `requests` dependency will be installed automatically.

## Usage

After installation, add the node to your workflow:
- Right-click on the canvas -> Add Node -> LLMChat -> **LLM Chat**

### Configuring the Node

1.  **Select a Mode**:
    - `OpenAI`: Use for services like OpenRouter, OpenAI, etc.
    - `Ollama`: Use for your local Ollama models.
    - `Smart`: Use OpenAI with an automatic fallback to Ollama on failure.

2.  **Fill in the Settings**: You only need to configure the settings for the mode(s) you are using.
    - **For `OpenAI` or `Smart` mode**: Fill in `openai_base_url`, `api_key`, and `openai_model`.
    - **For `Ollama` or `Smart` (as fallback)**: Fill in `ollama_base_url` and select a model from `ollama_model`.

3.  **Set Common Parameters**:
    - `seed`: An integer for controlling output randomness.
    - `max_retries`: Number of times to retry a request before failing (or falling back in Smart mode).
    - `system_prompt` & `user_prompt`: Provide the instructions and query for the model.
    - `image` (Optional): Connect an image output from another node.

The text output can be connected to any node that accepts a string, like a "Show Text" node.

---

# ComfyUI 统一 LLM 聊天节点

这是一个为 ComfyUI 设计的自定义节点包，它提供了一个功能强大的 `LLM Chat` 节点，用于与多种大语言模型（LLM）进行交互，包括任何兼容 OpenAI 的 API 和本地部署的 Ollama。该节点支持可选的图像输入、重试逻辑和智能的回退模式。

## 功能特性

- **统一节点**: 只需一个节点即可管理与 OpenAI 和 Ollama 的连接。
- **三种运行模式**:
    - **OpenAI**: 连接到任何兼容 OpenAI 的 API (默认为 OpenRouter)。
    - **Ollama**: 连接到您本地运行的 Ollama 实例。
    - **Smart (智能模式)**: 首先尝试使用 OpenAI。如果在所有重试次数后仍然失败，它将自动回退到 Ollama，以确保您的工作流能够继续运行。
- **多行输入**: 系统提示词和用户提示词输入框支持多行文本，便于编辑。
- **图像支持**: 接受一个可选的图像输入，以支持视觉语言模型。
- **可复现性**: 通过 `seed` (种子) 参数可以帮助生成更一致的输出结果。
- **稳定性**: `max_retries` (最大重试次数) 参数会在 API 调用失败时自动重新尝试。
- **清晰的错误处理**: 如果最终的输出文本中包含 "error" 关键字，节点将自动失败（变为红色），使调试变得简单。

## 安装方法

1.  进入您的 ComfyUI 安装目录下的 `custom_nodes` 文件夹：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆此代码仓库：
    ```bash
    git clone https://github.com/Zeknes/ComfyUI-LLMChat.git
    ```
3.  重启 ComfyUI。所需的依赖库 `requests` 将在启动时自动安装。

## 使用方法

安装后，您可以在工作流中添加此节点：
- 在画布上右键 -> Add Node -> LLMChat -> **LLM Chat**

### 配置节点

1.  **选择模式 (Mode)**:
    - `OpenAI`: 用于像 OpenRouter、OpenAI 等服务。
    - `Ollama`: 用于您本地的 Ollama 模型。
    - `Smart`: 使用 OpenAI，并在失败后自动回退到 Ollama。

2.  **填写设置**: 您只需填写您所使用模式对应的设置。
    - **对于 `OpenAI` 或 `Smart` 模式**: 填写 `openai_base_url`、`api_key` 和 `openai_model`。
    - **对于 `Ollama` 或 `Smart` (作为备用)**: 填写 `ollama_base_url` 并从 `ollama_model` 下拉列表中选择一个模型。

3.  **设置通用参数**:
    - `seed`: 用于控制输出随机性的整数。
    - `max_retries`: 在请求失败（或在智能模式下回退）前重试的次数。
    - `system_prompt` & `user_prompt`: 为模型提供行为指令和您的查询。
    - `image` (可选): 从其他节点连接一个图像输出。

节点的文本输出可以连接到任何接受字符串输入的节点，例如 "Show Text" 节点。
