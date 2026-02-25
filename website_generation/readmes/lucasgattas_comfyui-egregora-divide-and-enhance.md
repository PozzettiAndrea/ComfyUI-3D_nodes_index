<center>

# **ComfyUI · Egregora: Divide & Enhance** 🧩🚀

**⚡A set of ComfyUI nodes inspired by the Divide & Conquer algorithm, designed to split, enhance, and recombine images for high‑quality upscaling, with prompt mixing and analysis tools for cleaner, sharper results⚡**

<img width="1390" height="619" alt="image" src="https://github.com/user-attachments/assets/db49f88f-c6d4-4b74-899a-eb7e7edab5bb" />

</center>

---

## ✨ What is this?

**Egregora: Divide & Enhance** is a small suite of custom nodes that help you **split, enhance, and recombine** images, plus a clean **SDXL prompt mixer** that keeps things simple while staying robust with lots of customization.

Inspired by **Steudio’s Divide & Conquer** nodes, adapted and refactored to fit a streamlined upscaling workflow. 🧠✂️🧵

> **Why it’s special**
>
> * **Deterministic plan**: the same coordinate generator drives both **Divide** and **Combine**, so tiles align 1:1.
> * **Seam‑aware recomposition**: a controllable **edge‑feather transparency** (per‑tile) hides straight borders without creating gaps.
> * **Order you can trust**: linear, serpentine, spiral (in/out), and content/dependency‑aware orders for stable, reproducible passes.
> * **Preview before compute**: a visual overlay shows grid, overlaps, order, and feather zones.
> * **Minimal prompts, strong conditioning**: a turbo prompt node that just works with SDXL (with blacklist support).

---

## 🧱 Included Nodes

### 🚀 Egregora Turbo Prompt

A minimal, predictable prompt builder:

* **Positive** = `caption_text + global_positive_prompt` (plain concatenation; no weights).
* **Negative** = `global_negative_prompt` only.
* **Blacklist (optional):** removes whole‑word, case‑insensitive terms from the positive text before encoding.
* Outputs **SDXL‑compatible CONDITIONING** with proper pooled output.

**Typical wiring**

* `caption_text` ← captioner (e.g., Florence2)
* `global_positive_prompt` ← styles/quality you always want
* `global_negative_prompt` ← artifacts to avoid
* `blacklist_words` ← optional removals

---

### 🧠 Egregora Algorithm

Planner for Divide‑and‑Enhance upscaling.

**What it does**

* Computes an **upscaled canvas** that meets your **minimum scale factor**.
* Derives a **grid** of tiles from your **tile width/height** and **overlap**.
* Supports multiple **tile orders**: `linear`, `serpentine`, `spiral_outward`, `spiral_inward`, `content_aware`, and `dependency_optimized`.
* Uses the same coordinate logic consumed by **Divide & Select** and **Combine**, ensuring **perfect positional consistency**.

**Why it matters**

* Prevents off‑by‑one and drift errors between split and merge phases.
* Gives you predictable coverage for denoising/upscaling passes.

---

### ✂️ Egregora Divide & Select

Splits an image according to the planner.

**Highlights**

* Emits **all tiles** or lets you **select a specific tile** for targeted enhancement.
* Uses the **exact coordinates** and **order** from **Egregora Algorithm**.

---

### 🔗 Egregora Combine

Merges processed tiles back into a seamless image using **order‑dependent alpha‑over** with a **per‑tile edge‑feather mask**.

**How the seam fix works**

* Each tile gets an **analytic feather** that fades from **0 → 1** over a user‑controlled **`feather_size`**.
* Feather is **applied only on internal sides** (outer canvas edges stay solid).
* Effective feather is **clamped to the tile overlap**, so you **don’t create holes**.
* Because the **same coordinates** are used as in Divide/Algorithm, the blend lands exactly where it should.

**Tips**

* Start with `feather_size` between **8–64 px**; keep it **≤ min(overlap\_x, overlap\_y)**.
* Use **Preview** to visualize feather bands vs. overlaps.

---

### 👁️ Egregora Preview

Visual overlay to preview the plan **before** you spend compute:

* Draws **tile boundaries**, **overlap zones**, **processing order**, and **feather bands** for sanity checks.

---

### 🔍 Egregora Content Analysis *(optional)*

Analyzes gradient complexity to suggest:

* **Feather size** (more for complex scenes),
* **Overlap** adjustments, and
* A recommended **blending method** mindset (feather‑first, then overlap).

---

## 📦 Installation

1. Clone into ComfyUI’s custom nodes folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/lucasgattas/comfyui-egregora-divide-and-enhance.git
```

2. Ensure the folder contains `__init__.py` and `egregora_divide_and_enhance.py`.
3. Restart ComfyUI. Nodes appear under **Egregora/**.

> **Note:** You can rename the Python file; the package `__init__.py` controls what gets imported.

---

## 🛠️ Minimal Workflow (SDXL)

**Goal:** Use Turbo Prompt for text conditioning and keep the rest of your graph simple.

1. **Load Model (SDXL)** → **CLIP**
2. **Egregora Turbo Prompt**

   * *caption\_text* = your main description
   * *global\_positive\_prompt* = secondary style or theme
   * *blacklist\_words* = clean words from positive prompt (caption and global)
3. **KSampler** (Euler/Karras or your favorite)

   * Positive/Negative from Turbo Prompt, model & latent as usual.
4. **VAE Decode** → **Preview / Save**

**Upscaling (Divide & Enhance):**
Use **Algorithm → Divide & Select → \[process tiles] → Combine**. Start with moderate tile sizes and overlap; preview first.

---

## 📥 Example Workflow (.json)

<img width="1130" height="742" alt="Captura de tela 2025-08-27 220324" src="https://github.com/user-attachments/assets/91735827-b882-45d7-bf17-d90fd23ed100" />

* **Download:** `examples/divide_and_enhance_example_workflow.json` (included in this repo).
* **Import:** ComfyUI → Queue (☰) → **Load** → pick the JSON, or just drag it inside.

> **Prefer a one‑click experience?** Run the **improved, full tuned upscaler** on the cloud with the best settings at **([https://egregoralabs.com](https://egregoralabs.com))**.

---

## 🎚️ Practical Tips

* Keep prompts **concise**; long texts dilute signal.
* For realism vs. cartoon conflicts, add targeted **negatives** (e.g., `cartoon, plush, chibi`).
* For seams: increase **overlap** a step *or* raise **feather\_size** (stay ≤ overlap). Use **Preview** to inspect.
* Large tiles reduce passes but increase VRAM — balance tile size vs. overlap for your GPU.

---

## 🧪 Troubleshooting

* **Flat/grey outputs** → raise steps slightly or increase the stronger slider; ensure the CLIP/model are SDXL compatible.
* **Repetitions/Grid looks** → verify no external tiling patches are active; reduce extreme overlaps or tile size if using Divide/Combine.
* **Shape/key errors** → update to the latest version; Turbo Prompt sets pooled output; make sure you pass a valid LATENT.

---

## 🧾 Folder Structure

```
comfyui-egregora-divide-and-enhance/
├─ __init__.py
├─ egregora_divide_and_enhance.py
├─ README.md  ← you are here
├─ examples/
└─  └─ divide_and_enhance_example_workflow.json
```

---

## 🙌 Credits

* Inspired by **Steudio’s Divide & Conquer** node suite and community best practices around SDXL conditioning and tiling.
* Built for clarity: minimal controls, sensible defaults, strong integration with ComfyUI.

---

## 📜 License

**GPL‑3.0** — see [LICENSE](LICENSE).

---
