**PainterVideoUpscale**

---

**English** | **中文**
<img width="1027" height="526" alt="image" src="https://github.com/user-attachments/assets/70d7b9dd-3a93-409c-895e-017b347e34b2" />


- **Video Upscale & Encode | 视频放大与编码**  
  Automatically scales your input video to specified dimensions and encodes it into latent space for sampling.
  
  自动将输入视频缩放到指定尺寸并编码为潜在空间数据供采样使用。

- **First/Last Frame Control | 首尾帧控制**  
  Processes start and end images to guide the video generation with consistent opening and closing frames.
  
  处理起始和结束图像，为视频生成提供一致的开场和结尾画面。



**Use Case | 使用场景**

Perfect for Wan 2.1/2.2 video generation workflows where you need to:
- Upscale a source video while maintaining frame consistency
- Use specific start/end images to control video boundaries
- Reduce node clutter by combining preprocessing steps

适用于 Wan 2.1/2.2 视频生成工作流，当你需要：
- 放大源视频同时保持帧一致性
- 使用特定的起始/结束图像控制视频边界
- 通过合并预处理步骤减少节点混乱

---

**Note | 注意事项**

- Width and height affect both the video encoding and the frame conditioning preparation
- The output latent contains only the processed video data, not mixed with frame conditioning
- Length parameter only affects the conditioning preparation, not the input video frames

- 宽高设置同时影响视频编码和帧条件准备
- 输出的潜在数据仅包含处理后的视频数据，不与帧条件混合
- 长度参数仅影响条件准备，不影响输入视频帧
