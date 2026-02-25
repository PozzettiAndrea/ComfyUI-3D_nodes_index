# ComfyUI-Owlv_Nodes 🦉

[English](#english) | [简体中文](#简体中文)

---

## English

### Overview
A collection of custom utility nodes for ComfyUI, providing practical mini-tools with multiple functions.

### Node List

#### Save Image (Dir) 🦉| OwlV
An enhanced version of ComfyUI's official save_image node with curated project subfolder support inside the output directory, now powered by a lightweight frontend companion script.

**Features:**
- ✅ Retains all functionality of the official save_image node
- ✅ Optional toggle to enable project subfolders under `ComfyUI/output`
- ✅ Supports custom multi-level subfolders when enabled
- ✅ Frontend-injected dropdown picker that lists existing output folders and stays in sync with manual input
- ✅ One-click refresh button to pull the latest folder list from `/owlv/list_subfolders`
- ✅ Automatically creates missing subfolders on save
- ✅ Keeps saves within the sandbox (prevents absolute paths / `..` traversal)
- ✅ Supports PNG metadata (prompt, workflow info)
- ✅ Automatic file name conflict resolution

**Input Parameters:**
- `images`: Images to save (required)
- `filename_prefix`: Filename prefix (default: "ComfyUI")
- `use_custom_subfolder`: Toggle to activate custom subfolder handling
- `subfolder`: Relative subfolder path when the toggle is on (e.g., `projectA/run01`)

**Usage:**
1. Add the node to your workflow and connect the image input
2. Leave `use_custom_subfolder` off to mirror the official save_image (saves in `ComfyUI/output`)
3. Turn `use_custom_subfolder` on to manage project folders
4. When enabled, either type a relative path in `subfolder` (e.g., `clientA/run05`) or use the injected dropdown picker
5. Click **Refresh Folders** if you add folders while ComfyUI is running; the picker will resync with valid paths
6. Invalid values (absolute paths or `..`) will raise an error to keep saves sandboxed

**Path Safety & Management:**
- Saves are always scoped to `ComfyUI/output`
- Nested folders are allowed (e.g., `team/project/run01`)
- The node sanitises input to block absolute paths or directory traversal
- Existing folders appear automatically in the picker for quick reuse and can be refreshed without reloading the workflow

#### KontextTextEncode 🦉| Owlv
An operator-focused Kontext workflow node that gathers image/edit descriptions, calls an LLM preset, and returns CLIP-ready conditioning plus the final text string.

**Features:**
- ✅ Accepts an `LLM` service connector along with a CLIP encoder
- ✅ Three multiline text fields (`Image 1`, `Image 2`, `Edit Instruction`) that accept manual input or upstream string connections
- ✅ Dropdown of default + user Kontext presets with inline **Add Custom Preset** / **Remove Custom Preset** buttons
- ✅ Always honors `Edit Instruction` when present; presets only fill gaps when no instruction is given
- ✅ Outputs CLIP conditioning (with pooled metadata) and the final generated prompt text

**Input Parameters (key fields):**
- `clip`: CLIP encoder used for tokenisation (required)
- `llm`: Connected LLM service (required)
- `kontext_preset`: Select a default/custom Kontext preset
- `image1_text`, `image2_text`, `edit_instruction`: Multiline fields that can be typed or wired in
- `seed`: Base seed for LLM sampling

**Outputs:**
- `conditioning`: CLIP conditioning enriched with pooled output and final text metadata
- `text`: The generated/confirmed prompt string

**Usage:**
1. Connect the LLM service and CLIP node; provide or wire the three description fields.
2. Choose a Kontext preset; manage custom presets via the inline buttons.
3. Set the seed as needed and run the node to obtain conditioning for downstream diffusion workflows while retaining the text output for auditing.

#### Add Custom Kontext Preset 🦉| OwlV
A utility node that writes user-defined Kontext presets (`user_kontext_presets.json`) for reuse inside KontextTextEncode.

#### Remove Custom Kontext Preset 🦉| OwlV
Allows removing any previously saved Kontext preset from the shared preset store (shared with KontextTextEncode).

#### Text Editor 🦉| OwlV
A manual review checkpoint that pauses the workflow until an operator confirms or edits the generated prompt text.

**Features:**
- ✅ Receives upstream string output (e.g., captions/prompt inversion results)
- ✅ Displays an editable multiline text area inside the node UI
- ✅ Provides an inline `Confirm` button; the workflow waits until confirmation before resuming
- ✅ Re-encodes the final text via CLIP and forwards both conditioning and raw text downstream

**Input Parameters:**
- `text`: Incoming text for review (required, multiline)

**Outputs:**
- `text`: Final confirmed text string

**Usage:**
1. Connect a text-producing node (e.g., Florence inverse prompt) to `Text Editor 🦉| OwlV`.
2. When the workflow reaches this node, it populates the editor with the received text and suspends execution.
3. Review and adjust the text in the built-in editor if needed.
4. Click **Confirm** to resume the workflow. The node returns the confirmed text for downstream usage.

### Installation

#### Method 1: Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "ComfyUI-Owlv_Nodes" or "OwlV"
3. Click Install
4. Restart ComfyUI

#### Method 2: Manual Installation
1. Navigate to your ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/OwlvChirotha/ComfyUI-Owlv_Nodes.git
```

3. Restart ComfyUI

4. Find the `Save Image (Dir) 🦉| OwlV` node in the `image` category

### Requirements
- ComfyUI base installation
- No additional dependencies required

### License
Please see the [LICENSE](LICENSE) file for details.

### Author
**OwlV** - [GitHub](https://github.com/OwlvChirotha)

### Support
If you encounter any issues or have suggestions, please open an issue on [GitHub Issues](https://github.com/OwlvChirotha/ComfyUI-Owlv_Nodes/issues).

---

## 简体中文

### 概述
ComfyUI自定义实用节点集合，提供多种实用的小工具和多功能节点。

### 节点列表

#### Save Image (Dir) 🦉| OwlV
在ComfyUI官方save_image节点的基础上，结合前端脚本提供位于output目录内的项目化子目录管理能力。

**功能特点：**
- ✅ 保留官方save_image的所有功能
- ✅ 通过开关可选启用 `ComfyUI/output` 下的项目子目录
- ✅ 启用后支持多层级自定义目录
- ✅ 前端自动注入的下拉选择器会列出已有目录并与手动输入保持同步
- ✅ 「🔄 Refresh Folders」按钮可随时调用 `/owlv/list_subfolders` 刷新目录列表
- ✅ 保存时自动创建缺失目录
- ✅ 严格限制在安全沙箱内（禁止绝对路径 / `..`）
- ✅ 支持PNG元数据（prompt、workflow信息）
- ✅ 自动处理文件名冲突

**输入参数：**
- `images`: 要保存的图像（必需）
- `filename_prefix`: 文件名前缀（默认："ComfyUI"）
- `use_custom_subfolder`: 是否启用自定义子目录
- `subfolder`: 开关开启时可填写的相对子目录（如 `projectA/run01`）

**使用说明：**
1. 将节点添加到工作流并连接图像输入
2. 关闭 `use_custom_subfolder` 时，行为与官方 save_image 一致，保存到 `ComfyUI/output`
3. 开启 `use_custom_subfolder` 后，可在 `subfolder` 中输入相对路径，或使用自动注入的下拉列表快速选择
4. 若在运行过程中新增目录，可点击节点上的 **🔄 Refresh Folders** 按钮刷新列表
5. 输入绝对路径或包含 `..` 会被拒绝，以确保输出安全

**路径安全与管理：**
- 所有文件始终保存于 `ComfyUI/output` 范围内
- 支持多级目录（如 `team/project/run01`）
- 节点会自动清洗输入，阻止绝对路径或目录穿越
- 现有目录会自动出现在下拉列表，可随时刷新而无需重启面板

#### KontextTextEncode 🦉| Owlv
结合图像/指令描述与 Kontext 预设调用 LLM，并输出 CLIP conditioning 与最终文本的新一代节点。

**功能特点：**
- ✅ 同时接入 LLM 服务连接器与 CLIP，形成完整的文本生成链路
- ✅ 提供三个可手输或接线的多行文本框（图像1、图像2、编辑指令）
- ✅ 节点内置新增/删除自定义预设按钮，实时更新预设下拉列表
- ✅ 若填写 `Edit Instruction`，将严格优先执行该指令，预设仅在缺省时提供补充
- ✅ 输出 CLIP conditioning（含文本与种子元数据）与最终确认文本

**输入要点：**
- `clip`：目标 CLIP 模型（必填）
- `llm`：连接的 LLM 服务（必填）

**输出：**
- `conditioning`：CLIP conditioning 增强，包含池化输出和最终文本元数据
- `text`：最终确认的文本字符串

**使用说明：**
1. 连接 LLM 服务与 CLIP，并填写/接入三段文本描述。
2. 通过节点按钮快速新增或删除自定义 Kontext 预设，选择合适的预设执行。
3. 设置需要的种子并运行节点，即可获得 conditioning 与文本输出。

#### Add Custom Kontext Preset 🦉| OwlV
A utility node that writes user-defined Kontext presets (`user_kontext_presets.json`) for reuse inside KontextTextEncode.

#### Remove Custom Kontext Preset 🦉| OwlV
Allows removing any previously saved Kontext preset from the shared preset store (shared with KontextTextEncode).

#### Text Editor 🦉| OwlV
A manual review checkpoint that pauses the workflow until an operator confirms or edits the generated prompt text.

**Features:**
- ✅ Receives upstream string output (e.g., captions/prompt inversion results)
- ✅ Displays an editable multiline text area inside the node UI
- ✅ Provides an inline `Confirm` button; the workflow waits until confirmation before resuming
- ✅ Re-encodes the final text via CLIP and forwards both conditioning and raw text downstream

**Input Parameters:**
- `text`: Incoming text for review (required, multiline)

**Outputs:**
- `text`: Final confirmed text string

**Usage:**
1. Connect a text-producing node (e.g., Florence inverse prompt) to `Text Editor 🦉| OwlV`.
2. When the workflow reaches this node, it populates the editor with the received text and suspends execution.
3. Review and adjust the text in the built-in editor if needed.
4. Click **Confirm** to resume the workflow. The node returns the confirmed text for downstream usage.
