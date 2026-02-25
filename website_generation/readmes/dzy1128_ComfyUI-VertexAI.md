# ComfyUI-VertexAI

Google Gemini 图像生成节点，用于 ComfyUI。

## 功能特点

- 🎨 支持使用 Google Gemini API 生成图像
- 🖼️ 支持最多 6 张输入图片（可选）
- ⚙️ 可自定义提示词、分辨率、随机种子等参数
- 📊 详细的生成信息输出

## 安装

### 1. 安装节点

将此文件夹放置在 ComfyUI 的 `custom_nodes` 目录下：

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/dzy1128/ComfyUI-VertexAI.git
```

### 2. 安装依赖

```bash
cd ComfyUI-VertexAI
pip install -r requirements.txt
```

或者直接安装：

```bash
pip install google-genai
```

### 3. 设置环境变量（重要！）

**必须设置以下两个环境变量：**

```bash
export GOOGLE_CLOUD_API_KEY=YOUR_API_KEY
export GOOGLE_GENAI_USE_VERTEXAI=True
```

**永久设置（推荐）：**

在 `~/.bashrc` 或 `~/.zshrc` 中添加：

```bash
echo 'export GOOGLE_CLOUD_API_KEY=YOUR_API_KEY' >> ~/.bashrc
echo 'export GOOGLE_GENAI_USE_VERTEXAI=True' >> ~/.bashrc
source ~/.bashrc
```

**验证环境变量：**

```bash
echo $GOOGLE_CLOUD_API_KEY
echo $GOOGLE_GENAI_USE_VERTEXAI
```

### 4. 重启 ComfyUI

设置完环境变量后，重启 ComfyUI 即可在节点列表中找到 "Gemini Image Generator"。

---

## 节点说明

### Gemini Image Generator

#### 输入参数（必填）

- **user_prompt**: 用户提示词（支持多行文本）
- **model_name**: 模型名称
  - `gemini-3-pro-image-preview`
  - `gemini-2.5-flash-image-preview`
- **aspect_ratio**: 图片宽高比
  - `1:1` - 正方形
  - `16:9` - 横屏
  - `9:16` - 竖屏
  - `4:3` - 传统横屏
  - `3:4` - 传统竖屏
  - `21:9` - 超宽屏
  - `3:2` - 相机比例
  - `2:3` - 相机竖屏
- **image_resolution**: 图片分辨率
  - `1K` - 约 1024 像素
  - `2K` - 约 2048 像素
  - `4K` - 约 4096 像素
- **seed**: 随机种子（0 到 2^64-1）

#### 输入参数（可选）

- **system_prompt**: 系统提示词（支持多行文本）
- **image_1 ~ image_6**: 最多 6 张输入图片（每张都是可选的）

#### 输出

- **image**: 生成的图片（ComfyUI IMAGE 格式）
- **info_text**: 生成信息文本，包含：
  - 用户提示词
  - 模型名称
  - 图片宽高比
  - 图片分辨率
  - 生成时间
  - 生成状态（成功/失败）
  - 错误信息（如果失败）

---

## 快速开始

### 1. 基本图像生成

最简单的使用方式：

```
[Gemini Image Generator]
  user_prompt: "一个美丽的日落场景"
  model_name: gemini-3-pro-image-preview
  aspect_ratio: 16:9
  image_resolution: 2K
  seed: 42
  
  → image (连接到 Preview Image)
  → info_text (连接到 Show Text)
```

### 2. 基于输入图片生成

使用现有图片作为参考：

```
[Load Image] → image_1 → [Gemini Image Generator]
  user_prompt: "将这张图片转换为油画风格"
  aspect_ratio: 1:1
  image_resolution: 2K
  
  → image (连接到 Save Image)
```

### 3. 多图片输入

使用多张参考图片：

```
[Load Image 1] → image_1 ↘
[Load Image 2] → image_2 → [Gemini Image Generator]
[Load Image 3] → image_3 ↗
  user_prompt: "结合这些图片的风格生成新图片"
  system_prompt: "请保持一致的艺术风格"
  
  → image
```

---

## 参数详解

### aspect_ratio 宽高比选项

控制生成图片的宽高比例：

- **1:1** - 正方形，适合头像、产品图
- **16:9** - 横屏，适合电脑壁纸、视频封面
- **9:16** - 竖屏，适合手机壁纸、社交媒体
- **4:3** - 传统横屏，适合演示文稿
- **3:4** - 传统竖屏，适合海报
- **21:9** - 超宽屏，适合影院风格
- **3:2** - 相机比例（横向）
- **2:3** - 相机比例（竖向）

### image_resolution 分辨率选项

控制生成图片的分辨率大小：

- **1K** - 约 1024 像素，快速生成，适合预览
- **2K** - 约 2048 像素，平衡质量和速度，推荐使用
- **4K** - 约 4096 像素，最高质量，生成较慢

> 💡 提示：实际像素取决于宽高比。例如 16:9 + 2K 会生成约 2048x1152 的图片。

### model_name 模型选择

**gemini-3-pro-image-preview**
- 高质量图像生成
- 更好的细节表现
- 适合专业创作

**gemini-2.5-flash-image-preview**
- 更快的生成速度
- 轻量级模型
- 适合快速迭代和预览

### seed 随机种子

- 相同的 seed + 相同的提示词 = 相似的结果
- seed = 0 表示随机
- 可用于复现特定的生成效果

### system_prompt vs user_prompt

- **system_prompt**: 全局指导，如风格、约束条件
  - 例如："请使用水彩画风格"
  
- **user_prompt**: 具体生成内容
  - 例如："一只猫坐在窗台上"

---

## 常见工作流

### 工作流 1: 图片编辑

```
[Load Image]
  ↓
[Gemini Image Generator]
  user_prompt: "Remove the background and add a sunset"
  ↓
[Preview Image]
```

### 工作流 2: 风格迁移

```
[Load Image (内容)] → image_1 ↘
[Load Image (风格)] → image_2 → [Gemini Image Generator]
                                  user_prompt: "Apply the style of image_2 to image_1"
                                  ↓
                                [Save Image]
```

### 工作流 3: 批量生成

```
[Text Input] → user_prompt
  ↓
[Gemini Image Generator]
  seed: 随机种子循环 (0-999)
  ↓
[Save Image (批量)]
```

---

## 提示词技巧

### 基础结构

```
[主题] + [风格] + [细节] + [质量]
```

示例：
```
"A majestic mountain landscape, oil painting style, 
with snow-capped peaks and pine forests, 
dramatic lighting, highly detailed, 4K quality"
```

### 图片编辑提示词

**添加元素：**
```
"Add a rainbow in the sky"
"Put a hat on the person"
```

**移除元素：**
```
"Remove the background"
"Delete all text from the image"
```

**修改风格：**
```
"Convert to anime style"
"Make it look like a vintage photograph"
```

**调整属性：**
```
"Change the time to night"
"Make the colors more vibrant"
```

---

## 故障排查

### 问题 1: "No image generated"

**原因：** 提示词可能违反了内容政策

**解决：**
- 修改提示词，使其更加中性
- 检查是否包含敏感词汇

### 问题 2: "API Key Error"

**原因：** 环境变量未设置或 API Key 无效

**解决：**
```bash
export GOOGLE_CLOUD_API_KEY=YOUR_API_KEY
export GOOGLE_GENAI_USE_VERTEXAI=True
```

然后重启 ComfyUI

### 问题 3: 生成图片质量不佳

**解决：**
- 提高分辨率（使用 2K 或 4K）
- 在提示词中添加质量关键词："highly detailed", "4K", "professional"
- 使用 system_prompt 指定风格

### 问题 4: 生成时间太长

**解决：**
- 降低分辨率（使用 1K）
- 简化提示词
- 减少输入图片数量

---

## 高级技巧

### 1. 使用系统提示词控制整体风格

```python
system_prompt: """
You are an expert digital artist specializing in photorealistic rendering.
Always ensure:
- High attention to detail
- Proper lighting and shadows
- Realistic textures
- Professional composition
"""

user_prompt: "A red sports car"
```

### 2. 链式生成

```
[Gemini Generator 1] 
  → image → [Gemini Generator 2]
             user_prompt: "Enhance and refine"
             → final_image
```

### 3. 保存生成信息

info_text 输出包含了所有生成信息，可以：
- 连接到 [Show Text] 节点查看
- 连接到 [Save Text] 节点保存
- 用于记录和复现生成过程

---

## 性能优化

1. **批量生成时**：使用较低分辨率（1K）先预览，确定效果后再用高分辨率生成

2. **多图输入时**：只使用必要的参考图片，过多图片会增加处理时间

3. **网络优化**：确保网络连接稳定，API 调用需要良好的网络环境

---

## 最佳实践

1. ✅ 使用清晰、具体的提示词
2. ✅ 先用低分辨率测试，再用高分辨率生成
3. ✅ 保存 info_text 以便追踪生成参数
4. ✅ 使用 seed 来复现满意的结果
5. ❌ 避免使用模糊或矛盾的提示词
6. ❌ 不要一次性使用过多输入图片

---

## 测试

可以运行 `test.py` 来测试 API 连接：

```bash
export GOOGLE_CLOUD_API_KEY=YOUR_API_KEY
export GOOGLE_GENAI_USE_VERTEXAI=True
python test.py
```

---

## 注意事项

- 需要有效的 Google Gemini API Key
- 必须设置 `GOOGLE_CLOUD_API_KEY` 和 `GOOGLE_GENAI_USE_VERTEXAI` 两个环境变量
- 确保已启用 Vertex AI API
- 生成时间取决于图片复杂度和分辨率
- 如果遇到问题，请先检查环境变量是否正确设置

---

## 文件说明

- `gemini_image_generator_node.py`: ComfyUI 节点主文件
- `__init__.py`: 节点注册文件
- `test.py`: API 测试脚本
- `requirements.txt`: 依赖包列表
- `README.md`: 完整文档（本文件）

---

## License

MIT
