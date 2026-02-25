# ComfyUI Base64 IO (Serialization Nodes)

[中文说明](#中文说明) | [English Description](#english-description)

---

<a name="english-description"></a>

## 🇬🇧 English Description

### Introduction

**ComfyUI Base64 IO** is a set of custom nodes designed to serialize ComfyUI internal data types (Latents, Conditioning, Images, etc.) into Base64 strings and deserialize them back.

This tool aims to solve the problem of **Distributed Inference** and **Data Caching** in complex workflows.

### 🚀 Why do you need this?

In standard ComfyUI workflows, Text Encoding, VAE, and U-Net (Denoise) usually run on the same machine. However, this is not always efficient:

1.  **Distributed Inference:** You can run light tasks (CLIP Text Encode, VAE Decode) on a CPU or a weaker GPU, and send the heavy U-Net tasks to a high-end GPU server via API.
2.  **External Caching:** You can serialize the result of "Negative Prompt" (Conditioning) once, store the Base64 string in your database, and inject it directly into future workflows. This skips the CLIP model execution entirely for repetitive prompts.
3.  **Cross-Workflow Data Transfer:** Easily move Latents or Conditioning from one unrelated workflow to another via the clipboard or API.

### 📦 Features

- **AnyToBase64:** Serializes any PyTorch object (Latent, Conditioning, Image Tensor) to a Base64 string.
  - _Smart Device Handling:_ Automatically moves tensors to CPU before serialization to prevent device mismatch errors when loading on a different machine.
- **Base64ToLatent:** Decodes Base64 to `LATENT`.
- **Base64ToConditioning:** Decodes Base64 to `CONDITIONING`.
- **Base64ToAny:** Universal decoder for other types (e.g., Image Tensors).

### 🛠️ Installation

1.  Navigate to your ComfyUI custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/lenML/ComfyUI_Base64_IO.git
    ```
3.  Restart ComfyUI.

### ⚠️ Security Warning

**IMPORTANT:** This node uses `torch.load` with `weights_only=False` to support complex data structures used in ComfyUI.

- **Do not load Base64 strings from untrusted sources.**
- Malicious Pickle data can execute arbitrary code on your machine.
- Only use this for internal API calls or trusted storage.

### 📖 Node Usage

#### 1. AnyToBase64

- **Input:** connect any output (Latent, Clip Conditioning, etc.).
- **Output:** Returns the Base64 string.
- **API Usage:** The node returns `{"ui": {"text": [b64_str]}, "result": (b64_str,)}`, making it easy to fetch via the ComfyUI API.

#### 2. Base64To[Type]

- **Input:** Paste the Base64 string into the text widget, or feed it from another string node.
- **Output:** Restores the original object (Latent, Conditioning, etc.).

---

<a name="中文说明"></a>

## 🇨🇳 中文说明

### 简介

**ComfyUI Base64 IO** 是一组用于将 ComfyUI 内部数据类型（如 Latents, Conditioning, Images 等）序列化为 Base64 字符串以及反序列化的自定义节点。

开发此插件的核心目的是为了解决 **分布式推理** 和 **中间层缓存** 的问题。

### 🚀 为什么需要这个？

在标准的 ComfyUI 工作流中，文本编码 (Text Encode)、VAE 和去噪 (U-Net) 通常在同一台机器上运行。但这并不总是最高效的：

1.  **分布式推理 (跨机器运行):** 你可以在一台配置较低的机器（或 CPU）上运行 CLIP Text Encode 和 VAE，将生成的 Conditioning 和 Latent 序列化后，通过 API 发送给拥有强大 GPU 的机器专门运行 U-Net (KSampler)。
2.  **中间层缓存 (缓存 Conditioning):** 对于通用的 "Negative Prompt"（负面提示词），你可以只运行一次 CLIP Encode，将结果序列化保存到数据库或文件中。下次生成时，直接反序列化注入到 KSampler，从而跳过 CLIP 模型的加载和计算。
3.  **灵活的数据传输:** 方便地将 Latent 或 Conditioning 数据通过 API 在不同的工作流或服务之间传递。

### 📦 功能特性

- **AnyToBase64:** 将任何 PyTorch 对象（Latent, Conditioning, Image Tensor）序列化为 Base64 字符串。
  - _智能设备管理:_ 保存时自动剥离设备信息（map to CPU），确保在另一台不同硬件配置的机器上也能正常加载。
- **Base64ToLatent:** 将 Base64 解码为 `LATENT` 格式。
- **Base64ToConditioning:** 将 Base64 解码为 `CONDITIONING` 格式。
- **Base64ToAny:** 通用解码器，用于其他类型（如图像 Tensor 等）。

### 🛠️ 安装方法

1.  进入 ComfyUI 的插件目录：
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  克隆本项目：
    ```bash
    git clone https://github.com/lenML/ComfyUI_Base64_IO.git
    ```
3.  重启 ComfyUI。

### ⚠️ 安全警告

**重要提示：** 本节点使用了 `torch.load` 且设置了 `weights_only=False`，这是为了支持 ComfyUI 复杂的内部数据结构。

- **请勿加载来自不可信来源的 Base64 字符串。**
- 恶意的 Pickle 数据可能会在你的机器上执行任意代码。
- 请仅在受信任的内部 API 或存储环境中使用。

### 📖 使用说明

#### 1. 序列化 (AnyToBase64)

- **输入:** 连接任何输出端口 (Latent, Clip Conditioning 等)。
- **输出:** 返回 Base64 字符串。
- **API 集成:** 该节点会返回 `{"ui": {"text": [b64_str]}, "result": (b64_str,)}`，方便外部 API 直接获取序列化后的数据。

#### 2. 反序列化 (Base64To...)

- **输入:** 在文本框中粘贴 Base64 字符串，或通过其他字符串节点输入。
- **输出:** 还原原始对象 (Latent, Conditioning 等)，直接连入 KSampler 或 VAE Decode。

---

**License**: MIT
