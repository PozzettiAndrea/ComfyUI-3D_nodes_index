# SJ_SweepEffect_ComfyUI

一个专为 ComfyUI 设计的高质量扫光特效节点，支持多种参数调节和抗锯齿处理。

## 功能特性

- 🌟 **高质量扫光效果**：支持从左上角到右下角的平滑扫光动画
- 🎨 **丰富的参数控制**：速度、强度、角度、模糊半径、宽度等全面可调
- 🌈 **自定义颜色**：支持白色扫光和自定义颜色混合模式
- 🚀 **GPU 加速**：完整支持 CUDA 加速处理
- ✨ **超级抗锯齿**：多重采样抗锯齿技术，输出平滑无锯齿
- 📹 **GIF 优化**：专门针对 VideoCombine 和 GIF 输出进行优化

## 安装方法

### 方法一：手动安装
1. 克隆仓库到 ComfyUI 的 custom_nodes 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/BEIBEI-star661/SJ_sweepEffect_Comfyui.git
```

2. 安装依赖：
```bash
cd SJ_sweepEffect
pip install -r requirements.txt
```

3. 重启 ComfyUI

## 使用方法

### 基本工作流
1. 加载图片节点 → SJ_sweepEffect 节点 → VideoCombine 节点
2. 调整扫光参数
3. 生成 GIF 或视频

### 参数说明

| 参数 | 类型 | 默认值 | 范围 | 说明 |
|------|------|---------|------|------|
| **sweep_speed** | Float | 1.0 | 0.1-10.0 | 扫光速度，数值越大扫光越快 |
| **sweep_intensity** | Float | 1.0 | 0.1-2.0 | 扫光强度，控制光效亮度 |
| **sweep_angle** | Float | 0.0 | 0.0-360.0 | 扫光角度，0°为左上到右下 |
| **blur_radius** | Int | 30 | 0-100 | 模糊半径，数值越大边缘越柔和 |
| **sweep_width** | Float | 0.2 | 0.01-0.5 | 扫光宽度，控制光带厚度 |
| **sweep_color** | Color | #FFFFFF | - | 扫光颜色（需开启混合模式） |
| **pure_color_mode** | Boolean | False | - | 混合颜色开关 |
| **frames** | Int | 24 | 16-30 | 输出帧数 |
| **quality** | Combo | medium | low/medium/high | 抗锯齿质量 |

### 质量设置说明

- **Low**: 基础抗锯齿，速度最快
- **Medium**: 平衡质量和速度，推荐日常使用
- **High**: 最高质量抗锯齿，适合最终输出

## 工作流示例

```json
基本扫光效果：
LoadImage → SJ_sweepEffect → VideoCombine

参数建议：
- 速度较慢: sweep_speed = 0.5
- 柔和扫光: blur_radius = 50
- 彩色扫光: pure_color_mode = True, sweep_color = #00FF00
```

## 技术特性

### 抗锯齿技术
- **多重采样抗锯齿 (MSAA)**：高质量模式支持 25 点采样
- **可分离高斯模糊**：高效的边缘平滑处理
- **多层遮罩系统**：核心+过渡+边缘三层渐变

### 性能优化
- **GPU 优先处理**：自动检测并使用 CUDA 加速
- **设备一致性**：避免 CPU-GPU 数据传输
- **内存优化**：高效的张量操作

### 兼容性
- ✅ ComfyUI 0.3.49+
- ✅ PyTorch 1.13.0+
- ✅ CUDA 11.6+
- ✅ VideoCombine 节点
- ✅ Windows/Linux/macOS

## 故障排除

### 常见问题

**Q: 生成的 GIF 有锯齿怎么办？**
A: 尝试将 quality 设置为 "high"，或增加 blur_radius 数值。

**Q: 扫光颜色不生效？**
A: 确保 pure_color_mode 设置为 True，然后调整 sweep_color。

**Q: 处理速度很慢？**
A: 检查是否启用了 CUDA，或将 quality 设置为 "low"。

**Q: 内存不足错误？**
A: 减少 frames 数量或降低 quality 设置。

### 错误报告
如果遇到问题，请在 [GitHub Issues](https://github.com/BEIBEI-star661/SJ_sweepEffect_Comfyui/issues) 提交报告，包含：
- ComfyUI 版本
- 错误信息
- 使用的参数设置
- 系统信息


## 贡献指南

欢迎提交 Pull Request 或 Issues！

1. Fork 本仓库
2. 创建功能分支
3. 提交更改
4. 创建 Pull Request

## 许可证

MIT License - 详见 [LICENSE](https://github.com/BEIBEI-star661/SJ_sweepEffect_Comfyui/blob/main/LICENSE) 文件

## 致谢

感谢 ComfyUI 社区的支持和反馈！

---


**如果这个节点对您有帮助，请给个 ⭐ Star！**




