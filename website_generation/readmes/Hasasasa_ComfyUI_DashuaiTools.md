# ComfyUI DashuaiTools Node Overview
[English](README.md)  | [简体中文](README_CN.md)

## Plugin Intro Video
YouTube: https://youtu.be/hNIKSPjLhIc  
Bilibili: https://www.bilibili.com/video/BV1Fq6SBkEm6

## Image_Nodes

- **getImageRetio**  
  Computes the simplified aspect ratio of an input image (e.g. 3:4). Outputs the ratio string plus numeric width/height ratios for reuse in other nodes.

- **ImageComparisonGIF**  
  Takes two images and creates a left–right sliding comparison GIF. Supports custom frame count, automatically saves to the ComfyUI `output` folder and avoids filename collisions by adding numeric suffixes.

- **LoadImageList**  
  Loads images from a folder in batch. Supports sorting by alphabetical order, numeric order, or file modification time (ascending/descending), and lets you set start index and maximum number of outputs. Returns both image tensors and the corresponding filenames for easier batch processing and logging.

- **Load64image**  
  Loads an image from a Base64 string (supports optional `data:image/...;base64,` prefix) and outputs a ComfyUI `IMAGE` tensor.

- **SaveImageWithName**  
  Saves one or multiple images to a given path with custom filenames and optional suffix. Automatically fills in missing extensions, generates unique filenames to avoid overwriting, and handles EXIF orientation to prevent rotated outputs.

- **XY_Image (XY chart)**  
  A standalone XY Plot–style node for ComfyUI. It hooks into the entire workflow graph: you define X/Y axes as parameter overrides (prompt, CFG, seed, etc.), and it executes combinations to build comparison grids. It uses content hashing and a global cache so that only changes in upstream nodes or XY configuration trigger re‑execution; layout tweaks (gap, font size, layout mode) reuse cached results, giving a dashboard-like refresh experience. Supports three layouts: "XY Plot / X:Y / Y:X" with flexible labels and axis configuration, ideal for large workflows and parameter sweeps.

## PS_Nodes

- **MinimumFilter**  
  A Photoshop‑style minimum filter implemented with `skimage`’s rank minimum operator. Radius is configurable and it works on single images or batches, useful for pre‑processing tasks such as matte refinement or detail suppression.

## API_Nodes

- **Gemini_API_Image**  
  Calls Gemini image generation with optional reference images (up to 14). Supports aspect ratio, resolution, and seed control, and returns both the generated image and any text response.

- **api_caption**  
  Uses a multimodal chat API to generate descriptions/prompts for a single image. Compatible with the OpenAI‑style API schema and supports multiple providers (Siliconflow, ZhenZhen Workshop, OpenRouter). You can customize model name, temperature and base prompt, choose Chinese or English output, and get basic retry + error reporting.

- **batch_api_caption**  
  Processes all images in a folder and calls a multimodal API in parallel to generate text descriptions, saving each caption into a `.txt` file with the same basename. Allows configuring input/output folders, model, prompt, output language and concurrency level, and returns a JSON log summarizing total/succeeded/failed counts—suitable for large‑scale dataset labeling.

## Tools

- **ZImageLoraModelOnly**  
  A Z‑Image–specific LoRA loader based on the official "LoRA Model-Only Loader" and PGCRT/CRT-Nodes/blob/main/py/LoraLoaderZImage.py, rewritten. It loads Q/K/V‑fused Z‑Image LoRA weights and applies them only to the MODEL branch (leaving CLIP untouched). You can pick any existing LoRA by filename and adjust the model strength; recommended as the dedicated LoRA entry point for Z‑Image pipelines.
  
- **LoadTextList**  
  Loads `.txt` files from a folder in batch. Supports alphabetical / numerical / datetime sorting with start index and maximum count, and outputs a list of text contents together with their filenames. Internally it tries UTF-8 first and then common Chinese encodings (GBK/GB2312/BIG5), falling back to a raw-bytes `repr` string if decoding fails, which makes it robust for mixed-encoding text datasets.

- **qwenMultiAngles**  
  Builds a prompt in the format: `<sks> {azimuth} {elevation} {distance}` (e.g. `<sks> front view eye-level shot medium shot`).

## Video_Nodes

- **(Reserved)**  
  Currently no video nodes are shipped; this section is reserved for future extensions.

---

More examples and tutorials (Chinese) on Bilibili:  
https://space.bilibili.com/85024828

YouTube:
https://www.youtube.com/channel/UCqUEZlzmcEXKdU5zgnaT4Ig

---


