# ComfyUI-Rect

Interactive rectangle tools for ComfyUI.

Includes an interactive **Rect / Select** (marching-ants popup) plus **Rect / Crop**, **Rect / Mask**, and **Rect / Fill**.  
Outputs a reusable **RECT** object (`{x,y,w,h}`) **and** the four scalar values for compatibility with existing nodes.

---

## Screenshots
![Rect / Select overlay](assets/RectSelectMarchingAnts.png)

## Example Workflow
![Example workflow](assets/RectSelectNodes.png)

**Load this workflow:** 
[assets/demo-workflow.json](assets/RectExample.json)


## Features
- 🖱️ Interactive selector: draw/refine a box over your input image
- 🧱 Clean **RECT** type + `x/y/w/h` ints
- ✂️ Crop, 🧪 Mask (feather/invert/combine), 🟩 Fill/Outline (color + opacity)
- Bounds-safe, batch-safe, GPU/CPU friendly
- Modular pack layout (easy to extend)

---

## Install
1. Copy the folder **`ComfyUI-Rect`** into:
   ```
   ComfyUI/custom_nodes/
   ```
2. Restart ComfyUI.

> If the **“Open Rect / Select”** button doesn’t appear, it’s almost always cache—use `?nocache=1`.

---

## Nodes

### Rect / Select
**Inputs**
- `image: IMAGE` (required)

**Outputs**
- `rect: RECT` (object with `x,y,w,h`)
- `x: INT`, `y: INT`, `w: INT`, `h: INT`

**UI**
- Button **Open Rect / Select** opens an overlay where you drag a rectangle over the input image. Values sync back to the node.

### Rect / Crop
- **Inputs:** `image: IMAGE`, `rect: RECT`  
- **Output:** `image: IMAGE` (cropped)

### Rect / Mask
- **Inputs:** `image: IMAGE`, `rect: RECT`  
- **Options:** `feather (px)`, `invert`, `combine (replace/union/intersect/subtract/multiply)`  
- **Optional:** `existing_mask: MASK`  
- **Output:** `mask: MASK` (0..1)

### Rect / Fill
- **Inputs:** `image: IMAGE`, `rect: RECT`  
- **Color:** `r,g,b` (0–255), `opacity` (0..1)  
- **Mode:** `fill` or `outline`, `thickness` (outline), `feather`  
- **Output:** `image: IMAGE` (blended)

---

## Quickstart
1. **Load Image** → **Rect / Select** (click *Open Rect / Select*, draw a box)  
2. Feed `rect` to:
   - **Rect / Crop** → get a cropped image, or  
   - **Rect / Mask** → build a mask (then drive any mask-aware node), or  
   - **Rect / Fill** → draw a solid block or outline for redactions/callouts.

---

## RECT type
A simple JSON-like object:
```json
{"x": 100, "y": 80, "w": 256, "h": 256}
```
All coordinates are in **image pixel space**. Values are clamped to the image bounds for safety.

---

## Troubleshooting
- **Button missing (“Open Rect / Select”)** → open with `?nocache=1`.  
- **No image in selector** → ensure the node’s `image` input is connected.  
- **JS not loading** → verify the folder path is exactly `ComfyUI/custom_nodes/ComfyUI-Rect/` and restart ComfyUI.

---

## Roadmap
- Rect / Transform (offset/expand/scale-around-center)  
- Helper: Mask → Rect (BBox) (in companion *MaskTools* pack)

---

## License
MIT
