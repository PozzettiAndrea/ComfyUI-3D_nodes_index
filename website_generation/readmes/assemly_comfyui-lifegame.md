# ComfyUI-LifeGame

这是一个用于ComfyUI的生命游戏自定义节点，支持动态运行和实时控制。

## 项目概述

该项目实现了一个康威生命游戏的ComfyUI自定义节点，允许用户通过Web界面实时控制游戏的开始和停止，并观察游戏状态的动态变化。

## 系统架构设计

### 1. 前端（Web界面）
- **用户界面**：提供"开始"、"停止"按钮和游戏状态显示区域。
- **通信机制**：使用AJAX或WebSocket与后端进行通信，以便实时更新游戏状态。

### 2. 后端（生命游戏逻辑）
- **核心逻辑**：实现生命游戏的初始化、状态更新、开始和停止功能。
- **状态管理**：维护一个全局状态对象，记录当前的游戏状态。

### 3. 自定义节点（ComfyUI集成）
- **节点定义**：实现与ComfyUI的接口，处理用户输入和输出。
- **与后端通信**：通过API或消息队列与后端交互。

## 目录结构

```
/project_root
│
├── web/
│   ├── index.html          # 用户界面HTML文件
│   ├── styles.css          # 样式文件
│   ├── lifegame.js         # 生命游戏前端逻辑
│   ├── lifegame-ui.js      # 用户界面组件
│   ├── lifegame_preview.js # GIF预览功能
│   ├── utils.js            # 工具函数
│   └── temp/               # 临时文件目录
│
├── server/
│   ├── __init__.py
│   ├── lifegame_logic.py   # 生命游戏核心逻辑
│   ├── api.py              # 提供API接口与前端通信
│   └── monitor.py          # 监控和管理模块
│
├── comfyui_nodes/
│   ├── __init__.py
│   └── lifegame_node.py    # 自定义节点定义
│
├── examples/               # 示例工作流
│   └── lifegame_animation_workflow.json
│
├── requirements.txt        # 项目依赖
└── README.md               # 项目说明文档
```

## 使用说明

1. 将此项目克隆到ComfyUI的`custom_nodes`目录下
2. 安装必要的依赖：`pip install -r requirements.txt`
3. 重启ComfyUI
4. 在ComfyUI的节点列表中找到"LifeGame"节点并使用

## 功能特点

- 支持实时控制游戏的开始和停止
- 可自定义初始状态和游戏规则
- 动态生成的游戏状态可以作为图像输出到ComfyUI的其他节点
- 实时GIF预览和文件操作功能

## 生命游戏动画节点

除了实时的生命游戏控制面板外，本插件还提供了专用的ComfyUI节点，可以生成生命游戏动画：

### 1. 生命游戏动画 (LifeGameAnimation)

这个节点可以生成生命游戏动画序列。

**输入参数:**
- **width**: 网格宽度 (默认: 100)
- **height**: 网格高度 (默认: 100)
- **cell_size**: 细胞像素大小 (默认: 5)
- **frames**: 生成的帧数 (默认: 30)
- **mode**: 初始化模式 (preset/random)
- **preset**: 预设模式，当mode为preset时有效
- **density**: 随机填充密度，当mode为random时有效
- **alive_color**: 活细胞颜色
- **dead_color**: 死细胞颜色
- **x_offset**: 预设图案X偏移 (可选)
- **y_offset**: 预设图案Y偏移 (可选)

**输出:**
- **images**: 动画帧序列
- **final_state**: 最终状态信息

### 2. 保存生命游戏动画 (LifeGameSaveAnimation)

这个节点用于将生命游戏动画保存为GIF或图像序列。

**输入参数:**
- **images**: 来自LifeGameAnimation的图像序列
- **format**: 保存格式 (png/jpg/webp/gif)
- **fps**: 每秒帧数
- **filename_prefix**: 文件名前缀

**特色功能:**
- **实时GIF预览**: 生成GIF后会立即在节点内显示预览
- **文件操作**: 提供打开文件、在系统资源管理器中查看文件等功能
- **右键菜单选项**: 支持通过右键菜单访问更多文件操作

### 新增功能 - GIF预览与文件操作

节点现在支持以下文件操作功能：

1. **实时GIF预览**
   - 生成GIF后自动在节点内显示预览
   - 使用WebSocket实时通知机制，无需刷新或等待工作流完成

2. **文件操作按钮**
   - 在预览区域提供打开文件按钮
   - 悬停时显示提示信息

3. **右键菜单选项**
   - **在新窗口打开GIF**: 在浏览器新标签页查看生成的GIF
   - **复制文件名到剪贴板**: 复制文件名便于引用
   - **在系统资源管理器中显示**: 在本地文件系统中定位文件

4. **跨平台支持**
   - 支持Windows、macOS和Linux系统的文件操作

### 示例工作流

在`examples`目录中提供了示例工作流：

- `lifegame_animation_workflow.json`: 生成并保存滑翔机枪动画的示例

使用方法:
1. 在ComfyUI中，点击菜单中的"Load"按钮
2. 导航到`extensions/comfyui-lifegame/examples`
3. 选择`lifegame_animation_workflow.json`
4. 执行工作流，将生成一个GIF动画并保存在输出目录，同时在节点内显示预览

### 预设模式

支持多种经典的生命游戏图案:

- **glider**: 滑翔机
- **blinker**: 闪烁器
- **toad**: 蟾蜍
- **beacon**: 信标
- **pulsar**: 脉冲星
- **gosper_glider_gun**: Gosper滑翔机枪
- **diehard**: 顽强图案
- **acorn**: 橡子图案
- **lightweight_spaceship**: 轻型宇宙飞船
- **r_pentomino**: R五连体
- **infinite_growth**: 无限增长图案
- **glider_gun**: 滑翔机枪
- **line_puffer**: 线型推进器

## 技术实现

- **WebSocket通信**: 使用WebSocket实现服务器与前端的实时通信
- **Canvas绘制**: 使用LiteGraph的Canvas API进行GIF预览绘制
- **事件驱动**: 采用事件驱动模式处理节点状态变化和GIF生成
- **跨平台文件操作**: 支持多种操作系统的本地文件访问

## 贡献指南

欢迎提交问题和功能请求，也欢迎通过Pull Request贡献代码。

## 许可证

[许可证信息]
