# BV Node Pack (ComfyUI)

A curated collection of **quality-of-life**, **UI**, and **prompting** nodes for **ComfyUI**, with a strong focus on:

- clean graph layouts
- Subgraph/Subflow compatibility
- metadata-driven pipelines
- AST-based prompt tooling (no fragile string parsing)

> ⚠️ **Important**
> This pack includes **JavaScript UI extensions** for dynamic node behavior.
> These extensions fully support **Subgraphs / Subflows**.

---

## 📌 Table of Contents

- [Installation](#installation)
- [Update & Uninstall](#update--uninstall)
- [Node Overview](#node-overview)
    - [Pipe Nodes](#pipe-nodes)
    - [UI / Layout Nodes](#ui--layout-nodes)
    - [Prompt / AST Nodes](#prompt--ast-nodes)
    - [Util Nodes](#util-nodes)
    - [Beta Nodes](#beta-nodes)
- [Prompt AST Syntax & Markup Guide](#prompt-ast-syntax--markup-guide)
- [Example application for AST](#example-application-for-ast)
- [Quick Start (BV Pipe)](#quick-start-bv-pipe)
- [Notes & Design Principles](#notes--design-principles)
- [Changelog](#changelog)

---

## Installation

Clone into your ComfyUI `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/BlackVortexAI/bv_nodepack.git
```

Restart ComfyUI and hard-refresh the browser:

**Ctrl + F5**

---

## Update & Uninstall

### Update

```bash
cd ComfyUI/custom_nodes/bv_nodepack
git pull
```

Restart ComfyUI (recommended).

### Uninstall

1. Delete the folder in `custom_nodes`
2. Restart ComfyUI
3. Hard refresh the browser (**Ctrl + F5**)

---

## Node Overview

Nodes are grouped by **functional category**.
Each section below can be read independently.

---

## Pipe Nodes

<details>
<summary><strong>BV Pipe Config</strong></summary>

Defines the slot layout (names) for a BV Pipe.

**Screenshot**
> Shows the BV Pipe Config node with a multiline list of slot names.
>
> ![BV Pipe Config](docs/screenshots/bv_pipe_config.png)

**What it does**
- Define slot names (1 per line, max 100)
- Outputs a single `BV_PIPE` object (the "pipe")

**How to use**
1. Add **BV Pipe Config**
2. Enter slot names (one per line)
3. Connect its `pipe` output to **BV Pipe**

</details>

<details>
<summary><strong>BV Pipe</strong></summary>

A config-driven carrier node that forwards one pipe connection while exposing named slots.

**Screenshots**
> Connected state (slots visible)
>
> ![BV Pipe Connected](docs/screenshots/bv_pipe_connected.png)

> Slot override example
>
> ![BV Pipe Override](docs/screenshots/bv_pipe_override.png)

> Subgraph usage
>
> ![BV Pipe Subgraph](docs/screenshots/bv_pipe_subgraph.png)

**What it does**
- Shows only the slots defined by the connected **BV Pipe Config**
- Allows overriding individual slots
- Passes through all untouched slots

</details>

---

## UI / Layout Nodes

<details>
<summary><strong>BV Subgraph Heading</strong></summary>

A UI node that renders a bold header text inside the node.

Designed specifically for **Subgraphs/Subflows**:
When exposed, the heading is also rendered on the Subgraph node itself.

**Screenshots**
> Heading inside normal graph
>
> ![BV Subgraph Heading](docs/screenshots/bv_subgraph_heading.png)

> Heading inside Subgraph
>
> ![BV Subgraph Heading Subgraph](docs/screenshots/bv_subgraph_heading_subgraph.png)

> Heading rendered on Subgraph node
>
> ![BV Subgraph Heading](docs/screenshots/bv_subgraph_heading_subgraph.png)

> Editing the heading text (click on header text to edit)
>
> ![BV Subgraph Heading Edit](docs/screenshots/bv_subgraph_heading_edit.png)

**Inputs**
- `value` (STRING) — header text
- `font_size` (INT) — font size
- `show_divider` (BOOLEAN) — optional divider

</details>

<details>
<summary><strong>BV Spacer</strong></summary>

A UI-only spacer node used to add vertical whitespace.

**Screenshots**
> Normal graph
>
> ![BV Spacer](docs/screenshots/bv_spacer.png)

> Inside Subgraph
>
> ![BV Spacer Subgraph](docs/screenshots/bv_spacer_in_subgraph.png)

> Subgraph node view
>
> ![BV Spacer Subgraph](docs/screenshots/bv_spacer_subgraph.png)

> Editing the spacer height (click on spacer to edit)
>
> ![BV Spacer Edit](docs/screenshots/bv_spacer_edit.png)

**Inputs**
- `height` (INT) — spacer height in pixels
- `scale` (FLOAT, optional) — multiplier

</details>

<details>
<summary><strong>BV Divider</strong></summary>

A UI-only divider node that draws a horizontal separator line.

**Screenshots**
> Divider in graph
>
> ![BV Divider](docs/screenshots/bv_divider.png)

> Divider inside Subgraph
>
> ![BV Divider Subgraph](docs/screenshots/bv_divider_in_subgraph.png)

> Divider rendered on Subgraph node
>
> ![BV Divider Subgraph](docs/screenshots/bv_divider_subgraph.png)

**Inputs**
- `thickness` (INT)
- `padding` (INT)
- `alpha` (FLOAT)

</details>
<details>
<summary><strong>BV Dynamic Combo</strong></summary>

**Purpose**
- Creates a dynamic combo box from a list of strings

**Input**
- `prompt` (COMBO, STRING)

**Output**
- `value_str` (`STRING`)
- `value_int` (`INT`)
- `value_float` (`FLOAT`)
</details>

---

## Prompt / AST Nodes

> These nodes operate on a **structured AST (Abstract Syntax Tree)**, not on raw strings.
> This allows safe filtering, switching, inspection, and refactoring of prompts.

<details>
<summary><strong>BV Prompt Encode</strong></summary>

**Purpose**
- Parses a tagged prompt into an AST

**Input**
- `prompt` (STRING, multiline)

**Output**
- `ast` (`BV_AST`)
- `cleaned_prompt` (plain text, no markup, no comments)

**Screenshot**
> Example output
>
> ![BV Prompt Encode](docs/screenshots/bv_prompt_encoder.png)

</details>

<details>
<summary><strong>BV Prompt Decode</strong></summary>

**Purpose**
- Extracts plain text from the AST by category

**Key Features**
- Multi-category filtering
- `any` / `all` matching
- Inheritance (parent categories)
- Optional prettify pass
- If no filter is set, all categories are displayed.

**Screenshot**
> Example output
>
> ![BV Prompt Decode](docs/screenshots/bv_prompt_decoder.png)

</details>

<details>
<summary><strong>BV Prompt AST Debug</strong></summary>

**Purpose**
- Visual inspection of the AST

**Features**
- JSON pretty-print
- Readonly, scrollable output field
- Safe for large ASTs

**Screenshot**
> Example output
>
> ![BV Prompt AST Debug](docs/screenshots/bv_prompt_ast_debug.png)

</details>

<details>
<summary><strong>BV Prompt Category Switch</strong></summary>

**Purpose**
- Enable / disable categories directly on the AST
- No string parsing

**Features**
- Enable categories
- Disable categories (wins over enable)
- `inherit` and `any/all` matching

**Screenshot**
> Example output
>
> ![BV Prompt Category Switch](docs/screenshots/bv_prompt_switch.png)

</details>

---

## Prompt AST Syntax & Markup Guide

This section explains the **exact prompt syntax** that is parsed into the AST.

### Default (no markup)
```text
A beautiful landscape, sunset lighting
```

### Block categories
```text
@@style
cinematic lighting
@@subject
a woman in rain
```

### Inline categories
```text
a portrait with @<eye> green eyes @@ and @<hair> black hair @@
```

### Nested inline categories
```text
@<subject> a @<face> smiling woman @@ in rain @@
```

### Comments
```text
a portrait ## this is a comment
```

### ⚠️ Common Syntax Pitfalls (Important)

Category names must not contain spaces.

Inline categories are only recognized if the category name matches this pattern:

>[a-zA-Z0-9_-]+


#### ❌ Invalid
```text
@<clothing color> white dress @@
```

✅ Valid
```text
@<clothing_color> white dress @@
```
### Closing inline categories (@@)
```text
@@ closes one currently open inline category

Extra @@ without an open category are treated as literal text and will appear in the output
```
### ❌ Invalid (too many closings)
```text
@<clothing> long dress,@@@@
```

✅ Valid
```text
@<clothing> long dress,@@
```

## Example application for AST
![BV AST Example](workflows/workflow_AST_with_pipe.png)
---

## Latent Nodes

> A Collection of Latent Nodes.

<details>
<summary><strong>BV Latent Random Rotate 90</strong></summary>

**Purpose**
- Rotates a latent by 90 degrees deterministically based on seed if enabled

**Input**
- `latent` (LATENT)
- `seed` (INT)
- `enabled` (BOOLEAN)

**Output**
- `latent` (`LATENT`)
- `latent_width` (`INT`)
- `latent_hieght` (`INT`)


</details>

<details>
<summary><strong>BV Latent Random Aspect Ratio</strong></summary>

**Purpose**
- Generates or resizes a latent to a randomly selected aspect ratio based on a seed
- Selection is deterministic via seed and configurable via enabled aspect-ratio toggles
- Uses a 1:1 base resolution reference (e.g. 1024×1024) commonly assumed for model training

**Input**
- `latent` (LATENT, optional)
    - If connected, the current latent resolution is used as the 1:1 base reference
- `seed` (INT)
- `enabled` (BOOLEAN)
- `base_resolution_px` (INT)
    - Edge length of a square 1:1 reference in pixels (e.g. 1024 = 1024×1024), used when no latent is connected
- `use_1_1` (BOOLEAN) – Resolution 1×1
- `use_3_2` (BOOLEAN) – Resolution 3×2
- `use_2_3` (BOOLEAN) – Resolution 2×3
- `use_4_3` (BOOLEAN) – Resolution 4×3
- `use_3_4` (BOOLEAN) – Resolution 3×4
- `use_16_9` (BOOLEAN) – Resolution 16×9
- `use_9_16` (BOOLEAN) – Resolution 9×16
- `use_21_9` (BOOLEAN) – Resolution 21×9
- `use_9_21` (BOOLEAN) – Resolution 9×21

**Output**
- `latent` (LATENT)
- `latent_width` (INT)
- `latent_height` (INT)
- `picked_ratio` (STRING)

</details

## Util Nodes

> A Collection of Utility Nodes.

<details>
<summary><strong>BV Hex Color To Int</strong></summary>

**Purpose**
- Converts a HEX color code to an INT value

**Input**
- `prompt` (STRING)

**Output**
- `color` (`INT`)


</details>

## Beta Nodes

<details>
<summary><strong>BV Control Center</strong> ⚠️ BETA</summary>

Centralized runtime control for **mute / bypass** states of node groups.

**Key Features**
- Group-based control
- Subgraph-compatible
- Dynamic UI reconfiguration

**Screenshot**
> Configuration
>
> ![BV Divider](docs/screenshots/bv_controllconfig_button.png)

> Selected group
>
> ![BV Divider](docs/screenshots/bv_controllconfig_dialog1.png)

> Define status
>
> ![BV Divider](docs/screenshots/bv_controllconfig_dialog2.png)

>Columns are automatically expanded
>
>![BV Divider](docs/screenshots/bv_controllconfig_dialog3.png)

>After saving the configuration, the `BV Control Center` Node updates itself.
>
>![BV Divider](docs/screenshots/bv_controllconfig_dialog4.png)
>![BV Divider](docs/screenshots/bv_controllconfig_graph1.png)

>Here is an example if, for example, Only Preview is active
>
> ![BV Divider](docs/screenshots/bv_controllconfig_graph2.png)

</details>

---

## Quick Start (BV Pipe)

1. Add **BV Pipe Config** and enter slot names:

```txt
model
clip
vae
seed
prompt
```

2. Connect:

`BV Pipe Config (pipe)` → `BV Pipe (pipe)`

3. Optionally override individual slots.

---

## Notes & Design Principles

- Slot IDs are stable internally (`v_001…v_100`)
- Labels are user-defined and dynamic
- UI nodes are rendered via JavaScript
- All UI nodes support Subgraphs / Subflows
- Prompt nodes operate on **AST**, not raw strings

---

## Changelog

### 2026-01-29
- v0.0.24 — Make subgraph UI widgets more rebuild-safe.

### 2026-01-11
- v0.0.23 — Add BV Latent Random Aspect Ratio node.
- v0.0.22 — Change the category of BV Dynamic Combo. Add 90 Latent Rotate Node.

### 2026-01-10
- v0.0.21 — Add dynamic combo box node
- v0.0.20 — Add a HEX color to INT node

### 2026-01-02
- v0.0.19 — Update README: add AST example image with embedded workflow
- v0.0.18 — Add AST Prompting system
- v0.0.17 — Changed toggle label system (`BV Control Center`)
- v0.0.16 — Renamed inputs to avoid collisions

### 2026-01-01
- v0.0.15 — Fix subgraph renaming bug
- v0.0.14 — Widget fixes for subgraph usage

### 2025-12-31
- v0.0.13 — Fix label inversion error
- v0.0.12 — Fix input error
- v0.0.11 — Reworked renaming logic

### 2025-12-30
- v0.0.10 — Fix widget create event

### 2025-12-29
- v0.0.9 — Fix subgraph issues
- v0.0.8 — Major refactor to TypeScript

