中文：
ComfyUI Prompt Helper 是一个为 ComfyUI 用户设计的提示词管理与编辑工具，界面直观，减少重复劳动，让工作流更高效。

English：
ComfyUI Prompt Helper is a lightweight tool for managing and editing prompts in ComfyUI. It provides an intuitive UI that streamlines complex workflows and reduces manual work.

# ComfyUI Prompt Helper

一个 ComfyUI 自定义节点，用于处理中文提示词，生成适合不同模型的英文提示词及其翻译。

## 编写原因
- 有类似的节点，但是发现太重，响应速度也很慢
- 提示词太重要了，但英文的提示词有点难写，之前大部分都是复制粘贴，麻烦
- 尝试comfyui自定义开发流程，尝试用cursor开发


## 功能特点

- 支持多种模型类型（SD1.5、SDXL、FLUX）
- 支持多个 API 提供商（DeepSeek、OpenAI 等）
- 生成正向和负向提示词
- 提供中英文翻译
- 支持上下文关联
- 可配置的 API 密钥管理
- 支持代理设置

## 安装

1. 将本仓库克隆到 ComfyUI 的 `custom_nodes` 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Simlym/comfyui-prompt-helper.git
```

2. 安装依赖：
```bash
cd comfyui-prompt-helper
pip install -r requirements.txt
```

## 配置

编辑 `config.json` 文件，配置 API 密钥和其他设置：

```json
{
    "providers": {
        "DeepSeek": {
            "base_url": "https://api.deepseek.com",
            "api_key": "your_api_key_here",
            "models": [
                "deepseek-chat",
                "deepseek-reasoner"
            ]
        },
        "OpenAI": {
            "base_url": "https://api.openai.com",
            "api_key": "your_api_key_here",
            "models": [
                "gpt-4",
                "gpt-3.5-turbo"
            ]
        }
    },
    "default_provider": "DeepSeek",
    "default_model": "deepseek-chat",
    "settings": {
        "auto_save_api_key": false,
        "proxy": {
            "enabled": false,
            "http": "http://127.0.0.1:10808",
            "https": "http://127.0.0.1:10808"
        }
    }
}
```

## 使用方法

1. 在 ComfyUI 界面中找到 "conditioning" 类别
2. 添加 "Prompt LLM Helper" 节点
3. 配置以下参数：
   - 中文提示词：输入你想要转换的中文提示词
   - SD模型类型：选择目标模型（SD1.5、SDXL、FLUX）
   - 模型：选择要使用的 API 模型
   - 系统提示词：设置大模型的行为指导（可选）
   - API密钥：输入你的 API 密钥（可选，如果配置文件中已设置）
   - 使用上下文：是否启用上下文关联（可选）

## 输出

节点会生成四个输出：
- positive(en): 正向英文提示词
- negative(en): 负向英文提示词
- positive(zhs): 正向中文翻译
- negative(zhs): 负向中文翻译

## 注意事项

- 确保已正确配置 API 密钥
- 如果使用代理，请在配置文件中启用并设置代理地址
- API 密钥的优先级：界面输入 > 配置文件
- 如果启用了 `auto_save_api_key`，界面输入的 API 密钥会自动保存到配置文件

## 许可证

MIT 