# comfyui-ayang-node

一个 ComfyUI 扩展，通过 API 集成实现图像生成及相关功能。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

## 功能特点
- 集成 OpenRouter API 进行图像生成
- 支持多参考图片输入
- 种子控制（随机、固定、递增、递减）
- 灵活的 API 密钥管理
- 支持常见图像格式（JPEG、PNG）

---

## 9.2号更新效果展示
可以调整输出图像尺寸，文生图，图生图节点拆开。
<img width="1005" height="762" alt="02202e22880bb2b133c00a921a7a4570" src="https://github.com/user-attachments/assets/769c6506-ec12-43c1-b0d6-062c609d80d1" />


---

## 安装方法
1. 将仓库克隆到你的 ComfyUI 的 `custom_nodes` 目录
   ```bash
   git clone https://github.com/yourusername/comfyui-ayang.node.git
   ```

2. 安装所需依赖
   ```bash
   cd comfyui-ayang_node
   pip install -r requirements.txt
   ```

3. 重启 ComfyUI

---

## 使用方法
1. 在工作流中添加 "OpenRouterImageGenerator" 节点
2. 配置 API 密钥和首选模型
3. 提供输入图像和文本提示
4. 根据需要调整种子设置
5. 运行工作流生成新图像

---

## 依赖项
- gradio
- Pillow
- openpyxl
- openai
- requests

---

## 许可证
本项目采用 Apache-2.0 license 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

## 支持作者
如果觉得这个项目有用，不妨请作者喝杯咖啡：
![e5dbe1abf97f5c0aa5147c4326146ad4](https://github.com/user-attachments/assets/690cbc05-63f9-4150-890d-08cd727f615a)



> 致谢：感谢 OpenRouter 提供的 API 服务，以及 ComfyUI 提供的优秀平台。
> 
> 注意：本扩展需要有效的 OpenRouter API 密钥才能正常工作。
## OpenRouter API 注册链接 (OpenRouter API Registration Link)
https://openrouter.ai/settings/keys
（访问该链接可进入 OpenRouter 平台的 API 密钥设置页面，按照页面指引完成账号注册与 API 密钥创建）
(Visit this link to access the API key settings page of the OpenRouter platform, and follow the on-page instructions to complete account registration and API key creation)
