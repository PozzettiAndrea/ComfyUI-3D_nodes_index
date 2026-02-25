# ComfyUI Audio Batch & Utility Nodes &#x0001F3A7;&#x0001F39B;&#xFE0F;


![Audio Batch](https://raw.githubusercontent.com/set-soft/ComfyUI-AudioBatch/seconohe/assets/banner_1280.jpg)


This repository provides a set of custom nodes for ComfyUI focused on audio batching and common audio processing tasks like
channel conversion and resampling. These nodes are designed to help manage and prepare audio data within your ComfyUI
workflows, especially when dealing with multiple audio inputs or outputs.


## &#x2699;&#xFE0F; Main features

&#x2705; No extra heavy dependencies, we use the same modules as ComfyUI and a small module with ComfyUI helpers

&#x2705; All operations accepts batches (multiple audio in the same noodle)

&#x2705; Batch: create and separate

&#x2705; Conversion: channels and sample rate

&#x2705; Manipulation: cut, concatenate, blend, join/split stereo, de/normalization

&#x2705; QoL: audio information, download audio, musical note to freq, signal generator

&#x2705; Warnings and errors visible in the browser, configurable debug information in the console


## &#x0001F4DC; Table of Contents

- &#x0001F680; [Installation](#-installation)
- &#x0001F4E6; [Dependencies](#-dependencies)
- &#x0001F5BC;&#xFE0F; [Examples](#&#xFE0F;-examples)
- &#x2728; [Nodes](#-nodes)
  - [1. Batch Audios](#1-batch-audios)
  - [2. Select Audio from Batch](#2-select-audio-from-batch)
  - [3. Audio Channel Converter](#3-audio-channel-converter)
  - [4. Audio Force Channels](#4-audio-force-channels)
  - [5. Audio Resampler](#5-audio-resampler)
  - [6. Audio Channel Conv and Resampler](#6-audio-channel-conv-and-resampler)
  - [7. Audio Information](#7-audio-information)
  - [8. Audio Cut](#8-audio-cut)
  - [9. Audio Concatenate](#9-audio-concatenate)
  - [10. Audio Blend](#10-audio-blend)
  - [11. Audio Test Signal Generator](#11-audio-test-signal-generator)
  - [12. Audio Musical Note](#12-audio-musical-note)
  - [13. Audio Join 2 Channels](#13-audio-join-2-channels)
  - [14. Audio Split 2 Channels](#14-audio-split-2-channels)
  - [15. Audio Normalize (Peak)](#15-audio-normalize-peak)
  - [16. Audio Apply Batched Gain](#16-audio-apply-batched-gain)
  - [17. Audio Download and Load](#17-audio-download-and-load)
- &#x0001F4DD; [Usage Notes](#-usage-notes)
- &#x0001F6E0;&#xFE0F; [Future Improvements / TODO](#&#xFE0F;-future-improvements--todo)
- &#x0001F4DC; [Project History](#-project-history)
- &#x2696;&#xFE0F; [License](#&#xFE0F;-license)
- &#x0001F64F; [Attributions](#-attributions)

## &#x2728; Nodes

### 1. Batch Audios
   - **Display Name:** `Batch Audios`
   - **Internal Name:** `SET_AudioBatch`
   - **Category:** `audio/batch`
   - **Description:** Takes two audio inputs (which can themselves be batches) and combines them into a single, larger audio batch. The node handles differences in sample rate, channel count, and length between the two inputs to produce a unified batch.
   - **Inputs:**
     - `audio1` (AUDIO): The first audio input. Can be a single audio item or a batch.
     - `audio2` (AUDIO): The second audio input. Can be a single audio item or a batch.
   - **Output:**
     - `audio_batch` (AUDIO): A single audio object where the waveforms from `audio1` and `audio2` are concatenated along the batch dimension.
   - **Behavior Details:**
     - **Sample Rate:** All audio in the output batch will be resampled to match the sample rate of `audio1`.
     - **Channels:**
       - If both inputs are mono, the output batch will be mono.
       - If one input is mono and the other is stereo, the mono input will be converted to "fake stereo" (by duplicating its channel), and the output batch will be stereo.
       - If both inputs are stereo, the output batch will be stereo.
       - For more complex multi-channel inputs, it defaults to the maximum channel count of the two inputs with a warning, as advanced downmixing is not performed.
     - **Length (Samples):** All audio clips in the output batch will be padded with silence at the end to match the length of the longest clip (after any resampling).
     - **Input Batch Handling:** If `audio1` has B1 items and `audio2` has B2 items, the output `audio_batch` will contain B1 + B2 items.

### 2. Select Audio from Batch
   - **Display Name:** `Select Audio from Batch`
   - **Internal Name:** `SET_SelectAudioFromBatch`
   - **Category:** `audio/batch`
   - **Description:** Selects a single audio stream from an input audio batch based on a specified index. Provides options for handling out-of-range indices.
   - **Inputs:**
     - `audio_batch` (AUDIO): An audio batch (e.g., from the "Batch Audios" node).
     - `index` (INT): The 0-based index of the audio stream to select from the batch.
     - `behavior_out_of_range` (COMBO): What to do if the `index` is out of range:
       - `silence_original_length` (default): Output silent audio with the same channel count and duration as items in the original batch.
       - `silence_fixed_length`: Output silent audio with a duration specified by `silence_duration_seconds`.
       - `error`: Raise an error (which will halt the workflow and display an error in ComfyUI).
     - `silence_duration_seconds` (FLOAT): The duration of the silent audio if `behavior_out_of_range` is set to `silence_fixed_length`.
   - **Output:**
     - `selected_audio` (AUDIO): The selected audio stream (as a batch of 1) or silent audio if the index was out of range (and behavior was not "error").

### 3. Audio Channel Converter
   - **Display Name:** `Audio Channel Converter`
   - **Internal Name:** `SET_AudioChannelConverter`
   - **Category:** `audio/conversion`
   - **Description:** Converts the channel layout of an input audio (e.g., mono to stereo, stereo to mono). Handles batches.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
     - `channel_conversion` (COMBO): The desired channel conversion strategy:
       - `keep` (default): No changes are made to the channel count. Logs a warning if input has more than 2 channels.
       - `stereo_to_mono`: Converts stereo (or multi-channel) audio to mono by averaging all input channels. If already mono, no change.
       - `mono_to_stereo`: Converts mono audio to "fake stereo" by duplicating the mono channel. If already stereo, no change. For multi-channel (>2) inputs, it takes the first channel and duplicates it to create stereo.
       - `force_mono`: Always converts the input to mono by averaging all channels, regardless of the original channel count.
       - `force_stereo`:
         - If input is mono, converts to "fake stereo".
         - If input is stereo, no change.
         - If input has more than 2 channels, it takes the first channel and duplicates it to create stereo.
     - `downmix_method` (COMBO): How to convert to mono.
       - `average`: Simple average ((L+R)/2). Can reduce volume.
       - `standard_gain` (default): Sums channels with -3dB gain (0.707). Better preserves perceived loudness.
       - `spectral`: Averages frequency magnitudes to prevent phase cancellation.
     - `n_fft` (INT, optional): FFT size for spectral downmixing. Higher values give better frequency resolution but worse time resolution.
     - `hop_length` (INT, optional): Hop length for STFT. Typically n_fft / 4. Controls time resolution.
   - **Output:**
     - `audio_out` (AUDIO): The audio with the converted channel layout. The batch size and sample rate are preserved.

### 4. Audio Force Channels
   - **Display Name:** `Audio Force Channels`
   - **Internal Name:** `SET_AudioForceChannels`
   - **Category:** `audio/conversion`
   - **Description:** Forces the number of channels. 0 means keep same.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
     - `channels` (INT): The desired channel number of channels. This is equivalent to **Audio Channel Converter**:
       - `0`: `keep`
       - `1`: `force_mono`
       - `2`: `force_stereo`
     - `downmix_method` (COMBO): How to convert to mono.
       - `average`: Simple average ((L+R)/2). Can reduce volume.
       - `standard_gain` (default): Sums channels with -3dB gain (0.707). Better preserves perceived loudness.
       - `spectral`: Averages frequency magnitudes to prevent phase cancellation.
     - `n_fft` (INT, optional): FFT size for spectral downmixing. Higher values give better frequency resolution but worse time resolution.
     - `hop_length` (INT, optional): Hop length for STFT. Typically n_fft / 4. Controls time resolution.
   - **Output:**
     - `audio` (AUDIO): The audio with the converted channel layout. The batch size and sample rate are preserved.

### 5. Audio Resampler
   - **Display Name:** `Audio Resampler`
   - **Internal Name:** `SET_AudioResampler`
   - **Category:** `audio/conversion`
   - **Description:** Resamples the input audio to a specified target sample rate using `torchaudio.transforms.Resample`. Handles batches.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
     - `target_sample_rate` (INT): The desired sample rate in Hz (e.g., 44100, 48000, 16000). If set to 0 or if it matches the original sample rate, resampling is skipped.
   - **Output:**
     - `audio_out` (AUDIO): The resampled audio. The batch size and channel count are preserved.

### 6. Audio Channel Conv and Resampler
   - **Display Name:** `Audio Channel Conv and Resampler`
   - **Internal Name:** `SET_AudioChannelConvResampler`
   - **Category:** `audio/conversion`
   - **Description:** A convenience node that combines channel conversion and resampling into a single step.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
     - `channel_conversion` (COMBO): Same options as the "Audio Channel Converter" node.
     - `target_sample_rate` (INT): Same options as the "Audio Resampler" node.
     - `downmix_method` (COMBO): How to convert to mono.
       - `average`: Simple average ((L+R)/2). Can reduce volume.
       - `standard_gain` (default): Sums channels with -3dB gain (0.707). Better preserves perceived loudness.
       - `spectral`: Averages frequency magnitudes to prevent phase cancellation.
     - `n_fft` (INT, optional): FFT size for spectral downmixing. Higher values give better frequency resolution but worse time resolution.
     - `hop_length` (INT, optional): Hop length for STFT. Typically n_fft / 4. Controls time resolution.
   - **Output:**
     - `audio_out` (AUDIO): The audio after both channel conversion and resampling have been applied.

### 7. Audio Information
   - **Display Name:** `Audio Information`
   - **Internal Name:** `SET_AudioInfo`
   - **Category:** `audio/conversion`
   - **Description:** Shows information about the audio.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
   - **Output:**
     - `audio_bypass` (AUDIO): The audio from the input, here to make easier its use.
     - `batch_size` (INT): Size of the audio batch, how many sounds are in the batch.
     - `channels` (INT): Number of audio channels (1 mono, 2 stereo)
     - `num_samples` (INT): How many samples contains the audio. Duratio [s] = `num_samples` / `sample_rate`
     - `sample_rate` (INT): Sampling frequency, how many samples per second.
     - `mean` (TORCH_TENSOR): Mean value for each waveform in the batch.
     - `std` (TORCH_TENSOR): Standard deviation for each waveform in the batch.
     - `peak` (TORCH_TENSOR): Peak value (absolute) for each waveform in the batch.

### 8. Audio Cut
   - **Display Name:** `Audio Cut`
   - **Internal Name:** `SET_AudioCut`
   - **Category:** `audio/manipulation`
   - **Description:** Cuts a portion of the input audio.
   - **Inputs:**
     - `audio` (AUDIO): The input audio.
     - `start_time` (STRING): Starting time. Can be in the HH:MM:SS.ss format, or be just a float. I.e. 1:30 is 1 minute 30 seconds.
     - `end_time` (STRING): Ending time. Can be in the HH:MM:SS.ss format, or be just a float. I.e. 90.5 is 1 minute 30 seconds and 500 ms.
   - **Output:**
     - `audio_out` (AUDIO): The selected portion of the audio.

### 9. Audio Concatenate
   - **Display Name:** `Audio Concatenate`
   - **Internal Name:** `SET_AudioConcatenate`
   - **Category:** `audio/manipulation`
   - **Description:** Joins two audio clips end-to-end in time. This is the counterpart to the "Audio Cut" node.
   - **Inputs:**
     - `audio1` (AUDIO): The first audio clip to appear in the sequence.
     - `audio2` (AUDIO): The second audio clip to be appended to the end of the first.
   - **Output:**
     - `audio_out` (AUDIO): A single audio clip containing `audio1` followed immediately by `audio2`.
   - **Behavior Details:**
     - **Alignment:** Before concatenation, the two audio inputs are aligned to have the same sample rate and channel count, using the same logic as the "Batch Audios" node.
     - **Batch Handling:** If the inputs have different batch sizes, the last item of the shorter batch is repeated to ensure the output batch size matches the larger of the two inputs.

### 10. Audio Blend
   - **Display Name:** `Audio Blend`
   - **Internal Name:** `SET_AudioBlend`
   - **Category:** `audio/manipulation`
   - **Description:** Blends two audio inputs by applying gain and adding them. Supports batches. It can be used to amplify just one audio (or batch)
   - **Inputs:**
     - `audio1` (AUDIO): The first audio input (batch supported).
     - `audio2` (AUDIO): The second audio input (batch supported). Is optional.
     - `gain1` (FLOAT): Volume gain for the first audio. Can be negative to subtract.
     - `gain2` (FLOAT): Volume gain for the second audio. Can be negative to subtract.
   - **Output:**
     - `audio_out` (AUDIO): The blended audio.

### 11. Audio Test Signal Generator
   - **Display Name:** `Audio Test Signal Generator`
   - **Internal Name:** `SET_AudioTestSignalGenerator`
   - **Category:** `audio/generation`
   - **Description:** Generates various standard audio test signals. This node is perfect for creating predictable, clean audio to test or debug other audio processing nodes in your workflow without needing external files.
   - **Inputs:**
     - `waveform_type` (COMBO): The type of signal to generate.
       - **Periodic:** `sine`, `square`, `sawtooth`, `triangle`.
       - **Sweep:** `sweep` (a linear frequency chirp from `frequency` to `frequency_end`).
       - **Noise:** `white_noise`, `pink_noise`, `brownian_noise`.
       - **Special:** `impulse` (a single sample at full amplitude), `silence` (a signal of all zeros, to which a DC offset can be added).
     - `frequency` (FLOAT): The fundamental frequency in Hz for periodic waveforms, or the starting frequency for a sweep.
     - `frequency_end` (FLOAT): The ending frequency in Hz, used only for the `sweep` waveform type.
     - `amplitude` (FLOAT): The peak amplitude of the signal, from 0.0 to 1.0. This is ignored for `silence`.
     - `dc_offset` (FLOAT): A constant value to add to the entire signal, shifting it up or down. For the `silence` type, this directly sets the signal's value.
     - `phase` (FLOAT): A phase offset in degrees (0-360) for periodic waveforms.
     - `duration` (STRING): The total duration of the audio. Supports seconds (`"5.5"`) or time format (`"HH:MM:SS.ss"`).
     - `sample_rate` (INT): The sample rate for the output audio (e.g., 44100).
     - `batch_size` (INT): The number of identical audio clips to generate in the output batch.
     - `channels` (INT): The number of audio channels (1 for mono, 2 for stereo, etc.).
     - `seed` (INT, optional): A seed for random number generation, ensuring that noise waveforms are reproducible.
   - **Output:**
     - `audio_out` (AUDIO): The generated test signal.

### 12. Audio Musical Note
   - **Display Name:** `Audio Musical Note`
   - **Internal Name:** `SET_AudioMusicalNote`
   - **Category:** `audio/generation`
   - **Description:** Converts a musical note (e.g., C#, Gb) and an octave into its corresponding frequency in Hz. This is perfect for accurately setting the frequency of the `Audio Test Signal Generator` node.
   - **Inputs:**
     - `note` (STRING): The musical note name. It's case-insensitive and flexible, accepting formats like `"C#"`, `"Db"`, `"g sharp"`, or `"a flat"`.
     - `octave` (INT): The octave number for the note. Octave 4 is the standard middle range (containing A4=440Hz).
   - **Output:**
     - `frequency` (FLOAT): The calculated frequency of the note in Hz.

### 13. Audio Join 2 Channels
   - **Display Name:** `Audio Join 2 Channels`
   - **Internal Name:** `SET_AudioJoin2Channels`
   - **Category:** `audio/manipulation`
   - **Description:** Combines two separate audio inputs into a single stereo audio output, treating the first input as the left channel and the second as the right. It intelligently handles misaligned inputs.
   - **Inputs:**
     - `audio_left` (AUDIO): The audio signal for the left channel. If it's stereo or multi-channel, it will be automatically converted to mono before being used.
     - `audio_right` (AUDIO): The audio signal for the right channel. Will also be converted to mono.
   - **Output:**
     - `audio_out` (AUDIO): A stereo audio signal.
   - **Behavior Details:**
     - **Channel Conversion:** Both `audio_left` and `audio_right` are first forced into mono to ensure they each represent a single channel stream. Note that `average` method is used, do it manually to select another mechanism.
     - **Alignment:** The two mono signals are then aligned to have the same sample rate and length, using the same logic as the "Batch Audios" node (resamples to match `audio_left`'s SR, pads to match the longest duration).
     - **Batch Handling:** If the inputs have different batch sizes, the last item of the shorter batch is repeated to match the length of the longer batch.

### 14. Audio Split 2 Channels
   - **Display Name:** `Audio Split 2 Channels`
   - **Internal Name:** `SET_AudioSplit2Channels`
   - **Category:** `audio/manipulation`
   - **Description:** Takes a stereo audio input and separates it into two mono audio outputs, one for the left channel and one for the right.
   - **Inputs:**
     - `audio` (AUDIO): The stereo audio signal to be split. **The node will raise an error if the input is not 2-channel stereo.**
   - **Outputs:**
     - `audio_left` (AUDIO): A mono audio signal containing only the left channel data.
     - `audio_right` (AUDIO): A mono audio signal containing only the right channel data.

### 15. Audio Normalize (Peak)
   - **Display Name:** `Audio Normalize (Peak)`
   - **Internal Name:** `SET_AudioNormalize`
   - **Category:** `audio/manipulation`
   - **Description:** Normalizes the volume of an audio signal so that its loudest point (peak) reaches a specified target level. This is useful for maximizing volume without clipping.
   - **Inputs:**
     - `audio` (AUDIO): The audio to normalize. Supports batches.
     - `peak_level` (FLOAT): The target peak amplitude level. `1.0` is the maximum possible level (0 dBFS). Normalizing to slightly less, like `0.9`, can provide headroom.
   - **Outputs:**
     - `normalized_audio` (AUDIO): The audio with its volume adjusted.
     - `original_peak_level` (FLOAT): The original peak level of the input audio for each item in the batch. **This value can be used with the `Audio Apply Batched Gain` node to revert the normalization and restore the original volume.**

### 16. Audio Apply Batched Gain
   - **Display Name:** `Audio Apply Batched Gain`
   - **Internal Name:** `SET_AudioApplyBatchedGain`
   - **Category:** `audio/manipulation`
   - **Description:** Applies a separate gain (volume) level to each item in an audio batch. This is the perfect companion to the `Audio Normalize` node for reverting normalization.
   - **Inputs:**
     - `audio` (AUDIO): The audio batch to apply gain to.
     - `gain_values` (FLOAT): A batch of gain values. The node expects this to be a 1D tensor of shape `(batch_size,)`, which is the format provided by the `original_peak_level` output of the `Audio Normalize` node.
   - **Output:**
     - `audio_out` (AUDIO): The audio with the per-item gain applied.

### 17. Audio Download and Load
   - **Display Name:** `Audio Download and Load`
   - **Internal Name:** `SET_AudioDownload`
   - **Category:** `audio/io`
   - **Description:** Downloads an audio file from a URL into the `ComfyUI/input/` directory if it's not already there, and then loads it as an audio signal. This is perfect for creating self-contained, shareable workflows with example audio.
   - **Inputs:**
     - `audio_bypass` (AUDIO, Optional): If an audio is provided here it will be used for the output. You can connect a `Load Audio` node here, if the connected node is muted (bypassed) we download the file, otherwise we use the audio from the `Load Audio` node.
     - `base_url` (STRING): The URL of the directory containing the audio file.
     - `filename` (STRING): The name of the file to download and load (e.g., `music.mp3`).
     - `target_sample_rate` (INT): The sample rate to load the audio at. Set to `0` to use the file's original sample rate.
   - **Output:**
     - `audio` (AUDIO): The loaded audio signal.
   - **Behavior Details:**
     - **Caching:** The node checks the `ComfyUI/input/` folder first. If the file with the specified `filename` already exists, the download is skipped.
     - **Resampling:** `torchaudio` is used to load the audio, and it will resample to `target_sample_rate` during loading if a non-zero value is provided.
     - **Player**: This node uses an `AUDIO_UI` widget to allow playing the downloaded song.


## &#x0001F680; Installation

You can install the nodes from the ComfyUI nodes manager, the name is *Audio Batch*, or just do it manually:

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/set-soft/ComfyUI-AudioBatch ComfyUI-AudioBatch
    ```
2.  Install SeCoNoHe: `pip install seconohe`
3.  Restart ComfyUI.

The nodes should then appear under the "audio/batch", "audio/conversion","audio/manipulation", "audio/generation" and "audio/io" categories in the "Add Node" menu.


## &#x0001F4E6; Dependencies

- PyTorch: Installed by ComfyUI
- Torchaudio (for resampling and potentially other audio operations): Installed by ComfyUI
- NumPy: Installed by ComfyUI
- SeCoNoHe (seconohe): This is just some functionality I wrote shared by my nodes, only depends on ComfyUI.
- Requests (optional): Usually an indirect ComfyUI dependency. If installed it will be used for downloads, it should be more robust than then built-in `urllib`, used as fallback.
- Colorama (optional): Might help to get colored log messages on some terminals. We use ANSI escape sequences when it isn't installed.

These are typically already present in a standard ComfyUI environment.

## &#x0001F5BC;&#xFE0F; Examples

Once installed the examples are available in the ComfyUI workflow templates, in the *Audio Batch* section (or ComfyUI-AudioBatch).

- [audio_batch_select_example.json](example_workflows/audio_batch_select_example.json): Shows how to create a batch and
  how to extract a single element from the batch.
- [audio_batch_select_example_extra.json](example_workflows/audio_batch_select_example_extra.json): This is like
  **audio_batch_select_example.json**, but shows how to use `Audio Download and Load`, so you have three aeasy to use
  audio files that are automatically downloaded.
- [resample_force_stereo.json](example_workflows/resample_force_stereo.json): Shows how to change the number of channels
  and the sample rate.
- [resample_force_stereo_extra.json](example_workflows/resample_force_stereo_extra.json): This is like
  **resample_force_stereo.json** but with more information (needs Easy-Use nodes) and shows how to use `Audio Download and Load`
- [generate_and_blend.json](example_workflows/generate_and_blend.json): Shows how to generate four musical notes and blend
  them together to create a chord.
- [cut_and_concat.json](example_workflows/cut_and_concat.json): Shows how to cut and concatenate audio.
- [normalize_and_undo.json](example_workflows/normalize_and_undo.json): Shows how to normalize audio level and then revert it.

## &#x0001F4DD; Usage Notes

- **AUDIO Type:** These nodes work with ComfyUI's standard "AUDIO" data type, which is a Python dictionary containing:
  - `'waveform'`: A `torch.Tensor` of shape `(batch_size, num_channels, num_samples)`.
  - `'sample_rate'`: An `int` representing the sample rate in Hz.
- **Logging:** &#x0001F50A; The nodes use Python's `logging` module. Debug messages can be helpful for understanding the transformations being applied.
  You can control log verbosity through ComfyUI's startup arguments (e.g., `--preview-method auto --verbose DEBUG` for more detailed ComfyUI logs
  which might also affect custom node loggers if they are configured to inherit levels). The logger name used is "AudioBatch".
  You can force debugging level for these nodes defining the `AUDIOBATCH_NODES_DEBUG` environment variable to `1`.

## &#x0001F6E0;&#xFE0F; Future Improvements / TODO

- Add more sophisticated downmixing options for multi-channel audio (e.g., 5.1 to stereo).
- Allow user to choose padding value (e.g., silence, edge, reflect) for length matching in "Batch Audios".
- Option in "Batch Audios" to truncate to shortest instead of padding to longest.
- More options for stereo-to-mono conversion (e.g., take left channel, take right channel).
- If you are interested on them, please open an issue.

## &#x0001F4DC; Project History

- 1.0.0 2025-06-03: Initial release
  - Initial 5 nodes: `Batch Audios`, `Select Audio from Batch`, `Audio Channel Converter`, `Audio Resampler` and `Audio Channel Conv and Resampler`

- 1.1.0 2025-06-30: Two new nodes
  - Added 2 new nodes: `Audio Force Channels` and `Audio Information`

- 1.1.1 2025-06-30: Just better project description

- 1.2.0 2025-07-18: `Audio Cut`, `Audio Concatenate`, `Audio Blend`, `Audio Test Signal Generator`, `Audio Musical Note`, `Audio Join 2 Channels`, `Audio Split 2 Channels`, `Audio Normalize (Peak)` and `Audio Apply Batched Gain`

- 1.3.0 2025-07-21: `Audio Download and Load` node for simpler examples


## &#x2696;&#xFE0F; License

[GPL-3.0](LICENSE)

## &#x0001F64F; Attributions

- Good part of the initial code and this README was generated using Gemini 2.5 Pro.
- Audio Cut is highly based on [audio-separation-nodes-comfyui](https://github.com/christian-byrne/audio-separation-nodes-comfyui/)
