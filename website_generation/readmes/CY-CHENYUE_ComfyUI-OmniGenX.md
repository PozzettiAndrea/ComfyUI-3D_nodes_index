# ComfyUI-OmniGenX

<div align="center">

ComfyUI-OmniGenX 是一个 ComfyUI 的自定义节点，集成了 OmniGen 统一图像生成模型。该插件支持多种图像生成和编辑任务，包括文本到图像生成、主题驱动生成、身份保持生成和图像条件生成等功能。

[English](README_EN.md) | 简体中文

</div>

## ✨ 功能特点

- 🎨 **多模态图像生成**
  - 文本到图像生成
  - 主题驱动生成
  - 身份保持生成
  - 图像条件生成
  - 图像编辑
  - 风格迁移

## 📦 安装要求

### 系统要求
- Python 3.8+
- CUDA 支持的 GPU (建议至少 8GB 显存)
- ComfyUI 最新版本

> 注意：如果显存不足，可以在使用时设置 `cpu_offload=True` 和降低 `max_input_image_size` 来优化内存使用。

### 安装步骤

1. 克隆仓库到 ComfyUI 的 custom_nodes 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/CY-CHENYUE/ComfyUI-OmniGenX.git
```

2. 安装依赖：
```bash
cd ComfyUI-OmniGenX
pip install -r requirements.txt
```

## 💡 使用指南

### 提示词格式说明

OmniGen 使用特殊的图像占位符格式：`<img><|image_*|></img>`

在 ComfyUI 中使用时:
- 只需输入 `image_1`、`image_2` 等占位符名称
- 系统会自动将其转换为完整格式 `<img><|image_1|></img>`

示例：
- 单图像提示词: `a photo of image_1 in winter`
- 多图像提示词: `combine the style of image_1 with the content of image_2`

### 重要参数说明

| 参数名 | 说明 | 建议值 |
|--------|------|--------|
| use_input_image_size_as_output | 使用输入图像尺寸作为输出尺寸 | 图像编辑时建议启用 |
| max_input_image_size | 最大输入图像尺寸 | 多图像输入时建议降低此值 |
| guidance_scale | 文本引导强度 | 如果图像过饱和，请降低此值 |
| seed | 随机种子 | 编辑生成的图像时需要使用不同的种子 |

## 📝 使用技巧

1. **图像编辑任务**
   - 建议将输出图像尺寸设置为与输入图像相同
   - 可以启用 `use_input_image_size_as_output` 自动匹配尺寸

2. **内存优化**
   - 如果显存不足，可以设置 `cpu_offload=True`
   - 处理多张图像时，可以降低 `max_input_image_size`

3. **图像质量优化**
   - 如果图像过饱和，降低 `guidance_scale`
   - 更详细的提示词会带来更好的效果
   - 如果生成的图像带有动漫风格，可以在提示词中添加 "photo"

4. **图像编辑注意事项**
   - 编辑 OmniGen 生成的图像时，不能使用相同的种子
   - 例如：使用 seed=0 生成图像，则编辑时应使用 seed=1

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [OmniGen](https://huggingface.co/Shitao/OmniGen-v1) 

---

如果这个项目对您有帮助，请考虑给它一个 ⭐️