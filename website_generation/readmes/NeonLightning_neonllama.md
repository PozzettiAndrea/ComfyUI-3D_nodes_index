# 🧠 NeonLLama ComfyUI Extension

**NeonLLama** is a custom ComfyUI node that transforms one or more **idea lines** into vivid, richly detailed prompts using a local LLM — either through [Ollama](https://ollama.com) or [LM Studio](https://lmstudio.ai). It supports **avoid** content to guide generation and returns that list as the **negative prompt**.

---

## 🚀 Features

* 🧠 Converts simple ideas into rich, structured **positive prompts**.
* ✂️ Supports **multi-line input** — each idea line generates its own prompt.
* ⛔ Optional "avoid" list used to steer generation and returned as the negative prompt.
* 🔁 Retries with smart temperature adaptation to meet token targets.
* 🧮 Accurate token estimation using model-specific tokenizers.
* ⚙️ Fully configurable: model choice, token bounds, retry limits, and regeneration control.
* 🖨️ Logs all prompts and supports forced regeneration.

---

## 🧩 How It Works

1. Input one or more **idea lines** (line breaks separate them).
2. Optionally include **avoid terms** to bias generation away from undesired concepts.
3. The node:

   * Attempts generation using your configured local model.
   * Retries if the output is too short or too long.
   * Logs inputs and outputs.
4. Outputs include the final **positive prompt**, your **avoid list**, and original **idea**.

---

## 📤 Outputs

| Output     | Type   | Description                                            |
| ---------- | ------ | ------------------------------------------------------ |
| `prompt`   | STRING | Combined positive prompt(s), separated with `BREAK`.   |
| `negative` | STRING | Direct copy of avoid input, used as negative prompt.   |
| `idea`     | STRING | Original idea input, for UI traceability or debugging. |

---

## 📥 Inputs / Configuration Fields

| Name                | Type     | Description                                                      |
| ------------------- | -------- | ---------------------------------------------------------------- |
| `model`             | Dropdown | Select the model name to use (fetched from the running backend). |
| `idea`              | Text     | One idea per line. Each generates a separate prompt.             |
| `negative`          | Text     | Words to avoid — passed to model + used as negative prompt.      |
| `max_tokens`        | Int      | Upper bound for output tokens (default: 75, max: 231).           |
| `min_tokens`        | Int      | Lower bound for meaningful output (default: 50).                 |
| `max_attempts`      | Int      | How many times to retry if generation doesn’t meet criteria.     |
| `regen_on_each_use` | Bool     | Forces regeneration on every run, even with unchanged input.     |

---

## 🧪 Example

**Inputs:**

```text
idea:
    haunted subway station with broken lights

avoid:
    blood, gore, screaming
```

**Outputs:**

```text
prompt:
    dark abandoned subway, flickering fluorescent lights, cracked tiled walls, shadowy corners, old train cars, graffiti-covered pillars, dim green glow, debris scattered floor

negative:
    blood, gore, screaming
```

---

## 🔁 Token-Aware Generation

* Token count estimated using model-specific tokenizer.
* Retries generation using adaptive temperature — starts hot and cools with each failure.
* Adjusts prompt by trimming or elaborating until token limits are satisfied.
* Prompts too short or too long are discarded unless they fall within the required range.

---

## 🔒 Robust Logging

* Logs prompts and failures to disk for traceability.
* Logs include selected model, prompt source, token counts, and generation time.

---

## 🧠 Smart Prompt Structuring

Prompts follow rules enforced via system instructions to the model:

* Use **short, visually descriptive phrases**, not sentences.
* Avoid storytelling, abstract descriptions, or emotion-driven language.
* Keep outputs grounded and aligned with original idea’s visual core.
* Connect elements with simple language: “with”, “under”, “surrounded by”, etc.
* Avoid repetition, overgeneralization, or verbose commentary.

---

## 🛠️ Requirements

* At least one of:

  * [Ollama](https://ollama.com) running at `http://localhost:11434`
  * [LM Studio](https://lmstudio.ai) running with JIT server enabled
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI) installed and functional
* Python packages:

  * `requests`
  * `tokenizers`
  * `lmstudio` (only required for LM Studio support)

---

## 📄 License

MIT License

---

## ❤️ Credits

Built by Neon Lightning ⚡
Powered by open-source local LLMs, punk energy, and rat affection 🐀