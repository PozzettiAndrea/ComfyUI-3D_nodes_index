# ComfyUI Batching Nodes

A collection of custom nodes for ComfyUI that enable powerful batch processing capabilities for both prompts and images. Automate repetitive tasks and process multiple items through your workflow with ease.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Overview

This package provides essential nodes for automating batch processing in ComfyUI. Process multiple prompts, entire folders of images, or combine both for maximum workflow automation. No more manual copy-pasting or running workflows one-by-one!

### Nodes Included

**Prompt Batching:**

1. **Batch Text (Prompt Loop)** - Split multi-line text into individual prompts and batch process them
2. **Get Prompt From Batch** - Extract individual prompts from a batch for manual control

**Image Batching:** 3. **Batch Images (Folder Loader)** - Load all images from a folder and process them automatically 4. **Get Image From Batch** - Extract individual images from a batch for manual control

## ✨ Features

### Prompt Batching

- 📝 **Multi-Prompt Processing** - Process multiple prompts through your workflow automatically
- 🎯 **Flexible Text Splitting** - Use any delimiter (newline, comma, pipe, etc.) to split prompts
- ✂️ **Smart Trimming** - Automatically skip empty lines and trim whitespace

### Image Batching

- 📁 **Folder-Based Loading** - Point to any folder and process all images automatically
- 🖼️ **Multiple Format Support** - PNG, JPG, JPEG, WebP, BMP, GIF
- 📊 **Sorting Options** - Sort images by name, modification date, or creation date
- 🎛️ **Batch Control** - Skip first N images or limit to max N images
- 💾 **Filename Preservation** - Outputs original filenames for organized saving

### General

- 🔄 **Automatic Batch Processing** - Zero manual intervention required
- 🎨 **ComfyUI Native Integration** - Works seamlessly with existing ComfyUI workflows
- ⚡ **High Performance** - Efficient processing of large batches
- 🔗 **Combinable** - Mix prompt and image batching for powerful workflows

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "ComfyUI Batching Nodes" or "Batch Images"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:

   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:

   ```bash
   git clone https://github.com/hahihula/ComfyUI-batching-nodes.git
   ```

3. Restart ComfyUI

### Method 3: Direct Download

1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/ComfyUI-batching-nodes/`
3. Restart ComfyUI

## 🚀 Quick Start

### Example 1: Batch Generate from Multiple Prompts

```
Batch Text (Prompt Loop)
├─ Input: "a cat in a garden\na dog on a beach\na bird in the sky"
└─ Output: [prompt1, prompt2, prompt3]
    │
    ▼
CLIP Text Encode → KSampler → VAE Decode → Save Image
```

Result: 3 images generated automatically, one for each prompt!

### Example 2: Batch Process Images from Folder

```
Batch Images (Folder Loader)
├─ folder_path: "/ComfyUI/input/my_photos"
└─ Output: [image1, image2, image3, ...]
    │
    ▼
VAE Encode → KSampler → VAE Decode → Save Image
```

Result: All images in the folder processed through your workflow!

### Example 3: Combine Both - Prompts × Images

```
Batch Text                    Batch Images
(3 prompts)                  (5 images)
    │                            │
    └────────┬───────────────────┘
             ▼
    CLIP + VAE Encode → KSampler → VAE Decode → Save
```

Result: 15 variations (3 prompts × 5 images) generated automatically!

## 📖 Node Documentation

### Batch Text (Prompt Loop)

Splits a multi-line text input into individual prompts for batch processing.

**Inputs:**

- `text` (STRING): Multi-line text with one prompt per line
- `delimiter` (STRING): Character(s) to split by (default: `\n`)
- `skip_empty` (BOOLEAN): Skip empty lines (default: `True`)

**Outputs:**

- `prompts_list` (STRING LIST): List of individual prompts
- `count` (INT): Number of prompts

**Example:**

```python
Input text:
"photorealistic portrait of a warrior
cyberpunk cityscape at night
fantasy dragon in mountains"

Delimiter: "\n"
Skip empty: True

Output: ["photorealistic portrait of a warrior",
         "cyberpunk cityscape at night",
         "fantasy dragon in mountains"]
Count: 3
```

### Batch Images (Folder Loader)

Loads all images from a specified folder for batch processing.

**Inputs:**

- `folder_path` (STRING): Path to folder containing images
- `image_extensions` (STRING): Comma-separated extensions (default: `png,jpg,jpeg,webp,bmp,gif`)
- `sort_by` (CHOICE): Sort method - `name`, `modified`, or `created`
- `start_index` (INT, optional): Skip first N images (default: `0`)
- `max_images` (INT, optional): Limit to N images, 0 = all (default: `0`)

**Outputs:**

- `images` (IMAGE LIST): List of loaded images
- `filenames` (STRING LIST): List of filenames
- `count` (INT): Number of images loaded

**Example:**

```python
folder_path: "/ComfyUI/input/vacation_photos"
extensions: "jpg,png"
sort_by: "name"
start_index: 0
max_images: 10

Output: [img1, img2, ..., img10]
Filenames: ["photo_001.jpg", "photo_002.jpg", ...]
Count: 10
```

### Get Prompt From Batch

Extracts a single prompt from a batch by index (for manual control).

**Inputs:**

- `prompts_list` (STRING LIST): List from Batch Text node
- `index` (INT): Which prompt to extract (0-based)

**Outputs:**

- `prompt` (STRING): Single prompt at specified index

### Get Image From Batch

Extracts a single image from a batch by index (for manual control).

**Inputs:**

- `images` (IMAGE LIST): List from Batch Image Loader
- `index` (INT): Which image to extract (0-based)

**Outputs:**

- `image` (IMAGE): Single image at specified index
- `index` (INT): The index used

## 💡 Use Cases

### Prompt Batching Use Cases

#### 1. Style Variation Testing

Test different art styles on the same subject:

```
Batch Text Input:
"portrait in oil painting style
portrait in watercolor style
portrait in digital art style
portrait in pencil sketch style"
```

#### 2. Character Sheet Generation

Generate multiple views of a character:

```
Batch Text Input:
"character front view, white background
character side view, white background
character back view, white background
character 3/4 view, white background"
```

#### 3. Product Mockups

Create variations of product descriptions:

```
Batch Text Input:
"professional product photo, studio lighting
product in natural environment
product lifestyle shot
product detail close-up"
```

### Image Batching Use Cases

#### 4. Batch Upscaling

Upscale an entire folder of images:

```
Batch Images → VAE Encode → Upscale Model → VAE Decode → Save
```

#### 5. Dataset Preprocessing

Apply the same processing to hundreds of images:

```
Batch Images (max_images: 0) → Your Processing → Save
```

#### 6. Batch Style Transfer

Apply artistic style to photo collection:

```
Batch Images (vacation_photos/) → ControlNet → Style Model → Save
```

#### 7. Consistent Facial Fixes

Fix faces across multiple generated images:

```
Batch Images (generated_faces/) → Face Restore → VAE Decode → Save
```

### Combined Batching Use Cases

#### 8. Image Variations Matrix

Apply different prompts to multiple images:

```
Batch Text (3 styles) × Batch Images (5 photos) = 15 variations
```

#### 9. A/B Testing

Compare different prompts across same images:

```
Batch Text: Different prompt variations
Batch Images: Test images
Fixed Seed → KSampler → Compare outputs
```

#### 10. Product Catalog Generation

Generate product in different scenes:

```
Batch Images: Product photos
Batch Text: Different environment descriptions
ControlNet → Generate scenes
```

## 📸 Example Workflows

### Workflow 1: Multi-Prompt Batch Generation

**Download:** [example_workflows/multiprompt_generation.json](example_workflows/multiprompt_generation.json)

This workflow demonstrates:

- Using Batch Text to load multiple prompts
- Generating images for each prompt automatically
- Saving with organized filenames

**What it does:** Generate 4 different images from a single text input with multiple prompts.

### Workflow 2: Batch Image Processing

**Download:** [example_workflows/batch_image_processing.json](example_workflows/batch_image_processing.json)

This workflow demonstrates:

- Loading all images from a folder using Batch Images
- Applying upscaling/enhancement to each image
- Preserving original filenames in output

**What it does:** Upscale and enhance all images in a folder automatically.

### Workflow 3: Combined Batch Processing (Prompts × Images)

**Download:** [example_workflows/combined_batching.json](example_workflows/combined_batching.json)

This workflow demonstrates:

- Processing multiple images with multiple prompts
- Creating a matrix of variations (e.g., 3 prompts × 5 images = 15 outputs)
- Advanced batch processing techniques

**What it does:** Apply different style prompts to a set of images, creating variations.

## 🔧 Advanced Tips

### Custom Delimiters

Use different delimiters for different use cases:

```python
# Comma-separated
Delimiter: ","
Input: "style1, style2, style3"

# Pipe-separated
Delimiter: "|"
Input: "prompt1|prompt2|prompt3"

# Double newline (paragraph breaks)
Delimiter: "\n\n"
Input: "Long prompt 1

Long prompt 2"
```

### Organized File Naming

Name files with leading zeros for proper sorting:

```
✓ Good: 001_sunset.jpg, 002_mountain.jpg, 003_ocean.jpg
✗ Bad:  1_sunset.jpg, 10_mountain.jpg, 2_ocean.jpg
```

### Memory Management

For large batches:

1. Test with `max_images: 10` first
2. Use `start_index` to resume if interrupted
3. Process in chunks if memory is limited

### Combining Multiple Loops

Create complex generation matrices:

```
Prompt Loop (3 prompts) × Batch Image Loader (5 images) = 15 outputs
```

## 🐛 Troubleshooting

### Nodes Not Appearing

1. Check console for errors during startup
2. Verify files are in `ComfyUI/custom_nodes/ComfyUI-batching-nodes/`
3. Ensure `__init__.py` exists in the directory
4. Look for debug messages:

   ```
   ==================================================
   Prompt Loop Node - Loading...
   Registered nodes: ['PromptLoopNode', 'PromptFromListNode']
   ==================================================

   ==================================================
   Batch Image Loader Node - Loading...
   Registered nodes: ['BatchImageLoaderNode', 'ImageFromBatchNode']
   ==================================================
   ```

5. Restart ComfyUI completely

### No Images Loaded (Batch Images)

1. Check folder path is correct and absolute
2. Verify image extensions match (case-insensitive)
3. Check file permissions for the folder
4. Look for console message: `[BatchImageLoader] Loaded X images from...`
5. If you see `No images found`, check:
   - Path exists and is a directory
   - Files have correct extensions
   - You have read permissions

### No Prompts Generated (Batch Text)

1. Check delimiter matches your text format
2. Verify you have actual content (not just whitespace)
3. Look for count output - should be > 0
4. Try default delimiter `\n` first

### Images in Wrong Order

1. Use `sort_by: name` for consistent ordering
2. Rename files with leading zeros: `001.jpg`, `002.jpg`, not `1.jpg`, `2.jpg`
3. Check modification times if using `sort_by: modified`
4. Verify system time is correct if using `sort_by: created`

### Empty or Duplicate Prompts

1. Enable `skip_empty: True` to automatically remove blank lines
2. Check for extra newlines in your text input
3. Verify delimiter matches your text format
4. Trim whitespace before/after text

### Memory Issues with Large Batches

1. Start with small batches (`max_images: 10`) to test
2. Use `start_index` to process in chunks
3. Monitor RAM usage in task manager
4. Consider processing in smaller groups

### Combined Batching Not Working

1. Ensure both nodes output lists (OUTPUT_IS_LIST = True)
2. Check that list outputs are properly connected
3. Understand multiplication: 3 prompts × 5 images = 15 total outputs
4. May need to increase ComfyUI's memory allocation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- Inspired by the ComfyUI community's need for batch processing
- Thanks to all contributors and users!

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/hahihula/ComfyUI-batching-nodes/issues)
- **Discussions:** [GitHub Discussions](https://github.com/hahihula/ComfyUI-batching-nodes/discussions)

**Made with ❤️ for the ComfyUI community**

If this helps your workflow, consider giving it a ⭐!
