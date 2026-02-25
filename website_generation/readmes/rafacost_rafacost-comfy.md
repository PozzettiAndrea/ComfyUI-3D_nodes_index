# ComfyUI-DreamOmni2-GGUF

A **ComfyUI custom node** for **DreamOmni2 GGUF multimodal models** — powered directly by **`llama-cpp-python`**, no external executables required.

⚠️ **Work in Progress** — use at your own risk. <sub>(Or better: fork and help improve it.)</sub>

---

## ✨ Features

* Run **DreamOmni2 GGUF** models natively inside ComfyUI.
* Full **image + text multimodal support** through the `llama-cpp-python` backend.
* Accepts up to **four image inputs** simultaneously.
* Outputs either:

  * **conditioning embeddings** (for generation workflows), or
  * **text descriptions** (for captioning or analysis).
* Built-in **seeded cache system** for deterministic results across sessions.
* No dependency on external binaries or CLI tools.

---

## 🧩 Prerequisites

Requires **Python ≥ 3.12** and a working **ComfyUI ≥ 0.3.66**.

Install dependencies (CPU or CUDA builds supported):

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
torch>=2.2.0
numpy
Pillow
scikit-build-core
llama-cpp-python>=0.3.16
```

For CUDA acceleration, install the matching wheel from
[llama-cpp-python (CUDA builds)](https://github.com/abetlen/llama-cpp-python/releases).

Example (Windows CUDA 12.x):

```bash
pip install llama_cpp_python-0.3.16+cu124-cp312-cp312-win_amd64.whl
```

---

## 🧠 Installation

1. Clone this repository into your ComfyUI `custom_nodes` directory:

   ```bash
   git clone https://github.com/rafacost/rafacost-comfy.git
   ```

2. Download the **DreamOmni2 GGUF** and **mmproj** models from
   [Hugging Face](https://huggingface.co/rafacost/DreamOmni2-7.6B-GGUF).

3. Place them in:

   ```
   ComfyUI/models/unet/
   ├── DreamOmni2-Vlm-Model-7.6B-Q5_K.gguf
   ├── DreamOmni2-Vlm-Model-7.6B-f16-mmproj.gguf
   ├── flux1-kontext-dev-Q5_K.gguf
   ComfyUI/models/loras/
   ├── DreamOmni2-7.6B-Edit-Lora.safetensors
   ├── DreamOmni2-7.6B-Gen-Lora.safetensors
   ```

---

## ⚙️ Usage

1. Launch **ComfyUI**.

2. Add the **DreamOmni2-VLM** node under **rafacostComfy / VLM**.

3. Configure the node:

   * **Model** – select your `DreamOmni2` `.gguf` model.
   * **MMProj Path** – select your vision projection `.gguf`.
   * **Images** – connect up to four `Load Image` nodes.
   * **Prompt** – enter a description or instruction.
   * **Seed** – for deterministic results (cache linked).
   * **Use Cache** – toggle to reuse previous generations.
   * **As Conditioning** – output embeddings instead of raw text.

4. Optionally connect a **DreamOmni2 Output Node** to visualize the generated text inside the workflow.

---

## 🧪 Example

Use the sample workflow provided in `workflows/` or connect images manually.
Outputs appear both in the **ComfyUI graph** and in the **terminal console**.

---

## ⚙️ Troubleshooting

| Issue                                            | Cause                                  | Fix                                              |
| ------------------------------------------------ | -------------------------------------- | ------------------------------------------------ |
| `ImportError: cannot import Qwen25VLChatHandler` | Missing or outdated `llama-cpp-python` | `pip install --upgrade llama-cpp-python>=0.3.16` |
| Model loads but crashes                          | Out-of-memory                          | Try lower quant (e.g. `Q4_K`)                    |
| No output text                                   | Prompt too short / token limit         | Increase `max_tokens`                            |
| Different outputs for same seed                  | Cache disabled or model reset          | Enable **Use Cache**                             |
| “NoneType object” errors                         | Missing mmproj                         | Verify both GGUF files are present               |
| Low Image Quality                                | Low Base Model GGUF quant              | Try a higher GGUF quant for BaseModel (eg. use flux_kontext:`Q8_0`)      |
| Low Prompt Adherence                             | Low DreamOmni2 GGUF quant              | Try a higher GGUF quant for DreamOmni2 (eg. use DreamOmni2-GGUF:`Q8_0`)  |
|Slow generation                                   | CPU fallback.                          | Compile llama-cpp-python with CUDA for GPU acceleration.|

---

## 🗒️ Notes

* Requires **ComfyUI ≥ 0.3.66**.
* Tested on **Python 3.12** and **Windows 11**.
* GPU recommended for large GGUFs.
* Original model licensing applies — this node only provides an interface.

---

## 📜 License

Refer to the original model and `llama.cpp` licenses.
This node does not modify or supersede any upstream licensing.

---

