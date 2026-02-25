# PainterLongVideo Node for ComfyUI  
# ComfyUI 的 PainterLongVideo 节点

A powerful node for generating long-form videos with consistent motion, global scene coherence, and slow-motion correction in Wan 2.2-based workflows.  If you don’t connect to the previous_video access point, it is equivalent to a keyframe node with dynamic enhancement functionality.
一个强大的节点，用于在基于 Wan 2.2 的工作流中生成长视频，具备运动一致性、全局场景连贯性以及慢动作修复功能。如果你不接参考视频，它就等于是一个带动态加强功能的首尾帧节点。

---

## ✨ Features / 功能亮点

- **Long Video Continuation**: Seamlessly continues from the last frame of a previous video segment.  
  **长视频接续**：无缝接续上一段视频的最后一帧。

- **Slow-Motion Fix**: Built-in `motion_amplitude` control to enhance motion intensity and fix sluggish movement in 4-step LoRAs (e.g., lightx2v).  
  **慢动作修复**：内置 `motion_amplitude` 参数，增强运动幅度，修复 4 步 LoRA（如 lightx2v）中的迟缓问题。

- **Global Consistency Anchor**: Optional `initial_reference_image` input allows the model to remember the original character/scene layout from the first segment, preventing drift when the camera returns.  
  **全局一致性锚定**：可选的 `initial_reference_image` 输入，让模型记住第一段的初始人物与场景布局，防止镜头回溯时内容漂移。

- **Compact UI**: Clean, official-style node size with short name `PainterLongVideo`.  
  **紧凑界面**：简洁、官方风格的节点尺寸，名称简短为 `PainterLongVideo`。

---

## 📥 Installation / 安装方法

1. Place this folder into your ComfyUI custom nodes directory:  
   将本文件夹放入 ComfyUI 的自定义节点目录中：

   
2. Ensure you have the required dependencies (usually included with standard ComfyUI):  
确保已安装所需依赖（通常随标准 ComfyUI 自带）：
- `torch`
- `comfyui` (latest)

3. Restart ComfyUI. The node will appear under **`video/painter`** category.  
重启 ComfyUI。该节点将出现在 **`video/painter`** 分类下。

---

## ⚙️ Inputs / 输入参数

| Input | Type | Description |
|------|------|-------------|
| **positive** | CONDITIONING | Positive prompt conditioning. |
| **negative** | CONDITIONING | Negative prompt conditioning. |
| **vae** | VAE | VAE model for latent encoding/decoding. |
| **width** | INT | Output width (multiple of 16). Default: `832`. |
| **height** | INT | Output height (multiple of 16). Default: `480`. |
| **length** | INT | Number of output frames. Default: `81`. |
| **batch_size** | INT | Batch size for generation. Default: `1`. |
| **previous_video** | IMAGE | The full output video from the previous segment (used for continuity). |
| **motion_frames** | INT | Number of trailing frames from `previous_video` used as motion reference. Default: `5`. |
| **motion_amplitude** | FLOAT | Motion intensity multiplier (1.0 = normal, 1.15 = recommended). Range: `1.0–2.0`. |
| **initial_reference_image** *(optional)* | IMAGE | The **first frame** of the very first video segment. Helps maintain global consistency across segments. |
| **clip_vision_output** *(optional)* | CLIP_VISION_OUTPUT | Optional CLIP vision embedding for image-guided generation. |

| 输入 | 类型 | 说明 |
|------|------|------|
| **positive** | CONDITIONING | 正向提示词条件。 |
| **negative** | CONDITIONING | 负向提示词条件。 |
| **vae** | VAE | 用于 latent 编解码的 VAE 模型。 |
| **width** | INT | 输出宽度（需为 16 的倍数）。默认：`832`。 |
| **height** | INT | 输出高度（需为 16 的倍数）。默认：`480`。 |
| **length** | INT | 输出帧数。默认：`81`。 |
| **batch_size** | INT | 生成批次大小。默认：`1`。 |
| **previous_video** | IMAGE | 上一段视频的完整输出（用于连续性）。 |
| **motion_frames** | INT | 从 `previous_video` 末尾提取的参考帧数量。默认：`5`。 |
| **motion_amplitude** | FLOAT | 运动强度倍率（1.0=正常，1.15=推荐）。范围：`1.0–2.0`。 |
| **initial_reference_image** *(可选)* | IMAGE | **整个视频序列的第一帧**。用于跨段落保持全局一致性。 |
| **clip_vision_output** *(可选)* | CLIP_VISION_OUTPUT | 可选的 CLIP 视觉嵌入，用于图像引导生成。 |

---

## 💡 Usage Tips / 使用建议

- **For best results**, always provide the **first frame of Segment 1** as `initial_reference_image` to all subsequent segments.  
**为获得最佳效果**，请将**第一段的第一帧**作为 `initial_reference_image` 输入到所有后续段落中。

- Set `motion_amplitude = 1.15` as default. Increase to `1.2–1.3` if motion still feels too slow.  
默认设为 `motion_amplitude = 1.15`。若仍觉动作太慢，可增至 `1.2–1.3`。

- Keep `motion_frames` small (3–7) unless complex motion is needed.  
除非需要复杂运镜，否则保持 `motion_frames` 较小（3–7）。

- This node works best with **Wan 2.2 + 4-step LoRA** pipelines.  
本节点最适合搭配 **Wan 2.2 + 4 步 LoRA** 流程使用。

---

## 🧠 How It Works / 工作原理

The node:
1. Encodes the last frame of `previous_video` as the starting point.
2. Constructs a latent sequence with the first frame fixed and others initialized to gray.
3. Applies motion enhancement via latent difference scaling (`motion_amplitude`).
4. Injects both **last-frame** and **initial-frame** latents into `reference_latents` for dual-reference guidance.

该节点：
1. 将 `previous_video` 的最后一帧编码为起点；
2. 构建 latent 序列：首帧固定，其余初始化为灰色；
3. 通过 latent 差值缩放实现运动增强（`motion_amplitude`）；
4. 将**结尾帧**和**起始帧**同时注入 `reference_latents`，实现双重参考引导。

---

## 📜 License / 许可证

MIT License – Free to use, modify, and distribute.  
MIT 许可证 – 免费使用、修改和分发。
