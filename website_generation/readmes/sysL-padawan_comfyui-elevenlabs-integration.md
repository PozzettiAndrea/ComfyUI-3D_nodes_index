# ComfyUI ElevenLabs API integration
This ComfyUI node adds text-to-speech capabilities using the ElevenLabs API. If you enjoy using it and want to support my work, feel free to buy me a coffee — it’s much appreciated!

<a href="https://buymeacoffee.com/aoliao" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="40" width="174"></a>


![text-to-voice](./docs/text-to-voice.png)
![text-to-effect](./docs/text-to-effect.png)

## Installation

Install via the ComfyUI Manager or clone the repo into your `custom_nodes` folder:

```shell
git clone https://github.com/sysL-padawan/comfyui-elevenlabs-integration.git
```

Then change into the directory and install the dependencies:

```shell
pip install -r requirements.txt
```

Finally, restart ComfyUI.

## Nodes

Currently, there is one node for text-to-speech with ElevenLabs.

### ElevenlabsTextToSpeech

- **api_key**: Your ElevenLabs API key
- **voice_id**: The voice ID from ElevenLabs
- **model_id**: The desired model (e.g. `eleven_multilingual_v2`)
- **text**: The text to be spoken
- **output_format**: Optional, e.g. `mp3_44100_128` (default)
- **seed**: Optional, for reproducible results
- **apply_text_normalization**: Optional, choose between `auto`, `on`, or `off`
- **voice_settings_stability**: Optional, float (0.0–1.0), controls emotional range
- **voice_settings_use_speaker_boost**: Optional, boolean, boosts similarity to original speaker
- **voice_settings_similarity_boost**: Optional, float (0.0–1.0), how closely to match the original voice
- **voice_settings_style**: Optional, float (0.0–1.0), amplifies speaker style
- **voice_settings_speed**: Optional, float (0.5–2.0), adjusts speech speed

The node returns an audio tensor and the sample rate, which can be used directly for e.g. LipSync.

## Example Workflow

1. Generate text-to-speech with ElevenLabs.
2. Use the audio output for LipSync or other audio applications.

### ElevenlabsTextToEffect

- **api_key**: Your ElevenLabs API key
- **text**: The text to be converted into a sound effect
- **duration**: (Optional) Length of the effect in seconds (default: 3, range: 1–22)
- **prompt_influence**: (Optional) Influence of the text prompt on the generated effect (default: 0.3, range: 0–1)
- **output_format**: (Optional) e.g. `mp3_44100_128` (default)

The node returns an audio tensor and the sample rate, which can be used directly for further audio applications.

## Example Workflow

1. Generate a sound effect from text with ElevenLabs.
2. Use the audio output for sound design, effects, or other audio applications.

## License

- [This repo](LICENSE)
- ElevenLabs API: see [https://elevenlabs.io/terms](https://elevenlabs.io/terms)

## Credits
- [ElevenLabs](https://elevenlabs.io/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
