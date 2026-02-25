# Circle Pattern Processor for ComfyUI

这是一个用于ComfyUI的自定义节点，可以检测图像中的圆形图案并生成标准化的圆形输出。

## 功能特点

- 使用霍夫圆变换检测图像中的圆形
- 可调节的预处理阈值
- 可配置的圆形检测参数（最小/最大半径）
- 输出标准大小的圆形图案
- 支持将检测到的圆形导出为SVG格式

## 安装方法

1. 将此仓库克隆到ComfyUI的`custom_nodes`目录下：
   ```bash
   cd custom_nodes
   git clone https://github.com/mr7thing/circle_pattern_processor

2. 安装依赖：
   ```bash
   cd circle_pattern_processor
   pip install -r requirements.txt
   ```

## 使用方法

1. 启动ComfyUI
2. 在节点选择菜单中image/pattern找到"Circle Pattern Processor"和"Circle Pattern SVG Exporter"
3. 将节点添加到工作流中
4. 连接输入图像
5. 调整参数：
   - preprocessing_threshold：图像预处理的阈值（0-255）
   - min_radius：检测圆形的最小半径
   - max_radius：检测圆形的最大半径
   - output_circle_size：输出圆形的大小

![工作流示意](workflow/circle_pattern2svg.png)
## 参数说明

### CirclePatternProcessor节点

- min_radius (默认: 5)
  - 范围: 1-100
  - 检测圆形的最小半径

- max_radius (默认: 20)
  - 范围: 1-100
  - 检测圆形的最大半径

- output_circle_size (默认: 10)
  - 范围: 1-50
  - 输出图像中圆形的标准大小

- edge_detection_sensitivity (默认: 50)
  - 范围: 1-100
  - 边缘检测的灵敏度，值越大检测越精确

- circle_accumulator_threshold (默认: 30)
  - 范围: 1-100
  - 圆形检测的累加器阈值，值越小检测到的圆形越多

- min_center_dist (默认: 10)
  - 范围: 1-100
  - 圆心之间的最小距离，用于合并相近的圆形

- merge_mode (选项: ["keep_first", "use_average"])
  - 默认: "keep_first"
  - 圆形合并模式：保留第一个或使用平均值

### CirclePatternSVGExporter节点

- filename (默认: "pattern.svg")
  - 输出SVG文件的文件名
  - 支持子目录路径

- output_circle_size (默认: 10)
  - 范围: 1-50
  - SVG中圆形的标准大小

- circles (必需)
  - 圆形数据元组，包含圆心坐标

- image (必需)
  - 输入图像，用于获取画布尺寸

## 许可证

MIT License
