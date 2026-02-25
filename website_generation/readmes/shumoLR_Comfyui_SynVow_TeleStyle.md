# ComfyUI SynVow TeleStyle

基于 [TeleStyle](https://github.com/Tele-AI/TeleStyle) 的 ComfyUI 视频风格迁移插件。

## 原开源项目

[https://github.com/Tele-AI/TeleStyle](https://github.com/Tele-AI/TeleStyle)

## 功能特性

- 🎬 **视频风格迁移**: 将风格参考图的风格应用到源视频上
- 🤖 **自动模型下载**: 首次使用时自动从 HuggingFace 下载所需模型
- ⚙️ **灵活参数控制**: 支持调整分辨率、帧数、推理步数、引导强度等
- 📊 **实时进度显示**: 推理过程中显示进度条
- 🎯 **显存优化**: 内置 VAE Tiling 减少显存占用

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装核心依赖：

```bash
pip install transformers diffusers pillow decord opencv-python safetensors omegaconf einops sentencepiece accelerate peft ftfy regex
```

### 2. 模型下载

模型会在首次使用时**自动下载**到以下目录：

```
ComfyUI/models/TeleStyle/
├── Wan2.1-T2V-1.3B-Diffusers/    # Wan2.1 基础模型
├── dit.ckpt                       # TeleStyle 风格迁移权重
└── prompt_embeds.pth              # 预计算的文本嵌入
```

支持的基础模型：
- `Wan2.1-T2V-1.3B` - 1.3B 参数量，显存需求较低
- `Wan2.1-T2V-14B` - 14B 参数量，效果更好但显存需求高

## 节点说明

### 1. TeleStyle Video Loader

加载 TeleStyle 视频风格迁移模型。

**输入参数：**
- `wan_model`: 选择 Wan2.1 基础模型（1.3B 或 14B）

**输出：**
- `model`: 模型信息，用于后续的风格迁移节点

### 2. TeleStyle Video

执行视频风格迁移。

**输入参数：**
- `model`: 从 Loader 节点获取的模型
- `video_frames`: 源视频帧（IMAGE 类型）
- `style_first_frame`: 风格参考图（通常是风格化后的首帧）
- `height`: 输出视频高度（默认 1024）
- `width`: 输出视频宽度（默认 1024）
- `video_length`: 输出视频帧数（默认 81）
- `num_inference_steps`: 推理步数（默认 25，越少越快但质量下降）
- `guidance_scale`: 引导强度（默认 3.0，越大风格迁移越强）
- `seed`: 随机种子

**输出：**
- `video_frames`: 风格迁移后的视频帧（IMAGE 类型）

## 使用示例

### 基本工作流

1. 使用 `Load Video` 节点加载源视频
2. 使用 `Load Image` 节点加载风格参考图（风格化后的首帧）
3. 连接 `TeleStyle Video Loader` 加载模型
4. 连接 `TeleStyle Video` 进行风格迁移
5. 使用 `Video Combine` 节点保存输出视频

### 推荐参数（24GB 显存）

- height: 480
- width: 832
- video_length: 49
- num_inference_steps: 20-25

## 注意事项

1. **显存需求**: 
   - 1.3B 模型：建议 16GB+ 显存
   - 14B 模型：建议 40GB+ 显存
   - 可通过降低分辨率和帧数减少显存占用

2. **风格参考图**: 
   - 通常使用图像风格迁移工具（如 TeleStyle Image）先对首帧进行风格化
   - 风格参考图会影响整个视频的风格

3. **推理速度**: 
   - 推理步数越少速度越快，但质量会下降
   - 建议先用较少步数（如 10-15）测试效果

## 故障排除

### CUDA 显存不足

- 降低 `height` 和 `width` 参数
- 减少 `video_length` 帧数
- 使用 1.3B 模型而非 14B

### 输出视频黑屏

- 检查风格参考图是否正确连接
- 确保源视频帧格式正确（IMAGE 类型，值范围 0-1）

## 许可证

本项目遵循原 TeleStyle 项目的许可证。

## 相关链接

- [TeleStyle 原项目](https://github.com/Tele-AI/TeleStyle)
- [Wan2.1 模型](https://huggingface.co/Wan-AI)
