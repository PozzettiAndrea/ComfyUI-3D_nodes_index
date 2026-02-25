# YZZ Face Mosaic Plugin for ComfyUI

基于OpenCV的人脸马赛克ComfyUI插件，支持对视频和图像中的人脸进行马赛克处理。

## 功能特性

- 🎥 **视频人脸马赛克**: 对视频文件中的人脸进行实时马赛克处理
- 🖼️ **图像人脸马赛克**: 对单张图像中的人脸进行马赛克处理
- 📁 **批量处理**: 支持批量处理多个视频文件
- 🎨 **多种马赛克效果**: 支持像素化、模糊、黑色方块三种马赛克效果
- ⚙️ **可调参数**: 支持调整检测精度、马赛克大小等参数

## 安装要求

### 系统要求
- Python 3.8+
- OpenCV 4.8+
- ComfyUI

### 依赖安装

在ComfyUI的Python环境中安装依赖：

```bash
# 激活ComfyUI环境
source ENV/bin/activate  # Linux/Mac
# 或
ENV\Scripts\activate     # Windows

# 安装依赖
pip install opencv-python>=4.8.0
pip install opencv-contrib-python>=4.8.0
pip install numpy>=1.21.0
```

## 节点说明

### 1. 视频人脸马赛克 (FaceMosaicNode)

对单个视频文件进行人脸马赛克处理。

**输入参数:**
- `video_path`: 输入视频文件路径
- `mosaic_size`: 马赛克块大小 (5-100)
- `detection_scale`: 人脸检测缩放因子 (1.01-2.0)
- `min_neighbors`: 最小邻居数 (1-20)
- `mosaic_type`: 马赛克类型 (pixelate/blur/black_box)
- `output_format`: 输出格式 (mp4/avi/mov)
- `output_quality`: 输出质量 (1-100)
- `output_path`: 输出路径 (可选)

**输出:**
- `output_video_path`: 处理后的视频路径
- `processing_info`: 处理信息JSON

### 2. 图像人脸马赛克 (ImageFaceMosaicNode)

对单张图像进行人脸马赛克处理。

**输入参数:**
- `image`: 输入图像
- `mosaic_size`: 马赛克块大小 (5-100)
- `detection_scale`: 人脸检测缩放因子 (1.01-2.0)
- `min_neighbors`: 最小邻居数 (1-20)
- `mosaic_type`: 马赛克类型 (pixelate/blur/black_box)

**输出:**
- `image`: 处理后的图像

### 3. 批量视频人脸马赛克 (BatchVideoFaceMosaicNode)

批量处理多个视频文件。

**输入参数:**
- `input_directory`: 输入视频目录路径
- `mosaic_size`: 马赛克块大小 (5-100)
- `detection_scale`: 人脸检测缩放因子 (1.01-2.0)
- `min_neighbors`: 最小邻居数 (1-20)
- `mosaic_type`: 马赛克类型 (pixelate/blur/black_box)
- `output_format`: 输出格式 (mp4/avi/mov)
- `file_extensions`: 支持的文件扩展名 (逗号分隔)

**输出:**
- `output_directory`: 输出目录路径
- `processing_summary`: 处理摘要JSON

## 马赛克效果说明

### 1. 像素化 (pixelate)
将人脸区域缩小后放大，产生像素化效果。

### 2. 模糊 (blur)
使用高斯模糊对人脸区域进行模糊处理。

### 3. 黑色方块 (black_box)
用黑色方块完全覆盖人脸区域。

## 参数调优建议

### 检测精度调优
- `detection_scale`: 值越小检测越精确但速度越慢，建议1.1-1.3
- `min_neighbors`: 值越大误检越少但可能漏检，建议3-8

### 马赛克效果调优
- `mosaic_size`: 像素化效果时控制马赛克块大小，建议10-30
- 模糊效果时控制模糊程度，建议15-50

## 使用示例

### 基本工作流
1. 添加"视频人脸马赛克"节点
2. 设置输入视频路径
3. 调整马赛克参数
4. 运行工作流

### 图像处理工作流
1. 添加"Load Image"节点加载图像
2. 连接"图像人脸马赛克"节点
3. 调整参数并运行

### 批量处理工作流
1. 添加"批量视频人脸马赛克"节点
2. 设置输入目录路径
3. 配置批量处理参数
4. 运行工作流

## 输出文件位置

- 单个视频处理: `output/face_mosaic/`
- 批量处理: `output/batch_face_mosaic/`

## 故障排除

### 常见问题

1. **OpenCV分类器未找到**
   - 确保OpenCV安装正确
   - 检查分类器文件路径

2. **视频无法打开**
   - 检查视频文件路径是否正确
   - 确保视频格式受支持

3. **检测效果不佳**
   - 调整`detection_scale`和`min_neighbors`参数
   - 确保视频/图像质量良好

4. **处理速度慢**
   - 降低视频分辨率
   - 增加`detection_scale`值
   - 减少`min_neighbors`值

### 性能优化

- 对于长视频，建议先降低分辨率再处理
- 批量处理时建议分批进行，避免内存不足
- 可以调整检测参数在速度和精度间平衡

## 技术实现

- 使用OpenCV的Haar级联分类器进行人脸检测
- 支持多种视频编码格式
- 实时处理，逐帧检测和打码
- 兼容ComfyUI的图像处理流程

## 许可证

MIT License

## 更新日志

### v1.0.0
- 初始版本发布
- 支持视频和图像人脸马赛克
- 支持批量处理
- 三种马赛克效果
