# ComfyUI-free-drag-crop

[**English**](#english-version) | [**中文说明**](#中文说明) | [**Technical Highlights / 技术亮点**](#technical-highlights--技术亮点)

---

# English Version

A professional, high-precision interactive cropping node for ComfyUI. Drag, resize, and lock aspect ratios directly on the node's canvas.

![Node Preview](https://github.com/laolaoruqin/ComfyUI-free-drag-crop/raw/main/preview.png)

## Key Features 🚀

- **Interactive Canvas**: Drag to select, resize from 8-point handles, or move the entire selection area.
- **Real-Pixel Precision**: All calculations are based on original image dimensions to prevent resolution drifts.
- **Aspect Ratio Locking**: Lock your selection to a specific ratio and adjust boundaries while maintaining the frame.
- **Smart Presets**: Quick access to common ratios (4:3, 9:16, 9:20, 21:9, etc.).
- **Master Resets**: 
  - **Full Image Crop**: Expand to cover the entire image and automatically unlock the ratio for manual adjustment.
  - **No Crop**: Reset to origin (1x1) and clear all constraints.
- **Bilingual Help Sidebar**: Hover over the `?` icon to see a high-fidelity, adaptive instruction panel (English/Chinese) perfectly aligned with widgets.
- **Real-time Ratio Feedback**: The aspect ratio widget updates instantly during manual dragging to show actual `W:H` status.

## Installation 🛠️

1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/laolaoruqin/ComfyUI-free-drag-crop.git
   ```
3. Restart ComfyUI.

---

# 中文说明

为 ComfyUI 量身定做的专业级、高精度交互式裁剪节点。直接在画板上拖拽、缩放，并支持严格的比例锁定。

![节点预览](https://github.com/laolaoruqin/ComfyUI-free-drag-crop/raw/main/preview.png)

## 核心特性 🌟

- **交互式画板**：支持 8 点缩放、整体移动和拖拽选择。
- **真实像素精度**：所有计算均基于原图尺寸，彻底杜绝舍入误差造成的选区偏移。
- **比例锁定**：支持一键开启比例锁定（如 16:9），并在缩放边界时自动维持该比例。
- **比例预设**：内置常用比例（1:1, 4:3, 9:16, 9:20, 21:9 等）快速切换。
- **大师级重置**：
  - **Full Image Crop (全图自适应)**：一键铺满全图，并自动解除锁定以便自由调整。
  - **No Crop (清空裁剪)**：一键归零并重置所有限制。
- **双语交互式助手**：鼠标指向蓝色 `?` 图标可展开高保真、自适应宽高的中英双语详细说明面板。
- **实时比例反馈**：手动拖拽选区时，比例文本框会实时显示真实的像素宽度比（W:H）。

## 安装说明 📦

1. 进入 ComfyUI 的自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆本仓库：
   ```bash
   git clone https://github.com/laolaoruqin/ComfyUI-free-drag-crop.git
   ```
3. 重启 ComfyUI 即可使用。

---

# Technical Highlights / 技术亮点

> [!TIP]
> **[EN]** This node uses a high-performance rendering loop and a specialized "Resolution Stability Guard". Unlike other crop nodes that drift on large images, **Free Drag Crop** maintains sub-pixel accuracy even for 8K+ resolutions. Now with a fully adaptive, precision-aligned help UI for better accessibility.
>
> **[CN]** 该节点采用了高性能渲染循环和专门的“分辨率稳定性卫士”。与处理大图时容易产生偏移的其他裁剪节点不同，**Free Drag Crop** 即使在 8K+ 分辨率下也能保持亚像素级的精确度。现已配备全自适应、精准对齐的双语帮助面板，操作门槛更低。
