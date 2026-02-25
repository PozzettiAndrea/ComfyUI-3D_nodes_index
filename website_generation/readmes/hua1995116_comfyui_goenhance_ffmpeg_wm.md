# ComfyUI FFmpeg 水印节点

这是一个 ComfyUI 自定义节点，用于为视频添加水印。该节点使用第三方 `ffmpeg-watermark` 包来实现水印功能。

## 安装

1. 将此文件夹放置到 ComfyUI 的 `custom_nodes` 目录中
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用

在 ComfyUI 中，您可以在 "goenhance" 分类下找到 "GOENHANCE_FFmpegWatermark" 节点。

### 参数说明

- **filenames**: VHS_FILENAMES 类型，来自视频合成节点的输出
- **watermark_path**: 水印图片路径（PNG 格式）
- **position**: 水印位置
  - `upperLeft`: 左上角
  - `upperRight`: 右上角  
  - `lowerLeft`: 左下角
  - `lowerRight`: 右下角
  - `center`: 居中
- **opacity**: 透明度 (0-1)，0=完全透明，1=不透明
- **scale**: 缩放比例 (0.05-1)，0.3 表示缩放到 30% 原始尺寸
- **padding**: 边距 (0-0.2)，0.03 表示留 3% 画面宽高的边距
- **preset**: 编码预设
  - `h264_nvenc`: NVIDIA 硬件加速
  - `libx264`: CPU 编码
  - `copy`: 复制模式（实际会使用 NVENC）

## 依赖

- `ffmpeg-watermark`: 第三方水印处理包
- FFmpeg: 需要系统安装 FFmpeg

## 输出

返回添加水印后的视频文件路径。
