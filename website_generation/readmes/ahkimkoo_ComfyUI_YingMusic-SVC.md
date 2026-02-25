# ComfyUI_YingMusic-SVC
----
This project is based on the code from https://github.com/yourusername/ComfyUI_YingMusic-SVC.git.
It has been adapted into a ComfyUI custom node and is intended for use within ComfyUI workflows.


#### ch01. Installation
1. Clone the repository into the ComfyUI custom_nodes directory:
```bash
cd /path/to/ComfyUI
git clone https://github.com/yourusername/ComfyUI_YingMusic-SVC custom_nodes/ComfyUI_YingMusic-SVC

# cd custom_nodes/ComfyUI_YingMusic-SVC
# git mv requirements.txt requirements.txt.bk
# git mv README.md README.md.bk
# awk -F "[ =<>]" '$1=="torch" || $1=="torchvision" || $1=="torchaudio"{next} {print $1} \
#   END{print "\ndemucs\nrequests"}' requirements.txt.bk > requirements.txt
# ls -1 README.md __init__.py nodes.py
```

2. Install dependencies in the ComfyUI environment
```bash
conda install -c conda-forge -y sox      # @conda
# sudo apt install -y sox libsox-fmt-all # @debian/venv

pip install -r custom_nodes/ComfyUI_YingMusic-SVC/requirements.txt
```
Note: libsox is required for audio I/O and resampling via torchaudio.

3. Download models
- install commandline tool hf and create the models dir
```
pip install -U "huggingface_hub[cli]"
mkdir -p ./models/YingMusic-SVC
```
- Download GiantAILab/YingMusic-SVC
```
hf download --local-dir ./models/YingMusic-SVC GiantAILab/YingMusic-SVC YingMusic-SVC-full.pt
```
- Download funasr/campplus
```
hf download --local-dir ./models/YingMusic-SVC/funasr/campplus funasr/campplus
```
- Download lj1995/VoiceConversionWebUI
```
hf download --local-dir ./models/YingMusic-SVC/lj1995/VoiceConversionWebUI \
  lj1995/VoiceConversionWebUI rmvpe.pt
```
- Download nvidia/bigvgan_v2_44khz_128band_512x
```
hf download --local-dir ./models/YingMusic-SVC/nvidia/bigvgan_v2_44khz_128band_512x \
  nvidia/bigvgan_v2_44khz_128band_512x bigvgan_generator.pt config.json
```
- Download openai/whisper-small
```
hf download --local-dir ./models/YingMusic-SVC/openai/whisper-small openai/whisper-small
```
- Download for htdemucs for Demucs
```
mkdir -p ~/.cache/torch/hub/checkpoints

wget -O ~/.cache/torch/hub/checkpoints/955717e8-8726e21a.th \
  https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/955717e8-8726e21a.th
```

4. Copy the configuration files
- Copy the configuration file to models/configs(the filename must be converted to lowercase):
```
cp custom_nodes/ComfyUI_YingMusic-SVC/configs/YingMusic-SVC.yml models/configs/yingmusic-svc.yaml
```


#### ch02. Usage
1. Add nodes to your workflow
- Add a `YingMusicSVC: Load Models` node as `LoadModels`
- Add a `Upload Audio(Upload)` node as `UploadAudio`
- Add a `Upload Audio(Upload)` node as `UploadVolcals`
- Add a `YingMusicSVC: Audio Seperator` node as `AudioSeperator`
- Add a `YingMusicSVC: Voice Convert` node as `VoiceConvert`
- Add a `Preview Audio` node as `PreviewVocals`
- Add a `Preview Audio` node as `Preview Audio`
- Add a `Preview Any` node as `VoiceConvert_Metrics`

2. workflow
- docs/workflow.a01.png

3. Performing Voice Conversion
- Connect `LoadModels` model_bundle -> `Voice_Convert` model_bundle
- Connect `UploadAudio` audio -> `AduioSeparator` audio
- Connect `AduioSeparator` vocals -> `VoiceConvert` input_vocals
- Connect `AduioSeparator` instructmental -> `VoiceConvert` instructmental_audio
- Connect `UploadVocals` audio -> `VoiceConvert` ref_vocals
- Connect `VoiceConvert` vocals -> `PreviewVocals` audio
- Connect `VoiceConvert` audio -> `PreviewAudio` audio
- Connect `VoiceConvert` metrics -> `VoiceConvert_Metrics` source
- Adjust parameters as needed:
  - diffusion_steps: Number of diffusion steps (higher = better quality but slower). Typical range: 20–60.
  - inference_cfg_rate: Classifier-free guidance rate. Controls how strongly the model follows the reference (target) timbre/style versus the source content.
    - Lower: more “source-like” / less reference influence
    - Higher: more “target-like” / stronger reference influence
    - Typical: 0.5–1.0.
  - f0_condition: Enable/disable pitch (F0) conditioning.
    - True: better pitch accuracy / singing & expressive speech usually improves
    - False: can sound smoother for some speech, but pitch may drift
  - semi_tone_shift: Shift the output pitch in semitones.
    - Positive = higher pitch, negative = lower pitch
    - 0 (or None): no manual shift (uses adaptive/auto pitch adjustment if enabled in your pipeline)
  - vocal_gain: Gain applied to the converted vocal before mixing with accompaniment.
    - 1.0 = unchanged
    - Increase to make vocal louder in the final mix (e.g. 1.2–1.8)
  - instructmental_gain: Gain applied to accompaniment before mixing.
    - 1.0 = unchanged
    - Decrease to duck the backing track (e.g. 0.6–0.9) so vocals sit on top
  - save_debug_wav: Save intermediate/final WAV files to the ComfyUI output folder for debugging.
    - False: no files written, output only flows through the graph
    - True: writes a timestamped WAV (and optionally an additional mixed/accompany version, if you kept that logic)
  - fp16: Use half precision (float16) inference to reduce VRAM and speed up on NVIDIA GPUs.
    - Recommended True on CUDA GPUs
    - Automatically should be forced to False on CPU (fp16 typically doesn’t help and may break)

4. Debug Output(save_debug_wav=true), output/YingMusicSVC/:
- mixed_{pitch_shift}.{ts}.wav
- accompany.{ts}.wav
- vc_{pitch_shift}.{ts}.wav


#### ch04. Notes
- The model requires significant GPU memory for inference
- For best results, use high-quality input audio
- The reference audio should be clean speech without background noise


#### ch05. Troubleshooting
- If you encounter CUDA out of memory errors, try reducing the batch size or using a smaller model
- Make sure all required model files are downloaded and in the correct locations
- Check the ComfyUI console for error messages


#### ch06. License
This project is licensed under the same terms as the original YingMusic-SVC model.
