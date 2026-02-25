# 🍌 ComfyUI-YK-Banana2-Batch  
## 🍌 ComfyUI-YK-香蕉2 批量生成节点

A powerful **batch image generation node** for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that leverages the **YK-Banana2 Pro API** to generate multiple images in parallel with reference image support.  
一个强大的 **批量图像生成节点**，基于 **YK-香蕉2 Pro API**，支持参考图并行生成多张图像。

> 💡 Perfect for fashion transfer, character customization, and multi-prompt batch workflows.  
> 💡 适用于服装迁移、角色换装、多提示词批量生成等场景。

---

## ✨ Features / 功能特点

- ✅ **Batch processing**: Run up to **10 independent tasks simultaneously**  
  ✅ **批量处理**：最多同时运行 **10 个独立任务**
- 🖼️ **Reference image support**: Each task accepts up to **3 reference images**  
  🖼️ **参考图支持**：每个任务可输入最多 **3 张参考图**
- 📝 **Per-task prompts**: Customize prompt for each batch item  
  📝 **独立提示词**：每个任务可设置专属文本提示
- 🔍 **Preserve original resolution**: No forced resize or interpolation  
  🔍 **保留原始分辨率**：不强制缩放或插值
- ⏱️ **Parallel execution**: Faster than sequential generation  
  ⏱️ **并行执行**：比逐个生成更快
- 🧩 **Seamless ComfyUI integration**: Outputs standard `IMAGE` tensors  
  🧩 **无缝集成 ComfyUI**：输出标准 `IMAGE` 张量

---

## 🔑 Requirements / 所需条件

- A valid **API key** from YK-AI  
  👉 Contact on WeChat: **`v:YK-ai001`**  
- 有效的 **YK-AI API 密钥**  
  👉 微信联系：**`v:YK-ai001`**

> ⚠️ This node requires internet access and an active YK-Banana2 Pro subscription.  
> ⚠️ 本节点需要联网，并依赖有效的 YK-香蕉2 Pro 订阅服务。

---

## 📥 Installation / 安装方法

1. Open your ComfyUI directory  
   进入你的 ComfyUI 根目录
2. Navigate to the `custom_nodes` folder  
   进入 `custom_nodes` 文件夹
3. Clone this repository:  
   克隆本仓库：

```bash
cd custom_nodes
git clone https://github.com/YOUR_GITHUB_USERNAME/ComfyUI-YK-Banana2-Batch.git
Restart ComfyUI
重启 ComfyUI
The node will appear as YK_Banana2_Batch in the node menu.

节点将在菜单中显示为 YK_Banana2_Batch。

🧪 Usage Guide / 使用说明
Input Slots (per task i = 1..10)
输入接口（每个任务 i = 1..10）
Input / 输入	Type / 类型	Description / 说明
image_i_1	IMAGE	Reference image 1 (e.g., person) / 参考图1（如人物）
image_i_2	IMAGE	Reference image 2 (e.g., clothing) / 参考图2（如服装）
image_i_3	IMAGE	Optional third reference / 可选第三张参考图
prompt_i	STRING	Prompt for this task / 本任务的提示词
📌 Example prompt / 示例提示词:

“将图2的衣服穿在图1人物的身上，保持图1的人物不变，保持图1的场景不变”

"Wear the clothes from image 2 on the person in image 1, keep the person, scene, and pose from image 1 unchanged."

Output Slots / 输出接口
output_1 to output_10: Generated images (IMAGE type)
output_1 到 output_10：生成的图像（IMAGE 类型）
Unused outputs return blank images (safe to ignore)
未使用的输出返回空白图（可安全忽略）
🛠️ Configuration / 配置方式
Set your API key via environment variable (recommended):

通过环境变量设置 API 密钥（推荐）：

Bash
编辑
export YK_BANANA2_API_KEY="your_api_key_here"
Or enter it directly in the node’s api_key field (less secure).

或直接在节点的 api_key 输入框中填写（安全性较低）。

📞 Support & Contact / 支持与联系
For API access, bug reports, or feature requests:

如需获取 API、反馈 Bug 或提出功能建议：

💬 WeChat / 微信: v:YK-ai001

📜 License / 开源协议
This project is licensed under the MIT License – see LICENSE for details.

本项目采用 MIT 许可证，详情见 LICENSE 文件。