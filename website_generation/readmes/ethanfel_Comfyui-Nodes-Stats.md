# ComfyUI Node Usage Stats

<p align="center">
  <img src="docs/logo.svg" width="120" alt="Node Stats logo">
</p>

A ComfyUI custom node package that silently tracks which nodes and packages you actually use. Helps identify unused packages that are safe to remove — keeping your ComfyUI install lean.

## Features

- **Silent tracking** — hooks into every prompt submission, zero config needed
- **Per-package classification** — packages are sorted into tiers based on usage recency
- **Smart aging** — packages gradually move from "recently unused" to "safe to remove" over time
- **Uninstall detection** — removed packages are flagged separately, historical data preserved
- **Expandable detail** — click any package to see individual node-level stats
- **Non-blocking** — DB writes happen in a background thread, no impact on workflow execution

## Package Classification

Packages are classified into tiers based on when they were last used:

<table>
<tr>
<td><img src="docs/status_used.svg" width="18"> <b>Used</b></td>
<td>Actively used within the last month</td>
</tr>
<tr>
<td><img src="docs/status_unused_new.svg" width="18"> <b>Recently Unused</b></td>
<td>Not used yet, but tracking started less than a month ago — too early to judge</td>
</tr>
<tr>
<td><img src="docs/status_consider.svg" width="18"> <b>Consider Removing</b></td>
<td>Unused for 1–2 months — worth reviewing</td>
</tr>
<tr>
<td><img src="docs/status_safe.svg" width="18"> <b>Safe to Remove</b></td>
<td>Unused for 2+ months — confident removal candidate</td>
</tr>
<tr>
<td><img src="docs/status_uninstalled.svg" width="18"> <b>Uninstalled</b></td>
<td>Previously tracked but no longer installed — shown for reference</td>
</tr>
</table>

## Installation

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/ethanfel/Comfyui-Nodes-Stats.git
```

Restart ComfyUI. Tracking starts immediately and silently.

## Usage

### UI

Click the **Node Stats** button (bar chart icon) in the ComfyUI top menu bar. A dialog shows:

- **Summary bar** with counts for each classification tier
- **Sections** for each tier, sorted from most actionable to least
- **Expandable rows** — click any package to see per-node execution counts and timestamps

### API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/nodes-stats/packages` | GET | Per-package aggregated stats with classification |
| `/nodes-stats/usage` | GET | Raw per-node usage data |
| `/nodes-stats/reset` | POST | Clear all tracked data |

```bash
curl http://localhost:8188/nodes-stats/packages | python3 -m json.tool
```

<details>
<summary>Example response</summary>

```json
[
  {
    "package": "ComfyUI-Impact-Pack",
    "total_executions": 42,
    "used_nodes": 5,
    "total_nodes": 30,
    "last_seen": "2026-02-22T12:00:00+00:00",
    "installed": true,
    "status": "used",
    "nodes": [
      {
        "class_type": "SAMDetectorCombined",
        "package": "ComfyUI-Impact-Pack",
        "count": 20,
        "first_seen": "2026-01-01T00:00:00+00:00",
        "last_seen": "2026-02-22T12:00:00+00:00"
      }
    ]
  },
  {
    "package": "ComfyUI-Unused-Nodes",
    "total_executions": 0,
    "used_nodes": 0,
    "total_nodes": 12,
    "last_seen": null,
    "installed": true,
    "status": "safe_to_remove",
    "nodes": []
  }
]
```

</details>

## How It Works

```
Queue Prompt ──> Prompt Handler ──> Extract class_types ──> Background Thread
                                                                   │
                                         ┌─────────────────────────┘
                                         ▼
                                    SQLite DB
                                   usage_stats.db
                                    ┌──────────┐
                                    │node_usage │  per-node counts & timestamps
                                    │prompt_log │  full node list per prompt
                                    └──────────┘
                                         │
            GET /nodes-stats/packages ◄──┘
                      │
                      ▼
               Mapper merges DB data
               with NODE_CLASS_MAPPINGS
                      │
                      ▼
              Classify by recency ──> JSON response ──> UI Dialog
```

1. Registers a prompt handler via `PromptServer.instance.add_on_prompt_handler()`
2. On every prompt submission, extracts `class_type` from each node in the workflow
3. Offloads recording to a background thread (non-blocking)
4. Maps each class_type to its source package using `RELATIVE_PYTHON_MODULE`
5. Upserts per-node counts and timestamps into SQLite
6. On stats request, merges DB data with current node registry and classifies by recency

## Data Storage

All data is stored in `usage_stats.db` in the package directory.

| Table | Contents |
|-------|----------|
| `node_usage` | Per-node: class_type, package, execution count, first/last seen |
| `prompt_log` | Per-prompt: timestamp, JSON array of all class_types used |

Use `POST /nodes-stats/reset` to clear all data and start fresh.

## File Structure

```
__init__.py        Entry point: prompt handler, API routes
mapper.py          class_type → package name mapping
tracker.py         SQLite persistence and stats aggregation
js/nodes_stats.js  Frontend: menu button + stats dialog
pyproject.toml     Package metadata
```
