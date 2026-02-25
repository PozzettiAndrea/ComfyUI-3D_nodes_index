# ComfyUI-PowerVision 插件

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)

一个强大的 ComfyUI 视觉处理插件，集成了多种先进的计算机视觉和自然语言处理模型。

## ✨ 功能特性

- 🎯 **多模态理解**: 支持图像、视频和文本的联合处理
- 🔍 **目标检测**: 基于 Qwen-VL 的智能目标检测
- 🎨 **图像分割**: 使用 SAM2 进行精确的图像分割
- 💬 **视觉问答**: 支持图像理解和问答功能
- 🎬 **视频处理**: 支持视频内容理解和分析
- 🌐 **多语言支持**: 支持中英文界面和模型

## 🚀 快速开始

### 安装要求

- Python 3.8+
- ComfyUI
- CUDA 11.8+ (推荐，用于 GPU 加速)
- 8GB+ 内存 (推荐 16GB+)
- **transformers >= 4.57.0** (Qwen3-VL 模型最低要求)

### 安装步骤

1. **克隆插件到 ComfyUI 自定义节点目录**:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/whmc76/ComfyUI_PowerVision.git
   ```

2. **安装依赖**:
   ```bash
   cd ComfyUI_PowerVision
   pip install -r requirements.txt
   ```

3. **启动 ComfyUI**:
   ```bash
   cd ../../  # 回到 ComfyUI 根目录
   python main.py
   ```

### 模型下载

插件会自动下载所需的模型文件。首次使用时请确保网络连接正常。

## 📖 使用指南

### 基本节点

#### 1. PowerVision 图像理解节点
- **功能**: 对图像进行深度理解和分析
- **输入**: 图像、文本提示
- **输出**: 理解结果、置信度分数

#### 2. 目标检测节点
- **功能**: 检测图像中的目标对象
- **输入**: 图像、检测类别
- **输出**: 检测框、标签、置信度

#### 3. 图像分割节点
- **功能**: 对图像进行精确分割
- **输入**: 图像、分割提示
- **输出**: 分割掩码、分割结果

### 工作流示例

查看 `examples/` 目录中的示例工作流文件，了解如何使用各种节点。

## 📋 模型支持

### Qwen3-VL 模型

本插件支持最新的 Qwen3-VL 系列模型，包括：

- **Qwen3-VL-2B-Instruct**: 轻量级模型，适合快速推理
- **Qwen3-VL-4B-Instruct**: 平衡性能和速度
- **Qwen3-VL-8B-Instruct**: 高性能模型，适合复杂任务

#### 版本要求

- **transformers >= 4.57.0**: Qwen3-VL 模型的最低要求
- 推荐使用最新稳定版本以获得最佳性能和兼容性
- 如果遇到模型加载问题，请检查 transformers 版本是否满足要求

#### 模型特性

- 支持图像、视频和文本的多模态理解
- 优化的视觉推理能力
- 改进的多模态交互体验

## 🛠️ 开发指南

### 项目结构

```
ComfyUI_PowerVision/
├── __init__.py              # 插件入口
├── nodes.py                 # 主要节点定义
├── utils.py                 # 工具函数
├── models/                  # 模型相关代码
│   ├── qwen_vl.py          # Qwen-VL 模型
│   └── sam2.py             # SAM2 模型
├── web/                     # 前端资源
│   ├── js/                 # JavaScript 文件
│   └── css/                # CSS 文件
├── examples/                # 示例工作流
├── tests/                   # 测试文件
├── requirements.txt         # 依赖列表
├── README.md               # 项目说明
├── rules.md                # 开发规范
└── .gitignore              # Git 忽略文件
```

### 添加新节点

1. 在 `nodes.py` 中定义新节点类
2. 实现必要的输入/输出类型
3. 添加错误处理逻辑
4. 更新 `NODE_CLASS_MAPPINGS`
5. 编写测试用例

### 代码规范

请参考 `rules.md` 文件了解详细的代码规范和开发标准。

## 🧪 测试

运行测试套件:

```bash
python -m pytest tests/
```

运行特定测试:

```bash
python -m pytest tests/test_nodes.py -v
```

## 📝 更新日志

### v1.5.0 (2024-12-19)
- 🎥 Qwen2.5-VL 视频处理采用帧采样策略
- 🎯 解决视频处理内存不足问题
- ⚡ 优化内存使用和性能
- 🔧 统一视频输入处理逻辑
- 📈 采样模式下支持更多生成令牌

### v1.4.0 (2024-12-19)
- 🎬 支持直接视频输入处理
- 🔧 重构节点结构，移除重复节点
- 🐛 修复视频文件识别和处理问题
- ⚡ 优化性能和内存使用
- 🧹 清理代码，提升可读性

### v1.3.0 (2024-12-18)
- 🎯 集成 Qwen3-VL 模型支持
- 💬 多模态视觉问答功能
- 🎨 图像和视频理解能力
- 🔍 目标检测和分割功能

### v1.0.0 (2024-01-XX)
- 🎉 初始版本发布
- ✨ 支持 Qwen-VL 模型
- ✨ 支持 SAM2 分割模型
- ✨ 基础图像处理功能
- 📚 完整的文档和示例

## 🤝 贡献

我们欢迎社区贡献！请查看 [贡献指南](CONTRIBUTING.md) 了解如何参与开发。

### 贡献方式

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

本项目基于以下开源项目进行开发，特此感谢：

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 优秀的节点式 AI 工作流界面
- [Qwen-VL](https://github.com/QwenLM/Qwen-VL) - 强大的多模态大语言模型
- [SAM2](https://github.com/facebookresearch/segment-anything-2) - 先进的图像分割模型
- [ComfyUI_Qwen3-VL-Instruct](https://github.com/ComfyUI/ComfyUI_Qwen3-VL-Instruct) - Qwen3-VL 模型集成参考
- [Comfyui_Object_Detect_QWen_VL](https://github.com/ComfyUI/Comfyui_Object_Detect_QWen_VL) - 目标检测功能参考

详细的来源声明请查看 [ATTRIBUTION.md](ATTRIBUTION.md) 文件。

## 📞 支持

如果您遇到问题或有建议，请：

1. 查看 [常见问题](FAQ.md)
2. 在 [Issues](https://github.com/whmc76/ComfyUI_PowerVision/issues) 中搜索相关问题
3. 创建新的 Issue 描述您的问题
4. 加入我们的社区

## 🔗 相关链接

- [ComfyUI 官方文档](https://github.com/comfyanonymous/ComfyUI)
- [Qwen-VL 项目](https://github.com/QwenLM/Qwen-VL)
- [SAM2 项目](https://github.com/facebookresearch/segment-anything-2)
- [ComfyUI Registry](https://registry.comfy.org)

---

**注意**: 本插件需要大量的计算资源，建议使用 GPU 进行加速。首次使用时会自动下载模型文件，请确保网络连接稳定。
