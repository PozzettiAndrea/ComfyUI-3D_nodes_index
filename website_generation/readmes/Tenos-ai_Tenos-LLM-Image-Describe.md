# Tenos.ai LLM Image Describe

A swiss‑army ComfyUI node that lets **any** vision‑capable LLM (OpenAI GPT‑4o, Gemini 1.5 Pro Vision, Groq‑mix… you name it) rip through a reference image and return a prompt you can feed straight back into your diffusion pipeline—no hand‑crafting required.&#x20;

---

## Why you’ll want it

| ⚡   | **Auto‑prompt in three flavors** – “Style”, “Subject”, or “Describe” modes let you yank out pure style cues, pure content, or a balanced mix—all enforced by detailed system prompts baked into the node.                                                 |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔑  | **API‑key juggling** – Reads keys from `api_keys.json`, but you can hot‑swap a key per‑node at runtime if you’ve got a second account (or if someone else is paying).                                                                                     |
| 🖼️ | **Hash‑based caching** – It won’t re‑hit the LLM unless the image or model settings change, saving your tokens (and sanity).                                                                                                                              |
| 🧩  | **CLIP‑agnostic conditioning** – Detects whatever encoding method your CLIP loader exposes (`encode_from_tokens`, `encode_conditioning`, `encode`, `encode_text`, or even a bare callable) and formats the output so the rest of your graph stays happy.  |
| 🚑  | **Fails graceful‑ish** – No API key? Vision‑less model? Timeout? You get meaningful error text (and a blank conditioning tensor so the graph doesn’t hard‑crash).                                                                                         |

---

## File roster

```
custom_nodes/tenos_nodes/
├─ llm_describe_node.py          ← the node itself
├─ llm_models.json               ← list of provider → model names
└─ api_keys.json                 ← stash your secrets here (optional)
```

Both JSON helpers are optional but highly recommended—skip them and you’ll feed keys/models manually.&#x20;

---

## Quick install

```bash
# Inside your ComfyUI install:
mkdir -p custom_nodes/tenos_nodes
cp llm_describe_node.py llm_models.json api_keys.json custom_nodes/tenos_nodes/
# restart ComfyUI
```

> **Heads‑up:** the file expects to sit next to its two JSON sidekicks. If you rename the folder, update the import path in the code (line right after the imports).&#x20;

---

## JSON cheat‑sheets

### `api_keys.json`

```jsonc
{
  "openai_api_key":  "sk‑...",
  "google_api_key":  "AIza...",
  "groq_api_key":    "gsk_..."
}
```

Keys map 1‑to‑1 with provider names via an internal lookup table.&#x20;

### `llm_models.json`

```jsonc
{
  "providers": {
    "openai":  { "models": ["gpt-4o-mini", "gpt-4o-vision-preview"] },
    "gemini":  { "models": ["gemini-pro-vision", "gemini-1.5-pro"] },
    "groq":    { "models": ["llama-3-70b-vision"] }
  }
}
```

Anything not listed still works—type the full model string into the node’s dropdown or override box. The JSON just keeps the UI tidy.&#x20;

---

## Node I/O spec

| **Field**                       | **Type / UI**                    | **Description**                                                         |
| ------------------------------- | -------------------------------- | ----------------------------------------------------------------------- |
| `clip`                          | **CLIP**                         | Your text encoder. The node figures out how to talk to it.              |
| `image`                         | **IMAGE**                        | 4‑D tensor `(B,H,W,C)` from any loader.                                 |
| `llm_provider`                  | dropdown                         | Values sourced from `llm_models.json`; `"None"` skips the call.         |
| `llm_model`                     | dropdown                         | `"provider: model"` strings; editable.                                  |
| `description_mode`              | `["Style","Subject","Describe"]` | System‑prompt preset.                                                   |
| `auto_describe_on_image_change` | boolean                          | If **false**, you must nudge the node (toggle a field) to refresh.      |
| `override_api_key`              | string (optional)                | Beats whatever’s in `api_keys.json` for this one call.                  |
| **Returns**                     | `CONDITIONING`                   | List `[[embeddings, {"pooled_output": pooled}]]` ready for SDXL / Flux. |

---

## Example ComfyUI graph (pseudo)

```
Loader → Tenos LLM Image Describe (Style, GPT‑4o‑mini) → SDXL Style LO → Merge → ...
```

Or go all‑in:

```
Loader → Split → Tenos LLM Image Describe (Subject) ─┐
         |                                          ├→ Combine Conditioning → Diffusion
         └→ Tenos LLM Image Describe (Style) ───────┘
```

---

## Pro tips

* **Batching:** Node loops images internally, hitting the LLM once per frame. Keep batches small if you value tokens.
* **Model sanity:** Some providers don’t expose vision models yet. If you point “groq: llama‑3‑70b” at a JPEG, it’ll just ignore the picture and hallucinate—watch the console warnings.&#x20;
* **Clip weirdness:** If your custom CLIP lacks pooled output, Flux will still run—just with less global juice.

---

## Troubleshooting crib notes

| Symptom                                                         | Likely Cause                                                   | Fix                                                       |
| --------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| `Error: No API key provided…` in prompt output                  | Empty `api_keys.json` or bad override field                    | Paste key, restart                                        |
| Node prints `Unknown LLM provider`                              | Typo in dropdown or JSON                                       | Match provider names exactly (`openai`, `gemini`, `groq`) |
| Blank conditioning but no error                                 | `auto_describe_on_image_change` is **off** and nothing toggled | Tweak any field or feed a new image                       |
| `CLIP object … does not have a recognized text encoding method` | You forgot a CLIP loader                                       | Add a CLIP‑Loader node upstream                           |

---

Made with love and a dash of “why hasn’t ComfyUI done this yet?” ✨
