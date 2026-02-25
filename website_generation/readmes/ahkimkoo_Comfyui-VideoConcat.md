# ComfyUI 视频批处理插件 🎬

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen)](https://github.com/comfyanonymous/ComfyUI)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-4.0%2B-orange)](https://ffmpeg.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的专业视频批处理插件，提供强大的视频文件管理和合并功能，完全兼容 VideoHelperSuite 插件生态系统。

## ✨ 功能特性

### 🎯 核心节点

- **📂 BatchFilename**: 智能文件名批处理管理器
  - 逐步构建视频文件列表
  - 自动去重和路径标准化
  - 完全兼容 VideoHelperSuite 的 Select Filename 节点
  
- **🔗 VideoConcat**: 专业视频合并处理器
  - 高质量视频合并，保持音画同步
  - 智能分辨率统一和格式转换
  - 支持多种编码器和质量设置
  - **🎬 实时视频预览功能**

### 🎨 视频预览界面

- **🖥️ 现代化预览界面**: 模仿 VideoHelperSuite 的 Video Combine 节点
- **🎮 完整播放控制**: 播放、暂停、进度条、音量控制
- **🔧 丰富操作功能**: 打开、保存、隐藏预览
- **📱 响应式设计**: 适配不同节点大小和屏幕
- **🌗 暗色主题**: 与 ComfyUI 界面完美融合

### 🔗 完美兼容性

- ✅ **VideoHelperSuite 兼容**: 完全支持 VHS_FILENAMES 输出格式
- ✅ **ComfyUI 集成**: 标准节点接口和前端扩展
- ✅ **跨平台支持**: Windows、macOS、Linux

## 📥 安装指南

### 方法一：Git 克隆（推荐）

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/Comfyui-VideoConcat.git
cd Comfyui-VideoConcat
pip install -r requirements.txt
```

### 方法二：手动下载

1. 下载插件压缩包
2. 解压到 `ComfyUI/custom_nodes/Comfyui-VideoConcat` 目录
3. 安装依赖：`pip install -r requirements.txt`
4. 重启 ComfyUI

### 系统要求

- **ComfyUI**: 最新版本
- **Python**: 3.8 或更高版本
- **FFmpeg**: 4.0 或更高版本（需要 PATH 中可访问）
- **操作系统**: Windows 10+、macOS 10.14+、Ubuntu 18.04+

## 🚀 快速开始

### 基础工作流

1. **添加节点**: 在 ComfyUI 中添加 `BatchFilename` 和 `VideoConcat` 节点
2. **构建文件列表**: 使用 BatchFilename 逐步添加视频文件
3. **配置合并参数**: 设置帧率、编码器、质量等
4. **执行合并**: 运行工作流，自动显示视频预览

### 节点连接示例

```
[Select Filename] → [BatchFilename] → [VideoConcat] → [Preview]
      ↓                    ↓              ↓
  file_path          file_list    VHS_FILENAMES
```

## 📚 详细使用方法

### 📂 BatchFilename 节点

**输入参数**:
- `file` (必需): 要添加的单个文件路径
- `file_list` (可选): 现有的文件路径列表

**输出**:
- `file_list`: 更新后的文件路径列表

**功能说明**:
```python
# 第一次使用
file_list = BatchFilename(file="video1.mp4", file_list=None)
# 继续添加
file_list = BatchFilename(file="video2.mp4", file_list=file_list)
```

### 🔗 VideoConcat 节点

**输入参数**:
- `file_list` (必需): 要合并的视频文件列表
- `frame_rate` (可选): 输出帧率，默认 30.0
- `output_format` (可选): 输出格式，默认 "mp4"
- `video_codec` (可选): 视频编码器，默认 "libx264"
- `audio_codec` (可选): 音频编码器，默认 "aac"
- `video_quality` (可选): 视频质量 ("high", "medium", "low")
- `audio_bitrate` (可选): 音频比特率，默认 "128k"
- `output_filename` (可选): 自定义输出文件名

**输出**:
- `Filenames`: VHS_FILENAMES 格式的输出路径
- `video_info`: 详细的视频元数据信息

### 🎬 视频预览功能

视频合并完成后，VideoConcat 节点会自动显示预览界面：

- **🎮 播放控制**: 标准的视频播放控制条
- **📖 文件信息**: 显示输出文件名
- **🔗 操作按钮**:
  - `打开` (蓝色): 在新标签页打开视频
  - `保存` (绿色): 下载视频到本地
  - `隐藏` (红色): 隐藏预览界面

**右键菜单功能**:
- 显示/隐藏视频预览
- 刷新视频预览

## 📖 使用示例

### 示例 1: 基础视频合并

```python
# 构建文件列表
batch_node = BatchFilename()
file_list = batch_node.process_file("video1.mp4", None)
file_list = batch_node.process_file("video2.mp4", file_list)
file_list = batch_node.process_file("video3.mp4", file_list)

# 合并视频
concat_node = VideoConcat()
result = concat_node.concat_videos(
    file_list=file_list,
    frame_rate=30.0,
    output_format="mp4",
    video_quality="high"
)

vhs_filenames, video_info = result
print(f"输出文件: {vhs_filenames[1][0]}")
```

### 示例 2: 自定义配置

```python
# 高质量 4K 视频合并
result = concat_node.concat_videos(
    file_list=file_list,
    frame_rate=60.0,
    output_format="mov",
    video_codec="libx265",
    audio_codec="flac",
    video_quality="high",
    audio_bitrate="320k",
    output_filename="4k_master_video"
)
```

### 示例 3: ComfyUI 工作流

参考 `examples/basic_usage.py` 文件了解完整的工作流示例。

## ⚙️ 配置选项

### 视频编码器支持

| 编码器 | 质量 | 兼容性 | 推荐用途 |
|--------|------|--------|----------|
| libx264 | 高 | 优秀 | 通用视频 |
| libx265 | 极高 | 良好 | 4K/高质量 |
| libvpx-vp9 | 高 | 良好 | Web 视频 |
| mpeg4 | 中等 | 优秀 | 兼容性优先 |

### 输出格式支持

- **MP4**: 最通用的格式，推荐日常使用
- **AVI**: 兼容性好，适合旧设备
- **MOV**: 苹果生态系统，高质量
- **MKV**: 开源格式，功能丰富
- **WebM**: Web 优化格式

### 质量预设

| 预设 | CRF 值 | 比特率 | 适用场景 |
|------|--------|--------|----------|
| high | 18 | 自动 | 专业制作 |
| medium | 23 | 中等 | 一般用途 |
| low | 28 | 较低 | 快速预览 |

## 🔧 故障排除

### 常见问题

#### 1. 视频合并失败

**问题**: FFmpeg 执行失败，退出代码 1

**解决方案**:
- 确认 FFmpeg 已正确安装且在 PATH 中
- 检查输入视频文件是否存在和可读
- 验证视频文件格式是否受支持

```bash
# 检查 FFmpeg 安装
ffmpeg -version

# 检查文件信息
ffprobe input_video.mp4
```

#### 2. 分辨率不匹配错误

**问题**: "Input link parameters do not match"

**解决方案**:
插件自动处理分辨率统一，如果仍有问题：
- 确保所有输入视频都是有效的视频文件
- 检查视频是否损坏
- 尝试使用相同分辨率的视频

#### 3. 视频预览不显示

**问题**: 合并完成但预览界面不出现

**解决方案**:
- 检查浏览器控制台是否有 JavaScript 错误
- 确认输出文件确实生成
- 尝试右键节点选择 "显示视频预览"
- 清除浏览器缓存

#### 4. 音频同步问题

**问题**: 合并后音频和视频不同步

**解决方案**:
- 使用相同帧率的输入视频
- 确保音频采样率一致
- 尝试不同的音频编码器

### 调试模式

启用调试日志：
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

查看详细错误信息：
```bash
# 查看 ComfyUI 控制台输出
# 检查 logs/ 目录下的日志文件
```

## 🤝 兼容性说明

### VideoHelperSuite 兼容性

本插件与 [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) 完全兼容：

- ✅ **输出格式**: 支持 `VHS_FILENAMES` 格式
- ✅ **文件结构**: 使用相同的输出目录结构
- ✅ **节点接口**: 可与 VHS 节点无缝连接
- ✅ **预览功能**: 提供相似的预览体验

### 插件生态

可以与以下插件配合使用：
- VideoHelperSuite: 视频加载和基础处理
- ComfyUI-Manager: 插件管理
- 各种图像生成节点: 处理视频帧

## 📁 项目结构

```
Comfyui-VideoConcat/
├── __init__.py                 # 插件入口点
├── requirements.txt            # Python 依赖
├── README.md                   # 说明文档
├── nodes/                      # 节点实现
│   ├── __init__.py
│   ├── batch_filename.py       # BatchFilename 节点
│   ├── video_concat.py         # VideoConcat 节点
│   └── video_processor.py      # 视频处理核心
├── web/                        # 前端资源
│   ├── js/
│   │   └── video_concat_preview.js  # 预览 JavaScript
│   └── css/
│       └── video_concat_preview.css # 预览样式
├── examples/                   # 使用示例
│   └── basic_usage.py
├── tests/                      # 测试文件
└── docs/                       # 文档资源
```

## 🧪 测试

运行测试套件：

```bash
# 基础功能测试
python test_video_concat.py

# 预览功能测试
python test_video_preview.py

# VHS 兼容性测试
python test_vhs_compatibility.py

# 运行所有测试
python -m pytest tests/
```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🤝 贡献

欢迎贡献！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 开发指南

- 代码风格: 遵循 PEP 8
- 文档: 使用 Google 风格的 docstring
- 测试: 为新功能添加测试
- 兼容性: 确保与 ComfyUI 和 VideoHelperSuite 兼容

## 🆘 支持

如果您遇到问题或有建议：

- 📋 [提交 Issue](https://github.com/your-repo/Comfyui-VideoConcat/issues)
- 💬 [讨论区](https://github.com/your-repo/Comfyui-VideoConcat/discussions)
- 📧 Email: your.email@example.com

## 📊 更新日志

### v1.3.0 (最新)
- ✨ 添加实时视频预览功能
- 🎨 现代化预览界面设计
- 🔧 完善的播放控制和文件操作
- 📱 响应式界面设计

### v1.2.0
- 🔗 完全兼容 VideoHelperSuite
- 📁 VHS_FILENAMES 输出格式支持
- 🐛 修复分辨率不匹配问题

### v1.1.0
- 🚀 智能分辨率统一算法
- ⚡ 性能优化和错误处理改进
- 📝 详细的日志记录

### v1.0.0
- 🎉 初始版本发布
- 📂 BatchFilename 节点
- 🔗 VideoConcat 节点
- 🎬 基础视频合并功能

## 🙏 致谢

感谢以下项目和贡献者：

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的 AI 工作流平台
- [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) - 视频处理插件生态
- [FFmpeg](https://ffmpeg.org/) - 多媒体处理框架
- 所有贡献者和用户的反馈

---

<div align="center">
  <p>Made with ❤️ for the ComfyUI community</p>
  <p>
    <a href="#top">回到顶部</a> |
    <a href="https://github.com/your-repo/Comfyui-VideoConcat">GitHub</a> |
    <a href="https://github.com/your-repo/Comfyui-VideoConcat/issues">报告问题</a>
  </p>
</div>