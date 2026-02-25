# ComfyUI Dia TTS Nodes

This is an experimental WIP node pack that integrates the [Nari-Labs Dia](https://github.com/nari-labs/dia) 1.6b text-to-speech model into ComfyUI using safetensors.

Dia allows generating dialogue with speaker tags (`[S1]`, `[S2]`) and non-verbal sounds (`(laughs)`, etc.). It also supports **audio prompting** for voice cloning or style transfer.

It **requires a CUDA-enabled GPU**.

**Note:** This version is specifically configured for the `nari-labs/Dia-1.6B` model architecture.

![DiaTTS Workflow](https://github.com/BobRandomNumber/ComfyUI-DiaTTS/blob/main/example_workflows/DiaTTS.png)

## Installation

1.  Ensure you have a CUDA-enabled GPU and the necessary NVIDIA drivers installed.
2.  Download the Dia-1.6B model safetensors file from Hugging Face:
    *   **Model Page:** [https://huggingface.co/nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B)
    *   **Direct Download URL:** [https://huggingface.co/nari-labs/Dia-1.6B/resolve/main/model.safetensors?download=true](https://huggingface.co/nari-labs/Dia-1.6B/resolve/main/model.safetensors?download=true)
3.  Place the downloaded `.safetensors` file into your ComfyUI `diffusion_models` directory (e.g., `ComfyUI/models/diffusion_models/`).
4.  You might want to rename the file to `Dia-1.6B.safetensors` for clarity.
5.  Navigate to your `ComfyUI/custom_nodes/` directory.
6.  Clone this repository:
    ```bash
    git clone https://github.com/BobRandomNumber/ComfyUI-DiaTTS.git
    ```
    Alternatively, download the ZIP and extract it into `custom_nodes`.
7.  Install the required dependencies:
    *   Activate ComfyUI's Python environment (e.g., `source ./venv/bin/activate` or `.\venv\Scripts\activate` on Windows).
    *   Navigate to the node directory: `cd ComfyUI/custom_nodes/ComfyUI-DiaTTS`
    *   Install requirements: `pip install -r requirements.txt`
8.  Restart ComfyUI.

## Nodes

### Dia 1.6b Loader (`DiaLoader`)

Loads the Dia-1.6B TTS model from a local `.safetensors` file located in your `diffusion_models` directory. Loads the model weights and the required DAC codec onto the GPU. Caches the loaded model to speed up subsequent runs with the same checkpoint.

**Inputs:**

*   `ckpt_name`: Dropdown list of found `.safetensors` files within your `diffusion_models` directory. Select the file corresponding to the Dia-1.6B model.

**Outputs:**

*   `dia_model`: A custom `DIA_MODEL` object containing the loaded Dia model instance, ready for the `DiaGenerate` node.

### Dia TTS Generate (`DiaGenerate`)

Generates audio using a pre-loaded Dia model provided by the `DiaLoader` node. Displays a progress bar during generation. Supports optional audio prompting.

**Inputs:**

*   `dia_model`: The `DIA_MODEL` output from the `DiaLoader` node.
*   `text`: The main text transcript to generate audio for. Use `[S1]`, `[S2]` for speaker turns and parentheses for non-verbals like `(laughs)`. **If using `audio_prompt`, this input MUST contain the transcript of the audio prompt first, followed by the text you want to generate.**
*   `max_tokens`: Maximum number of audio tokens to generate (controls length). Default is 1720. Max usable is 3072.
*   `cfg_scale`: Classifier-Free Guidance scale. Higher values increase adherence to the text. (Default: 3.0)
*   `temperature`: Sampling temperature. Lower values are more deterministic, higher values increase randomness. (Default: 1.3)
*   `top_p`: Nucleus sampling probability. Filters vocabulary to most likely tokens. (Default: 0.95)
*   `cfg_filter_top_k`: Top-K filtering applied during CFG. (Default: 35)
*   `speed_factor`: Adjusts the speed of the generated audio (1.0 = original speed). (Default: 0.94)
*   `seed`: Random seed for reproducibility.
*   `audio_prompt` (Optional): An `AUDIO` input (e.g., from a `LoadAudio` node) to condition the generation, enabling voice cloning or style transfer.

**Outputs:**

*   `audio`: The generated audio (`AUDIO` format: `{'waveform': tensor[B, C, T], 'sample_rate': sr}`), ready to be saved or previewed. Sample rate is always 44100 Hz.

## Usage Example

### Basic Generation

1.  Add the `Dia 1.6b Loader` node (`audio/DiaTTS`).
2.  Select your Dia model file (e.g., `Dia-1.6B.safetensors`) from the `ckpt_name` dropdown.
3.  Add the `Dia TTS Generate` node (`audio/DiaTTS`).
4.  Connect the `dia_model` output of the Loader to the `dia_model` input of the Generate node.
5.  Enter your dialogue script into the `text` input on the Generate node (e.g., `[S1] Hello ComfyUI! [S2] This is Dia speaking. (laughs)`).
6.  Adjust generation parameters as needed.
7.  Connect the `audio` output of the Generate node to a `SaveAudio` or `PreviewAudio` node.
8.  Queue the prompt.

### Generation with Audio Prompt (Voice Cloning)

1.  Set up the `DiaLoader` as above.
2.  Add a `LoadAudio` node and load the `.wav` or `.mp3` file containing the voice you want to clone.
3.  Add the `Dia TTS Generate` node.
4.  Connect `dia_model` from Loader to Generate node.
5.  Connect the `AUDIO` output of `LoadAudio` to the `audio_prompt` input of the Generate node.
6.  **Crucially:** In the `text` input of the `Dia TTS Generate` node, you **must** provide the transcript of the audio prompt *first*, followed by the new text you want generated in that voice.
    *   Example `text` input:
        ```
        [S1] This is the exact transcript of the audio file I loaded into LoadAudio. [S2] It has the voice characteristics I want. (clears throat) [S1] Now generate this new sentence using that voice. [S2] This part will be synthesized.
        ```
7.  Adjust other generation parameters. Note that `cfg_scale`, `temperature`, etc., will affect how closely the generation follows the *style* of the prompt vs the *text* content.
8.  Connect the `audio` output to `SaveAudio` or `PreviewAudio`.
9.  Queue the prompt. The output audio should only contain the synthesized part (the text *after* the prompt transcript).

## Features

*   Generate dialogue via `[S1]`, `[S2]` tags.
*   Generate non-verbal sounds like `(laughs)`, `(coughs)`, etc.
    *   Supported tags: `(laughs), (clears throat), (sighs), (gasps), (coughs), (singing), (sings), (mumbles), (beep), (groans), (sniffs), (claps), (screams), (inhales), (exhales), (applause), (burps), (humming), (sneezes), (chuckle), (whistles)`. Recognition may vary.
*   **Audio Prompting:** Use an audio file and its transcript to guide voice style/cloning for new text generation.

## Notes

*   This node pack **requires a CUDA-enabled GPU**.
*   The `.safetensors` weights file for Dia-1.6B is required.
*   The first time you run the node, the `descript-audio-codec` model will be downloaded automatically. Subsequent runs will be faster.
*   Dependency `descript-audio-codec` must be installed via `requirements.txt`.
*   When using `audio_prompt`, ensure the provided `text` input correctly includes the prompt's transcript first. The model uses this text alignment to understand the audio prompt.
*   WARNING `descript-audio-codec` will install `protobuf >= 3.19.6, != 4.24.0, < 5.0.0` as a subdependancy. A user reported it installed 3.19.6 and caused errors in other nodes. This would occur if an old version is in PIP cache, if none were it would install 4.25.8.
