# SynVow-Nano2

ComfyUI custom nodes for AI image generation using SynVow API and compatible services.

## 功能特性 Features

- **T2I (Text-to-Image)**: 文本生成图片
- **I2I (Image-to-Image)**: 图片转换和编辑
- 支持多个API源 (T8Star, Apicore)
- 自定义分辨率和宽高比
- 批量生成 (最多4张)
- Seed控制实现可重复生成

## 安装 Installation

### 方法1: 克隆仓库 (推荐)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/Synvow-nano2.git
```

### 方法2: 手动下载

1. 下载此仓库的ZIP文件
2. 解压到 `ComfyUI/custom_nodes/Synvow-nano2`
3. 重启ComfyUI

## 使用方法 Usage

### SynVow-Nano2 T2I (文本生成图片)

1. 在ComfyUI中添加 `SynVow-Nano2 T2I` 节点
2. 配置参数:
   - **API Source**: 选择API提供商 (T8Star 或 Apicore)
   - **API Key**: 输入你的API密钥
   - **Model Select**: 选择模型 (默认: `gemini-3-pro-image-preview`)
   - **Prompt**: 输入图片描述
   - **Aspect Ratio**: 选择宽高比 (1:1, 16:9, 9:16, 4:3, 或自定义)
   - **Count**: 生成图片数量 (1-4)
   - **Seed**: 随机种子 (0为随机)

### SynVow-Nano2 I2I (图片转图片)

1. 在ComfyUI中添加 `SynVow-Nano2 I2I` 节点
2. 连接输入图片
3. 配置参数:
   - **Image_1**: 主要输入图片 (必需)
   - **Image_2-5**: 可选的额外参考图片
   - **API Source**: 选择API提供商
   - **API Key**: 输入你的API密钥
   - **Model Select**: 选择模型
   - **Prompt**: 输入转换指令
   - **Size Mode**: 
     - `Match Image_1 (Smart Crop)`: 匹配输入图片尺寸
     - `Keep Model Output`: 保持模型输出尺寸
     - `Custom Size`: 自定义尺寸
   - **Count**: 生成图片数量
   - **Seed**: 随机种子

## 参数说明 Parameters

### API配置
- **api_source**: API服务提供商
  - `T8Star (ai.t8star.cn)`
  - `Apicore (api.apicore.ai)`
- **api_key**: 你的API密钥
- **model_select**: 模型名称 (支持手动输入)

### 图片参数
- **aspect_ratio** (T2I): 宽高比选择
  - `1:1`: 正方形
  - `16:9`: 宽屏
  - `9:16`: 竖屏
  - `4:3`: 标准
  - `Custom Size`: 自定义尺寸
- **size_mode** (I2I): 输出尺寸模式
- **custom_w/h**: 自定义宽度/高度 (64-16384, 步长8)
- **count**: 生成数量 (1-4)
- **seed**: 随机种子 (0-2147483647, 0为随机)

## 技术特性 Technical Features

- 智能图片缩放和裁剪
- 支持Base64和URL图片输出
- 自动压缩输入图片 (最大1568px)
- 批量处理支持
- SSL验证禁用 (用于内网API)

## 依赖 Dependencies

```
torch
numpy
Pillow
requests
urllib3
```

## API兼容性 API Compatibility

此节点兼容OpenAI Vision API格式的服务，包括:
- SynVow AI (ai.synvow.cc)
- T8Star (ai.t8star.cn)
- Apicore (api.apicore.ai)

## 故障排除 Troubleshooting

### 常见问题

1. **API错误**: 检查API密钥是否正确
2. **超时**: 增加timeout值或检查网络连接
3. **图片未生成**: 查看控制台日志获取详细错误信息
4. **Seed值过大**: 节点会自动将超大值转换为Int32范围内

## 更新日志 Changelog

### v1.0.0
- 初始版本发布
- 支持T2I和I2I功能
- 多API源支持
- Seed控制功能

## 许可证 License

MIT License

## 作者 Author

SynVow Team

## 支持 Support

如有问题或建议，请在GitHub Issues中提出。

---

**注意**: 使用此节点需要有效的API密钥。请从相应的API提供商处获取。
