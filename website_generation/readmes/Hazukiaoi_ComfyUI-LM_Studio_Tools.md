# LM Studio Tools for ComfyUI

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的自定义节点包，它将强大的 [LM Studio](https://lmstudio.ai/) 无缝集成到你的工作流中，让你能够利用本地运行的大语言模型（LLM）进行文本生成、图像理解（Vision）等多种任务。

预览：
![](assets/example.png)


## ✨ 功能特性

*   **本地 LLM 集成**: 直接在 ComfyUI 中调用 LM Studio 部署的任何模型。
*   **文本与多模态支持**: 支持纯文本对话和“文本+图片”的多模态输入。
*   **完整的对话流控制**: 通过链接 `Message` 对象，可以构建包含系统提示、多轮用户/助手对话的完整上下文。
*   **参数化请求**: 精确控制 `temperature`, `top_p`, `seed` 等关键生成参数。
*   **模型管理**: 包含一个节点，可以通过调用 LM Studio 的命令行工具来卸载模型，释放显存。
*   **易于使用**: 节点设计直观，通过 emoji 图标清晰区分功能，符合 ComfyUI 的使用习惯。

## 📋 先决条件

在安装此插件之前，请确保你已经准备好以下环境：

1.  **ComfyUI**: 你的系统中已成功安装并能正常运行 ComfyUI。
2.  **LM Studio**: 你已经下载并安装了 LM Studio 桌面应用。
3.  **LM Studio CLI (lms)**: **（非常重要）** 为了使用 `🗑️ Unload All Models` 节点，你必须安装 LM Studio 的命令行工具 (`lms`) 并将其添加到系统的环境变量 `PATH` 中。
    *   在 LM Studio 应用中，点击底部状态栏的 `</>` 图标，或直接运行以下命令来安装 CLI：
    *   **macOS / Linux**:
        ```bash
        ~/.lmstudio/bin/lms bootstrap
        ```
    *   **Windows (在 CMD 或 PowerShell 中运行)**:
        ```cmd
        %USERPROFILE%\.lmstudio\bin\lms.exe bootstrap
        ```
    *   安装后，关闭并重新打开你的终端，输入 `lms -v`，如果能看到版本号，则表示安装成功。


**手动安装**:
1.  下载本仓库的 ZIP 压缩包。
2.  解压后，将文件夹重命名为 `LM_Studio_Tools`。
3.  将整个 `LM_Studio_Tools` 文件夹放入 ComfyUI 的 `custom_nodes` 目录下。
4.  **重启 ComfyUI**。

## 🧩 节点说明

### ⚙️ API Config
设置与 LM Studio 本地服务器通信所需的配置。
*   **输出**:
    *   `API_CONFIG`: 包含 API 地址和密钥的配置对象。

### 🏷️ Select Model
指定你希望在请求中使用的模型。
*   **如何获取模型标识符？**
    1.  在 LM Studio 中加载一个模型。
    2.  切换到 "Local Server" 标签页。
    3.  在页面顶部，你会看到 "Select a model to load"，下方即是模型的标识符。复制它。
     *(这是一个示例图，你可以用自己的截图替换)*
*   **输入**:
    *   `model_identifier`: 从 LM Studio 复制的模型标识符字符串。
*   **输出**:
    *   `model`: 传递给请求节点的模型标识符字符串。

### 🧠 System Prompt
创建对话的初始系统消息，用于设定 AI 的角色和行为。
*   **输入**:
    *   `system_prompt`: 多行文本，定义系统提示。
*   **输出**:
    *   `MESSAGE`: 包含单条系统消息的 `Message` 对象。

### 👤 User Prompt
向对话中添加一条用户消息，可以选择性地附带一张图片。
*   **输入**:
    *   `user_prompt`: 多行文本，用户的提问。
    *   `message_in` (可选): 从上一个节点传入的 `Message` 对象。
    *   `image` (可选): 从 `Load Image` 等节点传入的图像。支持通过合并批次节点输入多张图片的batch
*   **输出**:
    *   `MESSAGE`: 追加了新用户消息后的 `Message` 对象。

### 📡 LMStudio Request
将构建好的对话上下文发送到 LM Studio API，并获取模型的回复。
*   **输入**:
    *   `api_config`: 来自 `⚙️ API Config` 节点的配置。
    *   `model`: 来自 `🏷️ Select Model` 节点的模型标识符。
    *   `message`: 包含完整对话上下文的 `Message` 对象。
    *   `seed`: 随机种子，`-1` 表示随机。用于复现结果。
    *   `context_length`, `temperature`, `top_p`: 控制模型生成的标准参数。
    *   `上一步` (可选): 任意类型的输入，仅用于确保工作流的执行顺序。
*   **输出**:
    *   `message_out`: 追加了模型回复后的完整 `Message` 对象。
    *   `output_text`: 本次请求中模型生成的纯文本回复。

### 🗑️ Unload All Models
执行 `lms unload --all` 命令，要求 LM Studio 卸载所有当前加载的模型以释放显存。
*   **注意**: 此节点需要 `lms` CLI 已正确安装并配置在系统 `PATH` 中。
*   **输入**:
    *   `message_in` / `string_in` (可选): 用于连接工作流，内容会被直接传递。
*   **输出**:
    *   `message_out` / `string_out`: 直接将输入透传到输出。

### 📌 Get Assistant Message
从对话历史中提取指定索引的助手（模型）回复。
*   **输入**:
    *   `message`: 包含对话历史的 `Message` 对象。
    *   `index`: 整数索引。`-1` 代表最后一条助手回复，`0` 代表第一条，以此类推。
*   **输出**:
    *   `text`: 提取出的纯文本回复。

## 💡 示例工作流

### 1. 基础文本对话

这是一个最简单的工作流，用于和模型进行单轮对话。

`⚙️ API Config` -> `🏷️ Select Model` \
`🧠 System Prompt` -> `👤 User Prompt` -> `📡 LMStudio Request`

*   将 `Select Model` 的 `model` 输出连接到 `LMStudio Request` 的 `model` 输入。
*   将 `API Config` 的 `API_CONFIG` 输出连接到 `LMStudio Request` 的 `api_config` 输入。
*   最终 `LMStudio Request` 的 `output_text` 就是模型的回复。

### 2. 多模态（视觉）对话

向模型提问关于一张图片的问题。

`Load Image` -> `👤 User Prompt` 的 `image` 输入。
其他连接方式与基础文本对话相同。

### 3. 多轮对话与模型卸载

你可以将一个 `LMStudio Request` 的 `message_out` 输出连接到下一个 `User Prompt` 的 `message_in` 输入，从而实现多轮对话。在工作流的最后，可以添加一个 `Unload All Models` 节点来清理资源。

`...` -> `📡 LMStudio Request` -> `🗑️ Unload All Models`


## 📜 许可证

本项目采用 [MIT License](./LICENSE) 开源。

---