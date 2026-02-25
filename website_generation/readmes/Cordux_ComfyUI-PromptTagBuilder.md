# Tag Prompt Builder for ComfyUI
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)](https://github.com/Comfy-Org/ComfyUI)
[![Install via ComfyUI Manager](https://img.shields.io/badge/Install%20via-ComfyUI%20Manager-green)](https://registry.comfy.org/publishers/cordux/nodes/ComfyUI-PromptTagBuilder)

A flexible ComfyUI custom node that simplifies prompt building through organized dropdown categories. Works with any tag-based prompting system including Danbooru-style models (Illustrious, Pony Diffusion, NovelAI), Stable Diffusion, and more.

## Features

- **Organized Categories**: Quality, Style, Character, Pose, Camera, Lighting, Time, Expression, Background
- **Negative Prompts**: Dedicated node with Quality, Anatomy, Text, Artifacts, and Composition categories
- **Fully Customizable**: Edit `prompt_tags.json` to add your own tags and categories
- **Clean Output**: Automatic formatting and organization of your prompts
- **Flexible Separators**: Choose how tags are joined (commas, newlines, custom)
- **Universal Compatibility**: Works with Danbooru tags, natural language, or any prompting style

## Installation

### Method 1: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Create a new folder:
   ```bash
   mkdir ComfyUI-PromptTagBuilder
   cd ComfyUI-PromptTagBuilder
   ```

3. Copy these files into the folder:
   - `tag_prompt_builder.py` (the main node file)
   - `prompt_tags.json` (configuration file)
   - `__init__.py` (optional)

4. Restart ComfyUI

### Method 2: Git Clone

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/Cordux/ComfyUI-PromptTagBuilder.git
```

## File Structure

```
ComfyUI/
└── custom_nodes/
    └── ComfyUI-PromptTagBuilder/
        ├── tag_prompt_builder.py
        ├── prompt_tags.json
        ├── __init__.py (optional)
        └── README.md
```

### Method 3: ComfyUI Manager

1. search for `ComfyUI-PromptTagBuilder` and click install
2. Restart ComfyUI


## Usage

### Basic Workflow

1. Add **"Tag Prompt Builder"** node to your workflow (found in `utils/prompt` category)
2. Select tags from the dropdown menus
3. Add specific details in the **Custom** field
4. Connect output to your text encoder

<details><summary><h3>Screenshot</h3></summary>
  <img width="945" height="687" alt="image" src="https://github.com/user-attachments/assets/f2900ce5-6333-47cb-9b39-6e219468db9c" />
</details>

### Example: Creating an Anime Portrait

**Node Settings:**
- **NSFW**: none
- **Quality**: masterpiece, best quality, absurdres
- **Style**: anime
- **Character**: 1girl, solo
- **Pose**: standing
- **Camera**: portrait
- **Lighting**: soft lighting
- **Time**: none
- **Expression**: smile
- **Background**: simple background
- **Custom**: long hair, blue eyes, school uniform, white shirt, looking at viewer

**Output:**
```
masterpiece, best quality, absurdres, anime, 1girl, solo, standing, portrait, soft lighting, smile, long hair, blue eyes, school uniform, white shirt, looking at viewer, simple background
```

### Using the Negative Prompt Node

Add **"Negative Tag Builder"** node for organized negative prompts:

**Settings:**
- **Quality**: lowres, bad quality, worst quality
- **Anatomy**: bad anatomy, bad hands, missing fingers
- **Text**: signature, watermark, text, username, artist name
- **Artifacts**: blurry, deformed, ugly
- **Composition**: cropped, out of frame, bad composition
- **Custom**: (add any specific negatives)

**Output:**
```
lowres, bad quality, worst quality, bad anatomy, bad hands, missing fingers, signature, watermark, text, username, artist name, blurry, deformed, ugly, cropped, out of frame, bad composition
```

## Customization

### Editing Tags

Edit `prompt_tags.json` to customize available options:

```json
{
  "quality": [
    "none",
    "masterpiece, best quality",
    "your custom quality tags here"
  ],
  "style": [
    "none",
    "anime",
    "photorealistic",
    "your custom styles here"
  ]
}
```

### Available Categories (Positive Prompt)

- **nsfw**: NSFW rating tags
- **quality**: Image quality descriptors
- **style**: Art style (anime, realistic, sketch, etc.)
- **character_count**: Number of characters (1girl solo, 2girls, etc.)
- **pose**: Character poses and actions
- **camera**: Camera angles and shot types
- **lighting**: Lighting conditions
- **time**: Time of day
- **expression**: Facial expressions
- **background**: Background descriptions

### Available Categories (Negative Prompt)

- **negative_quality**: Quality issues to avoid
- **negative_anatomy**: Anatomical problems to avoid
- **text_issues**: Unwanted text/watermarks
- **negative_artifacts**: Visual artifacts to avoid
- **negative_composition**: Composition problems to avoid

### Adding New Options to Existing Categories

1. Open `prompt_tags.json`
2. Find the category you want to edit
3. Add your new option:
   ```json
   "quality": [
     "none",
     "masterpiece, best quality",
     "your new option here"
   ]
   ```
4. Save and restart ComfyUI

### Tag Format Guidelines

- Always include `"none"` as the first option in each category
- Use commas to separate multiple tags within one option
- Keep options concise and descriptive
- Group related concepts together

## Node Parameters

### Tag Prompt Builder (Positive)

**Required Inputs:**
- **NSFW**: NSFW rating (default: none)
- **Quality**: Quality tags (default: masterpiece, best quality, absurdres)
- **Style**: Art style (default: none)
- **Character**: Character count (default: 1girl, solo)
- **Pose**: Character pose (default: none)
- **Camera**: Camera angle (default: none)
- **Lighting**: Lighting type (default: none)
- **Time**: Time of day (default: none)
- **Background**: Background type (default: none)
- **Custom**: Multi-line text field for detailed descriptions
- **Expression**: Facial expression (default: none)

**Optional Inputs:**
- **separator**: String to separate tags (default: ", ")
- **newlines**: Add line breaks between tag groups (default: false)

**Output:**
- **Positive Prompt**: Combined text string

### Negative Tag Builder

**Required Inputs:**
- **Quality**: Quality issues (default: none)
- **Anatomy**: Anatomical issues (default: none)
- **Text**: Text/watermark issues (default: none)
- **Artifacts**: Visual artifacts (default: none)
- **Composition**: Composition issues (default: none)
- **Custom**: Multi-line text field for custom negatives

**Optional Inputs:**
- **separator**: String to separate tags (default: ", ")
- **newlines**: Add line breaks between tag groups (default: false)

**Output:**
- **Negative Prompt**: Combined text string

## Tips & Best Practices

### 1. **Organize Your Workflow**
Use the **Custom** field for specific details about your subject. Let the dropdowns handle the technical and stylistic aspects.

### 2. **Tag Order**
The node outputs tags in this order:
1. NSFW → Quality → Style → Character → Pose → Camera → Lighting → Time → Expression
2. Custom details
3. Background

This follows common prompting best practices where technical tags come first.

### 3. **Use "none" Liberally**
Set categories to "none" if you don't need them. This keeps your prompts clean and focused.

### 4. **Custom Separator**
Try different separators for different models:
- Standard: `, ` (comma space)
- Weighted: `:1.2, ` for emphasis systems
- Natural: ` ` (just space) for natural language models

### 5. **Enable Newlines for Readability**
Turn on `newlines` when building complex prompts to make them easier to read and debug.

### 6. **Model-Specific Presets**
Create different JSON configurations for different models by editing `prompt_tags.json` before use.

### 7. **Combine with Other Nodes**
- Chain multiple builders for complex scenes
- Use with wildcard nodes for variation
- Connect to prompt styling/weighting nodes

## Examples

### Example 1: Fantasy Character
```
Settings:
- Style: anime
- Character: 1girl, solo
- Pose: standing
- Camera: full body
- Lighting: dramatic lighting
- Expression: serious
- Custom: elf ears, long silver hair, green eyes, leather armor, holding sword
- Background: outdoors, forest

Output: anime, 1girl, solo, standing, full body, dramatic lighting, serious, elf ears, long silver hair, green eyes, leather armor, holding sword, outdoors, forest
```

### Example 2: Realistic Portrait
```
Settings:
- Quality: best quality, high quality
- Style: realistic
- Character: 1boy, solo
- Camera: close-up
- Lighting: natural lighting
- Time: golden hour
- Expression: smile
- Custom: stubble, brown eyes, casual clothing
- Background: detailed background

Output: best quality, high quality, realistic, 1boy, solo, close-up, natural lighting, golden hour, smile, stubble, brown eyes, casual clothing, detailed background
```

### Example 3: Chibi Art
```
Settings:
- Style: chibi
- Character: 2girls
- Pose: waving
- Camera: full body
- Expression: laughing
- Custom: colorful outfits, cat ears, holding hands
- Background: simple background, white background

Output: chibi, 2girls, waving, full body, laughing, colorful outfits, cat ears, holding hands, simple background, white background
```

## Troubleshooting

**Node doesn't appear in ComfyUI:**
- Verify files are in the correct directory
- Restart ComfyUI completely
- Check console for error messages

**Dropdowns are empty:**
- Ensure `prompt_tags.json` is in the same folder as the Python file
- Check JSON syntax is valid (use [jsonlint.com](https://jsonlint.com))
- Look for error messages in the console

**Tags not updating after JSON edit:**
- Restart ComfyUI (the JSON is loaded on startup)
- Verify JSON syntax is correct
- Check file permissions

**Output has unexpected formatting:**
- Check your separator settings
- Try toggling the newlines option
- Verify no trailing spaces in your JSON tags

## Model Compatibility

### Fully Compatible:
- ✅ Pony Diffusion (all versions)
- ✅ Illustrious XL
- ✅ NovelAI (Danbooru tags)
- ✅ Stable Diffusion (all versions)
- ✅ SDXL
- ✅ Most anime/manga models
- ✅ Any tag-based prompting system

### Adaptable:
- ⚠️ Natural language models (customize JSON for natural descriptions)
- ⚠️ Midjourney-style prompts (adjust separator and tag format)

## FAQ

**Q: Can I add my own categories?**
A: Yes, but it requires editing the Python code to add new inputs. Adding new options to existing categories only requires editing the JSON.

**Q: Will this work with SDXL?**
A: Yes! Just edit the JSON to use natural language descriptions instead of Danbooru tags.

**Q: Can I have multiple JSON files for different models?**
A: Currently the node uses one JSON file. You can manually swap files or edit the filename in the code.

**Q: Does this support weighted prompts like (tag:1.2)?**
A: The node passes through whatever you put in the JSON, so yes! Just include the weights in your tag options.

**Q: Can I use this for negative prompts only?**
A: Yes, use the "Negative Tag Builder" node independently.

## License

Free to use and modify for personal and commercial projects.

## Credits

Created for the ComfyUI community to streamline tag-based prompt creation across different models and prompting systems.

## Changelog

### Version 1.0
- Initial release
- Positive and negative prompt builders
- 11 customizable positive categories
- 5 customizable negative categories
- JSON-based configuration
- Flexible separator options
- Newline formatting support

---

**Need help?** Check the ComfyUI documentation or ask in the community forums!
