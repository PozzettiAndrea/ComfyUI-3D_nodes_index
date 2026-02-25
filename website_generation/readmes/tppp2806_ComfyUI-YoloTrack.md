# ComfyUI YoloTrack

一个用于ComfyUI的YOLO目标检测和跟踪节点插件，支持目标检测、选择和跟踪裁剪功能。

## 功能特点

- 🎯 **YOLO目标检测**：支持YOLOv8系列模型进行目标检测
- 🎨 **灵活的目标选择**：支持多种选择标准（面积、置信度、位置等）
- 📦 **智能裁剪**：支持多种裁剪比例和自动跟踪
- 🔄 **批量处理**：支持图像批处理和视频帧序列处理
- 🎭 **双掩码模式**：支持框掩码和分割掩码
- 🔧 **高度可配置**：丰富的参数设置满足不同需求

## 安装

### 方式1: 通过ComfyUI Manager安装（推荐）

1. 打开ComfyUI Manager
2. 搜索 "YoloTrack"
3. 点击安装

### 方式2: 手动安装

1. 克隆仓库到ComfyUI的custom_nodes目录：
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-username/comfyui-YoloTrack.git
```

2. 安装依赖：
```bash
cd comfyui-YoloTrack
pip install -r requirements.txt
```

3. 重启ComfyUI

## 模型准备

将YOLO模型文件（.pt格式）放置在以下目录：
```
ComfyUI/models/yolo/
```

支持的模型包括：
- yolov8n.pt（轻量级）
- yolov8s.pt（小型）
- yolov8m.pt（中型）
- yolov8l.pt（大型）
- yolov8x.pt（超大型）

如果目录中没有模型，插件会自动使用Ultralytics下载默认模型。

## 节点说明

### 1. YOLO Detection & Selection（YOLO检测与选择）

用于目标检测、选择和生成掩码。

**输入参数：**
- `image`: 输入图像
- `model_name`: YOLO模型选择
- `select_criteria`: 目标选择标准
  - Area Max/Min: 按面积大小
  - Confidence Max/Min: 按置信度
  - Center Top/Bottom/Left/Right: 按中心位置
- `select_count`: 选择目标数量（1-100）
- `confidence_threshold`: 置信度阈值（0.0-1.0）
- `nms_threshold`: NMS阈值（0.0-1.0）
- `output_mode`: 输出模式
  - Merged Mask: 合并所有目标的掩码
  - Individual Objects: 分别输出每个目标
- `class_ids`: 类别ID过滤（可选，用逗号分隔，如"0,2"）

**输出：**
- `preview_image`: 带检测框的预览图像
- `mask`: 目标掩码
- `x, y`: 边界框左上角坐标
- `width, height`: 边界框宽度和高度
- `x2, y2`: 边界框右下角坐标

### 2. YOLO Tracking & Crop（YOLO跟踪与裁剪）

用于目标跟踪和智能裁剪，特别适合视频处理。

**输入参数：**
- `image`: 输入图像序列
- `model_name`: YOLO模型选择
- `select_criteria`: 目标选择标准
- `select_count`: 跟踪目标数量
- `confidence_threshold`: 置信度阈值
- `nms_threshold`: NMS阈值
- `crop_ratio`: 裁剪比例
  - Original: 保持原始比例
  - 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2: 预设比例
- `crop_scale`: 裁剪缩放系数（0.01-5.0）
- `offset_x`: X轴偏移（-2.0-2.0）
- `offset_y`: Y轴偏移（-2.0-2.0）
- `smoothing`: 平滑系数（0.0-0.99），值越大越平滑
- `mask_type`: 掩码类型
  - Box: 边界框掩码
  - Segmentation: 分割掩码（如果模型支持）
- `class_ids`: 类别ID过滤（可选）

**输出：**
- `cropped_image`: 裁剪后的图像
- `mask`: 目标掩码

## 使用示例

### 基础目标检测
1. 添加"YOLO Detection & Selection"节点
2. 连接图像输入
3. 选择模型和检测参数
4. 连接输出到其他节点

### 视频目标跟踪
1. 添加"YOLO Tracking & Crop"节点
2. 连接视频帧序列
3. 设置跟踪参数和裁剪比例
4. 使用smoothing参数实现平滑跟踪
5. 输出裁剪后的目标区域

### 特定类别检测
在`class_ids`参数中输入COCO类别ID，例如：
- "0" - 仅检测人
- "0,2" - 检测人和汽车
- 留空 - 检测所有类别

## COCO类别参考

常用类别ID：
- 0: person（人）
- 1: bicycle（自行车）
- 2: car（汽车）
- 3: motorcycle（摩托车）
- 5: bus（公交车）
- 7: truck（卡车）
- 15: cat（猫）
- 16: dog（狗）

完整类别列表请参考[COCO数据集](https://cocodataset.org/#explore)。

## 技术细节

- **框架**: PyTorch, Ultralytics YOLO
- **图像处理**: OpenCV, PIL
- **批处理**: 支持批量图像和视频帧处理
- **平滑跟踪**: 指数移动平均实现平滑跟踪效果
- **边界处理**: 自动处理图像边界和裁剪溢出

## 性能建议

- 对于实时应用，推荐使用`yolov8n.pt`或`yolov8s.pt`
- 对于高精度需求，使用`yolov8l.pt`或`yolov8x.pt`
- 调整`confidence_threshold`来平衡检测灵敏度和误检率
- 使用`smoothing`参数减少跟踪抖动（推荐0.5-0.8）

## 故障排除

**模型加载失败**
- 确保模型文件在`ComfyUI/models/yolo/`目录下
- 检查模型文件完整性
- 首次使用时，Ultralytics会自动下载默认模型

**检测结果为空**
- 降低`confidence_threshold`值
- 检查`class_ids`设置是否正确
- 确认图像中包含可检测目标

**跟踪不稳定**
- 增加`smoothing`参数值
- 调整`crop_scale`和偏移参数
- 提高`confidence_threshold`减少误检

## 依赖项

- ultralytics
- numpy
- opencv-python-headless
- torch
- Pillow

## 许可证

[添加您的许可证信息]

## 贡献

欢迎提交问题和拉取请求！

## 更新日志

### v1.0.0
- 初始版本发布
- 支持YOLOv8系列模型
- 实现目标检测和跟踪功能

## 联系方式

- GitHub: [您的GitHub链接]
- Issues: [问题反馈链接]

---

如果这个插件对您有帮助，请给个⭐Star支持一下！