[中文](README-CN.md) | [English](README.md)

# ComfyUI Sing to MIDI Node

Quickly convert `sing` into an editable MIDI file, while also outputting a piano audio version of the MIDI file.
- The MIDI and audio files are saved in the `ComfyUI/output/midi` directory.

## 📣 Updates

[2025-06-10]⚒️: Released v1.0.0.

## Usage

![image](https://github.com/billwuhao/ComfyUI_SOME/blob/main/images/2025-06-05_01-43-33.png)

## Installation

If you need to output the `MIDI` piano piece as an `MP3`, you need to install MuseScore4. Add the MuseScore4 installation directory, for example `C:\Program Files\MuseScore 4\bin`, to the system's PATH variable.

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_SOME.git
cd ComfyUI_SOME
pip install -r requirements.txt

# For ComfyUI's embedded python
./python_embeded/python.exe -m pip install -r requirements.txt
```

## Model Download

- [0119_continuous128_5spk.zip](https://github.com/openvpi/SOME/releases/download/v1.0.0-baseline/0119_continuous128_5spk.zip) Manually download and unzip it to the `ComfyUI\models\TTS` directory. The extracted folder will be `0119_continuous256_5spk`.

- [rmvpe.pt](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/rmvpe.pt) This model is shared with [ComfyUI_Seed-VC](https://github.com/billwuhao/ComfyUI_Seed-VC), so place it in the `ComfyUI\models\TTS\Seed-VC` directory.

## Acknowledgements

[SOME](https://github.com/openvpi/SOME)