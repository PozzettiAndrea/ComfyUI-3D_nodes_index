# 此项目包含ComfyUI-PainterAI2V（音频驱动图生视频）和PainterAV2V（音频驱动视频对口型）2个节点（对comfyui官方infinitetalk节点添加功能优化而成） 由 绘画小子 制作
# ComfyUI-PainterAI2V

---
<img width="1011" height="894" alt="image" src="https://github.com/user-attachments/assets/0345c75c-63b6-4168-bc9b-a3834ce9dc99" />

## 节点特点

**专为 Wan2.2 双模型工作流优化的 InfiniteTalk 对口型节点，支持首尾帧精确控制**

- **帧率同步控制**：新增 `video_fps` 参数，可自定义设置视频帧率（1-120fps），音频口型自动匹配该帧率，完美解决原生硬编码 25fps 导致的音画不同步问题
- **Wan2.2 双模型架构**：同时支持高噪模型（0-2步）和低噪模型（2-4步）并行打补丁，保持与官方工作流完全一致
- **三模式首帧控制**：
  - **仅首帧**：传入 `start_image`，视频从首帧开始生成并全程对口型
  - **仅尾帧**：传入 `end_image`，视频最终定格指定画面并对口型
  - **首尾帧**：同时传入 `start_image` 和 `end_image`，视频从首帧自然过渡到尾帧，全程精准对口型
- **提示词动作运镜控制**：继承 Wan2.2 强大的提示词理解能力，可通过文本精确控制人物动作、相机运镜和场景变化
- **全功能保留**：支持单人/双人对口型、motion context、previous frames 延续生成等所有原生功能

- 图片+音频 生视频
<img width="2709" height="1191" alt="image" src="https://github.com/user-attachments/assets/ee5e719a-3eef-4148-868b-10310100352f" />

首尾帧+音频 生视频
---<img width="2706" height="1375" alt="image" src="https://github.com/user-attachments/assets/6d4eea34-0de7-448f-bd32-d5cd2b4f7e30" />


## Node Features

**InfiniteTalk lip-sync node optimized for Wan2.2 dual-model workflow with first/last frame precision control**

- **FPS Synchronization Control**: New `video_fps` parameter allows custom video frame rate settings (1-120fps), with audio lip-sync automatically matching the specified rate, completely solving audio-visual desynchronization caused by the original hard-coded 25fps
- **Wan2.2 Dual-Model Architecture**: Simultaneously patches both high-noise (0-2 steps) and low-noise (2-4 steps) models, maintaining full compatibility with official workflows
- **Three First/Last Frame Modes**:
  - **First frame only**: Pass `start_image` to generate video from first frame with continuous lip-sync
  - **Last frame only**: Pass `end_image` to end video at specified frame with lip-sync
  - **First & Last frames**: Pass both `start_image` and `end_image` for natural transition from start to end with precise lip-sync throughout
- **Prompt-Controlled Motion & Camera**: Inherits Wan2.2's powerful prompt comprehension, enabling precise control of character movements, camera operations, and scene changes through text prompts
- **Full Feature Retention**: Supports all native features including single/dual speaker lip-sync, motion context, and previous frames continuation

---


## 核心参数 / Core Parameters

| 参数 | 说明 | Parameter | Description |
|------|------|-----------|-------------|
| `video_fps` | 视频输出帧率，音频口型将自动匹配此速率 | Video output frame rate, audio lip-sync will automatically match this rate |
| `motion_frame` | 运动上下文帧数，用于延续生成 | Number of motion context frames for continuation |
| `audio_scale` | 口型强度系数，控制音频影响程度 | Lip-sync intensity coefficient, controls audio influence level |
| `mode` | 单/双说话人模式切换 | Single/dual speaker mode toggle |
| `start_image` | 首帧图像，视频从此帧开始 | First frame image, video starts from this frame |
| `end_image` | 尾帧图像，视频最终定格此画面 | Last frame image, video ends at this frame |

---
# PainterAV2V - Audio-Driven Video Lip Sync Node

# PainterAV2V - 音频驱动视频对口型节点

<img width="972" height="740" alt="image" src="https://github.com/user-attachments/assets/56963625-1f7b-497c-9611-5a65b94ac3e5" />
---

**One-sentence Intro / 一句话介绍**  
A streamlined ComfyUI node that allowing precise mouth synchronization by custom frame rate settings with InfiniteTalk lip-sync technology

一个精简的ComfyUI节点，支持InfiniteTalk对口型技术，对视频进行自定义帧率实现精准口型同步。

---
<img width="1908" height="918" alt="image" src="https://github.com/user-attachments/assets/3b7a9d35-29b0-4abd-be9e-93523c370738" />


**Key Features / 功能特点**



- **Customizable Frame Rate / 自定义帧率**  
  Set target FPS (1-60) to ensure lip movements align perfectly with audio timing.  
  可设置目标帧率(1-60)，确保口型与音频节奏精准对齐。

- **Smart Audio Processing / 智能音频处理**  
  Automatically interpolates audio features to match video length and frame rate.  
  自动插值音频特征以匹配视频长度与帧率。

- **Flexible Inputs / 灵活输入**  
  Supports video sequence, audio encoder output, reference image, and optional mask for latent encoding.  
  支持视频序列、音频编码输出、参考图及可选遮罩输入。



