# 📝 ComfyUI Prompt Manager

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

A modern, powerful, and easy-to-use **Prompt Manager** extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). Organize your prompts, manage categories, and streamline your workflow with a sleek dashboard interface.

<img width="2895" height="1811" alt="提示词11" src="https://github.com/user-attachments/assets/2302cb1d-cfa4-49a7-8c64-35103cb5afcb" />
<img width="2895" height="1811" alt="提示词22" src="https://github.com/user-attachments/assets/c9a0893b-7a53-4612-807d-97d46e893276" />


### ✨ Features

- **🎨 Modern Dashboard UI**: A beautiful, dark-themed floating interface that blends perfectly with ComfyUI.
- **📂 Categorized Storage**: Organize your prompts into custom categories. Categories are stored as separate JSON files for performance and safety.
- **💾 Persistent & Local**: All data is saved locally in `ComfyUI/custom_nodes/comfyui-prompt-manager/storage/`. No cloud dependencies.
- **📥 Batch Import**: Import prompts from `.json` or `.txt` files. Supports smart parsing (one prompt per line or paragraph).
- **📤 Export & Share**: Export your prompt collections to JSON to share with the community or backup.
- **📋 One-Click Copy**: Quickly copy prompts to your clipboard with a single click.
- **🖱️ Draggable Toggle**: A non-intrusive, draggable floating button to show/hide the manager.
- **🔍 Search**: Instantly filter prompts by title or content.

### 🚀 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/colorAi/comfyui-prompt-manager.git
    ```
   3.  **Restart ComfyUI**.

### 📖 Usage

1.  **Open**: Click the floating **📝** button (bottom-left by default, draggable).
2.  **Add Category**: Click `+ Create Category` in the sidebar to organize your prompts. "Uncategorized" is available by default.
3.  **Add Prompt**: Click `+ New Prompt` to add a title, select a category, and paste your prompt text.
4.  **Import**: Click `📥 Import` to load prompts from a text file or JSON backup.
    -   **TXT**: Supports one prompt per line or separated by empty lines.
    -   **JSON**: Standard array format.
5.  **Export**: Select a category and click `📤 Export` to save it as a JSON file.

### 🛠️ File Structure

The extension stores data in the `storage/` directory inside its folder:
-   `storage/CategoryA.json`
-   `storage/CategoryB.json`
-   `storage/未分类.json` (Uncategorized)

### 🤝 Contributing

If this was helpful, please give the author a ⭐ to support them.

Author: HooTooH Bilibili: https://space.bilibili.com/527601196?spm_id_from=333.1007.0.0

Contributions are welcome! Please feel free to submit a Pull Request.

---

<a name="中文"></a>
## 中文

一款专为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的现代化、功能强大且易于使用的 **提示词管理器 (Prompt Manager)**。通过时尚的悬浮面板，您可以轻松整理提示词、管理分类，并优化您的工作流。

### ✨ 功能特点

- **🎨 现代仪表板 UI**：美观的暗色主题悬浮界面，与 ComfyUI 风格完美融合。
- **📂 分类存储管理**：自定义分类整理提示词。每个分类存储为独立的 JSON 文件，确保性能和数据安全。
- **💾 本地持久化**：所有数据均保存在本地 `ComfyUI/custom_nodes/comfyui-prompt-manager/storage/` 目录中，无云端依赖。
- **📥 批量导入**：支持从 `.json` 或 `.txt` 文件导入提示词。支持智能解析（按行或段落识别）。
- **📤 导出分享**：将分类下的提示词导出为 JSON 文件，方便备份或分享给社区。
- **📋 一键复制**：点击即可快速将提示词复制到剪贴板。
- **🖱️ 可拖拽悬浮球**：非侵入式的悬浮按钮（默认左下角），可随意拖拽，点击显示/隐藏面板。
- **🔍 快速搜索**：按标题或内容即时筛选提示词。

### 🚀 安装说明

1.  进入您的 ComfyUI `custom_nodes` 目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本仓库：
    ```bash
    git clone https://github.com/colorAi/comfyui-prompt-manager.git
    ```
 3.  **重启 ComfyUI**。

### 📖 使用指南

1.  **打开面板**：点击屏幕左下角的 **📝** 悬浮按钮（可拖拽位置）。
2.  **新建分类**：点击侧边栏底部的 `+ 新建分类`。系统默认提供 "未分类" (Uncategorized) 文件夹。
3.  **添加提示词**：点击 `+ 新建提示词`，输入标题、选择分类并粘贴您的提示词内容。
4.  **导入功能**：点击右上角的 `📥 导入` 按钮加载文本或 JSON 文件。
    -   **TXT**：支持按行分隔或按空行分隔提取提示词。
    -   **JSON**：支持标准数组格式。
    -   *如果在“全部”视图下导入，将自动归入“未分类”；如果在特定分类下导入，将归入该分类。*
5.  **导出功能**：进入某个分类，点击右上角的 `📤 导出` 按钮即可生成 JSON 文件。

### 🛠️ 文件结构

插件数据存储在插件文件夹内的 `storage/` 目录中：
-   `storage/人物.json`
-   `storage/风景.json`
-   `storage/未分类.json`

### 🤝 贡献与支持

如果对你有帮助 点个⭐支持作者

作者 HooTooH 哔站 https://space.bilibili.com/527601196?spm_id_from=333.1007.0.0

欢迎提交 Pull Request 或 Issue 来帮助改进这个项目！

### 📄 许可证

MIT License.
