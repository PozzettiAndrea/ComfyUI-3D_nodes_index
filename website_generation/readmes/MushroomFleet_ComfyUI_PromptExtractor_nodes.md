# ComfyUI Prompt Extractor Nodes

Custom nodes for ComfyUI that extract text prompts from PNG image metadata. Recover prompts from any ComfyUI-generated image without needing the original workflow.

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Node-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **Extract prompts from PNG metadata** — Recovers positive and negative prompts from ComfyUI images
- **Smart prompt classification** — Automatically identifies positive vs negative prompts
- **Multiple extraction modes** — Longest string, positive only, negative only, or all prompts
- **Three node variants** — Single image, file path, and batch processing
- **Full metadata access** — Outputs complete workflow JSON for advanced use cases
- **Zero external dependencies** — Uses only PIL and standard Python libraries

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

Search for "DJZ Prompt Extractor" in ComfyUI Manager and click Install.

### Method 2: Manual Installation

Clone this repository into your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/MushroomFleet/ComfyUI_PromptExtractor_nodes.git
```

Restart ComfyUI after installation.

## 🎛️ Nodes

### DJZ Prompt Extractor

The main extraction node. Accepts an image input with an optional file path for metadata access.

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| `image` | IMAGE | ComfyUI image tensor |
| `image_path` | STRING | Optional: Direct path to PNG file (recommended for full metadata) |
| `extraction_mode` | ENUM | How to extract prompts |

**Outputs:**
| Output | Type | Description |
|--------|------|-------------|
| `prompt` | STRING | Extracted positive prompt |
| `negative_prompt` | STRING | Extracted negative prompt |
| `metadata_json` | STRING | Full metadata as JSON |

### DJZ Prompt Extractor (Path)

Simplified node that takes only a file path. Use when you have the path to a PNG file.

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| `image_path` | STRING | Path to PNG file |
| `extraction_mode` | ENUM | How to extract prompts |

**Outputs:** Same as main node.

### DJZ Prompt Extractor (Batch)

Processes all PNG files in a directory. Useful for bulk prompt extraction.

**Inputs:**
| Input | Type | Description |
|-------|------|-------------|
| `directory_path` | STRING | Path to folder containing PNGs |
| `max_images` | INT | Maximum images to process (1-100) |
| `extraction_mode` | ENUM | How to extract prompts |

**Outputs:**
| Output | Type | Description |
|--------|------|-------------|
| `prompts_list` | STRING | All extracted prompts (separated by ---) |
| `filenames_list` | STRING | Corresponding filenames |

## 🔧 Extraction Modes

| Mode | Description |
|------|-------------|
| `longest_string` | Returns the longest string found in metadata (default) |
| `positive_only` | Attempts to identify and return only the positive prompt |
| `negative_only` | Attempts to identify and return only the negative prompt |
| `all_prompts` | Returns all found prompts concatenated with \| separator |

## 💡 Usage Examples

### Basic Prompt Recovery

Connect a Load Image node to the extractor to recover its original prompt:

```
[Load Image] → [DJZ Prompt Extractor] → [Show Text]
                                      → [CLIP Text Encode]
```

### Re-generate with Extracted Prompt

Use the extracted prompt directly in a new generation:

```
[Load Image] → [DJZ Prompt Extractor] 
                    ↓ prompt
               [CLIP Text Encode (Positive)]
                    ↓ negative_prompt  
               [CLIP Text Encode (Negative)]
                    ↓
               [KSampler] → [Save Image]
```

### Batch Extract from Output Folder

Extract prompts from all images in your output directory:

```
[DJZ Prompt Extractor (Batch)]
    directory_path: "ComfyUI/output"
    max_images: 50
         ↓
    [Show Text] — View all extracted prompts
```

### Using File Path for Full Metadata

For complete metadata extraction, provide the file path directly:

```
[Load Image]
    ↓ image
[DJZ Prompt Extractor]
    image_path: "/path/to/your/image.png"
         ↓
    prompt, negative_prompt, metadata_json
```

## ⚠️ Important Notes

### PNG Metadata Preservation

ComfyUI embeds workflow and prompt data in PNG `tEXt` chunks. This metadata is lost when:

- Images are converted to tensors (IMAGE type in ComfyUI)
- Images are re-saved by other applications
- Images are uploaded to social media or image hosts
- Images are converted to JPEG or other formats

**For best results:** Use the `image_path` input with the original PNG file path, or use the Path variant node.

### Prompt Classification

The node uses two methods to classify prompts as positive or negative:

1. **Content analysis** — Looks for common negative prompt keywords (ugly, blurry, watermark, deformed, etc.)
2. **Workflow tracing** — Analyzes node connections to determine if a CLIPTextEncode connects to a sampler's positive or negative input

Classification may not be 100% accurate for unusual workflows or unconventional negative prompts.

## 🔍 How It Works

1. **Read PNG chunks** — Parses the PNG file structure to find `tEXt` and `iTXt` metadata chunks
2. **Extract JSON** — ComfyUI stores `workflow` and `prompt` data as JSON strings
3. **Find CLIPTextEncode nodes** — Locates all text encoding nodes in the workflow
4. **Extract text inputs** — Pulls the `text` field from each encoder's inputs
5. **Classify prompts** — Determines positive vs negative based on content and connections
6. **Return results** — Outputs the classified prompts and full metadata

## 🌐 Related Projects

This node is the Python/ComfyUI implementation of the prompt extraction logic. A browser-based JSX version is also available:

**[ComfyUI-Prompt-Extractor-JSX](https://github.com/MushroomFleet/ComfyUI-Prompt-Extractor-JSX)** — React component for extracting prompts in web applications

## 🐛 Troubleshooting

### "No prompts extracted" or empty output

- Ensure you're using the original PNG from ComfyUI's output folder
- Check that the file hasn't been re-saved or converted
- Try providing the `image_path` directly instead of relying on the tensor

### Prompts are misclassified

- Use `all_prompts` mode to see everything found
- Check the `metadata_json` output for the raw workflow data
- Some custom workflows may not follow standard positive/negative patterns

### File not found errors

- Use absolute paths when possible
- Check that the path doesn't contain special characters
- Verify the file exists and is readable

## 📄 License

MIT License — free for personal and commercial use.

---

## 📚 Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{comfyui_prompt_extractor_nodes,
  title = {ComfyUI Prompt Extractor Nodes: Custom nodes for extracting text prompts from PNG metadata},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI_PromptExtractor_nodes},
  version = {1.0.0}
}
```

### Donate:

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)