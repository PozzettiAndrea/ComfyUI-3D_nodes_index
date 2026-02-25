# ComfyUI 3D Cinematic Pose Node

**[English Version Below]**

一个用于 ComfyUI 的交互式 3D 摄像机角度控制节点。通过可视化的 3D 小人模型，精准控制生成画面的**水平视角 (Horizontal)**、**垂直视角 (Vertical)** 和 **景别 (Distance/Zoom)**，并输出专业的电影摄影提示词（Cinematography Prompts）。

不再需要猜测 "30度侧面" 是什么样子，**所见即所得**。

![Node Screenshot](https://github.com/user-attachments/assets/placeholder-image-link)
*(建议上传一张节点运行截图并替换此链接)*

## ✨ 核心功能 (Key Features)

*   **🎨 交互式 3D 预览**: 内置 Three.js 驱动的 3D 视窗。支持鼠标左键拖拽旋转、滚轮缩放，操作顺滑流畅。
*   **🧭 全方位方向标记**: 即使在垂直俯视等刁钻角度，也能瞬间分清人物朝向：
    *   🔴 **红鼻子**: 指示正面 (Front)
    *   🔵 **蓝后脑**: 指示背面 (Back)
    *   🟢 **绿脚面**: 指示正向/脚尖 (Forward)
    *   🟡 **黄脚跟**: 指示后方/脚跟 (Backward)
*   **📝 专业摄影提示词**: 摒弃混乱的描述，基于角度阈值输出 Stable Diffusion / Flux 最易理解的专业术语：
    *   例如：`front-right three-quarter view` (前右斜侧视 - 最具立体感的角度), `overhead shot` (垂直俯视), `extreme close-up` (极特写)。
*   **🔄 双向同步**: 拖动 3D 模型会自动更新数值控件；修改数值控件也会实时更新 3D 模型。
*   **📸 截图输出**: 节点提供 `IMAGE` 输出端口，实时输出当前 3D 预览的截图，可直接连接 ControlNet 或用于参考图。

## 📦 安装方法 (Installation)

1.  进入你的 ComfyUI 插件目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本仓库：
    ```bash
    git clone https://github.com/wanjin123111/ComfyUI-3D-Human-Pose.git
    ```
3.  重启 ComfyUI。

## 🎮 使用说明 (Usage)

1.  **添加节点**: 在 ComfyUI 画布中右键 -> `3D Pose` -> `3D Cinematic Pose`。
2.  **操作 3D 视窗**:
    *   **左键拖拽**: 旋转摄像机（改变水平/垂直角度）。
    *   **鼠标滚轮**: 缩放（改变景别）。
3.  **连接输出**:
    *   `image`: 输出 3D 预览的截图（可用于 IPAdapter 或 ControlNet）。
    *   `prompt`: 输出计算好的英文提示词字符串（String），连接到 Clip Text Encode。

## 📐 提示词逻辑 (Prompt Logic)

本节点根据摄像机位置自动计算以下三个维度的提示词，确保生成的 Prompt 干净、准确：

### 1. 水平视角 (Horizontal View)
基于 8 方向罗盘逻辑，特别区分了**正侧面**与**斜侧面**：
- **Front View** (正视)
- **Three-quarter View** (3/4 侧视 - 同时看到正面和侧面)
- **Side Profile** (正侧视 - 纸片感)
- **Back View** (背视)

### 2. 垂直视角 (Vertical Angle)
- **Overhead shot / Bird's-eye view**: 垂直俯视 (>70°)
- **High angle shot**: 俯视
- **Eye level shot**: 平视
- **Low angle shot**: 仰视
- **Worm's-eye view**: 虫视/极低仰视 (<-50°)

### 3. 景别 (Shot Size)
- **Extreme Close-up**: 极特写
- **Close-up**: 近景
- **Medium Shot**: 中景
- **Full Body Shot**: 全身
- **Wide Shot**: 远景

---

# ComfyUI 3D Cinematic Pose Node

An interactive 3D camera control node for ComfyUI. Precisely control **Horizontal Angle**, **Vertical Angle**, and **Zoom (Distance)** using a visualized 3D mannequin, and output professional **Cinematography Prompts** automatically.

Stop guessing numbers. **What You See Is What You Get.**

## ✨ Key Features

*   **🎨 Interactive 3D Preview**: Built-in Three.js viewport. Rotate with drag, zoom with scroll. Smooth and responsive.
*   **🧭 Clear Orientation Markers**: Never lose track of direction, even at extreme angles or overhead shots:
    *   🔴 **Red Nose**: Indicates Front.
    *   🔵 **Blue Back-head**: Indicates Back.
    *   🟢 **Green Feet**: Indicates Forward.
    *   🟡 **Yellow Heels**: Indicates Backward.
*   **📝 Professional Prompts**: Generates precise terminology optimized for Stable Diffusion / Flux, avoiding messy adjectives:
    *   e.g., `front-right three-quarter view`, `overhead shot`, `extreme close-up`.
*   **🔄 Bi-directional Sync**: Dragging the 3D model updates the sliders; changing sliders updates the 3D model.
*   **📸 Snapshot Output**: Provides an `IMAGE` output allowing you to use the 3D preview snapshot for ControlNet or reference images.

## 📦 Installation

1.  Navigate to your custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/wanjin123111/ComfyUI-3D-Human-Pose.git
    ```
3.  Restart ComfyUI.

## 🎮 Usage

1.  **Add Node**: Right-click -> `3D Pose` -> `3D Cinematic Pose`.
2.  **Interact**:
    *   **Left Click + Drag**: Rotate camera (Horizontal/Vertical).
    *   **Scroll**: Zoom (Distance).
3.  **Outputs**:
    *   `image`: The visual snapshot of the 3D viewer.
    *   `prompt`: The generated text prompt string (connect to Clip Text Encode).

## 📐 Prompt Logic

### 1. Horizontal
Based on an 8-point compass system to distinguish between "Flat Side" and "Three-Quarter" (Depth) views.

### 2. Vertical
Precise thresholding for:
- **Overhead shot / Bird's-eye view** (>70°)
- **High angle shot**
- **Eye level shot**
- **Low angle shot**
- **Worm's-eye view** (<-50°)

### 3. Distance (Zoom)
Maps camera distance to standard cinematic shot sizes (Extreme Close-up to Wide Shot).

---
**License**: MIT