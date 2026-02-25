[![CI](https://img.shields.io/github/actions/workflow/status/ExoticArts/comfyui-ea-nodes/ci.yml?branch=main&label=CI)](https://github.com/ExoticArts/comfyui-ea-nodes/actions/workflows/ci.yml)

# ComfyUI EA Nodes

Compact, user-friendly **LoRA stacking** nodes for ComfyUI. Designed to work cleanly with **WAN 2.2** video workflows and with **SD/SDXL/Flux** text-encoder pipelines.

---

## What’s inside

- **EA Power LoRA** — stack multiple LoRAs onto the **MODEL only** (no CLIP).
- **EA Power LoRA +CLIP** — stack LoRAs onto **MODEL** and **CLIP**.
- **EA Power LoRA WanVideo** — stack LoRAs using **WanVideoWrapper** style sockets (`prev_lora` / `blocks` → `lora`) so WAN 2.2 graphs stay compact.
- **EA Trim Frames** — trim frames from the start/end of an image sequence and return first/last previews + frame count.
- **EA Filename → Combine** — build a friendly filename prefix and full-path stub (with an optional “trigger” string to avoid cache collisions).

All LoRA pickers list files from `ComfyUI/models/loras` (falls back to a text box if the list can’t be fetched). Missing LoRAs are safely ignored at runtime.

---

## Nodes

### EA Power LoRA

Apply one or more LoRAs to the **MODEL only** (no CLIP path).

**Use this when:** your pipeline has no text-encoder/CLIP path (e.g., **WAN 2.2** UNet-only branches).

**Wiring**
```

\[Model Loader] → (model) → \[EA Power LoRA] → (model) → \[…]

```

---

### EA Power LoRA +CLIP

Apply one or more LoRAs to **MODEL** and **CLIP**.

**Use this when:** your pipeline includes a text encoder (e.g., **SD/SDXL/Flux**).  
To make a LoRA model-only, set its **CLIP** weight to **0.00**.

**Wiring**
```

\[Checkpoint Loader] → (model, clip) → \[EA Power LoRA +CLIP] → (model, clip) → \[…]

```

---

### EA Power LoRA WanVideo

A WanVideo-compatible variant that takes `prev_lora` and `blocks`, and outputs a stacked `lora`. Combine many LoRAs in a single node to keep WAN 2.2 graphs tidy.

**Use this when:** you’re wiring **WanVideoWrapper** nodes and want stackable LoRAs without a long chain of single-LoRA nodes.

**Wiring (typical WAN 2.2)**
```

\[WanVideo Lora Select] → (prev\_lora, blocks) → \[EA Power LoRA WanVideo] → (lora) → \[WanVideo Set LoRAs]

````

You can place separate WanVideo stacks for “high” and “low” groups just like you would with the native nodes.

---

## UI at a glance

- **＋ Add LoRA** — add a row.
- **✓** — enable/disable a row.
- **LoRA** — file from `/models/loras` (or type a name).
- **Weight** — UNet/model weight (left-aligned, two decimals).
- **CLIP** — text-encoder weight (shown only on **+CLIP**).
- **×** — remove the row.

The header row appears only when you have at least one LoRA.

---

## Notes & tips

- **Which node when**
  - **WAN 2.2:** use **EA Power LoRA** (or **EA Power LoRA WanVideo** if you’re using WanVideoWrapper blocks).
  - **SD/SDXL/Flux:** use **EA Power LoRA +CLIP**.
- **Order of LoRAs**  
  LoRA application is additive; order **does not change** the result.
- **Trigger words**  
  Many style LoRAs work fine with CLIP low/off; character/concept LoRAs often benefit from some CLIP weight.
- **Performance**  
  Each LoRA adds memory/compute overhead. If you stack many, consider reducing precision or VRAM usage elsewhere.

---

## Advanced: JSON payload (saved in workflows)

Each node serializes its rows to a hidden `loras_json` field. You normally don’t need this, but it’s useful for debugging or scripting.

**MODEL-only / WanVideo**
```json
{
  "rows": [
    { "enabled": true, "name": "foo.safetensors", "strength_model": 1.00 }
  ]
}
````

**MODEL + CLIP**

```json
{
  "rows": [
    { "enabled": true, "name": "bar.safetensors", "strength_model": 1.00, "strength_clip": 1.00 }
  ]
}
```

Unknown names are ignored at execution time.

---

## Utility nodes

### EA Trim Frames

Remove frames from the start/end of an image sequence.

**Inputs**

* `images` (IMAGE)
* `skip_first` (INT)
* `skip_last` (INT)

**Outputs**

* `images` (trimmed sequence)
* `first_frame` (IMAGE)
* `last_frame` (IMAGE)
* `frame_count` (INT)

Great for tightening loops and cleaning ping-pong segments.

---

### EA Filename → Combine

Build a folder + filename stem for saving outputs, with an optional **video\_info** string to make unique, cache-safe names.

**Outputs**

* `prefix_for_combine` — a Comfy-friendly prefix
* `fullpath_stub` — absolute path without extension

---

## Install

**Comfy Manager / Registry:** search `comfyui-ea-nodes` and install.

**Manual**

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ExoticArts/comfyui-ea-nodes
# Restart ComfyUI and hard refresh the browser (Ctrl/Cmd+Shift+R)
```

---

## License

See [LICENSE](LICENSE).

```
::contentReference[oaicite:0]{index=0}
```
