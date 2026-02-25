# 🐳 Remote Workflow Executor

ComfyUI 远程工作流执行节点，允许你从本地 ComfyUI 调用远程 ComfyUI 服务器执行工作流。

## 功能特性

- **远程执行**：连接到任意远程 ComfyUI 服务器，提交并执行工作流
- **多类型输入**：支持图像、文本、音频、视频四种输入类型
- **多类型输出**：自动收集远程工作流的图像、文本、音频、视频输出
- **工作流解析**：可视化解析工作流 JSON，选择需要替换输入的节点
- **动态端口**：根据选择的节点自动生成对应的输入端口
- **IP 隐私保护**：界面默认隐藏 IP 地址，防止屏幕分享时泄露
- **WebSocket 通信**：实时监听远程执行状态

## 安装

1. 将本节点文件夹复制到 ComfyUI 的 `custom_nodes` 目录下
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 重启 ComfyUI

## 使用方法

### 1. 添加节点

在 ComfyUI 中添加节点：`🐳Pond_Owner/IP` → `🐳IP Workflow`

### 2. 配置远程服务器

点击节点上的 ⚙️ 按钮，配置远程 ComfyUI 服务器：
- **IP 地址**：远程服务器的 IP 地址
- **端口**：远程服务器的端口（默认 8188）
- 支持连接测试功能

### 3. 导入工作流

1. 点击 **🔧 解析工作流** 按钮
2. 在弹出的对话框中粘贴工作流的 **API 格式 JSON**（在 ComfyUI 中通过 "Save (API Format)" 导出）
3. 点击 **解析** 按钮

### 4. 选择输入节点

解析后会显示工作流中的输入节点列表，包括：
- `LoadImage` - 图像输入
- `LoadVideo` - 视频输入  
- `LoadAudio` - 音频输入
- `CR Prompt Text` / `Text` / `easy showAnything` - 文本输入

勾选需要从本地传入数据的节点，然后点击 **保存配置**。

### 5. 连接输入

保存后，节点会自动生成对应的输入端口（如 `image_1`、`text_1` 等），将本地节点连接到这些端口即可。

### 6. 执行

运行工作流后，节点会：
1. 将输入数据上传到远程服务器
2. 提交修改后的工作流
3. 等待执行完成
4. 下载并返回输出结果

## 输入端口

| 端口 | 类型 | 说明 |
|------|------|------|
| `image_N` | IMAGE | 图像输入，替换远程 LoadImage 节点 |
| `text_N` | STRING | 文本输入，替换远程文本节点的 prompt/text 字段 |
| `audio_N` | AUDIO | 音频输入，替换远程 LoadAudio 节点 |
| `video_N` | IMAGE | 视频输入（帧序列），替换远程 LoadVideo 节点 |

## 输出端口

| 端口 | 类型 | 说明 |
|------|------|------|
| `output_image` | IMAGE | 远程工作流的图像输出 |
| `output_text` | STRING | 远程工作流的文本输出 |
| `output_audio` | AUDIO | 远程工作流的音频输出 |
| `output_video` | IMAGE | 远程工作流的视频输出（帧序列） |

## 支持的远程节点类型

### 输入节点
- LoadImage
- LoadVideo
- LoadAudio
- CR Prompt Text
- Text
- easy showAnything

### 输出节点
- SaveImage / PreviewImage
- VHS_VideoCombine
- SaveAudio
- easy showAnything（文本）

## 注意事项

1. **网络要求**：确保本地机器能够访问远程 ComfyUI 服务器的 HTTP 和 WebSocket 端口
2. **工作流格式**：必须使用 API 格式的 JSON（非普通保存格式）
3. **超时设置**：默认执行超时时间为 600 秒
4. **文件传输**：大文件（如视频）传输可能需要较长时间
5. **依赖一致**：远程服务器需要安装工作流所需的所有节点和模型

## 目录结构

```
remote_workflow_node/
├── __init__.py
├── remote_workflow_node.py
├── js/
│   └── remote_workflow_node.js
├── README.md
└── requirements.txt
```

## 许可证

MIT License
