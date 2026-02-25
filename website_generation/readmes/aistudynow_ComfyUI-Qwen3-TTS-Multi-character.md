# 🚀 ComfyUI-Qwen3-TTS

**An industrial-grade audio synthesis solution for ComfyUI, based on the open-source Qwen3-TTS model by the Alibaba Qwen Team.**

This extension not only perfectly reproduces the core capabilities of Qwen3-TTS but extends it with a **Smart Script Engine**, **Multi-Speaker Cinematic Engine**, and **Professional Audio Post-Processing**. It covers everything from simple single-sentence synthesis to complex, full-cast audio dramas.

# Video and Article coming Soon

---

## 📋 Changelog

* **2026-01-24: Core Architecture Upgrade**
    * **New Nodes:** Added `RoleBank` (Character Registry), `AdvancedDialogue` (Multi-speaker Engine), and `ScriptProcessor`.
    * **Smart Parsing:** Added support for auto-parsing `[Emotion Tags]` and `[pause:1.2s]` timing instructions within text.
    * **Control:** Added **Seed** control for deterministic generation, Output Mode (Merge/Split), and Audio-to-Text (ASR) capabilities.
* **2026-01-23: Sampling Controls**
    * **Basic Features:** Unlocked full sampling parameters for all generation nodes (`top_p`, `top_k`, `temperature`, `repetition_penalty`) to prevent audio degradation.

---

## ✨ Key Features

### 1. The Four Core Capabilities
* 🎭 **Custom Voice (Presets):** Access 9 high-quality internal presets immediately (e.g., Vivian, Uncle_Fu).
* 🎨 **Voice Design (Text-to-Voice):** Design unique voices using natural language prompts (e.g., *"A deep, rasping voice of an old wizard"*).
* 🦜 **Voice Clone (Zero-Shot):** Clone a voice using just 3+ seconds of reference audio. Includes an **X-Vector Mode** for pure timbre extraction without reference text.
* ⚡ **Pre-Compute (Latents):** Decouples voice analysis from generation. Analyze the reference audio once, and generate infinite text rapidly without re-processing the source.

### 2. Advanced Cinematic Features (New)
* 🧠 **Smart Sentiment Parsing:** Automatically detects and applies bracketed emotion tags like `[Happy]`, `[Cold]`, or `[Whisper]`.
* ⏱️ **Precision Timing Control:** Use `[pause:1.2]` inside your script to insert exact milliseconds of silence for pacing.
* 👥 **Multi-Role Orchestration:** Use the `RoleBank` to register multiple voices. The `AdvancedDialogue` node then automatically switches voices based on your script, generating a full conversation in one go.
* 💾 **Asset Persistence:** Save your cloned voice embeddings as `.qwen3tts` files to build a library of characters that can be reused anytime.

### 3. Engineering Optimizations
* **Deterministic Output:** Full **Seed** support allows you to lock the random noise. If you like a specific take, you can reproduce it exactly.
* **Batch Inference:** Supports multi-line input for parallel generation.
* **Dual Download Sources:** Supports automatic switching between ModelScope (CN) and HuggingFace.
* **Robust Execution:** Built-in VRAM management, forced garbage collection, and CPU fallback protection to prevent OOM crashes.

---

## 📦 Installation

### 1. Plugin Installation
Navigate to your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone [https://github.com/wanaigc/ComfyUI-Qwen3-TTS.git](https://github.com/wanaigc/ComfyUI-Qwen3-TTS.git)
cd ComfyUI-Qwen3-TTS


