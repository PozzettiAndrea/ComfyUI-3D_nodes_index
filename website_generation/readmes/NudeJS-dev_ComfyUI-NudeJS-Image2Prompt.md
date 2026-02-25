# ComfyUI NudeJS Image2Prompt 节点

这是一个 ComfyUI 自定义节点，可以将图片转换为文本提示。

## 功能特性

- **图片预处理**：自动调整图片尺寸（最大宽度 1000px，最大高度 800px）
- **Base64 编码**：将图片转换为 base64 格式
- **API 调用**：通过 POST 请求调用外部 API
- **智能重试**：支持配置重试次数，应对网络波动
- **双模式输出**：支持中性文本和提示词文本两种输出模式

## 安装方法

### 方法一：复制到 ComfyUI 目录

1. 将整个 `ComfyUI-NudeJS-Image2Prompt` 文件夹复制到 ComfyUI 的 `custom_nodes` 目录中：
   ```
   ComfyUI/custom_nodes/ComfyUI-NudeJS-Image2Prompt/
   ```

2. 重启 ComfyUI

### 方法二：符号链接

在 Linux/macOS 系统中：
```bash
ln -s /path/to/ComfyUI-NudeJS-Image2Prompt /path/to/ComfyUI/custom_nodes/
```

## 使用方法

在 ComfyUI 工作流中添加 "NudeJS/Image2Prompt" 节点：

### 输入参数

- **images** (必需): 输入图片
- **APIUrl** (必需): API 接口地址，例如：`https://api.example.com`
- **APIKey** (必需): API 鉴权密钥
- **RetryCount** (可选): 请求失败后的重试次数，默认值：3
- **Neutral** (可选): 是否使用中性文本模式，默认值：true

### 输出

- **text**: 转换后的文本提示

## 工作流程示例

1. 添加图片加载节点（如 Load Image、Checkpoint Loader 等）
2. 添加 "Image2Prompt" 节点
3. 将图片连接到 Image2Prompt 节点的 "images" 输入
4. 配置 APIUrl 和 APIKey
5. 运行工作流

## 技术实现

- **图片处理**：使用 Pillow 进行图片缩放和格式转换
- **网络请求**：使用 requests 库，支持重试和超时
- **Base64 编码**：使用标准库 base64 进行编码

## 错误处理

- 网络请求失败时会自动重试（最多 RetryCount 次）
- 失败时会在控制台输出错误信息
- 失败时返回 `None`

## 依赖

- ComfyUI
- Python 3.7+
- requests
- Pillow (PIL)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
