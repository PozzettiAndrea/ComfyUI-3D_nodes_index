# ComfyUI Simple File Batcher

A lightweight custom node for **ComfyUI** that lists and batches files from a folder with filtering and sorting options.

## ✨ Features

- List files from any folder
- Filter by:
  - Images
  - Videos
  - Text files
  - Custom extensions
- Sort by:
  - Name
  - Date
  - Size
- Outputs:
  - Human-readable file list
  - Full file paths (newline-separated)

## 📦 Installation

### Git clone (recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ai-joe-git/ComfyUI-Simple-File-Batcher.git
````

Restart ComfyUI.

## 🧩 Node

**Category:** `utils`
**Node name:** `Simple File Batcher`

### Inputs

* `folder_path` – Relative or absolute path
* `file_filter` – all / images / videos / text
* `sort_by` – name, date, or size (asc/desc)
* `file_extension` (optional) – `.png,.jpg,.txt`

### Outputs

* `file_list` – numbered filenames
* `file_path_list` – full paths, one per line

## 📄 Example Use Cases

* Batch image processing
* Feeding files into loaders
* Dataset iteration
* Video or text pipelines

## 🛠️ Compatibility

* Tested with ComfyUI
* No external dependencies

## 📜 License

MIT
