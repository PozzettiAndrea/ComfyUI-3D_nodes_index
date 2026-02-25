# ComfyUI-ElevenLabs

ElevenLabs Text-to-Speech and Voice Query nodes for ComfyUI.
![Demo](workflows/example_api.png)

## Features

- **ElevenLabsVoiceQuery**: Query ElevenLabs shared voice library with filters and random selection
- **ElevenLabsTTS**: Generate speech from text using ElevenLabs API

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/GuardSkill/ComfyUI-ElevenLabs.git
```

2. Install dependencies:
```bash
cd ComfyUI-ElevenLabs
pip install -r requirements.txt
```

3. Restart ComfyUI

## Usage

### ElevenLabsVoiceQuery

Query the ElevenLabs shared voice library to find and select voices based on various criteria.

**Parameters:**
- `api_key`: Your ElevenLabs API key
- `seed`: Random seed for reproducible voice selection (0 to 18446744073709551615)
- `category`: Voice category filter (all, high_quality, professional)
- `gender`: Gender filter (all, female, male, neutral)
- `age`: Age filter (all, middle-aged, old, young)
- `language`: Language code filter (all, ar, bg, cs, da, de, el, en, es, fi, etc.)
- `locale`: Locale filter (all, cmn-CN, cmn-TW, en-US, ja-JP, etc.)
- `use_cases`: Use case filter (all, advertisement, conversational, etc.)
- `descriptive`: Voice descriptive filter (all, calm, professional, warm, etc.)
- `page_size`: Number of voices to query (1-100)

**Outputs:**
- `voice_id`: The selected voice ID

**Features:**
- All filters support "all" option to skip filtering on that criterion
- Random seed ensures reproducible voice selection
- Automatically retries API calls up to 3 times on failure

### ElevenLabsTTS

Generate speech audio from text using a voice ID.

**Parameters:**
- `text`: The text to convert to speech
- `voice_id`: The ElevenLabs voice ID (can be connected from ElevenLabsVoiceQuery)
- `model_id`: The TTS model to use (eleven_multilingual_v2, eleven_turbo_v2, etc.)
- `api_key`: Your ElevenLabs API key

**Outputs:**
- `audio`: Generated audio in ComfyUI AUDIO format

**Features:**
- Automatically retries API calls up to 3 times on failure
- Supports multiple ElevenLabs TTS models

## Requirements

- elevenlabs
- librosa
- requests

## License

MIT
