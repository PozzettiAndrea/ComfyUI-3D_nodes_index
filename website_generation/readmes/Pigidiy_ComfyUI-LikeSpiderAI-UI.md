# ComfyUI-LikeSpiderAI-UI

**Declarative UI Framework for ComfyUI Nodes**

This extension introduces a base class for creating custom ComfyUI nodes using a declarative structure.

Instead of manually defining INPUT_TYPES and UI logic, you can focus on your node's functionality using an intuitive `UI_CONFIG` object.

---

## 📦 Features

- Minimalistic base class: `LikeSpiderUINode`
- Auto-generated UI based on simple schema
- Clean structure for rapid development
- Designed for scalability and extensions

---

## 🚀 Example Node

`Audio Export` — a sample node that saves audio files as `.mp3`, `.wav`, or `.flac`, with bitrate and filename options.

Source: [`nodes/audio_export.py`](nodes/audio_export.py)

---

## ⚖️ License

MIT © Pigidiy
