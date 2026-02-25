# ComfyUI-LLM

一个用于ComfyUI的LLM节点插件，支持调用各种LLM API。

## 功能特性

- 🚀 支持OpenAI兼容的API接口
- 🔧 可配置API地址、Token、模型等参数
- 📝 支持自定义系统提示词和用户输入
- 🎛️ 可调节温度和最大token数
- 📤 输出响应文本和完整JSON结果

## 安装方法

### 方法1：直接克隆到ComfyUI插件目录

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/10e9928a/ComfyUI-LLM.git
```

### 方法2：手动安装

1. 将此文件夹复制到 `ComfyUI/custom_nodes/` 目录下
2. 重启ComfyUI

## 使用方法

1. 在ComfyUI中，右键点击画布，选择 `Add Node` -> `ComfyUI-LLM` -> `LLM API Call`
2. 配置节点参数：
   - **api_url**: API端点地址（默认为OpenAI的地址）
   - **api_token**: 你的API密钥
   - **prompt**: 用户输入的提示词
   - **model**: 使用的模型名称（如 gpt-3.5-turbo）
   - **temperature**: 采样温度（0.0-2.0）
   - **max_tokens**: 最大生成token数
   - **system_prompt**: 系统提示词（可选）

3. 连接输出：
   - **response**: LLM返回的文本内容
   - **full_json**: 完整的JSON响应

## 支持的API

本插件支持所有OpenAI兼容的API，包括：

- OpenAI API
- Azure OpenAI
- 本地部署的LLM（如使用vLLM、text-generation-webui等）
- 其他兼容OpenAI格式的API服务

## 示例配置

### OpenAI API
```
api_url: https://api.openai.com/v1/chat/completions
api_token: sk-your-api-key-here
model: gpt-3.5-turbo
```

### 本地API
```
api_url: http://localhost:8000/v1/chat/completions
api_token: your-token-or-empty
model: your-local-model
```

## 依赖项

- requests

安装依赖：
```bash
pip install requests
```

## 注意事项

- 请妥善保管你的API密钥，不要泄露
- 根据你使用的API服务调整 `max_tokens` 参数
- 某些API可能需要不同的请求格式，请根据实际情况调整代码

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！
