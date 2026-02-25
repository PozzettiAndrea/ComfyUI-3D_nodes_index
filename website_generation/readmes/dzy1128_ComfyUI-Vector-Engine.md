# ComfyUI Vector Engine 图像生成节点

这是一个集成了 Vector Engine Gemini API 的 ComfyUI 自定义节点，用于高级图像生成和编辑。

## ✨ 功能特点

- 🖼️ **多图片输入**：支持最多 5 张可选输入图片
- 🎨 **灵活配置**：多种纵横比和分辨率选项
- 🎲 **种子控制**：可设置种子值（用于界面显示，不影响生成）
- 📝 **自定义提示词**：支持系统提示词和用户提示词
- ⚡ **性能优化**：自动压缩图片，大幅提升处理速度
- 📊 **详细信息**：输出生成详情和状态信息
- 💬 **进度日志**：显示实时处理进度

## 📦 安装

### 方法 1: 直接复制

1. 将整个文件夹复制到 ComfyUI 的 custom_nodes 目录：
```bash
cp -r ComfyUI-Vector-Engine /path/to/ComfyUI/custom_nodes/
```

2. 重启 ComfyUI

### 方法 2: Git Clone

```bash
cd /path/to/ComfyUI/custom_nodes/
git clone <repository-url> ComfyUI-Vector-Engine
```

### 依赖项

节点依赖以下库（ComfyUI 默认已包含）：
- torch
- numpy
- PIL (Pillow)
- 标准库：http.client, json, base64, time, io

## 🎮 使用方法

### 节点输入

#### 必选参数

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| **prompt** | 文本 | 用户提示词，描述要生成的内容 | "Generate a creative image..." |
| **system_prompt** | 文本 | 系统提示词，指导 AI 行为 | "You are an AI assistant..." |
| **aspect_ratio** | 下拉菜单 | 图片纵横比 | 1:1 |
| **image_size** | 下拉菜单 | 输出分辨率 | 1K |
| **seed** | 整数 | 种子值（仅显示用） | 0 |

**纵横比选项**：
- 1:1 (正方形)
- 2:3, 3:2 (标准照片)
- 4:3, 3:4 (传统屏幕)
- 16:9, 9:16 (宽屏/竖屏)

**分辨率选项**：
- 1K - 快速生成
- 2K - 平衡质量（推荐）
- 4K - 高质量（较慢）

#### 可选参数

| 参数 | 类型 | 说明 |
|------|------|------|
| **image_1 ~ image_5** | 图片 | 最多 5 张可选输入图片 |

### 节点输出

| 输出 | 类型 | 说明 |
|------|------|------|
| **image** | IMAGE | 生成的图片（可连接 Preview Image / Save Image） |
| **info** | STRING | 生成信息（模型、分辨率、耗时、状态等） |

### 信息输出示例

```
==============================================================
Vector Engine Image Generation Result
==============================================================
Model Name: gemini-3-pro-image-preview
Aspect Ratio: 2:3
Image Size: 2K
Resolution: 1024x1536
Seed: 12345
Input Images: 2
Generation Time: 26.34s
Status: SUCCESS
==============================================================
```

## 📝 使用示例

### 示例 1：纯文本生成

```
1. 添加 "Vector Engine Image Generator" 节点
2. 设置 prompt: "A beautiful sunset over mountains"
3. 不连接任何输入图片
4. 连接输出到 "Preview Image"
5. 执行工作流
```

### 示例 2：图片编辑/合成

```
1. 使用 "Load Image" 加载 2-3 张图片
2. 添加 "Vector Engine Image Generator" 节点
3. 连接图片到 image_1, image_2 等
4. 设置 prompt: "Combine these people in a group photo at the beach"
5. 设置 aspect_ratio: "16:9"
6. 连接输出到 "Save Image"
7. 执行工作流
```

### 示例 3：控制纵横比

```
1. 添加节点
2. 设置 aspect_ratio: "16:9" (宽屏)
3. 设置 image_size: "2K"
4. 设置 prompt: "A cinematic landscape with dramatic lighting"
5. 执行工作流
```

## ⚡ 性能优化

节点已内置自动优化：

### 自动图片压缩
- ✅ 自动调整图片尺寸（最大 2048px）
- ✅ 使用 JPEG 格式压缩（质量 85%）
- ✅ 文件大小减少约 90%
- ✅ 编码速度提升 10-15 倍

### 日志输出
运行时会在控制台显示处理进度：
```
[VectorEngine] Processing 2 input images...
[VectorEngine] Image 1: encoded in 0.15s, size: 245.3KB
[VectorEngine] Image 2: encoded in 0.12s, size: 189.7KB
[VectorEngine] Sending request to API (payload size: 0.58MB)...
[VectorEngine] API request completed in 26.34s
```

### 性能数据

**典型场景（2张 4000x3000 图片）：**
- 图片编码：~0.3 秒
- 数据上传：~1-2 秒
- API 生成：~26 秒
- **总耗时：~28-30 秒**

## ⚙️ 配置

### API Key 配置

**重要**：节点从环境变量读取 API Key，需要设置 `VECTOR_ENGINE_API_KEY` 环境变量。

#### Linux / macOS

**临时设置（仅当前终端）：**
```bash
export VECTOR_ENGINE_API_KEY="sk-your-api-key-here"
```

**永久设置（推荐）：**

1. 编辑 `~/.bashrc` 或 `~/.zshrc`：
```bash
echo 'export VECTOR_ENGINE_API_KEY="sk-your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

2. 或者在启动 ComfyUI 前设置：
```bash
export VECTOR_ENGINE_API_KEY="sk-your-api-key-here"
python main.py
```

#### Windows

**临时设置（仅当前命令行）：**
```cmd
set VECTOR_ENGINE_API_KEY=sk-your-api-key-here
```

**永久设置：**
```cmd
setx VECTOR_ENGINE_API_KEY "sk-your-api-key-here"
```

#### Docker / 容器环境

在 docker-compose.yml 中添加：
```yaml
environment:
  - VECTOR_ENGINE_API_KEY=sk-your-api-key-here
```

或使用 docker run：
```bash
docker run -e VECTOR_ENGINE_API_KEY="sk-your-api-key-here" ...
```

#### 验证配置

启动 ComfyUI 后，如果环境变量未设置，节点会抛出错误提示：
```
VECTOR_ENGINE_API_KEY environment variable is not set.
Please set it before using this node.
```

### 自定义压缩参数

如需调整图片压缩设置，修改 `vector_engine_node.py` 第 152 行：

```python
# 默认设置（推荐）
base64_data, mime_type = self.tensor_to_base64(img, max_size=2048, quality=85)

# 更快速度（质量略低）
base64_data, mime_type = self.tensor_to_base64(img, max_size=1536, quality=75)

# 更高质量（较慢）
base64_data, mime_type = self.tensor_to_base64(img, max_size=4096, quality=95)
```

## 🔧 故障排查

### 生成失败（输出黑色图片）

**检查步骤：**
1. 查看 info 输出中的错误信息
2. 确认 API Key 是否有效
3. 检查网络连接
4. 确认输入图片格式正确

**常见错误：**
- `Authentication failed` - API Key 无效
- `Network error` - 网络连接问题
- `No image found` - API 未返回图片

### 生成速度慢

**优化建议：**
1. 降低输出分辨率：4K → 2K → 1K
2. 减少输入图片数量
3. 使用稳定的网络连接
4. 检查日志确定瓶颈

### 图片质量不理想

**改善方法：**
1. 提高输出分辨率：1K → 2K → 4K
2. 调整纵横比匹配需求
3. 优化提示词描述
4. 提供更高质量的输入图片

## 🤖 模型信息

- **当前模型**：gemini-3-pro-image-preview
- **API 端点**：api.vectorengine.ai
- **支持功能**：
  - 文本生成图片
  - 图片编辑
  - 多图片合成
  - 风格迁移

## 📄 文件说明

```
ComfyUI-Vector-Engine/
├── vector_engine_node.py    # 主节点实现（已优化）
├── __init__.py              # 节点注册
├── config.example.py        # 配置说明和示例
├── README.md               # 完整使用文档（本文件）
├── .gitignore             # Git 忽略规则
├── test.py                # 测试脚本
└── assets/                # 测试资源（可选）
```

## 🐛 已知限制

1. **种子值**：seed 参数仅用于界面显示，不会传递给 API
2. **生成时间**：API 生成时间约 20-30 秒，无法优化
3. **图片数量**：最多支持 5 张输入图片
4. **模型固定**：当前只支持 gemini-3-pro-image-preview

## 📮 支持与反馈

如遇到问题或有功能建议，请提交 Issue 或 Pull Request。

## 📜 许可证

[请添加许可证信息]

---

**提示**：首次使用建议从 1K 分辨率开始测试，确认工作正常后再使用更高分辨率。
