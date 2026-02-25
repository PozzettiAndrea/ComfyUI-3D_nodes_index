# KokoroTTS Node 🚀
![demo-v4](https://raw.githubusercontent.com/MushroomFleet/DJZ-KokoroTTS/refs/heads/main/KokoroTTS_V4.png)

This node provides advanced text-to-speech functionality powered by KokoroTTS. Follow the instructions below to install, configure, and use the node within your portable ComfyUI installation.

## Installation 🔧

1. **Download/Clone the Node:**  
   Copy or download the entire `DJZ-KokoroTTS` folder into the `custom_nodes` folder inside your ComfyUI installation.

2. **Running the Installer for Portable ComfyUI:**  
   For Windows portable users:  
   - Execute the `install-portable.bat` file.
   - This batch file automatically sets up necessary dependencies and paths for the node to work correctly with your portable ComfyUI.
   - Simply double-click the file, or run it from the command line.  
     
   **Tip:** Make sure your ComfyUI portable installation is not running while you execute the batch file. ⚠️

## Model Setup 🗂️

This node requires two specific models to work correctly.

- **Required Model Location:**  
  All required models must be placed in the directory:  
  ```
  /comfyui/models/kokoro/
  ```
- The model location is defined in the `models.json` configuration file. Please ensure that the models (e.g., the voice synthesis model and the text processing model) are exactly in this folder for the node to detect and load them properly. https://github.com/taylorchu/kokoro-onnx/releases/download/v0.2.0/kokoro.onnx

## Usage 📖

1. **Configuration:**  
   Open your preferred workflow editor in ComfyUI and add the KokoroTTS node to your workflow.  
   Configure the available options directly on the node. Options may include parameters such as voice type, speed, pitch, or any additional experimental features defined in the node's interface.

2. **Running the Workflow:**  
   Once configured, run your workflow. The node processes text input and produces high-quality speech output. The audio will be played directly or saved to a user-defined file directory, based on your settings.

3. **Troubleshooting:**  
   - If the node does not work as expected, verify that:
     - You ran the `install-portable.bat` successfully.
     - The models are correctly placed in `/comfyui/models/kokoro/`.
     - All dependencies listed in `requirements.txt` have been installed.
   - Check your ComfyUI logs for any error messages. 🔍

## Additional Options ⚙️

Inside the node, you can adjust various parameters to suit your needs:
- **Voice Configuration:** Select between different voice profiles.
- **Synthesis Options:** Adjust processing speed and pitch.
- **Output Options:** Define whether to stream the audio directly or save it as a file.

These settings are fully customizable through the node interface within ComfyUI.

## Conclusion 🎉

Recent Updates:
- KokoroTTS_v2.py now provides a "default" blending method using a weighted sum approach.
- KokoroTTS_v3.py introduces Spherical Interpolation blending method for enhanced quality.

The KokoroTTS Node is a robust tool to add state-of-the-art text-to-speech capabilities to your image generation workflows. Follow the above steps to set up and enjoy seamless speech synthesis!

Happy synthesizing! 😊

## 📚 Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{djz_kokorottS,
  title = {DJZ Kokoro TTS: Extended voice merging with DJZ Kokoro TTS nodes in ComfyUI},
  author = {[Drift Johnson]},
  year = {2025},
  url = {https://github.com/MushroomFleet/DJZ-KokoroTTS},
  version = {1.0.0}
}
```


### Donate:

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)

