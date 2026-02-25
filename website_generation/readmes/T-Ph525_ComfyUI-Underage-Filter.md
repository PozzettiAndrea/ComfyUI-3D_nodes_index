# ComfyUI Underage Content Filter & Moderation Nodes

This extension adds moderation-focused nodes for ComfyUI to help filter, block, or gate content based on predicted age, classification confidence, and dynamic logic gates. It uses [nateraw/vit-age-classifier](https://huggingface.co/nateraw/vit-age-classifier) to determine age from images.

---

## 🚀 Features

### ✅ AgeCheckerNode
Performs age classification using a ViT-based model and optionally blocks underage content.

**Inputs:**
- `image`: Image tensor (1 image)
- `gate_enabled`: Boolean toggle to block underage output
- `use_local_model`: Toggle to load local model from `LOCAL_AGE_MODEL_PATH` environment variable

**Outputs:**
- `is_underage`: Boolean
- `predicted_age`: Integer (age bucket or class)
- `confidence`: Float (probability)
- `status`: String (`Underage` or `OK`)
- `gate_output`: Boolean for workflow continuation

> If `gate_enabled` is `True` and the subject is underage, it will raise a `PermissionError`.

---

### 🔎 UnderageFilterNode
A lightweight classifier that checks if the image falls into one of the underage classes (`0-2`, `3-9`, `10-19`) with a confidence threshold.

**Inputs:**
- `image`: Image tensor
- `score`: Minimum confidence threshold (default: `0.85`)

**Outputs:**
- `is_underage`: Boolean

---

### ⛔ MultiTypeGateNode
A flexible gate node that can conditionally halt workflows based on any value type.

**Inputs:**
- `value`: Supports `BOOLEAN`, `INT`, `FLOAT`, `STRING`
- `block_on`: Mode (`falsy`, `truthy`, `equal`)
- `match_value`: Value to match if using `equal` mode
- `message`: Custom error message to raise

**Outputs:**
- (None) — raises `PermissionError` if condition is met

---

## 📦 Installation

1. Clone or download this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   git clone https://github.com/your-repo/comfyui-underage-filter.git
