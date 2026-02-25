# ComfyUI zyd232 Nodes

## Node Description
### 1. Images Pixels Compare
This node is used to compare whether two input images are exactly the same (pixel-level comparison) and outputs a boolean value.

### 2. Save Preview Images
This node saves input images with various options including format (PNG/JPG), quality, metadata, and custom paths. It can also save the workflow as JSON and generate preview images. Preview images are controlled by the same options. The save function can be disabled to use the node solely for preview purposes.

### 3. Mask Batch Blend
This node blends multiple masks together using different operations (add, max, average). It can handle masks with different dimensions and batch sizes. The node supports:
- **Add operation**: Sums all masks together (overlay effect)
- **Max operation**: Takes the maximum value at each pixel across all masks
- **Average operation**: Computes the average of all masks
