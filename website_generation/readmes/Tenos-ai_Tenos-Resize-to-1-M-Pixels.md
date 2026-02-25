# Tenos Resize to \~1 M Pixels

A zero‑nonsense ComfyUI node that resizes every incoming image (or batch) so the final resolution hovers around **one million pixels**—while *respecting* the original aspect ratio *and* snapping both dimensions to multiples of 64. Perfect for pipelines that need a predictable VRAM footprint without destroying composition.

---

## Why you’d use it

* **Stable VRAM budgeting** – 1 Mpx keeps you under GPU‑meltdown territory for SDXL & friends.
* **Clean, divisible dims** – Multiples of 64 mean you never hit those “size must be divisible by 8/16/64” errors again.
* **No potato quality** – Pick from `nearest`, `bilinear`, `bicubic`, or `area`; the node auto‑anti‑aliases when down‑sampling with the smooth modes.
* **Batch‑safe** – Works on full tensors shaped `(B, H, W, C)`; each frame is resized independently.
* **Tenos‑grade math** – Two rounding strategies duel it out under the hood; whichever lands closer to 1 Mpx wins. (It’s nerdy—see the code.)&#x20;

---

## Quick install

1. **Drop it**
   Save `tenos_image_resize_target_pixels.py` into:

   ```text
   ComfyUI/custom_nodes/
   ```

   (Create the folder if it doesn’t exist.)

2. **Restart ComfyUI** – The node shows up under **TenosNodes ➜ Image Processing ➜ Tenos Resize to \~1M Pixels**.

3. **Wire it in** – Feed any image tensor; enjoy harmony.

---

## Node spec

| Field                     | Type / Options                                  | Notes                                             |
| ------------------------- | ----------------------------------------------- | ------------------------------------------------- |
| **Input – image**         | `IMAGE`                                         | 4‑D tensor `(B,H,W,C)`                            |
| **Input – interpolation** | One of `area`, `bicubic`, `bilinear`, `nearest` | Defaults to `bicubic` if you pass something weird |
| **Output – image**        | `IMAGE`                                         | Resized tensor, same batch size                   |

### Constants (tweak in code if you dare)

* `TARGET_TOTAL_PIXELS = 1_000_000` – The sweet spot.
* `DIMENSION_MULTIPLE  = 64` – Keeps UNet / VAE happy.


---

## How it works — the TL;DR math

1. Compute the *ideal* height and width for exactly 1 Mpx at the original aspect ratio.
2. Try rounding **height first** → recalc width → snap both to /64.
3. Try rounding **width first** → recalc height → snap.
4. Whichever candidate lands closer to 1 Mpx wins; ties go to option 1.&#x20;

Edge‑cases handled:

* Zero / negative dims fall back to a 64 × 64 stub.
* If the image already matches the target dims, it passes through untouched (zero extra ops).
* Anti‑aliasing toggles itself **only** when you’re down‑scaling with `bilinear` or `bicubic`.&#x20;

---

## Example workflow (pseudo‑graph)

```text
Loader → Tenos Resize to ~1M Pixels → Txt2Img → Save PNG
```

Need a weird upscale? Just chain it **before** a separate upscale node—this keeps your latent generation predictable.

---

## Performance tips

* **Area** and **nearest** are cheapest but can look crunchy.
* **Bicubic** is slowest but usually prettiest—especially for photo content.
* On big batches, the node loops per‑image, so your VRAM stays flat but it scales CPU‑side.

---

Created with love from Tenos.ai
