# ComfyUI OpenAI 接口服务调用的自定义节点
#### 🌐 语言选择 / Language Selection
[![English](https://img.shields.io/badge/lang-English-blue.svg)](./README_EN.md)
[![中文](https://img.shields.io/badge/lang-中文-red.svg)](./README.md)

一个自定义的ComfyUI节点，集成了OpenAI兼容的API，用于本地或云端部署的大模型API服务（Ollama、LM Studio,Vllm, Mindie等）调用，用于绘画提示词生成和增强，专为Stable Diffusion，FLux等模型工作流程设计。支持中文输入

![微信截图_20250805130100](https://github.com/user-attachments/assets/48f8de78-fde4-4c5f-ba73-b239c3b11432)
## 功能特性

- 🤖 **OpenAI兼容API集成**：支持任何OpenAI兼容的API端点
- 🎨 **Stable Diffusion提示词增强**：自动扩展和改进提示词以获得更好的图像生成效果
- 🧠 **DeepSeek R1支持**：预配置了DeepSeek-R1-Distill-Qwen-32B模型
- 🧹 **清洁输出**：自动移除响应中的思考标签（`<think>`块）
- ⚙️ **灵活配置**：可自定义模型、温度、令牌数和API设置

## 安装方法

1. 导航到ComfyUI自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. 克隆此仓库：
   ```bash
   git clone https://github.com/PICOPON/ComfyUI-API-OpenAI-Node.git
   ```

3. 安装必需的依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 重启ComfyUI

## 使用方法

1. 将**OpenAI Node**添加到您的ComfyUI工作流程中
2. 根据需要配置节点参数
3. 将输出连接到所需的下游节点

### 节点参数

| 参数 | 类型 | 默认值 | 描述 |
|------|------|--------|------|
| `prompt` | STRING | "user prompts" | 要处理的输入提示词 |
| `system_prompt` | STRING | *Stable Diffusion提示词生成器* | AI的系统指令 |
| `model` | STRING | "DeepSeek-R1-Distill-Qwen-32B" | 要使用的模型名称 |
| `api_url` | STRING | "http://127.0.0.1:1935/v1" | API端点URL |
| `api_key` | STRING | "123" | API认证密钥 |
| `temperature` | FLOAT | 0.6 | 创造性水平（0.0-1.0） |
| `max_tokens` | INT | 1024 | 最大响应长度 |

### 默认系统提示词

节点预配置了针对Stable Diffusion优化的系统提示词：

```
You are a prompt generation AI. your task is to take a user input for a stable difusion prompt and output and expand the supplied prompt in a stable difusion format to provide better output. Do not deviate from the format. Do not output anything other than a stable diffusion prompt.Output English whatever the input language is.
```
*（您是一个提示词生成AI。您的任务是接收用户输入的stable diffusion提示词，并输出扩展后的stable diffusion格式提示词以提供更好的输出。不要偏离格式。除了stable diffusion提示词之外不要输出任何其他内容。）*

## 使用示例

### 基本用法
1. **输入**："一只猫"
2. **输出**："一只美丽蓬松的猫，详细的毛发纹理，明亮的眼睛，坐姿，柔和的光线，高质量，逼真，8k分辨率"

### 高级工作流程
```
文本输入 → OpenAI节点 → 文本处理 → 图像生成
```
### 参考流程文件AI_generated_Flux_flow.json （支持中文输入）
![微信截图_20250805131154](https://github.com/user-attachments/assets/e5e4f036-388b-42d3-91af-e2496cd2e545)
<img width="1912" height="962" alt="image" src="https://github.com/user-attachments/assets/c26761ca-4493-40e8-bf47-c5800f6913f0" />


## API兼容性

此节点支持：
- ✅ OpenAI API
- ✅ DeepSeek API
- ✅ 本地LLM服务器（Ollama、LM Studio,Vllm, Mindie等）
- ✅ 任何OpenAI兼容的端点

## 配置示例

### 本地服务器（Ollama）
- **API URL**：`http://localhost:1935/v1`
- **模型**：`DeepSeek-R1-Distill-Qwen-32B`或任何已安装的模型
- **API密钥**：保持为"123"或留空

### DeepSeek API
- **API URL**：`https://api.deepseek.com/v1`
- **模型**：`deepseek-chat`
- **API密钥**：您的DeepSeek API密钥

### OpenAI API
- **API URL**：`https://api.openai.com/v1`
- **模型**：`gpt-4`或`gpt-3.5-turbo`
- **API密钥**：您的OpenAI API密钥

## 详细功能

### 自动标签清理
节点自动移除AI响应中的`<think>`和`</think>`标签及其内容，确保下游处理的输出干净。

### 错误处理
- 网络超时保护（100秒）
- HTTP错误状态处理
- 异常捕获并提供描述性错误消息

### 灵活的API集成
- OpenAI兼容端点的自动URL补全
- 可选的API密钥认证
- 可配置的模型参数

## 故障排除

### 常见问题

**API连接错误**
- 检查API URL是否正确且可访问
- 如需认证，请验证您的API密钥
- 确保本地服务器正在运行（对于本地API）

**找不到模型**
- 验证您的API提供商的模型名称是否正确
- 检查您的账户/服务器中是否有该模型

**超时问题**
- 如需要，在代码中增加超时值
- 检查您的网络连接
- 验证API服务器状态

## 贡献

1. Fork此仓库
2. 创建您的功能分支（`git checkout -b feature/AmazingFeature`）
3. 提交您的更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 打开Pull Request

## 许可证

本项目采用GNU 3.0许可证 - 详情请参阅[LICENSE](LICENSE)文件。

## 致谢

- ComfyUI团队提供的优秀框架
- OpenAI提供的API标准
- DeepSeek提供的强大模型

## 支持

如果您遇到任何问题或有疑问：
1. 检查[Issues](https://github.com/yourusername/comfyui-openai-node/issues)页面
2. 创建新的issue并提供详细信息
3. 包括您的ComfyUI版本和错误日志

---

⭐ 如果这个节点对您的工作流程有帮助，请考虑给它一个星标！
