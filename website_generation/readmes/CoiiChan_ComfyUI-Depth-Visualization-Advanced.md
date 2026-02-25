# ComfyUI-Depth-Visualization-Advanced

一个增强版的 ComfyUI 深度图可视化工具，支持深度图预览、3D 场景交互和 Quilt 图像生成。
An enhanced ComfyUI depth map visualization tool that supports depth map preview, 3D scene interaction, and Quilt image generation.

![Preview](https://github.com/CoiiChan/ComfyUI-Depth-Visualization-Advanced/blob/main/example/RGBD2QuiltsExample.png)

[3D多视点应用示例页面(https://gyro3dweb.pages.dev/)


## 主要功能 | Main Features

### 1. 深度图可视化 | Depth Map Visualization
- 实时预览深度图效果 | Real-time depth map preview
- 支持任意深度图输入 | Support for any depth map input
- 3D 场景交互式预览 | Interactive 3D scene preview

### 2. 增强的 UI 控制面板 | Enhanced UI Control Panel
- **视图控制 | View Control**
  - 回正视图：一键重置视角 | Reset View: One-click view reset
  - 场景坐标轴：显示 X、Y、Z 坐标轴，便于空间定位 | Scene Axes: Display X, Y, Z axes for spatial orientation
  - 自适应缩放：控制面板大小随窗口自动调整 | Adaptive Scaling: Control panel size automatically adjusts with window

- **深度效果控制 | Depth Effect Control**
  - 深度强度：调整深度效果的强度 | Depth Strength: Adjust the intensity of depth effect
  - 景深强度：控制景深效果的强度 | DOF Strength: Control the intensity of depth of field effect
  - 对焦距离：调整景深对焦点的位置 | Focus Distance: Adjust the focus point position
  - Z轴偏移：调整场景在 Z 轴上的位置 | Z-Axis Offset: Adjust the scene position on Z-axis
  - 相机FOV角：调整相机FOV角度 | Camera FOV angle: Adjust the camera FOV angle

- **Quilt 图像生成 | Quilt Image Generation**
  - Quilt 数量：设置生成的 Quilt 图像数量 | Quilt Number: Set the number of Quilt images
  - 角度范围：控制 Quilt 图像的视角范围 | Angle Range: Control the viewing angle range
  - 截图分辨率：支持 512×2^n 分辨率设置 | Screenshot Resolution: Support 512×2^n resolution settings
  - 自动缓存：保存历史生成的 Quilt 图像 | Auto Cache: Save historically generated Quilt images
  - 批量生成：支持从缓存中批量生成 Quilt 图像 | Batch Generation: Support batch generation from cache
    
![UI](https://github.com/CoiiChan/ComfyUI-Depth-Visualization-Advanced/blob/main/example/UI.png)

### 3. 视觉优化 | Visual Optimization
- 自适应布局：界面元素随窗口大小自动调整 | Adaptive Layout: UI elements automatically adjust with window size
- 高精度渲染：支持高分辨率输出 | High Precision Rendering: Support high-resolution output
- 实时预览：所有参数调整实时反映在预览中 | Real-time Preview: All parameter adjustments reflect in preview immediately

## 安装方法 | Installation

1. 在 ComfyUI 的 `custom_nodes` 目录下克隆仓库 | Clone the repository in ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/CoiiChan/ComfyUI-Depth-Visualization-Advanced.git
```

2. 重启 ComfyUI | Restart ComfyUI

## 使用说明 | Usage

1. 在 ComfyUI 工作流中添加 `DepthViewerAndQuilts` 节点 | Add `DepthViewerAndQuilts` node to ComfyUI workflow
2. 连接深度图和参考图像 | Connect depth map and reference image
3. 使用控制面板调整参数 | Adjust parameters using control panel
4. 点击 Quilt Capture 按钮生成 Quilt 图像 | Click Quilt Capture button to generate Quilt images

### 缓存生成说明 | Cache Generation Instructions

1. 实时渲染窗口调整参数后生成 Quilt 图像 | Generate Quilt images after adjusting parameters in real-time rendering window
2. 生成的图像将保存在 ComfyUI 的缓存 input 目录中 | Generated images will be saved in ComfyUI's cache input directory
3. 后续可以直接从缓存中读取使用 | Can be directly read from cache for subsequent use
4. 一次半自动执行后，后续可以以缓存读取形式使用 | After one-time semi-automatic execution, subsequent uses can be in cache reading form

### 未实现功能 | Unimplemented Features

1. 实时通过节点传递初始化控制参数 | Real-time initialization control parameter passing through nodes
2. 初始化全自动化无 GUI 无人值守生成 | Fully automated initialization without GUI for unattended generation

## 参数说明 | Parameter Description

### 视图控制 | View Control
- **回正视图 | Reset View**：将视角重置到默认位置 | Reset view to default position
- **场景坐标轴 | Scene Axes**：显示 X（红）、Y（绿）、Z（蓝）坐标轴 | Display X (red), Y (green), Z (blue) axes
- **自适应缩放 | Adaptive Scaling**：控制面板大小会根据窗口大小自动调整 | Control panel size automatically adjusts with window size

### 深度效果 | Depth Effect
- **深度强度 | Depth Strength**：范围 0-2，控制深度效果的强度 | Range 0-2, controls depth effect intensity
- **景深强度 | DOF Strength**：范围 0-1，控制景深效果的强度 | Range 0-1, controls depth of field effect intensity
- **对焦距离 | Focus Distance**：范围 0-1，调整景深对焦点的位置 | Range 0-1, adjusts focus point position
- **相机FOV角 | Focus Distance**：范围 5-120，调整相机FOV角度 | Range 5-120, Camera FOV angle: Adjust the camera FOV angle
- **Z轴偏移 | Z-Axis Offset**：范围 -5 到 5，调整场景在 Z 轴上的位置 | Range -5 to 5, adjusts scene position on Z-axis

### Quilt 设置 | Quilt Settings
- **Quilt 数量 | Quilt Number**：范围 2-8，设置生成的 Quilt 图像数量 | Range 2-8, sets number of Quilt images
- **角度范围 | Angle Range**：范围 0-30°，控制 Quilt 图像的视角范围 | Range 0-30°, controls viewing angle range
- **截图分辨率 | Screenshot Resolution**：支持 512、1024、2048、4096 分辨率 | Support 512, 1024, 2048, 4096 resolutions
- **自动缓存 | Auto Cache**：自动保存生成的 Quilt 图像 | Automatically save generated Quilt images
- **批量生成 | Batch Generation**：支持从缓存中批量生成 Quilt 图像 | Support batch generation from cache

## 注意事项 | Notes

1. 确保输入图像和深度图尺寸匹配 | Ensure input image and depth map dimensions match
2. 高分辨率输出可能需要更多内存 | High resolution output may require more memory
3. 建议使用支持 WebGL 的现代浏览器 | Recommended to use modern browsers with WebGL support

## 鸣谢 | Acknowledgements

本项目基于以下项目开发 | This project is based on:

1. [ComfyUI-Depth-Visualization](https://github.com/gokayfem/ComfyUI-Depth-Visualization)
2. [comfyui-mixlab-nodes](https://github.com/MixLabPro/comfyui-mixlab-nodes)

## 许可证 | License

本项目采用 GPL-3.0 许可证。
This project is licensed under GPL-3.0. 
