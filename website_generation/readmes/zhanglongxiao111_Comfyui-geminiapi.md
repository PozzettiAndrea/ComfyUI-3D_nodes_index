# ComfyUI-ExternalAPI-Helpers 中文说明

> 原作者：**Aryan185**（GitHub）。在此基础上，我们补充了 Gemini / Replicate 节点改进与中文文档，方便国内用户快速上手。

本仓库提供一组 ComfyUI 自定义节点，可在本地工作流中直接调用以下服务：  
Gemini（Chat / Segmentation / TTS / Nano Banana / Imagen / Veo）、OpenAI GPT-Image-1、Replicate 上的 FLUX 系列、ElevenLabs 语音等。

---

## 近期更新（2025-10）

- **Nano Banana 节点**
  - 最大生成数量提升为 **15 张**，支持端口覆写与并发控制。
  - 自动对齐输出尺寸，失败时补齐占位图并输出详细日志。
  - 支持环境变量回落（`GEMINI_API_KEY`）与端口输入互斥逻辑。
- 文档改为中文，补充了安装步骤、依赖说明、常见问题以及原作者信息。

---

## 安装步骤

1. **复制节点包至 custom_nodes**
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/zhanglongxiao111/Comfyui-geminiapi.git
   ```
   或直接拷贝压缩包解压到 `custom_nodes` 目录。

2. **安装依赖（使用 ComfyUI 的 Python 环境）**
   ```bash
   cd Comfyui-geminiapi
   python -m pip install -r requirements.txt
   ```
   主要依赖：`google-generativeai`、`requests`、`nest-asyncio` 等。如遇缺包，可再次执行该命令。

3. **重启 ComfyUI**。节点会自动加载，位于 `ExternalAPI/*`、`Replicate/` 等分类中。

---

## API Key / 权限需求

| 节点 | 所需凭证 |
| --- | --- |
| FLUX Kontext Pro / Max | Replicate API Token |
| Gemini Chat / Segmentation / TTS / Nano Banana | Google AI Studio API Key (`GEMINI_API_KEY`) |
| Imagen 生成 | Google AI Studio API Key |
| Imagen Edit（Vertex）/ Veo 视频 | Google Cloud 项目、服务账号 JSON、Region |
| GPT Image Edit | OpenAI API Key |
| ElevenLabs TTS | ElevenLabs API Key |

- 节点面板允许直接输入 Key；为空时会尝试读取环境变量。  
- 可通过「API Key 连接」节点输出给其他节点复用。

---

## 节点概览

### FLUX Kontext Pro / Max
- **分类**：`ExternalAPI/Image/Edit`
- **功能**：经由 Replicate 调用 FLUX 模型，对输入图像做风格转换或深度重绘。
- **要点**：支持选择输出比例、格式、安全等级，默认推荐 `aspect_ratio = match_input_image`。

### Gemini Chat
- **分类**：`ExternalAPI/Text`
- **功能**：多模态对话，可读取图片、生成描述或提示词。支持 `thinking`（思维预算）和 `system_instruction`。

### Gemini Segmentation
- **分类**：`ExternalAPI/Image/Analysis`
- **功能**：按文本描述生成分割掩码，可用于后续抠图、局部编辑。

### GPT Image Edit
- **分类**：`ExternalAPI/Image/Edit`
- **功能**：OpenAI `gpt-image-1` 版的局部修复。需同时提供图片与遮罩。

### Google Imagen 系列
- **生成**：`ExternalAPI/Image/Generation`，文本转图像。
- **编辑（Vertex）**：`ExternalAPI/Image/Edit`，支持 inpaint/outpaint/背景替换；需配置 Google Cloud 项目、区域和服务账号。

### Nano Banana
- **分类**：`ExternalAPI/Image/Generation`
- **功能**：基于 `gemini-2.5-flash-image` 的多图参考生成。
- **特性**：
  - `image_count` 1~15；配合 `use_concurrency` 控制并发。
  - 自动对齐输出尺寸；失败时补齐黑图并记录日志 `[Nano Banana] Request failed: ...`。
  - 支持提示词 / API Key 面板输入或端口覆写，优先级清晰。

### Veo 文生视频（Vertex）
- **分类**：`ExternalAPI/Video`
- **功能**：文生短视频，输出帧序列，可接 ComfyUI 内的打包/转码节点。

### ElevenLabs TTS & Gemini TTS
- **分类**：`ExternalAPI/Audio`
- **功能**：文本转语音，分别调用 ElevenLabs 与 Gemini 服务，可调语速、音色、种子等。

---

## 常见问题与建议

1. **生成时间较长或请求失败**
   - Google API 会对并发请求限速。当日志出现 `[Nano Banana] Request failed` 时，可降低 `image_count` 或取消并发。
   - 建议在节点下游留意文本输出，失败时会返回详细错误信息与占位图。

2. **API Key 没被读取**
   - 确认已在 ComfyUI 启动终端中设置环境变量，如 `set GEMINI_API_KEY=xxxx`（Windows）。
   - 或者使用「API Key 连接」节点，将密钥从上游传入。

3. **依赖安装失败**
   - 请先升级 pip：`python -m pip install --upgrade pip`。
   - 若使用 ComfyUI 捆绑 Python，请在 `ComfyUI/python/python.exe` 下执行安装命令。

4. **日志位置**
   - ComfyUI 根目录的 `comfyui.log`、`comfyui.prev.log`。
   - 本仓库的 `报错信息/*.md` 文件会记录最近的报错与工作流快照。

---

## 贡献与授权

- 欢迎 PR / Issue 反馈改进建议；提交代码时请附上测试说明。
- 请在二次分发或引用时保留原作者（Aryan185）与本中文维护者的信息，并附上本 README 供其他用户正确安装。

---

## 鸣谢

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 提供自由灵活的节点系统。
- [Google](https://deepmind.google/technologies/gemini/)、[OpenAI](https://openai.com/)、[Black Forest Labs](https://www.blackforestlabs.ai/)、[ElevenLabs](https://elevenlabs.io/) 等厂商的模型与 API 服务。
- [Replicate](https://replicate.com/) 为第三方模型提供方便的调用通道。

如在使用过程中遇到问题，欢迎在仓库中提交 Issue 或讨论。祝你玩得开心！
