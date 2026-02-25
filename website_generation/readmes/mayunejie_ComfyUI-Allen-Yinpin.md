# ComfyUI-Allen-Yinpin

一个功能增强的 ComfyUI 音频加载节点。
A custom audio loader node for ComfyUI with filename output and upload support.

## 功能特点 (Features)

1.  **加载音频 (Load Audio)**: 支持 .wav, .mp3, .flac, .ogg, .m4a 等常见格式。
2.  **输出文件名 (Filename Output)**: 增加了一个 `filename_text` 输出端口，可以输出不带后缀的文件名字符串，以供save audio使用，方便区别音频一一对应的关系。

## 安装方法 (Installation)

### 方法 1: 推荐 (Recommended)
使用 ComfyUI Manager，选择 "Install via Git URL"，输入本仓库地址安装。

### 方法 2: 手动 (Manual)
将本仓库克隆到 `ComfyUI/custom_nodes/` 目录下：
```bash
cd custom_nodes
git clone https://github.com/你的用户名/ComfyUI-Allen-Yinpin.git
