# ComfyUI-Text-Preserve

一个为 ComfyUI 提供文本保持预处理的自定义节点，利用 OCR 识别文本区域，对非文本区域进行模糊与噪点融合，从而在后续生成中更好地保留原始文字。

## 安装

1. 将本项目放入 `ComfyUI/custom_nodes/ComfyUI-Text-Preserve`
2. 安装依赖：
   ```bash
   pip install -r ComfyUI/custom_nodes/ComfyUI-Text-Preserve/requirements.txt
   ```

## 节点

- 名称：`Text Preserve Preprocessor (OCR)`
- 类别：`Custom/TextPreserve`
- 输入：
  - `image`：ComfyUI `IMAGE`，形状 `[B,H,W,C]`，值域 `0-1`
  - `blur_radius`：高斯模糊半径（自动校正为奇数）
  - `noise_sigma`：高斯噪声标准差（像素值，0-255）
  - `mask_dilation`：蒙版膨胀核尺寸，扩大保留区域
  - `text_threshold`：OCR 置信度阈值
- 输出：
  - `processed_image`：融合后的图像（文字区域保留清晰）
  - `text_mask`：识别到的文字蒙版（0-1）

## 特性

- 全局缓存 OCR 模型，首次加载后复用，降低开销
- 优先使用 GPU；若不可用自动回退到 CPU
- 依赖缺失时降级为空识别，节点可正常运行
- 支持 RGB/RGBA 输入，自动忽略 alpha

## 运行建议

- `blur_radius`：21–41；过大可能过度模糊非文字区
- `noise_sigma`：30–70；提供自然背景扰动
- `mask_dilation`：5–15；文字周边保留更安全
- `text_threshold`：0.3–0.6；含小字时可适当降低

## 许可

MIT