# ComfyUI_Sora

<div align="center">

![ComfyUI_Sora](https://img.shields.io/badge/ComfyUI-Sora-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![Version](https://img.shields.io/badge/version-1.4.0-orange)

**专业的 ComfyUI Sora 视频生成节点集合**

支持文生视频、图生视频、视频增强、水印添加等全流程视频创作功能

[功能特性](#-功能特性) • [快速开始](#-快速开始) • [API 申请](#-api-key-申请指南) • [使用教程](#-使用教程) • [常见问题](#-常见问题)

</div>

---

## 📑 目录

- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [API Key 申请指南](#-api-key-申请指南)
- [配置说明](#-配置说明)
- [节点详解](#-节点详解)
- [使用教程](#-使用教程)
- [工作流示例](#-工作流示例)
- [最佳实践](#-最佳实践)
- [常见问题](#-常见问题)
- [更新日志](#-更新日志)

---

## ✨ 功能特性

### 🎬 核心节点

#### 1. Sora 文生视频节点
- **多 API 提供商支持**
  - T8 (ai.t8star.cn) - 稳定可靠
  - Comfly (ai.comfly.chat) - 高速响应
  - Aabao (newapi.ai) - 最新模型

- **多种宽高比支持**
  - 16:9 横版（YouTube、B站、电影）
  - 9:16 竖版（抖音、快手、Instagram Stories）

- **多种质量级别**
  - 720p 高清
  - 1080p 全高清
  - 2K 超高清
  - 4K 超高清

- **时长控制**
  - 5 秒（标准）
  - 10 秒（标准）
  - 15 秒（需要 15s 模型）
  - 25 秒（仅 sora-2-pro 模型）⭐

- **HD 高清模式** ⭐
  - 支持 sora-2-pro 和 sora-2 模型
  - 通过 `hd` 参数启用，由 API 自动处理
  - 更高的视频质量和细节（约 1.6 倍价格）
  - 不能与 25s 时长同时使用

- **丰富的风格选项**
  - 自动（Auto）
  - 电影感（Cinematic）
  - 写实（Realistic）
  - 动漫（Anime）
  - 3D 渲染（3D）
  - 油画（Oil Painting）
  - 水彩（Watercolor）

- **精细控制**
  - 运动强度控制（0.0-1.0）
  - 随机种子控制（可复现）

#### 2. Sora 图生视频节点
- **图像输入支持**
  - 支持 ComfyUI 标准 IMAGE 格式
  - 自动调整图像尺寸以匹配目标宽高比

- **运动控制**
  - 自动运动
  - 方向控制（前、后、左、右、上、下）
  - 镜头控制（放大、缩小、旋转）
  - 运动强度调节

- **风格迁移**
  - 保持原样
  - 电影感、写实、动漫、3D
  - 油画、水彩

#### 3. Sora 多图参考视频生成节点 ⭐

> **✨ 新功能**：支持最多 4 张图片作为参考生成视频

- **多图输入**
  - 支持 1-4 张参考图片
  - 自动转换为 base64 格式
  - 仅 Comfly API 支持

- **高级控制**
  - HD 高清模式支持
  - 时长控制（5s-25s）
  - 随机种子控制

- **应用场景**
  - 多角度视频生成
  - 故事板转视频
  - 风格融合创作
  - 场景过渡效果

#### 4. Grok Imagine 视频生成节点 ⭐

> **✨ 新功能**：使用 xAI 的 Grok Imagine 0.9 模型生成视频

- **模型特性**
  - 基于 Aurora 引擎的视频生成模型
  - 原生音频-视频同步
  - 24 FPS，1024×1024 分辨率
  - 生成速度：12-15 秒

- **双模式支持** ⭐
  - **文本生成视频**（Text-to-Video）
    - 纯文本提示词生成视频
    - 适合从零创作
  - **图像生成视频**（Image-to-Video）
    - 将静态图片转换为动态视频
    - 支持 ComfyUI IMAGE 格式
    - 自动添加运动和音频

- **时长控制**
  - 6 秒（快速）
  - 8 秒（标准）
  - 10 秒（推荐）
  - 12 秒（详细）
  - 15 秒（最长）

- **质量选项**
  - Standard（标准）
  - High（高质量）

- **风格模式**
  - Normal（正常）
  - Fun（趣味）
  - Spicy（激烈）
  - Custom（自定义）

- **API 支持**
  - 仅支持 Aabao API 提供商
  - 通过 Chat Completions 端点调用
  - 支持多模态输入（文本 + 图像）
  - 按次计费（$0.240-$1.600/次）

- **应用场景**
  - 快速视频原型制作
  - 静态图片动画化
  - 音频-视觉同步内容
  - 营销视频生成
  - 社交媒体内容创作
  - 照片转短视频

#### 5. Topaz 视频增强节点 ⭐

> **⚠️ 注意**：此节点需要另外安装 [Topaz Video AI](https://www.topazlabs.com/topaz-video-ai) 软件才能使用

- **专业视频增强**
  - AI 超分辨率（最高 8K）
  - 去噪、去模糊
  - 帧率提升（最高 120fps）
  - 多种增强模型

- **智能输入处理**
  - 支持文件路径
  - 支持 ComfyUI VIDEO 对象
  - 自动提取视频路径

#### 6. 视频水印节点
- **基础水印**
  - 文字水印
  - 图片水印
  - 位置控制（9 个预设位置）
  - 透明度控制

- **高级水印** ⭐
  - 动态动画效果（淡入淡出、滑动、缩放、旋转等）
  - 多位置模式（单点、Z 字形、随机等）
  - 批量处理
  - 目标跟踪（实验性）

#### 7. 帧混合器节点
- **时间平滑**
  - 多帧混合
  - 降噪
  - 运动模糊效果

---

## 🚀 快速开始

### 📦 安装

#### 方法 1：通过 ComfyUI Manager（推荐）

1. 打开 ComfyUI Manager
2. 搜索 "ComfyUI_Sora"
3. 点击 "Install"
4. 重启 ComfyUI

#### 方法 2：手动安装

1. 克隆项目到 ComfyUI 的 `custom_nodes` 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI_Sora.git
```

2. 安装依赖：
```bash
cd ComfyUI_Sora
pip install -r requirements.txt
```

3. 重启 ComfyUI

### ✅ 验证安装

重启 ComfyUI 后，在控制台应该看到：
```
================================================================================
ComfyUI_Sora Nodes Loaded Successfully!
================================================================================
Available Nodes:
  * Sora Text2Video - Generate high-quality videos from text
  * Sora Image2Video - Generate dynamic videos from images
  * Topaz Video Enhancer - Professional video upscaling and enhancement (Requires Topaz Video AI software)
  * Frame Blender - Multi-frame blending and temporal averaging
  * Video Watermark - Add dynamic watermarks to videos
  * Video Watermark Advanced - Target tracking, anti-occlusion, batch processing
================================================================================
```

在节点菜单中，你应该能看到 `Ken-Chen/sora` 分类下的所有节点。

---

## 🔑 API Key 申请指南

### 1. T8 API (ai.t8star.cn) ⭐ 推荐

**特点**：
- ✅ 稳定可靠
- ✅ 价格实惠
- ✅ 支持多种模型
- ✅ 响应速度快

**申请步骤**：

1. **访问官网**
   - 打开 [https://ai.t8star.cn](https://ai.t8star.cn)

2. **注册账号**
   - 点击右上角"注册"
   - 填写邮箱和密码
   - 验证邮箱

3. **充值**
   - 登录后点击"充值"
   - 选择充值金额（建议先充值 10-20 元测试）
   - 支持支付宝、微信支付

4. **获取 API Key**
   - 进入"个人中心" → "API 密钥"
   - 点击"创建新密钥"
   - 复制生成的 API Key（格式：`sk-xxxxxx`）

5. **配置到 ComfyUI**
   ```json
   {
       "api_key": "sk-xxxxxx",
       "api_provider": "t8",
       "base_url": "https://ai.t8star.cn/v1"
   }
   ```

**价格参考**：
- 5 秒视频：约 0.5-1 元
- 10 秒视频：约 1-2 元
- 15 秒视频：约 2-3 元

---

### 2. Comfly API (ai.comfly.chat)

**特点**：
- ✅ 高速响应
- ✅ 支持最新模型
- ✅ 稳定性好

**申请步骤**：

1. **访问官网**
   - 打开 [https://ai.comfly.chat](https://ai.comfly.chat)

2. **注册账号**
   - 点击"注册"
   - 填写邮箱和密码
   - 验证邮箱

3. **充值**
   - 登录后进入"充值中心"
   - 选择充值金额
   - 支持多种支付方式

4. **获取 API Key**
   - 进入"API 管理"
   - 点击"创建 API Key"
   - 复制生成的密钥

5. **配置到 ComfyUI**
   ```json
   {
       "comfly_api_key": "your-comfly-api-key",
       "comfly_base_url": "https://ai.comfly.chat/v1"
   }
   ```

---

### 3. Aabao API (newapi.ai) ⭐ 最新模型

**特点**：
- ✅ 支持最新 sora-2-pro 模型
- ✅ 支持 25 秒超长视频
- ✅ 支持自定义分辨率
- ✅ 质量最高

**申请步骤**：

1. **访问官网**
   - 打开 [https://newapi.ai](https://newapi.ai) 或 [https://api.aabao.top](https://api.aabao.top)

2. **注册账号**
   - 点击"注册"
   - 填写信息并验证

3. **充值**
   - 进入"充值"页面
   - 选择充值金额（建议先充值 20-50 元）
   - 支持多种支付方式

4. **获取 API Key**
   - 进入"API 密钥管理"
   - 创建新密钥
   - 复制 API Key

5. **配置到 ComfyUI**
   ```json
   {
       "aabao_api_key": "your-aabao-api-key",
       "aabao_base_url": "https://api.aabao.top/v1"
   }
   ```

**价格参考**：
- sora-2-pro 25 秒视频：约 5-10 元
- sora-2 10 秒视频：约 1-2 元

**独家模型**：
- `sora-2-pro` - 最高质量，支持 25 秒
- `sora-2-landscape` - 横屏优化
- `sora-2-portrait` - 竖屏优化
- `sora-2-landscape-15s` - 横屏 15 秒
- `sora-2-portrait-15s` - 竖屏 15 秒

---

## ⚙️ 配置说明

### 方法 1：通过节点参数配置（推荐新手）

在节点的参数中直接设置：
- `api_provider`: 选择 API 提供商（t8 / comfly / aabao）
- `api_key`: 输入对应的 API Key

**优点**：
- ✅ 简单直观
- ✅ 可以在不同节点使用不同 API

**缺点**：
- ❌ 每次都要输入
- ❌ 工作流分享时可能泄露 API Key

---

### 方法 2：通过配置文件配置（推荐高级用户）

在 `ComfyUI_Sora` 目录下创建 `config.json` 文件：

```json
{
    "api_key": "your-t8-api-key-here",
    "api_provider": "t8",
    "base_url": "https://ai.t8star.cn/v1",

    "comfly_api_key": "your-comfly-api-key-here",
    "comfly_base_url": "https://ai.comfly.chat/v1",

    "aabao_api_key": "your-aabao-api-key-here",
    "aabao_base_url": "https://api.aabao.top/v1",

    "timeout": 600,
    "default_model": "sora_video2",
    "default_quality": "1080p",
    "default_aspect_ratio": "16:9",
    "default_duration": 5,
    "max_retries": 3,
    "retry_delay": 5
}
```

**优点**：
- ✅ 一次配置，永久使用
- ✅ 支持多个 API 提供商
- ✅ 工作流分享时不会泄露 API Key

**缺点**：
- ❌ 需要手动创建文件

---

### 配置参数说明

| 参数 | 说明 | 默认值 |
|-----|------|--------|
| `api_key` | T8 API 密钥 | - |
| `api_provider` | API 提供商（t8/comfly/aabao） | t8 |
| `base_url` | T8 API 地址 | https://ai.t8star.cn/v1 |
| `comfly_api_key` | Comfly API 密钥 | - |
| `comfly_base_url` | Comfly API 地址 | https://ai.comfly.chat/v1 |
| `aabao_api_key` | Aabao API 密钥 | - |
| `aabao_base_url` | Aabao API 地址 | https://api.aabao.top/v1 |
| `timeout` | 请求超时时间（秒） | 600 |
| `default_model` | 默认模型 | sora_video2 |
| `default_quality` | 默认质量 | 1080p |
| `default_aspect_ratio` | 默认宽高比 | 16:9 |
| `default_duration` | 默认时长（秒） | 5 |
| `max_retries` | 最大重试次数 | 3 |
| `retry_delay` | 重试延迟（秒） | 5 |

---

## 📚 节点详解

### 1. 🎬 Sora 文生视频节点

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `prompt` | 文本 | 视频描述提示词 | "一只可爱的小猫在阳光下玩耍" |
| `aspect_ratio` | 选择 | 宽高比（16:9 / 9:16） | 16:9 |
| `quality` | 选择 | 质量（720p / 1080p / 2k / 4k） | 1080p |
| `duration` | 选择 | 时长（5s / 10s / 15s / 25s (Pro)） | 5s |
| `hd` | 布尔 | HD高清模式（通过 `hd` 参数传递给 API）⭐ | False |
| `api_provider` | 选择 | API 提供商（t8 / comfly / aabao） | t8 |
| `api_key` | 文本 | API 密钥（可选） | - |
| `model` | 选择 | 模型选择 | sora_video2 |
| `style` | 选择 | 风格（auto / cinematic / realistic 等） | auto |
| `motion_intensity` | 浮点 | 运动强度（0.0-1.0） | 0.5 |
| `seed` | 整数 | 随机种子（-1 为随机） | -1 |
| `output_dir` | 文本 | 输出目录 | sora_videos |

**输出**：
- `video`: VIDEO 对象
- `Filenames`: VHS_FILENAMES 格式
- `video_url`: 视频 URL
- `response_info`: 响应信息（JSON）
- `prompt_used`: 实际使用的提示词

**支持的模型**：
- `sora_video2` - T8/Comfly 标准模型
- `sora_video2-portrait-hd` - 竖屏高清
- `sora_video2-landscape-hd` - 横屏高清
- `sora-2-pro` - Aabao 最高质量（支持 25s）⭐
- `sora-2` - Aabao 标准模型
- `[Aabao] sora-2-landscape` - 横屏优化
- `[Aabao] sora-2-portrait` - 竖屏优化
- `[Aabao] sora-2-landscape-15s` - 横屏 15 秒
- `[Aabao] sora-2-portrait-15s` - 竖屏 15 秒

---

### 2. 🖼️ Sora 图生视频节点

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `image` | IMAGE | 输入图像 | - |
| `prompt` | 文本 | 视频描述提示词 | "镜头缓慢向前推进" |
| `aspect_ratio` | 选择 | 宽高比 | 16:9 |
| `quality` | 选择 | 质量 | 1080p |
| `duration` | 选择 | 时长 | 5s |
| `hd` | 布尔 | HD高清模式（仅sora-2-pro/sora-2支持，不能与25s同时使用）⭐ | False |
| `motion_direction` | 选择 | 运动方向 | auto |
| `motion_intensity` | 浮点 | 运动强度 | 0.5 |
| `style` | 选择 | 风格 | keep_original |

**运动方向选项**：
- `auto` - 自动
- `forward` - 向前
- `backward` - 向后
- `left` - 向左
- `right` - 向右
- `up` - 向上
- `down` - 向下
- `zoom_in` - 放大
- `zoom_out` - 缩小
- `rotate_cw` - 顺时针旋转
- `rotate_ccw` - 逆时针旋转

---

### 3. 🎨 Topaz 视频增强节点

> **⚠️ 重要**：此节点需要另外安装 [Topaz Video AI](https://www.topazlabs.com/topaz-video-ai) 软件才能使用

**前置要求**：
- ✅ 必须安装 Topaz Video AI 软件（付费软件）
- ✅ 支持 Windows 和 macOS
- ✅ 下载地址：[https://www.topazlabs.com/topaz-video-ai](https://www.topazlabs.com/topaz-video-ai)

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `video` | VIDEO/STRING | 输入视频 | - |
| `enhancement_model` | 选择 | 增强模型 | Artemis - High Quality |
| `output_resolution` | 选择 | 输出分辨率 | 原始分辨率 |
| `fps` | 选择 | 输出帧率 | 原始帧率 |
| `denoise` | 选择 | 降噪强度 | auto |
| `sharpen` | 选择 | 锐化强度 | auto |

**增强模型**：
- **Artemis 系列** - 通用增强
  - High Quality - 高质量
  - Low Quality - 低质量输入
  - Medium Quality - 中等质量
- **Proteus 系列** - 细节增强
  - Fine Tune - 精细调整
  - Auto - 自动
- **Iris 系列** - 去隔行
  - Low Quality - 低质量
  - Medium Quality - 中等质量

**输出分辨率**：
- 原始分辨率
- 720p (1280x720)
- 1080p (1920x1080)
- 2K (2560x1440)
- 4K (3840x2160)
- 8K (7680x4320)

---

### 4. 🖼️🖼️ Sora 多图参考视频生成节点 ⭐

> **✨ 新功能**：支持最多 4 张图片作为参考生成视频

**功能特点**：
- ✅ 支持 1-4 张参考图片
- ✅ 仅 Comfly API 支持此功能
- ✅ 支持 HD 高清模式
- ✅ 支持 sora-2 和 sora-2-pro 模型

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `prompt` | 文本 | 视频描述提示词 | "根据参考图片生成视频" |
| `aspect_ratio` | 选择 | 宽高比（16:9 / 9:16） | 16:9 |
| `quality` | 选择 | 质量（720p / 1080p / 2k / 4k） | 1080p |
| `duration` | 选择 | 时长（5s / 10s / 15s / 25s (Pro)） | 10s |
| `hd` | 布尔 | HD高清模式（不能与25s同时使用） | False |
| `image1` | IMAGE | 第1张参考图片（可选） | - |
| `image2` | IMAGE | 第2张参考图片（可选） | - |
| `image3` | IMAGE | 第3张参考图片（可选） | - |
| `image4` | IMAGE | 第4张参考图片（可选） | - |
| `api_provider` | 选择 | API 提供商（仅支持 comfly） | comfly |
| `api_key` | 文本 | API 密钥（可选） | - |
| `model` | 选择 | 模型（sora-2 / sora-2-pro） | sora-2 |
| `seed` | 整数 | 随机种子（-1 为随机） | -1 |
| `output_dir` | 文本 | 输出目录 | sora_videos |

**输出**：
- `video`: VIDEO 对象
- `Filenames`: VHS_FILENAMES 格式
- `video_url`: 视频 URL
- `response_info`: 响应信息（JSON）
- `prompt_used`: 实际使用的提示词

**使用说明**：
1. **至少提供 1 张图片**：必须连接至少一个 image 输入
2. **图片顺序**：按 image1 → image2 → image3 → image4 的顺序提供
3. **API 限制**：此功能仅 Comfly API 支持，会自动切换到 Comfly
4. **HD 限制**：HD 模式和 25s 时长不能同时使用
5. **模型限制**：仅支持 sora-2 和 sora-2-pro 模型

**应用场景**：
- 📸 **多角度视频**：使用多张不同角度的照片生成连贯视频
- 🎬 **故事板视频**：将故事板图片转换为动态视频
- 🎨 **风格融合**：结合多张不同风格的图片生成独特视频
- 🏞️ **场景过渡**：使用多张场景图片生成平滑过渡视频

**示例提示词**：
```
根据这些参考图片，生成一段流畅的视频，展示从白天到黄昏的景色变化，镜头缓慢推进
```

---

### 5. 🎨 视频水印节点

#### 基础水印节点

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `video` | VIDEO | 输入视频 | - |
| `text` | 文本 | 水印文字 | "Watermark" |
| `position` | 选择 | 位置 | bottom_right |
| `font_size` | 整数 | 字体大小 | 48 |
| `opacity` | 浮点 | 透明度（0.0-1.0） | 0.5 |
| `color` | 文本 | 颜色（RGB） | "255,255,255" |

**位置选项**：
- `top_left` - 左上
- `top_center` - 上中
- `top_right` - 右上
- `center_left` - 左中
- `center` - 正中
- `center_right` - 右中
- `bottom_left` - 左下
- `bottom_center` - 下中
- `bottom_right` - 右下

#### 高级水印节点 ⭐

**额外功能**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `animation` | 选择 | 动画效果 | none |
| `multi_position` | 选择 | 多位置模式 | single |
| `batch_mode` | 布尔 | 批量处理 | False |

**动画效果**：
- `none` - 无动画
- `fade_in` - 淡入
- `fade_out` - 淡出
- `fade_in_out` - 淡入淡出
- `slide_in_left` - 从左滑入
- `slide_in_right` - 从右滑入
- `slide_in_top` - 从上滑入
- `slide_in_bottom` - 从下滑入
- `zoom_in` - 放大
- `zoom_out` - 缩小
- `rotate` - 旋转
- `pulse` - 脉冲
- `bounce` - 弹跳

**多位置模式**：
- `single` - 单个位置
- `z_pattern` - Z 字形
- `random` - 随机位置
- `corners` - 四角
- `edges` - 四边

---

### 5. 🎨 帧混合器节点

**输入参数**：

| 参数 | 类型 | 说明 | 默认值 |
|-----|------|------|--------|
| `video` | VIDEO | 输入视频 | - |
| `blend_frames` | 整数 | 混合帧数（3-15） | 5 |
| `blend_mode` | 选择 | 混合模式 | average |

**混合模式**：
- `average` - 平均
- `weighted` - 加权平均
- `median` - 中值

**用途**：
- 降噪
- 运动模糊
- 时间平滑

---

## 📖 使用教程

### 教程 1：生成第一个视频（文生视频）

1. **添加节点**
   - 在 ComfyUI 中右键 → `Add Node` → `Ken-Chen/sora` → `🎬 Sora 文生视频`

2. **配置参数**
   ```
   prompt: 一只可爱的金毛犬在海滩上奔跑，阳光洒在海面上
   aspect_ratio: 16:9
   quality: 1080p
   duration: 5s
   api_provider: t8
   api_key: sk-xxxxxx（或留空使用配置文件）
   ```

3. **运行生成**
   - 点击 `Queue Prompt`
   - 等待 2-5 分钟（取决于时长和质量）

4. **查看结果**
   - 视频保存在 `ComfyUI/output/sora_videos/` 目录
   - 可以连接 `Preview Video` 节点预览

---

### 教程 2：图片转视频（图生视频）

1. **准备图片**
   - 添加 `Load Image` 节点
   - 选择一张图片

2. **添加图生视频节点**
   - 右键 → `Add Node` → `Ken-Chen/sora` → `🖼️ Sora 图生视频`

3. **连接节点**
   - 将 `Load Image` 的 `IMAGE` 输出连接到 `Sora 图生视频` 的 `image` 输入

4. **配置参数**
   ```
   prompt: 镜头缓慢向前推进，展现更多细节
   motion_direction: forward
   motion_intensity: 0.5
   style: cinematic
   ```

5. **运行生成**
   - 点击 `Queue Prompt`
   - 等待生成完成

---

### 教程 3：视频增强（Topaz）

1. **前置准备**
   - 确保已安装 Topaz Video AI
   - 确保 Topaz 安装在默认路径

2. **添加节点**
   - 右键 → `Add Node` → `Ken-Chen/sora` → `🎨 Topaz 视频增强`

3. **连接视频**
   - 将 Sora 节点的 `video` 输出连接到 Topaz 节点的 `video` 输入

4. **配置参数**
   ```
   enhancement_model: Artemis - High Quality
   output_resolution: 4K (3840x2160)
   fps: 原始帧率
   denoise: auto
   sharpen: auto
   ```

5. **运行增强**
   - 点击 `Queue Prompt`
   - 等待处理完成（可能需要较长时间）

---

### 教程 4：添加水印

1. **添加水印节点**
   - 右键 → `Add Node` → `Ken-Chen/sora` → `🎨 Video Watermark`

2. **连接视频**
   - 将视频输出连接到水印节点

3. **配置水印**
   ```
   text: @YourChannel
   position: bottom_right
   font_size: 48
   opacity: 0.7
   color: 255,255,255
   ```

4. **高级效果**（使用高级水印节点）
   ```
   animation: fade_in_out
   multi_position: z_pattern
   ```

---

## 🎯 工作流示例

我们提供了 9 个即用型工作流，可直接导入 ComfyUI 使用：

### Sora 工作流

| 工作流 | 场景 | 宽高比 | 难度 |
|--------|------|--------|------|
| [01_基础文生视频](workflows/01_basic_text2video.json) | YouTube、电影 | 16:9 | ⭐ |
| [02_竖版短视频](workflows/02_vertical_video.json) | 抖音、快手 | 9:16 | ⭐ |
| [03_图生视频](workflows/03_image2video.json) | 图片动态化 | 16:9 | ⭐⭐ |
| [04_多风格对比](workflows/04_multi_style_comparison.json) | 风格探索 | 16:9 | ⭐⭐⭐ |
| [05_图生视频高级](workflows/05_image2video_advanced.json) | 运动控制 | 16:9 | ⭐⭐⭐ |
| [06_方形社交媒体](workflows/06_square_social_media.json) | Instagram | 1:1 | ⭐ |

### Grok Imagine 工作流 ⭐

| 工作流 | 场景 | 模式 | 难度 |
|--------|------|------|------|
| [07_Grok文生视频](workflows/07_grok_imagine_text2video.json) | 快速视频原型 | Text-to-Video | ⭐ |
| [08_Grok图生视频](workflows/08_grok_imagine_image2video.json) | 照片动画化 | Image-to-Video | ⭐⭐ |
| [09_Grok风格对比](workflows/09_grok_imagine_style_comparison.json) | 风格探索 | Text-to-Video | ⭐⭐⭐ |

**使用方法**：
1. 将 JSON 文件拖放到 ComfyUI 窗口，或点击 "Load" 加载
2. 修改提示词和参数
3. 点击 "Queue Prompt" 生成

详细说明请查看 [工作流文档](workflows/README.md)

---

## 💡 使用示例

### 示例 1：横版视频（YouTube / B站）

```
提示词：一只可爱的金毛犬在海滩上奔跑，阳光洒在海面上，波浪轻轻拍打着沙滩，电影级画质
宽高比：16:9
质量：1080p
时长：5s
风格：cinematic
运动强度：0.6
API 提供商：t8
```

**预期效果**：
- 横屏视频，适合 YouTube、B站
- 电影感画面，色彩饱和
- 流畅的运动

---

### 示例 2：竖版短视频（抖音 / 快手）

```
提示词：城市夜景，霓虹灯闪烁，车流穿梭，从高楼俯瞰，赛博朋克风格
宽高比：9:16
质量：1080p
时长：10s
风格：cinematic
运动强度：0.7
API 提供商：comfly
```

**预期效果**：
- 竖屏视频，适合抖音、快手
- 动感十足的城市夜景
- 赛博朋克氛围

---

### 示例 3：超长视频（sora-2-pro）⭐

```
提示词：清晨的森林，阳光透过树叶洒下，薄雾弥漫，小鹿在林间漫步，镜头缓慢跟随
宽高比：16:9
质量：1080p
时长：25s (Pro)
模型：sora-2-pro
风格：realistic
运动强度：0.4
API 提供商：aabao
```

**预期效果**：
- 25 秒超长视频
- 最高质量
- 自然流畅的镜头运动

**注意**：
- 仅 sora-2-pro 模型支持 25 秒
- 生成时间约 20-30 分钟
- 费用较高（约 5-10 元）

---

### 示例 4：图生视频（图片动态化）

```
输入：一张风景照片（山脉、湖泊）
提示词：镜头缓慢向前推进，展现更多细节，云朵飘动
运动方向：forward
运动强度：0.5
风格：keep_original
时长：5s
```

**预期效果**：
- 静态图片变成动态视频
- 保持原图风格
- 自然的镜头推进

---

### 示例 5：图生视频（人物动态）

```
输入：一张人物肖像
提示词：人物微笑，头发随风飘动，眼神生动
运动方向：auto
运动强度：0.3
风格：cinematic
时长：5s
```

**预期效果**：
- 人物表情生动
- 自然的微动效果
- 电影感画面

---

### 示例 6：Grok Imagine 文本生成视频 ⭐

```
节点：GrokImagineNode
提示词：A majestic golden eagle soaring through a mountain valley at sunset, with dramatic lighting and cinematic camera movement
时长：10秒
质量：high
风格：normal
API 提供商：aabao
```

**预期效果**：
- 6-15 秒带音频的视频
- 原生音频-视频同步
- 生成速度：12-15 秒
- 1024×1024 分辨率，24 FPS

**特点**：
- ✅ 自动生成背景音乐和环境音
- ✅ 快速生成（比 Sora 快 10 倍）
- ✅ 适合快速原型制作

---

### 示例 7：Grok Imagine 图像生成视频 ⭐

```
节点：GrokImagineNode
输入：一张人物肖像照片
提示词：Make the person smile naturally and blink, add subtle head movement, with soft lighting
时长：6秒
质量：high
风格：normal
API 提供商：aabao
```

**预期效果**：
- 静态照片变成动态视频
- 人物自然微笑和眨眼
- 带有同步的环境音
- 适合社交媒体分享

**应用场景**：
- ✅ 照片动画化
- ✅ 产品展示视频
- ✅ 历史照片复活
- ✅ 艺术作品动态化

---

### 示例 8：Grok Imagine 风格对比

```
节点：GrokImagineNode (3个)
提示词：A cute cat playing with a ball of yarn in a cozy living room
时长：8秒
质量：high
种子：42 (固定种子确保可比性)

风格 1：normal - 真实自然
风格 2：fun - 趣味活泼，色彩鲜艳
风格 3：spicy - 戏剧性强烈，视觉冲击
```

**预期效果**：
- 相同提示词，不同风格表现
- 可对比选择最佳效果
- 探索创意可能性

---

## 🎨 最佳实践

### 提示词编写技巧

#### 1. 描述要具体详细

❌ **不好的提示词**：
```
一只狗
```

✅ **好的提示词**：
```
一只金毛犬在阳光明媚的草地上欢快地奔跑，尾巴摇摆，舌头伸出
```

---

#### 2. 包含镜头运动描述

❌ **不好的提示词**：
```
城市街道
```

✅ **好的提示词**：
```
城市街道，镜头从低角度向上仰拍，缓慢推进，逐渐展现高楼大厦的壮观
```

**常用镜头运动词汇**：
- 推进（push in）
- 拉远（pull out）
- 平移（pan）
- 跟随（follow）
- 俯拍（top-down）
- 仰拍（low-angle）
- 环绕（orbit）

---

#### 3. 添加氛围和情绪

❌ **不好的提示词**：
```
森林
```

✅ **好的提示词**：
```
清晨的森林，阳光透过树叶洒下斑驳的光影，薄雾在林间缓缓流动，宁静祥和
```

**氛围词汇**：
- 时间：清晨、黄昏、午夜、黎明
- 天气：晴朗、多云、雨天、雪天
- 光线：柔和、强烈、逆光、侧光
- 情绪：宁静、激动、神秘、浪漫

---

#### 4. 指定画面质量和风格

✅ **推荐添加**：
```
电影级画质，4K超高清，专业摄影，色彩饱和，细节丰富
```

**质量词汇**：
- 电影级（cinematic）
- 专业摄影（professional photography）
- 高清（high definition）
- 细节丰富（highly detailed）
- 色彩鲜艳（vibrant colors）

---

### 参数选择建议

#### 宽高比选择

| 宽高比 | 适用场景 | 推荐用途 |
|--------|---------|---------|
| **16:9** | YouTube、B站、电影 | 风景、产品宣传、教程 |
| **9:16** | 抖音、快手、Instagram Stories | 人物特写、短视频、竖屏内容 |

#### 质量选择

| 质量 | 分辨率 | 适用场景 | 生成时间 | 费用 |
|-----|--------|---------|---------|------|
| **720p** | 1280x720 | 快速预览、测试 | 快 | 低 |
| **1080p** | 1920x1080 | 标准输出、社交媒体 | 中 | 中 |
| **2K** | 2560x1440 | 高质量输出 | 慢 | 高 |
| **4K** | 3840x2160 | 专业制作、大屏展示 | 很慢 | 很高 |

**建议**：
- ✅ 先用 720p 测试提示词和参数
- ✅ 满意后再用 1080p 或更高质量生成
- ✅ 4K 仅用于专业项目

---

#### 时长选择

| 时长 | 适用场景 | 生成时间 | 费用 | 支持模型 |
|-----|---------|---------|------|---------|
| **5s** | 快速预览、测试 | 2-3 分钟 | 低 | 所有模型 |
| **10s** | 标准短视频 | 3-5 分钟 | 中 | 所有模型 |
| **15s** | 长视频 | 5-10 分钟 | 高 | 15s 模型 |
| **25s** | 超长视频 ⭐ | 20-30 分钟 | 很高 | 仅 sora-2-pro |

---

#### API 提供商选择

| 提供商 | 特点 | 推荐场景 |
|--------|------|---------|
| **T8** | 稳定、价格实惠 | 日常使用、批量生成 |
| **Comfly** | 高速响应 | 快速测试、紧急项目 |
| **Aabao** | 最新模型、最高质量 | 专业项目、25s 视频 |

---

### 高级技巧

#### 1. 种子控制（可复现）

使用相同的种子值可以生成相似的视频，便于微调和迭代：

```
seed: 12345  # 固定种子，每次生成相似结果
seed: -1     # 随机种子，每次生成不同结果
```

**使用场景**：
- ✅ 微调提示词时保持画面一致
- ✅ 生成系列视频时保持风格统一
- ✅ A/B 测试不同参数

---

#### 2. 运动强度控制

| 强度 | 范围 | 效果 | 适用场景 |
|-----|------|------|---------|
| **低** | 0.0-0.3 | 缓慢、平稳 | 风景、静物、延时摄影 |
| **中** | 0.4-0.6 | 自然、流畅 | 大多数场景 |
| **高** | 0.7-1.0 | 快速、动态 | 运动、动作、快节奏 |

---

#### 3. 风格组合

可以在提示词中组合多种风格描述：

```
提示词：一座未来城市，赛博朋克风格，霓虹灯光，电影级画质，3D渲染效果，细节丰富
```

**风格关键词**：
- 电影感：cinematic, film grain, depth of field
- 写实：realistic, photorealistic, lifelike
- 动漫：anime style, cel shading, vibrant colors
- 3D：3D render, CGI, ray tracing
- 艺术：oil painting, watercolor, impressionist

---

#### 4. 多模型对比

对于重要项目，建议使用多个模型生成，选择最佳结果：

1. 使用 `sora_video2` 快速测试
2. 使用 `sora-2` 生成标准版本
3. 使用 `sora-2-pro` 生成最高质量版本
4. 对比选择最佳结果

---

## 📊 输出说明

### Sora 节点输出

每个 Sora 节点返回 5 个输出：

| 输出 | 类型 | 说明 | 用途 |
|-----|------|------|------|
| `video` | VIDEO | 视频对象 | 连接到其他视频处理节点 |
| `Filenames` | VHS_FILENAMES | VHS 格式文件名 | 兼容 VHS 节点 |
| `video_url` | STRING | 视频 URL | 分享、下载、调试 |
| `response_info` | STRING | 响应信息（JSON） | 查看生成参数、调试 |
| `prompt_used` | STRING | 实际使用的提示词 | 查看完整提示词 |

### 视频保存位置

生成的视频保存在：
```
ComfyUI/output/sora_videos/sora_YYYYMMDD_HHMMSS_xxxxx.mp4
```

**文件命名规则**：
- `sora_` - 前缀
- `YYYYMMDD_HHMMSS` - 时间戳
- `xxxxx` - 随机 ID
- `.mp4` - 格式

---

## ⚠️ 注意事项

### 1. API 密钥安全 🔒

- ❌ **不要**在公开的工作流中包含 API 密钥
- ✅ **建议**使用配置文件方式管理密钥
- ✅ **建议**使用环境变量存储密钥
- ❌ **不要**将包含密钥的配置文件提交到 Git

### 2. 网络要求 🌐

- ✅ 需要稳定的网络连接
- ✅ 视频生成和下载可能需要较长时间
- ✅ 建议使用代理（如果在国内）
- ✅ 确保防火墙允许访问 API 地址

### 3. 资源消耗 💰

| 质量 | 时长 | 预估费用 | 生成时间 |
|-----|------|---------|---------|
| 720p | 5s | 0.3-0.5 元 | 2-3 分钟 |
| 1080p | 5s | 0.5-1 元 | 3-5 分钟 |
| 1080p | 10s | 1-2 元 | 5-8 分钟 |
| 1080p | 15s | 2-3 元 | 10-15 分钟 |
| 1080p | 25s (Pro) | 5-10 元 | 20-30 分钟 |

**建议**：
- ✅ 先用 720p 测试提示词
- ✅ 满意后再用高质量生成
- ✅ 避免重复生成相同内容

### 4. 提示词限制 📝

- ❌ 避免包含敏感、违规内容
- ❌ 避免暴力、血腥、色情内容
- ❌ 避免政治敏感内容
- ✅ 提示词建议在 200 字以内
- ✅ 使用中性、积极的描述

### 5. 生成时间 ⏱️

**sora-2-pro 模型特别说明**：
- ⚠️ 25 秒视频生成需要 **20-30 分钟**
- ⚠️ 请耐心等待，不要中断
- ⚠️ 轮询超时已设置为 40 分钟
- ✅ 可以在控制台查看进度

---

## 🐛 常见问题

### Q1: 节点无法加载

**症状**：
- ComfyUI 启动后看不到 Sora 节点
- 控制台报错

**解决方案**：
1. 检查是否安装了所有依赖：
   ```bash
   cd ComfyUI/custom_nodes/ComfyUI_Sora
   pip install -r requirements.txt
   ```

2. 检查 Python 版本（建议 3.9+）：
   ```bash
   python --version
   ```

3. 检查是否有语法错误：
   ```bash
   python -m py_compile sora_text2video.py
   ```

4. 重启 ComfyUI

---

### Q2: API 调用失败

**症状**：
- 提示 "API 调用失败"
- 提示 "401 Unauthorized"
- 提示 "网络连接错误"

**解决方案**：

1. **检查 API 密钥是否正确**：
   - 确认密钥格式正确（通常以 `sk-` 开头）
   - 确认密钥未过期
   - 确认密钥有足够余额

2. **检查网络连接**：
   ```bash
   ping ai.t8star.cn
   ```

3. **检查 API 配额**：
   - 登录 API 提供商网站
   - 查看余额和使用情况

4. **检查代理设置**（如果使用代理）：
   ```json
   {
       "proxy": "http://127.0.0.1:7890"
   }
   ```

---

### Q3: 视频下载失败

**症状**：
- 提示 "视频下载失败"
- 提示 "404 Not Found"
- 下载进度卡住

**解决方案**：

1. **检查磁盘空间**：
   - 确保有足够的磁盘空间（至少 1GB）

2. **检查网络稳定性**：
   - 尝试重新下载
   - 使用更稳定的网络

3. **等待更长时间**：
   - 视频可能还在生成中
   - sora-2-pro 需要 20-30 分钟

4. **手动下载**：
   - 从 `video_url` 输出获取 URL
   - 在浏览器中打开并下载

---

### Q4: 生成的视频不符合预期

**症状**：
- 视频内容与提示词不符
- 视频质量不佳
- 运动不自然

**解决方案**：

1. **优化提示词**：
   - 使用更具体、详细的描述
   - 添加镜头运动描述
   - 添加氛围和情绪描述

2. **调整参数**：
   - 尝试不同的风格（cinematic / realistic）
   - 调整运动强度（0.3-0.7）
   - 尝试不同的种子值

3. **更换模型**：
   - 尝试 `sora-2-pro`（最高质量）
   - 尝试专用模型（landscape / portrait）

4. **多次生成**：
   - 使用随机种子（seed: -1）
   - 生成多个版本
   - 选择最佳结果

---

### Q5: Topaz 节点无法工作

**症状**：
- 提示 "Topaz Video AI 未安装"
- 提示 "无法找到 ffmpeg"

**解决方案**：

1. **安装 Topaz Video AI**：
   - 下载：[https://www.topazlabs.com/topaz-video-ai](https://www.topazlabs.com/topaz-video-ai)
   - 安装到默认路径

2. **检查安装路径**：
   - Windows: `C:\Program Files\Topaz Labs LLC\Topaz Video AI\`
   - macOS: `/Applications/Topaz Video AI.app/`

3. **手动指定路径**（如果安装在非默认路径）：
   - 修改 `topaz_video_ai_node.py`
   - 添加自定义路径

---

### Q6: 视频生成超时

**症状**：
- 提示 "视频生成超时"
- 等待很久仍未完成

**解决方案**：

1. **检查模型和时长**：
   - sora-2-pro + 25s 需要 20-30 分钟
   - 确认超时设置足够长

2. **查看控制台日志**：
   - 检查是否有错误信息
   - 查看轮询进度

3. **联系 API 提供商**：
   - 可能是服务器问题
   - 查看服务状态页面

---

### Q7: 水印节点不工作

**症状**：
- 水印没有显示
- 视频处理失败

**解决方案**：

1. **检查输入视频**：
   - 确保视频格式正确（MP4）
   - 确保视频路径有效

2. **检查字体**：
   - 确保系统有中文字体
   - 尝试使用英文水印

3. **调整参数**：
   - 增大字体大小
   - 增加透明度
   - 更换位置

---

## 📝 更新日志

### v1.4.0 (2025-10-18) ⭐ 最新

**新功能**：
- ✨ **Grok Imagine 视频生成节点**：支持 xAI 的 Grok Imagine 0.9 模型
  - 基于 Aurora 引擎的视频生成
  - 原生音频-视频同步
  - 6-15 秒时长控制
  - 多种质量和风格选项
  - 仅支持 Aabao API 提供商

**改进**：
- 🔧 添加 Grok Imagine 节点文档
- 🔧 更新节点列表和功能说明

### v1.3.0 (2025-10-18)

**新功能**：
- ✨ **HD 高清模式支持**：sora-2-pro 和 sora-2 模型支持 HD 参数（通过 `hd: true` 传递给 API）
- ✨ **多图参考视频生成节点**：支持最多 4 张图片作为参考生成视频
- ✨ 添加 HD 和 25s 互斥验证
- ✨ 添加 Comfly 多图 API 调用方法
- 🔧 **HD 参数实现优化**：统一使用 `hd` 参数而非模型名称切换，兼容所有镜像站

**改进**：
- 🔧 优化参数验证逻辑
- 🔧 改进日志输出（显示 HD 状态）
- 🔧 更新文档和使用说明
- 🔧 添加多图节点使用示例

**技术细节**：
- 📦 新增 `sora_multi_image2video.py` 节点
- 📦 新增 `_call_comfly_multi_image_api()` 方法
- 📦 支持 base64 图片数组传输
- 📦 支持 Comfly `/v2/videos/generations` 端点

---

### v1.2.0 (2025-10-17)

**新功能**：
- ✨ 添加 Aabao API 支持
- ✨ 支持 sora-2-pro 模型
- ✨ 支持 25 秒超长视频
- ✨ 动态轮询超时（根据模型和时长自动调整）
- ✨ 改进的进度显示（显示已等待/剩余时间）

**改进**：
- 🔧 优化 Topaz 节点视频输入处理
- 🔧 添加 `saved_path` 属性支持
- 🔧 改进错误提示和调试日志
- 🔧 更新文档和示例

**修复**：
- 🐛 修复 VideoFromFile 对象路径提取问题
- 🐛 修复 sora-2-pro 超时问题
- 🐛 修复空字符串路径处理

---

### v1.1.0 (2025-10-15)

**新功能**：
- ✨ 添加高级水印节点
- ✨ 支持动态动画效果
- ✨ 支持多位置模式
- ✨ 添加帧混合器节点

**改进**：
- 🔧 优化视频下载逻辑
- 🔧 添加多 URL fallback
- 🔧 改进错误处理

---

### v1.0.0 (2025-10-02)

**初始版本**：
- ✨ 支持文生视频
- ✨ 支持图生视频
- ✨ 支持多种宽高比和质量
- ✨ 支持风格和运动控制
- ✨ 完整的错误处理和进度显示
- ✨ Topaz 视频增强
- ✨ 基础水印功能

---

## 🤝 贡献

欢迎贡献代码、报告问题、提出建议！

### 如何贡献

1. **Fork 项目**
2. **创建分支** (`git checkout -b feature/AmazingFeature`)
3. **提交更改** (`git commit -m 'Add some AmazingFeature'`)
4. **推送分支** (`git push origin feature/AmazingFeature`)
5. **提交 Pull Request**

### 报告问题

如果遇到问题，请提交 Issue 并包含：
- 问题描述
- 复现步骤
- 错误日志
- 系统信息（OS、Python 版本、ComfyUI 版本）

---

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 📧 联系方式

- **GitHub Issues**: [提交问题](https://github.com/yourusername/ComfyUI_Sora/issues)
- **讨论区**: [GitHub Discussions](https://github.com/yourusername/ComfyUI_Sora/discussions)

---

## 🙏 致谢

感谢以下项目和服务：

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 强大的 AI 工作流平台
- [Topaz Video AI](https://www.topazlabs.com/) - 专业视频增强工具
- T8、Comfly、Aabao - API 服务提供商

---

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star ⭐！

---

## 💬 联系与支持

### 📱 添加微信

如有问题或需要技术支持，欢迎添加微信：

<div align="center">

<img src="assets/wechat_qrcode.png" alt="微信二维码" width="200"/>

**扫码添加微信**

</div>

---

### ☕ 支持项目

如果这个项目对你有帮助，欢迎请我喝杯咖啡 ☕

<div align="center">

<img src="assets/wechat_pay_qrcode.png" alt="微信收款二维码" width="200"/>

**微信赞赏**

</div>

你的支持是我持续更新的动力！🙏

---

<div align="center">

**享受创作！🎉**

Made with ❤️ by Ken-Chen

</div>

