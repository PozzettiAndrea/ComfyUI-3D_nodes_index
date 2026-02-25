# ComfyUI-Qwen3-TTS

面向 ComfyUI 的 Qwen3-TTS 自定义节点，包含 Voice Design（配音设计）与 Voice Clone（声音克隆/自定义音色）两类节点。节点代码基于上游开源项目 [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS.git) 适配、内置。

<img width="982" height="1097" alt="Image" src="https://github.com/user-attachments/assets/cc4e9242-edcd-4f33-9088-2f14f7682c9e" />

## 目录结构

```
custom_nodes/ComfyUI-Qwen3-TTS/
├─ __init__.py
└─ nodes/
   └─ qwen3_tts_nodes.py
```

## 安装依赖

```bash
git clone https://github.com/starsFriday/ComfyUI-Qwen3-TTS.git
cd ComfyUI-Qwen3-TTS
pip install -r requirements.txt
# 可选：pip install flash-attn --no-build-isolation
```

## 模型放置

按项目根目录相对路径放置模型（可从 Hugging Face 下载）：
- Voice Design：`models/Qwen3-TTS/Qwen3-TTS-12Hz-1.7B-VoiceDesign`  
  模型地址：https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
- Voice Clone（默认使用 CustomVoice，如需真·参考音频克隆请放置 Base 权重）：  
  `models/Qwen3-TTS/Qwen3-TTS-12Hz-1.7B-CustomVoice`  
  模型地址：https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
- Base（真人声音克隆专用）：`models/Qwen3-TTS/Qwen3-TTS-12Hz-1.7B-Base`  
  模型地址：https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base

> 说明：如果使用 Base 模型进行参考音频克隆，请将 Base 权重放在同一目录并在加载器中指向它。

## 节点说明

- **Qwen3TTSLoader**
  - 选择 `task=voice_design` 或 `task=voice_clone`。
  - `model_name` 下拉直接列出 `models/Qwen3-TTS/` 目录中的模型，无需手输路径。
  - 可配置 `device`（如 `cuda:0` / `auto` / `cpu`）、`dtype`、`use_flash_attention`、`low_cpu_mem_usage`。
  - 输出类型：`QWEN3_TTS_MODEL`，供后续节点使用。

- **Qwen3TTSVoiceDesign**
  - `model`: Loader 输出
  - `text`: 要合成的文本（多行可填）
  - `instruct`: 配音/风格描述
  - `language`: 下拉（Auto/中/英/日/韩/德/法/俄/葡/西/意）
  - `non_streaming_mode`: 是否用非流式文本输入（仅模拟）
  - `top_p` / `temperature` / `max_new_tokens`: 采样/长度控制
  - 仅支持 VoiceDesign 模型。
  - 输出：`AUDIO` + 采样率。

- **Qwen3TTSVoiceClone**
  - `model`: Loader 输出（可选 Base 或 CustomVoice）
  - `text`: 要合成的文本
  - `language`: 下拉
  - Base 模式参数：
    - `reference_audio`: 参考音频（3–10s）
    - `reference_text`: 参考文本（x_vector_only=False 时必填）
    - `x_vector_only`: True 仅用声纹，False 走 ICL 需要参考文本
  - CustomVoice 模式参数：
    - `speaker`: 预置音色下拉
    - `instruct`: 可选风格提示
  - 通用：`non_streaming_mode`、`top_p`、`temperature`、`max_new_tokens`
  - 输出：`AUDIO` + 采样率。

- **Qwen3TTSRealVoiceClone**
  - `model`: Loader 输出，必须是 Base 模型
  - `text`: 要合成的文本
  - `reference_audio`: 参考音频（3–10s）
  - `reference_text`: 可选参考文本
  - `x_vector_only`: True 仅用声纹，False 需要参考文本
  - 其他：`language` 下拉、`non_streaming_mode`、`top_p`、`temperature`、`max_new_tokens`
  - 使用模型：`models/Qwen3-TTS/Qwen3-TTS-12Hz-1.7B-Base`（Hugging Face: https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base）。
  - 其他参数同上（`language` 下拉等）。

## 快速使用

1. 将模型权重放到指定目录。
2. 在工作流中添加 `Qwen3TTSLoader` → 连接到 `Qwen3TTSVoiceDesign` 或 `Qwen3TTSVoiceClone`。
3. 通过 ComfyUI 原生的 `SaveAudio` / 其他音频节点保存输出。

## 提示

- 默认仅输出第一段音频；如需批量可在节点层面扩展文本列表支持。
- 如果遇到显存不足，可将 `dtype` 设为 `float16` 或关闭 `flash_attention` 并启用 `low_cpu_mem_usage`。
- 当使用 CustomVoice 路径时，Voice Clone 节点不需要参考音频；若要真·克隆，请加载 Base 模型。
