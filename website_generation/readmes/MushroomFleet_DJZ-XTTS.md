# DJZ XTTS Custom Node 🎤

## Overview
The DJZ XTTS Custom Node converts input text into speech using an advanced XTTS engine. Designed for high-quality audio output, it supports multiple languages and efficiently processes audio data with PyTorch and NumPy.

## Features ✨
- 🔊 **Text-to-Speech Conversion:** Generates natural-sounding audio from text.
- ⚙️ **Dynamic Device Selection:** Automatically utilizes CUDA if available, otherwise defaults to CPU.
- 🌐 **Multilingual Support:** Supports languages including English (en), Spanish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), and Chinese (zh-cn).
- 👌 **Robust Audio Processing:** Converts and reshapes audio waveforms into PyTorch tensors for further processing.
- 🚀 **Efficient Error Handling:** Provides clear and informative error messages when synthesis fails.

## How It Works 🚀
1. **Initialization:**  
   - The `DJZ_XTTS_v1` class initializes the XTTS model using the `initialize_tts` method.
   - It detects CUDA capability to ensure optimal performance, defaulting to CPU if CUDA is unavailable.

2. **Synthesis:**  
   - The `synthesize` method accepts text and a language code.
   - It synthesizes speech by invoking the XTTS model, processes the raw waveform data using NumPy, and formats it into a PyTorch tensor.
   - If available, the model uses a default speaker to improve output consistency.

3. **Integration:**  
   - This node is designed to be integrated seamlessly into larger TTS pipelines.
   - It outputs a dictionary containing the waveform tensor, sample rate, and additional metadata.

## Dependencies 📦
- [PyTorch](https://pytorch.org/)  
- [NumPy](https://numpy.org/)  
- [TTS](https://github.com/coqui-ai/TTS)  

## Usage Instructions 📝
- **Input:**  
  Provide a text string and select one of the supported language codes.
- **Output:**  
  Receives an audio tensor along with its sample rate.
- **Error Handling:**  
  Detailed exceptions are raised in case of any issues during the synthesis process.

## Code Structure 📂
- **DJZ_XTTS_v1.py:**  
  Contains the class definition for the custom node, detailing methods for initialization (`initialize_tts`) and speech synthesis (`synthesize`).

---

Enjoy using the DJZ XTTS Custom Node and happy coding! 🚀🌟
