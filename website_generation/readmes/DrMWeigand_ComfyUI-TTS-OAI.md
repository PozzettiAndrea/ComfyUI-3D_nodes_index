# ComfyUI-TTS-OAI-API

A custom [ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for interfacing with an OpenAI‑compatible TTS API endpoint. This node is designed for flexible TTS integration. When using the official OpenAI API, it can produce audio in various formats. However, when using the non‑official Kokoros self‑hosted endpoint, the node supports only MP3 and WAV formats but provides a voice combining feature through comma‑separated voice identifiers (with optional weights)—a feature not available on the official API.

> **Important Note:**  
> When using the non‑official Kokoros self‑hosted TTS endpoint (see below), only the **mp3** and **wav** formats are supported. In contrast, the official OpenAI API may support additional formats.

## Features

- **OpenAI‑Compatible TTS:**  
  Send text to either the official OpenAI endpoint or a self‑hosted alternative (such as Kokoros) that conforms to OpenAI's API format.
  
- **Audio Format Options for Kokoros:**  
  If using the Kokoros endpoint, you must select **mp3** or **wav** as the output format. Other endpoints (like the official OpenAI API) may allow additional formats.
  
- **Voice Combining (Kokoros Only):**  
  When using the non‑official Kokoros self‑hosted TTS endpoint, the `voice` parameter supports multiple comma‑separated voice identifiers (with optional weights) for blending voices. For example, you can specify `"af_sky,af_nicole.5"` to blend voices. Other endpoints (such as the official OpenAI API) do not support voice combination and accept only a single voice identifier.
  
- **Direct Audio Integration:**  
  Returns an audio dictionary containing the waveform tensor and sample rate, ready for processing by other ComfyUI audio nodes.

## Requirements

- **Python Dependencies:**  
  - `torch`
  - `torchaudio`
  - `pydub`
  - `numpy`
  - `requests`
  
  Install them via pip:

  ```bash
  pip install torch torchaudio pydub numpy requests
  ```

- **FFmpeg:**  
  [pydub](https://github.com/jiaaro/pydub) requires FFmpeg to be installed. Follow the [FFmpeg installation guide](https://ffmpeg.org/download.html) for your platform.

## Installation

1. Place the `tts_node.py` file and its accompanying `__init__.py` into your ComfyUI custom nodes directory.
2. Ensure that all dependencies listed above are installed.
3. Configure your `pyproject.toml` as needed (an example is provided in the repository).

## Usage

1. **Configuration:**  
   Launch ComfyUI and open your node editor. Your node, **OpenAI TTS** (displayed as "ComfyUI-TTS-OAI-API"), should now be available.
   
2. **Parameters:**  
   - **text:**  
     The text you wish to convert to speech.
     
   - **model:**  
     Specify the TTS model identifier required by your endpoint.
     
   - **voice:**  
     A string representing the voice. Supply a single voice identifier (default `"af_sky"`) or, for the Kokoros endpoint, a comma‑separated list with optional weights (e.g., `"af_sky.4,af_nicole.5"`) for voice blending.
     
     > **Voice Combining:**  
     When using the Kokoros endpoint, multiple voice IDs (with or without weights) are supported. The endpoint blends the voices accordingly. This feature may not apply (or may take a different format) if using the official OpenAI API.
     
   - **api_key:**  
     Your API key for authentication, if required.
     
   - **url:**  
     The URL for your TTS service. For a self‑hosted solution (using Kokoros), a typical URL might be:  
     `http://localhost:3001/v1/audio/speech`
     
   - **response_format:**  
     For Kokoros, choose either `"mp3"` or `"wav"`. If using another endpoint (e.g., the official OpenAI API), other formats might be supported.

3. **Connecting in ComfyUI:**  
   Connect the output of the **OpenAI TTS** node to an audio preview or processing node. The node outputs an AUDIO dictionary with these keys:
   - `waveform`: A torch tensor with normalized audio samples in the range [-1, 1].
   - `sample_rate`: The sample rate at which the audio is produced (as reported by the endpoint).

## Self-Hosting with Kokoros

For those interested in self-hosting an OpenAI‑compatible TTS endpoint:

- **Kokoros Project:**  
  Visit the [Kokoros repository](https://github.com/DrMWeigand/Kokoros) for a complete implementation of a self‑hosted TTS endpoint built in Rust. This project provides detailed instructions for deploying your own API endpoint.
  
- **Format Limitation:**  
  Note that when using Kokoros, the endpoint supports only MP3 and WAV output. Make sure to select one of these formats in the `response_format` parameter.
  
- **Endpoint URL:**  
  After setting up Kokoros, update the `url` parameter in the node (e.g., `http://<your-server-ip>:3001/v1/audio/speech`).

## Example Configuration Using Kokoros

- **text:** `"Hello, world!"`
- **model:** `"default_tts_model"`
- **voice:** `"af_sky,af_nicole.5"`
- **api_key:** `""` (or your API key)
- **url:** `"http://localhost:3001/v1/audio/speech"`
- **response_format:** `"mp3"`

This configuration sends the text to your self‑hosted Kokoros endpoint, which returns an MP3 file. The node processes this file into an audio waveform for playback or additional processing in ComfyUI.

## License

This project is licensed under the terms defined in the `LICENSE` file.

## Contributing

Contributions, improvements, and bug fixes are welcome. Please submit pull requests or open issues on GitHub.
