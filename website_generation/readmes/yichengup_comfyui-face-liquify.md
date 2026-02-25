# ComfyUI Face Liquify

一个用于ComfyUI的人脸液化效果插件，支持单图多种脸部变形效果和批量处理功能（视频）。

## 功能特点

- 支持多种脸部变形效果：
  - **Fat Face**: 胖脸效果，使脸部看起来更饱满
  - **Thin Face**: 瘦脸效果
  - **Big Face**: 大脸效果
  - **Small Face**: 小脸效果，整体缩小脸部

- 支持多人脸处理，可以按照不同顺序选择处理人脸：
  - 大到小
  - 小到大
  - 从左到右
  - 从右到左

- 精细参数控制：
  - 效果强度调节
  - 平滑度调节
  - 眼睛大小调节
  - 变形区域大小调节
  - 帧间混合（视频处理）

- 批量处理支持：
  - 处理图像序列或视频帧
  - 帧间平滑处理，确保效果连贯

## 安装要求

- 已安装的ComfyUI环境
- Python 3.8+
- CUDA环境（推荐）用于GPU加速，系统的cuda和torch的cuda要一致，这样生成的时间20s左右，不然用cpu很慢。

## 安装方式

1. 在ComfyUI的custom_nodes目录下克隆此仓库：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui-face-liquify.git
```

2. 安装依赖：

```bash
cd comfyui-face-liquify
pip install -r requirements.txt
```

3. 重启ComfyUI服务

## 使用方法

1. 在ComfyUI中，在节点浏览器中找到"Face Liquify/image"分类
2. 将Face Liquify节点添加到工作流中
3. 连接图像输入
4. 选择所需的效果类型和参数
5. 运行工作流，查看变形效果

## 参数说明

- **image**: 输入图像
- **effect_type**: 变形效果类型
- **strength**: 效果强度（0-1）
- **eye_scale**: 眼睛放大比例（用于Thin Face效果）
- **smooth**: 效果平滑度（0-1）,建议效果为0
- **area_scale**: 变形区域大小（0.5-2.0）
- **frame_blend**: 帧间混合强度（用于视频处理）
- **face_order**: 多人脸处理顺序
- **face_indices**: 指定处理哪些人脸（all或0,1,2...）

## 示例
![image](https://github.com/user-attachments/assets/58784783-1b03-4de6-898f-1860c51dd5d7)


https://github.com/user-attachments/assets/19bfe38f-7fb0-4a63-8dc8-58124be2d1e1



## 许可证

MIT

## 致谢

- 基于insightface库进行人脸检测和关键点提取
- ComfyUI社区 
