# ComfyUI-SortList

Custom nodes for ComfyUI with video processing utilities.

## Installation

### Google Colab
```bash
cd /content/ComfyUI/custom_nodes
git clone https://github.com/huyl3-cpu/comfyui-sortlist.git
```

## Update to Latest Version

### On Google Colab

**Method 1: Quick Update (Recommended)**
```bash
cd /content/ComfyUI/custom_nodes/comfyui-sortlist
git pull origin main
```

**Method 2: Using Update Script**
```bash
cd /content/ComfyUI/custom_nodes/comfyui-sortlist
bash update_colab.sh
```

**After updating:**
1. Restart Runtime: `Runtime → Restart Runtime`
2. Re-run ComfyUI startup cells
3. Nodes will be updated!

---

## Nodes

### Video Cut to 8s Segments
Cuts large videos into smaller segments with customizable duration.

**Features:**
- ✅ Auto FPS detection
- ✅ Frame-accurate cutting
- ✅ Guaranteed output: H.264, MP4, YUV420P
- ✅ Auto-fallback: GPU → CPU encoding
- ✅ Parallel processing

**Parameters:**
- `video_url`: Path to input video
- `segment_duration`: Segment length in seconds (default: 8)
- `output_prefix`: Output filename prefix (default: "a")
- `use_gpu`: Try GPU encoding first (default: true, auto-fallback to CPU)
- `accurate_cut`: Accurate seeking (default: true)
- `parallel_workers`: Number of parallel workers (default: 4)

**Outputs:**
- `videos_list`: List of output video paths
- `output_directory`: Path to output directory (`videos_cut/`)

**Example:**
```
Input: video.mp4 (268.2s, 25 FPS)
segment_duration: 8s
Output: 34 segments (33 × 8.0s + 1 × 4.2s)
```

---

## Recent Updates

### v1.1 (2026-01-26)
- ✅ Added auto-fallback from GPU to CPU encoding
- ✅ Enhanced error logging for better debugging
- ✅ Fixed NVENC compatibility on Google Colab
- ✅ Improved terminal output compatibility
- ✅ Added diagnostic tools

---

## License

MIT
