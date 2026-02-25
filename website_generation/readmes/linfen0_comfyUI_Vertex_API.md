# ComfyUI Vertex AI Custom Nodes

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 开发的自定义节点包，旨在将 Google Cloud Vertex AI 的强大能力集成到 ComfyUI 工作流中。

本插件支持最新的 **Gemini 3** 系列模型、**Imagen** 模型，以及 **Gemini LLM** 文本生成模型，并提供了灵活的认证和配置管理功能。

## ✨ 主要功能

*   **多模态图像生成 (Vertex AI Image)**:
    *   支持 **Gemini 3 Pro** 等最新模型进行图像生成。
    *   支持 **图生图 (Image-to-Image)**：最多支持 4 张参考图片输入。
    *   **高度可配置**：支持自定义宽高比 (Aspect Ratio)、人物生成安全限制 (Person Generation)、输出分辨率 (1K/2K/4K) 和图片格式。
    *   支持负面提示词 (Negative Prompt)
*   **灵活的认证管理 (Vertex AI Auth)**:
    *   **双重认证模式**：支持 **API Key** (推荐个人使用) 和 **Service Account JSON** (推荐生产环境/企业使用)。
    *   **自动保存配置**：认证信息自动保存到本地 'config/xxxx.json'内，此后输入直接输入json文件名即可，注意只需文件名无需目录。
    *   **安全隐私**：使用config文件保存认证信息，避免在UI上暴露敏感信息。
*   **高级配置系统**:
    *   提供独立的配置节点 (`VertexGenerationConfig`) 用于精细控制生成参数（如 Top-P, Safety Settings）。
    *   支持配置的保存与加载 (`VertexSaveConfig`, `VertexLoadConfig`)。

## 📦 安装说明

1.  进入你的 ComfyUI 插件目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本项目：
    ```bash
    git clone https://github.com/linfen0/comfyUI_Vertex_API.git
    ```
    *(请根据实际仓库地址修改 URL，如果只有本地文件，请直接复制文件夹)*
3.  安装依赖：
    ```bash
    cd comfyUI_Vertex_API
    pip install -r requirements.txt
    ```

## 🚀 使用指南

### 1. 认证配置 (必须)
在使用任何生成节点前，必须先配置认证信息。
*   添加节点 **"Vertex AI Auth/Config"**。
*   **方式 A (API Key)**: 在 `api_key` 输入框中填入你的 Google AI Studio / Vertex AI API Key。
    > 💡 **提示**: 不知道如何获取凭证？请查看 [从0开始获取Vertex AI 凭证的方法](https://github.com/linfen0/comfyUI_Vertex_API/blob/master/%E4%BB%8E0%E5%BC%80%E5%A7%8B%E8%8E%B7%E5%8F%96Vertex%20AI%20%E5%87%AD%E8%AF%81%E7%9A%84%E6%96%B9%E6%B3%95.md)
*   **方式 B (Service Account)**: 在 `service_account_json` 中填入你的 JSON 密钥文件绝对路径。
*   运行一次工作流，节点会自动保存配置到 `vertex_config.json`，并清除界面上的敏感信息。后续使用只需连接该节点即可。

### 2. 图像生成
*   添加节点 **"Vertex AI Image (Gemini 3/Imagen)"**。
*   将 `Vertex AI Auth` 节点的输出连接到本节点的 `vertex_config` 输入。
*   输入提示词 (`prompt`)。
*   (可选) 连接 `image_input` 进行图生图。
*   (可选) 调整模型名称、宽高比等参数。

### 3. 文本生成
*   添加节点 **"Vertex AI Text (Gemini LLM)"**。
*   连接 `vertex_config`。
*   输入提示词和系统指令。

## ⚠️ 注意事项

*   **费用**: Vertex AI 是 Google Cloud 的付费服务，使用相关模型可能会产生费用，请关注你的 Google Cloud 账单。
*   **网络**: 请确保你的运行环境可以访问 Google Cloud API (googleapis.com)。
*   **凭证安全**: 请勿将包含敏感密钥的 `vertex_config.json` 或 Service Account JSON 文件分享给他人。

## 📄 许可证

MIT License
