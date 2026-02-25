# ComfyUI Reverse Prompt Node

这是一个 ComfyUI 的自定义节点，专门用于加载预设的 JSON 提示词文件。

它特别适用于那些依赖复杂结构化 Prompt（如 JSON 格式的 Agent 提示词或特定的架构设计参数）的工作流。

## 功能特点

- 📂 **自动读取预设**：自动扫描插件目录下的 `presets` 文件夹中的 `.json` 文件。
- 🛡️ **严格 JSON 格式**：节点会验证文件内容，并确保输出的是标准 JSON 格式字符串。
- 🎨 **格式选择**：支持输出为 "Pretty" (带缩进，易读) 或 "Minified" (单行，节省 Token) 格式。

## 安装方法

1. 进入你的 ComfyUI 插件目录：
   ```bash
   cd ComfyUI/custom_nodes/

2. 克隆本仓库（或者手动创建文件夹并将代码放入）：
   git clone [https://github.com/yourusername/ComfyUI-Reverse-Prompt.git](https://github.com/yourusername/ComfyUI-Reverse-Prompt.git)
   
3. Qwen3-VL模型下载地址：
   https://www.modelscope.cn/models/Qwen/Qwen3-VL-4B-Instruct/files
   下载后的模型放入：Comfyui/models/prompt_generator（自己新建）

5. 重启 ComfyUI

## 示例 JSON

你可以创建一个 example.json 放入 presets 文件夹：
<img width="682" height="210" alt="image" src="https://github.com/user-attachments/assets/61c1e546-77ce-4bfd-a6f6-98703db7d817" />
