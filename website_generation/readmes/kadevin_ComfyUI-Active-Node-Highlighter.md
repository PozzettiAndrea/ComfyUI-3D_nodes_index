# ComfyUI Active Node Highlighter

[English](#english) | [中文](#中文)

---

## English

A lightweight ComfyUI extension that highlights the currently executing node by inverting its colors. When execution finishes, the node automatically restores to its original appearance.

### Features

- 🎨 **Color Inversion Highlight**: Inverts node colors during execution for clear visibility
- ⚡ **Minimal Performance Impact**: Event-driven design, no polling
- 🔧 **Zero Configuration**: Works out of the box
- 🔄 **Auto Restore**: Automatically restores original colors after execution
- ✅ **Frontend Compatible**: Works with both legacy LiteGraph and new Vue frontend

### Installation

#### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kadevin/ComfyUI-Active-Node-Highlighter.git
```

#### Method 2: Manual Download

1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/ComfyUI-Active-Node-Highlighter`
3. Restart ComfyUI

### Usage

No configuration needed. Simply run any workflow and watch the executing node highlight with inverted colors!

---

## 中文

一个轻量级的 ComfyUI 扩展，通过反转颜色的方式高亮当前正在执行的节点。执行完成后自动恢复原始外观。

### 功能特性

- 🎨 **颜色反转高亮**：执行时反转节点颜色，清晰可见
- ⚡ **最小性能开销**：事件驱动设计，无轮询
- 🔧 **零配置**：开箱即用
- 🔄 **自动恢复**：执行完成后自动恢复原始颜色
- ✅ **前端兼容**：同时支持旧版 LiteGraph 和新版 Vue 前端

### 安装方法

#### 方法一：Git 克隆（推荐）

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/kadevin/ComfyUI-Active-Node-Highlighter.git
```

#### 方法二：手动下载

1. 下载本仓库 ZIP 压缩包
2. 解压到 `ComfyUI/custom_nodes/ComfyUI-Active-Node-Highlighter`
3. 重启 ComfyUI

### 使用方法

无需任何配置。只需运行任意工作流，即可看到正在执行的节点以反转颜色高亮显示！

---

## License

MIT License - see [LICENSE](LICENSE)
