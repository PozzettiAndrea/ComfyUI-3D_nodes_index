# ComfyUI-PromptHistoryGallery

Capture ComfyUI prompts and generated images with a history dialog, popup previews, and a full gallery viewer.

## Features

- Save prompts to history while still returning the `CONDITIONING` output for your workflow.
- View the latest thumbnail and total image count per prompt, and jump straight into the gallery.
- Search history by prompt text or tags, then send to node, copy, or delete with quick actions.
- See popup previews when generations finish; click a preview to open the gallery.
- Tune history limit, frequent-prompt highlighting, and popup preview size/duration/position in the Settings tab.

## Prompt History Input Node

<img width="350" alt="Screenshot of prompt history node" src="https://github.com/user-attachments/assets/00837c62-24f9-472f-a29a-b72e28ffcce6" /><br>

- `CLIP`: Connect the CLIP text encoder that should be used to embed the prompt.
- `Prompt`: Provide any text prompt. The node saves it to history and returns a matching `CONDITIONING`.

Output:

- `conditioning`: The `CONDITIONING` tensor produced by encoding the prompt with the supplied CLIP model.

The node executes on every graph run so repeated prompts are captured. Each execution appends or touches an entry in a SQLite database (default: `prompt_history_gallery/data/prompt_history.db`). Set the `COMFYUI_PROMPT_HISTORY_DIR` environment variable to override the storage location.

## History Dialog + Popup Preview (History button on the node)

<img width="500" alt="Screenshot of prompt history window" src="https://github.com/user-attachments/assets/9d3e3633-ed31-48b6-8cf8-7c40a4b73c34" /><br>
<img width="500" alt="Screenshot of image preview" src="https://github.com/user-attachments/assets/2e1a971f-dfa1-4b3b-84fa-a7beceadcdaf" />

- Each `Prompt History Input` node includes a `History` button. Clicking it opens a dialog with recent prompts grouped by text and sorted by recent use.
- Search by prompt text or tags. Entries show the latest preview, image count, and tags when available.
- Actions: send the prompt back to the selected node (falls back to copy if no node is active), copy, delete, and open the full gallery.
- The dialog refreshes when new prompts finish so it stays in sync with the latest generations.
- Popup previews appear when images complete; click a preview to open the gallery.
- Use the Settings tab to toggle popup previews, adjust preview duration/size, change the history limit, and tune frequent-prompt highlighting.

## Development

### Formatting

- One-shot fixer: `scripts/format.sh` (needs `pipx` and Node) runs Ruff via `pipx run --spec ruff==0.14.10` plus Prettier `-w` to apply fixes.
- Install dev tools: `pip install -e .[dev]` (provides Ruff).
- Python: run `ruff format --check .` and `ruff check --select I .` (add `--fix` locally if you want auto-fixes).
- Web/JS/CSS: run `npx prettier@3.7.4 --check "web/**/*.{js,jsx,ts,tsx,css,scss,html,json}"` (honors `.prettierignore`; `web/vendor/` is excluded).
- CI: `.github/workflows/ci.yml` runs `ruff format --check .`, `ruff check --select I .`, and `npx prettier@3.7.4 --check "web/**/*.{js,jsx,ts,tsx,css,scss,html,json}"` on pushes/PRs to `main`.

### Release

- Release bundles are published by GitHub Actions; no manual `node.zip` rebuild is required.
