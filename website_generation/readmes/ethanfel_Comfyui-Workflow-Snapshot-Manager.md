<p align="center">
  <img src="assets/banner.png" alt="Workflow Snapshot Manager" width="100%"/>
</p>

<p align="center">
  <a href="https://registry.comfy.org/publishers/ethanfel/nodes/comfyui-snapshot-manager"><img src="https://img.shields.io/badge/ComfyUI-Registry-blue?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMMyA3djEwbDkgNSA5LTVWN2wtOS01eiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=" alt="ComfyUI Registry"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"/></a>
  <img src="https://img.shields.io/badge/version-2.5.0-blue" alt="Version"/>
  <img src="https://img.shields.io/badge/ComfyUI-Extension-purple" alt="ComfyUI Extension"/>
</p>

---

**Workflow Snapshot Manager** automatically captures your ComfyUI workflow as you edit. Browse, name, search, and restore any previous version from a sidebar panel — stored as JSON files on the server, accessible from any browser.

<p align="center">
  <img src="assets/sidebar-preview.png" alt="Sidebar Preview" width="300"/>
</p>

## Features

- **Auto-capture** — Snapshots are saved automatically as you edit, with configurable debounce
- **Custom naming** — Name your snapshots when taking them manually ("Before merge", "Working v2", etc.)
- **Search & filter** — Quickly find snapshots by name with the filter bar
- **Restore or Swap** — Open a snapshot as a new workflow, or replace the current one in-place
- **Workflow browser** — Browse and recover snapshots from any workflow, including renamed or deleted ones
- **Per-workflow storage** — Each workflow has its own independent snapshot history
- **Theme-aware UI** — Adapts to light and dark ComfyUI themes
- **Toast notifications** — Visual feedback for save, restore, and error operations
- **SaveSnapshot node** — Trigger snapshot captures from your workflow with a custom node; node snapshots are visually distinct (purple border + "Node" badge) and have their own rolling limit
- **Change-type icons** — Timeline markers show what kind of change each snapshot represents (node add, remove, connection, parameter, move, mixed) with distinct colored icons — like Fusion 360's operation timeline
- **Timeline bar** — Optional centered floating bar on the canvas showing all snapshots as iconic markers, with a Snapshot button for quick captures; tucks behind the sidebar when open
- **Active & current markers** — When you swap to a snapshot, the timeline highlights where you came from (green dot) and where you are (white ring)
- **Auto-save before swap** — Swapping to an older snapshot automatically saves your current state first, so you can always get back; browsing between saved snapshots skips redundant saves
- **Ctrl+S shortcut** — Press Ctrl+S (or Cmd+S on Mac) to take a manual snapshot alongside ComfyUI's own save
- **SVG graph previews** — Hover any snapshot for a tooltip preview of the workflow graph; click the eye button for a full-size modal; diff view now shows side-by-side SVG comparison with color-coded highlights (green = added, red = removed, amber = modified)
- **Diff view** — Compare any snapshot against the current workflow (one click) or two snapshots against each other (Shift+click to set base); see added/removed/modified nodes, widget value changes, and rewired connections in a single modal
- **Lock/pin snapshots** — Protect important snapshots from auto-pruning and "Clear All" with a single click
- **Concurrency-safe** — Lock guard prevents double-click issues during restore
- **Server-side storage** — Snapshots persist on the ComfyUI server's filesystem, accessible from any browser
- **Automatic migration** — Existing IndexedDB snapshots are imported to the server on first load

## Installation

### ComfyUI Manager (Recommended)

Search for **Workflow Snapshot Manager** in [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) and click Install.

### Git Clone

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ethanfel/Comfyui-Workflow-Snapshot-Manager.git
```

Restart ComfyUI after installing.

## Usage

### 1. Open the Sidebar

Click the **clock icon** (<img src="https://img.shields.io/badge/-pi pi--history-333?style=flat" alt="history icon"/>) in the ComfyUI sidebar to open the Snapshots panel.

### 2. Snapshots are Captured Automatically

As you edit your workflow, snapshots are saved automatically after a configurable delay (default: 3 seconds). An initial snapshot is also captured when the workflow loads.

### 3. Take a Named Snapshot

Click **Take Snapshot** to manually save the current state. A prompt lets you enter a custom name — great for checkpoints like "Before refactor" or "Working config".

### 4. Search & Filter

Use the filter bar at the top of the panel to search snapshots by name. The clear button (**&times;**) resets the filter.

### 5. Restore or Swap

Each snapshot has action buttons:

| Button | Action |
|--------|--------|
| **Preview** (eye icon) | Opens a full-size SVG preview of the workflow graph |
| **Lock** | Toggles lock protection (padlock icon) |
| **Swap** | Replaces the current workflow in-place (same tab) |
| **Restore** | Opens the snapshot as a new workflow |

### 6. Lock / Pin Snapshots

Click the **padlock icon** on any snapshot to lock it. Locked snapshots are protected from:

- **Auto-pruning** — When the snapshot count exceeds the max, only unlocked snapshots are pruned
- **Clear All** — Locked snapshots survive bulk deletion (the toast reports how many were kept)

To unlock, click the padlock again. Deleting a locked snapshot individually is still possible but requires confirmation.

### 7. Browse Other Workflows

Click the **workflow name** below the header to expand the workflow picker. It lists every workflow that has snapshots in the database, with counts. Click any workflow to view its snapshots — an amber banner confirms you're viewing a different workflow, and "Take Snapshot" is disabled to avoid confusion. Click **Back to current** to return.

This is especially useful for recovering snapshots from workflows that were renamed or deleted.

### 8. Timeline Bar

Enable the timeline in **Settings > Snapshot Manager > Timeline > Show snapshot timeline on canvas**. A centered floating bar appears at the bottom of the canvas with an iconic marker for each snapshot — each icon shows what kind of change the snapshot represents:

<p align="center">
  <img src="assets/timeline-icons.svg" alt="Timeline change-type icons" width="720"/>
</p>

| Icon | Color | Change Type |
|------|-------|-------------|
| Filled circle | Blue | **Initial** — first snapshot after load |
| Plus **+** | Green | **Node Add** — nodes were added |
| Minus **−** | Red | **Node Remove** — nodes were removed |
| Zigzag | Amber | **Connection** — links/wires changed |
| Wave | Purple | **Param** — widget values changed |
| Arrows ↕ | Gray | **Move** — nodes repositioned |
| Star ✱ | Orange | **Mixed** — multiple change types |
| Faded dot | Gray | **Unknown** — legacy snapshot or no detected change |

Additional marker styles are layered on top of the change-type icon:

| Overlay | Meaning |
|---------|---------|
| **Purple background** | Node-triggered snapshot (overrides change-type color) |
| **Yellow border** | Locked snapshot |
| **White ring (larger)** | Active — the snapshot you swapped TO |
| **Green background** | Current — your auto-saved state before the swap |

Click any marker to swap to that snapshot. Hover to see a tooltip with the snapshot name, time, and change description. The **Snapshot** button on the right takes a quick manual snapshot. The bar is centered at 80% width to clear both the sidebar icon strip and bottom-right controls, and tucks behind the sidebar panel when it's open.

The sidebar list also shows the change type in the meta line below each snapshot (e.g., "5 nodes · Parameters changed").

### 9. Auto-save Before Swap

When you swap to an older snapshot (via the sidebar or timeline), the extension automatically captures a "Current" snapshot of your work-in-progress first. This green-marked snapshot appears on the timeline so you can click it to get back. The marker disappears once you edit the graph (since auto-capture creates a proper snapshot at that point). Browsing between existing snapshots does not create additional "Current" entries — the auto-save only triggers on the first swap away from unsaved work.

### 10. Keyboard Shortcut

Press **Ctrl+S** (or **Cmd+S** on Mac) to take a manual snapshot. This works alongside ComfyUI's own workflow save — both fire simultaneously.

### 11. Delete & Clear

- Click **&times;** on any snapshot to delete it individually (locked snapshots prompt for confirmation)
- Click **Clear All Snapshots** in the footer to remove all unlocked snapshots for the current workflow (locked snapshots are preserved)

### 12. Diff View

Compare two snapshots — or a snapshot against the current workflow — to see exactly what changed without touching the graph.

**One-click (vs current workflow):** Click **Diff** on any snapshot to see what changed between that snapshot and your current live workflow.

**Two-snapshot compare:** **Shift+click** **Diff** on snapshot A to set it as the base (purple outline + toast confirmation), then click **Diff** on snapshot B to compare A → B. The base clears after comparison.

The diff modal shows:

| Section | Details |
|---------|---------|
| **SVG comparison** | Side-by-side graph previews at the top — base on the left, target on the right, with highlighted nodes (green = added, red = removed, amber = modified) |
| **Summary pills** | Colored counts — green (added), red (removed), amber (modified), blue (links) |
| **Added Nodes** | Nodes present in the target but not the base |
| **Removed Nodes** | Nodes present in the base but not the target |
| **Modified Nodes** | Nodes with changed position, size, title, mode, widget values, or properties — each change shown as old (red strikethrough) → new (green) |
| **Link Changes** | Added/removed connections with node names and slot indices |

Sections are collapsible (click the header to toggle). If the two snapshots are identical, a "No differences found." message is shown. Dismiss the modal with **Escape**, the **X** button, or by clicking outside.

### 13. SVG Graph Previews

Visually inspect any snapshot without restoring or swapping it.

**Hover tooltip:** Hover over any snapshot in the sidebar list. After 200ms, a small SVG preview appears next to the item showing the graph layout with nodes, links, and groups. Move the mouse away to dismiss.

**Preview modal:** Click the **eye button** on any snapshot to open a full-size preview modal showing the complete graph with node titles, colored link beziers, input/output slot dots, and group overlays. Dismiss with **Escape**, the **X** button, or by clicking outside.

The SVG renderer draws nodes with their stored position, size, and colors. Links are rendered as bezier curves colored by type (blue for IMAGE, orange for CLIP, purple for MODEL, etc.). Collapsed nodes appear as thin title-only strips. Thumbnails (hover tooltips) auto-simplify by hiding labels and slot dots for clarity at small sizes.

## Settings

All settings are available in **ComfyUI Settings > Snapshot Manager**:

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| **Auto-capture on edit** | Toggle | `On` | Automatically save snapshots when the workflow changes |
| **Capture delay** | Slider | `3s` | Seconds to wait after the last edit before auto-capturing (1–30s) |
| **Max snapshots per workflow** | Slider | `50` | Maximum number of unlocked snapshots kept per workflow (5–200). Oldest unlocked are pruned automatically; locked snapshots are never pruned |
| **Capture on workflow load** | Toggle | `On` | Save an "Initial" snapshot when a workflow is first loaded |
| **Max node-triggered snapshots** | Slider | `5` | Rolling limit for SaveSnapshot node captures per workflow (1–50). Node snapshots are pruned independently from auto/manual snapshots |
| **Show snapshot timeline** | Toggle | `Off` | Display a timeline bar at the bottom of the canvas with snapshot markers, active/current indicators, and a quick Snapshot button |

## Architecture

<p align="center">
  <img src="assets/architecture.png" alt="Architecture Diagram" width="100%"/>
</p>

**Auto/manual capture flow:**

1. **Graph edits** trigger a `graphChanged` event
2. A **debounce timer** prevents excessive writes
3. The workflow is serialized and **hash-checked** against the last capture (per-workflow) to avoid duplicates
4. The previous graph state is diffed against the current to **detect the change type** (node add/remove, connection, parameter, move, or mixed) — stored as a `changeType` field on the record
5. New snapshots are sent to the **server** and stored as individual JSON files under `data/snapshots/`
6. The **sidebar panel** and **timeline bar** fetch snapshots from the server and render them with change-type icons
7. **Restore/Swap** loads graph data back into ComfyUI with a lock guard to prevent concurrent operations, and updates the graph cache so the next diff is accurate

**Node-triggered capture flow:**

1. **SaveSnapshot node** executes during a queue prompt run
2. A **WebSocket event** is sent to the frontend, **skipping hash dedup** (the workflow doesn't change between runs)
3. The snapshot is saved with `source: "node"` and pruned against its own rolling limit (`maxNodeSnapshots`)
4. Node snapshots appear in the sidebar with a **purple left border** and **"Node" badge**

**Swap with auto-save:**

1. User clicks **Swap** (sidebar or timeline marker)
2. If the current graph is unsaved work (not already a swapped snapshot), `captureSnapshot("Current")` saves it **before** the swap — browsing between existing snapshots skips this step
3. The target snapshot is loaded into the graph
4. The **timeline** updates: the swapped-to snapshot gets a white ring (active), the auto-saved snapshot gets a green dot (current)
5. Clicking the green dot swaps back; editing the graph clears both markers (the next auto-capture supersedes them)

**Storage:** Snapshots are stored as JSON files on the server at `<extension_dir>/data/snapshots/<workflow_key>/<id>.json`. They persist across browser sessions, ComfyUI restarts, and are accessible from any browser connecting to the same server.

## FAQ

**Where are snapshots stored?**
On the server's filesystem under `<extension_dir>/data/snapshots/`. Each workflow gets its own directory, and each snapshot is an individual JSON file. They persist across browser sessions and are accessible from any browser connecting to the same ComfyUI server.

**I'm upgrading from v1.x — what happens to my existing snapshots?**
On first load after upgrading, the extension automatically migrates all snapshots from your browser's IndexedDB to the server. Once migration succeeds, the old IndexedDB database is deleted. If migration fails (e.g., server unreachable), your old data is preserved and migration will retry on the next load.

**Will this slow down ComfyUI?**
No. Snapshots are captured asynchronously after a debounce delay. The hash check prevents redundant writes.

**What happens if I switch workflows?**
Each workflow has its own snapshot history. Switching workflows cancels any pending captures and shows the correct snapshot list. You can also browse snapshots from other workflows using the workflow picker.

**I renamed/deleted a workflow — are my snapshots gone?**
No. Snapshots are keyed by the workflow name at capture time. Use the workflow picker to find and restore them under the old name.

**Can I use this with ComfyUI Manager?**
Yes — install via ComfyUI Manager or clone the repo into `custom_nodes/`.

## License

[MIT](LICENSE)
