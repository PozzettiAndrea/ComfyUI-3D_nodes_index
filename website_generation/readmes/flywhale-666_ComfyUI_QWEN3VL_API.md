# ComfyUI QWEN3VL API 节点

这是一个 ComfyUI 自定义节点插件，集成了阿里云 Qwen3-VL 多模态大模型的 API 调用功能，支持图像理解和视频理解。还支持批量加载图片和视频，由于是调用了API，所以就不需要再COMFYUI里升级transformers了，你的其他节点就能用了！

## 🖼️ 工作流示例

![示例](1.png)

## ✨ 功能特性

- 🖼️ **图像理解**：使用 Qwen3-VL 模型分析图像内容
- 🎬 **视频理解**：使用 Qwen3-VL 模型分析视频内容
- 💬 **文本对话生成**：使用 Qwen3/Qwen-Plus/Qwen-Flash 进行多轮对话
- 📝 **文本处理**：提供去换行、去空行、去空格、添加编号、统计字数等功能
- ✂️ **文本操作**：支持添加前缀/后缀、删除内容等多种文本编辑操作
- 📁 **批量加载图像**：从文件夹批量加载图像文件
- 📂 **批量加载视频**：从文件夹批量加载视频文件
- 🔀 **多种排序方式**：支持字母、数字、时间等多种排序方式
- 🌐 **中英文支持**：配合 DD-Translation 插件实现完整中文化

## 📦 安装

### 方法一：通过 ComfyUI Manager 安装（推荐）

1. 打开 ComfyUI Manager
2. 搜索 `ComfyUI_QWEN3VL_API`
3. 点击安装

### 方法二：手动安装

1. 克隆本仓库到 ComfyUI 的 `custom_nodes` 目录：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/flywhale-666/ComfyUI_QWEN3VL_API
```

2. 安装依赖：

```bash
cd ComfyUI_QWEN3VL_API
pip install -r requirements.txt
```

## 🔑 配置 API Key

1. 前往 [阿里云](https://bailian.console.aliyun.com/?tab=model#/api-key) 获取 API Key

2. 在插件目录下创建或编辑 `api_key.ini` 文件：

```ini
DASHSCOPE_API_KEY=你的API密钥
```

## 🎯 节点说明

### 1. QWEN3 文本对话生成

支持多轮对话的文本生成节点。

**输入**：
- `model`：模型选择（qwen3-max / qwen-plus / qwen-flash）
- `user_prompt`：用户输入的问题或指令
- `system_prompt`：系统提示词，定义AI的角色和行为
- `temperature`：温度参数（0.0-2.0），控制回答的创造性
- `top_p`：核采样参数（0.0-1.0），控制回答的随机性
- `seed`：随机种子，控制输出的一致性
- `conversation_history`：对话历史（可选，JSON格式）

**输出**：
- `response`：AI的回复内容
- `conversation_history`：更新后的对话历史（可循环连接实现多轮对话）

**使用提示**：
- 单次对话：直接使用，不连接 `conversation_history` 输入
- 多轮对话：将 `conversation_history` 输出连接回自己的输入端，实现连续对话

### 2. QWEN3-VL 图像理解

分析单张图像内容。

**输入**：
- `image`：图像输入（IMAGE类型）
- `model`：模型选择（qwen3-vl-flash / qwen3-vl-plus / qwen-vl-max）
- `user_prompt`：提示词，描述你想让模型做什么
- `seed`：随机种子，控制输出的一致性

**输出**：
- `text`：模型分析结果（文本）

### 3. QWEN3-VL 视频理解

分析视频内容。

**输入**：
- `video_path`：视频文件路径（字符串）
- `video`：视频输入（VIDEO类型，可选）
- `model`：模型选择
- `user_prompt`：提示词
- `seed`：随机种子

**输出**：
- `text`：模型分析结果（文本）

### 4. QWEN3-VL 加载图像(文件夹)

从指定文件夹批量加载图像文件。

**输入**：
- `folder_path`：文件夹路径
- `image_limit`：加载数量上限（0表示不限制）
- `start_index`：起始索引
- `sort_method`：排序方式
  - None（无排序）
  - Alphabetical (ASC/DESC)（字母顺序）
  - Numerical (ASC/DESC)（数字顺序）
  - Datetime (ASC/DESC)（修改时间）

**输出**：
- `images`：图像列表（IMAGE类型）
- `file_paths`：文件路径列表（STRING类型）

**支持格式**：jpg, jpeg, png, bmp, gif, webp, tiff, tif

### 5. QWEN3-VL 加载视频(文件夹)

从指定文件夹批量加载视频文件。

**输入**：
- `folder_path`：文件夹路径
- `video_limit`：加载数量上限（0表示不限制）
- `start_index`：起始索引
- `sort_method`：排序方式（同上）

**输出**：
- `videos`：视频列表（VIDEO类型）
- `file_paths`：文件路径列表（STRING类型）

**支持格式**：mp4, avi, mov, mkv, webm, flv, wmv, mpeg, mpg

### 6. QWEN 文本处理

提供常用的文本处理功能，支持两个主操作。

**输入**：
- `text`：待处理的文本（必须连接输入）
- `main_operation_1`：第一个主操作
- `main_operation_2`：第二个主操作

**操作选项**：
- 不改变：保持原文本
- 去换行：移除所有换行符
- 去空行：移除空白行
- 去空格：移除所有空格和制表符
- 添加编号：为每个非空行添加序号（格式：1.内容）
- 统计字数：统计字符总数

**输出**：
- `text`：处理后的文本
- `count`：统计数值（添加编号时为段落数，统计字数时为字符数）

### 7. QWEN 文本操作

提供5个操作槽位的文本编辑功能，按顺序执行。

**输入**：
- `text`：待操作的文本（必须连接输入）
- `operation_1~5`：操作类型选择
- `content_1~5`：对应操作的内容参数

**操作选项**：
- 无：跳过该操作槽
- 添加前缀：在整个文本开头添加内容
- 每段添加前缀：为每个非空行开头添加内容
- 添加后缀：在整个文本末尾添加内容
- 删除开始内容：删除第一次出现的指定内容
- 删除结束内容：删除最后一次出现的指定内容
- 删除指定内容：删除所有匹配的内容

**输出**：
- `text`：操作后的文本

### 8. QWEN API Key

用于在工作流中传递 API Key，作为可选的配置方式。

**输入**：
- `api_key`：API 密钥字符串

**输出**：
- `api_key`：传递给其他节点使用

**使用提示**：可以将此节点的输出连接到其他节点的 `api_key` 输入端，优先级高于 `api_key.ini` 文件。

## 💡 使用示例

### 示例 1：多轮文本对话

1. 添加 `QWEN3 文本对话生成` 节点
2. 设置 `system_prompt`（如："你是一个专业的写作助手"）
3. 输入第一个问题到 `user_prompt`
4. 将 `conversation_history` 输出连接回输入，实现连续对话
5. 每次修改 `user_prompt` 后执行，保持对话上下文

### 示例 2：批量图像分析

1. 使用 `QWEN3-VL 加载图像(文件夹)` 节点加载图像
2. 连接到 `QWEN3-VL 图像理解` 节点进行分析
3. 输出分析结果

### 示例 3：视频内容理解

1. 使用 `QWEN3-VL 加载视频(文件夹)` 节点加载视频
2. 连接到 `QWEN3-VL 视频理解` 节点进行分析
3. 获取视频内容描述

### 示例 4：文本处理流水线

1. 使用 `QWEN3 文本对话生成` 或其他节点获取文本
2. 使用 `QWEN 文本处理` 节点清理文本（如去空行、添加编号）
3. 使用 `QWEN 文本操作` 节点进行格式化（如每段添加前缀）
4. 输出处理后的文本供后续使用

## 🌐 中文化支持

本插件支持 [ComfyUI-DD-Translation](https://github.com/Dontdrunk/ComfyUI-DD-Translation) 插件的自动翻译功能。

安装 DD-Translation 后，将项目中的 `ComfyUI_QWEN3VL_API.json` 文件复制到 DD-Translation 插件的 `zh-CN/Nodes/` 目录下，节点界面即可自动显示中文。

```bash
# 复制翻译文件
cp ComfyUI_QWEN3VL_API.json ../ComfyUI-DD-Translation/zh-CN/Nodes/
```

## 📝 可用模型

### 视觉理解模型
- `qwen3-vl-flash`：快速模型，适合实时应用
- `qwen3-vl-flash-2025-10-15`：指定版本的快速模型
- `qwen3-vl-plus`：增强模型，更强的理解能力
- `qwen3-vl-plus-2025-09-23`：指定版本的增强模型
- `qwen-vl-max`：最强模型，最佳效果

### 文本对话模型
- `qwen3-max`：最强性能，适合复杂任务
- `qwen-plus`：平衡性能，适合通用场景
- `qwen-flash`：快速响应，适合简单对话

## ⚠️ 注意事项

1. **API Key 安全**：请妥善保管 API Key，不要将其提交到公开仓库
2. **API 费用**：使用阿里云 DashScope API 会产生费用，请注意额度管理
3. **视频大小限制**：超大视频文件可能导致 API 调用失败或超时
4. **网络连接**：需要稳定的网络连接访问阿里云 API

## 🔧 依赖项

- `openai`：OpenAI 兼容接口库
- `torch`：PyTorch（ComfyUI 已包含）
- `Pillow`：图像处理库（ComfyUI 已包含）

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📮 联系方式

如有问题或建议，请在 GitHub 上提交 Issue。

## 🙏 致谢

- [Alibaba Cloud DashScope](https://dashscope.aliyuncs.com/)：提供强大的多模态大模型 API
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)：优秀的 Stable Diffusion 图形界面
- [ComfyUI-DD-Translation](https://github.com/Dontdrunk/ComfyUI-DD-Translation)：节点中文化支持# ComfyUI_QWEN3VL_API

