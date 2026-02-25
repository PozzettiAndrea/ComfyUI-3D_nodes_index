# Gemini prompt generator JT version
Custom node to use Gemini 2.5/2.0 and above for Comfyui to generates theme related prompts for image generators
Fork from Magifactory, added many feature on top of it.

# 配置说明
1. 复制 `config.json.default` 为 `config.json`
2. 在 `config.json` 中填入您的 Gemini API 密钥：
```bash
{
    "GEMINI_API_KEY": "YOUR_API_KEY_HERE"
}
```

<img src="https://github.com/user-attachments/assets/fe987a9f-06c8-4a35-8de2-4b301007b266" width="400">

## 🚨 重要迁移提醒 (2025年更新)

**Gemini 1.5 Flash/Pro 已弃用！如果您仍在使用这些模型，请立即迁移以避免服务中断。**

### ⚡ 推荐的最新模型（全部免费可用）：

#### 🔥 主力推荐：
- **gemini-2.5-flash** - 🏆 最新混合推理模型，性价比最高，支持思维链推理
  - 💰 免费限制：**10 RPM, 250K TPM, 250 RPD**
  - ✅ 最适合：复杂推理任务、代码生成、高质量文本创作

- **gemini-2.0-flash** - 🎯 均衡的多模态模型，各种任务表现优异
  - 💰 免费限制：**15 RPM, 1M TPM, 200 RPD**  
  - ✅ 最适合：多模态任务、通用文本生成

#### 💡 经济选择：
- **gemini-2.5-flash-lite** - 💸 最经济实惠，适合大规模使用
  - 💰 免费限制：**15 RPM, 250K TPM, 1000 RPD**（每日请求数最高！）
  - ✅ 最适合：批量处理、简单任务、高频使用

- **gemini-2.0-flash-lite** - ⚡ 轻量级高效，成本最低
  - 💰 免费限制：**30 RPM, 1M TPM, 200 RPD**（每分钟请求数最高！）
  - ✅ 最适合：高频调用、轻量级任务

#### 🎓 高性能选择：
- **gemini-2.5-pro** - 🧠 最强大的模型，适用于极复杂任务
  - 💰 免费限制：**2 RPM, 125K TPM, 50 RPD**
  - ✅ 最适合：需要深度推理的复杂任务、专业内容创作

### 📊 免费层限制说明：
- **RPM** = 每分钟请求数 (Requests Per Minute)
- **TPM** = 每分钟Token数 (Tokens Per Minute) 
- **RPD** = 每日请求数 (Requests Per Day)

<img src="https://github.com/user-attachments/assets/bfe6831b-3189-43e8-bc5e-1fde60f24d4f" width="400">

## 💬 系统提示词重写支持

Added System prompt override support, it can turn into a LLM
Please, Leave the Override system prompt area empty, if you wish to use this node as a normal Prompt Generator.
Unless you have other needs.

<img src="https://github.com/user-attachments/assets/ad215761-d8ca-4d1a-bfb5-c774a0b70b66" width="400">

# 安装方法
cd your custom_nodes folder location
ie. E:\ComfyUI_windows_portable\ComfyUI\custom_nodes
then type following:

```bash
git clone https://github.com/LiJT/ComfyUI-Gemini-Prompt-Generator-JT
```

# 使用说明
The Seed actually is NOT for Gemini, just tell ComfyUI when to generate the new prompt, if the seed is fixed, then Node wont generate a new one
Input your API Key here: config.json 

<img src="https://github.com/user-attachments/assets/96a03508-8965-4960-8a9e-10e96e94b277" width="400">

## 🚨 关于Gemini 1.5 Flash模型无法使用的详细说明

### ❓ 为什么Gemini 1.5 Flash突然无法使用了？

根据Google官方政策的最新变更，**Gemini 1.5 Flash和1.5 Pro系列模型已被标记为"Legacy"（遗留）状态**：

#### 📅 重要时间节点：
1. **2025年4月29日起**：新项目无法访问1.5系列模型
2. **2025年9月24日**：所有1.5系列模型完全退役

#### 🤔 为什么有些人的1.5 Pro还能用？
- 如果您的API Key**之前使用过**1.5 Pro，暂时还可以继续使用
- 但这只是临时的，Google强烈建议立即迁移到新模型
- 新的API Key或项目已无法访问1.5系列模型

#### 📋 具体退役时间表：
- `gemini-1.5-flash-002`: **2025年9月24日**退役
- `gemini-1.5-pro-002`: **2025年9月24日**退役
- `gemini-1.5-flash-8b`: **2025年9月24日**退役

### 🔄 推荐迁移路径

| 从旧模型 | 迁移到新模型 | 理由 |
|---------|-------------|------|
| **1.5 Flash** | **2.5-flash-lite** 或 **2.0-flash** | 性能更强，免费配额更高 (2.5-lite: 1000 RPD!) |
| **1.5 Pro** | **2.5-flash** 或 **2.5-pro** | 更强性能，支持思维链推理 |
| **1.5 Flash-8B** | **2.0-flash-lite** 或 **2.5-flash-lite** | 轻量级替代，更高效 (2.0-lite: 30 RPM!) |

### 🎉 迁移到新模型的优势

#### 💰 更高的免费配额（根据官方2025年最新数据）
- **2.5-flash-lite**：每天可用 **1000 次请求** (RPD)，是老模型的数倍！
- **2.0-flash-lite**：每分钟可用 **30 次请求** (RPM)，适合高频调用
- **2.0-flash**：每分钟可用 **1M Token** (TPM)，处理长文本无压力
- **2.5-flash**：每天 **250 次请求**，支持思维链推理

#### 🚀 更好的性能  
- 新模型在各种基准测试中**表现更优**
- **2.5系列**支持**思维链推理**，让AI先"思考"再回答
- 更强的**多模态能力**（图像、音频、视频理解）
- 更准确的内容生成和更好的指令遵循能力

#### 💸 更低的成本
- 简化的定价结构，**更经济实惠**
- 部分模型的付费价格也更便宜
- 免费层配额大幅提升，减少付费需求

#### 🔧 新功能支持
- **思维链推理**：让AI"思考"后再回答，提升复杂任务准确性
- **更好的代码理解**和生成能力
- **增强的图像和视频理解**
- **更长的上下文窗口**，处理更多信息

### ⚡ 立即行动建议

1. **立即**将默认模型切换为新模型：
   - **通用推荐**：`gemini-2.5-flash` (10 RPM, 250K TPM, 250 RPD)
   - **高频使用**：`gemini-2.5-flash-lite` (15 RPM, 250K TPM, **1000 RPD**)
   - **快速响应**：`gemini-2.0-flash-lite` (**30 RPM**, 1M TPM, 200 RPD)
2. 测试新模型的性能，确保符合您的需求  
3. 更新您的工作流程和配置文件
4. **在2025年9月24日之前**完成完整迁移（1.5系列将完全退役）

### 🛠️ 如何在此节点中迁移

1. 打开ComfyUI，找到Gemini节点
2. 在模型下拉菜单中选择推荐的新模型（列表顶部的模型）
3. 测试生成效果，如果满意就保存工作流

**💡 提示**：新模型通常生成质量更好，您可能会发现提示词效果比以前更出色！

---

这样可以确保您的ComfyUI节点继续稳定运行，并享受到更好的性能和更低的成本。如果您在迁移过程中遇到任何问题，请查看节点的tooltip说明或参考官方文档。
