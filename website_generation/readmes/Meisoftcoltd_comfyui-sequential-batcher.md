# 🔁 ComfyUI Sequential Batcher & Video Loop Master (Beta v0.9.3)

> [!IMPORTANT]
> This version is currently in **BETA**. We have fully transitioned the terminology from "Job" to **Batch** to align with ComfyUI standards and the project name.

The ultimate tool for creating complex iterative workflows and frame-by-frame video processing in ComfyUI. Designed to handle huge tasks (like high-res video generation with Wan2.2 or LTX Video) without crashing your GPU by using intelligent sequential looping instead of VRAM-heavy batching.

## 🚀 Why use this?

Standard ComfyUI batching processes everything at once (4D tensors). For video or large batches, this leads to **Out of Memory (OOM)** errors. 
**Sequential Batcher** allows you to "split" these tasks and process them **one-by-one** (sequentially) within a single "Queue Prompt" run, then "gather" the results back into a single batch or video file.

---

## 🛠️ Installation

1. Clone this repo into `custom_nodes/comfyui-sequential-batcher`.
2. Restart ComfyUI. 
3. Dependencies (`torch`, `numpy`) will be handled automatically if using ComfyUI Manager.

---

## 📖 Key Concepts

- **SEQUENCE**: A simple list of values (numbers, strings, etc.).
- **BATCH**: A structured collection of "steps". Each step has named **Attributes**.
- **Iteration**: The magic happens in nodes like `Batch To List`, `Image Batch To List`, or `Latent Batch To List`. When ComfyUI sees a "List" output from these nodes, it executes all downstream nodes once for each item in that list.

---

## 🎞️ Video Workflow (Wan2.2 / LTX-Video / Future Models)

Video models produce many frames that can easily exceed 24GB VRAM.
1. **Split**: Use `Latent Batch To List` to turn your video latent into a list of single frames.
2. **Process**: Connect to your KSampler/VAE Decoder. ComfyUI will process Frame 1, then Frame 2, then Frame 3...
3. **Gather**: Use `Latent List To Batch` (or `Image List To Batch` if you decoded first) to reconstruct the full video batch for saving.

---

## 🔢 Detailed Node Reference

### 🔄 Loop Category (`🔁 Sequential Batcher/Loop`)
- **🔁 Sequential Loop Index**: The simplest way to start a loop.
  - *Input*: `count` (How many times to run).
  - *Output*: `index` (0, 1, 2...). Useful for seeding or selecting specific items.
- **🔁 Repeat**: Takes any input and repeats it N times.
  - *Input*: `input` (Any), `count` (INT).
  - *Output*: `output` (List of the same input).

### 🛠️ Batch Category (`🔁 Sequential Batcher/Batch`)
- **📂 Load CSV**: Loads a CSV file as a Batch. Now includes a table preview in the workflow.
  - *Input*: `path` (File location), `delimiter`, `quotechar`.
  - *Optional Input*: `index` (To pick a specific row).
  - *Output*: `batch` (The full list), `current_attributes` (Dict of the selected row), `count` (Total rows).
- **📊 Preview Batch**: Displays a table of the batch content in the workflow.
  - *Input*: `batch`, `index` (Highlight specific row), `max_rows`.
- **🛠️ Make Batch**: Turns a sequence into a "Batch" object.
  - *Input*: `sequence` (The data), `name` (The attribute name, e.g., "cfg_scale").
- **🖇️ Combine Batches**: Merges multiple batches.
  - *Modes*: `zip` (paired) or `product` (every combination).
- **🔄 Batch To List**: **CRITICAL**. Converts a Batch into a stream of attributes that triggers the sequential loop.
- **📥 Get Attribute**: Extracts a specific value from the current batch step by its name.

### 🖼️ Image & Latent Category (`🔁 Sequential Batcher/Image` & `/Latent`)
- **🖼️ Image Batch To List**: Splits a [N,H,W,C] tensor into N separate images.
- **🖼️ Image List To Batch**: Reconstructs a batch from iterated images.
- **🎞️ Latent Batch To List**: Splits video latents frame-by-frame for VRAM-safe processing.
- **🎞️ Latent List To Batch**: Merges individual frames back into a video latent batch.
- **⏳ Progress Bar**: Generates a visual progress indicator.

---

## 💡 Pro Tips & Use Cases

### 📝 Using CSV for Prompts and Scenes
You can create a CSV with columns like `prompt`, `negative_prompt`, and `seed`.
1. Use **📂 Load CSV** to load your file.
2. Connect `batch` to **🔄 Batch To List**.
3. Use **📥 Get Attribute** to pull the `prompt` into your CLIP Text Encode.
4. Each row in your CSV will be processed as one "frame" or "job" in the sequence.

### 🎬 Scene Timings for Video
If you have a CSV with `frame_start` and `prompt`, you can use it to change prompts at specific points in a video generation loop.

### 🧪 XY Plots
Use **🖇️ Combine Batches** in `product` mode to create XY Plots (e.g., test every Prompt against every CFG scale).

### 🔍 Automatic Model Iteration
Use **🔍 Model Finder** to automatically iterate through a folder of LoRAs or Checkpoints.
