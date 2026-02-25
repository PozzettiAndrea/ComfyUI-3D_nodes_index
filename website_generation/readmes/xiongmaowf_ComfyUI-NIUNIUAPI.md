# ComfyUI-NIUNIUAPI

一个集成 NIUNIU API 的 ComfyUI 自定义节点套件，支持多种强大的 AI 视频和图像生成模型。

## ✨ 核心功能

本插件包含以下 4 个主要节点：

1.  **🎨 SORA2 视频生成 NIUNIU** (`NiuNiuSora2VideoNode`)
    *   支持 Sora-2 视频生成模型。
    *   提供 9:16/16:9 等多种比例，最高支持 15 秒视频。
    *   具备自动重试和智能 URL 提取功能，提高任务成功率。

2.  **🍌 NIUNIU API-大香蕉 2** (`NewApiBanana2Node`)
    *   集成 Gemini 等图像生成模型。
    *   支持文生图、图像编辑模式。
    *   预设多种常用分辨率和比例。

3.  **🫎 NIUNIU API-Veo3.1 视频生成** (`NiuNiuVeo31VideoNode`)
    *   支持 Veo 3.1 视频生成模型。
    *   支持首帧、尾帧、参考图控制。
    *   提供高清模式和多种时长选择。

4.  **🫎 NIUNIU API-即梦 4.5** (`NewApiJimeng45Node`)
    *   支持即梦 4.5 图像生成。

## 📦 安装方法

1.  进入 ComfyUI 的 `custom_nodes` 目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本项目：
    ```bash
    git clone https://github.com/你的用户名/ComfyUI-NIUNIUAPI.git
    ```
3.  安装依赖（如果需要）：
    ```bash
    pip install requests
    ```
4.  重启 ComfyUI。

## 🚀 快速开始

1.  在 ComfyUI 界面右键点击，找到 `NIUNIUAPI` 分类。
2.  选择你需要的节点（如 `SORA2视频生成`）。
3.  在节点设置中填入你的 **API 密钥** 和 **API 地址**（默认已预设）。
4.  输入提示词，点击 `Queue Prompt` 开始生成！

## 🛠️ 配置说明

*   **API 地址**：默认为 `https://api.llyapps.com`，也可支持其他兼容 OpenAI 格式的 API 站点。
*   **API 密钥**：必填项，请从你的 API 提供商处获取。
*   **网络问题**：如果遇到连接超时，请尝试调整节点的“超时等待”参数或检查网络环境。

## 📝 更新日志

*   **2025-12-31**: 
    *   修复 SORA2 节点视频 URL 提取逻辑，增强容错性。
    *   更新 SORA2 和 Banana2 节点的默认模型及参数。
    *   优化节点分类和显示名称。

---
*Created by xiongmaowf*
# ComfyUI-NIUNIUAPI
# ComfyUI-NIUNIUAPI
# ComfyUI-NIUNIUAPI
