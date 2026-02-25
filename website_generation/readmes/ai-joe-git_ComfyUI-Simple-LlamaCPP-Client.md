# ComfyUI-Simple-LlamaCPP-Client

A lightweight custom node for **ComfyUI** that connects directly to a local **llama.cpp OpenAI-compatible server**.

It supports:

- 💬 Chat completions (`/v1/chat/completions`)
- 🖼 Vision models (image + prompt input)
- ⚡ Streaming mode (SSE token accumulation)
- 🧠 Clean Answer + Thinking separation
- 📦 Optional JSON-only output mode
- 🔑 Optional API key authentication
- 🎛 Minimal design (server-side parameters stay server-side)

---

## ✨ Features

✅ Works with any OpenAI-compatible llama.cpp server  
✅ Supports **system prompt + user prompt**  
✅ Optional **image input** for multimodal models  
✅ Outputs: Answer, Thinking, JSON, Raw, Model Used  
✅ Auto-detects model from `/v1/models`  
✅ Clean dropdown UI (no ugly free-text params)

---

## 📦 Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ai-joe-git/ComfyUI-Simple-LlamaCPP-Client.git
```

Restart ComfyUI.

---

## 🚀 Server Example

```bat
llama-server.exe ^
  -m Ministral-3-8B-Instruct.gguf ^
  --host 127.0.0.1 ^
  --port 8082 ^
  --mmproj mmproj.gguf ^
  -c 8192
```

---

## 🧩 Node Inputs

| Input | Description |
|------|------------|
| `server_url` | llama.cpp server URL (default: `http://127.0.0.1:8082`) |
| `prompt` | User message text |
| `system_prompt` | Optional system instruction |
| `image` | Optional IMAGE input (vision models) |
| `api_key` | Optional Bearer token |

### Model Selection

| Input | Description |
|------|------------|
| `model_mode` | Dropdown: `auto` / `custom` |
| `model_override` | Only used if `model_mode = custom` |

### Stop Control

| Input | Description |
|------|------------|
| `stop_mode` | Dropdown: `none`, `preset:common_eot`, `preset:triple_hash`, `custom` |
| `stop_custom` | Used only if stop_mode = custom |

### Text Cleanup

| Input | Description |
|------|------------|
| `text_postprocess` | Dropdown: `fix_mojibake`, `none`, `ascii_quotes`, `fix_mojibake+ascii_quotes` |

(Default fixes `Hereâs` → `Here’s`)

---

## 📤 Node Outputs

| Output | Description |
|-------|------------|
| `answer` | Final cleaned answer |
| `thinking` | Reasoning if provided |
| `json` | Parsed JSON output (if enabled) |
| `raw` | Full raw server response |
| `model_used` | Model name used |

---

## 📜 License

MIT License.
