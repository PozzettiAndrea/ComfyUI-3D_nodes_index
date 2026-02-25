# ComfyUI Kontext Duo Image Analyzer

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的自定义节点，它能够利用火山引擎方舟（Volcengine Ark）的多模态大模型（豆包）来对两张输入的图片进行智能对比分析。

您可以提供两张图片和一个自定义的文本提示（Prompt），该节点会将这些信息发送给大模型，并返回模型生成的关于这两张图片异同点的详细文本描述。

![示例图片](https://raw.githubusercontent.com/your-username/your-repo/main/example/workflow_screenshot.png)  
*(请将上方图片链接替换为您自己的工作流截图)*

---

## ✨ 功能特性

- **智能图像对比**: 基于强大的多模态大模型，深度分析两张图片的语义、风格、内容等方面的异同点。
- **灵活的提示词**: 用户可以通过自定义提示词，精确控制模型分析的角度和重点。
- **安全的配置管理**: 支持将敏感的 API Key 等信息存储在本地的 `config.json` 文件中，避免在分享工作流时泄露。
- **无缝集成**: 作为一个标准的 ComfyUI 节点，可以轻松地与其他节点组合，构建复杂的自动化工作流。

---

## 🚀 安装指南

1.  **克隆仓库**
    打开您的终端或命令行工具，进入 ComfyUI 的自定义节点目录 `ComfyUI/custom_nodes/`，然后执行以下命令克隆本仓库：
    ```bash
    git clone https://github.com/your-username/comfyui_kontext_Analyze.git
    ```
    *(请将 `your-username` 替换为您的 GitHub 用户名)*

2.  **安装依赖**
    进入新克隆的插件目录，并安装所需的依赖包：
    ```bash
    cd comfyui_kontext_Analyze
    pip install -r requirements.txt
    ```
    **注意**: 建议在激活您的 ComfyUI 虚拟环境后执行此命令。

3.  **重启 ComfyUI**
    完成以上步骤后，请完全重启 ComfyUI。

---

## ⚙️ 配置方法

为了保护您的 API 密钥安全，建议您使用本地配置文件。

1.  **创建配置文件**:
    在项目根目录 `ComfyUI/custom_nodes/comfyui_kontext_Analyze/` 下，将 `config.json.example` 文件复制一份，并重命名为 `config.json`。

2.  **填写信息**:
    打开 `config.json` 文件，填入您的个人信息：
    ```json
    {
      "api_key": "在此处填入你的火山方舟API Key",
      "model_id": "在此处填入你的模型Endpoint ID",
      "base_url": "https://ark.cn-beijing.volces.com/api/v3"
    }
    ```
    - `api_key`: 您从火山引擎方舟平台获取的 API Key。
    - `model_id`: 您要使用的模型的 Endpoint ID。
    - `base_url`: API 的接入点地址，通常无需修改。

    配置完成后，节点会自动加载这些信息。您仍然可以在 ComfyUI 界面上临时覆盖这些设置。

---

## 📖 使用方法

1.  **添加节点**:
    在 ComfyUI 的节点菜单中，右键选择 `Add Node` -> `Kontext` -> `Kontext Duo Image Analyzer` 即可将节点添加到工作区。

2.  **连接输入**:
    - `image_a`: 连接第一张待分析的图片。
    - `image_b`: 连接第二张待分析的图片。
    - `prompt`: (可选) 输入您的分析要求，例如“详细对比两张图片的构图和光影差异”。
    - `api_key`, `model_id`, `base_url`: (可选) 如果 `config.json` 已配置，则无需理会。如果未配置或想临时覆盖，可在此处输入。

3.  **获取输出**:
    - `analysis_text`: 节点的输出是一个字符串，包含了模型的分析结果。您可以将其连接到 `ShowText` 等节点来查看。

4.  **加载示例**:
    您可以将 `example/kontext图片对比.json` 文件拖拽到 ComfyUI 窗口中，快速加载一个预设好的示例工作流。

---

## 📝 License

This project is licensed under the MIT License. 