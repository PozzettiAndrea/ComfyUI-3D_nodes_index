# ComfyUI OpenAI Compatible API Node

一个支持 OpenAI 兼容 API 的 ComfyUI 自定义节点，可以调用任何兼容 OpenAI API 格式的大语言模型服务（如 vLLM、LM Studio、Ollama、LocalAI 等）。

## 功能特性

- ✅ 支持纯文本对话
- ✅ 支持图片+文本的视觉对话（Vision API）
- ✅ 完全兼容 OpenAI Chat Completions API 格式
- ✅ 支持自定义 API 端点
- ✅ 支持温度、最大 token 数等参数调节
- ✅ 支持图片细节控制（auto/low/high）

## 安装方法

### 方法一：直接克隆到 custom_nodes 目录

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/ComfyUI-OpenAI-Compatible-API.git
```

### 方法二：手动下载

1. 下载本仓库的所有文件
2. 将文件夹复制到 `ComfyUI/custom_nodes/` 目录下
3. 重启 ComfyUI

### 安装依赖

本节点需要以下 Python 包（ComfyUI 通常已包含）：

```bash
pip install requests pillow torch numpy
```

## 使用说明

### 基本参数

- **prompt**: 发送给模型的文本提示词
- **endpoint**: API 端点地址（例如：`http://localhost:3010/v1/chat/completions`）
- **model**: 模型名称或路径
- **max_tokens**: 最大生成 token 数（1-32000）
- **temperature**: 温度参数，控制生成的随机性（0.0-2.0）

### 可选参数

- **image**: 图片输入（支持 ComfyUI 的 IMAGE 类型）
- **api_key**: API 密钥（如果服务需要）
- **image_detail**: 图片细节级别
  - `auto`: 自动选择
  - `low`: 低细节（更快，更便宜）
  - `high`: 高细节（更详细，更慢）

## 使用示例

### 示例 1：纯文本对话

1. 添加 `OpenAI Compatible LLM` 节点
2. 设置 `endpoint` 为你的 API 地址
3. 设置 `model` 为模型名称
4. 在 `prompt` 中输入你的问题
5. 连接到输出节点查看结果

### 示例 2：图片+文本对话（视觉模型）

1. 添加 `Load Image` 节点加载图片
2. 添加 `OpenAI Compatible LLM` 节点
3. 将图片输出连接到节点的 `image` 输入
4. 在 `prompt` 中输入关于图片的问题（如 "描述这张图片"）
5. 确保 `model` 是支持视觉的模型（如 Qwen-VL、LLaVA 等）
6. 连接到输出节点查看结果

## 兼容的后端服务

本节点兼容任何实现了 OpenAI Chat Completions API 的服务：

- **vLLM**: 高性能推理服务器
- **Ollama**: 本地大模型运行工具
- **LM Studio**: 桌面端大模型应用
- **LocalAI**: 本地 AI API 服务
- **Text Generation WebUI**: OpenAI API 扩展
- **OpenAI 官方 API**: 需要设置正确的 endpoint 和 api_key

## 支持的视觉模型

如果要使用图片输入功能，你的模型需要支持视觉输入，例如：

- Qwen-VL / Qwen2-VL
- LLaVA
- MiniGPT-4
- BLIP-2
- CogVLM
- GPT-4 Vision（通过 OpenAI API）

## 注意事项

1. 确保你的 API 服务正在运行并且可访问
2. 如果使用图片输入，确保模型支持视觉功能
3. 某些服务可能需要 API 密钥
4. 超时时间设置为 120 秒，处理大图片或长文本时可能需要调整

## 故障排除

### 连接错误

- 检查 endpoint 地址是否正确
- 确认服务是否正在运行
- 检查防火墙设置

### 模型不支持图片

- 确认模型是否为视觉模型
- 检查 API 服务的日志
- 尝试纯文本对话测试连接

### API 密钥错误

- 确认 api_key 是否正确
- 检查服务是否需要认证

## 开发和贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 致谢

感谢 ComfyUI 社区和所有贡献者！
