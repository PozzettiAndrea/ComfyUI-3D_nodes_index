#  绘梦拾光全景图接缝修复插件

## 概述
这是一个针对 [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/) 的扩展脚本，在原有功能基础上进行了修改，现在可以支持修复 FLUX 全景图接缝。它允许用户独立配置 X 和 Y 轴的无缝图像平铺，同时具备处理 FLUX 全景图接缝问题的能力。

## 功能概述

「绘梦拾光全景图接缝修复插件」是一款专为全景图像生成优化的智能接缝修复插件，通过以下核心技术实现无缝全景效果：

- 🌐 **智能比例适配**：自动识别2:1等全景比例
- 🌀 **环形融合技术**：采用自适应环形填充算法
- ⚡ **实时处理**：无需预处理/后处理操作
- 🧩 **兼容性保障**：完美兼容ControlNet/ImpactPack等主流插件

## 升级计划
-下一版本重点解决接缝处颜色色差

## 注意事项
- 与现有的平铺选项一样，此功能不能 100% 保证无缝平铺，但对于大多数提示词应该可以有效管理接缝问题。
- 可以使用在线工具如([https://www.pycheung.com/checker/](https://renderstuff.com/tools/360-panorama-web-viewer/)) 来检查图像是否有接缝

- ![ComfyUI_00040_](https://github.com/user-attachments/assets/5e0cbcea-bd1f-48b4-87ed-80f7e53dd0b6)  
- ![ComfyUI_00044_](https://github.com/user-attachments/assets/3eef2c17-ac48-425c-8c8a-0a86e10084a6)
- ![ComfyUI_00043_](https://github.com/user-attachments/assets/a694015b-c0d4-4134-b24c-6cdb8f659f8d)
- ![ComfyUI_00042_](https://github.com/user-attachments/assets/cd6ee473-138b-401a-8439-c5d7a29fecfa)
- ![ComfyUI_00041_](https://github.com/user-attachments/assets/45f41b82-afcd-4828-8a4e-01deb2daf7b2)

## 安装指南

### 手动安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/huimengshiguang/AspectAwareTiling.git


