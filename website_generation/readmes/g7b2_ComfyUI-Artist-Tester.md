# ComfyUI Artist Tester (V2.0)

A powerful custom node suite for **Batch Testing** artists, styles, and prompts in ComfyUI. 

Now updated to **V2.0** with **No-Repeat Random**, **Counter Isolation**, **Filename Indexing**, and **Smart Sanitization**.

## ✨ Features

### 👉 1. Artist List Iterator (V2.0)
The core node to manage your list.
- **Random (No Repeat)**: Uses a `seed` to shuffle the list deterministically. You can run through 100 artists without repeating a single one!
- **Counter Isolation**: Counters are now tied to the list content. Multiple iterator nodes won't interfere with each other.
- **New Outputs**: 
  - `index_string`: Outputs formatted numbers like "001", "002" for sorting filenames.
  - `total_count`: Total number of lines.

### 👉 2. Artist Prompt Composer (Flexible)
- **Custom Template**: Now supports flexible prompt weighting and positioning!
  - Default: `{base}, {artist}`
  - Example: `{base}, (style of {artist}:1.2)`
  - Example: `(artist:{artist}), {base}`
- **Auto-Connect**: Automatically combines Base Prompt + Artist + Negative.

### 💾 3. Save Image (Auto Name)
- **Smart Sanitization**: 
  - Automatically fixes Windows filename errors (e.g., converts `artist:tag` to `artist-tag`).
  - Removes illegal characters (`\ / : * ? " < > |`).
  - Truncates filenames if they are too long.
- **Plug & Play**: Connect the `final_text` directly to `filename_prefix`.

## 📦 Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   Clone this repository:
   git clone https://github.com/g7b2/ComfyUI-Artist-Tester.git