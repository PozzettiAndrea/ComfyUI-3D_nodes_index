# craftgear nodes

some tiny nodes for better QoL.

## Node List

See the linked documentation for each node for details.

- [Load LoRAs With Tags](./docs/load_loras_with_tags.md) : Load and select tags from LoRA & JSON files. LoRA selection supports fuzzy matching by name plus preview images with hover zoom (configurable in settings)
- [Toggle Tags](./docs/toggle_tags.md) : Toggle tags on/off with clicks from input tag text
- [Commentable Multiline Text](./docs/commentable_multiline_text.md) : Remove comment lines and output the result
- [Checkpoint Selector](./docs/checkpoint_selector.md) : Pick one checkpoint from up to 20 slots with search, preview, hover zoom, and configurable font size
- [Join Texts](./docs/join_texts.md) : Join multiple text inputs into a single line
- [Image Batch Loader](./docs/image_batch_loader.md) : Load images from a directory as a batch
- [Camera Shake](./docs/camera_shake.md) : Add handheld-style shake to image batches
- [A1111 Metadata Writer](./docs/a1111_metadata_writer.md) : Writes prompts and tag data from this pack’s nodes (e.g., Load Loras With Tags, Commentable Multiline Text, Toggle Tags) as A1111-compatible `parameters` into PNG/WebP outputs, with a `png/webp` format toggle
- [A1111 Metadata Reader](./docs/a1111_metadata_reader.md) : Reads A1111-style metadata from WebP/PNG/JPEG images and returns parsed prompts, model JSON, and LoRA JSON


## Installation

### Using Comfy Manager

Search for `craftgear` in Comfy Manager's Custom Nodes Manager and install.

Note: Selecting `nightly` in the version selection screen will fail due to security restrictions. Please select a numbered version to install.

### Using git clone

Run the following command in the ComfyUI custom nodes directory:

```bash
git clone https://github.com/craftgear/comfyui-craftgear-nodes
```


## LICENSE
MIT
