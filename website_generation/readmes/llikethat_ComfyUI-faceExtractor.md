# Face Extractor for ComfyUI

**Version 4.0 - Generic Face Extraction Tool**

Memory-efficient face extraction with reference-based matching. Works with videos of any length.

---

## ⚠️ IMPORTANT: License Information

This tool supports multiple face detection backends with **different licenses**:

| Backend | License | Commercial Use | Quality | GPU | Embeddings |
|---------|---------|----------------|---------|-----|------------|
| **facenet** ⭐ | MIT | ✅ YES | ⭐⭐⭐⭐⭐ Best | ✅ | Neural (512-dim) |
| **yolov8** | AGPL-3.0 | ⚠️ License required | ⭐⭐⭐⭐ Good | ✅ | Neural (if FaceNet installed) |
| **insightface** | Non-Commercial | ❌ NO | ⭐⭐⭐⭐⭐ Best | ✅ | Neural (512-dim) |
| **mediapipe** | Apache 2.0 | ✅ YES | ⭐⭐⭐⭐ Good | ❌ | Histogram |
| **opencv_cascade** | BSD | ✅ YES | ⭐⭐⭐ Basic | ❌ | Histogram |

### ⭐ Recommended for Commercial Projects: `facenet`

FaceNet (facenet-pytorch) provides:
- **MIT License** - fully free for commercial use
- **High-quality neural embeddings** (512-dim, comparable to InsightFace)
- **GPU acceleration** (CUDA)
- **MTCNN face detection** (also MIT licensed)

```
detection_backend: "facenet"   # Recommended for commercial
```

### YOLOv8 License Notice

YOLOv8 (Ultralytics) uses **AGPL-3.0** license:
- ✅ Free for open-source projects
- ⚠️ Commercial closed-source use requires purchasing a license from Ultralytics
- See: https://ultralytics.com/license

### InsightFace License Notice

InsightFace is provided under a **non-commercial license**:

> The InsightFace project is released under the MIT License for non-commercial purposes only.
> For commercial use, please contact the authors for licensing terms.
> 
> Source: https://github.com/deepinsight/insightface#license

---

## Features

- **Built-in Video Loading**: No VHS dependency needed
- **Memory-Efficient**: Streaming mode uses ~500MB regardless of video length
- **Aspect Ratio Preservation**: No more squashed faces
- **GPU Memory Management**: Automatic flush after each chunk
- **Multiple Backends**: Choose based on quality vs license needs
- **Browser-Friendly**: Minimal data sent back to browser

---

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/comfyui_face_extractor.git
cd comfyui_face_extractor

# Recommended: FaceNet (commercial OK, high quality)
pip install facenet-pytorch mediapipe psutil

# Optional: YOLOv8 (fast detection, AGPL license)
pip install ultralytics

# Optional: InsightFace (non-commercial only, highest quality)
pip install insightface onnxruntime-gpu
```

### Minimal Installation (Commercial OK)
```bash
pip install facenet-pytorch psutil
```

### Full Installation (All backends)
```bash
pip install facenet-pytorch ultralytics insightface onnxruntime-gpu mediapipe psutil
```

---

## Quick Start

1. Load reference image(s) of target face
2. Set `video_path` to your video file (NOT VHS_LoadVideo!)
3. Choose `detection_backend` based on your license needs
4. Run - faces saved to `ComfyUI/output/face_extract_001/`

---

## Nodes

### Face Reference Embedding

Creates face embedding from reference images.

| Input | Description |
|-------|-------------|
| reference_images | One or more face images |
| detection_backend | "insightface", "mediapipe", or "opencv_cascade" |
| min_confidence | Minimum detection confidence (0.5 default) |

### Face Extractor

Main extraction node with built-in video loading.

| Input | Description |
|-------|-------------|
| **video_path** | Direct path to video (RECOMMENDED) |
| images | Alternative: IMAGE from other nodes |
| reference_embedding | From Face Reference Embedding |
| similarity_threshold | Match threshold (0.6 default) |
| margin_factor | Padding around face (0.4 default) |
| output_size | Output resolution, aspect preserved (512 default) |
| max_faces_per_frame | Max faces per frame (1 default) |
| frame_skip | Process every Nth frame (1 default) |
| processing_mode | "streaming" or "chunked" |
| memory_threshold_percent | RAM limit for chunked mode (75% default) |
| **chunk_size** | **Frames per chunk (0 = auto-calculate)** |
| detection_backend | Choose based on license needs |

### Face Matcher

Compare two faces for threshold tuning.

---

## Processing Modes

### Streaming (Default) ⭐
- One frame at a time
- ~500 MB RAM constant
- Best for: Large videos, limited RAM

### Chunked
- Batches of frames processed together
- GPU flushed after EVERY chunk
- Faster than streaming
- Best for: When you have RAM to spare

**Chunk Size Configuration:**
- `chunk_size = 0` (default): Auto-calculate based on available memory and `memory_threshold_percent`
- `chunk_size = 100`: Process exactly 100 frames per chunk
- `chunk_size = 500`: Process 500 frames per chunk (faster, uses more RAM)

Console output shows which mode is used:
```
[Face Extractor] Auto chunk size: 287 (based on 75.0% memory threshold)
# or
[Face Extractor] Using manual chunk size: 500
```

---

## Aspect Ratio Preservation

**Before (v3)**: Faces were squashed to square
```
Original: 400x500 → Forced to 512x512 → Distorted!
```

**Now (v4)**: Aspect ratio preserved with padding
```
Original: 400x500 → Scaled to 409x512 → Centered on 512x512 canvas
```

---

## Memory Optimization

### GPU Memory
- Flushed after EVERY chunk in chunked mode
- Flushed every 500 frames in streaming mode
- Console shows GPU usage: `GPU after flush: 0.42GB`

### Browser Memory
- Preview grid reduced to 256x256 (was 512x512)
- Only 16 preview faces stored
- Minimal tensor data returned

### RAM
- Streaming: ~500 MB constant
- Chunked: Up to `memory_threshold_percent` of system RAM

---

## Backend Comparison

### FaceNet ⭐ RECOMMENDED (Commercial OK)
```
+ High accuracy (comparable to InsightFace)
+ Neural network embeddings (512-dim)
+ GPU accelerated (CUDA)
+ MIT License - fully commercial safe!
+ MTCNN detection (also MIT)
```

### YOLOv8 (AGPL - Commercial needs license)
```
+ Very fast detection
+ Good accuracy
+ GPU accelerated
+ Uses FaceNet embeddings if available
- AGPL-3.0 - commercial closed-source needs Ultralytics license
```

### InsightFace (Non-Commercial Only)
```
+ Best accuracy
+ Neural network embeddings (512-dim ArcFace)
+ GPU accelerated
- Non-commercial license only!
```

### MediaPipe (Commercial OK)
```
+ Good accuracy  
+ Apache 2.0 license - commercial safe
+ Google maintained
- CPU only (but still fast)
- Uses histogram-based embeddings (less precise)
```

### OpenCV Cascade (Commercial OK)
```
+ Always available (built into OpenCV)
+ BSD license - commercial safe
+ Very fast
- Lower accuracy
- Uses histogram-based embeddings
```

---

## Similarity Threshold Guide

| Backend | Same Person | Different Person | Recommended |
|---------|-------------|------------------|-------------|
| facenet | 0.65-0.85 | 0.20-0.40 | 0.55-0.65 |
| yolov8 (w/FaceNet) | 0.65-0.85 | 0.20-0.40 | 0.55-0.65 |
| insightface | 0.65-0.85 | 0.20-0.40 | 0.55-0.65 |
| mediapipe | 0.70-0.90 | 0.40-0.60 | 0.65-0.75 |
| opencv_cascade | 0.75-0.95 | 0.50-0.70 | 0.70-0.80 |

**Note:** FaceNet, YOLOv8 (with FaceNet embeddings), and InsightFace all use neural network embeddings with similar behavior. MediaPipe and OpenCV use histogram-based embeddings which require higher thresholds.

**Use Face Matcher node to find optimal threshold for your specific use case!**

---

## Output Structure

```
ComfyUI/output/
├── face_extract_001/
│   ├── aligned/
│   │   ├── 00000000_0.png
│   │   ├── 00000024_0.png
│   │   └── ...
│   ├── masks/
│   │   ├── 00000000_0_mask.png
│   │   └── ...
│   └── extraction_log.json
```

The `extraction_log.json` includes:
- Backend used and its license type
- Aspect ratio preservation info
- Similarity scores for each face
- Processing statistics

---

## Use with DeepFaceLab

After extraction, copy faces to DFL workspace:

```bash
cp ComfyUI/output/face_extract_001/aligned/* workspace/data_src/aligned/
```

---

## Workflows

| Workflow | Description |
|----------|-------------|
| 01_basic_extraction | Single reference + video path |
| 02_multi_reference | Multiple references for robust matching |
| 03_threshold_tuning | Find optimal similarity threshold |
| 04_deaging_pipeline | Source + destination extraction |

---

## Troubleshooting

### "InsightFace not available"
```bash
pip install insightface onnxruntime-gpu
```

### "MediaPipe not available"  
```bash
pip install mediapipe
```

### GPU memory keeps growing
- Use `streaming` mode instead of `chunked`
- Or reduce `memory_threshold_percent`

### Faces look squashed
- Update to v4 - aspect ratio is now preserved

### Browser tab using too much memory
- v4 returns smaller preview (256x256)
- Consider closing preview nodes if not needed

---

## License

MIT License (this ComfyUI node code)

**IMPORTANT**: The detection backends have their own licenses:
- InsightFace: Non-Commercial only
- MediaPipe: Apache 2.0
- OpenCV: BSD

Your use of this tool must comply with the license of the backend you choose.

---

## Credits

- [InsightFace](https://github.com/deepinsight/insightface) - Face detection/recognition (non-commercial)
- [MediaPipe](https://github.com/google/mediapipe) - Face detection (Apache 2.0)
- [OpenCV](https://opencv.org/) - Computer vision library (BSD)
