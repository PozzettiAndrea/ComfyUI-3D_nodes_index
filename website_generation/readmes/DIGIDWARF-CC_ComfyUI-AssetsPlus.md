# ComfyUI-AssetsPlus <img alt="Static Badge" src="https://img.shields.io/badge/OpenAI-Codex-gray?style=plastic&label=OpenAI&labelColor=0fa37f&color=gray">
<p align="center">
  <img src="/meta/img/logo_1024x700.png" alt="ai-generated assets-plus logo" width="600"/>
</p>

Assets+ is an extension for ComfyUI that adds the **Assets+ Explorer** sidebar panel and provides a
persistent overview of the output and input directories via the `/assets_plus` API.

## Disclaimer about AI usage
* This extension code was written almost purely by OpenAI Codex. Please report any quirks or mishaps at Issues page.
* Any PRs will be greatly appreciated, thank you!

## Installation

1. Clone the repository into ComfyUI’s `custom_nodes/` (you should end up with
   the folder `custom_nodes/ComfyUI-AssetsPlus/`).
2. Restart ComfyUI.
3. (Optional) To enable sending files to the trash bin, install the dependency:
   `pip install send2trash`.

The frontend part is located at `custom_nodes/ComfyUI-AssetsPlus/web/assets_plus.js` and will be
loaded automatically.

## How to open Assets+ Explorer

1. Open the ComfyUI sidebar.
2. Click the **Assets+ Explorer** tab (folder icon).

If the panel doesn’t show up:
- check that the folder is named `custom_nodes/ComfyUI-AssetsPlus/`;
- make sure ComfyUI was restarted after installation.

## Settings

The config file is located at `user/__assets_plus/config.json`. If the file doesn’t exist,
defaults are used.

Available options:
- `allowed_extensions`: a list of extensions (e.g. `[".png", ".jpg", ".webp"]`).
- `thumbnail_quality`: `"low"` (256px) or `"high"` (512px).
- `list_limit`: page size for list requests.
- `recursive`: recursive scan of the output directory (`true/false`).
- `default_delete_mode`: `"trash" | "delete" | "hide"`.
- `scan_depth`: depth limit for recursive scanning (`null` = no limit).

UI settings (ComfyUI Settings → Assets+ Explorer):
- **Assets+ page size** — number of items fetched per page.
- **Assets+ confirm deletions** — toggle confirmation dialogs for delete/hide actions.
- **Assets+ show overlay navigation hint** — toggle the on-screen navigation hint in the lens overlay.
- **Assets+ keep overlay open when opening/replacing workflow** — keep the lens overlay open after workflow actions.
- **Assets+ thumbnail quality** — pick low (256px) or high (512px) previews.
- **Assets+ clear thumbnail cache** — action button to remove cached previews on disk.

Example:
```json
{
  "allowed_extensions": [".png", ".jpg", ".jpeg", ".webp", ".mp4", ".webm"],
  "thumbnail_quality": "low",
  "list_limit": 200,
  "recursive": true,
  "default_delete_mode": "trash",
  "scan_depth": null
}
````

## Features

* List assets from the output and input directories (recursively).
* Thumbnails via `/assets_plus/output/thumb` and `/assets_plus/input/thumb`.
* Workflow/prompt metadata via `/assets_plus/output/meta` and `/assets_plus/input/meta`.
* Deleting from disk (trash/delete) or hiding (hide) with confirmation in both tabs.
* Full-screen lens overlay with navigation, workflow actions, zoom/pan controls, and keybindings registered in ComfyUI.
* Assets+ shortcuts tab in the ComfyUI Shortcuts panel for overlay navigation actions.
* Multi-selection via checkboxes on each asset tile.
* Sticky header with icon-based actions (search toggle, select all, invert selection, download/delete) while only the gallery area scrolls.
* Server-side search optimized for large galleries.
* Lazy loading of thumbnails and paged scrolling for large galleries.
* Event-driven updates when ComfyUI emits execution or upload events (no polling).

## Deletion modes

* **trash** — moves files to the trash bin via `send2trash` (if available). If the dependency
  is not installed, regular deletion is used.
* **delete** — permanently deletes the file.
* **hide** — hides the asset from the list while keeping the file on disk
  (the index is stored in `user/__assets_plus/hidden.json`).

## Workflow actions

If an asset has workflow metadata, the tile menu (burger button in the top-right corner) exposes:

* **Open workflow (new tab)** — opens the workflow in a new tab (like standard Media Assets).
* **Replace current workflow** — replaces the workflow in the current tab without creating a new one.

If there’s no metadata, the menu is hidden.

## Limitations

* Asset sources are ComfyUI’s output/input directories only (no arbitrary paths).
* Videos (`.mp4/.webm`) are served as-is; no thumbnails are generated.
* Search is executed by the backend (depends on `/assets_plus/*/list?query=`).
* Delete confirmations can be disabled in Settings (Assets+ confirm deletions).

## ComfyUI-Manager compatibility

The extension structure matches Manager requirements:

* `__init__.py` exports `WEB_DIRECTORY` so the frontend is picked up automatically.
* `web/assets_plus.js` registers the **Assets+ Explorer** tab via `registerSidebarTab`.
* No extra installation steps are needed besides restarting ComfyUI.

## Notes

* `send2trash` is used for moving to trash (if available).
* Hidden assets are stored in `user/__assets_plus/hidden.json` (input entries are namespaced).
* Thumbnail cache: `user/__assets_plus/thumb_cache/`.
* The thumbnail cache can be cleared from settings or via `POST /assets_plus/thumb/clear`.
