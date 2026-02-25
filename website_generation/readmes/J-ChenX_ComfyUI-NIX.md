# NIX ComfyUI Plugin

一个针对 ComfyUI 的插件集合，提供多种实用节点（批量路径加载、旋转裁剪、蒙版裁剪与合成、等比缩放、切片、字符串工具、任意类型切换、图像推理等）。

## 安装

- 手动克隆（推荐）
  1. 找到你的 ComfyUI/custom_nodes 目录。
  2. 在该目录执行：
     ```
     git clone https://github.com/J-ChenX/ComfyUI-NIX.git
     ```
  3. 重启 ComfyUI。

- ComfyUI Manager
  - 在 Manager 中通过仓库地址安装。本插件提供 `requirements.txt`，Manager 会自动安装依赖。

## 依赖与环境

- Python 3.10+
- ComfyUI（含 PyTorch 环境，插件不安装/不修改 PyTorch）
- 依赖见 `requirements.txt`：
  - numpy>=1.23
  - Pillow>=10.0.0
  - openai>=1.0.0（仅 NIX_ImageInference 需要）

> 注意：本插件不安装 torch（PyTorch）。请确保你的 ComfyUI 环境中已正确安装与显卡匹配的 PyTorch。

## 节点列表与简要说明

- NIX_PathLoading
  - 功能：从目录加载图片与蒙版，支持自然排序、起始下标、数量限制、通道提取为蒙版。
  - 关键参数：image_path、mask_path、channel（red/green/blue/yellow/purple/cyan/white）、load_quantity、start_index。
  - 输出：image（列表）、mask（列表）、filename（列表）、quantity_number（字符串）。

- NIX_RotateImage
  - 功能：对批量图像（及可选蒙版）进行旋转与水平翻转，自动扩充画布避免裁切。
  - 参数：angle、flip_horizontal、可选 masks。
  - 输出：images、masks。

- NIX_MaskCrop
  - 功能：以蒙版区域为核心进行裁剪与填充，支持比例匹配、扩展、模糊、两种填充策略（filling/move），并生成 pipe 数据用于后续合成。
  - 参数：width/height、expand、blur、filling_method、optional original_image/mask、binarize。
  - 输出：crop_image、crop_mask、pipe（PIPE_LINE）。

- NIX_ImageComposite
  - 功能：将采样图（sampled_image）按 pipe 的坐标与尺寸合成回原图，自动对齐与边界处理。
  - 输入：sampled_image、pipe、可选 original_image。
  - 输出：合成后的 IMAGE。

- NIX_RotateCrop
  - 功能：将旋转后的大画布中心裁成与原图同大小。
  - 输入：rotate_image、original_image。
  - 输出：IMAGE。

- NIX_ImageUpscaleProportionally
  - 功能：按最长/最短边或指定宽/高等比缩放，支持 8 的倍数。
  - 参数：side_length、side（Longest/Shortest/Width/Height）、eight_multiples。
  - 输出：IMAGE。

- NIX_SaveImage
  - 功能：保存图像到输出目录或自定义目录；image_format 为 png 时写入工作流元数据，为 jpg 时不写入。
  - 参数：images、filename_prefix、optional output_path、image_format（png/jpg）。
  - 输出：UI 预览信息。

- NIX_ImageTile
  - 功能：将一张图按网格切成多张瓦片，支持重叠。
  - 参数：rows、cols、overlap_x/overlap_y。
  - 输出：瓦片 IMAGE 以及瓦片尺寸与重叠信息。

- NIX_ImageInference
  - 功能：将图像编码为 base64 PNG，调用 OpenAI Chat Completions（v1 SDK）生成文本。
  - 参数：model_name、base_url、api_key、user_prompt。
  - 输出：prompt_word（STRING）。
  - 说明：
    - 默认 base_url 为第三方代理 `https://api.openai-proxy.org/v1`，如需官方服务请改为 `https://api.openai.com/v1`。
    - 需要安装 `openai>=1.0.0` 且提供有效的 `api_key`。
    - 网络请求可能失败时会返回错误信息。

- NIX_MaskNull
  - 功能：判断蒙版是否全为 0。
  - 输出：boolean。

- NIX_StringMatch
  - 功能：将整数按位数补零。
  - 参数：serial_number、figure。
  - 输出：text（STRING）。

- NIX_XYGridMapper
  - 功能：将索引映射为 X/Y 两个序列中的坐标与名称。
  - 参数：x_min/x_max/x_step、y_min/y_max/y_step、index。
  - 输出：x_value（FLOAT）、y_value（INT）、name（STRING）。

- NIX_StringMatcher
  - 功能：在最多 32 个字符串中精确匹配 judge_string，返回匹配到的最小编号 index，未匹配返回 -1。
  - 参数：string_1、string_2、judge_string、inputcount（2~32）、string_3 ... string_32（可选）。
  - 输出：index（INT）。

- NIX_SwitchAnything
  - 功能：按 index 选择返回任意类型的输入 anything_n。
  - 参数：anything_1、index（>=1），以及可选 anything_2 ... anything_N。
  - 输出：value（ANY_T，兼容 IO.ANY 或 "*"）。

## 注意事项与兼容性

- IO 类型兼容：
  - 代码会尝试导入 `comfy.comfy_types.node_typing.IO`。如不可用则降级为 `ANY_T = "*"`, 以保证节点在不同版本的 ComfyUI 中加载。
- 路径与通道：
  - NIX_PathLoading 支持自然排序与 1 基下标；`channel` 提取会做非负截断并归一化到 [0,1]。
- 图像/蒙版批次对齐：
  - 合成与裁剪节点会自动对齐 batch 数量；部分情况下会截断或重复最后一张以维持正确维度。
- OpenAI 推理：
  - 使用第三方代理地址可能带来合规与稳定性问题。推荐改为官方地址，并遵守 OpenAI 使用条款。

## 许可

本仓库建议使用 GPLv3 许可。

## 致谢

- ComfyUI 与其文档/社区。


