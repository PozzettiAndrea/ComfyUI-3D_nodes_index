# ComfyUI-DAP

A ComfyUI extension for the [Insta360 DAP](https://github.com/Insta360-Research-Team/DAP) (Depth Any Panorama) model. This plugin provides high-quality depth estimation specifically optimized for panoramic (equirectangular) images, with seamless integration for 3D workflows.

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes` folder.
    ```bash
    cd ComfyUI/custom_nodes
    git clone --recursive https://github.com/maxious/comfyui-dap
    ```
2.  Install the required dependencies in your ComfyUI virtual environment:

```bash
# Example for Windows with the default venv
"S:/ComfyUI/venv/Scripts/python.exe" -m pip install -r requirements.txt

# IMPORTANT: You need xformers for optimal performance and compatibility
"S:/ComfyUI/venv/Scripts/python.exe" -m pip install torch torchvision xformers -U --index-url https://download.pytorch.org/whl/cu130
```

## Nodes

### 1. DAP Loader
Handles automatic weight downloading from HuggingFace and model initialization.
*   **model_size**: Currently only `vitl` is available (official Large weights).
*   **precision**: Choose between `fp16`, `fp32`, and `bf16`.
*   **Auto-Patching**: Automatically fixes hardcoded relative paths in the research codebase to work within ComfyUI.

### 2. DAP Inference
The primary node for generating depth maps from panoramas.
*   **image**: Input panoramic image.
*   **invert_output**: Invert the depth map (standard for ComfyUI depth).
*   **resize_input**: Resizes to the model's preferred patch size (multiples of 14).
*   **Masking**: Uses the model's internal prediction mask to clean up non-panorama boundaries.

### 3. DAP Panoramic Mesh
Generates 3D geometry from the depth map using spherical unprojection.
*   **Compatibility**: Outputs a `TRIMESH` object, making it fully compatible with [ComfyUI-GeometryPack](https://github.com/idm-lab/ComfyUI-GeometryPack).
*   **mesh_scale**: Factor to scale the 3D depth intensity.
*   **downsample**: Reduce mesh density for faster performance.

### 4. DAP Normal Map
Generates surface normals optimized for panoramic projections.
*   **normal_standard**: Choose between `ComfyUI` (standard RGB) or `DAP` (original research format).
*   **Spherical Awareness**: Computes normals based on 3D unprojected points rather than 2D pixel gradients.

### 5. DAP ERP to Cubemap
Converts Equirectangular (2:1) panoramas into Cube Map faces.
*   **layout**: `six_faces` (returns a batch of 6) or `cross` (standard 3x4 grid).
*   **interpolation**: Uses high-quality `lanczos` by default.

## Usage & Templates

### Workflow Templates
A basic workflow template is included in the `workflow_templates` directory. You can access it through the ComfyUI "Templates" menu or by dragging and dropping `workflow_templates/dap_basic.json` into the ComfyUI workspace.

### Sample Image
To test the model, you can use this official sample panoramic image:
*   [01.jpg (HuggingFace)](https://huggingface.co/spaces/Insta360-Research/DAP/blob/main/hfdemo/01.jpg)

## Technical Details
*   **Submodule**: This plugin uses the official DAP repository as a Git submodule (`dap_core`) to ensure compatibility with future research updates.
*   **Interoperability**: By using standard `TRIMESH` and `IMAGE` types, DAP outputs can be piped directly into mesh decimators, 3D exporters, and controlnets.

## Testing
This plugin includes a `pytest` suite for headless verification of all nodes.

```bash
"S:/ComfyUI/venv/Scripts/python.exe" -m pytest
```

## Project History & Status
This project was developed with a focus on robust environment handling and automated testing. All core features from the initial PRD (Loader, Inference, Geometry, Conversions, and Normals) are completed and verified.

**Next Steps**:
*   Tiling support for ultra-high resolution (8k+) panoramas.
*   Integration of additional model sizes (vits/vitb/vitg) as they are released.
