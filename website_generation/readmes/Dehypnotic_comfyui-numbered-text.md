# Numbered Text (ComfyUI custom node)
Node for handling text with automatic numbering of divisions and extraction of selected division(s).

A new text division is created for every Return/Enter.

Pick a text divison via the index and output only that text’s content (without the optional “n. ” prefix). Alternatively select several text divisions and an optional separator string. Empty lines are ignored.

Lightweight, no additional dependencies.

1-based indexing.

---

<img width="604" height="454" alt="image" src="https://github.com/user-attachments/assets/8bbd5670-3355-4150-89e3-5320e45b5bbd" />

---

## Usage ideas
I find it useful for prompts. You get a new idea, hit enter and start anew without discarding the old; select, go back, combine; or you can load/paste a list of frequently used prompts and save/copy them for later. May also be useful in combination with a save node for several disk locations etc.

---
## Installation

### 1. Installation via ComfyUI Manager

1. Open ComfyUI Manager → Custom Nodes
2. Search for **NumberedText**.
3. Press **Install** and restart ComfyUI.

### 2. Copy or clone the folder to ComfyUI/custom_nodes/

```bashcd
cd ComfyUI/custom_nodes/
git clone https://github.com/dehypnotic/comfyui-numbered-text.git
```
Restart ComfyUI.

---

### Examples

<img width="949" height="409" alt="image" src="https://github.com/user-attachments/assets/989151bf-156a-4fae-8309-c7d536f3e6af" />
<img width="949" height="402" alt="image" src="https://github.com/user-attachments/assets/96545fa3-cf4d-4119-b720-9fb9d4219f3b" />


---

### Inputs
- String of the whole text.
- Integer of selected text division.
- String of comma separated text divisions.
- String of optional separator.
- Integer of max text divisions for the numbered text output.

### Outputs

- String of selected text division(s).
- String of the whole text, numbered and limited by the max value.

---

### License
MIT License. Feel free to modify; please keep attribution.
