### ComfyUI Persistent Queue

A simple, friendly way to make your ComfyUI job queue survive restarts and crashes. It remembers what you’ve queued, saves finished jobs (with thumbnails), and adds a clean UI panel to pause/resume, reorder, rename, and manage your queue and history.

This extension does not add new nodes to your graph. It integrates with ComfyUI’s queue and UI directly.

---

### What you get (at a glance)
- **Persistent queue**: Jobs are saved to a small local database and restored on restart.
- **Pause/Resume**: Temporarily stop execution without losing your place.
- **Reorder**: Drag-and-drop reordering.
- **Rename jobs**: Give jobs friendlier names for easier tracking.
- **Delete from queue**: Remove items you no longer want.
- **History with thumbnails**: Finished jobs are saved with small previews.
- **History filter**: Filter by date and time
- **Quick restore**: Drag a history thumbnail back into ComfyUI to restore its workflow.
- **Progress display**: Shows running job progress when available.
- **No extra setup**: Uses ComfyUI’s built-in server and libraries.

---

### Installation

1) Quit ComfyUI if it’s running.

2) Install the extension into your `ComfyUI/custom_nodes` folder. You can:
- **Clone or copy** this folder as `ComfyUI/custom_nodes/ComfyUI-Persistent-Queue`, or
- Download a ZIP of this project and extract it to `ComfyUI/custom_nodes/ComfyUI-Persistent-Queue`.

3) Start ComfyUI.

That’s it. No extra dependencies are typically required on current ComfyUI versions. If you’re on an older environment and see errors about Pillow or aiohttp, install them:

---

### Uninstall

1) Quit ComfyUI.
2) Delete the folder `ComfyUI/custom_nodes/ComfyUI-Persistent-Queue`.
3) (Optional) Delete the local database file if you want to clear saved queue/history:
   - It’s stored in ComfyUI’s user directory as `persistent_queue.sqlite3` (e.g. `ComfyUI/user/persistent_queue.sqlite3`). Deleting this removes the saved queue and history.

---

### How to use the UI

When ComfyUI starts, this extension injects a **Persistent Queue** panel and toolbar button.

- **Open/Close the panel**: Use the toolbar button (or the panel toggle in the UI). If you do not see it, see “Troubleshooting” below.
- The panel has tabs that typically include: **Queue**, **History**, (and may show Gallery/Workflow tools depending on build).

#### Queue tab
- **See what’s running and what’s pending**: The top shows current running job (with progress if available) and the list of pending jobs.
- **Pause / Resume**: Click the Pause/Resume button to temporarily stop or continue automatic execution.
- **Reorder**: Drag-and-drop items to change their execution order.
- **Priority**: Increase/decrease priority to influence ordering. Higher priority runs sooner.
- **Rename**: Give a job a more recognizable name. This is stored with the job for easy identification.
- **Delete**: Remove selected jobs from the queue.

#### History tab
- **Finished jobs list**: Shows recent job runs with small thumbnails.
- **Search & filter**: Filter by status, time, or quickly search by text (when available).
- **Preview**: Click a thumbnail to open a lightweight preview.
- **Restore workflows**: Drag a thumbnail directly into the ComfyUI canvas to load the workflow that produced it. Thumbnails embed workflow info so round-tripping is easy.

Tips:
- Queues are **restored automatically** when ComfyUI restarts. If a job was pending, it will be re-validated and placed back in the queue.
- If an output image can’t be thumbnailed, you’ll still see a placeholder so you can restore the workflow.

---

### Where your data lives
- The extension stores its data in a small SQLite database at:
  - `ComfyUI/user/persistent_queue.sqlite3` (exact path depends on your ComfyUI “user” directory).
- Thumbnails are stored inside that database; your actual images remain in your normal ComfyUI output folders.

---

### FAQ

- **I don’t see any new nodes. Is that expected?**
  Yes. This is an extension that integrates with ComfyUI’s queue and UI; it does not add custom nodes to place on the canvas.

- **My panel doesn’t show up. What should I check?**
  1) Ensure the folder name is exactly `ComfyUI-Persistent-Queue` under `custom_nodes`.
  2) Restart ComfyUI completely.
  3) Check the terminal logs for a line like "ComfyUI-Persistent-Queue initialization failed"—if you see errors about missing packages, install them (see Installation step 3).

- **How do I completely reset the extension?**
  Quit ComfyUI and delete `persistent_queue.sqlite3` from your ComfyUI user folder (see “Where your data lives”). This clears saved queue items and history.

- **Does this slow down ComfyUI?**
  The database is tiny and uses safe defaults. It should have negligible impact in normal use.

---

### Advanced (optional)
For users integrating with external tools, the extension exposes small HTTP endpoints under your ComfyUI server:
- `GET /api/pqueue` — queue state (paused, running, pending, basic progress)
- `POST /api/pqueue/pause` — pause execution
- `POST /api/pqueue/resume` — resume execution
- `POST /api/pqueue/reorder` — reorder by an array of `prompt_id`s
- `PATCH /api/pqueue/priority` — set priority for a `prompt_id`
- `POST /api/pqueue/delete` — delete one or more `prompt_id`s
- `PATCH /api/pqueue/rename` — rename a job (stored in its workflow JSON)
- `GET /api/pqueue/history` — list history (supports pagination, filters, sorting)
- `GET /api/pqueue/history/thumb/{id}` — fetch a stored thumbnail
- `GET /api/pqueue/preview` — lightweight image previews with embedded workflow metadata

Most users won’t need these directly—the UI uses them for you.

---

Enjoy smoother, safer batch runs with a queue that remembers. If you run into problems or have ideas for improvements, please open an issue in the project repository or share feedback where you obtained this extension.
