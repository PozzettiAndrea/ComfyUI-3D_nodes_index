# Anima Style Explorer (Anima-2b)
![Anima Style Explorer](assets/banner.jpg)
A quality-of-life node for ComfyUI that adds artist and style browsing, visual selection, and prompt autocomplete directly inside the workflow.

> This is an independent community tool.
> It does **not** connect to or make requests to the original website.

---

## Installation

1. Download or clone this repository
2. Place the folder inside:

```
ComfyUI/custom_nodes/
```

3. Restart ComfyUI

The node will appear as:

```
Anima Style Explorer
```

---

## What it does

This node replaces the usual “type and guess” prompt workflow with an interactive style selector.

It works similarly to **CLIP Text Encode**:

* connect a CLIP model
* write your prompt
* send conditioning directly to KSampler

The node automatically injects the selected `@artist` tag into the prompt and encodes everything in a single step.

---

## Basic Workflow

```
CheckpointLoader
      |
   (clip) ──► Anima Style Explorer ──► (conditioning) ──► KSampler (positive)
                    |
                 prompt
```

No extra nodes required.

---

## Features

### Visual Style Browser

Open a gallery of 5000+ artists with thumbnails and preview references.
Click any artist to instantly apply it to the prompt.

### Prompt Autocomplete

Type `@` in the prompt box and a live suggestion list appears with previews.

### Random Style

Instantly injects a random artist into your prompt — useful for exploration and inspiration.

### Auto Cycle

Automatically queues generations while cycling artists one by one.
Great for discovering new styles hands-free.

### Update Styles

The node includes a built-in database of 5,000+ artists. You can manually refresh this data by clicking the **Update Styles** button on the node or the refresh icon in the Browser. This avoids automatic downloads on startup.

---

## Credits

Style explorer and dataset concept by @ThetaCursed
https://thetacursed.github.io/Anima-Style-Explorer

All credit for the organization, tagging, and visual references belongs to its original creator.
If the original author requests any modification or removal of dataset content, it will be respected.

---

## Compatibility

* ComfyUI (latest)
* Anima 2B

---

## License

Code: MIT License

Dataset: Provided only for offline autocomplete and browsing functionality with attribution to the original project.
