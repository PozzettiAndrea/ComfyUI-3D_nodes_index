# ComfyUI Leputen Utils

A collection of utility nodes for ComfyUI designed to streamline workflows, especially for game development and batch processing. This pack includes advanced tools for DDS texture handling, PBR map generation, batch image operations, and AI upscaling via DeepBump and Topaz Gigapixel AI.

> [!NOTE]
> This node pack is primarily **Windows-oriented**. Many core features (DDS conversion, DeepBump GPU acceleration) rely on Windows-native binaries or DirectX/DirectML technologies. While basic functionality may work on other platforms, Windows is required for the full feature set.

---

## Features

- **DDS Texture Support** - Load and save DirectDraw Surface files with full format control
- **Visual DDS Previews** - View DDS files directly in the graph with custom API integration
- **PBR Map Generation** - Generate AO, normal, height, and curvature maps with GPU acceleration
- **Normal Map Tools** - Convert, blend, adjust, and normalize normal maps
- **GPU Accelerated** - DeepBump supports DirectML/CUDA, AO generation uses PyTorch CUDA
- **High-Speed Parallel Saving** - Multi-threaded batch saving for DDS and standard images
- **Batch Processing** - Efficient batch loading with file caching and progress feedback
- **Settings Panel** - Configurable log verbosity via ComfyUI Settings
- **Smart Connections** - Format and color space combo outputs wire directly to savers
- **Input Validation** - Clear error messages before execution

---

## Installation

1. **Clone or download** this repository into your `ComfyUI/custom_nodes/` directory.

    ```bash
    git clone https://github.com/lilquail/ComfyUI-Leputen-Utils
    ```

2. **Restart** ComfyUI.

### Dependencies

This node pack has two types of dependencies:

1. **Python Packages**: The `requirements.txt` file lists all necessary Python packages (like `scipy`, `onnxruntime`, `tqdm`). ComfyUI will automatically install these packages upon startup.
2. **External Tools & Repositories**:
    - **[DeepBump-dml](https://github.com/lilquail/DeepBump-dml)**: Automatically cloned into `vendor/DeepBump` on first startup.
    - **[Texconv-Custom-DLL](https://github.com/matyalatte/Texconv-Custom-DLL)**: Pre-bundled `texconv.dll` in the `bin/` folder for fast in-process DDS conversion.

### Optional Dependencies

- **`onnxruntime-directml`**: For GPU-accelerated DeepBump on Windows (AMD/Intel/NVIDIA)
- **`tqdm`**: For console progress bars when verbose mode is enabled

---

## Settings

Access settings via **Settings** (⚙️) → **Leputen Utils**

| Category  | Setting                | Description                                             |
| --------- | ---------------------- | ------------------------------------------------------- |
| General   | **Log Verbosity**      | Controls console logging (Debug/Info/Warning/Error)     |
| Upscaling | **Gigapixel CLI Path** | Path to `gigapixel.exe` for Topaz Gigapixel AI          |

### Log Verbosity

- **Debug**: All messages including verbose debug output
- **Info**: Standard info messages (default)
- **Warning**: Warnings and errors only
- **Error**: Errors only

---

## Nodes

All nodes can be found under the `Leputen-Utils` category in ComfyUI.

### DDS Texture Nodes

| Node                           | Description                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **Load DDS Image**             | Loads a single `.dds` file with preview, width/height outputs, and alpha bleeding |
| **Save DDS Image**             | Saves images as `.dds` with BC1-7, HDR, and parallel processing                   |
| **Load DDS Images (Batch)**    | Loads `.dds` files from a directory (set `batch_size=-1` to load all at once)     |
| **Cubemap Assembler**          | Creates DDS cubemaps from 6 face images with compression/mipmaps                  |
| **Load Cubemap Faces**         | Pattern-based loader for 6 cubemap face images                                    |
| **Equirectangular to Cubemap** | Converts 360 panorama to 6 faces (supports **Auto** sizing)                       |

#### DDS Format & Color Space Connections

The DDS loader nodes output `format` and `color_space` as **combo types** that connect directly to the DDS Saver inputs:

```text
DDSLoader.format      → DDSSaver.format
DDSLoader.color_space → DDSSaver.output_color_space
```

This preserves the original file's format and color space when re-saving.

### PBR & Normal Map Nodes

| Node                             | Description                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| **Generate AO Map**              | Generates ambient occlusion from height maps (GPU accelerated)                      |
| **Height to Normal**             | Fast Sobel-based normal map generation from height maps                             |
| **DeepBump Color to Normal**     | AI-powered normal map from color images                                             |
| **DeepBump Normal to Height**    | AI-powered height map from normal maps                                              |
| **DeepBump Normal to Curvature** | AI-powered curvature map from normal maps                                           |
| **Normal Map Converter**         | Converts between DirectX (Y-) and OpenGL (Y+) formats                               |
| **Normal Map Strength**          | Adjusts intensity using **Partial Derivatives** or **Angles** modes                 |
| **Normal Map Add**               | Blends maps using **UDN**, **Whiteout**, **PD**, or **Reoriented (RNM)** algorithms |
| **Normal Map Extract Details**   | High-pass filter for extracting normal map details                                  |
| **Normal Map Normalize**         | Reconstructs the Z-channel for valid unit-length normals                            |

### Image Utility Nodes

| Node                               | Description                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------- |
| **Load Image (Leputen)**           | Enhanced loader with alpha bleeding, subfolder support, and EXR (HDR)              |
| **Load Images (Batch)**            | Batch loads PNG, JPG, EXR, etc. from a directory (set `batch_size=-1` for all)     |
| **Resize Power of 2**              | Resizes or crops to power of 2 dimensions                                          |
| **Z-Stack (Median/Mean)**          | Statistical stacking with dynamic inputs for noise reduction                       |
| **Color Space Converter**          | Converts between sRGB and Linear color spaces                                      |
| **Roughness/Glossiness Converter** | Converts roughness ↔ glossiness via inversion                                      |
| **Height Map Adjust**              | Adjusts levels and offset of height maps                                           |
| **Equalize**                       | Increases contrast using histogram equalization                                    |
| **Histogram Matcher**              | Matches grayscale histogram to a reference image                                   |
| **Channel Operations**             | Per-channel manipulation: normalize, invert, or set to fixed values                |
| **Save Image (Leputen)**           | Saves as **PNG, JPEG, WebP, TIFF, TGA, or EXR (HDR float32)**                      |

### Upscaling Nodes

| Node                 | Description                                                            |
| -------------------- | ---------------------------------------------------------------------- |
| **DeepBump Upscale** | AI upscaling x2 or x4 (GPU accelerated)                                |
| **Gigapixel CLI**    | Upscales using Topaz Gigapixel AI (set path in Settings → Upscaling)   |

---

## Pattern Matching Syntax

Batch loader nodes use **glob-style patterns** to filter files:

| Pattern           | Matches                          |
| ----------------- | -------------------------------- |
| `*`               | All files (default)              |
| `*_albedo.dds`    | Files ending with `_albedo.dds`  |
| `texture_*`       | Files starting with `texture_`   |
| `floor_??_a.png`  | `?` matches any single character |

### Multiple Patterns

Use **semicolons (`;`)** to match multiple patterns at once:

| Pattern                 | Matches                           |
| ----------------------- | --------------------------------- |
| `*_a.dds;*_n.dds`       | Albedo and normal maps            |
| `*_diffuse.*;*_color.*` | Diffuse/color maps, any extension |
| `hero_*;boss_*`         | All hero and boss textures        |

> [!NOTE]
> Patterns are case-sensitive on Linux/macOS but case-insensitive on Windows.

---

## Performance Features

### File Caching

Directory scans are cached to speed up iterative batch processing:

- **First run**: Full directory scan (~2s for 13,000 files)
- **Subsequent runs**: Instant cache hit (<1s)
- **Auto-invalidation**: Cache updates when directory content changes

### In-Place Progress

Large directory scans show progress updates on a single line instead of spamming the console:

```text
INFO: [DDSIterator] Scanning... 13000 files found (8200 directories)
```

---

## GPU Acceleration

### DeepBump Nodes (ONNX Runtime)

DeepBump nodes can use GPU acceleration via DirectML on Windows:

| Provider     | Platform | GPUs               |
| ------------ | -------- | ------------------ |
| **DirectML** | Windows  | AMD, Intel, NVIDIA |
| **CPU**      | All      | Fallback           |

On startup, you'll see a log message indicating the active provider:

```text
INFO: [DeepBump] GPU acceleration enabled via DirectML (Windows)
```

To enable DirectML, install `onnxruntime-directml`:

```bash
pip install onnxruntime-directml
```

### AO Map Generation (PyTorch)

The `Generate AO Map` node uses PyTorch and automatically uses CUDA when available (via ComfyUI's existing PyTorch installation), falling back to CPU otherwise.

---

## Usage & Best Practices

- **Alpha Bleeding**: Enable `alpha_bleed` to prevent halos around transparent textures. Use `blur_radius` (1.0 - 3.0) to soften the transitions at the texture edges for better blending in-engine.

- **Metadata Embedding**: Generation metadata (prompt/extra_pnginfo) is currently only embedded when saving in **PNG** format. Other formats (TGA, WebP, etc.) do not include this metadata.

- **Parallel Saving**: Both the DDS and standard Save nodes use a pool of worker threads to save batches of images simultaneously, significantly reducing processing time for large batches.

- **Verbose Mode**: DeepBump nodes have a `verbose` option that shows detailed console progress bars using `tqdm`.

- **Color Space Workflow**: Connect the `color_space` output from DDS Loader directly to the `output_color_space` input on DDS Saver.

- **Batch Processing**: Use `batch_size=-1` to load all files at once, or use positive values for memory-efficient batch processing.

- **DDS Format Guide**:

    | Format      | Use Case                         |
    | ----------- | -------------------------------- |
    | BC1_UNORM   | Opaque textures (no alpha)       |
    | BC3_UNORM   | Textures with alpha transparency |
    | BC4_UNORM   | Grayscale (height maps)          |
    | BC5_UNORM   | Normal maps (RG channels)        |
    | BC6H_UF16   | HDR textures (no alpha)          |
    | BC7_UNORM   | Highest quality (larger files)   |

- **Normal Map Formats**: Pay attention to **DirectX (Y-)** vs **OpenGL (Y+)** formats.
  - DeepBump and most Game Engines (Unreal, Unity HDRP) often prefer specific formats.
  - Use the **Normal Map Converter** node to flip the Y channel if your lighting looks "inside out" or shadows are wrong.

---

## Troubleshooting

- **`texconv.exe` not found**: The utility is bundled in the `bin/` directory. Ensure it exists and you have execute permissions.

- **Dependency Issues**: If automatic installation fails, run manually:

    ```bash
    pip install -r custom_nodes/ComfyUI-Leputen-Utils/requirements.txt
    ```

- **DeepBump Clone Fails**: Ensure `git` is installed and in PATH. Alternatively, clone manually:

    ```bash
    cd custom_nodes/ComfyUI-Leputen-Utils
    git clone https://github.com/lilquail/DeepBump-dml.git vendor/DeepBump
    ```

- **Gigapixel CLI Errors**: Set the path to your `gigapixel.exe` via **Settings** → **Leputen Utils** → **Upscaling** → **Gigapixel CLI Path**.

    > [!NOTE]
    > CLI requires **Gigapixel AI Pro**.

- **GPU Not Detected**: For DeepBump GPU acceleration on Windows, install `onnxruntime-directml`:

    ```bash
    pip install onnxruntime-directml
    ```

- **DLL COM Error**: If you see `E_NOINTERFACE` or `RPC_E_CHANGED_MODE` warnings in the console, do not worry. The node has automatically fallen back to using `texconv.exe` (subprocess mode) and your workflow will proceed normally. This occurs when another node has already locked the COM threading model.

- **Cross-Platform DDS**: For macOS or Linux, download the appropriate shared library from [Texconv-Custom-DLL releases](https://github.com/matyalatte/Texconv-Custom-DLL/releases) and place it in the `bin/` folder:
  - Windows: `texconv.dll` (bundled)
  - macOS: `libtexconv.dylib`
  - Linux: `libtexconv.so`

---

## Known Issues

- **BC5 DDS Loading**: BC5-compressed images can be saved but not loaded right now unfortunately. Attempting to load them will result in an error and needing to restart ComfyUI.

---

## Acknowledgements

- **[DeepBump-dml](https://github.com/lilquail/DeepBump-dml)**: ML-powered PBR map generation, forked from [DeepBump](https://github.com/HugoTini/DeepBump) by Hugo Tini (GPLv3)
- **[Texconv-Custom-DLL](https://github.com/matyalatte/Texconv-Custom-DLL)** by matyalatte: Cross-platform texconv DLL for fast in-process DDS conversion (MIT)
- **[DirectXTex](https://github.com/microsoft/DirectXTex)** by Microsoft: DDS handling via `texconv.exe` fallback (MIT)
- **[Blending in Detail](https://blog.selfshadow.com/publications/blending-in-detail/)** by Colin Barré-Brisebois and Stephen Hill: Normal map blending algorithms
- **[chaiNNer](https://github.com/chaiNNer-org/chaiNNer)**: Inspiration for a lot of the nodes

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

> [!NOTE]
> DeepBump is licensed under GPLv3 and is cloned separately at runtime. It is not distributed with this package.

<p align="center">
  <img src="Leputen.png" width="128" alt="Leputen Logo">
</p>
