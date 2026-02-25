# ComfyUI Wireless Transmission Nodes

**English** | [中文](#中文)

A clean, lightweight ComfyUI plugin to transmit data wirelessly between nodes using a global key-value store. This helps clean up messy "spaghetti" workflows by removing long connecting wires.

## Features
- **Zero Latency**: Uses internal Python dictionary storage.
- **Strict Typing**: Separate nodes for `Any`, `Image`, and `Latent` to ensure compatibility with ComfyUI's visual cues.
- **Pass-through**: Set nodes pass the value through, allowing linear workflow continuation.
  
## Nodes Included
1. **Universal**: `Set Wireless (Any)` / `Get Wireless (Any)` 
   - Accepts **ALL** data types (Wildcard `*`).
   - Supports complex types: `Model`, `VAE`, `CLIP`, `Conditioning`, `Mask`.
   - Supports primitive types: `INT` (steps, width, height), `FLOAT` (fps), `STRING` (prompts).
2. **Image**: `Set Wireless (Image)` / `Get Wireless (Image)` - Blue connections.
3. **Latent**: `Set Wireless (Latent)` / `Get Wireless (Latent)` - Orange connections.

## Installation

### Method 1: Git Clone (Recommended)
1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ComfyUI-Wireless.git
   ```
3. Restart ComfyUI.

### Method 2: Manual Installation
1. Download the ZIP file of this repository.
2. Extract it into your `ComfyUI/custom_nodes/` folder.
3. Ensure the folder is named `ComfyUI-Wireless`.
4. Restart ComfyUI.

## Usage

### Basic Linking
1. Add a **Set Wireless** node. Connect your data and give it a unique Key (e.g., `face_image`).
2. Place a **Get Wireless** node anywhere else. Enter the same Key (`face_image`).
3. The data is now wirelessly transferred!

### Multiple Channels (Example)
You can create multiple independent channels by using different keys:
- **Channel 1**: Set Node (Key: `1`) ➔ Get Node (Key: `1`)
- **Channel 2**: Set Node (Key: `2`) ➔ Get Node (Key: `2`)
- **Channel A**: Set Node (Key: `model_base`) ➔ Get Node (Key: `model_base`)

Make sure the **Key** strings match exactly between the Set and Get nodes you want to pair.
We know it’s easy to accidentally copy a stray space when pasting your key. That’s why we’ve added an auto-trim feature—it automatically removes spaces at the beginning and end, making sure your key works perfectly every time.

## License
This project is licensed under the MIT License.

---

# 中文 (Chinese)

# ComfyUI 无线传输节点

**中文** | [English](#english)

一个简洁、轻量级的 ComfyUI 插件，用于通过全局键值对在节点之间无线传输数据。通过移除长距离的连线，帮助你清理混乱的“面条式”工作流。

## 特性
- **零延迟**: 使用 Python 内部字典存储，速度极快。
- **严格类型**: 提供 `Any` (通用)、`Image` (图像) 和 `Latent` (潜空间) 的专用节点，完美适配 ComfyUI 的端口颜色系统。
- **透传设计**: Set 节点支持数据透传，不打断原有的线性工作流。

## 包含的节点
1. **通用型**: `Set Wireless (Any)` / `Get Wireless (Any)` 
   - 接受 **所有** 数据类型 (通配符 `*`)。
   - 支持复杂类型：`Model` (模型), `VAE`, `CLIP`, `Conditioning` (条件), `Mask` (遮罩)。
   - 支持基础类型：`INT` (步数, 宽, 高), `FLOAT` (帧率), `STRING` (文本)。
2. **图像型**: `Set Wireless (Image)` / `Get Wireless (Image)` - 对应蓝色端口。
3. **潜空间型**: `Set Wireless (Latent)` / `Get Wireless (Latent)` - 对应橙色端口。

## 安装方法

### 方法 1: Git Clone (推荐)
1. 进入你的 ComfyUI `custom_nodes` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. 克隆本仓库（请将下方链接替换为实际仓库地址）：
   ```bash
   git clone https://github.com/your-username/ComfyUI-Wireless.git
   ```
3. 重启 ComfyUI。

### 方法 2: 手动安装
1. 下载本仓库的 ZIP 压缩包。
2. 将其解压到 `ComfyUI/custom_nodes/` 目录下。
3. 确保文件夹名称为 `ComfyUI-Wireless`。
4. 重启 ComfyUI。

## 使用说明

### 基础连接
1. 添加一个 **Set Wireless** 节点。连接你的数据并给它起一个唯一的 Key（例如 `face_image`）。
2. 在工作流的任何其他位置放置一个 **Get Wireless** 节点。输入相同的 Key（`face_image`）。
3. 数据即可无线传输！

### 多通道示例
你可以通过不同的 Key 创建多个独立的通道，最简单的“Set 1 对应 Get 1”：
- **通道 1**: Set 节点 (Key: `1`) ➔ Get 节点 (Key: `1`)
- **通道 2**: Set 节点 (Key: `2`) ➔ Get 节点 (Key: `2`)
- **通道 A**: Set 节点 (Key: `model_base`) ➔ Get 节点 (Key: `model_base`)

**注意**：Set 和 Get 节点之间的 **Key** 必须完全一致才能成功配对。为了彻底防止因手误（多打空格）导致的问题，我设置了代码自动帮你去除 Key 前后的空格（Trim），这样无论你是否不小心加了空格，只要字符匹配就能成功传输。

## 许可证
本项目采用 MIT 许可证授权。
