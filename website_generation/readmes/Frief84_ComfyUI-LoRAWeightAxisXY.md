# ComfyUI-LoRAWeightAxisXY

**XY Input: LoRA Weight (simple)** is a tiny **XY input node** for the *Efficiency Nodes* that lets you **sweep LoRA strength** along one axis of an XY plot.  
It outputs an **XY value of subtype `LoRA`** — a list of triples **`(lora_name, weight, weight)`** — linearly spaced from *min → max* in *steps*.  
This makes it **directly combinable with `XY Input: Checkpoint`** (e.g., X = checkpoint, Y = LoRA weight) without having to use the more constrained “LoRA Plot” modes.

---

## Why this node?

In Efficiency Nodes, the stock XY-plot logic blocks mixing **Checkpoint** with certain **LoRA-special** types (`"LoRA Wt"`, `"LoRA MStr"`, …) when only one axis is LoRA.  
This node sidesteps that by emitting the regular **`LoRA`** subtype with the **same strength applied to Model and Clip**.  
**Result:** you can render **multiple checkpoints × multiple LoRA strengths** in **a single grid**.

**Typical use cases**
- Compare how **one LoRA** behaves across **different checkpoints**.
- Find the **best LoRA weight** (0.0 → 1.0) for a specific checkpoint.
- Quickly explore **LoRA intensity** without the extra constraints of “LoRA Plot”.

---

## Requirements

- **ComfyUI**
- **Efficiency Nodes** (XY Plot + Efficient Loader + KSampler)
- **No additional dependencies**

---

## Installation

### With ComfyUI Manager (recommended)
Use **Install via Git URL**, paste your repository URL, then restart ComfyUI.

### Manual
Place the folder inside your ComfyUI directory and restart:
```text
ComfyUI/custom_nodes/LoRAWeightAxisXY/
  ├─ __init__.py
  └─ lora_weight_axis_xy.py
```

---

## Node overview

**Name:** `XY Input: LoRA Weight (simple)`  
**Category:** `Efficiency Nodes/XY Inputs`

### Inputs
- **`lora_name`** — dropdown from `models/loras` (pick the LoRA to sweep)
- **`min_value`** — start weight (default **0.0**)
- **`max_value`** — end weight (default **1.0**)
- **`steps`** — number of points **including** endpoints (default **3**)  
  → Example: `0.0 → 1.0`, `steps=3` → weights `0.00`, `0.50`, `1.00` (rounded to **2 decimals**)

### Output
- **`XY`** (label: *X or Y*), subtype **`LoRA`**, structure:
```text
[
  [ (lora_name, weight, weight) ],
  [ (lora_name, weight, weight) ],
  ...
]
```

---

## Quickstart (wiring)

1. Add **Efficient Loader** (checkpoint/CLIP/tokenizer as usual)  
   → **`DEPENDENCIES`** → **`XY Plot.dependencies`**
2. **X axis:** `XY Input: Checkpoint` (e.g., two ckpt names) → **`XY Plot.X`**
3. **Y axis:** `XY Input: LoRA Weight (simple)` (choose your LoRA, e.g., `min=0.0`, `max=1.0`, `steps=3`) → **`XY Plot.Y`**
4. **`XY Plot.script`** → **Efficiency Nodes / KSampler.script**  
   *(must be the Efficiency KSampler with a `script` input)*
5. In **XY Plot**, set **`ksampler_output_image = Plot`** *(returns the grid as a single image)*
6. **`KSampler.IMAGE`** → **Save Image**

**Result:** a grid sized `(#checkpoints × #weight-steps)` (e.g., **2×3**).

---

## Notes & limitations

- The node sets **Model and Clip strength to the same value** (`(v, v)`), which is sufficient for most “how strong?” comparisons.  
  If you need separate model/clip axes, use the **standard LoRA XY inputs** — both axes must then be **LoRA-special** types.
- Avoid having a separate **`Load LoRA`** node with fixed weights active in your main path; it can override the sweep.
- Rendering must use the **Efficiency KSampler** (with the `script` input). Core/other KSamplers ignore XY plot scripts.

---

## Troubleshooting

### Only one image instead of a grid
- Confirm the **KSampler** is the **Efficiency Nodes** version (has a `script` input).
- Ensure **`XY Plot.dependencies`** is connected to **Efficient Loader → `DEPENDENCIES`**.
- Set **`ksampler_output_image = Plot`** in XY Plot.
- Check the terminal for an **“XY Plot Error:”** message (then recheck types/wiring).

### Can’t connect the Y axis
- Some XY-plot variants show linkable ports only after clicking the small link/chain icon next to the field.

---

## Examples

### A) 2 checkpoints × 3 LoRA weights
- **X:** `XY Input: Checkpoint` → `[ckpt_A, ckpt_B]`  
- **Y:** `XY Input: LoRA Weight (simple)` → `LoRA=myStyle.safetensors`, range `0.0 → 1.0`, `steps=3`  
→ 6 tiles: A×(0.00, 0.50, 1.00) and B×(0.00, 0.50, 1.00)

### B) LoRA sweep only (single checkpoint)
- **X:** *(empty)*  
- **Y:** `XY Input: LoRA Weight (simple)` → `0.0 → 0.8`, `steps=5`  
→ 1×5 strip

---

## Files

- `__init__.py`  
- `lora_weight_axis_xy.py`

---

## License

MIT © 2025
