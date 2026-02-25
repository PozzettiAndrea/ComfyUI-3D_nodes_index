# ComfyUI-Qwen3-TTS

[中文文档 (Chinese Documentation)](README_CN.md)

This is a **Qwen3-TTS** node for ComfyUI, supporting the Alibaba Qwen3-TTS series models for speech generation.

Features:
- **Custom Voice**: Use high-quality preset voices.
- **Voice Design**: Create brand new voices through text descriptions.
- **Voice Clone**: Clone voices from reference audio.

## 📦 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/Startgame/ComfyUI-kaola-Qwen-TTS.git
    ```
3.  Install dependencies:
    ```bash
    cd ComfyUI-kaola-Qwen-TTS
    pip install -r requirements.txt
    ```

## 📥 Model Download

The nodes support automatic model downloading (cached to the default HuggingFace directory), but manual downloading is recommended for better management.

Please place the models in the following directory structure:

```
ComfyUI/models/qwen3_tts/
```

If the directory does not exist, please create it manually.

Recommended Models:
- `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` (Recommended for Custom Voice)
- `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` (Recommended for Voice Design)
- `Qwen/Qwen3-TTS-12Hz-1.7B-Base` (Recommended for Voice Clone)

## 🧩 Nodes

### 1. Qwen3TTS Loader (Model Loader)
- **Function**: Loads model weights.
- **Note**: Ensure you select the model type matching your generation task!
    - For Custom Voice -> Load `CustomVoice` model.
    - For Voice Design -> Load `VoiceDesign` model.
    - For Voice Clone -> Load `Base` model.

### 2. Qwen3TTS Custom Voice
- **Parameters**:
    - `text`: The text to be spoken.
    - `speaker`: Select a preset speaker (e.g., Vivian, Ryan, etc.).
    - `instruct`: (Optional) Emotion/tone description, e.g., "Happy", "Sad".
    - `language`: Output language (Auto for automatic detection).

### 3. Qwen3TTS Voice Design
- **Parameters**:
    - `instruct`: **Required**. Describe the voice you want using natural language, e.g., "A deep, husky male voice".
    - `text`: The text to be spoken.

### 4. Qwen3TTS Voice Clone
- **Parameters**:
    - `ref_audio`: Reference audio. Can be connected via ComfyUI audio input or specified by local file path `ref_audio_path`.
    - `ref_text`: **Required**. The text content (transcript) of the reference audio. This significantly improves cloning similarity.
    - `text`: The text to be spoken.
    - `x_vector_only`: If checked, only voice print features are used (in this case `ref_text` can be omitted), but the effect is usually not as good as the cloning mode with text.

## ⚠️ Notes

1.  **VRAM Requirements**: The 1.7B model requires approximately 4GB+ VRAM. If VRAM is insufficient, try using the 0.6B version.
2.  **Flash Attention**: If you are using an NVIDIA GPU, it is recommended to install the `flash-attn` library for faster inference speeds.
3.  **Model Matching**: **Do NOT** connect the `Base` model to the `CustomVoice` node, or the `CustomVoice` model to the `VoiceDesign` node, as this will cause errors. Please ensure the Loader and Generator types are consistent.

## Examples
The `examples/` folder in the project root directory contains the following workflows:

1.  `examples/qwen3_tts_example_workflow.json`: Example with basic features.
2.  `examples/qwen3_tts_design_then_clone.json`: Advanced example showing how to design a voice first and then clone it.
3.  `examples/qwen3_tts_full_studio.json`: **Stage Manager Full Feature Example**, supporting multi-role dialogue, script parsing, and mixed orchestration of voice cloning and design.

You can directly drag the JSON files into the ComfyUI interface to load them.
