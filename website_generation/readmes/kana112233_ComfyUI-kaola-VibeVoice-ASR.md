# ComfyUI VibeVoice ASR

A ComfyUI custom node for [Microsoft VibeVoice ASR](https://github.com/microsoft/VibeVoice).
This node allows you to perform high-quality, long-form speech recognition, speaker diarization, and timestamping directly within ComfyUI.

## features

*   **Long-form ASR**: Supports processing up to 60 minutes of audio in a single pass.
*   **SRT Export**: Automatically generates standard SRT subtitles with timestamps.
*   **Speaker Diarization**: Identifies different speakers (Speaker 0, Speaker 1, etc.).
*   **Context/Hotwords**: Improve accuracy for specific terms or names by providing context.
*   **Rich Output**: Provides both SRT strings and raw JSON data for advanced processing.
*   **Multi-Speaker TTS**: Generate speech with different voice characteristics for each speaker using reference audios.
*   **Voice Cloning**: Clone voice characteristics from reference audio samples.


## Model Download / 模型下载

### Supported Models / 支持的模型:

| Model | Type | Download |
|-------|------|----------|
| **VibeVoice-Realtime-0.5B** | Streaming TTS | [HuggingFace](https://huggingface.co/microsoft/VibeVoice-Realtime-0.5B) |
| **VibeVoice-1.5B** | High-Quality TTS | Contact Microsoft |

**1.5B Model Structure / 1.5B 模型结构:**
```
VibeVoice-1.5B/
    checkpoints/           # Model weights
        config.json
        model-00001-of-00003.safetensors
        ...
    Figures/tmp/           # Tokenizer files (required)
        tokenizer.json
        vocab.json
        ...
```

**Recommended Path / 推荐路径:**
`ComfyUI/models/vibevoice/`

## Installation

1.  **Clone the repository** into your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/kana112233/ComfyUI-kaola-VibeVoice-ASR.git
    cd ComfyUI-kaola-VibeVoice-ASR
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    > **Note**: This node requires `transformers>=4.51.3`. Please ensure your environment is updated.

3.  **Restart ComfyUI**.

## Usage

You can find the nodes under the `VibeVoice` category.

### Nodes

1.  **VibeVoice Model Loader**
    *   Loads the model.
    *   **model_name**: 
        *   **Auto Download**: Keep default `microsoft/VibeVoice-ASR`. It will download automatically to your HuggingFace cache folder on first run.
        *   **Manual**: You can download the model from [HuggingFace](https://huggingface.co/microsoft/VibeVoice-ASR), place it in a local folder (e.g., `ComfyUI/models/vibevoice`), and paste the **absolute path** to that folder here.
    *   **precision**: `bf16` (recommended for modern GPUs), `fp16`, or `fp32`.
    *   **device**: `auto` (recommended), `cuda`, `mps` (Mac), `cpu`.

## Model Download regarding
By default, the node uses `microsoft/VibeVoice-ASR` from HuggingFace.
If you have internet access, it will download automatically (~7B model) to your `~/.cache/huggingface` directory.

### Manual Download (Offline)
1. Download the model files from: [microsoft/VibeVoice-ASR](https://huggingface.co/microsoft/VibeVoice-ASR)
2. Place them in a folder, for example: `ComfyUI/models/vibevoice/VibeVoice-ASR`
3. In the `VibeVoiceLoader` node, replace `microsoft/VibeVoice-ASR` with the **absolute path** to your folder (e.g., `/content/ComfyUI/models/vibevoice/VibeVoice-ASR` or `D:\ComfyUI\models\vibevoice\VibeVoice-ASR`).

2.  **VibeVoice Transcribe**
    *   Performs the transcription.
    *   **audio**: Connect a standard AUDIO output (e.g., from `LoadAudio`).
    *   **context_info**: (Optional) Enter names, technical terms, or context to help the model recognize them correctly.
    *   **Outputs**:
        *   `srt_content`: Subtitle text.
        *   `json_content`: Detailed JSON data.

3.  **VibeVoice TTS Model Loader**
    *   Loads the TTS model (e.g., `microsoft/VibeVoice-1.5B`).
    *   Same parameters as ASR loader.

4.  **VibeVoice TTS Inference**
    *   Basic TTS with single reference audio (optional).
    *   **text**: Input text in format `"Speaker 0: Hello. Speaker 1: Hi."`
    *   **reference_audio**: (Optional) Single reference audio for voice cloning.

5.  **VibeVoice TTS Inference (Multi-Speaker)** ⭐ RECOMMENDED
    *   Multi-speaker TTS using **segment-by-segment generation** (generates each speaker separately, then concatenates).
    *   **text**: Input text in format `"Speaker 0: Hello. Speaker 1: Hi."`
    *   **speaker_0_audio**: (Optional) Reference audio for Speaker 0's voice.
    *   **speaker_1_audio**: (Optional) Reference audio for Speaker 1's voice.
    *   **speaker_2_audio**: (Optional) Reference audio for Speaker 2's voice.
    *   **speaker_3_audio**: (Optional) Reference audio for Speaker 3's voice.
    *   Each speaker will use the voice characteristics from their corresponding reference audio.
    *   If no reference audio is provided for a speaker, the model's default voice is used.
    *   **Method**: Generates each segment separately with correct reference audio, then concatenates with 100ms silence.
    *   **Status**: ✅ Verified working correctly


### Example Workflows
- **ASR**: `examples/vibevoice_workflow_example.json` - Speech recognition with transcription
- **TTS Basic**: `examples/vibevoice_tts_workflow.json` - Basic text-to-speech
- **TTS Multi-Speaker (Recommended)**: `examples/vibevoice_tts_multispeaker_workflow.json` - Multi-speaker TTS with segment-by-segment generation
- **Streaming**: `examples/vibevoice_streaming_workflow.json` - Real-time streaming inference

Drag and drop any workflow into ComfyUI to get started.

## Updating

This node contains the original VibeVoice repository as a submodule in `VibeVoice_src`. To update the core VibeVoice library:

```bash
cd custom_nodes/ComfyUI-kaola-VibeVoice-ASR/VibeVoice_src
git pull
```

## Credits

Based on [Microsoft VibeVoice](https://github.com/microsoft/VibeVoice).
