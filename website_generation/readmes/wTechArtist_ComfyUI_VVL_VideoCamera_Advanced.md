# ComfyUI VVL Video Camera Advanced

专业的视频相机参数估计工具集，基于 VGGT 模型。

## 节点说明

### 1. VVL VGGT Model Loader
独立的模型加载器，从 `ComfyUI/models/vggt/` 目录加载模型。

**输入**: 
- `device`: 设备选择 (auto/cuda/cpu)
- `vggt_model`: 模型版本 (VGGT-1B)

**输出**: 
- `vggt_model`: 模型实例

### 2. VVL VGGT Video Camera Estimator
视频相机参数估计节点。

**输入**: 
- `vggt_model`: 来自模型加载器的模型实例
- `video`: 视频文件或对象
- `frame_interval`: 帧间隔 (默认5)
- `max_frames`: 最大帧数 (默认60)

**输出**: 
- `intrinsics_json`: 相机内参 (JSON)
- `trajectory_preview`: 轨迹可视化图像
- `poses_json`: 相机外参和位置 (JSON)

## 模型目录

模型会从以下目录自动加载：
```
ComfyUI/models/vggt/
├── vggt_1b.pt    # VGGT-1B 模型文件
```

如果本地没有模型文件，会自动从 HuggingFace 下载。

## 使用流程

1. 添加 `VVL VGGT Model Loader` 节点
2. 添加 `VVL VGGT Video Camera Estimator` 节点
3. 连接模型加载器输出到估计器的 `vggt_model` 输入
4. 连接视频源到 `video` 输入
5. 运行获得相机参数和轨迹可视化

## 技术特性

- **模块化设计**: 独立的模型加载和处理节点
- **智能缓存**: 避免重复加载模型
- **多设备支持**: 自动选择最优设备
- **精度适配**: 根据硬件自动调整数据类型
- **3D可视化**: 多视角轨迹预览 