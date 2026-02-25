# ComfyUI-Polymath-Vibenodes

<img width="1280" height="720" alt="Custom Vibe" src="https://github.com/user-attachments/assets/9aedba75-b2ee-4688-8e66-35977b49908a" />


## Polymath JSON Prompt

A custom ComfyUI node that lets you make auto json prompts with a simple placeholder templating syntax, while automatically creating **dynamic input ports** for any referenced placeholders.


### Why

Чтобы автоматизировать json промпты, работая с n8n и создавая dataset for lora with qwen-edit in one click

<img width="420" height="420" alt="polymath json node" src="https://github.com/user-attachments/assets/0f1cfd41-a19b-406d-a517-fa36daa0335d" />


<img width="690" height="420" alt="panda example" src="https://github.com/user-attachments/assets/84f59aba-e121-4ed1-935d-eb130baec933" />
<img width="690" height="420" alt="panda salto" src="https://github.com/user-attachments/assets/f0b88386-9de0-4e23-a7ac-b5b71a26c389" />

### Node

- **Name**: Polymath JSON Prompt
- **Category**: Polymath
- **Output**: `STRING` (pretty-printed valid JSON)

### Placeholder syntax

Use placeholders **without quotes**:

```json
{
  "scene": {{ $json['scene'].prompt }},
  "identity": {{ $json['identity'].prompt }}
}
```

Rules:

- Placeholders are matched by the pattern:

  `{{ $json['KEY'].prompt }}`

- `KEY` becomes a **dynamic input port** on the node.
- The incoming value is treated as a **string**, JSON-escaped, and inserted into the template.
- The final rendered result is validated with `json.loads()`.
  If it is not valid JSON, the node throws an error.

### Example template

```json
{
  "scene": {{ $json['scene'].prompt }},
  "character": [
    {
      "identity": {{ $json['identity'].prompt }},
      "pose": {{ $json['pose'].prompt }},
      "dress": {{ $json['dress'].prompt }},
      "emotion": {{ $json['emotion'].prompt }},
      "action": {{ $json['action'].prompt }}
    }
  ],
  "style": "...",
  "lighting": "...",
  "mood": "...",
  "camera": {
    "angle": "high angle",
    "distance": "medium shot",
    "focus": "Sharp focus on ... in frame",
    "lens-mm": 85,
    "f-number": "f/5.6",
    "ISO": 200
  }
}
```

### Install

1. Manual git clone into ComfyUI/custom_nodes:

   ```
   git clone https://github.com/polymath-wtf/ComfyUI-Polymath-Vibenodes.git
   ```

3. Restart UI.

### Development notes

- First VibeNode&VibeCode, Enjoy
- Backend is implemented using the ComfyUI V3 API (`comfy_api.latest.IO`). v3? wtf? idk


