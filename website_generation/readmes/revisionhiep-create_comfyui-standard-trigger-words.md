# Standard Trigger Words Loader 📝

An interactive, professional-grade trigger word management node for ComfyUI. Optimized for SDXL, Illustrious, and Pony models, this node provides a high-performance button-based interface to build complex prompts with precision and speed.

## 🌟 Comprehensive Feature Set

- **Interactive Button UI**: Toggle trigger words on/off with a single click using a modern, two-column grid layout inspired by high-end workflow nodes.
- **Precision Strength Control**: 
    - **Master STR Toggle**: Enable/disable weighted prompt generation globally (Muted professional grey theme).
    - **Inline Precision Sliders**: Adjust individual tag weights from 0.0 to 2.0 with real-time feedback.
    - **Manual Numeric Entry**: Click any strength value to type a precise number directly for ultimate control.
    - **Mouse Wheel Integration**: Hover and scroll to adjust weights instantly when Strength Mode is active.
- **Dynamic Responsive Layout**: The tag grid automatically adapts its columns based on the node's width, scaling from a compact two-column view to a wide multi-column layout.
- **Single Source of Truth (SSoT)**: Centralized preset management in Python. Update your library in `standard_trigger_presets.py` and the UI builds itself dynamically on load.
- **Portable JSON Collections**:
    - **📥 Import**: Seamlessly load custom category collections from portable JSON files.
    - **📤 Export**: Backup your custom tag setups or share them with the community.
- **Advanced State Sync**:
    - **Zero-Latency Interaction**: Pure event-driven synchronization eliminates UI "snap-back" and ensure data integrity.
    - **Robust Workflow Persistence**: Automatically remembers active categories, tag states, and custom weights across workflow reloads.
    - **Bootstrap Loading**: High-speed initial load extracts library data during the extension registration phase.
- **Nuclear Scrubbing**: Built-in safety filters and regex-based cleaning prevent internal metadata, technical JSON, or "funky text" from leaking into your final prompt.
- **Smart UI Logic**:
    - **Auto-Baseline Reset**: Strength values automatically return to 1.0 when a tag is deactivated or during a master reset.
    - **Dynamic Category Management**: Create, rename, and delete custom categories directly within the UI.
    - **Automatic Color Coding**: Categories starting with "Pos:" or "Neg:" automatically inherit Green/Red visual styles.
    - **Batch Operations**: Quick master **ON** and **OFF** buttons for rapid experimentation.
    - **Collapsible categories and drag-and-drop reordering
- **Curated Preset Library**:
    - **120+ Curated Tags**: Pre-loaded with high-quality trigger words for modern image generation.
    - **13+ Default Categories**: Quality, Lighting, Composition, Poses, Expressions, Style, Detail, Aesthetic, Motion, and specialized Negative (Anatomy, Technical, etc.) groups.
- **Universal Compatibility**:
    - **Lora Manager Ready**: Works out-of-the-box with [Lora Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) and standard Lora Loaders.
    - **Text Node Integration**: Compatible with Text Concatenate and other standard string manipulation nodes.
    - **Auto-Deduplication**: Ensures your final prompt is clean and free of redundant tags.

## 📦 Installation

### Method 1: Via ComfyUI Manager (Recommended)
1. Open **ComfyUI Manager**.
2. Search for `standard trigger words`.
3. Click **Install** and restart ComfyUI.

### Method 2: Git Clone
1. Navigate to your `ComfyUI/custom_nodes/` directory.
2. Run:
   ```bash
   git clone https://github.com/revisionhiep-create/comfyui-standard-trigger-words.git
   ```
3. Restart ComfyUI.

## 🚀 Usage Guide

1. **Initialize**: Search for `Standard Trigger Words 📝` in the node menu.
2. **Library Setup**: Click **☰ Categories** to select which groups you want to see.
3. **Prompt Building**: Click tags to activate them. Active tags turn Green (Positive) or Red (Negative).
4. **Fine-Tuning**: 
   - Click **STR** to show sliders. 
   - Adjust weights using sliders or your mouse wheel.
   - Click the numeric label to type a value manually.
5. **Customization**: Use the `+` buttons to add custom tags or the "New Category" input to organize your own library.

---
*Created for the ComfyUI community by Revisionhiep. Distributed under the MIT License.*
