# Comfyg Queue

**ComfygQueue** is a custom node for **ComfyUI** designed to streamline batch image generation with multiple resolutions. Its boring to stay changing resolutions, to test which one is the best for each model, so I made this node for me too :)

**Ignore the "ComfygQueueTrigger" node, I'm still working...**

#### v1.2.0:
- New format output options:
I'm running out of storage space, so I realized that the AVIF/Webp format is almost half the size of PNG, so I decided to make a new selection of options for the output file format: PNG, AVIF or WEBP. I'm still testing these formats and will think of more approaches to reduce size consumption. 

---

# Features

- **Batch Resolution Support**: Generate images at multiple resolutions in a single run.
- **Seed Control**:
  - Use a fixed seed or allow random generation.
  - Optionally increment +1 in seed for each resolution.
  - BUT! The node dont get the seed from the generated PNG, when you import, so pay attention.
- **Latent Input Handling**: If an input latent is provided, the node uses its resolution and skips multi-resolution loops.

---

## Inputs

- **Required**:
  - `res_presets`: String, e.g., `"1024x1024,1152x896"`
  - `save_prefix`: Prefix for saved files
  - `batch_seed`: Integer, `-1` for random, or a fixed seed
- **Optional**:
  - `incremental_seed`: Boolean, increment +1 per resolution
  - `model`, `positive`, `negative`, `vae`: Standard ComfyUI connections
  - `latent`: Optional latent image input
  - `steps`, `cfg`, `sampler_name`, `scheduler`, `denoise`: Sampling parameters
  - `output_subdir`: Subfolder for saved images
- **Hidden**:
  - `prompt`, `extra_pnginfo`

---

## Outputs

- `save_info`: Summary of generation
- `file_list`: JSON array of saved file paths

---

## Example Usage

1. Connect your model, prompt, and VAE as usual.
2. Set `res_presets` for desired resolutions.
3. Optionally provide a latent to preserve resolution.
4. Set `batch_seed` for reproducibility.
5. Run the node; files are saved in default output directory.

---

## File Naming

```text
<save_prefix>_<YYYYMMDD_HHMMSS>_<width>x<height>_<seed>.png
```
---

## Contributing

Contributions and suggestions are welcome! If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
