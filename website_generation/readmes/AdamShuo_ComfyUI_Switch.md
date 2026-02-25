# ComfyUI Switch Any Node

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[English](./README.md) | [中文](./README.md#comfyui-switch-any-节点-中文说明)

This is a custom node for ComfyUI that provides a dynamic "Switch" for routing purposes. It allows you to define a list of named labels and select one, outputting the corresponding index and label name. This is useful for controlling the flow of your workflow based on a selection.

---

## Features

- **Clean Initial State**: New nodes start completely empty with no preset data, ready for custom configuration.
- **Dynamic Label Inputs**: Start with a single label input. As you fill them in, new empty inputs appear automatically after a refresh.
- **UI Refresh Button**: A **"Save & Refresh UI"** button is included directly on the node. This saves your current labels and reloads the ComfyUI interface in one click, updating the dropdown menu and input fields instantly.
- **No Data Input**: This node is purely for routing and does not take any data inputs. It only outputs the selected `index` (INT) and `label` (STRING).
- **Persistent Labels**: Your list of labels is saved in a JSON file within the node's directory, so they persist across ComfyUI sessions.
- **Order Preservation**: Labels maintain their original input order in the dropdown menu, ensuring consistent index-label correspondence.
- **Workflow Migration**: All label states are fully preserved when migrating workflows between different machines.

## How to Use

1.  **Add the Node**: Add the `Switch Any` node to your workflow.
2.  **Define Labels**:
    - Initially, you will see one input field, `label_1`. Enter a name for your first route (e.g., "SDXL").
    - To add more labels, you can fill in the next available input field (`label_2`, etc.).
    - **Note**: Labels are processed in the exact order they are entered, maintaining index-label correspondence.
3.  **Save and Refresh**:
    - Click the **"Save & Refresh UI**" button on the node.
    - The page will automatically reload.
4.  **Select a Label**:
    - After reloading, the `select_label` dropdown menu will be populated with all the labels you defined, displayed in their original input order.
    - The node will now show all your saved labels plus one new empty input field for the next one.
5.  **Get Output**: The node will output the 1-based `index` and the `label` string of your selection from the dropdown menu. The index corresponds exactly to the input order.

## Installation

1.  Clone or download this repository.
2.  Place the `ComfyUI_Switch` folder into the `ComfyUI/custom_nodes/` directory.
3.  Restart ComfyUI.

---

# ComfyUI Switch Any 节点 (中文说明)

这是一个为 ComfyUI 设计的自定义节点，提供了一个用于路由目的的动态“切换”功能。它允许您定义一个带名称的标签列表并从中选择一个，然后输出对应的索引和标签名。这对于根据选择来控制您的工作流非常有用。

---

## 功能特性

- **干净的初始状态**: 新节点完全为空，不包含预设数据，可进行自定义配置。
- **动态标签输入**: 从一个标签输入框开始。当您填写后，刷新界面即可自动出现新的空输入框。
- **UI 刷新按钮**: 节点上直接集成了一个 **"Save & Refresh UI"** 按钮。一键即可保存当前所有标签并重新加载 ComfyUI 界面，即时更新下拉菜单和输入框。
- **无数据输入**: 这是一个纯粹的路由节点，不接收任何数据输入。它只输出所选的 `index` (整数) 和 `label` (字符串)。
- **标签持久化**: 您的标签列表会保存在节点目录下的一个 JSON 文件中，因此可以在不同的 ComfyUI 会话之间保持不变。

## 如何使用

1.  **添加节点**: 在工作流中添加 `Switch Any` 节点。
2.  **定义标签**:
    - 最初，您会看到一个输入框 `label_1`。为您的第一个路由输入一个名称 (例如 "SDXL")。
    - 要添加更多标签，只需填写下一个可用的输入框 (`label_2` 等) 即可。
3.  **保存并刷新**:
    - 点击节点上的 **"Save & Refresh UI"** 按钮。
    - 页面将会自动重新加载。
4.  **选择标签**:
    - 重新加载后，`select_label` 下拉菜单中将填充您定义的所有标签。
    - 节点现在会显示所有已保存的标签，并额外提供一个新的空输入框供您继续添加。
5.  **获取输出**: 节点将输出您从下拉菜单中所选项的 `index` (从1开始的整数) 和 `label` (字符串)。

## 安装方法

1.  克隆或下载此仓库。
2.  将 `ComfyUI_Switch` 文件夹放入 `ComfyUI/custom_nodes/` 目录下。
3.  重启 ComfyUI。

---

## 更新日志

### 修复的问题
- ✅ **index-label对应关系**: 修复了标签索引与显示名称不对应的问题
- ✅ **下拉框排序**: 修复了下拉菜单中标签按字母排序而非输入顺序的问题  
- ✅ **工作流迁移**: 修复了工作流迁移时标签数量和状态丢失的问题

### 技术改进
- 优化了标签处理逻辑，保持原始输入顺序
- 改进了空字符串和空白字符串的过滤机制
- 增强了工作流迁移时的数据完整性