# Asset Manager for ComfyUI

**Asset Manager** is a sidebar-based image asset browser for ComfyUI. It scans your input, output, and custom directories for PNG/WebP images, reads embedded metadata, and lets you browse, filter, search, favorite, and reload workflows directly from the sidebar.

Published to the Comfy Registry under publisher `c0dezer019`.

## Features

### Asset Browsing
- **Sidebar integration** — renders as a dedicated ComfyUI sidebar tab with a responsive image grid
- **Multi-source scanning** — browses ComfyUI's input directory, output directory, and any number of user-configured custom folders
- **Configurable output path** — override the default ComfyUI output directory in settings
- **Workflow loading** — click any image to load its embedded ComfyUI workflow, or right-click for more options
- **Integrated image viewer** — double-click any image to open it in a fullscreen viewer with zoom, pan, and navigation
- **External viewer** — open images in your system's default image viewer via the context menu
- **Live file watching** — the sidebar updates automatically when files are added, deleted, or moved in your scanned directories
- **SQLite index** — a persistent on-disk index caches all file and metadata information so queries hit the database instead of the filesystem, making search and filtering near-instant even with thousands of images

### Search

The search bar supports free-text search across all fields and targeted prefix searches for specific metadata. Multiple terms are AND-matched — every term must match for an image to appear.

#### Basic search

Type any word to search across filenames, asset metadata (title, description, tags), and all embedded workflow data:

```
cat                     # matches "cat" anywhere
golden retriever        # matches "golden" AND "retriever" separately
"golden retriever"      # matches the exact phrase "golden retriever"
```

#### Prefix search

Use `key:value` to target specific fields. For simple values (no spaces or commas), quotes are optional. For values containing spaces or commas, wrap the value in quotes:

```
seed:12345              # exact match on seed value
model:sdxl              # substring match on model/checkpoint name
sampler:euler           # match sampler name
prompt:cat              # substring match in prompt text
prompt:"a brown kitty, realistic"   # match a phrase with spaces and commas
```

#### Available prefixes

| Prefix | Matches against | Match type |
|--------|----------------|------------|
| `seed:` | Seed values | Exact |
| `model:` | Checkpoint/model names | Substring |
| `lora:` | LoRA names | Substring |
| `prompt:` | Prompt text from CLIPTextEncode and similar nodes | Substring |
| `sampler:` | Sampler name (euler, dpmpp_2m, etc.) | Substring |
| `scheduler:` | Scheduler name | Substring |
| `steps:` | Step count | Exact |
| `cfg:` | CFG scale value | Exact |
| `node:` | Node class types in the workflow | Substring |
| `filename:` or `name:` | Filename | Substring |
| `type:` | File type (PNG, WEBP) | Exact |
| `size:` | Formatted file size (e.g. "2.3 MB") | Substring |
| `path:` | Full file path on disk | Substring |
| `date:` | Formatted creation date (e.g. "Jan 15, 2026") | Substring |

#### Combining terms

All terms are AND-matched. Combine freely:

```
model:sdxl sampler:euler prompt:"cute cat"
type:png seed:12345
filename:img path:/output
date:"Jan 15" model:sdxl
```

### Filtering
- **Tab navigation** — switch between All, Inputs, Outputs, and Custom folder views
- **Utility type filter** — show only generated images (with workflow metadata) or only input assets (no workflow)
- **Model/LoRA filtering** — filter by specific checkpoints or LoRAs extracted from embedded prompt metadata
- **Workflow-only mode** — show only images that contain embedded workflows
- **NSFW filter** — hide images matching a customizable keyword list (`filters.json`), scans filenames, asset metadata, and prompt data
- **Active filter chips** — see and clear active filters from the status bar

### Sorting
- Sort by date (newest/oldest), file size (largest/smallest), or name (A-Z / Z-A)
- Left-click the sort button to toggle direction; right-click to pick a different sort field

### Favorites
- **Toggle favorites** — click the bookmark icon on any card or use the right-click context menu to add/remove favorites
- **Filter by favorites** — click the bookmark toolbar button to show only favorited images
- Favorites are persisted in `config.json`

### Image Viewer
Double-click any image card (or choose **View image** from the context menu) to open the integrated fullscreen viewer.

- **Navigation** — previous/next buttons, left/right arrow keys, or drag/swipe the image horizontally (with ghost previews of adjacent images)
- **Zoom** — mouse wheel, `+`/`-` keys, or click the zoom percentage chip for a preset menu (25 % – 500 %)
- **Pan** — drag the image when zoomed in
- **Details panel** — press `I` or click the info button to toggle a collapsible side panel showing File Info and Workflow data; individual values can be copied to clipboard
- **Fullscreen** — press `F` or click the expand button to fill the entire browser window
- **Keyboard shortcuts**

| Key | Action |
|-----|--------|
| `Esc` | Close viewer |
| `←` / `→` | Previous / next image |
| `+` / `-` | Zoom in / out |
| `0` | Reset zoom |
| `I` | Toggle details panel |
| `F` | Toggle fullscreen |

### Context Menu (Right-Click)
Right-click any image card for quick actions:
- **Add/remove favorites**
- **View image** — open in the integrated image viewer
- **Load workflow** — load the image's embedded workflow into ComfyUI
- **Open in external viewer** — open the file in your system's default image viewer
- **Edit metadata** (PNG only) — open the metadata editor panel
- **Copy > Metadata** — copy file-level info (filename, type, size, date, path) to clipboard
- **Copy > Workflow** — browse workflow nodes and copy individual input values (seed, prompt text, model name, etc.) to clipboard. Each node appears as a submenu listing its scalar parameters.
- **Delete** — permanently delete the file

### Asset Metadata (PNG)
- **Embedded metadata editor** — right-click a PNG and select "Edit metadata" to set a title, description, tags, and star rating
- Metadata is stored as custom PNG `tEXt` chunks, so it travels with the file
- NSFW filter also checks asset metadata fields

### Index Management
- **Index health dashboard** — open the settings panel to see index statistics: total assets, workflow/non-workflow counts, model and LoRA counts, file type breakdown, and database size
- **Rebuild index** — click the "Rebuild Index" button in settings to drop and re-index all files from scratch (runs in the background without blocking the UI)
- **Automatic reconciliation** — on startup, the index reconciles with the filesystem in a background thread, only re-reading files whose size or modification time has changed

### Security
- **Secure file proxy** — images are served through a validated proxy route (`/cm-ext-view`) that only allows access to files within configured directories

## Installation

### Via ComfyUI Manager (Recommended)
Search for "Asset Manager" in ComfyUI Manager and install.

### Manual
1. Navigate to your `ComfyUI/custom_nodes/` directory.
2. Clone or symlink this repository.
3. Restart ComfyUI.

No build step required — JavaScript files are served directly.

## Configuration

- **Custom folders**: Click the gear icon in the sidebar to add/remove custom scan directories. You can also use the folder browser to navigate your filesystem.
- **Output directory**: Override the default ComfyUI output path in the settings panel.
- **NSFW filter terms**: Edit `filters.json` to customize the keyword blocklist.
- **Favorites & folders**: Persisted automatically in `config.json`.
- **Index database**: Stored as `index.db` in the extension directory. Delete this file to force a full re-index on next startup, or use the "Rebuild Index" button in settings.

## Architecture

This extension has **no Python nodes** — `NODE_CLASS_MAPPINGS` is empty. It consists of:

- **`__init__.py`** — Registers all HTTP routes at import time
- **`routes/`** — Route handlers split by concern (`favorites.py`, `files.py`, `folders.py`, `history.py`, `metadata.py`, `settings.py`, `tags.py`)
- **`utils/`** — Shared utilities (`config.py`, `helpers.py`, `indexer.py`, `metadata.py`, `png_io.py`, `search.py`, `security.py`, `watcher.py`)
- **`js/sidebar.js`** — Frontend entry point; registers the sidebar extension as `DefinitelyNotHuman.AssetManager`
- **`js/components/`** — UI components (`cardRenderer.js`, `contextMenu.js`, `filterChips.js`, `filterMenu.js`, `imageViewer.js`, `infoPanel.js`, `settingsPanel.js`, `sortMenu.js`)
- **`js/folderSelector.js`** — Modal directory picker component
- **`js/api.js`** — API call helpers
- **`js/state.js`** — Shared sidebar state
- **`js/template.js`** — Sidebar HTML template
- **`js/style.css`** — All styles using the `cm-` class prefix

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/dnh-assetmanager/history` | Main asset listing with filtering |
| GET | `/dnh-assetmanager/tags` | Available checkpoints and LoRAs |
| GET | `/dnh-assetmanager/subdirs` | Directory browser |
| GET | `/dnh-assetmanager/config` | Current configuration |
| GET | `/dnh-assetmanager/metadata` | Read PNG asset metadata |
| GET | `/dnh-assetmanager/version` | Extension version from pyproject.toml |
| POST | `/dnh-assetmanager/folders` | Add/remove custom folders |
| POST | `/dnh-assetmanager/favorite` | Toggle favorite on a file |
| POST | `/dnh-assetmanager/delete` | Delete an asset file |
| POST | `/dnh-assetmanager/settings` | Update settings |
| POST | `/dnh-assetmanager/metadata` | Save PNG asset metadata |
| POST | `/dnh-assetmanager/open` | Open file in system viewer |
| GET | `/dnh-assetmanager/index/stats` | Index health statistics |
| POST | `/dnh-assetmanager/index/rebuild` | Drop and rebuild the index |
| GET | `/cm-ext-view` | Secure file proxy |

## Development

### Linting
```bash
ruff check .
```

Ruff is configured via `pyproject.toml`.

### Requirements
- ComfyUI with `PromptServer`
- Python 3.10+
- `watchdog` (for live file watching)
