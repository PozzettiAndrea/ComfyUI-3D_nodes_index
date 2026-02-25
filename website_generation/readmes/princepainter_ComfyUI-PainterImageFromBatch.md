## 中文

### 简介
PainterImageFromBatch 是一个增强型 ComfyUI 自定义节点，用于从图片批次中提取单帧或连续帧。支持双向提取（从开头或末尾）、负索引和自动边界保护。
<img width="981" height="214" alt="image" src="https://github.com/user-attachments/assets/0baa7902-4a6c-4bcc-a606-811868573449" />

### 特性
- **双向提取**: 可从批次开头或末尾提取帧
- **负索引支持**: 使用负值从末尾开始计数
- **智能边界**: 自动裁剪防止越界错误
- **清晰参数**: 直观的控制选项和工具提示
- **安全保护**: 始终返回至少一帧有效结果

### 安装方法
1. 进入 `ComfyUI/custom_nodes/` 目录
2. 克隆仓库：
   ```bash
   git clone https://github.com/princepainter/ComfyUI-PainterImageFromBatch.git
   ```
3. 重启 ComfyUI

### 使用说明
在工作流中添加 **"Image From Batch (Painter)"** 节点。

#### 参数说明
- **image**: 输入的图片批次
- **start_from**: 选择 `"beginning"`（开头）或 `"end"`（末尾）作为参考点
- **start_frame**: 起始帧索引（支持负值）
- **frame_count**: 要提取的帧数量

#### 使用示例（81帧批次）
| 目标 | start_from | start_frame | frame_count | 结果 |
|------|------------|-------------|-------------|------|
| 提取视频首帧 | beginning | 0 | 1 | 第1帧 |
| 提取最后15帧 | end | -15 | 15 | 第67-81帧 |
| 提取66-81帧 | beginning | 65 | 16 | 第66-81帧 |
| 提取视频尾帧 | end | 0 | 1 | 最后1帧 |

### 许可证
MIT 许可证



---

## English

### Description
PainterImageFromBatch is an enhanced ComfyUI custom node for extracting one frame or contiguous frames from image batches. It supports bidirectional extraction (from start or end), negative indexing, and automatic boundary protection.
<img width="981" height="214" alt="image" src="https://github.com/user-attachments/assets/aa9bbe59-da76-43b5-909b-1debb67b6221" />

### Features
- **Dual-direction extraction**: Extract frames from batch beginning or end
- **Negative indexing**: Use negative values to count from the end
- **Smart boundaries**: Automatic clipping prevents out-of-bounds errors
- **Clear parameters**: Intuitive controls with tooltips
- **Error-safe**: Always returns at least one valid frame

### Installation
1. Navigate to `ComfyUI/custom_nodes/`
2. Clone the repository:
   ```bash
   git clone https://github.com/princepainter/ComfyUI-PainterImageFromBatch.git
   ```
3. Restart ComfyUI

### Usage
Add the **"Image From Batch (Painter)"** node to your workflow.

#### Parameters
- **image**: Input image batch
- **start_from**: Choose `"beginning"` or `"end"` as reference point
- **start_frame**: Starting frame index (supports negative values)
- **frame_count**: Number of frames to extract

#### Examples (81-frame batch)
| Goal | start_from | start_frame | frame_count | Result |
|------|------------|-------------|-------------|--------|
| Frames 1-15 | beginning | 0 | 15 | First 15 frames |
| Last 15 frames | end | -15 | 15 | Frames 67-81 |
| Frames 66-81 | beginning | 65 | 16 | Frames 66-81 |
| Last 10 frames | end | -10 | 10 | Frames 72-81 |

### License
MIT License

---

