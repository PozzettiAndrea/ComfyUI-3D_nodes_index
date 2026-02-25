# ComfyUI ▸ Trajectory Drawer

> Recreate motion trails in a single picture on top of any single image and export every intermediate frame.

https://github.com/user-attachments/assets/8e9dec19-28f2-4621-b072-f6c2db51eb29

https://github.com/user-attachments/assets/d738882e-668b-4f7f-a627-9952148d63b3

<img width="1046" height="834" alt="Image" src="https://github.com/user-attachments/assets/04e2fa15-4775-4c6d-9aa7-5481c272c3c6" />
<img width="932" height="1163" alt="Image" src="https://github.com/user-attachments/assets/4406aa93-d70a-441e-b134-02986c23c9bd" />
## Highlights

- ✅ **Shift + drag painting** – The node ships with an interactive canvas: hold `Shift`, drag to paint, release to finish the stroke. No extra tools required.
- ✅ **Customizable look** – Tune stroke width, color, glow decay, sampling density, and background dim to match the neon trail aesthetics in the reference video.
- ✅ **Per-frame output** – The node returns an `IMAGE` batch representing the entire drawing animation, ready to be piped into `SaveImage`, `VideoHelperSuite`, etc.
- ✅ **JSON trajectory** – All stroke data is persisted as JSON inside the workflow so you can version, reuse, or share it effortlessly.

## Installation

```
ComfyUI/custom_nodes/ComfyUI-Trajectory
```

Restart ComfyUI and the node will appear under **“🧭 Trajectory”**.

## Node Parameters

| Parameter | Description |
|-----------|-------------|
| `base_image` | Image to draw on (only the first frame of the batch is used). |
| `path_json` | Trajectory JSON produced by the built‑in editor. Click “Edit Trajectory (Shift Draw)” to open it. |
| `stroke_width` | Stroke width in pixels. |
| `frames_per_segment` | Extra interpolation samples inserted between adjacent points. Higher values = smoother trails. |
| `line_color` | Stroke color (`#00f0ff`, `r,g,b`, etc.). |
| `tail_alpha` | Opacity of the main stroke (0–1). |
| `background_dim` | Darkens the base image before drawing so the trail pops out. |
| `trail_decay` | Per-frame decay factor (default 0.3). Values <1 create persistent light trails; smaller values decay slower. |
| `line_style` | Stroke style (`solid` or `neon`). |
| `fps` | Output frame rate (use the same value when assembling a video). |
| `duration_seconds` | Target animation duration. Set to 0 to derive from stroke length. |
| `show_pointer` | Draw a pointer arrow in the output (for presentations/debug) without affecting the glow. |

Outputs:
- `frames` (`IMAGE`): the animation frames showing the trail being drawn.
- `info` (`STRING`): JSON metadata (fps, resolution, decay settings, etc.).
- `tracks_json` (`STRING`): the full list of pixel coordinates (e.g. `[{"x":309,"y":338}, ...]`) for downstream nodes or scripts.

## Canvas Workflow

1. Click **“Edit Trajectory (Shift Draw)”** on the node.
2. Optionally load any PNG/JPG reference. The canvas automatically adopts the image’s original resolution and persists it for the next edit session.
3. Hold `Shift` and drag with the left mouse button to draw; release to finish a stroke.
4. Use **Undo** / **Clear** for quick fixes, **Export PNG** to snapshot the current view.
5. Hit **Apply Path** to store the JSON back into `path_json`, then run the workflow to render frames.

> On touch devices you can draw directly. On desktop, holding `Shift` is required; otherwise the canvas shows a reminder.

## Example Pipelines

1. `LoadImage` → `TrajectoryDrawer` → `SaveImage` (PNG sequence).
2. `LoadImage` → `TrajectoryDrawer` → `VideoHelperSuite ▸ ImagesToVideo` (render MP4/GIF).

## Matching the Reference Video

- Import a still frame from `large-motion-1-top.mp4` as the reference image to trace the exact path.
- Increase `frames_per_segment`, lower `stroke_width`, and set `background_dim` to ~0.2–0.4 to mimic the glowing trail look.

## Limitations

- Only the first image in the batch is used. Split batches upstream if you need multiple trajectories.
- The JSON stores the reference image Base64 and size, but not the original file path—keep backups if necessary.

Feel free to extend the node (multi-color trails, speed curves, etc.) according to your workflow needs.
