```markdown
# ComfyUI_FMJ_SaveImageVersions

Save images with full metadata (prompt, workflow, software versions, commit)

This repository provides ComfyUI nodes to:
- Save PNG images with embedded metadata (positive / negative prompts and other JSON fields),
- Generate and copy a snapshot describing the environment (commits, versions, GPU, etc.),
- Load an image and restore information from its metadata.

Important: this project runs a local script `snapshot.py` to capture the state of ComfyUI and custom nodes. Only run it in trusted environments.

---

## Quick summary

- Installation (Manager or manual)
- Usage (ComfyUI nodes)
- Tests (pytest)
- Security & recommendations
- Contribution & releases
- License

---

## Installation

Two options: via the ComfyUI Manager (if available) or by manual install.

### 1) Via ComfyUI Manager (UI)
1. Open ComfyUI and go to the Manager / Plugins tab.
2. Choose “Install from Git repository” or “Install from URL”.
3. Enter the repository URL:
   ```
   https://github.com/bulldog68/ComfyUI_FMJ_SaveImageVersions
   ```
4. If the Manager asks for a branch or subdirectory, specify the desired branch (default `main`) and leave the subdirectory empty if nodes are at the repo root.
5. Install and restart ComfyUI if required.

> Note: Manager implementations vary between ComfyUI versions. If direct install is not available, use the manual method below.

### 2) Manual installation (reliable)
From your ComfyUI installation root:
```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/bulldog68/ComfyUI_FMJ_SaveImageVersions
```
Then restart ComfyUI.

---

## Dependencies

- Python 3.8+
- Pillow
- numpy
- (optional) torch if you use features that depend on PyTorch

Quick install for usual dependencies:
```bash
pip install pillow numpy
# for tests
pip install pytest
```

---

## Usage

After installation, available nodes include (example names):
- `FMJ_SaveImagesWithSnapshot` — save images with metadata and optional snapshot
- `FMJ_LoadImageWithSnapshot` — load an image and read its metadata

Basic flow for the Save node:
1. Configure the output directory using ComfyUI (folder_paths).
2. In `FMJ_SaveImagesWithSnapshot`, provide:
   - `images` (tensors from the graph),
   - `filename_prefix` (will be sanitized),
   - `positive` / `negative` (prompts),
   - `extra_pnginfo` (optional dictionary),
   - `save_snapshot` (bool).
3. The node writes a PNG and, if enabled, runs `snapshot.py` and copies `comfyui_snapshot.txt` into the output folder.

Load node: reads PNG metadata if present and returns `image, positive, negative, config_info, restore_command`.

---

## Tests

A small pytest suite is included for the security utilities.

Run the tests from the repository (or by setting PYTHONPATH):

Option A — run from the package folder:
```bash
cd custom_nodes/ComfyUI_FMJ_SaveImageVersions
PYTHONPATH=. pytest -q tests/test_security_utils.py
```

Option B — run from the ComfyUI repo root (adjust the path):
```bash
PYTHONPATH=custom_nodes/ComfyUI_FMJ_SaveImageVersions pytest -q custom_nodes/ComfyUI_FMJ_SaveImageVersions/tests/test_security_utils.py
```

The tests cover:
- robustness of path checks (`is_within_directory`)
- `safe_run_git` behavior in a folder without a git repo
- SHA256 computation for files

> On Windows, the symlink test is skipped by default (symlink creation may require elevated privileges).

---

## Security — key points

Several security improvements were applied. In short:

- Replaced git calls that used `shell=True` with safe `subprocess.run([...])` calls (`security_utils.safe_run_git`).
- Robust output path checks: uses `os.path.realpath` + `os.path.commonpath` (`is_within_directory`) to prevent path traversal and symlink-based attacks.
- Logs the SHA256 of `snapshot.py` before executing it (for audit).
- More specific exception handling (avoid bare `except:`).
- Limits on PNG metadata sizes (to avoid abuse or very large payloads).
- When restoring from the snapshot, strictly validate any values used to construct commands (e.g., validate commit SHAs with a hex regex) before using them.

Operational recommendations:
- Only execute `snapshot.py` and copy snapshots on trusted systems.
- Restrict write permissions for the `custom_nodes` folder and the outputs folder — do not allow untrusted users to overwrite scripts.
- Do not include secrets in PNG metadata or `comfyui_snapshot.txt`.
- For stronger protection, consider keeping an expected SHA256 hash for `snapshot.py` and refusing execution if it differs.

---
