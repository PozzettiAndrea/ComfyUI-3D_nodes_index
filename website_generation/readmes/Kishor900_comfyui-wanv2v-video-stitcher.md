# ComfyUI WANv2v Video Stitcher & ControlNet Manager

🚀 **ComfyUI custom node pack for WAN v2v long-video generation**.  
This pack provides all the tools you need to build **seamless long-form videos** using **chunking + overlap stitching** techniques. It includes debug nodes, iteration-based control group orchestration, and a de-overlap merge node to produce smooth transitions without frame duplication.

---

## ✨ What You Get with This Pack
- **Seamless long video generation**: Split videos into overlapping chunks, process with WAN v2v, then stitch without artifacts.
- **Chunk + overlap orchestration**: Handle `chunk_size` and `overlap_size` automatically across iterations.
- **De-overlap merging**: Drop duplicate frames from overlapping regions for a clean final sequence.
- **Debug-friendly workflow**: Visualize frame numbering to ensure sequential order without skips or repeats.
- **Ready for ControlNet pipelines**: Works with ControlNet batches for consistent conditioning.

This pack is especially useful if you are generating videos with **WAN v2v** where the KSampler must process limited frame chunks (e.g., 81 frames) and you want to stitch them into **one continuous video**.

---

## 🧩 Nodes Included

### 1. **WanV2V Debug: Number Batch**
- Input: `IMAGE` batch  
- Output: Same batch with numbers stamped in the **top-right corner** (1,2,3...).  
- **Purpose**: Debug sequential frame flow across nodes.  
- ✅ Helps verify frame order and detect overlaps/skips.

---

### 2. **WanV2V: Iter Control Group**
- Inputs:  
  - `controlnet_images` (full ControlNet frame sequence)  
  - `prev_output` (optional, previous sampler output)  
  - `chunk_size`, `overlap_size`, `iter`, `fps`  
- Outputs:  
  - `control_group` (IMAGE batch for this iteration)  
  - `info` (summary string with frame ranges, drops, padding info)  
- **Purpose**: Builds each chunk for WAN v2v long-video generation.  
- **Logic**:  
  - Iter 1: Takes first `chunk_size` frames.  
  - Iter ≥2: Prepends `last x frames` from previous sample, adds residue from prior group, and appends current frames while dropping overlaps.  
  - Final Iter: Supports **conclusive stitching** by padding tail frames if ControlNet frames run out.  
- ✅ Ensures no skipped or duplicated frames across iterations.

---

### 3. **WanV2V: Merge De-Overlap (10x)**
- Inputs: Up to 10 `IMAGE` batches (`image_1 ... image_10`), plus `overlap_size`.  
- Output: A **single merged sequence** with overlaps removed.  
- **Purpose**:  
  - Removes first `x` frames from every batch except the first.  
  - Concatenates sequentially → clean video-ready batch.  
- ✅ Final step before video export.

---

## 🔧 Installation
1. Navigate to your ComfyUI `custom_nodes` folder:
   ```bash
   cd ComfyUI/custom_nodes
   
2. Clone this repo:
  ```bash
  git clone https://github.com/<your-username>/comfyui-wanv2v-video-stitcher.git
 ```

3. Restart ComfyUI.
  The new nodes will appear under:
  ```bash
  WanV2vControlnetManager/Debug
 ```
  ```bash
  WanV2vControlnetManager/WAN
```

## 🚀 Usage Example (Workflow)

1. **Prepare ControlNet frames** (all input images).  

2. Use **Iter Control Group**:  
   - **Iter 1** → input ControlNet → KSampler → output `sample_op_1`.  
   - **Iter 2** → input ControlNet + `prev_output=sample_op_1` → KSampler → `sample_op_2`.  
   - **Iter 3** → input ControlNet + `prev_output=sample_op_2` … continue until last iteration.  

3. (Optional) Use **Debug Number Batch** on each sample to confirm frame continuity.  

4. Merge all sampler outputs with **Merge De-Overlap**:  
   - (`image_1=sample_op_1`, `image_2=sample_op_2`, etc).  

5. Send merged sequence to your **video writer node**.  

---

**Result:** 🎬 A seamless, artifact-free long video.


## 🔑 Features Recap

- ✅ Designed for **WAN v2v long video workflows**  
- ✅ Handles **chunking + overlap** seamlessly  
- ✅ Prevents **skipped or duplicated frames**  
- ✅ Debug-friendly with **numbered overlays**  
- ✅ Flexible: supports up to **10 chunk merges** in one step  


## 📌 SEO Keywords

- ComfyUI  
- WAN v2v  
- video stitching  
- long video generation  
- chunk overlap  
- ControlNet manager  
- de-overlap merge  
- KSampler workflow  
- seamless video  
- AI video tools  


## 📜 License

MIT License – free to use and modify.


