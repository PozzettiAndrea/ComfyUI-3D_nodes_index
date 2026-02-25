<!-- English -->
# ComfyUI-Gemini-Prompt-Studio

**Enhance your ComfyUI prompts with Google Gemini's dynamic “artist persona” system.**  
One node generates both T2I & I2V positive/negative conditioning in a single click.

---

<!-- 中文 -->
# ComfyUI Gemini 提示词工作室节点

**借助 Google Gemini 的「动态艺术人格」系统，一键生成文生图 + 图生视频的正反提示词与条件。**

---

<!-- English -->
## Features
- 5 built-in artist personas (film director, art historian, concept artist, novelist, creative director)
- Automatic quality modifiers & negative prompts
- Seed-controlled randomness for reproducible results
- Outputs 4 × conditioning + 4 × raw text + status string

---

<!-- 中文 -->
## 主要功能
- 内置 5 种艺术人格（电影导演、艺术史学家、概念设计师、文学家、广告创意总监）
- 自动附加画质增强与负面提示词
- 支持种子复现，结果可复现
- 同时输出 4 组条件 + 4 段文本 + 状态信息

---

<!-- English -->
## Installation

### ✅ Recommended: ComfyUI-Manager
1. Open **Manager** → **Install Custom Nodes**
2. Search `Gemini Prompt Studio`
3. Click **Install**

### 🖥️ Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DaLongZhuaZi/ComfyUI-Gemini-Prompt-Studio.git
cd ComfyUI-Gemini-Prompt-Studio
pip install -r requirements.txt
```
Restart ComfyUI.

---

<!-- 中文 -->
## 安装方式

### ✅ 推荐：ComfyUI-Manager
1. 打开 **管理器** → **安装自定义节点**
2. 搜索 `Gemini Prompt Studio`
3. 点击 **安装**

### 🖥️ 手动安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/DaLongZhuaZi/ComfyUI-Gemini-Prompt-Studio.git
cd ComfyUI-Gemini-Prompt-Studio
pip install -r requirements.txt
```
重启 ComfyUI 即可。

---

<!-- English -->
## Quick Start

### Step 1: Get API Key
Get a [Google AI Studio API key](https://aistudio.google.com/apikey) (free tier available)

### Step 2: Add Node to Workflow
1. Drag node `Gemini Prompt Studio (T2I+I2V) ✨` into your ComfyUI workflow
2. The node appears in category: **Magic Tools/Generation**

### Step 3: Configure Inputs
| Input | Type | Description | Example |
|-------|------|-------------|---------|
| **clip** | CLIP | Connect from your model's CLIP encoder | Required connection |
| **api_key** | STRING | Your Google AI Studio API key | `xxxxxxx...` |
| **model_name** | DROPDOWN | Gemini model selection | `gemini-2.5-flash` (recommended) |
| **keywords** | STRING | Core subject/scene description | `A beautiful girl in a white dress, sitting by a window` |
| **animation_effect** | STRING | How the image should animate (optional) | `She slowly turns her head to look at the camera, wind blows her hair` |
| **seed** | INT | Random seed for reproducible results | `42` |

### Step 4: Connect Outputs
The node provides **9 outputs**:

| Output | Type | Description | Connect To |
|--------|------|-------------|------------|
| **T2I_POSITIVE** | CONDITIONING | Enhanced positive prompt for text-to-image | KSampler → positive |
| **T2I_NEGATIVE** | CONDITIONING | Enhanced negative prompt for text-to-image | KSampler → negative |
| **I2V_POSITIVE** | CONDITIONING | Enhanced positive prompt for image-to-video | AnimateDiff → positive |
| **I2V_NEGATIVE** | CONDITIONING | Enhanced negative prompt for image-to-video | AnimateDiff → negative |
| **t2i_pos_text** | STRING | Raw positive text (for preview/debug) | Text Display Node |
| **t2i_neg_text** | STRING | Raw negative text (for preview/debug) | Text Display Node |
| **i2v_pos_text** | STRING | Raw I2V positive text (for preview/debug) | Text Display Node |
| **i2v_neg_text** | STRING | Raw I2V negative text (for preview/debug) | Text Display Node |
| **gemini_status** | STRING | API call status and error messages | Text Display Node |

### Step 5: Basic Workflow Connection
```
[Load Checkpoint] → CLIP → [Gemini Prompt Studio] → T2I_POSITIVE → [KSampler]
                                                  → T2I_NEGATIVE → [KSampler]
```

### Step 6: Advanced I2V Workflow
```
[Image] → [Gemini Prompt Studio] → I2V_POSITIVE → [AnimateDiff/SVD]
                                → I2V_NEGATIVE → [AnimateDiff/SVD]
```

---

<!-- 中文 -->
## 快速上手

### 步骤 1：获取 API 密钥
申请 [Google AI Studio API 密钥](https://aistudio.google.com/apikey)（有免费额度）

### 步骤 2：添加节点到工作流
1. 拖拽节点 `Gemini Prompt Studio (T2I+I2V) ✨` 到你的 ComfyUI 工作流中
2. 节点位于分类：**Magic Tools/Generation**

### 步骤 3：配置输入参数
| 输入参数 | 类型 | 说明 | 示例 |
|----------|------|------|------|
| **clip** | CLIP | 连接模型的 CLIP 编码器 | 必须连接 |
| **api_key** | STRING | 你的 Google AI Studio API 密钥 | `xxxxxxx...` |
| **model_name** | 下拉选择 | Gemini 模型选择 | `gemini-2.5-flash`（推荐） |
| **keywords** | STRING | 核心主题/场景描述 | `一个穿白裙的美丽女孩，坐在窗边` |
| **animation_effect** | STRING | 画面如何动起来（可选） | `她慢慢转头看向镜头，微风轻抚头发` |
| **seed** | INT | 随机种子，用于结果复现 | `42` |

### 步骤 4：连接输出
节点提供 **9 个输出**：

| 输出 | 类型 | 说明 | 连接到 |
|------|------|------|--------|
| **T2I_POSITIVE** | CONDITIONING | 增强的文生图正面提示词 | KSampler → positive |
| **T2I_NEGATIVE** | CONDITIONING | 增强的文生图负面提示词 | KSampler → negative |
| **I2V_POSITIVE** | CONDITIONING | 增强的图生视频正面提示词 | AnimateDiff → positive |
| **I2V_NEGATIVE** | CONDITIONING | 增强的图生视频负面提示词 | AnimateDiff → negative |
| **t2i_pos_text** | STRING | 原始正面文本（预览/调试用） | 文本显示节点 |
| **t2i_neg_text** | STRING | 原始负面文本（预览/调试用） | 文本显示节点 |
| **i2v_pos_text** | STRING | 原始 I2V 正面文本（预览/调试用） | 文本显示节点 |
| **i2v_neg_text** | STRING | 原始 I2V 负面文本（预览/调试用） | 文本显示节点 |
| **gemini_status** | STRING | API 调用状态和错误信息 | 文本显示节点 |

### 步骤 5：基础工作流连接
```
[加载检查点] → CLIP → [Gemini Prompt Studio] → T2I_POSITIVE → [KSampler]
                                            → T2I_NEGATIVE → [KSampler]
```

### 步骤 6：高级图生视频工作流
```
[图像] → [Gemini Prompt Studio] → I2V_POSITIVE → [AnimateDiff/SVD]
                               → I2V_NEGATIVE → [AnimateDiff/SVD]
```

---

<!-- English -->
## Example Workflow
Download [`examples/T2I+I2V.json`](examples/T2I%2BI2V.json) and [`examples/TexttoImage.json`](examples/TexttoImage.json) → drag into ComfyUI → Run.

---

<!-- 中文 -->
## 示例工作流
下载 [`examples/T2I+I2V.json`](examples/T2I%2BI2V.json) 和 [`examples/TexttoImage.json`](examples/TexttoImage.json) → 拖进 ComfyUI → 运行。

---

<!-- English -->
## Troubleshooting
| Problem | Solution |
|---------|----------|
| Node not visible | Make sure `__init__.py` is in the repo root |
| `ModuleNotFoundError: google.generativeai` | Re-run `pip install -r requirements.txt` |
| API returns empty | Check key quota & safety filters; lower temperature or tweak prompt |
| Other API issues | [Visit](https://ai.google.dev/gemini-api/docs/troubleshooting) |

---

<!-- 中文 -->
## 常见问题
| 问题 | 解决方法 |
|------|----------|
| 节点未显示 | 确认 `__init__.py` 位于仓库根目录 |
| 提示缺少 `google.generativeai` | 重新执行 `pip install -r requirements.txt` |
| API 返回为空 | 检查密钥额度及安全过滤，可调低 temperature 或修改提示词 |
| 其他 API 相关问题 | [访问](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=zh-cn) Google AI Studio 文档排查 |

---

<!-- English -->
## Contributing
Pull requests are welcome!  
Please run `python -m ruff check .` before submitting.

---

<!-- 中文 -->
## 参与贡献
欢迎提交 PR！  
提 PR 前请执行 `python -m ruff check .` 保证代码风格一致。

---

<!-- English -->
## License
MIT © 2025 DaLongzhuazi

---

<!-- 中文 -->
## 开源协议
MIT 许可证 © 2025 DaLongZhuaZi

---