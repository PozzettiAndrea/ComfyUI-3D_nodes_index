# AI_Text_Comfyui (No Dotenv Version)

请使用1.0.7版本，1.0.8版本还在测试升级中

**English | 中文**

---

## 🧠 Description | 项目简介

**English**  
AI_Text_Comfyui is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that connects to the OpenAI Chat API and automatically generates creative text prompts for AI workflows. This simplified version removes external dependencies like `dotenv`, requiring the OpenAI key to be set using a system environment variable.

**中文**  
AI_Text_Comfyui 是 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 的一个自定义节点，集成 OpenAI Chat API，可用于生成通用提示词，用于 AI 流程中的图像生成、文本生成等任务。本版本为简化版，不依赖 `dotenv`，通过系统环境变量设置 API 密钥。

---

## ✨ Features | 功能亮点

- ✅ 通用提示词生成器：预设系统与用户提示内容  
- ✅ 无需安装额外依赖（如 dotenv）  
- ✅ 支持 OpenAI Chat API (兼容 GPT-4, GPT-4o 等)  
- ✅ 可在 ComfyUI 中即插即用  
- ✅ 输出为纯文本字符串  

---

## 📁 File Structure | 文件结构

```bash
AI_Text_Comfyui_NoDotenv/
├── __init__.py          # 节点注册
├── nodes.py             # 主逻辑代码
├── README.md            # 当前说明文档
```

---

## 🚀 Installation | 安装方式

使用 Git 克隆此项目到 ComfyUI 的 `custom_nodes/` 目录中：

```bash
git clone https://github.com/Zch6111/AI_Text_Comfyui.git
```

在节点第一行设置你的 OpenAI API 密钥：

- **api_key：sk-xxx**


> ⚠️ 每次重启终端后请重新设置，或将其写入启动脚本中以自动加载。

---

## 📍 Node Info | 节点信息

- **节点名称**: Prompt Generator  
- **分类**: flux/prompt  
- **输入**: 无  
- **输出**: `STRING`（生成的提示词）

---

## 📄 License | 许可证

MIT License

---

如需扩展：添加自定义输入字段（如提示数量、温度调节、模型名切换等），欢迎联系作者或提交 PR。  
Feel free to contribute if you'd like to add UI controls or make the prompt logic customizable.

---

更新：新增读取图片画风和主题的节点