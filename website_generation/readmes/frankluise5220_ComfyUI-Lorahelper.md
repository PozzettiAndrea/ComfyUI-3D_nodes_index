# 🚀 ComfyUI-LoraHelper

一个专为 ComfyUI 打造的 **全能型 Prompt 引擎与 LoRA 炼丹助手**。

它不仅是一个简单的 GGUF 模型加载器，更内置了 **“专家级” Prompt 工程师逻辑**：
*   ✨ **灵魂反推 (Soul-Deep Captioning)**：超越简单的看图说话，精准捕捉画面氛围与意境，转化为 Flux/SD 可用的高质量 Prompt。
*   🚀 **智能扩写 (Intelligent Expansion)**：让简单的“女孩在海边”瞬间变成包含光影、材质、构图的 300 字大师级描述。
*   💾 **一键炼丹 (One-Click Dataset)**：自动整理 LoRA 训练素材，图片、标签、工作流元数据一键打包，拖入即复现。

**无需昂贵显卡**，本地 GGUF 模型即可驱动这一切，让你的工作流彻底自动化。

An **All-in-One Prompt Engine & LoRA Training Assistant** for ComfyUI.

More than just a GGUF loader, it embeds **Expert-Level Prompt Engineering logic**:
*   ✨ **Soul-Deep Captioning**: Goes beyond object detection to capture atmospheric nuance and artistic essence, converting images into production-ready Flux/SD prompts.
*   🚀 **Intelligent Expansion**: Instantly transforms simple inputs like "girl at beach" into 300-word masterworks rich in lighting, texture, and composition.
*   💾 **One-Click Dataset Prep**: Automates LoRA training data organization—images, tags, and workflow metadata saved in one click. Drag-and-drop to reproduce.

**No expensive GPU required.** Power your automated workflow with local GGUF models.

---

[English Version](#-english-version) | [中文说明](#-中文说明)

<a name="-english-version"></a>
## 🌏 English Version

### 📦 Installation
1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/yourusername/ComfyUI-Lorahelper.git
   ```
2. Install the required dependencies:
   ```bash
   cd ComfyUI-Lorahelper
   pip install -r requirements.txt
   ```
   *Note: This project requires `llama-cpp-python` for GGUF model support. For vision capabilities, ensure your installation supports CLIP/MMProj.*

### 🌐 Language Switching
The plugin supports one-click language switching (English/Chinese) via the ComfyUI menu. No restart required.

### 🧩 Node Overview

#### 1. LH_GGUFLoader (GGUF Model Loader)
*   **Function**: Loads `.gguf` format LLM models.
*   **Supported Models**: Extensive support for mainstream VLM/LLM GGUF models, including **Qwen2.5-VL / Qwen2-VL**, **Llama 3.2 Vision**, **Yi-VL**, **Llava 1.5/1.6**, and other GGUF-compatible models.
*   **Path**: Place your models in `ComfyUI/models/llm/`.
*   **Features**:
    *   **GGUF Model**: Select your main LLM.
    *   **CLIP Model**: (Optional) Load a CLIP/MMProj model to enable vision capabilities for image analysis.
    *   **GPU Layers**: Supports auto-offloading VRAM.
    *   **n_ctx**: Maximum context window size (default: 8192).

#### 2. LH_AIChat (DeepBlue Architecture)
The core intelligence node. [View Logic Flowchart](./Logic_Flowchart.md)
*   **Inputs**:
    *   `model`: The loaded LLM.
    *   `image` (Optional): Connecting an image automatically triggers **Implicit Vision Mode**.
    *   `user_material`: Input material/text (Ignored in Vision Mode).
    *   `instruction`: Executive instructions for the AI.
    *   `max_tokens`: Max generation length.
    *   `temperature`: Creativity (higher = more random).
    *   `repetition_penalty`: Penalty for repeating text.
    *   `force_chinese`: (Boolean) Appends a Chinese translation directive to the system prompt, ensuring detailed Chinese output.
    *   `seed`: Random seed for reproducibility.
    *   `release_vram`: Auto-release VRAM after generation.
*   **Outputs**:
    *   `prompt`: Core prompt output (description).
    *   `tags`: Extracted Danbooru tags (if enabled).
    *   `filename`: Extracted filename (if enabled).
    *   `raw_output`: Full raw AI conversation output (for debugging/instruction tuning).
*   **Vision Mode (Implicit)**:
    *   Triggered automatically when an image is connected.
    *   **Auto-Instruction**: If `instruction` is left default/empty, it uses a built-in **JoyCaption-style Uncensored** prompt for detailed image captioning.
    *   **Customizable**: You can override the built-in behavior by providing your own `instruction`.
*   **Modes (Text-only)**:
    *   **Enhance_Prompt**: Creatively expands on user inputs.
    *   **Debug_Chat**: Analyzes prompts based on instructions.

#### 3. LH_History_Monitor (History Viewer)
*   **Function**: Manages conversation history and context.
*   **Features**:
    *   **Visual History**: Displays the last 5 rounds in clear "Round X" cards.
    *   **Auto-Resize**: Automatically adjusts size to fit content.
    *   **Context Loop**: Outputs formatted context to be copied into `user_material` for multi-turn debugging.

#### 5. LH_AllInOne_Saver (Dataset Saver)
*   **Function**: One-click solution for saving training data, prompts, tags, and workflows.
*   **Features**:
    *   **One-Click Save**: Simultaneously saves Images, Caption text, Log files, and ComfyUI Workflow metadata.
    *   **Workflow Embedding**: Supports saving the full ComfyUI workflow into the PNG, allowing drag-and-drop to reproduce the generation.
    *   **Flexible Naming**: Supports custom prefixes, filename overrides, and auto-incrementing.
*   **Inputs**:
    *   `images`: Input images to save.
    *   `folder_path`: Subfolder path in output directory (default: "LoRA_Train_Data").
    *   `filename_prefix`: Prefix for filenames (default: "Anran").
    *   `trigger_word`: Trigger word added to the start of caption files (default: "ChenAnran").
    *   `save_workflow`: Toggle to save ComfyUI workflow metadata in PNG.
    *   `gen_prompt`: (Optional) Connect full description text to save in `_log.txt`.
    *   `lora_tags`: (Optional) Connect tags to save in `.txt`.
    *   `filename_final`: (Optional) Override specific filename (will be combined with prefix).
*   **Outputs**:
    *   **Image**: `.png` with metadata (Workflow).
    *   **Tags**: `.txt` file with format `trigger_word, tags`.
    *   **Log**: `_log.txt` with the full raw AI response.
*   **Path**: Default saves to `ComfyUI/output/LoRA_Train_Data/`.

#### 6. LH_MultiTextSelector (Dynamic Prompt Generator)
*   **Function**: A powerful text selector with support for Dynamic Prompts syntax and Batch Processing.
*   **Features**:
    *   **Batch Mode**: Paste multiple lines of text into `batch_text`. The node can output them as a list, running one workflow for each line (Sequential).
    *   **Mode**: `Random` (select one randomly) or `Sequential` (cycle through list/batch).
    *   **Seed Control**: Ensure reproducible results.

#### 7. LH_SuperText
*   **Function**: **Bidirectional Text Node (Input/Output)**. Supports disconnected editing and rapid image generation.
*   **Features**:
    *   **Dual Role**: Acts as both an upstream text aggregator/pass-through and a direct downstream text source.
    *   **Editable Mode**: Automatically enables editing when disconnected, bypassed, or when the upstream node is disabled. Supports instant editing and locking of current content.
    *   **Quick Generation**: Perfect for "Gacha" style prompting. Generate a prompt, then temporarily bypass/disable the upstream workflow to "lock" the text in SuperText. Use this fixed text as the prompt for image generation, avoiding constant re-generation from the upstream LLM.

#### 8. LH_LoraLoader (Keyword Lora Loader)
*   **Function**: Automatically loads specific LoRAs based on keywords found in the prompt.
*   **Features**:
    *   **Keyword Trigger**: Monitors `prompt_text` input. Loads LoRA if any keyword in `trigger_keywords` (comma-separated) is found.
    *   **Smart Bypass**: If not triggered, passes through model and CLIP unchanged, consuming no extra resources.
    *   **Preset Strength**: Independently sets model and CLIP strength for this conditional LoRA.
    *   **Status Feedback**: Provides a dedicated text output port to indicate which keyword triggered the load (useful for saving in Log files).

#### 9. LH_AutoRatio (Smart Resolution Calculator)
*   **Function**: Calculates the optimal width and height based on an input image's aspect ratio or a default setting.
*   **Features**:
    *   **Smart Matching**: Analyzes the input image's aspect ratio and automatically snaps to the nearest standard ratio (16:9, 3:2, 1:1, 2:3, 9:16).
    *   **Max Edge Control**: You define the longest side (e.g., 1024), and it calculates the short side to maintain the ratio.
    *   **Safe Dimensions**: Ensures outputs are always multiples of 8 (preventing VAE errors).
    *   **Fallback**: Uses `default_ratio` if no image is connected.

### 🎨 Global Feature: Dynamic Prompts Engine
*   **Supported Nodes**: `LH_AIChat`, `LH_MultiTextSelector`, `LH_SuperText` (via Utils).
*   **Advanced Syntax**:
    *   **Recursive Wildcards**: `__colors__` - Reads from `.txt` files (supports recursive lookup in `ComfyUI/wildcards` or plugin's `wildcards` folder).
    *   **Deep Nesting**: `{A|{B|C}}` - Supports complex nested choices up to 20 levels.
    *   **Weighted Choices**: `{80::Red|20::Blue}` - Robust probability control.
    *   **Full Unicode**: Perfect support for **Chinese/Japanese** characters in wildcards and content.
    *   **Auto-Cleaning**: Automatically removes invisible characters (Zero-Width Space) that often cause parsing errors.

## 💡 Best Practice

It is recommended to use this tool with **[Dynamic Prompts (DP)](https://github.com/adieyal/comfyui-dynamicprompts)**:
1.  **DP Randomization**: Use DP nodes to generate random combinations (e.g., `{white dress|red cheongsam}, {black hair|blonde hair}`).
2.  **AI Refinement**: Feed the random output from DP into this plugin as `user_material`.
3.  **Deep Expansion**: This plugin will automatically add lighting, composition, and scene details based on the random attributes.

**Core Advantage**: Combines the "breadth" of randomness with the "depth" of AI to quickly generate high-quality, diverse LoRA training datasets.

---

<a name="-中文说明"></a>
## 🇨🇳 中文说明

### 📦 安装指南
1. 将本项目克隆到 `ComfyUI/custom_nodes/` 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/yourusername/ComfyUI-Lorahelper.git
   ```
2. 安装必要的依赖库：
   ```bash
   cd ComfyUI-Lorahelper
   pip install -r requirements.txt
   ```
   *注意：本项目依赖 `llama-cpp-python` 来加载 GGUF 模型。如需使用视觉反推功能，请确保安装版本支持 CLIP/MMProj。*

### 🌐 中英文切换
插件菜单支持一键切换语言（中/英），无需重启 ComfyUI。

### 🧩 节点详解

#### 1. LH_GGUFLoader (模型加载器)
*   **功能**: 加载 `.gguf` 格式的大语言模型。
*   **路径**: 请将模型文件放入 `ComfyUI/models/llm/` 目录。
*   **特性**:
    *   **GGUF Model**: 选择主 LLM 模型。
    *   **CLIP Model**: (可选) 加载 CLIP/MMProj 模型以启用视觉能力。
    *   **GPU Layers**: 支持自动显存分流 (Offload)。
    *   **n_ctx**: 最大上下文窗口大小 (默认: 8192)。

#### 2. LH_AIChat (DeepBlue Architecture)
核心智能节点。[查看逻辑流程图](./Logic_Flowchart.md)
*   **输入参数**:
    *   `image` (可选): 连接图片后自动触发 **隐形反推模式**。
    *   `user_material`: 用户输入的素材/文本 (反推模式下忽略)。
    *   `instruction`: 给 AI 的执行指令。
    *   `max_tokens`: 最大生成长度。
    *   `temperature`: 温度 (创造力，越高越随机)。
    *   `repetition_penalty`: 重复惩罚系数。
    *   `force_chinese`: (布尔值) 强制开启中文模式，在系统指令中追加翻译要求，确保输出详尽的中文内容。
    *   `seed`: 随机种子 (控制结果一致性)。
    *   `release_vram`: 生成后自动释放显存。
*   **输出端口**:
    *   `prompt`: 核心功能，提示词输出 (description).
    *   `tags`: 从提示词中提取的danbooru标签 。
    *   `filename`: 提取的文件名。
    *   `raw_output`: AI对话全过程内容输出（方便debug、调整指令）。
*   **隐形反推模式**:
    *   **自动触发**: 只要连接图片，无需输入任何用户指令，即刻生效。
    *   **智能指令**: 若 `instruction` 保持默认或留空，将使用内置的 **JoyCaption 同款无审查** 强力反推指令，生成极详尽的视觉描述。
    *   **用户指令**: 您也可以输入自定义 `instruction` 来覆盖内置行为。
*   **运行模式**:
    *   **Enhance_Prompt**: 对用户素材（包括image和文本）进行创意扩写。
    *   **Enhance_Beauty (Film-level)**: **新增!** 专为女性人像设计的高阶无审查扩写模式，兼顾解剖学细节与胶片质感。
    *   **Debug_Chat**: 根据指令分析素材，输出思考过程。
*   **视觉预设**:
    *   **Vision_Beauty (Film-level)**: **新增!** 法医级女性人像分析，在无审查与艺术美感之间取得平衡。

#### 3. LH_History_Monitor (历史看板)
*   **功能**: 维护并显示最近 5 轮的对话历史。
*   **特性**:
    *   **可视化显示**: 以 "Round X" 卡片形式清晰展示对话内容，自动调整窗口大小。
    *   **上下文循环**: 输出格式化后的 `context` 文本，可复制到 `user_material` 实现多轮对话调试。

#### 5. LH_AllInOne_Saver (数据集保存器)
*   **功能**: 一“键”保存 LoRA 训练所需的所有文件（图片、Prompt、Tags、工作流）。
    *   **灵活命名**: 支持自定义前缀、覆盖文件名和自动递增。
*   **输入参数**:
    *   `folder_path`: 保存路径子文件夹 (默认: "LoRA_Train_Data")。
    *   `filename_prefix`: 文件名前缀 (默认: "Anran").
    *   `trigger_word`: 触发词，自动添加在 caption 文件的最开头 (默认: "ChenAnran").
    *   `save_workflow`: 开关，决定是否将 ComfyUI 工作流元数据写入图片 (支持拖入复现)。
    *   `gen_prompt`: (可选) 连接完整描述文本，保存到 `_log.txt`。
    *   `lora_tags`: (可选) 连接标签文本，保存到 `.txt` (位于触发词之后)。
    *   `filename_final`: (可选) 覆盖具体文件名 (会自动拼接前缀)。
*   **路径**: 默认保存在 `output/LoRA_Train_Data/`，支持自定义子文件夹。

#### 6. LH_MultiTextSelector (多行提示词选择器)
*   **功能**: 支持动态语法 (Dynamic Prompts) 和批量处理的多功能文本选择器。
*   **特性**:
    *   **批量模式 (Batch)**: 在 `batch_text` 中粘贴多行文本，节点可将其作为列表输出，实现“一行文本运行一次工作流”的批量生成。
    *   **模式切换**: `Random` (随机选择) 或 `Sequential` (顺序循环/批量列表)。
    *   **Seed 控制**: 通过种子固定随机结果，方便复现。

#### 7. LH_SuperText
*   **功能**: **双向文本节点（输入/输出）**，支持断链编辑与快速出图。
*   **特性**:
    *   **双重角色**: 既能作为上游文本的聚合/透传节点，也能作为下游的直接文本输出节点。
    *   **可编辑模式**: 当断开、绕开或关闭上游节点时，自动进入可编辑状态，支持在节点内即时编辑与锁定当前内容。
    *   **快速出图**: 抽卡获得提示词后，可暂时屏蔽上游工作流，直接使用 SuperText 的文本作为 Prompt 投喂至下游生成节点，避免上游反复改写带来的干扰。

#### 8. LH_LoraLoader (关键词 Lora 加载器)
*   **功能**: 与手动填写触发词不同，该节点根据检查提示词中的关键词，自动判断是否加载指定的 LoRA。
*   **特性**:
    *   **关键词触发**: 监控 `prompt_text` 输入。如果包含 `trigger_keywords` (逗号分隔) 中的任意词，则加载 LoRA。
    *   **智能直通**: 如果未触发，则原样输出模型和 CLIP，不消耗额外资源。
    *   **预设强度**: 为该条件 LoRA 单独设置模型和 CLIP 的强度。
    *   **状态反馈**: 提供专门的文本输出端口，告知是哪个关键词触发了加载，可以输出文本用来保存在Log文件中。

#### 9. LH_AutoRatio (智能分辨率计算器)
*   **功能**: 根据输入图片的宽高比或默认设置，自动计算最佳的宽和高。
*   **特性**:
    *   **智能匹配**: 分析输入图片的原始比例，自动吸附到最近的标准比例 (16:9, 3:2, 1:1, 2:3, 9:16)。
    *   **长边控制**: 您只需指定最长边 (如 1024)，它会自动计算短边长度以维持比例。
    *   **安全尺寸**: 确保输出尺寸永远是 8 的倍数 (防止 VAE 报错)。
    *   **默认回退**: 如果未连接图片，则使用 `default_ratio` 作为默认比例。

### 🎨 全局特性：动态提示词引擎 (Dynamic Prompts Engine)
*   **支持节点**: `LH_AIChat`, `LH_MultiTextSelector` 等所有核心节点。
*   **进阶语法**:
    *   **递归通配符**: `__colors__` - 读取 `.txt` 文件 (支持递归查找 `ComfyUI/wildcards` 或本插件内置目录)。
    *   **深度嵌套**: `{A|{B|C}}` - 支持高达 20 层嵌套选择。
    *   **权重抽卡**: `{80::红|20::蓝}` - 鲁棒的概率控制。
    *   **全语种支持**: 完美支持 **中文/日文** 通配符文件名和内容。
    *   **自动清洗**: 自动移除导致报错的隐形字符 (Zero-Width Space)，让复制粘贴更省心。

---

## 💡 使用建议 (Best Practice)

建议配合 **[Dynamic Prompts (DP)](https://github.com/adieyal/comfyui-dynamicprompts)** 插件使用：
1.  **DP 抽签**: 使用 DP 节点生成随机组合（如 `{白色长裙|红色旗袍}, {黑发|金发}`）。
2.  **AI 润色**: 将 DP 的随机输出作为 `user_material` 输入给本插件。
3.  **深度扩写**: 本插件会基于随机属性，自动补充灯光、构图及场景细节。

**核心优势**: 结合了随机性的“广度”和 AI 的“深度”，能够快速生成高质量、多样化的 LoRA 训练数据集。

---

## 📅 Update Log

### v1.2.3 (2025-02-12)
*   **[New]** **LH_SuperText**: Added `force_text` input port. Supports external input while keeping the text widget editable (auto-fallback logic).
*   **[Improvement]** **LH_SuperText**: The text widget is now automatically disabled (read-only) when `force_text` is connected, preventing accidental edits.
*   **[Fix]** **LH_SuperText**: Changed `force_text` input type to wildcard (`*`) to support connecting any type of text node.
*   **[Improvement]** **LH_SuperText**: Added `seed` control and `IS_CHANGED` signal to ensure correct random updates for wildcards.
*   **[Fix]** **Dynamic Prompts**: Fixed path resolution issues for wildcard files and optimized random seed handling (seed=-1 is now true random).

### v1.2.1 (2025-02-09)
*   **[CRITICAL]** Fixed "Access Violation" crashes by implementing metadata-based GGUF architecture detection. Now safely identifies Qwen/Llava/Yi models to load the correct vision handler.
*   **[CRITICAL]** Fixed crash on older `llama-cpp-python` versions lacking `Q8_0` support (added silent fallback).
*   **[FIX]** **Saver Node**: Fixed long filename errors. Filenames >100 chars or with illegal chars are now auto-replaced with `Error_Timestamp` markers instead of failing.
*   **[OPTIMIZATION]** Removed aggressive `gc.collect()` calls during inference loops to reduce micro-stutters.

### v1.2.2 更新日志
*   **[新增]** **LH_SuperText**: 新增 `force_text` 输入端口。支持接入外部文本，断开时自动回退到文本框内容，实现连线/手动编辑的无缝切换。
*   **[改进]** **LH_SuperText**: 增加 `seed` 种子控制和 `IS_CHANGED` 信号，确保通配符 (Wildcards) 每次运行都能正确随机更新。
*   **[修复]** **Dynamic Prompts**: 修复了通配符文件的路径搜索问题，并优化了随机种子逻辑（seed=-1 现在是真随机）。

### v1.2.1 更新日志
*   **[严重修复]** 修复�?"Access Violation" 崩溃问题。新�?Metadata 元数据检测机制，精准识别 Qwen/Llava/Yi 模型架构，防止因加载错误的视觉处理器导致崩溃�?*   **[严重修复]** 修复了旧�?`llama-cpp-python` 不支�?`Q8_0` 量化导致的报错（增加自动回退机制）�?*   **[修复]** **Saver 节点**：修复长文件名保存失败问题。超�?00字符或含非法字符的文件名将自动替换为 `Error` 标记，确保图片数据不丢失�?*   **[优化]** 移除了推理循环中不必要的强制内存回收 (`gc.collect`)，大幅减少卡顿，提升批处理速度�?
