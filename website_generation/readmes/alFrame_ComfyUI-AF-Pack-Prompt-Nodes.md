# AF - Pack Prompt Nodes

A lightweight suite of ComfyUI custom nodes for AI prompt management and history tracking.

## 📦 What's Included

**[AF - Edit Generated Prompt](#af---edit-generated-prompt)** - Receive LLM-generated prompts and optionally edit them manually  
**[AF - Save Prompt History](#af---save-prompt-history)** - Archive prompts to JSON files with timestamps  
**[AF - Load Prompt History](#af---load-prompt-history)** - Browse and load previous prompts by index  
**[AF - Show Text](#af---show-text)** - Simple node that displays the connected text  
**[AF - Model Switch](#af---model-switch)** - A dynamic model/clip/vae switching node

---

## 🚀 Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "AF - Pack Prompt Nodes"
3. Install

### Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes.git
```

---

## AF - Edit Generated Prompt

**Purpose:** Pipe LLM output through your workflow with optional manual editing.

### How It Works
- **Upper field** (read-only, grayed): Displays incoming prompt from LLM
- **Lower field** (editable): Manual input or edited version
- **Output priority**: Lower field → Upper field → Empty string

**Key Feature:** Click "Copy Generated Prompt for Editing" to move prompt from upper to lower field for modifications.

<img width="1890" height="919" alt="AF - Edit Generated Prompt" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Edit_Generated_Prompt_Node.png" />

### Typical Usage
```
[Ollama/LLM Node] → [AF - Edit Generated Prompt] → [CLIP Text Encode]
```

<img width="2095" height="521" alt="AF - Edit Generated Prompt - Workflow Download" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Edit_Generated_Prompt_Workflow_Example.png" />

[Download example workflow](https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/example_workflows/AF-Edit_Generated_Prompt.json) (right click -> save as...)

#### Short Video

https://github.com/user-attachments/assets/f16e0324-ddad-41fd-92a9-860cac2d02e3

[Watch the Video on Youtube in higher Resolution](https://www.youtube.com/watch?v=VJmRcnJ60fc)   

#### Video of "AF - Edit Generated Prompt" in a workflow

<a href="https://youtu.be/H0ZfDIShJLQ">
  <img src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Edit-Generated-Prompt_Workflow_SmallThumb.jpg" width="100%" alt="Click to watch">
</a>

---

## AF - Save Prompt History

**Purpose:** Save up to 4 prompts per entry with automatic timestamps.

<img width="1877" height="609" alt="AF - Save Prompt History" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Save_Prompt_History_Node.png" />

### Inputs
- `directory` - Folder name (default: "Prompt-History")
- `filename` - JSON file name (default: "default")
- `project` - Project identifier (stored as metadata in JSON for reference)
- `global_positive/negative` - Main prompts (optional)
- `local_positive/negative` - Secondary prompts (optional)

<img width="1726" height="679" alt="Af - Save Prompt History - Workflow Download" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Save_Prompt_History_Workflow_Example.png" />

[Download example workflow](https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/example_workflows/AF-Save_and_Load_Prompt_History.json) (right click -> save as...)

### Where Files Are Saved
1. **Primary:** `ComfyUI/output/{directory}/` (user working files)
2. **Fallback:** `{node_pack_folder}/{directory}/` (bundled defaults)

### Output Format
```json
[
  {
    "timestamp": "2025-10-29 14:32:15",
    "project": "MyProject",
    "global_positive": "your prompt",
    "global_negative": "negative prompt",
    "local_positive": "local detail",
    "local_negative": "local negative"
  }
]
```

**Note:** All prompts are automatically cleaned (trailing whitespace removed, internal formatting preserved). The `project` field is stored for your reference but not used for filtering.

### 🔗 Common Workflow Patterns

### AI-Assisted with History Backup with the "AF - Save Prompt History" Node
```
[LLM] → [Edit Prompt] ┬ → [CLIP Encode] → [KSampler]
                      └ → [Save History]
```

---

## AF - Load Prompt History

**Purpose:** Load saved prompts using index-based time-travel through your history.

<img width="1095" height="945" alt="AF - Load Prompt History" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Load_Prompt_History_Node.png" />

### Quick Reference
```
┌─────────────────────────────────┐
│ AF - Load Prompt History        │
├─────────────────────────────────┤
│ directory: [AF-PromptHistory  ] │
│ filename:  [MyProject        ▼] │
│ timestamp_index: [0           ] │
├─────────────────────────────────┤
│ Outputs:                        │
│ • global_positive               │
│ • global_negative               │
│ • local_positive                │
│ • local_negative                │
│ • info (connect to Show Text!)  │
└─────────────────────────────────┘
```

### How It Works
- **Filename dropdown** - Lists all `.json` files in the directory (without .json extension)
- **Index selection** - Choose which timestamp to load (0 = newest)
- **Info output** - Shows selected prompt content and metadata

<img width="1564" height="935" alt="AF - Load Prompt History - Workflow Download" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Load_Prompt_History_Workflow_Example.png" />

[Download example workflow](https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/example_workflows/AF-Save_and_Load_Prompt_History.json) (right click -> save as...)

### Index System
- `0` = Most recent prompt
- `1` = Second most recent
- `2` = Third most recent
- etc.

### Directory Priority
Files in `output/{directory}/` override files in `{node_pack}/{directory}/` with the same name.

### Critical: Connect the Info Output!
Always connect `info` → `Show Text` node to see:
- Currently selected filename and timestamp
- Full content of all 4 prompts being loaded
- Total available timestamps count
- Error messages if index is out of range

### Example Info Display
```
══════════════════════════════════════════════════
  AF - LOAD PROMPT HISTORY
══════════════════════════════════════════════════
📄 Filename: MyProject
📊 Available Timestamps: 205

🔢 SELECTED: [126] | 2025-10-29 | 14:32:15

Global Positive:
A serene mountain landscape at sunset, golden hour lighting...

Global Negative:
ugly, deformed, low quality, blurry

Local Positive:
detailed foreground rocks, wildflowers

Local Negative:
(empty)
```

**Console Output:**
```
AF Load - ✓ Successfully loaded: ID: 126 | 2025-10-29 14:32:15
```

### 🔗 Common Workflow Patterns (suggestions)

### "AF - Load Prompt History" Node, Compare Previous Prompts
```
[Load History: index=0] → [Edit] → [CLIP] ┐
[Load History: index=5] → [Edit] → [CLIP] ├→ [KSampler]
[Load History: index=10]→ [Edit] → [CLIP] ┘
```

### Pattern 3: Multi-File Workflow
```
[Load: FileA.json] → [Edit Global+] → ┐
[Load: FileB.json] → [Edit Local+]  → ├→ [CLIP Encode]
[Load: FileC.json] → [Edit Global-] → ┘
```

---


## 💡 Pro Tips

- **Index 0 is your friend** - Always points to newest prompt
- **Info output shows everything** - See exactly what you loaded
- **Console logging** - Check ID and timestamp confirmation
- **Multiple load nodes** - Each can access different files/indices
- **Workflows persist** - Your selections save with the workflow
- **Project field** - Use it as a mental note when saving, great for manual inspection

---

### AF - Show Text

A very simple node that shows the text connected to the input of the Node

<img width="1052" height="550" alt="AF - Show Text" src="https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/blob/main/Docs/screenshots/AF-Show_Text_Node.png" />


---

## 🔧 Troubleshooting

### Files not appearing in dropdown
- Check ComfyUI console for cache messages
- Verify `.json` files exist in `output/{directory}/`
- Restart ComfyUI to rebuild cache
- Ensure files end with `.json` extension

### Index out of range
- Connect `info` output to Show Text to see available count
- Example: 205 timestamps = valid indices are 0-204
- The info display shows total count at the top

### Prompts not loading
- Ensure filename is selected (not "none")
- Check timestamp_index is within range (see info output)
- Verify JSON file format matches example above
- Look for error messages in console

### Directory not found
- Use relative path from ComfyUI root e.g.: `AF-PromptHistory`
- Or absolute path: `/full/path/to/directory`
- Check folder exists and has read/write permissions

---

## AF - Model Switch

A dynamic model switching node that allows you to toggle between multiple model/CLIP/VAE combinations without rewiring your workflow.

<img width="1067" height="945" alt="image" src="https://github.com/user-attachments/assets/dab5fb34-0161-40ab-97c0-f7280a6ccc74" />
On the left the model switch node with it's 2 default inputs and set to auto (Any Switch node style). On the right with all 10 inputs enabled and rail selection set to use rail 3.

### Features

- **Dynamic Rails**: Add 2-10 model rails on demand
- **Smart AUTO Mode**: Automatically selects the first connected rail
- **1-Based Indexing**: Intuitive numbering (Rail 1, Rail 2, Rail 3...)
- **Permanent Base Rails**: Rails 1-2 never lose connections when adjusting rail count
- **Real-Time Status**: Color-coded display shows active rail instantly
- **Flexible Sizing**: Resizable node that preserves your layout preferences

### How It Works

The Model Switch acts as a gateway for your model pipeline. Instead of maintaining multiple workflow branches or manually reconnecting loaders, you can:

1. Connect multiple checkpoint loaders (or AIO loaders) to different rails
2. Choose which rail to use via the `selected_rail` parameter
3. The node outputs the MODEL, CLIP, and VAE from your selected rail

### Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `number_of_rails` | INT | 2-10 | Number of visible model rails |
| `selected_rail` | INT | 0-10 | Active rail: `0` = AUTO (first connected), `1-10` = manual selection |
| `status` | STRING | - | Read-only display showing current active rail |

### Status Display Colors

- 🟠 **Orange**: AUTO mode - automatically using first connected rail
- 🔵 **Blue**: Manual mode - specific rail selected
- 🔴 **Red**: Error - no models connected

### Usage Example

**Basic Setup:**
```
Checkpoint Loader A → model_1, clip_1, vae_1
Checkpoint Loader B → model_2, clip_2, vae_2
                          ↓
                   AF Model Switch
                 (selected_rail: 0)
                          ↓
                  → model, clip, vae
```

**A/B Testing Workflow:**
1. Set `number_of_rails: 2`
2. Connect two different models to Rails 1 and 2
3. Set `selected_rail: 1` to use first model, `2` for second model
4. Set `selected_rail: 0` for AUTO mode (uses first connected)

**Advanced: Quality vs Speed:**
1. Set `number_of_rails: 3`
2. Rail 1: High-quality slow model
3. Rail 2: Balanced model
4. Rail 3: Fast draft model
5. Switch between them by changing `selected_rail`

### Tips

- **Rails 1-2 are permanent**: These connections are never lost when you adjust `number_of_rails`
- **Rails 3-10 are dynamic**: These are added/removed as needed
- **Use with rgthree Group Bypasser**: Bypass entire model loading groups to save memory - only the selected rail's loaders will execute
- **AUTO mode is smart**: It will find the first rail with actual data, skipping any bypassed/muted nodes
- **Status updates instantly**: No need to run the workflow to see which rail is selected

### Integration with Other Nodes

**Works great with:**
- `rgthree Context Switch` - for full pipeline switching
- `rgthree Group Bypasser` - to disable unused model loaders
- `AF - Save Prompt History` - save which model was used with each prompt
- Any checkpoint loader or AIO loader node

### Technical Notes

- Input names are 1-based: `model_1`, `clip_1`, `vae_1`, etc.
- Internally consistent: no confusing 0-based conversions
- Minimum node width: 160px
- Height auto-adjusts based on number of rails

---

## 📋 Requirements

- ComfyUI (recent version recommended)
- No external dependencies required
- Works with any LLM/text generation nodes, or your manual prompting text nodes

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🐛 Issues & Contributions

Found a bug? Have a feature request?  
→ [GitHub Issues](https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/issues)

---

## ⚠️ Disclaimer

This ComfyUI custom node is developed through AI-assisted coding. While carefully tested, it is provided **"as is" without warranty**. 

**By using this node pack:**
- You install and run at your own risk
- The creator is not liable for damages or data loss
- Compatibility with your setup is not guaranteed
- Test in a safe environment before production use

Report issues on GitHub - we appreciate your feedback!

---

## 📚 Additional Resources

- **[Changelog](CHANGELOG.md)** - Version history and updates
- [GitHub Issues](https://github.com/alFrame/ComfyUI-AF-Pack-Prompt-Nodes/issues) - Report bugs & request features
- [License](LICENSE) - MIT License details

---

**Made with ❤️ by Alex Furer & Qwen3, Claude AI, DeepSeek**
