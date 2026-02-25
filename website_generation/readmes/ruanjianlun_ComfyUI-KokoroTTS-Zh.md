# ComfyUI-KokoroTTS-Zh

A custom node extension for ComfyUI that integrates KokoroTTS for high-quality Chinese text-to-speech synthesis.

## Introduction

ComfyUI-KokoroTTS-Zh is a collection of extension nodes for ComfyUI that integrates the KokoroTTS voice synthesis engine into ComfyUI workflows. It provides high-quality Chinese speech synthesis with support for multiple voices and speech speed adjustment.

## Features

- Load KokoroTTS models
- Process multi-paragraph text input
- Support for nearly 100 different Chinese voices (50 female and 50 male)
- Control silence between paragraphs
- Sentence joining option
- Support for automatic and fixed speed modes
- Generate high-quality 24kHz WAV audio
- Compatible with ComfyUI audio nodes

## Installation


### Installation Steps

1. Make sure ComfyUI is installed and running properly

2. Clone this repository to the `custom_nodes` directory of ComfyUI:

   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/ruanjianlun/ComfyUI-KokoroTTS-Zh.git
       pathto\python_embeded\python.exe -m pip install "kokoro>=0.8.1" "misaki[zh]>=0.8.1"  "soundfile>=0.10.0" 
   ```

3. Install dependencies:

   ```bash
   cd ComfyUI-KokoroTTS-Zh
   pip install -r requirements.txt
   ```

4. Restart the ComfyUI service

## Usage

In ComfyUI, you can use the following nodes:

1. **KokoroModelLoader**: Loads the KokoroTTS model
   - Input: Hugging Face repository ID
   - Output: Model and voice pipeline objects

2. **KokoroTextInput**: Input text to synthesize
   - Input: Multi-line text (split by paragraphs)
   - Output: Processed text paragraph list

3. **KokoroVoiceSelector**: Select voice and silence settings
   - Input: Voice ID, silence length between paragraphs, whether to join sentences
   - Output: Voice settings dictionary

4. **KokoroTTSGenerator**: Generate audio
   - Input: Model, pipeline, text, voice settings, output filename, speed mode, fixed speed value
   - Output: Audio object and file path

### Basic Workflow

1. Load the model
2. Input text to synthesize
3. Configure voice and silence settings
4. Generate and save audio

## Example

Here's an example of a basic workflow configuration:

1. **KokoroModelLoader** → Load default model "hexgrad/Kokoro-82M-v1.1-zh"
2. **KokoroTextInput** → Input "欢迎使用KokoroTTS！这是一个很棒的语音合成引擎。"
3. **KokoroVoiceSelector** → Select female voice "zf_018", paragraph interval 5000, don't join sentences
4. **KokoroTTSGenerator** → Generate audio, using automatic speed

## Advanced Options

- **Speed Control**: You can select "auto" or "fixed" speed mode in the KokoroTTSGenerator node
  - Auto mode: Dynamically adjusts speed based on text length to avoid fast speech with long text
  - Fixed mode: Uses the specified fixed speed value (0.5-2.0)

- **Sentence Joining**: Choose whether to join multiple sentences in a paragraph for processing

## License

MIT License

## Contributing

Pull requests and issues are welcome.

## Acknowledgements

- [KokoroTTS](https://github.com/hexgrad/kokoro) - High-quality Chinese speech synthesis engine
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Powerful node-based UI framework
