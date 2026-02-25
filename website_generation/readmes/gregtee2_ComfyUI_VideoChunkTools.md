# ComfyUI VideoChunkTools

**10 utility nodes for generating long videos in ComfyUI by splitting them into overlapping chunks with rolling reference frames.**

Designed to solve the **"context window reversal" problem** — where video generation models (Wan 2.1/2.2, FantasyPortrait, etc.) revert to the starting state after ~135 frames because the reference image embedding pulls the generation back.

Now with **per-chunk text prompting** — change the narrative as your video progresses.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Nodes-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## The Problem

Most image-to-video models have a limited context window (~81–137 frames). When you try to generate longer videos, the model "forgets" the accumulated motion and snaps back to looking like frame 1. The result is an obvious loop or identity shift.

## The Solution

**Rolling Reference**: Generate video in chunks, using the **last frame** of each chunk as the **reference image** for the next chunk. This keeps identity consistent while allowing pose/action to progress naturally.

```
Chunk 0: [ref=original portrait]  → 81 frames → last frame becomes next ref
Chunk 1: [ref=chunk 0 last frame] → 81 frames → last frame becomes next ref
Chunk 2: [ref=chunk 1 last frame] → 81 frames → ...
Final:   Concatenate all chunks → 240+ frame seamless video
```

---

## Nodes

### Core Utility Nodes (7 nodes — no dependencies beyond ComfyUI)

| Node | Purpose |
|------|---------|
| **Extract Video Chunk** | Pull chunk N from a longer driving video, with configurable overlap |
| **Blend Video Chunks (Crossfade)** | Crossfade-blend two overlapping pixel-space chunks into one seamless video |
| **Blend Latent Chunks (Pre-Decode)** | Join two latent chunks before VAE decode — supports slerp, hard_cut, crossfade |
| **Concat Video Chunks** | Simple concatenation with optional first-frame trim (for rolling reference) |
| **Get Frame By Index** | Extract a single frame by index (-1 = last frame = next reference) |
| **Get Frame Range** | Extract a range of frames with negative indexing support |
| **Video Chunk Planner** | Calculate chunking strategy — shows chunk count, frame ranges, workflow steps |

### Wan-Specific Nodes (2 nodes — require [ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper))

| Node | Purpose |
|------|---------|
| **Wan Chunked I2V Sampler ♾️** | All-in-one node: encode→sample→decode→extract ref→repeat. Supports per-chunk text prompting. |
| **Wan Chunk Calculator 🧮** | Calculate exact total_frames for N chunks with 4n+1 normalization |

### Text Conditioning Node (1 node — for per-chunk prompting)

| Node | Purpose |
|------|---------|
| **Chain Text Embeds 🔗** | Chain multiple WanVideoTextEncode outputs into an ordered sequence for per-chunk text conditioning |

> The Wan nodes gracefully degrade — if WanVideoWrapper isn't installed, the 7 core nodes still load and work fine.

---

## Installation

### Option 1: ComfyUI Manager (Recommended)
Search for `VideoChunkTools` in ComfyUI Manager and click Install.

### Option 2: Git Clone
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/gregtee2/ComfyUI_VideoChunkTools.git
```

### Option 3: Manual Download
Download the ZIP from GitHub, extract to `ComfyUI/custom_nodes/ComfyUI_VideoChunkTools/`.

**Restart ComfyUI after installation.**

No pip dependencies required — uses only PyTorch (already in ComfyUI).

---

## Workflows

### Rolling Reference (Manual — Any I2V Model)

Use the core utility nodes to build a rolling-reference pipeline with any image-to-video model:

1. **Video Chunk Planner** → See how many chunks you need
2. **Extract Video Chunk** (index=0) → Get first driving chunk
3. Run your I2V model with your **original reference image**
4. **Get Frame By Index** (index=-1) → Extract last frame as new reference
5. **Extract Video Chunk** (index=1) → Get next driving chunk
6. Run your I2V model with the **new reference**
7. **Blend Video Chunks** or **Concat Video Chunks** → Join the results
8. Repeat for each chunk

### All-In-One (Wan Models)

The **Wan Chunked I2V Sampler** handles everything in a single node:

1. Connect your Wan model, VAE, and start image
2. Set `total_frames` (e.g., 241 for ~15 seconds at 16fps)
3. Set `chunk_frames` (e.g., 81)
4. Hit Queue — the node generates all chunks automatically

**Features:**
- **Single-pass** or **Two-pass** sampling (connect `model_b` for split denoising)
- **FLF (First-Last-Frame)** — connect an `end_image` to guide the final frame
- **Multi-keyframe FLF** — provide a batch of end images to distribute across chunks
- **Crossfade overlap** — set `end_blend_chunks` for smooth FLF transitions
- **Auto 4n+1 normalization** — chunk sizes are automatically adjusted for Wan's requirements
- **Per-chunk text prompts** — connect a `ChainTextEmbeds` node to change the text conditioning per-chunk

### Per-Chunk Text Prompting (Wan Models)

Change the narrative as your video progresses — each chunk can have its own text prompt:

1. Add multiple **WanVideoTextEncode** nodes, each with a different prompt
2. Connect them to a **Chain Text Embeds 🔗** node (`embed_1`, `embed_2`, `embed_3`, ...)
3. Connect the `embed_sequence` output to the sampler's `text_embed_sequence` input
4. Chunk 1 uses embed_1, chunk 2 uses embed_2, etc.
5. If you have fewer prompts than chunks, the last prompt repeats for remaining chunks

```
[WanVideoTextEncode: "A cat sleeps on a sofa"]──┐
[WanVideoTextEncode: "The cat wakes up"]─────────┼──▶ [Chain Text Embeds 🔗]──▶ text_embed_sequence
[WanVideoTextEncode: "The cat jumps off"]────────┘
                                                              │
[Wan Model + VAE + Image]──────────────────────────▶ [Wan Chunked I2V Sampler ♾️]
```

> **Tip**: You can still use the single `text_embeds` input if you want the same prompt for all chunks. The sequence input takes priority when connected.

---

## Node Details

### Extract Video Chunk

Divides a video into chunks with overlap. Adjacent chunks share `overlap_frames` at their boundary.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| images | IMAGE | — | Full driving video |
| chunk_index | INT | 0 | Which chunk to extract (0-based) |
| chunk_frames | INT | 81 | Frames per chunk |
| overlap_frames | INT | 16 | Frames shared between adjacent chunks |

| Output | Type | Description |
|--------|------|-------------|
| chunk | IMAGE | Extracted chunk |
| total_chunks | INT | How many chunks cover the full video |
| chunk_index | INT | Pass-through for chaining |
| is_last_chunk | BOOLEAN | True if this is the final chunk |

### Blend Video Chunks (Crossfade)

Crossfade two overlapping pixel-space chunks. The last N frames of chunk_a smooth-transition into the first N frames of chunk_b.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| chunk_a | IMAGE | — | First (earlier) chunk |
| chunk_b | IMAGE | — | Second (later) chunk |
| overlap_frames | INT | 16 | Frames to crossfade |
| blend_curve | ENUM | ease_in_out | linear, ease_in_out, sigmoid |

### Blend Latent Chunks (Pre-Decode)

Join two 5D video latents along the temporal dimension **before** VAE decode. Operates in latent space — overlap is in latent frames (Wan: pixel_overlap / 4).

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| latent_a | LATENT | — | First latent chunk |
| latent_b | LATENT | — | Second latent chunk |
| overlap_frames | INT | 4 | Overlap in latent temporal frames |
| blend_curve | ENUM | hard_cut | hard_cut, slerp, linear, ease_in_out, sigmoid |

**hard_cut** (recommended for rolling reference): Clean cut at the overlap midpoint — no dissolve artifacts.

**slerp**: Spherical linear interpolation — preserves latent vector magnitude. Standard technique for diffusion model interpolation.

### Concat Video Chunks

Simple concatenation. For rolling-reference workflows where chunk B's first frame naturally matches chunk A's last frame.

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| chunk_a | IMAGE | — | First chunk |
| chunk_b | IMAGE | — | Second chunk |
| trim_b_start | INT | 1 | Frames to trim from B's start (1 = drop duplicate ref frame) |

### Get Frame By Index

Extract a single frame. Use `-1` for the last frame (rolling reference).

### Get Frame Range

Extract a range of frames. Supports negative indexing. `end=0` means "to the end".

### Video Chunk Planner

Outputs the total number of chunks needed and a detailed text plan showing frame ranges and workflow steps.

### Wan Chunked I2V Sampler ♾️

All-in-one node for Wan I2V models. See the [Workflows](#all-in-one-wan-models) section above.

### Wan Chunk Calculator 🧮

Simple math: calculates `total_frames = chunk_frames + (num_chunks - 1) * (chunk_frames - 1)` with 4n+1 normalization.

### Chain Text Embeds 🔗

Chains up to 8 pre-encoded text embeddings into an ordered sequence for per-chunk text conditioning.

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| embed_1 | WANVIDEOTEXTEMBEDS | Yes | Text embedding for chunk 1 |
| embed_2–embed_8 | WANVIDEOTEXTEMBEDS | No | Text embeddings for chunks 2–8 |

| Output | Type | Description |
|--------|------|-------------|
| embed_sequence | TEXT_EMBED_SEQUENCE | Ordered list of embeddings — connect to sampler's `text_embed_sequence` input |

If you have fewer embeds than chunks, the last embed repeats for all remaining chunks. Non-connected slots are skipped (embed_1 + embed_3 = 2-entry sequence).

---

## Tips

- **Overlap of 16 frames** works well for most cases (about 1 second at 16fps)
- **ease_in_out blend curve** gives the smoothest pixel-space transitions
- **hard_cut in latent space** is usually best — rolling reference already makes the overlap zone match
- **slerp** is the gold standard for latent interpolation if you need blending
- For Wan models, **chunk_frames must be 4n+1** (5, 9, 13, ..., 77, 81, 85, ...). The nodes auto-normalize this.
- Use **Video Chunk Planner** first to understand how your video will be divided

---

## Requirements

- **ComfyUI** (any recent version)
- **PyTorch** (included with ComfyUI)
- **[ComfyUI-WanVideoWrapper](https://github.com/kijai/ComfyUI-WanVideoWrapper)** — only needed for the 2 Wan-specific nodes. The 7 core nodes work without it.

---

## License

MIT — see [LICENSE](LICENSE)

---

## Credits

Built by [Greg Tee](https://github.com/gregtee2) for the ComfyUI community.
