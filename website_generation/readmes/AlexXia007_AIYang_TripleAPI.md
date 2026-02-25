# ComfyUI 三合一 AI 图像生成节点

这个项目为 ComfyUI 提供了两个强大的自定义节点，集成了三个主流的中文AI图像生成平台：**即梦AI**、**火山引擎豆包**和**NanoBanana**。支持文生图和图生图功能。

## 功能特点

- 🎨 **三平台集成**：同时支持即梦AI、火山引擎豆包、NanoBanana三个平台
- 🔄 **双模式支持**：文生图 (Text-to-Image) 和 图生图 (Image-to-Image)
- ⚡ **并行生成**：可同时调用多个平台生成图片，提高效率
- 🎯 **智能轮询**：自动等待图片生成完成，无需手动查询
- 🛡️ **容错处理**：单个平台失败不影响其他平台正常工作
- 📊 **详细状态**：实时显示每个平台的生成状态和错误信息
- 🔗 **URL输出**：提供每个API生成的图片URL，便于后续处理和分享
- 🔄 **重试机制**：支持API调用失败时自动重试，提高成功率
- ⏱️ **超时控制**：可配置请求和轮询超时时间，避免长时间等待

## 系统要求

- Python 3.8 或更高版本
- ComfyUI 已安装并运行
- 至少 4GB 可用内存

## 依赖说明

本项目需要以下 Python 包：

- **Pillow** (>=9.0.0): 用于图像处理
- **numpy** (>=1.21.0): 用于数值计算和数组操作
- **torch** (>=1.12.0): PyTorch 深度学习框架（ComfyUI 通常已包含）

> **注意**: ComfyUI 通常已经包含了 `torch` 和 `numpy`，如果您的 ComfyUI 环境已配置好，可能只需要安装 `Pillow`。

## 安装方法

### 方法一：使用 Git 克隆（推荐）

1. 将此仓库克隆到 ComfyUI 的 `custom_nodes` 目录：
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/AlexXia007/AIYang_TripleAPI.git
```

2. 进入项目目录并安装依赖：
```bash
cd AIYang_comfyui_tripapi
pip install -r requirements.txt
```

3. 重启 ComfyUI

### 方法二：手动安装

1. 下载项目 ZIP 文件并解压到 `ComfyUI/custom_nodes` 目录

2. 在项目目录下打开终端，执行：
```bash
pip install -r requirements.txt
```

3. 重启 ComfyUI

### 验证安装

重启 ComfyUI 后，在节点菜单中应该能看到：
- `TripleAPIGenerate` (三合一文生图节点)
- `TripleAPIImg2Img` (三合一图生图节点)

如果节点未出现，请检查：
- 依赖是否安装成功
- ComfyUI 控制台是否有错误信息
- 项目是否在正确的 `custom_nodes` 目录下

## 节点说明

### 1. TripleAPIGenerate (三合一文生图节点)

用于根据文字描述生成图片。

#### 输入参数详解

**基础参数**
- **`prompt`** (STRING): 
  - **描述**: 图片生成的主要提示词
  - **填写**: 详细描述你想要生成的图片内容，如"一只可爱的小猫坐在花园里，阳光明媚，高清摄影风格"
  - **建议**: 越详细越好，包含风格、场景、光线、质量等描述

- **`negative_prompt`** (STRING): 
  - **描述**: 负面提示词，指定不想要的元素
  - **填写**: 如"模糊，低质量，变形，多余的手指，nsfw"
  - **可选**: 可以留空，但建议填写以提高图片质量

- **`image_urls_input`** (STRING): 
  - **描述**: 参考图片的URL地址（多个URL用换行分隔）
  - **填写**: 如"https://example.com/image1.jpg"
  - **用途**: 提供风格参考或构图参考
  - **可选**: 纯文生图时可留空

**平台开关**
- **`enable_hidream`** (BOOLEAN): 是否启用即梦AI (默认: True)
- **`enable_volcengine`** (BOOLEAN): 是否启用火山引擎豆包 (默认: True)  
- **`enable_nanobanana`** (BOOLEAN): 是否启用NanoBanana (默认: True)

**API配置**
- **`hidream_req_key`** (STRING): 即梦AI的API密钥
- **`volcengine_api_key`** (STRING): 火山引擎的API密钥
- **`nanobanana_api_key`** (STRING): NanoBanana的API密钥

**生成参数**
- **`image_width`** (INT): 生成图片宽度 (默认: 1024, 范围: 256-2048)
- **`image_height`** (INT): 生成图片高度 (默认: 1024, 范围: 256-2048)
- **`num_images`** (INT): 生成图片数量 (默认: 1, 范围: 1-4)

**高级设置**
- **`request_timeout`** (INT): 单次请求超时时间，秒 (默认: 240)
- **`poll_interval`** (INT): 轮询间隔时间，秒 (默认: 3)
- **`poll_timeout`** (INT): 总轮询超时时间，秒 (默认: 240)
- **`max_retries`** (INT): 最大重试次数 (默认: 3, 范围: 1-5)
- **`white_image_width`** (INT): 失败时白色占位图宽度 (默认: 512)
- **`white_image_height`** (INT): 失败时白色占位图高度 (默认: 512)

**特定平台参数**
- **`nanobanana_model`** (STRING): NanoBanana使用的模型 (默认: "flux")
- **`nanobanana_style`** (STRING): NanoBanana的艺术风格 (默认: "默认")

#### 输出说明

**图片输出**
- **`nanobanana_image`** (IMAGE): NanoBanana生成的图片张量
- **`doubao_image`** (IMAGE): 豆包生成的图片张量  
- **`hidream_image`** (IMAGE): 即梦AI生成的图片张量

**任务信息**
- **`nanobanana_task_id`** (STRING): NanoBanana任务ID
- **`hidream_task_id`** (STRING): 即梦AI任务ID

**API响应**
- **`nanobanana_response`** (STRING): NanoBanana的完整API响应 (JSON格式)
- **`doubao_response`** (STRING): 豆包的完整API响应 (JSON格式)
- **`hidream_response`** (STRING): 即梦AI的完整API响应 (JSON格式)

**状态信息**
- **`status_info`** (STRING): 详细的状态信息，包含每个平台的执行结果

**图片URL输出** ⭐ **新功能**
- **`nanobanana_image_url`** (STRING): NanoBanana生成的图片URL
- **`doubao_image_url`** (STRING): 豆包生成的图片URL
- **`hidream_image_url`** (STRING): 即梦AI生成的图片URL

**URL值说明**：
- **成功时**: 返回实际的图片URL地址
- **API错误时**: 返回 `"api_error"`
- **API禁用时**: 返回 `"api_disabled"`

### 2. TripleAPIImg2Img (三合一图生图节点)

用于基于输入图片进行图像转换和编辑。

#### 输入参数详解

**图片输入**
- **`input_image`** (IMAGE): 
  - **描述**: 输入的基础图片张量
  - **连接**: 从图片加载节点或其他图像处理节点连接
  - **必填**: 图生图必须提供基础图片

**基础参数**
- **`prompt`** (STRING): 
  - **描述**: 对图片进行修改的描述
  - **填写**: 如"将这个人的头发改为金色，背景改为海滩"
  - **建议**: 描述你想要的变化，而不是重复描述原图内容

- **`negative_prompt`** (STRING): 
  - **描述**: 不想要的效果
  - **填写**: 如"模糊，扭曲，多余的肢体"

**其他参数**: 与文生图节点相同

#### 输出说明

输出与文生图节点完全相同。

## URL输出功能详解

### 什么是URL输出？

URL输出功能为每个API生成的图片提供直接的URL链接，让您可以：

- **直接访问图片**：无需下载到本地即可查看生成的图片
- **分享图片**：将URL分享给他人查看
- **集成到其他系统**：将URL传递给其他应用或服务
- **调试和监控**：快速检查API是否成功生成了图片

### URL值含义

| 值 | 含义 | 说明 |
|---|---|---|
| `https://example.com/image.jpg` | 成功 | 返回实际的图片URL地址 |
| `api_error` | API错误 | API调用失败或响应格式错误 |
| `api_disabled` | API禁用 | 该API被禁用或未提供密钥 |

### 使用场景

1. **质量对比**：同时获取三个平台的图片URL，对比生成效果
2. **自动化流程**：将URL传递给后续的图片处理节点
3. **错误诊断**：通过URL值快速判断哪个API出现问题
4. **批量处理**：收集多个生成的图片URL进行批量操作

## 使用示例

### 文生图工作流

1. 添加 `TripleAPIGenerate` 节点
2. 填写提示词: "一只橘色的小猫在阳光下睡觉，温暖的午后，高清摄影"
3. 填写负面提示词: "模糊，低质量，变形"
4. 配置API密钥
5. 设置图片尺寸 (如 1024x1024)
6. 运行生成

**获取图片URL**：
- 连接 `nanobanana_image_url` 输出到文本显示节点，查看NanoBanana生成的图片URL
- 连接 `doubao_image_url` 输出到文本显示节点，查看豆包生成的图片URL
- 连接 `hidream_image_url` 输出到文本显示节点，查看即梦AI生成的图片URL

### 图生图工作流

1. 添加图片加载节点，加载基础图片
2. 添加 `TripleAPIImg2Img` 节点
3. 将图片加载节点的输出连接到 `input_image`
4. 填写修改提示词: "将背景改为星空，保持人物不变"
5. 配置其他参数
6. 运行生成

### API密钥获取

**即梦AI**
1. 访问 [即梦AI官网](https://jimeng.jianying.com/)
2. 注册账号并获取API密钥

**火山引擎豆包**
1. 访问 [火山引擎控制台](https://console.volcengine.com/)
2. 开通豆包大模型服务
3. 创建API密钥

**NanoBanana**
1. 访问 [NanoBanana官网](https://nanobanana.ai/)
2. 注册账号并获取API访问权限
