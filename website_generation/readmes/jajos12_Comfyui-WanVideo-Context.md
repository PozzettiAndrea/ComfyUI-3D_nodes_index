# ComfyUI-WanVideo-Context

An advanced context management node for **WanVideo** (and other video diffusion models) in ComfyUI. 
It replaces simple sliding-window history with an **Intent-Aware Mixture of Contexts (MoC)** system.

This node allows your video generation model to "remember" relevant scenes from minutes ago (long-term memory) while maintaining perfect motion continuity (short-term memory), enabling coherent long-form video generation.

## 🚀 Features

### 1. Hybrid Context Strategy
Instead of just feeding the last $N$ frames (which causes drift), this node constructs a hybrid context:
*   **Zone A (Motion Buffer):** Always keeps the last $M$ frames (default 4) to ensure the character's movement doesn't jump-cut.
*   **Zone B (Semantic Memory):** Dynamically retrieves the top $K$ most relevant frames from the entire generated history.

### 2. Multi-Modal Retrieval ("Director Mode")
You can steer the memory retrieval using both Visuals and Text:
*   **Visual Query:** Automatically finds past frames that visually match the current scene.
*   **Text Query:** If you provide a prompt (e.g., "A dark cave"), the node will "read" your script and pull past frames that match that description, even if they look different from the current frame.
*   **Weighted Fusion:** Control the balance via `text_weight` (0.0 = Visual Only, 1.0 = Text Only).

### 3. Diversity Sampling (Soft-NMS)
Prevents the "Clumping" problem where the model retrieves 16 nearly identical frames from the same second. 
*   Uses **Soft Non-Maximum Suppression** to force the selector to pick temporally distinct keyframes (e.g., Frame 100, Frame 350, Frame 800) rather than (Frame 100, 101, 102).

### 4. Smart Caching
*   Includes a sequential embedding cache that prevents slowdowns. 
*   As your video grows to 1000+ frames, the node only runs the heavy CLIP Vision encoder on the *new* frames from the latest batch.
*   **Auto-Invalidation:** Automatically detects if you swap models upstream and clears the cache.

---

## 📦 Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/your-repo/ComfyUI-WanVideo-Context.git
    ```
3.  Restart ComfyUI.

---

## 🔧 Usage

**Node Name:** `WanVideo Context Selector`

### Basic Setup (Sliding Window Replacement)
1.  Remove your existing `GetImageRangeFromBatch` logic inside your loop.
2.  Add **WanVideo Context Selector**.
3.  Connect your accumulated **History Images** map to `images`.
4.  Set `selection_mode` to `contiguous`.

### Advanced Setup (MoC)
1.  Set `selection_mode` to `moc`.
2.  **Required:** Connect a **CLIP Vision** model to `clip_vision`.
3.  **(Optional) Text Control:** Connect your **CLIP** model and **Current Prompt** string.

### Parameters Guide

| Parameter | Default | Description |
| :--- | :---: | :--- |
| **context_size** | 16 | Total number of frames to feed the sampler. |
| **contiguous_size** | 4 | **Hybrid Ratio.** How many "recent" frames must be kept for motion smoothness. |
| **text_weight** | 0.0 | **Fusion Control.** 0.0 relies on visual history. Increase to allow text prompts to steer retrieval. |
| **diversity_radius** | 16 | **De-Clumper.** Penalizes selecting neighbor frames within this radius. Increase to get more diverse history. |
| **similarity_threshold** | 0.0 | **Quality Gate.** If the best match score is below this, the frame is ignored. Reduces hallucinations. |

---

## 🏗️ Architecture
The codebase uses a modular `Strategy` pattern:
*   `core/strategies/moc.py`: Contains the Hybrid + Multi-Modal + NMS logic.
*   `core/cache_manager.py`: Handles caching and invalidation.
*   `nodes/wan_context_node.py`: The ComfyUI interface.

## License
MIT
