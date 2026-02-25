# Vsaan212-workflow-utilities

Subject & Scenario Selectors (with subfolders), Text Split, Optional Switch LoRA, and Lazy Prompt Saver utilities for ComfyUI.

- **Subject Selector** — load subject `.txt` prompts from `SubjectFiles/` (recursive subfolders supported).
- **Scenario Selector** — load scenario `.txt` prompts from `ScenarioFiles/` (recursive subfolders supported).
- **Text Split** — split long prompt text into numbered chunks and a remainder.
- **Optional Switch LoRA** — quick toggle to bypass or apply a LoRA path without rewiring your graph.
- **Lazy Prompt Saver** — save, edit, clone, and delete reusable prompt snippets from a persistent local library, all within the ComfyUI graph.

## Installation

### Via Comfy Registry (recommended)
Search for **`vsaan212/Vsaan212-workflow-utilities`** in the ComfyUI Manager and click **Install**.

### Manual (development)
Clone into your Comfy install:

<ComfyUI root>/
└─ custom_nodes/
└─ vsaan212_workflow_utilities/ # this repo's custom_nodes/* contents

Restart ComfyUI.

## Folder Layout & Auto-Creation

On first load the pack ensures these exist (created automatically if missing):

custom_nodes/vsaan212_workflow_utilities/
├─ ScenarioFiles/
└─ SubjectFiles/


Put your `.txt` files anywhere under those folders (nested subfolders are fine).  
Selectors show **relative POSIX paths without the `.txt` extension** and support ComfyUI’s built-in dropdown filtering.

## Nodes

### Subject Selector
- **Input:** `subject` (dropdown of relative paths)
- **Outputs:** `text`, `preview`
- **Notes:** Use subfolders to organize characters (e.g., `characters/main/ashley_summer`).

### Scenario Selector
- **Input:** `scenario` (dropdown of relative paths)
- **Outputs:** `text`, `preview`
- **Notes:** Useful for episode/scene breakdowns (e.g., `sets/city/night_market`).

### Text Split
- **Purpose:** Split long prompt text into up to N chunks plus remainder.
- **Outputs:** chunk_1..chunk_n, remainder (see node UI).

### Optional Switch LoRA
- **Purpose:** Pass model/clip through unchanged when "bypass" is the lora name; otherwise apply LoRA from a provided path.
- **Tip:** Great for A/B testing and clean disabling without graph edits.

### Lazy Prompt Saver
- **Inputs:** `prompt_name` (string), `prompt_text` (multiline string), `saved_prompts` (dropdown)
- **Output:** `prompt_text` (STRING) — connect to CLIP Text Encoder or any string input
- **Buttons:**
  - **Save** — saves the current name + text to the local `lazy_prompts.json` database
  - **Clone** — copies the current name with a `_copy` suffix for editing (does not save until you click Save)
  - **Delete** — removes the selected prompt after confirmation
- **Notes:** The dropdown updates live after every save/delete. Data persists in `lazy_prompts.json` alongside the node files.

## Troubleshooting

- **New files not appearing:** Refresh ComfyUI (hotkey `R`) and the selector dropdowns will pick up any new `.txt` files — no restart needed.
- **Duplicate filenames in different folders:** Use the full relative path (subfolders disambiguate).
- **Line endings:** Nodes normalize `\r\n` and `\r` to `\n`.

### Example of how to add this to an existing workflow
<img width="2409" height="1254" alt="image" src="https://github.com/user-attachments/assets/704942fe-796c-422b-888b-3ebab1fd838c" />


## License
MIT (see `LICENSE`)
