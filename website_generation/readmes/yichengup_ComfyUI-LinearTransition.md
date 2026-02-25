# 图片过渡效果节点 (LinearTransition)

这是一个为ComfyUI设计的自定义节点，用于创建两张图片之间的过渡效果，并生成视频帧序列。

## 功能特点

- **LinearTransition**：实现两张图片之间的线性过渡效果（硬边界）
- **GradientTransition**：实现两张图片之间的平滑渐变过渡效果（柔和边界）
- 支持多种过渡方向：左到右、右到左、上到下、下到上
- 可自定义过渡帧数和帧率
- 自动处理不同尺寸的图片

## 安装方法

1. 将整个`LinearTransition`文件夹复制到ComfyUI的`custom_nodes`目录下
2. 重启ComfyUI服务

## 使用方法

### 基本工作流程

1. 加载两张图片
2. 连接到`LinearTransition`或`GradientTransition`节点
3. 设置所需的帧数、方向和帧率
4. 将生成的帧序列连接到`CreateVideo`节点
5. 保存视频

### 参数说明

#### LinearTransition节点
- **image1**: 起始图片
- **image2**: 结束图片
- **frames**: 生成的过渡帧数量
- **direction**: 过渡方向（左到右、右到左、上到下、下到上）
- **fps**: 生成视频的帧率

#### GradientTransition节点
- **image1**: 起始图片
- **image2**: 结束图片
- **frames**: 生成的过渡帧数量
- **transition_width**: 过渡区域的宽度（0-1之间，数值越大过渡越平滑）
- **direction**: 过渡方向（左到右、右到左、上到下、下到上）
- **fps**: 生成视频的帧率

## 示例工作流

将两张图片加载后，使用以下连接方式：

```
LoadImage1 -> image1
LoadImage2 -> image2               -> GradientTransition -> frames -> CreateVideo -> SaveVideo
                frames=24            transition_width=0.2   fps_int
                direction=left_to_right
                fps=24.0
```

## 注意事项

- 如果两张图片尺寸不同，第二张图片会自动调整为第一张图片的尺寸
- 为获得最佳效果，建议使用相同尺寸、相似内容的图片
- 帧数越多，过渡效果越平滑，但生成时间也会相应增加 