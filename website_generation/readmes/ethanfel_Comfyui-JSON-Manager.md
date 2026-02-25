<p align="center">
  <svg xmlns="http://www.w3.org/2000/svg" width="480" height="100" viewBox="0 0 480 100">
    <defs>
      <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
        <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
      </linearGradient>
      <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" style="stop-color:#e94560" />
        <stop offset="100%" style="stop-color:#0f3460" />
      </linearGradient>
    </defs>
    <rect width="480" height="100" rx="16" fill="url(#bg)" />
    <rect x="20" y="72" width="440" height="3" rx="1.5" fill="url(#accent)" opacity="0.6" />
    <text x="240" y="36" text-anchor="middle" fill="#e94560" font-family="monospace" font-size="13" font-weight="bold">{ JSON }</text>
    <text x="240" y="60" text-anchor="middle" fill="#eee" font-family="sans-serif" font-size="22" font-weight="bold">ComfyUI JSON Manager</text>
    <text x="240" y="90" text-anchor="middle" fill="#888" font-family="sans-serif" font-size="11">Visual dashboard &amp; dynamic nodes for AI video workflows</text>
  </svg>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-green" alt="Python" />
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-red" alt="Streamlit" />
  <img src="https://img.shields.io/badge/ComfyUI-Custom%20Nodes-purple" alt="ComfyUI" />
</p>

A visual dashboard for managing, versioning, and batch-processing JSON configuration files used in AI video generation workflows (I2V, VACE). Two parts:

1. **Streamlit Web Interface** &mdash; Dockerized editor for prompts, LoRAs, settings, and branching history
2. **ComfyUI Custom Nodes** &mdash; Read JSON files directly into workflows, including a dynamic node that auto-discovers keys

---

## Features

<table>
<tr>
<td width="50%">

<h3>
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><rect width="20" height="20" rx="4" fill="#e94560"/><text x="10" y="14" text-anchor="middle" fill="#fff" font-size="11">B</text></svg>
Batch Processor
</h3>

- Unlimited sequences within a single JSON file
- Import settings from any file or history entry
- Per-shot custom keys (e.g. Shot 1: `fog: 0.5`, Shot 2: `fog: 0.0`)
- Clone, reorder, and manage sequences visually
- Conflict protection against external file modifications
- Snippet library for reusable prompt fragments

</td>
</tr>
<tr>
<td width="50%">

<h3>
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><rect width="20" height="20" rx="4" fill="#533483"/><text x="10" y="14" text-anchor="middle" fill="#fff" font-size="11">T</text></svg>
Visual Timeline
</h3>

- Git-style branching with horizontal node graph
- Non-destructive: forking on old-version edits preserves all history
- Visual diff highlighting changes between any two versions
- Restore any past state with one click

</td>
<td width="50%">

<h3>
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><rect width="20" height="20" rx="4" fill="#2b9348"/><text x="10" y="14" text-anchor="middle" fill="#fff" font-size="11">D</text></svg>
Dynamic Node (New)
</h3>

- Auto-discovers all JSON keys and exposes them as outputs
- No code changes needed when JSON structure evolves
- Preserves connections when keys are added on refresh
- Native type handling: `int`, `float`, `string`

</td>
</tr>
</table>

---

## Installation

### 1. Unraid / Docker (Streamlit Manager)

```bash
# Repository: python:3.12-slim
# Network: Bridge
# WebUI: http://[IP]:[PORT:8501]
```

**Path Mappings:**
| Container | Host | Purpose |
|:---|:---|:---|
| `/app` | `/mnt/user/appdata/ai-manager/` | App files |
| `/mnt/user/` | `/mnt/user/` | Project data / JSON location |

**Post Arguments:**
```bash
/bin/sh -c "apt-get update && apt-get install -y graphviz && \
  pip install streamlit opencv-python-headless graphviz streamlit-agraph && \
  cd /app && streamlit run app.py --server.headless true --server.port 8501"
```

### 2. ComfyUI (Custom Nodes)

```bash
cd ComfyUI/custom_nodes/
git clone <this-repo> ComfyUI-JSON-Manager
# Restart ComfyUI
```

---

## ComfyUI Nodes

### Node Overview

<!--
  Diagram: shows JSON file flowing into different node types
-->
<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="280" viewBox="0 0 720 280">
  <defs>
    <linearGradient id="nodeBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#2d2d3d" />
      <stop offset="100%" style="stop-color:#1e1e2e" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="1" dy="2" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>

  <!-- JSON File -->
  <rect x="10" y="100" width="120" height="60" rx="8" fill="#0f3460" filter="url(#shadow)" />
  <text x="70" y="125" text-anchor="middle" fill="#aaa" font-family="monospace" font-size="10">batch_prompt</text>
  <text x="70" y="142" text-anchor="middle" fill="#fff" font-family="monospace" font-size="13" font-weight="bold">.json</text>

  <!-- Arrow -->
  <line x1="130" y1="130" x2="170" y2="130" stroke="#555" stroke-width="2" marker-end="url(#arrowhead)"/>
  <defs><marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#555"/></marker></defs>

  <!-- Dynamic Node -->
  <rect x="180" y="20" width="200" height="70" rx="10" fill="url(#nodeBg)" stroke="#2b9348" stroke-width="2" filter="url(#shadow)" />
  <text x="280" y="44" text-anchor="middle" fill="#2b9348" font-family="sans-serif" font-size="12" font-weight="bold">JSON Loader (Dynamic)</text>
  <text x="280" y="62" text-anchor="middle" fill="#888" font-family="monospace" font-size="10">auto-discovers keys</text>
  <text x="280" y="78" text-anchor="middle" fill="#666" font-family="monospace" font-size="9">click Refresh to populate</text>

  <!-- Batch I2V Node -->
  <rect x="180" y="105" width="200" height="50" rx="10" fill="url(#nodeBg)" stroke="#e94560" stroke-width="2" filter="url(#shadow)" />
  <text x="280" y="127" text-anchor="middle" fill="#e94560" font-family="sans-serif" font-size="12" font-weight="bold">JSON Batch Loader (I2V)</text>
  <text x="280" y="144" text-anchor="middle" fill="#888" font-family="monospace" font-size="10">prompts, flf, seed, paths</text>

  <!-- Batch VACE Node -->
  <rect x="180" y="170" width="200" height="50" rx="10" fill="url(#nodeBg)" stroke="#533483" stroke-width="2" filter="url(#shadow)" />
  <text x="280" y="192" text-anchor="middle" fill="#533483" font-family="sans-serif" font-size="12" font-weight="bold">JSON Batch Loader (VACE)</text>
  <text x="280" y="209" text-anchor="middle" fill="#888" font-family="monospace" font-size="10">+ vace frames, schedule</text>

  <!-- Custom Nodes -->
  <rect x="180" y="235" width="200" height="40" rx="10" fill="url(#nodeBg)" stroke="#0f3460" stroke-width="2" filter="url(#shadow)" />
  <text x="280" y="260" text-anchor="middle" fill="#0f3460" font-family="sans-serif" font-size="12" font-weight="bold">JSON Loader (Custom 1/3/6)</text>

  <!-- Output labels -->
  <line x1="380" y1="55" x2="420" y2="55" stroke="#2b9348" stroke-width="1.5"/>
  <text x="430" y="47" fill="#aaa" font-family="monospace" font-size="9">general_prompt</text>
  <text x="430" y="59" fill="#aaa" font-family="monospace" font-size="9">seed (int)</text>
  <text x="430" y="71" fill="#aaa" font-family="monospace" font-size="9">my_custom_key ...</text>

  <line x1="380" y1="130" x2="420" y2="130" stroke="#e94560" stroke-width="1.5"/>
  <text x="430" y="127" fill="#aaa" font-family="monospace" font-size="9">general_prompt, camera,</text>
  <text x="430" y="139" fill="#aaa" font-family="monospace" font-size="9">flf, seed, paths ...</text>

  <line x1="380" y1="195" x2="420" y2="195" stroke="#533483" stroke-width="1.5"/>
  <text x="430" y="192" fill="#aaa" font-family="monospace" font-size="9">+ frame_to_skip, vace_schedule,</text>
  <text x="430" y="204" fill="#aaa" font-family="monospace" font-size="9">input_a_frames ...</text>

  <line x1="380" y1="255" x2="420" y2="255" stroke="#0f3460" stroke-width="1.5"/>
  <text x="430" y="259" fill="#aaa" font-family="monospace" font-size="9">manual key lookup (1-6 slots)</text>
</svg>
</p>

### Dynamic Node

The **JSON Loader (Dynamic)** node reads your JSON file and automatically creates output slots for every key it finds. No code changes needed when your JSON structure evolves.

**How it works:**
1. Enter a `json_path` and `sequence_number`
2. Click **Refresh Outputs**
3. Outputs appear named after JSON keys, with native types preserved

<p align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="240" viewBox="0 0 500 240">
  <defs>
    <linearGradient id="dynBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#353545" />
      <stop offset="100%" style="stop-color:#252535" />
    </linearGradient>
  </defs>

  <!-- Node body -->
  <rect x="20" y="10" width="240" height="220" rx="10" fill="url(#dynBg)" stroke="#2b9348" stroke-width="2" />
  <rect x="20" y="10" width="240" height="28" rx="10" fill="#2b9348" />
  <rect x="20" y="28" width="240" height="10" fill="#2b9348" />
  <text x="140" y="31" text-anchor="middle" fill="#fff" font-family="sans-serif" font-size="13" font-weight="bold">JSON Loader (Dynamic)</text>

  <!-- Inputs -->
  <text x="35" y="60" fill="#ccc" font-family="monospace" font-size="10">json_path: /data/prompt.json</text>
  <text x="35" y="78" fill="#ccc" font-family="monospace" font-size="10">sequence_number: 1</text>

  <!-- Refresh button -->
  <rect x="45" y="88" width="190" height="24" rx="5" fill="#2b9348" opacity="0.3" stroke="#2b9348" stroke-width="1"/>
  <text x="140" y="104" text-anchor="middle" fill="#2b9348" font-family="sans-serif" font-size="11" font-weight="bold">Refresh Outputs</text>

  <!-- Output slots -->
  <circle cx="260" cy="130" r="5" fill="#6bcb77"/>
  <text x="245" y="134" text-anchor="end" fill="#ccc" font-family="monospace" font-size="10">general_prompt</text>

  <circle cx="260" cy="150" r="5" fill="#6bcb77"/>
  <text x="245" y="154" text-anchor="end" fill="#ccc" font-family="monospace" font-size="10">negative</text>

  <circle cx="260" cy="170" r="5" fill="#4d96ff"/>
  <text x="245" y="174" text-anchor="end" fill="#ccc" font-family="monospace" font-size="10">seed</text>

  <circle cx="260" cy="190" r="5" fill="#ff6b6b"/>
  <text x="245" y="194" text-anchor="end" fill="#ccc" font-family="monospace" font-size="10">flf</text>

  <circle cx="260" cy="210" r="5" fill="#6bcb77"/>
  <text x="245" y="214" text-anchor="end" fill="#ccc" font-family="monospace" font-size="10">camera</text>

  <!-- Connection lines to downstream -->
  <line x1="265" y1="130" x2="340" y2="130" stroke="#6bcb77" stroke-width="1.5"/>
  <line x1="265" y1="170" x2="340" y2="165" stroke="#4d96ff" stroke-width="1.5"/>

  <!-- Downstream node -->
  <rect x="340" y="115" width="140" height="65" rx="8" fill="url(#dynBg)" stroke="#555" stroke-width="1.5" />
  <text x="410" y="137" text-anchor="middle" fill="#aaa" font-family="sans-serif" font-size="11">KSampler</text>
  <circle cx="340" cy="130" r="4" fill="#6bcb77"/>
  <text x="350" y="150" fill="#777" font-family="monospace" font-size="9">positive</text>
  <circle cx="340" cy="165" r="4" fill="#4d96ff"/>
  <text x="350" y="170" fill="#777" font-family="monospace" font-size="9">seed</text>

  <!-- Legend -->
  <circle cx="30" y="248" r="4" fill="#6bcb77"/>
  <text x="40" y="252" fill="#888" font-family="monospace" font-size="9">STRING</text>
  <circle cx="100" y="248" r="4" fill="#4d96ff"/>
  <text x="110" y="252" fill="#888" font-family="monospace" font-size="9">INT</text>
  <circle cx="155" y="248" r="4" fill="#ff6b6b"/>
  <text x="165" y="252" fill="#888" font-family="monospace" font-size="9">FLOAT</text>
</svg>
</p>

**Type handling:** Values keep their native Python type &mdash; `int` stays `int`, `float` stays `float`, booleans become `"true"`/`"false"` strings, everything else becomes `string`. The `*` (any) output type allows connecting to any input.

**Refreshing is safe:** Clicking Refresh after adding new keys to your JSON preserves all existing connections. Only removed keys get disconnected.

### Standard & Batch Nodes

| Node | Outputs | Use Case |
|:---|:---|:---|
| **JSON Loader (Standard/I2V)** | prompts, flf, seed, paths | Single-file I2V workflows |
| **JSON Loader (VACE Full)** | above + VACE integers | Single-file VACE workflows |
| **JSON Loader (LoRAs Only)** | 6 LoRA strings | Single-file LoRA loading |
| **JSON Batch Loader (I2V)** | prompts, flf, seed, paths | Batch I2V with sequence_number |
| **JSON Batch Loader (VACE)** | above + VACE integers | Batch VACE with sequence_number |
| **JSON Batch Loader (LoRAs)** | 6 LoRA strings | Batch LoRA loading |
| **JSON Loader (Custom 1/3/6)** | 1, 3, or 6 string values | Manual key lookup by name |

---

## Web Interface Usage

Navigate to your container's IP (e.g., `http://192.168.1.100:8501`).

**Path navigation** supports case-insensitive matching &mdash; typing `/media/P5/myFolder` will resolve to `/media/p5/MyFolder` automatically.

- **Custom Parameters:** Scroll to "Custom Parameters" in any editor tab. Type a key and value, click Add.
- **Timeline:** Switch to the Timeline tab to see version history as a graph. Restore any version, and new edits fork a branch automatically.
- **Snippets:** Save reusable prompt fragments and append them with one click.

---

## JSON Format

```jsonc
{
  "batch_data": [
    {
      "sequence_number": 1,
      "general_prompt": "A cinematic scene...",
      "negative": "blurry, low quality",
      "seed": 42,
      "flf": 0.5,
      "camera": "pan_left",
      "video file path": "/data/input.mp4",
      "reference image path": "/data/ref.png",
      "my_custom_key": "any value"
      // ... any additional keys are auto-discovered by the Dynamic node
    }
  ]
}
```

---

## File Structure

```
ComfyUI-JSON-Manager/
├── __init__.py            # ComfyUI entry point, exports nodes + WEB_DIRECTORY
├── json_loader.py         # All ComfyUI node classes + /json_manager/get_keys API
├── web/
│   └── json_dynamic.js    # Frontend extension for Dynamic node (refresh, show/hide)
├── app.py                 # Streamlit main entry point & navigator
├── utils.py               # I/O, config, defaults, case-insensitive path resolver
├── history_tree.py        # Git-style branching engine
├── tab_batch.py           # Batch processor UI
├── tab_timeline.py        # Visual timeline UI
├── tab_comfy.py           # ComfyUI server monitor
├── tab_raw.py             # Raw JSON editor
└── tests/
    ├── test_json_loader.py
    ├── test_utils.py
    └── test_history_tree.py
```

---

## License

[Apache 2.0](LICENSE)
