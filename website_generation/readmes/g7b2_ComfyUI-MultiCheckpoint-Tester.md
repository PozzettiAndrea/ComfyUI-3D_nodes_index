# ComfyUI Multi-Checkpoint Tester

一个功能强大的 ComfyUI 自定义节点，专为模型对比测试设计。支持一次性加载多个 Checkpoint 模型，自动管理显存，并生成带有独立文件名的对比图。

## ✨ 主要功能

- **批量对比**：支持同时输入 1-5 个 Checkpoint 模型进行对比。
- **显存保护**：内置自动显存清理机制（GC + Soft Empty Cache），防止显存溢出 (OOM)。
- **智能保存**：
  - 文件名自动递增（`filename_01.png`, `filename_02.png`），不覆盖旧图。
  - 自动将 Tensor 维度转换为 ComfyUI 标准预览格式 `[B,H,W,C]`。
- **元数据保留**：生成的图片包含完整的工作流元数据（Prompt, Seed 等），支持拖入 ComfyUI 复现。
- **异常处理**：如果某个模型加载失败，会自动跳过并继续处理下一个，不会导致整个工作流崩溃。

## 🔧 安装方法

### 方法 1: 手动安装
1. 进入 ComfyUI 的 `custom_nodes` 目录。
2. 打开终端/CMD，运行：
   ```bash
   git clone https://github.com/g7b2/ComfyUI-MultiCheckpoint-Tester.git