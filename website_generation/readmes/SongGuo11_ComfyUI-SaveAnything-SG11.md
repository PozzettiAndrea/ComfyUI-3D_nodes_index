# ComfyUI SaveAnything Node (SG11)

一个用于保存图片的 ComfyUI 自定义节点，支持多种格式并进行了性能优化。

## 功能特点
- 支持多种图片格式（PNG、JPEG、WEBP、BMP、TIFF）
- 针对性能进行优化
- 简单易用的界面
- 保持原始图片质量

## 安装方法

1. 将此仓库克隆到你的 `ComfyUI/custom_nodes/` 目录下


2. 重启 ComfyUI

## 使用方法
1. 在节点菜单中找到 "Save Anything (SG11)"
2. 连接图片输出到该节点
3. 设置所需的文件名和格式
4. 运行工作流

## 支持的格式
- PNG（默认）
- JPEG
- WEBP
- BMP
- TIFF

## 性能优化
- 使用 torch 操作进行图像转换
- 优化的保存参数配置
- 减少不必要的 CPU-GPU 数据传输

- ## 联系微信：NFTSongGuo11

🔴

