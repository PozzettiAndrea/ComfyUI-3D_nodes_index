# ComfyUI_OmniAvatar
[![python](https://img.shields.io/badge/python-3.12.9-green)](https://www.python.org/downloads/release/python-3129/)

基于 [OmniAvatar](https://github.com/Omni-Avatar/OmniAvatar) 开发的 ComfyUI 自定义节点，可通过输入人像图片、音频和文本提示，生成同步口型与表情的视频序列。节点参数和调用方式与 OmniAvatar 官方推理保持完全一致。

---

## 核心功能

- **一体化处理**：人像 (IMAGE) + 音频 (AUDIO) + 文本提示 (STRING) → 视频 (MP4) + 帧图像序列 (IMAGE)
- **可调参数**：`sample_steps`, `sample_text_guide_scale`, `sample_audio_guide_scale`, `teacache_thresh`, `seed`, `control_after_generate`
- **自动格式兼容**：MP3/WAV/Buffer → WAV（自动重采样到16kHz）
- **标准输出**：
  - `frames` 张量 `(F,C,H,W)`
  - ComfyUI `VIDEO`对象，支持后续节点（如 `GetVideoComponents`、`SaveVideo`、`VideoViewer`）
- **透明延迟加载**：启动时延迟加载模型与权重，不影响 UI 响应速度

---

## 文件说明

- `__init__.py` – 节点入口
- `node_omniavatar_allinone.py` – 节点实现
- `requirements.txt` – 基础依赖列表

---

## 安装步骤

1. **获取 OmniAvatar 源码及模型**

```bash
git clone https://github.com/Omni-Avatar/OmniAvatar
# 下载14B模型权重和配置文件，记录路径
```

2. **设置 PYTHONPATH**

```bash
export PYTHONPATH=/path/to/OmniAvatar:$PYTHONPATH
# 示例（Windows）：
$env:PYTHONPATH = "F:\Comfyui\custom_nodes\OmniAvatar;" + $env:PYTHONPATH
```

3. **安装依赖**

```bash
pip install -r requirements.txt
# 其余依赖参照 OmniAvatar 官方 requirements
```

4. **放置节点文件**

将本仓库放入 ComfyUI 的 `custom_nodes` 目录下：

```
<ComfyUI 根目录>/custom_nodes/
├── ComfyUI_OmniAvatar/
│   ├── __init__.py
│   └── node_omniavatar_allinone.py
└── OmniAvatar/
    ├── configs/
    │   ├── inference.yaml
    │   └── inference_1.3B.yaml
    └── scripts/
        └── inference.py
```

---

## 使用方法

启动 ComfyUI 后，节点位于 **OmniAvatar** 分类。

### 输入参数

- `portrait_image`：人像图片
- `audio_file`：音频文件路径
- `prompt_text`：文本提示
- `config_path`：配置文件路径
- `ckpt_path`：模型权重路径

节点执行过程中将调用 `OmniAvatar.infer`，生成视频过程中控制台显示进度条。

---

## 使用示例


**步骤**：

1. 拖入 **“OmniAvatar All-in-One (14B)”** 节点
2. 连接输入（Image、Audio、Text）
3. 调整参数，运行节点

---

## 常见问题（FAQ）

- **找不到`WanInferencePipeline`？**
  - 检查`custom_nodes/OmniAvatar/scripts/inference.py`路径
  - 检查`sys.path`是否包含正确路径

- **音频格式不支持？**
  - 节点自动转换为16kHz WAV，建议使用 MP3/WAV 文件

- **视频不输出到UI？**
  - 确认输出为`VIDEO`对象，可用`SaveVideo`保存

---

## 许可证 & 致谢

- 本项目遵循 **MIT License**。
- 特别感谢原作者：[OmniAvatar](https://github.com/Omni-Avatar/OmniAvatar)
- 感谢 ComfyUI 社区：[ComfyUI Custom Nodes](https://docs.comfy.org/custom-nodes/walkthrough)

---
## ⭐ Support
If you like my projects and wish to see updates and new features, please consider supporting me. It helps a lot! 
如果你也喜欢我的项目并且期待更多更新，可以点赞收藏

---

## 联系方式

- **Issue 提交**：[仓库Issue页面](https://github.com/CallMe1101/ComfyUI_OmniAvatar/issues)
- **邮箱**：[z15194913998@outlook.com](mailto:your.email@example.com)

欢迎提交 PR 和问题讨论！
