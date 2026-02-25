# ComfyUI DMOSpeech2 Node

A ComfyUI custom node implementation of [DMOSpeech2](https://github.com/yl4579/DMOSpeech2) - Reinforcement Learning for Duration Prediction in Metric-Optimized Speech Synthesis.

## Features

- High-quality text-to-speech synthesis with metric optimization
- Reinforcement learning-based duration prediction
- Teacher-guided sampling for improved diversity
- Support for multi-speaker speech generation
- Zero-shot voice cloning capabilities

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/HM-RunningHub/ComfyUI_RH_DMOSpeech2.git
```

3. Install requirements:
```bash
cd ComfyUI_RH_DMOSpeech2
pip install -r requirements.txt
```

4. Restart ComfyUI

## Model Download

You need to download 4 model components to the following directories:

### 1. DMOSpeech2 Main Models
Create `ckpts` directory and download:
```bash
cd models/DMOSpeech2
mkdir ckpts
cd ckpts
wget https://huggingface.co/yl4579/DMOSpeech2/resolve/main/model_85000.pt
wget https://huggingface.co/yl4579/DMOSpeech2/resolve/main/model_1500.pt
```

### 2. Emilia Vocabulary
Create `Emilia_ZH_EN_pinyin` directory and download vocab file:
```bash
mkdir Emilia_ZH_EN_pinyin
# Download vocab.txt to this directory
https://huggingface.co/spaces/mrfakename/E2-F5-TTS/blob/27cee60c0890d22dab124730a73d5453fc8359a5/data/Emilia_ZH_EN_pinyin/vocab.txt
```

### 3. Vocos Vocoder
Download Vocos mel vocoder model:
```bash
# Create vocos-mel-24khz directory and download required files
# config.yaml, pytorch_model.bin, etc.
https://huggingface.co/charactr/vocos-mel-24khz/tree/main
```

### 4. Whisper Model
Download Whisper large v3 turbo model:
```bash
# Create whisper-large-v3-turbo directory and download required files
# All tokenizer and model files
https://huggingface.co/openai/whisper-large-v3-turbo/tree/main
```

## Usage

1. Load the DMOSpeech2 node in ComfyUI
2. Connect text input and reference audio (for voice cloning)
3. Configure generation parameters
4. Generate high-quality speech output

## Models Directory Structure

```
DMOSpeech2/
├── ckpts/
│   ├── model_1500.pt           # Duration predictor
│   └── model_85000.pt          # Main DMOSpeech2 model
├── Emilia_ZH_EN_pinyin/
│   └── vocab.txt               # Vocabulary file
├── vocos-mel-24khz/            # Vocos vocoder
│   ├── config.yaml
│   ├── pytorch_model.bin
│   └── ...
├── whisper-large-v3-turbo/     # Whisper ASR model
│   ├── config.json
│   ├── model.safetensors
│   └── ...


## Credits

- Original DMOSpeech2: [yl4579/DMOSpeech2](https://github.com/yl4579/DMOSpeech2)
- Based on F5-TTS architecture
- Implements GRPO (Group Relative Preference Optimization) for duration prediction

## License

MIT License
