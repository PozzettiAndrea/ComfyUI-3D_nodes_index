# ComfyUI 3D Angles Selector

[中文](#中文说明) | [English](#english)

---

## 中文说明

用于multi-angle LoRA 提示词生成的 ComfyUI 自定义节点。
LOAR 下载地址https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA
### 功能特点

- 3D 可视化角度选择器，支持鼠标拖拽旋转、滚轮缩放
- 简易角度选择器，通过下拉菜单快速选择
- 根据系统语言自动切换中英文界面
- 支持 8 个方位角 × 4 个仰角 × 3 个距离 = 96 种视角组合

### 安装

将本项目克隆到 ComfyUI 的 `custom_nodes` 目录：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jianglinbin/comfyui-angles-selector.git
```

重启 ComfyUI 即可使用。

### 节点说明

#### 3D角度选择器 (3D Angles Selector)

- 3D 球面可视化界面，点击选择多个角度点
- 支持三层距离（近景/中景/远景）的显示切换
- 输出：提示词列表

#### 简易角度选择器 (Simple Angles Selector)

- 三个下拉参数：方位角、仰角、距离
- 输出：单条提示词

### 提示词格式

```
<sks> [方位角] [仰角] [距离]
```

示例：`<sks> front-right quarter view elevated shot close-up`

### 参数对照表

| 方位角 | 仰角 | 距离 |
|--------|------|------|
| front view | low-angle shot | close-up |
| front-right quarter view | eye-level shot | medium shot |
| right side view | elevated shot | wide shot |
| back-right quarter view | high-angle shot | |
| back view | | |
| back-left quarter view | | |
| left side view | | |
| front-left quarter view | | |

---

## English

ComfyUI custom nodes for multi-angle LoRA prompt generation.
LOAR Download Url https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA
### Features

- 3D visual angle selector with mouse drag rotation and scroll zoom
- Simple angle selector with dropdown menus
- Auto language switching based on system locale (Chinese/English)
- Supports 8 azimuths × 4 elevations × 3 distances = 96 view combinations

### Installation

Clone this repository to ComfyUI's `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jianglinbin/comfyui-angles-selector.git
```

Restart ComfyUI to use.

### Nodes

#### 3D Angles Selector

- 3D spherical visualization, click to select multiple angle points
- Toggle visibility for three distance layers (close-up/medium/wide)
- Output: List of prompts

#### Simple Angles Selector

- Three dropdown parameters: Azimuth, Elevation, Distance
- Output: Single prompt

### Prompt Format

```
<sks> [azimuth] [elevation] [distance]
```

Example: `<sks> front-right quarter view elevated shot close-up`

### Parameter Reference

| Azimuth | Elevation | Distance |
|---------|-----------|----------|
| front view | low-angle shot | close-up |
| front-right quarter view | eye-level shot | medium shot |
| right side view | elevated shot | wide shot |
| back-right quarter view | high-angle shot | |
| back view | | |
| back-left quarter view | | |
| left side view | | |
| front-left quarter view | | |

### License

MIT
