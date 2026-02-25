# comfyui-usetaesd

A custom node set for ComfyUI that provides nodes for encoding and decoding images using Tiny AutoEncoders for Stable Diffusion (TAESD) models.

TAESD models are highly optimized, lightweight VAEs designed for extremely fast encoding and decoding, requiring significantly less VRAM compared to full Stable Diffusion VAEs. They are ideal for quick previews, animations, or when VRAM is a major limitation.

## Features

*   **Fast Encoding/Decoding:** Utilize TAESD models for rapid image-to-latent and latent-to-image conversions.
*   **Multiple TAESD Models Supported:**
    *   `taesd` (default)
    *   `taesdxl`
    *   `taesd3`
    *   `taef1`
*   **Automatic Model Loading and Caching:** Models are loaded on demand and cached in memory for efficient reuse.
*   **Correct VAE Scale/Shift:** Automatically applies the specific `vae_scale` and `vae_shift` values required by each TAESD variant for accurate results.
*   **Tiled Processing:** Includes nodes for tiled encoding and decoding, allowing processing of very large images even with TAESD's already low VRAM footprint.

## Installation

1.  **Navigate to your ComfyUI custom nodes directory:**
    ```bash
    cd ComfyUI/custom_nodes
    ```
2.  **Clone this repository:**
    ```bash
    git clone https://github.com/neocrz/comfyui-usetaesd.git
    ```
3.  **Restart ComfyUI.**

## Model Download

**This custom node set does NOT bundle the TAESD models themselves.** You need to download them separately.

1.  **Download the TAESD model files:**
    The official TAESD models are typically found on HuggingFace:
    *   **MadeByOllin's TAESD models:** [huggingface.co/madebyollin/taesd](https://huggingface.co/madebyollin/taesd)
    *   **Recommended files to download:**
        *   `taesd_encoder.safetensors`
        *   `taesd_decoder.safetensors`
        *   `taesdxl_encoder.safetensors`
        *   `taesdxl_decoder.safetensors`
        *   `taesd3_encoder.safetensors`
        *   `taesd3_decoder.safetensors`
        *   `taef1_encoder.safetensors`
        *   `taef1_decoder.safetensors`

2.  **Place the downloaded files into your ComfyUI `vae_approx` directory:**
    ```
    ComfyUI/models/vae_approx/
    ```
    If the `vae_approx` directory does not exist, create it.

## Usage

After installation and placing the TAESD model files, the new nodes will appear in the ComfyUI workflow editor under the `latent/TAESD` category.

A typical workflow might look like this:

`Load Image` -> `TAESD Encode` -> `KSampler` (or other latent operations) -> `TAESD Decode` -> `Save Image`

## Node Descriptions

### EncodeTAESD

*   **Category:** `latent/TAESD`
*   **Description:** Encodes an image into TAESD's latent space.
*   **Inputs:**
    *   `pixels` (IMAGE): The image to encode.
    *   `taesd_model_name` (Enum: `taesd`, `taesdxl`, `taesd3`, `taef1`): Selects which TAESD model to use for encoding.
*   **Outputs:**
    *   `LATENT`: The encoded latent representation.

### DecodeTAESD

*   **Category:** `latent/TAESD`
*   **Description:** Decodes latents from TAESD's latent space back to an image.
*   **Inputs:**
    *   `samples` (LATENT): The latent samples to decode.
    *   `taesd_model_name` (Enum: `taesd`, `taesdxl`, `taesd3`, `taef1`): Selects which TAESD model to use for decoding.
*   **Outputs:**
    *   `IMAGE`: The decoded image.

### EncodeTAESDTiled

*   **Category:** `latent/TAESD`
*   **Description:** Encodes an image into TAESD's latent space using tiled processing, useful for very large images.
*   **Inputs:**
    *   `pixels` (IMAGE): The image to encode.
    *   `taesd_model_name` (Enum: `taesd`, `taesdxl`, `taesd3`, `taef1`): Selects which TAESD model to use.
    *   `tile_size` (INT, default: 512): The size of the image tiles (in pixels) for processing.
    *   `overlap` (INT, default: 64): The overlap between tiles (in pixels) to ensure seamless stitching.
*   **Outputs:**
    *   `LATENT`: The encoded latent representation.

### DecodeTAESDTiled

*   **Category:** `latent/TAESD`
*   **Description:** Decodes latents from TAESD's latent space back to an image using tiled processing, useful for very large generated latents.
*   **Inputs:**
    *   `samples` (LATENT): The latent samples to decode.
    *   `taesd_model_name` (Enum: `taesd`, `taesdxl`, `taesd3`, `taef1`): Selects which TAESD model to use.
    *   `tile_size` (INT, default: 512): The *image pixel* size that corresponds to the latent tile size for decoding. The node will automatically convert this to the correct latent dimension based on the VAE's compression factor.
    *   `overlap` (INT, default: 64): The *image pixel* overlap that corresponds to the latent overlap. The node will automatically convert this to the correct latent dimension.
*   **Outputs:**
    *   `IMAGE`: The decoded image.

## Important Notes & Considerations

*   **Quality vs. Speed:** TAESD models are *approximations* of full VAEs. While incredibly fast, they may not always produce the same level of detail or fidelity as a full Stable Diffusion VAE, especially for intricate details. They are generally excellent for quick previews, animations, or memory-constrained environments.
*   **Missing Files:** If the required `_encoder.safetensors` or `_decoder.safetensors` files for a selected TAESD model are not found in `ComfyUI/models/vae_approx/`, the node will raise a `FileNotFoundError`. Ensure all necessary files are downloaded and placed correctly.
*   **File Extensions:** The script will try common extensions (`.safetensors`, `.pt`, `.bin`, `.pth`) when looking for the model files.

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.