# ComfyUI_DeleteModelPassthrough_ExecutionFlowControl (WIP)
A memory management custom node

## 📌 Overview
This custom node provides a **memory management utility** for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).  
It allows you to **delete a specific model** (checkpoint, etc.) completely from **VRAM and system RAM** after use, while **passing through any other input type unchanged** (IMAGE, LATENT, CLIP, STRING, INT, CONDITIONING, VAE, etc.). It also contains experimental nodes which can be used to modify the order of execution in comfyUI for better memory management.

This is especially useful for **low VRAM & low RAM environments**, helping to reduce *out-of-memory (OOM) errors* in long workflows.

---

## ⚙️ Node Details
- **Name:** `Delete Model (Passthrough Any)`  
- **Inputs:**
  - `data` → any input type (IMAGE, LATENT, CLIP, STRING, INT, CONDITIONING, VAE, etc.)
  - `model` → the MODEL you want to remove
- **Outputs:**
  - The `data` input, passed through unchanged
- **Effect:**  
  Deletes the `model` completely from Python, VRAM, and RAM using:
  ```python
  del model
  torch.cuda.empty_cache()
  gc.collect()


## 🛠️ Installation

1. Navigate to your ComfyUI custom_nodes folder:
  ```python
  cd .../ComfyUI/custom_nodes
  ```

2. Clone or copy this repository into the folder:
  ```python
  git clone https://github.com/Isi-dev/ComfyUI_DeleteModelPassthrough_ExecutionFlowControl
  ```
3. Install dependencies:
  ```python
  pip install -r requirements.txt
  ```

## 📝 Usage

Assume you have a large CLIP model that you want to remove from VRAM (without unloading it into low system RAM) before loading your diffusion model to avoid OOM errors:

- Connect the output from the CLIPTextEncode node into this node’s data input.

- Connect the output from the CLIPLoader node into this node’s model input.

- Connect the output from this node into your sampler node.

The CLIP model will be deleted from memory after use, while your encoded text (data) continues downstream into the workflow.


## 🔍 How This Node Differs from Normal ComfyUI Memory Management

By default, ComfyUI has its own memory manager that tries to balance VRAM and system RAM usage:

When a model is not needed in VRAM, ComfyUI may move it from VRAM to system RAM (“unloading” it) so it can be reloaded faster later.

This is efficient if you have enough RAM, because models don’t need to be reloaded from disk each time.

However, in low RAM environments, this behavior can cause your system RAM to fill up, leading to slowdowns or even OOM crashes.


## ⚖️ Downsides of Using This Node

While this node is powerful for low-memory setups, there are trade-offs:

**Slower reloads**

Since the model is completely deleted, if you need it again later in the workflow, ComfyUI must reload it from disk.

Disk loads are much slower than reloading from RAM.

**No caching benefit**

ComfyUI’s memory manager caches models to speed up reuse.

This node removes that cache advantage; models won’t be instantly available later.

**Workflow fragility**

If another node down the line expects the model still to exist, your workflow may break.

This node is best used only when you’re sure the model will not be needed again.

**One-way action**

Once deleted, the model is gone. There’s no “undo” unless it is explicitly reloaded by another loader node.


## 📝 When to Use This Node

You have low VRAM and low system RAM.

You want to run multiple heavy models in a single workflow without hitting OOM errors.

You are done using a model (e.g., CLIP for text encoding, or a helper model), and it won’t be needed again later.


## 🚫 When Not to Use This Node

If you have enough RAM and want to benefit from ComfyUI’s smart caching.

If you plan to use the same model multiple times in the workflow.
