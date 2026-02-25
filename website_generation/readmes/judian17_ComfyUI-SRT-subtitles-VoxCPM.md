# ComfyUI-SRTVoxCPM

A set of ComfyUI nodes based on [VoxCPM](https://github.com/OpenBMB/VoxCPM) for generating and editing speech from SRT subtitle files.

## [中文说明](README-zh.md)

## Instructions

### Node Descriptions

#### 1. VoxCPM Loader
- **Function**: Loads the VoxCPM TTS model.
- **Parameters**:
  - `model_name`: Select the model to load. The default option, `openbmb/VoxCPM-0.5B (Auto-Download)`, will automatically download the model from Hugging Face.
  - `optimize`: Enables `torch.compile` for optimization. This feature may not work directly on Windows due to some bugs, but it is retained as it might be fixed by the community.

#### 2. VoxCPM Cache Builder
- **Function**: Creates a voiceprint (feature cache) for a specified speaker.
- **Parameters**:
  - `speaker_name`: Manually enter a unique identifier for the speaker (e.g., `speaker1`). This name must exactly match the speaker prefix used in the corresponding lines of the SRT file.
  - `prompt_audio`: Input the reference audio. You can use the built-in `Load Audio` node in ComfyUI or use the `Audio Trimmer` node to extract a specific segment from a longer audio file.
  - `prompt_text`: Enter the transcript of the reference audio.

#### 3. VoxCPM Cache Combiner (Chainable)
- **Function**: Combines the voice caches of multiple speakers to support multi-character dialogues.
- **How to use**:
  - This node can be chained together, with each node adding one speaker.
  - The `cache_group` input of the first `Cache Combiner` node should be left unconnected.
  - The `cache_group` input of subsequent nodes should be connected to the output of the previous `Cache Combiner` node.
  - The output of the final node connects to the `cache_group` input of the `SRT Processor` or `SRT Dubber` node.

#### 4. Audio Trimmer (by Timestamp)
- **Function**: Precisely trims an audio clip based on a timestamp.
- **Parameters**:
  - `timestamp`: Enter a timestamp in the format `00:00:06,500 --> 00:00:08,000`. The node will output only the audio within this time range.

#### 5. VoxCPM SRT Processor (from Scratch)
- **Function**: Generates a complete dialogue audio from scratch based on an SRT subtitle file and the voice caches.
- **SRT Format**:
  - **Multi-speaker mode**: Before each line of dialogue in the SRT file, use the format `SpeakerID + Space` to differentiate characters. For example:
    ```srt
    1
    00:00:00,500 --> 00:00:05,000
    speaker1 Hello world!

    2
    00:00:06,500 --> 00:00:08,000
    speaker2 Hello, world!
    ```
  - **Single-speaker mode**: When there is only one speaker, no prefix is needed before the subtitle text. For example:
    ```srt
    1
    00:00:00,500 --> 00:00:05,000
    Hello world!
    ```

#### 6. VoxCPM SRT Dubber (Replace Audio)
- **Function**: Replaces the speech for specific subtitle entries in an existing audio file. This can be used to correct pronunciation, change lines, or replace a character's voice entirely.
- **Parameters**:
  - `entries_to_replace`: Enter the **subtitle numbers** from the SRT file that you want to replace, separated by spaces (e.g., `1 3 5`). The node will generate new audio using the provided voice and the text from the corresponding subtitle number, then replace it at the correct time in the original audio.
  - **Note**: This refers to the subtitle **number**, not its order in the file. For example, in a non-standard subtitle file with numbers `1 2 3 5 6`, entering `4` will not match anything. If a number is duplicated (e.g., `1 2 3 4 4 5`), entering `4` will process both entries numbered `4`.

### Common Parameters

- **`normalize_text`**: Normalizes the text before synthesis. For example, when enabled, the number `50` will be read as "fifty" instead of "five zero".
- **`stretch_method`**: Method for time-stretching the audio to align the generated speech with the subtitle's duration.
  - `none`: No stretching is applied. If the generated audio is longer than the subtitle duration, it will overlap with the next line.
  - `librosa`: Uses the `librosa` library for time-stretching. The quality can be inconsistent; you can adjust `stretch_n_fft` and `stretch_hop_length` to mitigate artifacts like "metallic" sounds.
  - `pydub`: Uses the `pydub` library, which generally produces better results than `librosa`. This method requires **FFmpeg** to be installed and configured in your system's PATH.
- **`cfg_value`**: Defaults to `2.0`, which is a balanced setting. Higher values can sometimes improve results but may lead to instability.
- **`inference_timesteps`**: The number of inference steps. `10` steps can produce good results, but more steps can further improve audio quality.
- **`retry_threshold`**: The threshold for triggering a retry. The model compares the length ratio of the generated audio to the input text. If this ratio exceeds the threshold (meaning the audio is too long for the text), it's considered a failure and triggers a retry. For very slow speakers, you may need to increase this value (e.g., to `8.0` or `10.0`).
- **`retry_max_attempts`**: The maximum number of retries. When a generation fails, the model discards the result and tries again with a new random seed. Set to `0` to disable this feature.

## Model Download

- **Auto-Download (Recommended)**: In the `VoxCPM Loader` node, select `openbmb/VoxCPM-0.5B (Auto-Download)`. The model will be automatically downloaded and cached in ComfyUI's `models/TTS` folder.
- **Manual Download**: You can also download all model files from [VoxCPM-0.5B on Hugging Face](https://huggingface.co/openbmb/VoxCPM-0.5B) and place them in a subfolder within ComfyUI's `models/TTS` directory, for example: `\ComfyUI\models\TTS\VoxCPM-0.5B`.

## Example Workflows

### 1. Generate Audio from SRT (SRT to Speech)
- **Workflow File**: [SRT Processor Workflow](\workflows\SRT_VoxCPM.json)
- **Screenshot**:
  ![SRT Processor Workflow](assets/SRT_Processor.png)

### 2. Edit Audio with SRT (Dubbing)
- **Workflow File**: [SRT Dubber Workflow](\workflows\SRT_VoxCPM_edit.json)
- **Screenshot**:
  ![SRT Dubber Workflow](assets/SRT_dubber.png)

### 3. Transfer language with SRT
- **Workflow File**: [SRT Dubber Workflow](\workflows\SRT_VoxCPM_transfer.json)
- **Screenshot**:
  ![SRT Dubber Workflow](assets/SRT_Transfer_language.png)

### Example

[Mr.Ma.mp4](assets/Mr.Ma.mp4)

## Additional Notes

I have only a little knowledge of python code. This node is based on [VoxCPM](https://github.com/OpenBMB/VoxCPM), and the code was written with the assistance of Gemini 2.5 Pro.

The node still has some areas for improvement (like `torch.compile` compatibility and the model offloading mechanism). Due to limitations in my personal time and skills, I warmly welcome anyone in the community to freely use, modify, and improve this node, while respecting the [VoxCPM license](https://github.com/OpenBMB/VoxCPM). Your contributions are appreciated!
