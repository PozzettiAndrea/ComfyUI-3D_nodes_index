# ydem_nodes

ComfyUI 自定义节点集合

## 节点列表

### 基础节点
- **YDem Example Node**: 示例节点，用于演示基本功能
- **YDem Image Processor**: 图像处理节点，支持图像缩放

### 面部处理节点
- **YDem Face Direction**: 面部朝向检测节点，使用InstantID的面部分析模型检测面部朝向

## 安装

1. 将 `ydem_nodes` 文件夹复制到 ComfyUI 的 `custom_nodes` 目录
2. 确保已安装 `comfyui_instantid` 节点包（提供面部分析模型）
3. 重启 ComfyUI

## 使用方法

1. 在 ComfyUI 中，节点会出现在对应的分类下：
   - 基础节点：`ydem_nodes` 分类
   - 图像处理节点：`ydem_nodes/image` 分类
   - 面部处理节点：`ydem_nodes/face` 分类
2. 拖放节点到工作区并连接输入输出

## 示例

### Example Node
- 输入文本和数字
- 输出处理后的文本和数字（数字会乘以2）

### Image Processor
- 输入图像和缩放因子
- 输出缩放后的图像

### Face Direction
- 输入：
  - `faceanalysis`: 来自 "InstantID Face Analysis" 节点的面部分析模型
  - `image`: 要检测的图像
- 输出：
  - `angle`: 面部朝向角度（-90到90），0表示正面，90表示右侧脸，-90表示左侧脸
  - `direction`: 方向描述（Front, Right Quarter, Left Quarter, Right Side, Left Side）

## 版本

v1.1.0 - 添加面部朝向检测节点
