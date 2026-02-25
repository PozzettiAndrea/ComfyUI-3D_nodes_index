12.15更新
1.修复了预览图像大小变化问题.

2.增加了一些实用设定，在A/D切换帧的同时，画笔可以一直保留，在处理批量连续帧的时候会快很多.

3.增加了通过鼠标滚轮调整画笔大小的功能.

4.增加了BBox和Square模式单独作用于这个节点所编辑的遮罩的功能，开启该功能后，使用这些模式的时候不会对原遮罩产生影响.


# ComfyUI MIKKY Video Mask Editor 🎬

一个功能强大的 ComfyUI 视频逐帧遮罩编辑节点。支持在 Web UI 中直接对视频帧进行绘制、修改遮罩，并提供自动包围盒转换、孔洞填充、边缘羽化以及视频切片功能。

A powerful frame-by-frame video mask editor for ComfyUI. Supports painting masks directly in the Web UI, with features like Auto BBox, Hole Filling, Blur/Feathering, and Video Slicing.

## ✨ 特性 / Features

*   **逐帧编辑 (Frame-by-Frame Editing)**: 在 ComfyUI 界面内直接预览视频流，并对每一帧进行遮罩绘制。
*   **智能绘制模式 (Smart Modes)**:
    *   `Original`: 原始手绘遮罩。
    *   `BBox`: 自动将手绘区域转换为最小包围盒 (Bounding Box)。
    *   `Square`: 自动将手绘区域转换为正方形 (适合模型训练或特定采样需求)。
*   **遮罩后处理 (Post-Processing)**:
    *   **Fill Holes**: 自动填充遮罩内部的闭合孔洞。
    *   **Blur/Feathering**: 支持遮罩边缘高斯模糊/羽化。
    *   **Padding**: 为 BBox 或 Square 模式增加额外的边距。
*   **视频切片 (Video Slicing)**: 通过 `start_frame` 和 `end_frame` 直接截取视频片段，节点将同时输出切片后的 `IMAGE` 和对应的 `MASK`。
*   **快捷键支持 (Hotkeys)**: 支持键盘快捷键快速切换帧，极大提高工作流效率。

## 📥 安装 / Installation

1.  进入你的 ComfyUI 插件目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本仓库：
    ```bash
    git clone https://github.com/XYMikky12138/ComfyUI-MIKKY-Video-Mask-Editor.git
    ```
3.  安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
4.  重启 ComfyUI。

## 🎮 操作指南 / UI Controls

在节点界面中：

*   **绘制 (Draw)**: `鼠标左键 (Left Click)`
*   **擦除 (Erase)**: `鼠标右键 (Right Click)`
*   **切换上一帧 (Previous Frame)**: `A` 键 或 `左箭头 (Left Arrow)`
*   **切换下一帧 (Next Frame)**: `D` 键 或 `右箭头 (Right Arrow)`
*   **清除当前帧 (Clear Current)**: 点击 `🗑 Current` 按钮
*   **清除所有帧 (Clear All)**: 点击 `🗑 All Frames` 按钮

## ⚙️ 参数说明 / Parameters

| 参数名 | 说明 |
| :--- | :--- |
| **images** | 输入的视频图像序列 (IMAGE)。 |
| **mode** | **Original**: 输出原始手绘形状。<br>**BBox**: 自动转为矩形包围盒。<br>**Square**: 自动转为正方形区域。 |
| **start_frame** | 切片起始帧 (包含)。 |
| **end_frame** | 切片结束帧 (不包含，设为 0 表示到最后)。 |
| **padding** | 在 BBox 或 Square 模式下，向外扩充的像素值。 |
| **fill_holes** | (Boolean) 是否自动填充遮罩内部的黑色孔洞。 |
| **blur_radius** | 遮罩边缘模糊半径 (0 表示不模糊)。 |
| **optional_mask** | (可选) 输入已有的 Mask，手绘内容将与此 Mask 叠加 (Union)。 |

## 📤 输出 / Outputs

*   **MASK**: 处理完成后的遮罩序列 (仅包含 start_frame 到 end_frame 范围内的帧)。
*   **IMAGE**: 切片后的图像序列 (与 MASK 一一对应)。

## 📝 Changelog

*   **Initial Release**: 发布基础版本，支持手绘、BBox转换及基础快捷键。

---
**Created by XYMikky12138**
