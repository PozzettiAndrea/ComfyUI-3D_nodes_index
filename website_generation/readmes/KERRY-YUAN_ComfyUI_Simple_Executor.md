# ComfyUI_Simple_Executor
This node package includes nodes for automatically processing sampler settings based on model names and resizing images with specific constraints within ComfyUI. Subject to occasional updates.
本节点包包含在 ComfyUI 中根据模型名称自动处理采样器设置、按特定约束调整图像大小和一些其他节点。不定时更新中。

---
---

## Node List

*   **NodeAutoSampler**: Automatically sets sampler settings.
*   **NodeImageResize**: Resizes images, rounding dimensions up to multiples of 16x.
*   **NodeImagePre**: According to the image intelligently processed based on the short side, automatically generate parameters for adjusting size(16x), latent space, and magnification size(8x). 

## Node Descriptions

### 1. NodeAutoSampler (`NodeAutoSampler`)

*   **Description**: Sets sampler steps, CFG, and name based on the input `ckpt_name` and selected `mode` ("Auto", "If_include", "Else", "User"). Uses conditional logic based on keywords in `ckpt_name` or predefined settings.
*   **Category**: `custom`
*   **Key Inputs**:
    *   `ckpt_name` (STRING): Checkpoint name for logic.
    *   `mode` (COMBO): Operation mode.
    *   Optional settings for `if`, `else`, `user` conditions (steps, cfg, sampler).
*   **Outputs**: `steps` (INT), `cfg` (FLOAT), `sampler` (STRING), `text` (STRING summary).
*   **Usage**: Use 'Auto' mode with `if_include`='light' to apply specific settings (e.g., low steps/cfg) when 'light' is in the model name.
![image](https://github.com/KERRY-YUAN/ComfyUI_Simple_Executor/blob/main/Examples/NodeAutoSampler.png)

---
### 2. NodeImageResize (`NodeImageResize`)

*   **Description**: Resizes an image based on a target `shortside` length, maintaining aspect ratio. Final width and height are both rounded *up* (ceil) to the nearest multiple of 16.
*   **Category**: `Image/Transform`
*   **Inputs**:
    *   `image` (IMAGE): Image to resize.
    *   `shortside` (INT): Target length for the shorter side.
*   **Outputs**:
    *   `image_resize` (IMAGE): Resized image.
    *   `width` (INT): Final width (multiple of 16).
    *   `height` (INT): Final height (multiple of 16).
*   **Usage**: Resize 800x600 with `shortside`=768 results in 1024x768 output dimensions, as both are rounded up to the nearest 16x multiple.
![image](https://github.com/KERRY-YUAN/ComfyUI_Simple_Executor/blob/main/Examples/NodeResizeImage_16ceil.png)

---
### 3. NodeImagePre (`NodeImagePre`)

*   **Description**: Intelligently processes image workflows based on the target short side, automatically generating resized dimensions, empty latent space, and upscaled size parameters. Preset dimensions are rounded up to multiples of 16, and upscaled dimensions are rounded up to multiples of 8.
*   **Category**: `Image/Transform`
*   **Inputs**:
    *   `image` (IMAGE): Required input image.
    *   `mask` (MASK, optional): Optional input mask.
    *   `shortside` (INT, {"default": 800, "min": 560, "max": 9600, "step": 16}): Target short side length (multiple of 16).
    *   `batch` (INT, {"default": 1}): Batch size.
    *   `ups` (FLOAT, {"default": 1.00}): Upscaling factor.
*   **Outputs**:
    *   `image_resize` (IMAGE): Resized image.
    *   `mask_resize` (MASK): Resized mask.
    *   `empty_latent` (LATENT): Empty latent space (generated based on resized dimensions).
    *   `batch` (INT): Pass - through batch size.
    *   `width` (INT): Resized width (multiple of 16).
    *   `height` (INT): Resized height (multiple of 16).
	*   `ups` (FLOAT): Upscaling factor.
    *   `width_ups` (INT): Upscaled width (multiple of 8).
    *   `height_ups` (INT): Upscaled height (multiple of 8).
*   **Usage**: Inputting an 800x600 image with `shortside` = 768 and `ups` = 1.5 outputs: `image_resize`: 1024x768 image; `width_resize`/`height_resize`: 1024/768; `ups`=1.5; `width_ups`/`height_ups`: 1536/1152.
![image](https://github.com/KERRY-YUAN/ComfyUI_Simple_Executor/blob/main/Examples/NodeImagePre.png)

---

## Installation Steps

1.  Clone the repository into ComfyUI's `custom_nodes` directory:
    cd /path/to/comfyui/custom_nodes
    git clone https://github.com/KERRY-YUAN/ComfyUI_Simple_Executor.git
2.  Restart ComfyUI.

---
---

## 节点列表

*   **NodeAutoSampler**: 自动设置采样器参数。
*   **NodeResizeImage**: 调整图像大小，并将尺寸向上取整至16的倍数。
*   **NodeImagePre**: 根据目标短边智能处理图像，生成调整尺寸(16的倍数)、空潜在空间及放大参数(8的倍数)。

## 节点说明

### 1. NodeAutoSampler (`NodeAutoSampler`)

*   **描述**: 根据输入的 `ckpt_name` 中的关键字和选择的 `mode`（"Auto", "If_include", "Else", "User"）设置采样器步数、CFG 和名称。
*   **分类**: `custom`
*   **主要输入**:
    *   `ckpt_name` (STRING): 用于逻辑判断的检查点名称。
    *   `mode` (下拉框): 操作模式。
    *   用于 `if`, `else`, `user` 条件的可选设置 (步数, cfg, 采样器)。
*   **输出**: `steps` (INT), `cfg` (FLOAT), `sampler` (STRING), `text` (STRING 摘要)。
*   **使用**: 
    *   使用 'Auto'时按照对话框三组自动匹配：按照输入框包含'light'或'turbo'时应用对应设置（如低步数/CFG）；不包含时应用'Else'对应设置，
    *   使用'If_include',  "Else", "User"时将直接执行对应设置。

---
### 2. NodeImageResize (`NodeImageResize`)

*   **描述**: 根据目标 `shortside` 长度调整图像大小，保持宽高比。最终宽度和高度都将向上（ceil）取整至最接近的 16 的倍数。
*   **分类**: `Image/Transform`
*   **输入**:
    *   `image` (IMAGE): 待调整图像。
    *   `shortside` (INT): 目标短边长度。
*   **输出**:
    *   `image_resize` (IMAGE): 调整后的图像。
    *   `width` (INT): 最终宽度（16的倍数）。
    *   `height` (INT): 最终高度（16的倍数）。
*   **使用**: 使用 `shortside`=768 调整 800x600 图像，输出尺寸为 1024x768，因为宽高都向上取整至最接近的16倍数。

---
### 3. NodeImagePre (`NodeImagePre`)

*   **描述**: 根据目标短边智能处理图像，生成调整尺寸、空潜在空间及放大尺寸参数。预设尺寸向上取整为16的倍数，放大尺寸向上取整为8的倍数。
*   **分类**: `Image/Transform`
*   **输入**:
    *   `image` (IMAGE): 必选输入图像
    *   `mask` (MASK, 可选): 可选输入遮罩
    *   `shortside` (INT, {"default": 800, "min": 560, "max": 9600, "step": 16}): 目标短边长度（16的倍数）
    *   `batch` (INT, {"default": 1}): 批次数量
    *   `ups` (FLOAT, {"default": 1.00}): 尺寸放大倍数
*   **输出**:
    *   `image_resize` (IMAGE): 调整后的图像
    *   `mask_resize` (MASK): 调整后的遮罩
    *   `empty_latent` (LATENT): 空潜在空间（基于调整尺寸生成）
    *   `batch` (INT): 透传的批次数量
    *   `width` (INT) 调整后宽度（16的倍数）
    *   `height` (INT): 调整后高度（16的倍数）
	*   `ups` (FLOAT): 尺寸放大倍数
    *   `width_ups` (INT): 放大宽度（8的倍数）
    *   `height_ups` (INT): 放大高度（8的倍数）
*   **使用**: 输入800x600图像，`shortside`=768，`ups`=1.5；输出：`image_resize`: 1024x768图像；`width_resize`/`height_resize`: 1024/768； `ups`=1.5; `width_ups`/`height_ups`: 1536/1152

---

## 安装步骤

1.  将仓库克隆到 ComfyUI 的 `custom_nodes` 目录：
    cd /path/to/comfyui/custom_nodes
    git clone https://github.com/KERRY-YUAN/ComfyUI_Simple_Executor.git
2.  重启 ComfyUI。