# ComfyUI WhisperX Pro

简体中文 | [English](README_EN.md)

ComfyUI 专业自定义节点，使用 [WhisperX](https://github.com/m-bain/whisperx) 提供精确的音频文本对齐和 SRT 字幕生成功能。

## ✨ 功能特性

- 🎯 **精确对齐**：使用 WhisperX 实现词级时间戳对齐
- 🎬 **SRT 字幕生成**：自动生成 SRT 格式字幕文件，支持自定义格式
- 🌍 **多语言支持**：支持 9 种语言（英语、中文、法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、日语）
- 🌐 **双语界面**：节点界面根据系统语言自动在中英文之间切换
- 📦 **本地模型加载**：从 ComfyUI/models 目录加载对齐模型 - 无需自动下载
- ⚡ **GPU 加速**：支持 CUDA 以获得更快的处理速度
- 🎛️ **灵活配置**：可自定义行时长、字符限制和标点触发器
- 🔧 **轻松集成**：与 ComfyUI 音频加载节点无缝集成

## 📋 目录

- [安装](#-安装)
- [模型设置](#-模型设置)
- [节点概述](#-节点概述)
- [使用示例](#-使用示例)
- [支持的语言](#-支持的语言)
- [配置建议](#-配置建议)
- [故障排除](#-故障排除)
- [致谢](#-致谢)

## 🚀 安装

### 步骤 1：安装自定义节点

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/loockluo/comfyui-whisperx-pro.git
cd comfyui-whisperx-pro
pip install -r requirements.txt
```

### 步骤 2：安装 WhisperX（如需要）

如果自动安装失败，可以手动安装 WhisperX：

```bash
pip install git+https://github.com/m-bain/whisperx.git
```

对于 CUDA GPU 支持，请确保安装了带 CUDA 的 PyTorch：

```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 步骤 3：重启 ComfyUI

安装完成后，重启 ComfyUI 以加载新节点。

## 📦 模型设置

### 模型目录结构

模型必须放置在：`ComfyUI/models/whisperx/[模型文件夹名称]/`

节点将根据选择的语言自动加载相应的对齐模型。

### 下载预训练对齐模型

#### 选项 1：HuggingFace（全球）

下载完整的模型文件夹（所有文件，包括 `config.json`、`pytorch_model.bin`、`preprocessor_config.json`、`tokenizer_config.json`、`vocab.json`）：

- **英语**：[wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english)
- **中文**：[wav2vec2-large-xlsr-53-chinese-zh-cn](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn)
- **法语**：[wav2vec2-large-xlsr-53-french](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-french)
- **德语**：[wav2vec2-large-xlsr-53-german](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-german)
- **西班牙语**：[wav2vec2-large-xlsr-53-spanish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish)
- **意大利语**：[wav2vec2-large-xlsr-53-italian](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-italian)
- **葡萄牙语**：[wav2vec2-large-xlsr-53-portuguese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-portuguese)
- **日语**：[wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese)
- **荷兰语**：[wav2vec2-large-xlsr-53-dutch](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-dutch)

#### 选项 2：魔塔社区（国内更快）

- **英语**：[wav2vec2-large-xlsr-53-english](https://modelscope.cn/models/jonatasgrosman/wav2vec2-large-xlsr-53-english)
- **中文**：[wav2vec2-large-xlsr-53-chinese-zh-cn](https://modelscope.cn/models/jonatasgrosman/wav2vec2-large-xlsr-53-chinese-zh-cn)
- 其他语言类似

### 示例：安装中文模型

```bash
cd ComfyUI/models/whisperx

# 从模型页面下载所有文件，并放置在：
# wav2vec2-large-xlsr-53-chinese-zh-cn/
#   ├── config.json
#   ├── pytorch_model.bin
#   ├── preprocessor_config.json
#   ├── tokenizer_config.json
#   └── vocab.json
```

## 📦 节点概述

### WhisperX SRT 生成器

该节点将文本与音频对齐，并生成带有精确词级时间戳的 SRT 字幕格式输出。

#### 输入参数

| 参数 | 类型 | 默认值 | 范围 | 描述 |
|------|------|--------|------|------|
| `audio` | AUDIO | 必需 | - | 来自 ComfyUI 官方音频加载器的音频数据 |
| `text` | STRING | 必需 | - | 要与音频对齐的文本内容 |
| `language` | DROPDOWN | `zh` | en/fr/de/es/it/pt/nl/ja/zh | 对齐模型的语言代码 |
| `max_sec` | FLOAT | 4.5 | 1.0 - 10.0 | 每行字幕的最大时长（秒） |
| `max_ch` | INT | 28 | 10 - 100 | 每行字幕的最大字符数 |
| `punct` | STRING | `，。！？；、,.!?;…` | - | 触发换行的标点符号 |
| `device` | DROPDOWN | `auto` | auto/cuda/cpu | 用于处理的设备 |

#### 输出结果

| 输出 | 类型 | 描述 |
|------|------|------|
| `SRT字幕内容` | STRING | 生成的带时间戳的 SRT 字幕内容 |
| `对齐信息` | STRING | 关于对齐过程的 JSON 元数据 |

#### 输出示例

**SRT 内容：**
```srt
1
00:00:00,520 --> 00:00:02,350
大家好。

2
00:00:02,350 --> 00:00:04,180
今天我们来讨论

3
00:00:04,180 --> 00:00:06,890
WhisperX 这个工具。
```

**对齐信息：**
```json
{
  "language": "zh",
  "device": "cuda",
  "audio_duration_seconds": 10.5,
  "text_length": 87,
  "aligned_words": 15,
  "subtitle_lines": 8,
  "max_duration_per_line": 4.5,
  "max_characters_per_line": 28,
  "punctuation_triggers": "，。！？；、"
}
```

## 🎯 使用示例

### 前置要求

您首先需要一个 ComfyUI 音频加载节点。安装以下任一选项：
- **ComfyUI-Advanced-Audio**：提供 "Load Audio" 节点
- 或任何其他输出 AUDIO 类型的 ComfyUI 音频加载器

### 基本工作流

1. **添加音频加载节点**
   - 添加 "Load Audio" 节点（来自 ComfyUI-Advanced-Audio 或类似插件）
   - 设置音频文件路径

2. **添加 WhisperX SRT 生成器节点**
   - 在工作流中添加 "WhisperX SRT Generator" 节点
   - 将音频加载器的 `audio` 输出连接到该节点

3. **配置参数**
   - 设置 `language` 以匹配您的音频（例如，英语为 "en"，中文为 "zh"）
   - 在 `text` 字段中粘贴您的转录文本
   - 调整时间参数：
     - `max_sec`：控制每行字幕的时长
     - `max_ch`：控制每行的字符数
     - `punct`：指定哪些标点符号触发换行

4. **运行和导出**
   - 执行工作流
   - 节点将输出 SRT 格式的字幕
   - 使用文本输出节点将输出保存为 `.srt` 文件

### 示例 1：英语视频字幕

**场景**：您有一个英语视频并想生成字幕

```
设置：
- 语言：en
- 最大时长：4.5 秒
- 最大字符数：28
- 标点符号：,.!?;…

输入文本：
"Hello everyone. Today we're going to talk about WhisperX. It's an amazing tool for speech recognition and alignment. Let me show you how it works."

输出：
自动生成 4-6 行字幕，具有精确的词级时间戳
```

### 示例 2：中文音频字幕

**场景**：您有一个中文播客并想生成字幕

```
设置：
- 语言：zh
- 最大时长：4.5 秒
- 最大字符数：28
- 标点符号：，。！？；、

输入文本：
"大家好。今天我们来讨论一下WhisperX这个工具。它是一个非常强大的语音识别和对齐工具。让我来给大家演示一下它的使用方法。"

输出：
自动生成遵循中文标点规则的字幕行
```

### 示例 3：多语言内容

对于混合多种语言的内容，请为 `language` 参数使用主要语言，或分别处理每个语言段。

## 🌍 支持的语言

| 语言 | 代码 | 所需模型 |
|------|------|----------|
| 英语 | `en` | wav2vec2-large-xlsr-53-english |
| 中文 | `zh` | wav2vec2-large-xlsr-53-chinese-zh-cn |
| 法语 | `fr` | wav2vec2-large-xlsr-53-french |
| 德语 | `de` | wav2vec2-large-xlsr-53-german |
| 西班牙语 | `es` | wav2vec2-large-xlsr-53-spanish |
| 意大利语 | `it` | wav2vec2-large-xlsr-53-italian |
| 葡萄牙语 | `pt` | wav2vec2-large-xlsr-53-portuguese |
| 荷兰语 | `nl` | wav2vec2-large-xlsr-53-dutch |
| 日语 | `ja` | wav2vec2-large-xlsr-53-japanese |

## ⚙️ 配置建议

### 优化字幕行长度

**短行（max_ch: 15-20，max_sec: 2-3）**
- ✅ 适用于：社交媒体视频、移动端观看
- ✅ 优点：易于阅读，适合快节奏内容
- ❌ 缺点：字幕切换频繁，可能分散注意力

**中等行（max_ch: 25-35，max_sec: 3-5）**
- ✅ 适用于：大多数标准视频、演示文稿
- ✅ 优点：可读性和字幕频率平衡
- ⭐ **推荐默认值**

**长行（max_ch: 40-60，max_sec: 5-8）**
- ✅ 适用于：纪录片、讲座、慢节奏内容
- ✅ 优点：字幕切换较少，可见上下文更多
- ❌ 缺点：可能难以阅读，尤其是在小屏幕上

### 标点符号配置

**英语：**
```
推荐：,.!?;…
```

**中文：**
```
推荐：，。！？；、
如果内容是混合的，包含英文标点：，。！？；、,.!?
```

**日语：**
```
推荐：。！？、
```

### 设备选择

- **auto**：自动选择 CUDA（如果可用），否则选择 CPU（推荐）
- **cuda**：强制 GPU 处理（更快，需要带 CUDA 的 NVIDIA GPU）
- **cpu**：强制 CPU 处理（较慢，但在所有系统上都能工作）

**性能比较：**
- CUDA（GPU）：比 CPU 快约 10-30 倍
- CPU：较慢但在所有地方都能工作，适合测试

## 🔧 故障排除

### 问题："WhisperX is not installed"

**解决方案：**
```bash
pip install git+https://github.com/m-bain/whisperx.git
```

如果失败，请先尝试安装 PyTorch：
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install git+https://github.com/m-bain/whisperx.git
```

### 问题："Failed to align any words"

**可能的原因和解决方案：**

1. **音频太短**：使用长度超过 2-3 秒的音频片段
2. **音频质量问题**：确保清晰的语音，没有过多的背景噪音
3. **语言不匹配**：确保选择的语言与音频匹配
4. **文本-音频不匹配**：验证文本内容与口述内容匹配
5. **音频格式不正确**：尝试将音频转换为 WAV 格式（16kHz，单声道）

### 问题："Out of memory" 错误

**解决方案：**
1. 切换到 CPU：将 `device` 设置为 "cpu"
2. 处理更短的音频段
3. 关闭其他应用程序以释放内存
4. 升级 GPU 内存（对于 CUDA 用户）

### 问题：模型无法从本地目录加载

**检查：**
1. 模型文件在正确的目录中：`ComfyUI/models/whisperx/[模型文件夹名称]/`
2. 所有必需的文件都存在：`config.json`、`pytorch_model.bin`、`preprocessor_config.json`、`tokenizer_config.json`、`vocab.json`
3. 模型文件夹名称与语言代码映射匹配（例如，英语为 "wav2vec2-large-xlsr-53-english"）

### 问题：SRT 时间戳不准确

**解决方案：**
1. 确保文本与口述内容完全匹配
2. 尝试调整 `max_sec` 和 `max_ch` 参数
3. 检查音频质量和清晰度
4. 验证语言选择是否正确

## 📝 系统要求

- **Python**：3.8 或更高版本
- **PyTorch**：2.0 或更高版本
- **ComfyUI**：推荐最新版本
- **CUDA**：可选，用于 GPU 加速（CUDA 11.7 或更高版本）

### 磁盘空间要求

- 基础安装：约 500 MB
- 每个语言模型：约 1.2 GB
- 典型安装（2-3 种语言）：3-4 GB

## 🙏 致谢

- [WhisperX](https://github.com/m-bain/whisperx) by Max Bain - 高级音频文本对齐
- [OpenAI Whisper](https://github.com/openai/whisper) - 基础语音识别模型
- [Wav2Vec2](https://huggingface.co/transformers/model_doc/wav2vec2.html) - Facebook AI 的对齐模型
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的 Stable Diffusion 节点化 UI

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🤝 支持

- **问题反馈**：[GitHub Issues](https://github.com/loockluo/comfyui-whisperx-pro/issues)
- **讨论交流**：[GitHub Discussions](https://github.com/loockluo/comfyui-whisperx-pro/discussions)
- **贡献代码**：欢迎提交 Pull Request！

## 🗺️ 开发路线图

- [ ] 添加批处理支持
- [ ] 支持其他字幕格式（VTT、ASS）
- [ ] 字幕时间的实时预览
- [ ] 自定义模型微调支持
- [ ] 自动标点恢复

---

如果您觉得这个项目有帮助，请在 GitHub 上给我们一个 ⭐！
