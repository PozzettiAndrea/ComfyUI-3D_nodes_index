# Elevenlabs-ComfyUI

**ElevenLabs API Integration for ComfyUI**

Complete suite of 13 nodes providing full access to ElevenLabs AI audio capabilities including text-to-speech, voice cloning, dubbing, sound effects, music generation, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/) [![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Getting Your API Key](#-getting-your-api-key)
- [Available Nodes](#-available-nodes)
- [Quick Start](#-quick-start)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

---

## ✨ Features

- **13 Specialized Nodes** covering all ElevenLabs API endpoints
- **Auto-Refresh** voices when API key changes
- **V3 Model Support** with emotional expressiveness (70+ languages)
- **Voice Cloning** from audio samples
- **Dubbing** for video localization
- **Sound Effects** generation from text
- **Music Generation** with AI
- **Voice Isolation** to remove background noise
- **Account Management** to check credits and usage
- **Comprehensive Error Logging** for debugging

---

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager

2. Search for "Elevenlabs-ComfyUI"

3. Click Install

### Method 2: Manual Installation

```bash
cd  ComfyUI/custom_nodes/
git  clone  https://github.com/karthikg-09/Elevenlabs-ComfyUI.git
cd  Elevenlabs-ComfyUI
pip  install  -r  requirements.txt
```

### Method 3: Portable/Standalone Installation

```bash
cd  ComfyUI_windows_portable/ComfyUI/custom_nodes/
git  clone  https://github.com/karthikg-09/Elevenlabs-ComfyUI.git
cd  Elevenlabs-ComfyUI
../../python_embeded/python.exe  -m  pip  install  -r  requirements.txt
```

**Restart ComfyUI** after installation.

---

## 🔑 Getting Your API Key

1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up for a free account (or log in)
3. Navigate to your [Profile Settings](https://elevenlabs.io/app/settings/api-keys)
4. Click **"Generate API Key"**
5. Copy the API key
6. Paste it into the `api_key` field in any node

**Note:** Keep your API key secure and never share it publicly.

---

## 📦 Available Nodes

All nodes are located in the **"ElevenLabs"** category in ComfyUI's Add Node menu.

### 1. ElevenLabs TTS (Text-to-Speech)

Convert text to natural-sounding speech with full control over voice characteristics.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **text** (STRING) - Text to synthesize (3K-40K character limit depending on model)

-  **voice** (DROPDOWN) - Voice selection from your account (auto-populated)

-  **model** (DROPDOWN) - AI model (`eleven_v3`, `eleven_multilingual_v2`, `eleven_turbo_v2_5`, etc.)

-  **stability** (FLOAT 0-1) - Voice consistency - Lower = more expressive, Higher = more stable

-  **similarity_boost** (FLOAT 0-1) - How closely output matches original voice characteristics

-  **style** (FLOAT 0-1) - Emotional expressiveness - Higher = more dramatic (especially for `eleven_v3`)

-  **use_speaker_boost** (BOOLEAN) - Enhance voice clarity and cloning accuracy (recommended: ON)

-  **language_code** (DROPDOWN) - Target language (or "auto" for automatic detection)

-  **output_format** (DROPDOWN) - Audio format: `mp3_44100_128`, `pcm_16000`, `pcm_44100`, etc.

-  **seed** (INT) - Seed for reproducible generation (-1 for random)

**Outputs:**

-  **AUDIO** - Generated speech audio (compatible with ComfyUI audio nodes)

**Use Cases:** Voiceovers, audiobooks, narration, character dialogue, e-learning content

---

### 2. ElevenLabs Speech-to-Text

Transcribe spoken audio into text with high accuracy (99 languages supported).

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **audio** (AUDIO) - Audio input to transcribe

-  **model** (DROPDOWN) - Transcription model (`scribe_v1` or `scribe_v1_experimental`)

-  **language** (DROPDOWN) - Target language for transcription (or "auto" for detection)

**Outputs:**

-  **transcription** (STRING) - Text transcription of the audio

**Use Cases:** Subtitles, transcription services, voice-to-text workflows

---

### 3. ElevenLabs Sound Effects

Generate cinematic sound effects from text descriptions.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **text** (STRING) - Description of the sound effect (e.g., "thunder rumbling", "door creaking")

-  **duration_seconds** (FLOAT 0.5-22) - Length of the generated sound effect

-  **prompt_influence** (FLOAT 0-1) - How closely to follow the prompt - Higher = more literal

**Outputs:**

-  **AUDIO** - Generated sound effect

**Use Cases:** Game audio, film/video sound design, podcast effects, ambient sounds

---

### 4. ElevenLabs Voice Isolator

Remove background noise and isolate clean voice audio from recordings.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **audio** (AUDIO) - Audio input with background noise

**Outputs:**

-  **AUDIO** - Clean audio with voice isolated

**Use Cases:** Podcast cleanup, interview enhancement, noise reduction, vocal extraction

---

### 5. ElevenLabs Voice Changer (Speech-to-Speech)

Transform the voice in an audio recording to a different voice while preserving speech patterns.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **audio** (AUDIO) - Original audio with voice to transform

-  **target_voice** (DROPDOWN) - Voice to transform into (from your account)

-  **model** (DROPDOWN) - STS model (`eleven_english_sts_v2` or `eleven_multilingual_sts_v2`)

-  **stability** (FLOAT 0-1) - Voice consistency in transformation

-  **similarity_boost** (FLOAT 0-1) - How closely to match target voice

-  **style** (FLOAT 0-1) - Expressiveness of transformed voice

-  **use_speaker_boost** (BOOLEAN) - Enhance transformation accuracy

**Outputs:**

-  **AUDIO** - Audio with transformed voice

**Use Cases:** Voice anonymization, character voice acting, voice modification, creative projects

---

### 6. ElevenLabs Dubbing

Automatically dub videos or audio into different languages while preserving voice characteristics.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **audio** (AUDIO) - Source audio to dub

-  **target_language** (DROPDOWN) - Language to translate/dub into

-  **source_language** (DROPDOWN) - Original language (or "auto" for detection)

-  **num_speakers** (INT 1-10) - Number of distinct speakers in the audio

-  **watermark** (BOOLEAN) - Add ElevenLabs watermark (required for free tier)

**Outputs:**

-  **AUDIO** - Dubbed audio in target language

**Use Cases:** Video localization, multilingual content, international distribution

---

### 7. ElevenLabs Voice Design

Create custom voices from text descriptions using AI.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **text** (STRING) - Text description of desired voice (e.g., "young female, British accent, calm")

-  **gender** (DROPDOWN) - Voice gender: `male`, `female`, or `neutral`

-  **age** (DROPDOWN) - Voice age: `young`, `middle_aged`, or `old`

-  **accent** (DROPDOWN) - Voice accent: `american`, `british`, `australian`, etc.

-  **accent_strength** (FLOAT 0-2) - Strength of the accent - 1.0 is neutral

**Outputs:**

-  **voice_id** (STRING) - ID of the generated voice

-  **AUDIO** - Preview of the generated voice

**Use Cases:** Rapid character voice creation, A/B testing voices, prototyping

---

### 8. ElevenLabs Voice Clone

Clone a voice from audio samples for use in text-to-speech.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **voice_name** (STRING) - Name for the cloned voice

-  **audio** (AUDIO) - Audio sample of the voice to clone (1-5 minutes recommended)

-  **description** (STRING) - Optional description of the voice

**Outputs:**

-  **voice_id** (STRING) - ID of the cloned voice (use in TTS node)

-  **status** (STRING) - Status message

**Use Cases:** Personal voice cloning, character voice creation, voice preservation

**Note:** Requires appropriate subscription tier. Only clone voices you have permission to use.

---

### 9. ElevenLabs Music Generation

Generate studio-quality music from text prompts.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **prompt** (STRING) - Description of desired music (e.g., "upbeat electronic dance music")

-  **duration_seconds** (FLOAT 1-300) - Length of generated music

-  **model** (DROPDOWN) - Music model (`eleven_music_gen_v1`)

-  **temperature** (FLOAT 0.1-2.0) - Creativity/randomness - Higher = more variation

**Outputs:**

-  **AUDIO** - Generated music

**Use Cases:** Background music, game soundtracks, video scoring, creative projects

**Note:** Requires specific subscription tier with music generation access.

---

### 10. ElevenLabs User Info

Check your account status, credits, character usage, and subscription details.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **refresh** (BOOLEAN) - Force refresh account data from API

**Outputs:**

-  **user_info** (STRING) - Formatted account information including:

- Email and subscription tier

- Character usage and limits

- Remaining character quota

- Voice cloning slots

- API access status

**Use Cases:** Monitor usage, check remaining credits, verify subscription status

---

### 11. ElevenLabs Refresh Voices

Manually refresh the cached list of voices and models from your account.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **refresh_voices** (BOOLEAN) - Refresh voice list from API

-  **refresh_models** (BOOLEAN) - Refresh available models list

**Outputs:**

-  **status** (STRING) - Refresh status message

**Use Cases:** Update voice list after cloning, force cache refresh, sync account changes

**Note:** TTS and Voice Changer nodes automatically refresh when API key changes. This node is for manual control.

---

### 12. ElevenLabs History

View your generation history and retrieve previous audio generations.

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **page_size** (INT 1-100) - Number of history items to retrieve

**Outputs:**

-  **history** (STRING) - Formatted list of recent generations with metadata

**Use Cases:** Track usage, review previous generations, audit API calls

---

### 13. ElevenLabs Voice Manager

Manage voices in your account (list, delete, or get details).

**Inputs:**

-  **api_key** (STRING) - Your ElevenLabs API key

-  **action** (DROPDOWN) - Action to perform: `list`, `get_details`, or `delete`

-  **voice_id** (STRING) - Voice ID (required for `get_details` and `delete` actions)

**Outputs:**

-  **result** (STRING) - Result of the action

**Use Cases:** Voice library management, cleanup unused voices, voice information retrieval

---

## 🎯 Quick Start

### Basic Text-to-Speech Workflow

1.  **Add Node:** Right-click → Add Node → ElevenLabs → ElevenLabs TTS

2.  **Enter API Key:** Paste your ElevenLabs API key

3.  **Enter Text:** Type or connect text input

4.  **Select Voice:** Choose from dropdown (auto-populated from your account)

5.  **Select Model:** Choose `eleven_v3` for emotions, or `eleven_turbo_v2_5` for speed

6.  **Adjust Settings:**

-  `stability`: 0.5 (default)

-  `similarity_boost`: 0.75 (default)

-  `style`: 0.7 for emotional delivery, 0.0 for neutral

7.  **Run Workflow:** Queue Prompt

8.  **First Run:** Voices refresh automatically

9.  **Reload Node:** Right-click node → Reload Node to see updated voice list

### Voice Cloning Workflow

1. Add **ElevenLabs Voice Clone** node
2. Enter API key and voice name
3. Connect audio sample (1-5 minutes of clear speech)
4. Run to create cloned voice
5. Copy the `voice_id` output
6. Use in **ElevenLabs TTS** node for generation

### Emotional Speech (V3 Model)

1. Add **ElevenLabs TTS** node
2. Select `eleven_v3` model
3. Set `style` to 0.7-1.0
4. Set `stability` to 0.3-0.5
5. Use descriptive text with emotional context
6. Generate dramatic, expressive speech in 70+ languages

---

## 🎛️ Parameter Guide

### Voice Settings

-  **Stability** (0.0-1.0)

-  **Low (0.0-0.3)** = Expressive, variable speech

-  **Mid (0.4-0.6)** = Balanced delivery

-  **High (0.7-1.0)** = Consistent, predictable

-  **Similarity Boost** (0.0-1.0)

-  **Low (0.0-0.3)** = Generic voice qualities

-  **Mid (0.4-0.6)** = Match original voice

-  **High (0.7-1.0)** = Exact voice match

-  **Style** (0.0-1.0)

-  **Low (0.0-0.3)** = Neutral, calm tone

-  **Mid (0.4-0.6)** = Moderate emotion

-  **High (0.7-1.0)** = Dramatic, intense delivery

### Model Selection

-  **`eleven_v3`**

- Latency: High | Languages: 70+ | Char Limit: 3,000

-  **Best for:** Emotional content, audiobooks, dramatic delivery

-  **`eleven_multilingual_v2`**

- Latency: Medium | Languages: 29 | Char Limit: 10,000

-  **Best for:** General purpose, high quality speech

-  **`eleven_turbo_v2_5`**

- Latency: Low | Languages: 32 | Char Limit: 40,000

-  **Best for:** Speed + quality balance, long content

-  **`eleven_flash_v2_5`**

- Latency: Ultra-low (~75ms) | Languages: 32 | Char Limit: 40,000

-  **Best for:** Real-time applications, voice agents

**For emotional speech:** Use `eleven_v3` with high `style` (0.7-1.0)

**For fast generation:** Use `eleven_flash_v2_5` or `eleven_turbo_v2_5`

**For long text:** Use `eleven_turbo_v2_5` (40K char limit)

---

## 🔧 Troubleshooting

### Voices Not Appearing

**Cause:** Voice list needs refresh after adding new voices.

**Solution:**
1. Enter/modify API key in TTS node
2. Run the node once (Queue Prompt)
3. Console shows: `🔄 New API key detected - Auto-refreshing voices...`
4. Right-click node → **Reload Node** (or F5)
5. Voices appear in dropdown

**Alternative:** Use **ElevenLabs Refresh Voices** node

### Error: Invalid API Key

**Cause:** API key is incorrect, expired, or not properly formatted.

**Solution:**
1. Verify API key at [ElevenLabs Settings](https://elevenlabs.io/app/settings/api-keys)
2. Generate new API key if needed
3. Copy entire key including any dashes or special characters
4. Ensure no extra spaces before/after key

### Error: Character Limit Exceeded

**Cause:** Text exceeds model's character limit.

**Solution:**

-  `eleven_v3`: Max 3,000 characters

-  `eleven_multilingual_v2`: Max 10,000 characters

-  `eleven_turbo_v2_5`: Max 40,000 characters

- Split long text into chunks or use a model with higher limit

### Error: Insufficient Credits

**Cause:** Account has run out of character quota.

**Solution:**
1. Use **ElevenLabs User Info** node to check remaining credits
2. Upgrade subscription at [ElevenLabs Pricing](https://elevenlabs.io/pricing)
3. Wait for monthly quota reset

### Audio Quality Issues

**Common Fixes:**

- Increase `stability` for more consistent output

- Increase `similarity_boost` for better voice matching

- Enable `use_speaker_boost` for cloned voices

- Try different voices (some are more stable)

- Use higher quality `output_format` (e.g., `pcm_44100`)

### Console Errors and Logging

All nodes output detailed error messages to the ComfyUI console/terminal:

- API request details (voice ID, model, settings)

- HTTP status codes and error responses

- Helpful suggestions for fixing issues

**Always check the console for debugging information.**

---

## 📚 Additional Resources

-  **ElevenLabs Documentation:** [elevenlabs.io/docs](https://elevenlabs.io/docs/overview)

-  **API Reference:** [elevenlabs.io/docs/api-reference](https://elevenlabs.io/docs/api-reference)

-  **Model Information:** [elevenlabs.io/docs/models](https://elevenlabs.io/docs/models)

-  **Voice Library:** [elevenlabs.io/voice-library](https://elevenlabs.io/voice-library)

-  **Pricing:** [elevenlabs.io/pricing](https://elevenlabs.io/pricing)

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Important Notes

-  **API Key Security:** Never share your API key publicly or commit it to version control

-  **Voice Cloning Ethics:** Only clone voices you have permission to use

-  **Rate Limits:** Respect ElevenLabs API rate limits (varies by subscription tier)

-  **Terms of Service:** Use in compliance with [ElevenLabs Terms of Service](https://elevenlabs.io/terms)

-  **Data Privacy:** Review [ElevenLabs Privacy Policy](https://elevenlabs.io/privacy) for data handling

---

## 🎉 Credits

Created and maintained by the karthikg-09.

Built for the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) community.

Powered by [ElevenLabs](https://elevenlabs.io/) AI audio technology.

---

**Enjoy creating amazing AI audio with ElevenLabs in ComfyUI! 🎙️✨**