# ArkVideoGenerate - ComfyUI 火山引擎视频生成节点

一个用于 ComfyUI 的自定义节点，集成字节跳动火山引擎的视频生成 AI 模型，支持文本到视频和图像到视频的生成。

## ✨ 特性

- 🎬 **文本生成视频**：基于提示词生成高质量视频
- 🖼️ **图像生成视频**：支持首帧/尾帧条件的视频生成
- 🎥 **多种分辨率**：支持 480p、720p、1080p
- 📐 **灵活比例**：支持 16:9、4:3、1:1、3:4、9:16、21:9、9:21 等多种画面比例
- ⏱️ **可调时长**：支持 5 秒和 10 秒视频生成
- 🎯 **帧率控制**：支持 16fps 和 24fps
- 🔄 **本地转换**：自动将生成的视频转换为 ComfyUI 兼容的张量格式
- 📁 **自动保存**：生成的视频自动保存到本地

## 🚀 安装

1. 将整个项目克隆或下载到你的 ComfyUI 自定义节点目录：
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/your-username/ComfyUI-ArkVideoGenerate.git
   ```
   
   或者直接下载项目文件并解压到：
   ```
   ComfyUI/custom_nodes/ark-video-generate/
   ```

2. 重启 ComfyUI，系统会自动根据 `requirements.txt` 安装所需依赖

## 📋 前置条件

### 获取火山引擎 API Key

1. 访问 [火山引擎控制台](https://console.volcengine.com/)
2. 注册/登录账号
3. 开通视频生成服务
4. 获取 API Key

### 支持的模型

- `doubao-seedance-1-0-pro-250528`
- `wan2-1-14b-flf2v`
- 其他可以自行加入

## 🛠️ 使用方法

### 基础文本生成视频

1. 在 ComfyUI 中添加 `ArkVideoGenerate` 节点
2. 配置必填参数：
   - **api_key**: 你的火山引擎 API Key
   - **model**: 选择要使用的模型
   - **prompt**: 视频生成提示词
   - **resolution**: 视频分辨率（480p/720p/1080p）
   - **ratio**: 画面比例
   - **duration**: 视频时长（5秒/10秒）
   - **fps**: 帧率（16/24）

### 图像条件生成视频

通过连接图像输入来进行条件生成：

- **first_frame_image**: 连接首帧图像（可选）
- **last_frame_image**: 连接尾帧图像（可选，需要同时提供首帧）

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `api_key` | STRING | - | 火山引擎 API Key（必填） |
| `model` | DROPDOWN | doubao-seedance-1-0-pro-250528 | 选择视频生成模型 |
| `prompt` | STRING | "a cat is dancing" | 视频生成提示词 |
| `resolution` | DROPDOWN | 720p | 视频分辨率 |
| `ratio` | DROPDOWN | 16:9 | 画面比例 |
| `duration` | DROPDOWN | 5 | 视频时长（秒） |
| `fps` | DROPDOWN | 24 | 视频帧率 |
| `seed` | INT | -1 | 随机种子（-1为随机） |
| `watermark` | DROPDOWN | false | 是否添加水印 |
| `camera_fixed` | DROPDOWN | false | 是否固定摄像机 |
| `callback_url` | STRING | - | 回调URL（可选） |

### 输出

节点提供两个输出：

- **frames**: 视频帧张量 `(T, H, W, C)` 格式，可连接到其他 ComfyUI 节点
- **frame_count**: 视频总帧数

## 📝 示例工作流

### 文本生成视频
```
提示词: "一只橙色的猫咪在花园里追逐蝴蝶，阳光明媚的下午"
分辨率: 1080p
比例: 16:9
时长: 10秒
帧率: 24fps
```

### 图像条件生成
```
首帧: 上传一张静态图片
提示词: "让图片中的角色开始跳舞"
分辨率: 720p
时长: 5秒
```

## 🔧 工作原理

1. **参数构建**：将用户输入的参数组合成完整的提示词
2. **图像编码**：将输入图像转换为 Base64 格式
3. **任务创建**：通过火山引擎 API 创建视频生成任务
4. **状态轮询**：每 3 秒检查一次任务状态
5. **视频下载**：任务完成后自动下载生成的视频
6. **格式转换**：使用 OpenCV 将 MP4 解码为 ComfyUI 兼容的张量格式

## 📂 文件结构

生成的视频将保存在：
```
ComfyUI/output/ark_video/{task_id}.mp4
```

## ⚠️ 注意事项

- 确保网络连接稳定，视频生成和下载需要时间
- API Key 请妥善保管，不要泄露
- 生成时间取决于视频长度和分辨率，通常需要几分钟
- 如果使用尾帧图像，必须同时提供首帧图像
- 建议先用较短时长和较低分辨率进行测试

## 🐛 故障排除

### 常见问题

**Q: 提示 "Cannot open video" 错误**
A: 检查下载的视频文件是否完整，网络是否稳定

**Q: API 调用失败**
A: 检查 API Key 是否正确，账户余额是否充足

**Q: 任务状态一直是 pending**
A: 可能是服务器繁忙，请耐心等待或稍后重试

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 🔗 相关链接

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [火山引擎官网](https://www.volcengine.com/)
- [火山引擎 AI 服务文档](https://www.volcengine.com/docs/82379)
