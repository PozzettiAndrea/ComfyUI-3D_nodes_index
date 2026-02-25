## Other My Nodes

Utilities for working with Lists, Regions, Toggling groups, Caching conditions: [ComfyUI AK Pack](https://github.com/akawana/ComfyUI-AK-Pack)

Folding of promts in to tree with extra features. Extra shortcuts for editing prompts. Reginal prompting text separation: [ComfyUI Folded Prompts](https://github.com/akawana/ComfyUI-Folded-Prompts)

RGBYP 5-color mask editor: [ComfyUI RGBYP Mask Editor](https://github.com/akawana/ComfyUI-RGBYP-Mask-Editor)

AK XZ Axis so called XY testing for any type of KSampler: [ComfyUI AK XZ Axis](https://github.com/akawana/ComfyUI-AK-XZ-Axis)

---

## Version changes

**V 3.00**

In my node pack [ComfyUI Utils Extra](https://github.com/akawana/ComfyUI-Utils-extra), I’ve added a new node called **“CLIP Text Encode Cached”**. I highly recommend using it together with **FPFoldedPrompts** and **FPTextAreaPlus**!

This node can cache the previous **CONDITIONING** and avoids re-encoding. Unfortunately, ComfyUI is designed in such a way that if you change anything in **FPFoldedPrompts** or **FPTextAreaPlus**, the encode step will always be triggered. However, you often change text inside the `<ARn>` tags, and this should *not* cause a re-encode of the main text.

I also want to remind you that the same pack [ComfyUI Utils Extra](https://github.com/akawana/ComfyUI-Utils-extra) includes the **CLIPEncodeMultiple** node, which is specifically designed to encode individual lines `<AR1>`…`<AR5>`. It simply works faster because it also uses caching.

**V 2.0**

Added line weight control to the "FP Folded Prompts" node. You can now set the weight of tags or any text.

---

# Folded Prompts

This extension now provides **3 utility nodes**:

- **FP Folded Prompt** – hierarchical prompt organizer with folder-based editing UI  
- **FP Text Clean And Split** – parser that removes commented lines and extracts Regional Prompting areas  
- **FP Text Area Plus** – extended text input node with before/after text injection  

And new keyboard shortcuts with settings.
---

## Keyboard Shortcuts

### 1. Toggle line comment — `Ctrl + /`

**Behavior**
- Press `Ctrl + /` to comment/uncomment the current line or selected lines.
- By default it uses `// ` (with a space).
- If a line already starts with `//` or `// `, the shortcut removes it.

### Configurable comment prefix

In **ComfyUI → Settings → Keybinding Extra** you can set any prefix you want, for example:

- `//`
- `#`
- `--`
- `;`

There is also an enable/disable toggle for the comment shortcut.

### 2. Delete line — `Ctrl + Shift + L`

**Behavior**
- Press `Ctrl + Shift + L` to delete the current line.
- If multiple lines are selected, deletes all selected lines.
- Deletion supports editor undo (`Ctrl + Z`) where possible.

### 3. Move & Comment word(tag) or selection — `Ctrl + Shift + /`

**Behavior**
- Press `Ctrl + Shift + /` to cut the word under the cursor (or all selected words).
- Removes the word(s) from anywhere in the line.
- Inserts them on the next new line.
- Comments the moved word(s) on new line using the comment prefix set in the extension settings.
- Supports editor undo (`Ctrl + Z`) (I know about whole text selection).

---

## FP Folded Prompt

Builds a **folder-based tree** from your prompt lines.  
Useful for large projects where you need to store many previous prompts, reuse prompt blocks, or quickly insert sets of tags without typing them manually.

The node saves JSON representations of your trees in `/input/prompts_folded/`.  
This folder is optional — you may delete it at any time. All data is still stored in the workflow itself.

**V 2.0**
Added line weight control to the "FP Folded Prompts" node. You can now set the weight of tags or any text.

<img src="preview_folded_prompt.jpg" width="100%"/>

### Modes

#### 1. Tree Mode

- Visual folder tree  
- Enable/disable lines  
- Assign Regional Prompting areas  
- Edit everything using the mouse  

#### 2. Edit Mode

Write your structure manually using `[Folder]` syntax:

```text
[Folder]
string1 some text or tags, bla, bla, bla
string2 some text or tags, bla, bla, bla

[Folder/Subfolder]
string1 some text or tags, bla, bla, bla
string2 some text or tags, bla, bla, bla

[Folder/Subfolder/SubSubfolder]
string1 some text or tags, bla, bla, bla
string2 some text or tags, bla, bla, bla
```

### Commenting

Use `//` at the start of a line:

```text
string1 normal line
// string2 commented line
```

Commented lines appear disabled in the tree.

### Regional Prompting Support

You may assign any line to one of **five** AR regions using HTML-like tags:

```text
<AR1>text...</>
<AR2>text...</>
<AR3>text...</>
<AR4>text...</>
<AR5>text...</>
```

**Important:** The closing tag is always `</>`.  
This makes editing large texts easier — no need to rename closing tags.

All AR features can also be controlled visually in Tree Mode.

<img src="preview_folded_prompt_edit.jpg" width="100%"/>

---

## FP Text Clean And Split

Utility node that processes raw text (either from FP Folded Prompt or from any normal text input).

### Behavior

- Removes commented lines (`// ...`)
- Detects AR blocks (`<AR1>...</>`, … `<AR5>...</>`)
- Extracts AR blocks and outputs them as a **list** on `ar_list`
- Removes AR blocks from the main text and outputs the cleaned version

### Why this is useful

You can:

- quickly compose prompts by hand  
- comment out what you don't need  
- use Regional Prompting without manually parsing anything  

<img src="preview_text_clean.jpg" width="100%"/>

---

## FP Text Area Plus

Simple utility text node.

### Features

- Standard text input field  
- Optional *before text* field  
- Optional *after text* field  
- Outputs the concatenated full result  

## Installation

You can install this extension in two ways:

### 1. Through ComfyUI Manager (recommended)

Open **ComfyUI Manager → Install**,  
then simply search for **Folded prompts** in the search bar.  
Select the extension and click **Install**.

### 2. Manual installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/akawana/ComfyUI-Folded-Prompts.git

