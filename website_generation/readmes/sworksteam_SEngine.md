# SEngine - SWORKS_TEAM LoRA Browser for ComfyUI

A ComfyUI plugin that provides a sidebar interface for browsing, downloading, and applying SWORKS_TEAM LoRAs from Civitai. Current implementation uses **klein-9b** and **klein-9b-base** models.

![SEngine Sidebar](https://img.shields.io/badge/ComfyUI-Custom_Node-blue)

## Features

### Core Features
- **Tabbed Interface** - Clean UI with LoRAs and Settings tabs
- **Sidebar Browser** - Browse all SWORKS_TEAM LoRAs with image previews
- **Tag Filtering** - Filter LoRAs by tags using a multi-select dropdown
- **Search** - Search by name, trained words, or tags
- **Auto-Download** - LoRAs are automatically downloaded on first use
- **Smart Validation** - Helpful popups guide you if API key or cookie is missing
- **Dynamic Node** - Strength sliders appear on the node for each selected LoRA
- **Overall Strength** - Master strength slider (0.0 - 1.0) to control all LoRAs at once
- **Reorder LoRAs** - Change the order LoRAs are applied using up/down buttons
- **Standard Storage** - Downloads go to ComfyUI's `models/loras/` folder

### Saved Configurations
- **Save Favorites** - Save your LoRA combinations with a 💾 button
- **Thumbnail Preview** - Automatically captures last generated image as preview
- **Quick Load** - One-click to restore saved configurations
- **Persistent Storage** - Saved to browser localStorage

### Advanced Upload Features
- **Batch Image Selection** - When batch_size > 1, choose which image to upload
- **Auto-extracted Metadata** - Prompt, seed, sampler, CFG, steps automatically detected
- **Automatic LoRA Tagging** - All used LoRAs tagged on Civitai post
- **Flux Tool Tagging** - Model name automatically added
- **ComfyUI Tool Tagging** - SEngine configuration (overall strength + LoRA strengths) included
- **Image-to-Image Support** - Creates composite images showing source → generated

### Performance & Reliability
- **Memory Optimization** - LoRAs cached in memory to prevent reloading
- **Clear Cache Button** - Manually free memory when needed
- **Corrupted File Detection** - Automatically detects and re-downloads corrupted files
- **Connection Tracing** - Smart positive/negative prompt detection via node connections

## Installation

### Option 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/SWORKS_TEAM/SEngine.git
pip install -r SEngine/requirements.txt
```

### Option 2: Manual Download

1. Download the repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/SEngine`
3. Install requirements: `pip install -r requirements.txt`

### Option 3: ComfyUI Manager

Search for "SEngine" in ComfyUI Manager and click Install.

---

After installation, restart ComfyUI.

## Requirements

- ComfyUI (recent version with sidebar support)
- Python packages (install via `pip install -r requirements.txt`):
  - `Pillow` (usually included with ComfyUI)
  - `blurhash` (for image upload)
  - `numpy` (usually included with ComfyUI)
  - `requests` (for Civitai upload)

## Usage

### 1. Open the Sidebar

Click the **⚡ bolt icon** in ComfyUI's sidebar to open the SEngine panel.

### 2. Configure Settings

Switch to the **Settings** tab and enter:

- **Civitai API Key** - Get it from [Civitai Account Settings](https://civitai.com/user/account)
  - Required for downloading LoRAs
  - Saved locally in your browser

- **Session Cookie** (for uploading only):
  - Log into Civitai in your browser
  - Open DevTools (F12) → Application → Cookies
  - Copy the value of `__Secure-civitai-token`
  - Paste into the Session Cookie field

**Note:** If you try to select LoRAs or upload images without these credentials, helpful popups will guide you to enter them.

### 3. Browse and Select LoRAs

Switch to the **LoRAs** tab:

- Click **↻** to load LoRAs
- Use the **search box** to find specific LoRAs
- Use the **tag dropdown** to filter by category
- **Click a LoRA** to select/deselect it

When you select your first LoRA, an **SEngine LoRA Loader** node is automatically created.

### 4. Connect the Node

Connect the SEngine node to your workflow:

```
[Load Diffusion Model] → MODEL → [SEngine LoRA Loader] → MODEL → [BasicGuider]
```

### 5. Adjust Strengths

In the **Selected** section at the bottom:

- **Overall Strength** slider (0.0 - 1.0) - Master control for all LoRAs
- Each LoRA has an **individual strength** slider (0.0 - 2.0)
- Use **▲/▼ buttons** to reorder LoRAs
- LoRAs set to 0.0 strength are effectively disabled

### 6. Save Configurations (Optional)

After setting up your perfect LoRA combination:

1. Generate an image to capture a preview
2. Click the **💾 button** in the Selected header
3. Enter a name for your configuration
4. Click **Save**

Your configuration appears in the **Saved Configurations** section with:
- Thumbnail preview
- Configuration name
- Number of LoRAs
- Save date

**Load a saved configuration:**
- Click the **📂 button** on any saved config to apply it
- Click the **🗑️ button** to delete

### 7. Run Your Workflow

- LoRAs are downloaded automatically if not cached
- Download progress is shown in the sidebar
- Downloaded LoRAs stored in `ComfyUI/models/loras/`
- Memory-optimized: LoRAs loaded once and cached

### 8. Upload to Civitai (Optional)

After generating images, share them to Civitai:

#### Single Image Upload

1. Generate an image
2. Click **📤 Upload Last Image** at the top of the LoRAs tab
3. The image is uploaded with:
   - Auto-extracted metadata (prompt, seed, sampler, CFG, steps)
   - All LoRAs tagged
   - Flux model name tagged
   - SEngine configuration tagged
   - Post auto-published

#### Batch Image Selection

When using `batch_size > 1`:

1. Generate multiple images
2. Click **📤 Upload Image (X)** - shows number of images
3. A modal appears with thumbnails of all generated images
4. Click the image you want to upload
5. Proceed with normal upload flow

#### Image-to-Image Workflows

If your workflow includes **Load Image** nodes:

1. SEngine detects img2img workflow
2. Shows preview modal with composite image
3. Choose:
   - **Upload Composite** - Source images → generated image
   - **Upload Original Only** - Just the generated image
   - **Cancel** - Cancel upload

The composite displays source images on the left with an arrow pointing to the generated image on the right.

### 9. Memory Management

If you experience memory issues:

1. Go to **Settings** tab
2. Click **Clear LoRA Memory Cache**
3. This frees RAM by clearing cached LoRA weights

LoRAs will be automatically reloaded from disk on next use.

## Interface Overview

### LoRAs Tab
- **Upload Button** - Upload last generated image(s) to Civitai
- **Saved Configurations** - Quick access to favorite setups
- **Search & Filter** - Find and browse LoRAs
- **LoRA Grid** - Visual browser with previews
- **Selected LoRAs** - Currently active LoRAs with strengths

### Settings Tab
- **Node Status** - Shows if SEngine node is connected
- **Civitai API Key** - For downloading LoRAs
- **Session Cookie** - For uploading images
- **Clear Memory** - Free LoRA cache

## Node Inputs/Outputs

| Input | Type | Description |
|-------|------|-------------|
| model | MODEL | Base model to apply LoRAs to |
| clip | CLIP | (Optional) CLIP model for text encoder LoRA weights |

| Output | Type | Description |
|--------|------|-------------|
| MODEL | MODEL | Model with LoRAs applied |
| CLIP | CLIP | CLIP with LoRAs applied |

## Node Widgets

| Widget | Range | Description |
|--------|-------|-------------|
| overall_strength | 0.0 - 1.0 | Master strength multiplier for all LoRAs |
| [LoRA Name] | 0.0 - 2.0 | Individual strength for each selected LoRA |

## File Locations

| File | Location | Purpose |
|------|----------|---------|
| Downloaded LoRAs | `ComfyUI/models/loras/` | Standard ComfyUI loras folder |
| API Cache | `SEngine/cache/api_cache.json` | Cached LoRA list (1 hour) |
| Download Manifest | `SEngine/cache/manifest.json` | Tracks downloaded files |
| Saved Configs | Browser localStorage | User-saved configurations |

## Troubleshooting

### LoRAs not loading
- Check the ComfyUI console for error messages
- Ensure your API key is correct in Settings tab
- Try clicking the ↻ refresh button
- If you see a popup about missing API key, follow the prompt to Settings

### Sidebar not appearing
- Make sure you're using a recent version of ComfyUI with sidebar support
- Check browser console (F12) for JavaScript errors

### Downloads failing
- Verify your Civitai API key is valid
- Check your internet connection
- Some models may require authentication
- Corrupted downloads are automatically detected and can be re-downloaded

### Upload failing
- Verify your session cookie is valid (they expire periodically)
- Re-copy the `__Secure-civitai-token` cookie from Civitai
- Check the ComfyUI console for error messages
- If you see a popup about missing cookie, follow the prompt to Settings

### Image-to-image not detected
- Ensure you're using a standard "LoadImage" node
- Check browser console (F12) for debug messages showing detected node types

### Memory issues
- Use "Clear LoRA Memory Cache" in Settings tab
- LoRAs are now cached to prevent reloading, but you can clear the cache if needed
- Corrupted files are automatically detected and cleaned up

### Batch selection not working
- Make sure batch_size > 1 in your workflow
- Check browser console (F12) for any errors
- Multiple images should show in the selection modal

## Tips & Best Practices

1. **Save your favorite combinations** - Use the 💾 button to save LoRA setups you like
2. **Use Overall Strength** - Quickly adjust all LoRAs at once instead of individual sliders
3. **Reorder matters** - LoRAs are applied in order, use ▲/▼ to experiment
4. **Batch selection** - When generating multiple images, select the best one before uploading
5. **Clear cache** - If experiencing memory issues, clear the LoRA cache periodically

## License

MIT License

## Credits

- **SWORKS_TEAM** - LoRA creators
- Built for the ComfyUI community
