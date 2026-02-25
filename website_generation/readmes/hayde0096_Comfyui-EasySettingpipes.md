# ComfyUI Easy Setting Pipes

[English](#english) | [中文](#中文)

---

## 中文

### 简介

ComfyUI Easy Setting Pipes 是一套为 ComfyUI 设计的实用工具节点集合，旨在简化工作流、提高生产效率。该插件包含三大核心功能模块，可以有效减少节点数量，提升工作流的整洁度和可维护性。

### 核心功能

#### 1. 采样器配置节点 (Sampler Setup)

将采样的所有关键参数打包到单个节点中，减少布线和节点数量：

**主要特性：**

- **参数集成**：steps（步数）、cfg（引导系数）、clip_skip（CLIP层跳过）、sampler（采样器）、scheduler（调度器）、width（宽度）、height（高度）、batch_size（批次大小）
- **快速交换**：一键交换宽高值，方便快速切换纵横比
- **解包功能**：支持将打包的参数拆分为单独输出，灵活适配各种节点
- **空间节省**：显著减少工作流中的连接线和节点数量

**可用节点：**

- `SamplerSetup`：将采样参数打包成单一数据管道
- `SamplerSetupUnpack`：将打包的参数拆分为单独的输出

**参数说明：**

| 参数 | 默认值 | 范围 | 说明 |
|------|--------|------|------|
| steps | 20 | -1000~1000 | 采样步数 |
| cfg | 7.0 | -100~100 | 无条件引导强度 |
| clip_skip | -1 | -100~100 | CLIP编码器跳过层数（-1为不跳过） |
| sampler_name | - | - | 选择采样算法（euler、dpmpp等） |
| scheduler | - | - | 噪声调度器类型 |
| width | 1024 | 32~8192 | 生成图像宽度（8像素递增） |
| height | 1024 | 32~8192 | 生成图像高度（8像素递增） |
| swap_wh | False | True/False | 快速交换宽高值 |
| batch_size | 1 | 1~128 | 批处理大小 |

#### 2. Power LoRA 加载器与堆栈 (Power LoRA Loader & Stacker)

专业级 LoRA 管理工具，支持动态加载和管理多达 100 个 LoRA 模型：

**主要特性：**
- **多模型管理**：在单个节点中管理多达 100 个 LoRA 模型
- **拖拽排序**：直观的拖拽界面，轻松调整 LoRA 加载顺序
- **灵活的强度模式**：支持单强度模式和双强度模式（Model/Clip 分离）
- **可视化反馈**：彩色编码的强度控制和状态指示器
- **批量控制**：一键启用/禁用所有 LoRA
- **右键菜单**：快捷菜单支持快速启用/禁用或删除 LoRA
- **智能缓存**：避免重复加载相同的 LoRA 文件，提升性能

**可用节点：**

**Power LoRA Loader**

- 功能：加载并应用 LoRA 模型到基础模型和 CLIP 编码器
- 输入：model（模型）、clip（CLIP编码器）、optional lora_stack（可选LoRA堆栈）
- 输出：model（处理后的模型）、clip（处理后的CLIP）
- 特点：
  - 支持单强度和双强度两种模式
  - 可与其他 LoRA 加载器链接，实现多级加载
  - 强度为 0 时自动跳过加载，节省性能


**Power LoRA Stacker**

- 功能：创建 LoRA 堆栈供其他节点使用（如 Efficiency 节点）
- 输入：optional lora_stack（可选，用于堆栈链接）
- 输出：lora_stack（LoRA 配置堆栈）
- 特点：
  - 兼容各类基于堆栈的工作流
  - 支持单强度和双强度模式
  - 格式：`[(lora_name, model_strength, clip_strength), ...]`


**强度模式说明：**

点击强度模式按钮可在两种模式间切换：

- **单强度模式**：单一强度值同时应用于 Model 和 CLIP
- **双强度模式（Model/Clip 模式）**：为 Model 和 CLIP 分别设置强度
  - 左值（橙色）：Model 强度
  - 右值（青色）：Clip 强度

**使用技巧：**

- 点击数值可直接输入精确数值
- 点击两侧的上下按钮可微调强度（步长 0.05）
- 拖拽数值左右可平滑调整强度
- 点击开关按钮可启用/禁用单个 LoRA


#### 3. 通用类型转换节点 (Convert Any)

实用工具节点，用于解决某些采样节点无法直接使用标准采样器和调度器输入的兼容性问题：

**功能：**

- 接受任意类型的输入
- 原样返回输入值，不进行任何修改
- 用作类型适配器，绕过 ComfyUI 的类型检查限制


### 安装

#### 方法一：ComfyUI Manager（推荐）

1. 打开 ComfyUI Manager
2. 搜索 'Easy Setting Pipes'
3. 点击安装按钮

#### 方法二：手动安装

1. 进入 ComfyUI 自定义节点文件夹：

```bash
cd ComfyUI/custom_nodes/
```

2. 克隆此仓库：

```bash
git clone https://github.com/user-attachments/Comfyui-EasySettingPipes.git
```

3. 重启 ComfyUI

### 使用指南

#### Sampler Setup 节点使用步骤

1. 添加 `SamplerSetup` 节点到工作流
2. 配置所需的采样参数（详见上方参数说明表）
3. 将 `setup_pipe` 输出连接到其他节点
4. 如需获取单独参数，可使用 `SamplerSetupUnpack` 节点进行拆包

**使用示例：**

```txt
[SamplerSetup] → setup_pipe → [KSampler]
或
[SamplerSetup] → setup_pipe → [SamplerSetupUnpack] → 单独参数输出
```

#### Power LoRA 节点使用步骤

1. 添加 `Power LoRA Loader` 或 `Power LoRA Stacker` 节点
2. 点击 "Add LoRA" 按钮从模型库中选择 LoRA 文件
3. 调整强度值：
   - 直接点击数值输入框输入精确数值
   - 使用上下箭头按钮微调（步长 0.05）
   - 拖拽数值进行平滑调整
4. 点击开关按钮启用/禁用单个 LoRA
5. 使用 "Toggle All" 按钮一键启用/禁用所有 LoRA

**高级用法：**

- **LoRA 链接**：将 Loader 的输出连接到另一个 Loader，实现多级加载
- **堆栈模式**：使用 Stacker 创建堆栈，兼容 Efficiency 等基于堆栈的节点


### 系统要求

- **ComfyUI 版本**：2024+ 及更新版本
- **Python**：3.9+
- **操作系统**：Windows、Linux、macOS

### 许可证

MIT License

### 致谢与灵感

- 灵感来自 ComfyUI 社区的高效工作流设计
- 核心技术参考来自 rgthree 和 pythongosssss 的开源项目
- 旨在提供更友好的用户体验和更灵活的节点设计

---

## English

### Overview

ComfyUI Easy Setting Pipes is a suite of utility nodes designed for ComfyUI to streamline workflows and improve productivity. This plugin features three core modules that effectively reduce node count and enhance workflow clarity and maintainability.

### Core Features

#### 1. Sampler Setup Nodes

Consolidates all critical sampling parameters into a single node, reducing wiring and node complexity:

**Key Features:**

- **Parameter Integration**: steps, cfg, clip_skip, sampler, scheduler, width, height, batch_size
- **Quick Swap**: One-click width/height exchange for convenient aspect ratio switching
- **Unpack Function**: Split packed parameters into individual outputs for flexible node compatibility
- **Space Saving**: Significantly reduce connection lines and node count in workflows

**Available Nodes:**

- `SamplerSetup`: Pack sampling parameters into a single data pipe
- `SamplerSetupUnpack`: Unpack parameters into individual outputs

**Parameter Reference:**

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| steps | 20 | -1000~1000 | Number of sampling steps |
| cfg | 7.0 | -100~100 | Classifier-free guidance scale |
| clip_skip | -1 | -100~100 | CLIP encoder layer skip count (-1 for no skip) |
| sampler_name | - | - | Sampling algorithm (euler, dpmpp, etc.) |
| scheduler | - | - | Noise scheduler type |
| width | 1024 | 32~8192 | Generated image width (increments by 8) |
| height | 1024 | 32~8192 | Generated image height (increments by 8) |
| swap_wh | False | True/False | Quick swap width and height |
| batch_size | 1 | 1~128 | Batch processing size |

#### 2. Power LoRA Loader & Stacker

Professional-grade LoRA management tool supporting dynamic loading and management of up to 100 LoRA models:

**Key Features:**
- **Multi-Model Management**: Manage up to 100 LoRA models in a single node
- **Drag & Drop Reordering**: Intuitive drag interface for easy LoRA ordering adjustment
- **Flexible Strength Modes**: Single strength mode and dual strength mode (Model/Clip separate)
- **Visual Feedback**: Color-coded strength controls and state indicators
- **Batch Control**: One-click enable/disable all LoRAs
- **Context Menu**: Quick access to enable/disable or delete LoRAs
- **Smart Caching**: Avoids redundant LoRA file loading for improved performance

**Available Nodes:**

**Power LoRA Loader**
- Function: Load and apply LoRA models to base model and CLIP encoder
- Inputs: model, clip, optional lora_stack
- Outputs: model (processed), clip (processed)
- Features:
  - Supports single strength and dual strength modes
  - Chainable with other LoRA loaders for multi-stage loading
  - Auto-skips loading when strength is 0 for performance optimization

**Power LoRA Stacker**

- Function: Create LoRA stacks for use with other nodes (e.g., Efficiency nodes)
- Inputs: optional lora_stack (for stack chaining)
- Outputs: lora_stack (LoRA configuration stack)
- Features:
  - Compatible with stack-based workflows
  - Supports single and dual strength modes
  - Format: `[(lora_name, model_strength, clip_strength), ...]`

**Strength Mode Guide:**

Click the mode toggle button to switch between modes:

- **Single Strength Mode**: One strength value applied to both Model and CLIP
- **Dual Strength Mode (Model/Clip Mode)**: Separate values for Model and CLIP
  - Left value (orange): Model strength
  - Right value (cyan): Clip strength

**Usage Tips:**

- Click the value field to enter precise numbers
- Use arrow buttons for fine adjustment (step: 0.05)
- Drag the value left/right for smooth adjustment
- Click the toggle switch to enable/disable individual LoRAs


#### 3. Convert Any Node

Utility node that resolves compatibility issues where certain sampler nodes cannot directly use standard sampler and scheduler inputs:

**Function:**

- Accepts any input type
- Passes through input values without modification
- Acts as a type adapter to bypass ComfyUI's type checking restrictions


### Installation

#### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for 'Easy Setting Pipes'
3. Click the Install button

#### Method 2: Manual Installation

1. Navigate to ComfyUI custom nodes folder:

```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:

```bash
git clone https://github.com/user-attachments/Comfyui-EasySettingPipes.git
```

3. Restart ComfyUI

### Usage Guide

#### Using Sampler Setup Nodes

1. Add a `SamplerSetup` node to your workflow
2. Configure the desired sampling parameters (see parameter reference table above)
3. Connect the `setup_pipe` output to other nodes
4. Use `SamplerSetupUnpack` node to unpack parameters into individual outputs if needed

**Usage Example:**

```txt
[SamplerSetup] → setup_pipe → [KSampler]
or
[SamplerSetup] → setup_pipe → [SamplerSetupUnpack] → individual parameter outputs
```

#### Using Power LoRA Nodes

1. Add a `Power LoRA Loader` or `Power LoRA Stacker` node
2. Click the "Add LoRA" button to select LoRA files from your model library
3. Adjust strength values:
   - Click the value field to enter precise numbers
   - Use arrow buttons for fine adjustment (step: 0.05)
   - Drag the value for smooth adjustment
4. Click the toggle switch to enable/disable individual LoRAs
5. Use "Toggle All" button to enable/disable all LoRAs at once

**Advanced Usage:**

- **LoRA Chaining**: Connect Loader output to another Loader for multi-stage loading
- **Stack Mode**: Use Stacker to create stacks compatible with Efficiency and other stack-based nodes


### System Requirements

- **ComfyUI Version**: 2024+ and newer
- **Python**: 3.9+
- **Operating System**: Windows, Linux, macOS

### License

MIT License

### Credits & Inspiration

- Inspired by efficient workflow design patterns from the ComfyUI community
- Core technical references from open-source projects by rgthree and pythongosssss
- Designed to provide better user experience and more flexible node architecture
