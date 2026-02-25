# ComfyUI-multiGPU-upscaler

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Multi-GPU batch-parallel upscaling nodes for ComfyUI.

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Performance](#performance)
* [Installation](#installation)
* [Nodes](#nodes)
    * [multiGPU\_upscaler: Multi-GPU Batch Parallel](#multigpu_upscaler-multi-gpu-batch-parallel)
* [Recommended Settings](#recommended-settings)
* [Tips & Debugging](#tips--debugging)
* [License](#license)

---

## Features

This extension is designed to:

* Use 1–10 GPUs efficiently.
* By default, auto-detect and use up to 2 GPUs.
* Split batched images across GPUs and upscale them in parallel.
* Use robust tiled upscaling with OOM-safe fallback.
* Work great with RealESRGAN / ESRGAN style models (e.g. `RealESRGAN_4xplus`).

**Tested with:**

* Dual RTX 3060 setup
* SDXL generation + 4x RealESRGAN upscaling, batch 4–8
* Achieved measurable speedups vs single-GPU upscaling.

---

## Requirements

* **NVIDIA GPUs only.** This extension relies on CUDA for device management and communication.

---

## Performance

Here are some sample benchmarks comparing a standard `Upscale Image (using Model)` node against the `multiGPU_upscaler` node.

* **Test Setup:** Dual RTX 3060
* **Workflow:** SDXL Generation + 4x RealESRGAN Upscaling
* **Resolution:** 1024x1024 upscaled to 4K (4096x4096)
* **Batch Size:** 8 (split as 4 images per GPU in the multi-GPU test)

| Run Type | Standard Upscaler (1 GPU) | multiGPU Upscaler (2 GPUs) | Speedup |
| :--- | :--- | :--- | :--- |
| **Cold Run (gen0)** | 261.81s | 233.53s | ~10.8% |
| **Run 1 (gen1)** | 259.57s | 223.22s | ~14.0% |
| **Run 2 (gen2)** | 251.65s | 226.82s | ~9.9% |

*Results show a measurable speedup, especially on repetitive runs, by parallelizing the upscale task across both GPUs.*

---

## Installation

1.  Go to your ComfyUI `custom_nodes` directory.

    Example:
    ```bash
    cd ComfyUI/custom_nodes
    ```

2.  Clone this repository:
    ```bash
    git clone [https://github.com/alludus/ComfyUI-multiGPU-upscaler.git](https://github.com/alludus/ComfyUI-multiGPU-upscaler.git)
    ```

    Or download the ZIP from GitHub and extract it to:
    ```text
    ComfyUI/custom_nodes/ComfyUI-multiGPU-upscaler/
    ```

3.  Ensure the structure looks like this:
    ```text
    ComfyUI/custom_nodes/ComfyUI-multiGPU-upscaler/__init__.py
    ComfyUI/custom_nodes/ComfyUI-multiGPU-upscaler/multiGPU_upscaler.py
    ```

4.  Restart ComfyUI.

All nodes will appear under the category:

* `multiGPU_upscaler`

---

## Nodes

### multiGPU\_upscaler: Multi-GPU Batch Parallel

Main node. Splits the batch across multiple GPUs and upscales in parallel.

Best for:
* Batch size ≥ 4
* 2 or more GPUs
* Post-generation upscaling (e.g. SDXL → 8 images → 4x RealESRGAN upscale)

* **Inputs:**
    * `upscale_model`: **Note:** Load this using a standard `Load Upscale Model` node.
    * `image`: Batched input tensor from ComfyUI.
    * `device_list`:
        * How to select GPUs.
        * `auto` (default): Uses up to `auto_max_devices` GPUs with the most free VRAM.
        * Custom list (Examples: `cuda:0,cuda:1` or `0,1,2`).
        * Up to 10 GPUs supported.
    * `auto_max_devices`:
        * Default: `2`
        * Used only when `device_list = "auto"`.
        * Limits the number of GPUs auto mode uses.
    * `primary_share`:
        * Default: `0.5`
        * Approximate fraction of the batch assigned to the first (best) GPU.
        * If one GPU is stronger or has more free VRAM, increase (e.g. `0.7`).
    * `tile_size`:
        * Default: `512`
        * Starting tile size on all GPUs. Automatically reduced on OOM.
    * `min_tile_size`:
        * Default: `128`
        * Smallest allowed tile size before failing.
    * `overlap`:
        * Default: `32`
        * Tile overlap in pixels.

* **Behavior:**
    * **Determines GPUs:**
        * If `device_list` is set: Uses exactly that set (filtered by availability).
        * If `device_list = "auto"`: Uses up to `auto_max_devices` GPUs with the most free VRAM.
    * **Splits Batch:**
        * First GPU receives about `primary_share` of the images.
        * Remaining GPUs share the rest.
    * **Executes:**
        * Spawns a worker thread for each GPU.
        * Each worker instantiates its own copy of the model on that GPU.
        * Each worker runs tiled upscaling on its subset with OOM-safe tiling.
    * **Finishes:**
        * Outputs are concatenated in the original batch order.
        * If any worker errors or OOMs, it falls back to a single-GPU tiled upscale on the best available GPU.

---

## Recommended Settings

For a setup like:
* 2x RTX 3060
* SDXL generation
* RealESRGAN\_4xplus 4x upscaling
* Batch size 4–8

**Recommended Node:** `multiGPU_upscaler: Multi-GPU Batch Parallel`

* **Settings:**
    * `device_list`: `auto`
    * `auto_max_devices`: `2`
    * `primary_share`: `0.5`
    * `tile_size`: `512`
    * `min_tile_size`: `128`
    * `overlap`: `32`

This configuration lets the extension pick the two best GPUs, splits work evenly, and uses robust tiling.

---

## Tips & Debugging

* **If you encounter OOM:**
    * Lower `tile_size` (e.g. to `256`).
    * Optionally increase `min_tile_size` to reduce retries.
* **If one GPU is stronger:**
    * Increase `primary_share` (e.g. `0.6`–`0.8`) so it does more work.
* **Debugging:**
    * Watch the ComfyUI console/log for `[multiGPU]` messages.
    * Use `nvidia-smi` to confirm multiple GPUs are active during upscaling.

---

## License

This project is released under the **Apache 2.0 License**.

See the `LICENCE` file for details.
