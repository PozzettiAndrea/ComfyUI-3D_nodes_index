# ComfyUI-NL_Nodes

Custom ComfyUI nodes and UI panels maintained by NOLABEL. The pack focuses on studio workflow context, IO helpers, model localization, and a WanVideo encoder utility.

## Installation
- Copy `//alien/comfyui/extra_model_paths.yaml` to your local `ComfyUI` installation folder directory (if you have existing one, rename it to `extra_model_paths_old.yaml` or backup it somewhere).
- Open the newly created `ComfyUI/extra_model_paths.yaml` and adjust **models1** paths so they will point to your chosen local `/models` folder.
- Restart ComfyUI. You should see top-bar buttons for "NL Workflow" and "NL Tools".



https://github.com/user-attachments/assets/5d2572b3-5aec-476f-8f9c-c039f73219be


## What You Get

Top-bar tools:
- `NL Workflow`: shot context panel (project, shot, resolution, fps, frame range, project path).
- `NL Tools` menu: groups NL buttons and includes a simple `Configuration` panel (username).
- `NL Models Manager`: model localization manager (network <-> local cache).
- `NL Templates`: shared workflow library with metadata, tags, and poster images.
- `NL Subgraphs`: shared blueprint library for reusable graph blocks.
- `NL Cost Ledger`: API usage and cost tracking panel.


Nodes:
- `NOLABEL/IO`: `NL Read`, `NL Write`.
- `NOLABEL/Workflow`: `NL Resolution`, `NL FPS`, `NL Frame Range`, `NL Project Path`, `NL Context Debug`.
- `NOLABEL/Utilities`: `NL Constant Color`.
- `WanVideoWrapper`: `NL WanVideo ImageToVideo Encode v2 (multi-ref)`.



## Artist Quick Start

1. Open `NL Workflow`, fill `project/scene/shot` and `project_path`, then click `Apply`.
2. Use `NL Read` and `NL Write` in your graph.
3. Open `NL Templates` to load a starting setup, or `NL Subgraphs` to insert reusable blueprint blocks.
4. If a model is missing locally, open `NL Models Manager` and localize it from network storage.

## Panels (Top Bar)

### NL Workflow
- Stores the current shot context and makes it available to helper/IO nodes.
- Save defaults and history for quick reuse between sessions.
- Includes quick tools such as copy workflow JSON and context helpers.

Saved files:
- `ComfyUI/user/default/nl_workflow.json`
- `ComfyUI/user/default/nl_workflow_history.json`

### NL Models (Model Manager)
- Scans the current graph for model path widgets.
- Shows local/network availability, file size, and usage.
- Supports `Localize`, `Re-localize`, `Upload`, `Delete local`, and batch actions.
- Includes cache pruning by size with optional auto-delete.

Notes:
- Uses `models1` as local root and `models2` as network root from `extra_model_paths.yaml`.
- If categories only exist on one side, missing side entries are auto-filled.

### NL Templates
- Browse templates with search, sort, tags, and popularity signals.
- Load templates directly into the current graph.
- On load, network paths are normalized for the host OS (`\\server\\...` <-> `/mnt/server/...`; set `normalize_paths=0` on `/nl_templates/load` to disable).
- Create/update templates from the current graph or from JSON.
- During create/update, `NL Read` source assets are copied into shared template storage (`<templates_root>/<user>/__assets/<template_stem>/...`) and workflow paths are rewritten to those copies so templates stay self-contained.
- Supports metadata, versioning, stack confirmations, and poster images (card/header).
- Includes a `Copy Prompt` helper to generate a metadata-writing prompt with current tags and workflow JSON.

Requires:
- `shared.nl_templates` in `extra_model_paths.yaml`.
- Optional migration helper for existing templates: `python scripts/nl_templates_localize_assets.py --root /path/to/templates`.

### NL Subgraphs
- Lists local and shared subgraph blueprints (`.json`).
- Click an entry to insert its blueprint node into the active workflow.
- Publish local subgraphs to shared storage (with overwrite confirmation).
- Marks local/shared conflicts when hashes differ.

Shared path keys (first available is used):
- `shared.nl_subgraphs`
- `shared.subgraphs`
- `shared.nl_subgraph_blueprints`
- `shared.subgraph_blueprints`

### NL Cost Ledger
- Tracks API workflow usage rows in SQLite with production tags (`project`, `scene`, `shot`, `user`, optional `task`).
- Non-API prompts are ignored.
- Includes list filtering, detail modal, summary, and CSV export.
- Read source toggle supports `Local` (default) and optional read-only `Global` DB.
- After each successful run, NL Ledger schedules delayed Local -> Global sync (upsert).
- `Refresh` still triggers manual Local -> Global sync before reloading panel data.
- Uses `POST /nlnodes/prompt` for queueing plus ledger capture.
- Optional credits from Comfy `/customers/balance` deltas (`211 credits = 1 USD`).
- Balance amounts are normalized to USD with `NL_LEDGER_BALANCE_USD_SCALE` (default `0.01`).
- Ledger rows also store post-run `Wallet` state (after-balance USD) when available from balance tracking, plus derived wallet-in-credits.
- Balance-delta rows include confidence classification (`high`/`medium`/`low`) and the panel colors cost cells green/yellow/red.
- When credits cannot be resolved immediately, ledger rows store capture status/reason in `credits_json` and retry in the background with exponential backoff.
- Retry tuning: `NL_LEDGER_BALANCE_RETRY_ATTEMPTS`, `NL_LEDGER_BALANCE_RETRY_INITIAL_DELAY_SEC`, `NL_LEDGER_BALANCE_RETRY_MAX_DELAY_SEC`, `NL_LEDGER_BALANCE_RETRY_BACKOFF`, `NL_LEDGER_BALANCE_RETRY_BATCH`.
- Local DB defaults to `ComfyUI/user/default/nl_cost_ledger.sqlite3` (or `NL_LEDGER_DB_PATH` override).
- Global DB path: `NL_LEDGER_GLOBAL_DB_PATH` or legacy `extra_model_paths.yaml` ledger `db_path`.
- Auto sync controls: `NL_LEDGER_AUTO_SYNC` (`true`/`false`) and `NL_LEDGER_AUTO_SYNC_DELAY_SEC`.

More verification steps:
- See `TESTING.md`.

### NL Tools Menu + Configuration
- Consolidates NL buttons into one dropdown menu (cleaner top bar).
- Stores username used by NL Templates and NL Ledger flows.
- Shows a username prompt strip when required data is missing.

## Nodes

### NOLABEL/IO
- `NL Read`: read image, sequence, or video with range controls, sampling, reverse, resize, preview, and upload-to-input support.
- `NL Write`: write stills or sequences with versioned names based on workflow context; optional MP4/MOV (ffmpeg), alpha/mask, and compare outputs.

### NOLABEL/Workflow
- `NL Resolution`, `NL FPS`, `NL Frame Range`, `NL Project Path`: reads cached workflow values.
- `NL Context Debug`: outputs cached context JSON (and optional console print).

### NOLABEL/Utilities
- `NL Constant Color`: constant color image + mask at workflow or custom resolution.

### WanVideoWrapper
- `NL WanVideo ImageToVideo Encode v2 (multi-ref)`: WanVideo reference encode utility with optional temporal mask/control embeds/tiled VAE paths.

## Dependencies

- Required for most nodes: `torch`, `numpy`, `Pillow`.
- Optional for video IO: `imageio`, `ffmpeg`.
- Required for YAML config parsing: `PyYAML`.

## Manual Testing (No Automated Test Suite)

- `NL Workflow`: apply context, save defaults, restart ComfyUI, verify reload + history behavior.
- `NL Read/Write`: test image, sequence, and video; verify naming/versioning and optional video output.
- `NL Models`: test scan/localize/upload/delete/prune and missing-network behavior.
- `NL Templates`: test load, create/update, search/tags/sort, posters, and confirmations.
- `NL Subgraphs`: test list, click-to-insert, publish, overwrite prompt, and conflict indicators.
- `NL Ledger`: run `TESTING.md` checklist end-to-end.
