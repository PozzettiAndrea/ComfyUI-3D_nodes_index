# ComfyUI-Banana-Node

一个用于ComfyUI的自定义节点，使用Google的Gemini 2.5 Flash Image 与 Gemini 3 Pro Image Preview API生成图像。

新增在线调用
[无敌banana2 🍌 0.2/张](https://www.runninghub.cn/post/1991513043091857410/?inviteCode=rh-v1118)

[使用教程](https://www.bilibili.com/video/BV1ByU5BbEqS/?share_source=copy_web&vd_source=e82febcd63de4c3684cb2d737bbe5050)

- 支持1K、2K、4K、8K等多种分辨率缩放

## 功能特性

- 使用Google Gemini 2.5 Flash Image Preview模型
- 支持多张输入图像
- 可自定义提示词
- 支持多种输出尺寸比例
- 完整的错误处理和日志记录
- **新增**：图像比例调整节点 - 支持裁剪、填充、拉伸等多种调整方式
- **新增**：分辨率缩放节点 - 支持1K、2K、4K、8K等多种分辨率缩放

## 安装

1. 将此仓库克隆到你的ComfyUI自定义节点目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/ComfyUI-Banana-Node.git
```

2. 安装依赖：
```bash
cd ComfyUI-Banana-Node
pip install google-generativeai pillow numpy torch
```

3. 配置API密钥：
- 复制 `config.json.example` 为 `config.json`
- 在 `config.json` 中填入你的Google AI API密钥
- 获取API密钥：访问 Google AI Studio: https://aistudio.google.com/app/apikey
- 需绑定一张visa或者master 信用卡即可获得300美元的免费额度
- 绑定方法：访问 Google AI Studio，点击"绑定信用卡"，输入信用卡信息即可绑定。

```json
{
    "api_key": "your_google_ai_api_key_here"
}
```

4. 重启ComfyUI

## 使用方法

### Banana Gemini Gen 节点
1. 在ComfyUI中找到 "Banana" 分类下的 "Banana Gemini Gen" 节点
2. 连接输入图像
3. 设置提示词（描述你想要生成的图像）
4. 选择输出尺寸比例
5. 运行工作流

### Banana Ratio Adjuster 节点
1. 在ComfyUI中找到 "Banana Node/Ratio" 分类下的 "Banana Ratio Adjuster" 节点
2. 连接输入图像
3. 选择目标比例（1:1、4:3、16:9等常见比例或自定义比例）
4. 选择调整方法：
   - **crop**: 裁剪图像以匹配目标比例
   - **pad**: 填充图像以匹配目标比例
   - **stretch**: 拉伸图像以匹配目标比例
5. 如选择填充模式，可设置填充颜色
6. 运行工作流

### Banana Resolution Scaler 节点
1. 在ComfyUI中找到 "Banana Node/Ratio" 分类下的 "Banana Resolution Scaler" 节点
2. 连接输入图像
3. 选择目标分辨率（1K、2K、4K、8K或自定义）
4. 选择是否保持宽高比
5. 运行工作流

## 输入参数

### Banana Gemini Gen 节点
- **model**: 模型选择（目前支持 gemini-2.5-flash-image 与 gemini-3-pro-image-preview）
- **prompt**: 文本提示词，描述你想要生成的图像
- **size**: 输出图像尺寸比例
- **input_image**: 输入图像（必需）

### Banana Ratio Adjuster 节点
- **image**: 输入图像
- **target_ratio**: 目标比例（1:1、4:3、16:9等或自定义）
- **resize_method**: 调整方法（crop、pad、stretch）
- **custom_width**: 自定义宽度比例（当选择自定义比例时）
- **custom_height**: 自定义高度比例（当选择自定义比例时）
- **pad_color_r/g/b**: 填充颜色的RGB值（当选择pad方法时）

### Banana Resolution Scaler 节点
- **image**: 输入图像
- **target_resolution**: 目标分辨率（1K、2K、4K、8K、自定义）
- **maintain_ratio**: 是否保持宽高比
- **custom_size**: 自定义尺寸（当选择自定义分辨率时）

## 输出

### Banana Gemini Gen 节点
- **image**: 生成的图像
- **revised_prompt**: 修订后的提示词（当前为N/A）
- **image_url**: 图像URL（当前为N/A）

### Banana Ratio Adjuster 节点
- **image**: 调整后的图像
- **width**: 输出图像宽度
- **height**: 输出图像高度
- **ratio**: 最终宽高比

### Banana Resolution Scaler 节点
- **image**: 缩放后的图像
- **width**: 输出图像宽度
- **height**: 输出图像高度

## 注意事项

- 需要有效的Google AI API密钥
- 确保网络连接正常
- API调用可能产生费用，请查看Google AI的定价政策

## 故障排除

1. **"config.json文件未找到"错误**：
   - 确保已将 `config.json.example` 复制为 `config.json`
   - 检查文件是否在正确的目录中

2. **API密钥错误**：
   - 验证API密钥是否正确
   - 确保API密钥有足够的权限和配额

3. **依赖包错误**：
   - 确保已安装所有必需的Python包
   - 尝试重新安装依赖包

## 许可证

MIT License

## 贡献

欢迎提交问题和拉取请求！

## 更新日志

### v1.1.0
- 新增图像比例调整节点（Banana Ratio Adjuster）
- 新增分辨率缩放节点（Banana Resolution Scaler）
- 支持多种图像比例调整方式（裁剪、填充、拉伸）
- 支持1K、2K、4K、8K多种分辨率缩放
- 完善的比例计算和图像处理工具类

### v1.0.0
- 初始版本
- 支持Gemini 2.5 Flash Image Preview API
- 基本的图像生成功能

---

## English Version

# ComfyUI-Banana-Node

A custom node for ComfyUI that uses Google's Gemini 2.5 Flash Image and Gemini 3 Pro Image Preview APIs to generate images.

New: Online invocation
[Invincible banana2 🍌 0.2/image](https://www.runninghub.ai/post/1991513043091857410/?inviteCode=rh-v1118)
[Tutorial](https://www.bilibili.com/video/BV1ByU5BbEqS/?share_source=copy_web&vd_source=e82febcd63de4c3684cb2d737bbe5050)

- Supports resolution scaling for 1K, 2K, 4K, 8K, etc.
## Features

- Uses Google Gemini 2.5 Flash Image Preview model
- Supports multiple input images
- Customizable prompts
- Multiple output aspect ratios
- Complete error handling and logging
- New: Image Ratio Adjuster node — supports crop, pad, stretch
- New: Resolution Scaler node — supports 1K, 2K, 4K, 8K resolution scaling

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-username/ComfyUI-Banana-Node.git
```

2. Install dependencies:
```bash
cd ComfyUI-Banana-Node
pip install google-generativeai pillow numpy torch
```

3. Configure your API key:
- Copy `config.json.example` to `config.json`
- Fill in your Google AI API key in `config.json`
- Get your API key: visit Google AI Studio: https://aistudio.google.com/app/apikey
- Bind a Visa or MasterCard to receive $300 in free credits
- Binding method: visit Google AI Studio, click "Bind Credit Card", and enter card information

```json
{
    "api_key": "your_google_ai_api_key_here"
}
```

4. Restart ComfyUI

## Usage

### Banana Gemini Gen Node
1. In ComfyUI, find the "Banana" category and add the "Banana Gemini Gen" node
2. Connect input image(s)
3. Set the prompt (describe the image you want to generate)
4. Choose the output aspect ratio
5. Run the workflow

### Banana Ratio Adjuster Node
1. In ComfyUI, find the "Banana Node/Ratio" category and add the "Banana Ratio Adjuster" node
2. Connect input image(s)
3. Choose target ratio (1:1, 4:3, 16:9 or custom)
4. Choose adjustment method:
   - crop: crop the image to match the target ratio
   - pad: pad the image to match the target ratio
   - stretch: stretch the image to match the target ratio
5. If pad mode is selected, set the padding color
6. Run the workflow

### Banana Resolution Scaler Node
1. In ComfyUI, find the "Banana Node/Ratio" category and add the "Banana Resolution Scaler" node
2. Connect input image(s)
3. Choose target resolution (1K, 2K, 4K, 8K or custom)
4. Choose whether to maintain aspect ratio
5. Run the workflow

## Input Parameters

### Banana Gemini Gen Node
- model: model selection (currently supports gemini-2.5-flash-image & gemini-3-pro-image-preview)
- prompt: text prompt describing the image you want to generate
- size: output image aspect ratio
- input_image: input image (required)

### Banana Ratio Adjuster Node
- image: input image
- target_ratio: target ratio (1:1, 4:3, 16:9 or custom)
- resize_method: adjustment method (crop, pad, stretch)
- custom_width: custom width ratio (when using custom ratio)
- custom_height: custom height ratio (when using custom ratio)
- pad_color_r/g/b: RGB values of the padding color (when using pad)

### Banana Resolution Scaler Node
- image: input image
- target_resolution: target resolution (1K, 2K, 4K, 8K, custom)
- maintain_ratio: whether to maintain aspect ratio
- custom_size: custom size (when using custom resolution)

## Output

### Banana Gemini Gen Node
- image: generated image
- revised_prompt: revised prompt (currently N/A)
- image_url: image URL (currently N/A)

### Banana Ratio Adjuster Node
- image: adjusted image
- width: output image width
- height: output image height
- ratio: final aspect ratio

### Banana Resolution Scaler Node
- image: scaled image
- width: output image width
- height: output image height

## Notes

- A valid Google AI API key is required
- Ensure your network connection is stable
- API calls may incur costs; please check Google AI pricing

## Troubleshooting

1. "config.json file not found" error:
   - Ensure `config.json.example` has been copied to `config.json`
   - Check that the file is in the correct directory

2. API key error:
   - Verify that the API key is correct
   - Ensure the API key has sufficient permissions and quota

3. Dependency errors:
   - Ensure all required Python packages are installed
   - Try reinstalling dependencies

## License

MIT License

## Contributing

Issues and pull requests are welcome!

## Changelog

### v1.1.0
- Added Image Ratio Adjuster node (Banana Ratio Adjuster)
- Added Resolution Scaler node (Banana Resolution Scaler)
- Supports multiple ratio adjustment methods (crop, pad, stretch)
- Supports 1K, 2K, 4K, 8K resolution scaling
- Enhanced ratio calculation and image processing utilities

### v1.0.0
- Initial release
- Supports Gemini 2.5 Flash Image Preview API
- Basic image generation features