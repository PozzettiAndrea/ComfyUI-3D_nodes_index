# ComfyUI-PainterVideoInfo

轻量级视频信息提取节点，专为 ComfyUI 设计。

<img width="2486" height="1038" alt="image" src="https://github.com/user-attachments/assets/a82df69d-db7f-41e0-8f8b-a10c488b59f0" />

## 🎯 功能

从 Video Helper Suite 的 `VHS_VIDEOINFO` 中提取视频元数据，提供两个独立节点：

- **VideoInfoSource** 🟡：提取**源视频**信息
- **VideoInfoLoaded** 🟢：提取**加载后**视频信息

## 📥 安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/princepainter/ComfyUI-PainterVideoInfo.git
```

重启 ComfyUI 即可使用。

## 🎮 使用

1. 使用 Video Helper Suite 加载视频（如 `Load Video` 节点）
2. 将 `video_info` 输出连接到本节点的 `video` 输入
3. 获取视频的帧率、帧数、宽度和高度信息

## 📊 输入输出

**共同输入：**
- `video`: VHS_VIDEOINFO (来自 Video Helper Suite)

**VideoInfoSource 输出：**
- `fps🟡`: 源视频帧率 (FLOAT)
- `Frame_count🟡`: 源视频帧数 (INT)
- `width🟡`: 源视频宽度 (INT)
- `height🟡`: 源视频高度 (INT)

**VideoInfoLoaded 输出：**
- `fps🟢`: 加载后视频帧率 (FLOAT)
- `Frame_count🟢`: 加载后视频帧数 (INT)
- `width🟢`: 加载后视频宽度 (INT)
- `height🟢`: 加载后视频高度 (INT)

## ⚡ 特点

- 节点宽度自适应，可手动调整至最窄
- 彩色图标清晰区分源/加载后数据
- 简洁命名，节省工作流空间
- 完全兼容 Video Helper Suite

