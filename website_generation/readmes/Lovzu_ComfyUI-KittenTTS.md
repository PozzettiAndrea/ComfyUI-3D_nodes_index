# KittenTTS Node for Voice Generation

This Python class defines a custom node `KittenTTS` intended for generating audio from text using a selection of predefined voices. It is categorized under `"utils"` and integrates with a node-based workflow system.

---

## Description

- The `KittenTTS` node accepts a text string and a voice selection from a fixed list of available voice models.
- It calls the `generate_audio` function (imported from the local `.generate_voice` module) to produce synthesized speech audio.
- The node outputs the generated audio data, making it usable in downstream audio processing or playback nodes.

---

## Input Parameters

- **text** (`STRING`):  
  The input text that will be converted to speech.

- **voice** (`STRING`):  
  The voice model to use for synthesis. Allowed values are:  
  - `expr-voice-2-m`  
  - `expr-voice-2-f`  
  - `expr-voice-3-m`  
  - `expr-voice-3-f`  
  - `expr-voice-4-m`  
  - `expr-voice-4-f`  
  - `expr-voice-5-m`  
  - `expr-voice-5-f`

---

## Return Value

- Returns a tuple containing one item of type `AUDIO` — the synthesized speech audio.

---

## Integration Details

- `INPUT_TYPES` class method defines the input interface, listing required parameters and valid voice options.
- `RETURN_TYPES` specifies the output type as `"AUDIO"`.
- `FUNCTION` names the method `apply_generate_voice` to be called when executing this node.
- `CATEGORY` groups this node under `"utils"`.
- `NODE_CLASS_MAPPINGS` links the identifier `"KittenTTS"` to the `KittenTTS` class.
- `NODE_DISPLAY_NAME_MAPPINGS` sets the display name as `"Generate voice"` for UI presentation.

---

## Usage Example

```python
kitten_tts_node = KittenTTS()
audio_output, = kitten_tts_node.apply_generate_voice(
    text="Hello, how are you today?",
    voice="expr-voice-3-f"
)
# `audio_output` contains the generated audio data, ready for playback or saving.
