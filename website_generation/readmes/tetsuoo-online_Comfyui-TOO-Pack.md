# ComfyUI-TOO-Pack 🎨
<img width="2398" height="1304" alt="image" src="https://github.com/user-attachments/assets/f873d352-db24-4751-b2a8-760789c7ff68" />

**Tetsuoo's custom nodes pack for ComfyUI**

A collection of utility nodes designed to enhance your ComfyUI workflow with smart image loading, metadata management, widget extraction, Krita integration and more.

**Category:** `TOO-Pack`

---

## 📦 Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/tetsuoo-online/Comfyui-TOO-Pack
```


### Requirements

- **ComfyUI** (latest version recommended)
- **Python** 3.8+
- **PyTorch**
- **Pillow** (PIL)
- **NumPy**

---

## 🎯 Nodes Overview

| Node | Category | Description |
|------|----------|-------------|
| [Simple Image Loader](#simple-image-loader-) | `TOO-Pack/image` | Simple image loader with a dynamic preview, no need to start the workflow :) |
| [Smart Image Loader](#smart-image-loader-) | `TOO-Pack/image` | Flexible image loader with multiple sources |
| [Smart Image Saver](#smart-image-saver-) | `TOO-Pack/image` | Intelligent saver with flexible naming and metadata |
| [Smart Image Saver (Advanced)](#smart-image-saver-advanced-) | `TOO-Pack/image` | Advanced saver with dynamic naming and A1111/Civitai metadata |
| [TOO Crop Image](#too-crop-image-) | `TOO-Pack/image` | Interactive cropping tool  |
| [TOO lmage Metadata](#too-image-metadata-) | `TOO-Pack/image` | Metadata editing  |
| [Krita Bridge](#krita-bridge-) | `TOO-Pack/image` | Auto-load images from Krita |
| [Extract Widget From Node](#extract-widget-from-node-) | `TOO-Pack/utils` | Extract widget values from workflow nodes |
| [Collection Categorizer](#collection-categorizer-llm-) | `TOO-Pack/utils` | Categorize files with local LLM (Ollama) |

---

## 📚 Node Documentation

### Simple Image Loader 🖼

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

An image loader that show instant preview with any path. You're no longer limited to ComfyUI/input folder.</br>
The idea was inspired by the <b>Load Image (Path)</b> node from [comfyui-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), with a few more features.

<img width="354" height="637" alt="Image" src="https://github.com/user-attachments/assets/70d198bc-3267-4349-9c4e-963a1d7000c8" />

#### Features

- 🖼️ **Image input via path** img_path will work with any path on your computer, it doesn't have to be in ComfyUI folders
- 🖼️ **Image Preview** Instant preview, no need to start the workflow. Can be toggled on/off
- 📊 **A1111/Civitai** metadata extraction
- 🔄 **ComfyUI** workflow extraction
- **Returns file path** of loaded image

#### Parameters

**Required Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **img_path** | STRING | Direct path to an image file | - |

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **IMAGE** | IMAGE | The loaded image (from image input or widgets) |
| **FILE_PATH** | STRING | Path of loaded file |
| **metadata** | METADATA | A1111/Civitai metadata extracted from file |
| **workflow** | WORKFLOW | ComfyUI workflow extracted from file |

</details>

---

### Smart Image Loader 🖼

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

A flexible image loader that supports multiple input sources with metadata extraction.

#### Features

- **Multiple sources**: txt, direct path, directory, or direct image
- **Smart priority order** with configurable inputs
- **Random selection** with reproducible seed
- **Multiple formats** supported (PNG, JPG, JPEG, BMP, WEBP, TIFF)
- 🖼️ **Image Preview**
- 📊 **A1111/Civitai** metadata extraction
- 🔄 **ComfyUI** workflow extraction
- **Returns file path** of loaded image

#### Parameters

**Required Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **seed** | INT | Seed for reproducible random selection | `0` |
| **img_dir_level** | INT | Subdirectory depth: -1=all, 0=current, 1-10=levels | `0` |
| **show_preview** | BOOLEAN | Show image preview in the node | `True` |

**Optional Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **txt_path** | STRING | Path to text file containing image paths | - |
| **img_path** | STRING | Direct path to an image file | - |
| **img_directory** | STRING | Path to directory containing images | - |
| **image** | IMAGE | Direct image input (priority for IMAGE output) | - |

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **IMAGE** | IMAGE | The loaded image (from image input or widgets) |
| **FILE_PATH** | STRING | Path of loaded file |
| **metadata** | METADATA | A1111/Civitai metadata extracted from file |
| **workflow** | WORKFLOW | ComfyUI workflow extracted from file |

#### Priority Order

The node loads images in this order (from highest to lowest priority):

1. **image** ⚡ : Uses the provided image input (for passing images only - does not load metadata or workflow)
2. **txt_path** 📄 : Randomly selects a path from text file
3. **img_path** 🖼 : Loads the specific image file
4. **img_directory** 📁 : Randomly selects an image from directory


#### Usage Examples

**Case 1: Text file with image list**
```python
# Content of image_list.txt:
# /path/to/image1.png
# /path/to/image2.jpg
# /path/to/image3.webp

txt_path = "/path/to/image_list.txt"
seed = 42  # Reproducible
```

**Case 2: Direct path to image**
```python
img_path = "/path/to/specific/image.png"
```

**Case 3: Image directory**
```python
img_directory = "/path/to/images/"
seed = 123
```

**Case 4: Combination with priority**
```python
txt_path = "/path/to/list.txt"       # Priority 1
img_path = "/path/to/fallback.png"   # Priority 2 (if txt_path fails)
img_directory = "/path/to/backup/"   # Priority 3 (if img_path fails)
```

#### Technical Details

**Text file format (txt_path)**

The text file should contain one image path per line:

```
/home/user/images/photo1.png
/home/user/images/photo2.jpg
/home/user/images/photo3.webp
```

- Empty lines are ignored
- UTF-8 encoding supported
- A random path is selected using the seed

**Seed handling**

- **seed = 0**: Different random selection each run
- **seed > 0**: Identical selection with same parameters (reproducible)

**FILE_PATH values**

| Value | Description |
|-------|-------------|
| Full path | Image loaded from txt_path, img_path or img_directory |
| `"external_input"` | Image provided via image parameter |
| `"none"` | No valid source found (error) |

</details>

---

### Smart Image Saver 💾

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

An intelligent image saver that replaces the SAVE_IMG subgraph with flexible filename customization.

#### Features

- **Flexible naming**: Customizable prefix, suffix, and separator
- **Date tokens**: YYYY, MM, DD, HH, mm, ss, timestamp support
- **Smart metadata extraction**: Auto-extract seed and model name from workflow
- **Node targeting**: Target nodes by class name or direct ID (#10)
- **Multiple formats**: WEBP (lossy/lossless), PNG, JPG/JPEG
- **Metadata preservation**: Saves prompt and workflow in EXIF/PNG info

#### Parameters

**Required Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **images** | <span style="background-color:#7c2d12;color:#fb923c;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">IMAGE</span> | Images to save | - |
| **output_folder** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Output folder (supports date tokens) | `YYYY-MM-DD` |
| **prefix** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Filename prefix (supports date tokens) | `ComfyUI_YYYY-MM-DD_HHmmss` |
| **seed_node_name** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Node containing seed (class name or #ID) | `KSampler` |
| **model_node_name** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Node containing model (class name or #ID) | `CheckpointLoaderSimple` |
| **suffix** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Filename suffix (supports date tokens) | `""` |
| **output_format** | <span style="background-color:#4a5568;color:#a0aec0;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">COMBO</span> | Image format | `webp` |
| **quality** | <span style="background-color:#1e4d3e;color:#34d399;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">INT</span> | Compression quality (1-100) | `97` |

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **images** | <span style="background-color:#7c2d12;color:#fb923c;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">IMAGE</span> | Pass-through of input images |
| **filepath** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Path of the first saved file |

#### Filename Structure

The node builds filenames in this order:
```
[prefix]_[seed]_[model_name]_[suffix].[format]
```

Elements are joined by the separator. Empty elements are skipped.

#### Usage Examples

**Case 1: Basic usage with date folder**
```python
output_folder = "YYYY-MM-DD"           # → 2024-01-30/
prefix = "render_YYYYMMDD"              # → render_20240130
seed_node_name = "KSampler"
model_node_name = "CheckpointLoaderSimple"
```
**Output:** `2024-01-30/render_20240130_123456_mymodel.webp`

**Case 2: Target node by ID**
```python
seed_node_name = "#10"                  # Target node with ID 10
model_node_name = "#5"                  # Target node with ID 5
```

**Case 3: Disable seed or model**
```python
seed_node_name = ""                     # Don't include seed
model_node_name = ""                    # Don't include model
prefix = "my_render"
suffix = "HHmmss"                       # Add timestamp
```
**Output:** `my_render_143025.webp`

#### Date Tokens

All date tokens are replaced with current date/time values:

| Token | Description | Example |
|-------|-------------|---------|
| `YYYY` | Year (4 digits) | 2024 |
| `MM` | Month (2 digits) | 01 |
| `DD` | Day (2 digits) | 30 |
| `HH` | Hour 24h (2 digits) | 14 |
| `mm` | Minutes (2 digits) | 30 |
| `ss` | Seconds (2 digits) | 25 |
| `timestamp` | Unix timestamp | 1706626225 |

#### Node Targeting

**By class name:**
```python
seed_node_name = "KSampler"
model_node_name = "CheckpointLoaderSimple"
```

**By ID:**
```python
seed_node_name = "#10"                   # Targets node with ID 10
```

</details>

---

### Smart Image Saver (Advanced) 💾

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

Node for saving images with advanced file naming and A1111/Civitai Auto V3 compatible metadata.

**Category:** TOO-Pack/image

#### Features

- Dynamic file naming with workflow extraction
- Metadata injection/editing
- Support for 3 universal inputs (`any1`, `any2`, `any3`)
- Automatic model and LoRA extraction with hash calculation
- Targeted text replacement
- Customizable date formatting
- A1111/Civitai compatible metadata
- Output formats: PNG, JPG, WebP

#### Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| `images` | IMAGE | Images to save (required) |
| `metadata` | METADATA | Optional metadata |
| `workflow` | WORKFLOW | Workflow to embed |
| `any1` | * | Universal input 1 |
| `any2` | * | Universal input 2 |
| `any3` | * | Universal input 3 |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `images` | IMAGE | Images passthrough |
| `filepath` | STRING | Saved file path |

#### Configuration (JS Interface)

##### DATA
Create custom data fields for metadata and naming.

**Value formats:**
- **Static text:** `"my_text"`
- **Widget extraction:** `#123:widget_name` (node ID) or `ClassName:widget_name`
- **Any input:** `[any1]`, `[any2]`, `[any3]`

**Example:**
```
name: positive
value: #45:text

name: model_used
value: [any1]
```

##### DATE FORMAT
Format dates for naming.

- **date1:** Date format (e.g. `YYYY-MM-DD`)
- **date2:** Time format (e.g. `HHmmss`)
- **date3:** Custom format

**Available tokens:** `YYYY`, `YY`, `MM`, `DD`, `HH`, `mm`, `ss`, `timestamp`

##### MODEL
Automatic model extraction.

**Value:** `#123:ckpt_name` or `[any1]`

The node automatically calculates:
- Model name (basename without extension)
- Model hash (first 10 characters of SHA256)

##### LORAS
Automatic LoRA extraction with Civitai-compatible hash.

**Add multiple loras:**
- Lora 1: `#45:lora_name` or `[any1]`
- Lora 2: `#67:lora_name` or `[any2]`

**Multiline support:** If `[any1]` contains:
```
lora1.safetensors
lora2.safetensors
```
→ Both are parsed automatically

##### TEXT REPLACE
Replace text in fields before naming.

**Target:**
- Empty or `[any1]`/`[any2]`/`[any3]` → Apply to all fields
- `positive` → Apply only to "positive" field
- `model` → Apply only to model

**Example:**
```
target: positive
in: (masterpiece)
out: 
```
→ Removes "(masterpiece)" from positive prompt

##### NAMING
Build filename with available elements.

**Available fields:**
- `output_folder` : Output subfolder
- `prefix` : File prefix
- `extra1`, `extra2`, `extra3` : Additional fields
- `model` : Model name
- `suffix` : File suffix
- `separator` : Separator character (default: `_`)

**Available sources:**
- Empty (ignored)
- `[any1]`, `[any2]`, `[any3]` : Universal inputs
- Data field name: `positive`, `seed`, `steps`, etc.
- `model`, `loras` : Extracted values
- `%date1`, `%date2`, `%date3` : Formatted dates

**Naming example:**
```
prefix: %date1
extra1: positive
model: model
suffix: seed
separator: _
```
→ `2025-02-12_beautiful_landscape_MyModel_12345.webp`

##### OUTPUT
Output configuration.

- **format:** `png`, `jpg`, `webp`
- **quality:** 1-100 (for jpg/webp)
- **save metadata:** Include A1111 metadata
- **embed workflow:** Embed ComfyUI workflow (except JPG)

#### Usage Examples

##### Example 1: Naming with model and seed

**Configuration:**
```
DATA:
  - name: seed, value: #10:seed

MODEL:
  - extract: KSampler:ckpt_name

NAMING:
  - prefix: %date1
  - model: model
  - suffix: seed
  - separator: _
```

**Result:** `2025-02-12_MyCheckpoint_8675309.webp`

##### Example 2: LoRA extraction from any1

**Workflow:**
```
ExtractWidgetFromNode → any1 (TOO Smart Image Saver)
```

**Configuration:**
```
LORAS:
  - lora 1: [any1]

NAMING:
  - prefix: %date1
  - extra1: loras
```

**If any1 contains:**
```
style_lora_v2.safetensors
quality_lora_v1.safetensors
```

**Generated metadata:**
```
Lora hashes: "style_lora_v2: a1b2c3d4e5f6, quality_lora_v1: f6e5d4c3b2a1"
```

##### Example 3: Prompt cleanup with Text Replace

**Configuration:**
```
TEXT REPLACE:
  - target: positive
  - in: (masterpiece, best quality)
  - out: 

NAMING:
  - prefix: positive
```

**If positive = "beautiful landscape, (masterpiece, best quality)"**  
**→ Filename:** `beautiful_landscape.webp`

#### Practical Use Cases

##### 1. Multi-LoRA Workflow
Use `ExtractWidgetFromNode` to retrieve all used LoRAs → connect to `any1` → The node automatically calculates all hashes for Civitai compatibility.

##### 2. Organization by Model
Configure `output_folder: model` to automatically sort images by model used.

##### 3. Complete Metadata
Create data fields for all important parameters (seed, steps, cfg, sampler, scheduler) → The node generates complete A1111 metadata readable by Civitai and Automatic1111.

##### 4. Smart Naming
Use `any` inputs to inject dynamic information from other nodes (tags, descriptions, scores, etc.).

#### Tips

- **Data fields** are flexible: create as many fields as needed
- **[any1]**, **[any2]**, **[any3]** accept any data type (converted to string)
- **Multiline** is supported for loras: one line = one lora
- **LoRA hashes** exclude safetensors metadata (Civitai AutoV3 compatible)
- **Text replace** applies to extracted values before filename construction
- **Empty lines** in data fields are automatically ignored
- The **metadata** input has priority over node data fields, unless data fields are explicitly set (enables metadata injection/editing)

</details>

---

### Extract Widget From Node 🔧

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

Extracts specific widget values from any node in the ComfyUI workflow.

#### Features

- **Targeted extraction** of specific widgets by name
- **Multiple widgets** supported (comma-separated)
- **Multi-node support**: Targets all nodes matching class name
- **Direct ID targeting** with `#ID` syntax
- **Intelligent parsing** of nested structures
- **"on" filter**: Ignores disabled elements

#### Parameters

**Required Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **node_name** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Node class name or `#ID` to target | - |
| **widget_names** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Widget name(s) to extract (comma-separated) | - |

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **extracted_values** | <span style="background-color:#1e3a5f;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Extracted values (multiline if multiple) |

#### Usage Examples

**Case 1: Extract a single widget**
```python
node_name = "KSampler"
widget_names = "seed"
```
**Output:** `"12345"`

**Case 2: Extract multiple widgets**
```python
node_name = "CLIPTextEncode"
widget_names = "text, strength"
```
**Output:** 
```
beautiful landscape, masterpiece
0.85
```

**Case 3: Target specific node by ID**
```python
node_name = "#10"
widget_names = "ckpt_name"
```

**Case 4: Extract from multiple matching nodes**
```python
node_name = "LoraLoader"
widget_names = "lora_name"
```
**Output (if 2 LoraLoader nodes exist):**
```
style_lora.safetensors
detail_lora.safetensors
```

#### Technical Details

**Node Targeting**

The node supports two targeting modes:

1. **By class name** (e.g., `"KSampler"`)
   - Finds **all nodes** of this class
   - Extracts from all matching nodes

2. **By ID** (e.g., `"#10"`)
   - Targets **specific node** with ID 10
   - Only one node targeted

**Widget Extraction**

- **Simple values**: `"my_value"`
- **Multiple values**: Separated by newlines
- **Comma support**: `"widget1, widget2"` extracts both

**Nested Dictionary Handling**

The node intelligently handles nested dictionaries:

**Simple structure:**
```json
{
  "lora_name": "my_lora.safetensors",
  "strength_model": 0.85
}
```

**Nested structure (Power Lora Loader):**
```json
{
  "loras": {
    "on": true,
    "lora_name": "my_lora.safetensors",
    "strength_model": 0.85
  }
}
```

The node automatically extracts values from both structures.

**"on" filter**

If a dictionary contains `"on": false`, its values are **ignored**.

#### Advanced Use Cases

**1. Extract prompts from workflow**
```python
node_name = "CLIPTextEncode"
widget_names = "text"
```

**2. Retrieve used seeds**
```python
node_name = "KSampler"
widget_names = "seed"
```

**3. List all loaded models**
```python
node_name = "CheckpointLoader"
widget_names = "ckpt_name"
```

**4. Extract control parameters**
```python
node_name = "ControlNetLoader"
widget_names = "control_net_name, strength"
```

</details>

---

### TOO Crop Image 🖼

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

Interactive tool for cropping your image before output.

<img width="593" height="900" alt="Image" src="https://github.com/user-attachments/assets/e21571be-fd90-4f8b-bb95-9287f90e06fd" />

If you use the image input then the cropping will apply to it. However the interactive preview works only with img_path input so you will need to use that.
You can also use only img_path like you would with a Simple Image Loader

</details>

---

### TOO Image Metadata 🖼

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

Editing tool for A1111/Civitai metadata.

<img width="472" height="678" alt="Image" src="https://github.com/user-attachments/assets/3891ca35-3e5a-4d46-b797-16faef5111dd" />

Very straight forward, you will need <b>TOO Simple Image Loader</b> or <b>TOO Smart Image Loader</b> to input the metadata to modify. Any empty field will be ignored, the node will not erase any original metadata unless you specify something.</br>
For the model field you might want to follow A1111/Civitai syntax [``Model hash: <hash>, Model: modelName``] -> Only 1 model can be input, as far as I know... Maybe something to investigate later x)</br>
As for the loras, the syntax is [``Lora hashes: "<lora1>:<hash>,<lora2>:<hash>,<lora....>:<hash>"``] -> As many loras as necessary</br>

</details>

---

### Krita Bridge 🎨

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

Automatically loads the latest image from the `input/krita/` folder for seamless Krita integration.

#### Features

- **Automatic loading** of latest image from krita folder
- **Real-time detection** of new files
- **Auto-update** during generation
- **Alpha support**: extracts alpha channel as mask
- **Auto-create** folder if doesn't exist
- **No parameters** - works directly

#### Parameters

**Required Parameters**

**No parameters required** - The node works automatically!

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **image** | <span style="background-color:#7c2d12;color:#fb923c;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">IMAGE</span> | The loaded image (RGB) |
| **mask** | <span style="background-color:#4c1d95;color:#c4b5fd;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">MASK</span> | Mask extracted from alpha channel |

#### Setup

**Working Directory**

The node automatically loads from:
```
ComfyUI/input/krita/
```

If the folder doesn't exist, it's created automatically on first launch.

**Export from Krita**

1. **Open Krita**
2. **Create or modify** your image
3. **Export as PNG**: `File > Export`
4. **Destination**: `ComfyUI/input/krita/filename.png`
5. The node automatically detects the new file

**Recommended Workflow**

```
Krita → Export PNG → ComfyUI/input/krita/ → Krita Bridge → [your workflow]
```

#### Usage Examples

**Case 1: Simple loading**
```python
# No configuration needed
# Node automatically loads latest image
```

**Case 2: Using alpha mask**
```python
# Connect 'mask' to a mask node (Mask Composite, etc.)
# Krita image's alpha channel becomes usable mask
```

**Case 3: Iterative Krita ↔ ComfyUI workflow**
```
1. Draw in Krita
2. Export → input/krita/sketch.png
3. ComfyUI detects and generates
4. Get result
5. Refine in Krita
6. Re-export → Node loads new version
```

**Case 4: Inpainting with Krita mask**
```python
# Workflow:
# Krita Bridge (image + mask) → Inpaint Model → VAE Decode
# Krita's alpha mask defines inpainting area
```

#### Technical Details

**File Detection**

The node:
1. Scans `input/krita/` folder for all `.png` files
2. Finds file with **most recent modification**
3. Compares timestamp with last loaded file
4. Reloads if change detected

**Alpha Channel Handling**

**RGBA image (with transparency):**
- RGB channels → `image` output
- Alpha channel → `mask` output (0-1 values)

**RGB image (no transparency):**
- RGB → `image` output
- Uniform white mask → `mask` output

**Automatic Update**

The `IS_CHANGED` function returns current timestamp, forcing ComfyUI to:
- Re-evaluate node on every execution
- Detect new files in real-time
- Update image automatically

#### Krita Integration

**Krita Configuration**

1. **Set default export folder**
   - `Settings > Configure Krita > General`
   - Set default folder: `ComfyUI/input/krita/`

2. **Keyboard shortcut for quick export**
   - `Settings > Configure Krita > Keyboard Shortcuts`
   - Assign key to `Export`
   - Example: `Ctrl+Shift+E`

3. **Export format**
   - Format: **PNG**
   - Compression: as preferred
   - **Important**: Enable "Save alpha channel" if using mask

**Optimal Workflow**

```
┌─────────┐    Export PNG    ┌──────────────┐
│  Krita  │ ───────────────> │ input/krita/ │
└─────────┘                   └──────────────┘
                                      │
                                      ▼
                              ┌──────────────┐
                              │ Krita Bridge │
                              └──────────────┘
                                      │
                     ┌────────────────┴────────────────┐
                     ▼                                 ▼
                ┌────────┐                        ┌──────┐
                │ image  │                        │ mask │
                └────────┘                        └──────┘
```

</details>

---

### Collection Categorizer (LLM) 🗂

<details>
<summary><b><span style="color:#60a5fa;">Click to expand full documentation</span></b></summary>

A ComfyUI node that automatically scans your folders and categorizes content with a local LLM (Ollama).

#### Features

- **Automatic scanning** of folders (video files, archives, documents)
- **Smart categorization** via local LLM (Ollama)
- **Recursive scanning** of subfolders (optional)
- **Reproducible seed** for identical results
- **Custom Ollama models** supported
- **Auto-save** JSON output
- **Compatible** with Collection Manager
- **100% local** - no external APIs

#### Parameters

**Main Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **ollama_model** | <span style="background-color:#4a5568;color:#a0aec0;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">COMBO</span> | LLM model to use (or "custom") | `qwen2.5:7b` |
| **custom_ollama_model** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Model name if "custom" selected | - |
| **folder_path** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Path to folder to scan | - |
| **scan_subfolders** | <span style="background-color:#7c3aed;color:#a78bfa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">BOOLEAN</span> | Recursively scan subfolders | `False` |
| **save_json** | <span style="background-color:#7c3aed;color:#a78bfa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">BOOLEAN</span> | Auto-save JSON output | `True` |
| **collection_title** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Collection title | `Ma Collection` |
| **content_type** | <span style="background-color:#4a5568;color:#a0aec0;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">COMBO</span> | Content type (or "custom") | `films` |

**Optional Parameters**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| **custom_type_name** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Type name if "custom" selected | - |
| **custom_categories** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Custom categorization criteria (multiline) | (empty = LLM decides) |
| **seed** | <span style="background-color:#059669;color:#34d399;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">INT</span> | Seed for reproducible results | `0` (random) |

**Outputs**

| Parameter | Type | Description |
|-----------|------|-------------|
| **json_output** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | The complete collection JSON |
| **summary** | <span style="background-color:#2563eb;color:#60a5fa;padding:2px 8px;border-radius:4px;font-family:monospace;font-size:0.9em;">STRING</span> | Categorization summary |

#### Usage Examples

**Case 1: Movies with automatic categories**
```python
content_type = "films"
custom_categories = ""  # Empty
# LLM decides categories (Genre, Era, etc.)
```

**Case 2: TV Series with custom criteria**
```python
content_type = "series"
custom_categories = "Genre, Year, Studio"
# LLM categorizes by these criteria
```

**Case 3: Custom type**
```python
content_type = "custom"
custom_type_name = "Documentaries"
custom_categories = "Theme, Duration"
```

**Case 4: Custom model**
```python
ollama_model = "custom"
custom_ollama_model = "mistral:7b"
```

**Case 5: Reproducible results**
```python
seed = 42
# Always same result with same parameters
```

#### Installation

**Requirements**

1. **Ollama** installed and running
   ```bash
   # Download: https://ollama.ai
   ollama --version
   ```

2. **Python requests** (for local HTTP API)
   ```bash
   pip install requests --break-system-packages
   ```

3. **At least one LLM model**
   ```bash
   ollama pull qwen2.5:7b
   ```

#### Supported File Types

**Videos**
`.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`

**Archives**
`.cbz`, `.cbr`, `.zip`, `.rar`

**Documents**
`.epub`, `.pdf`, `.mobi`

**Folders**
Subfolders are treated as individual items (unless `scan_subfolders` is enabled)

#### Recommended Models

| Model | Size | Speed | Quality | Usage |
|-------|------|-------|---------|--------|
| **qwen2.5:7b** | 7B | ⚡⚡⚡ | ⭐⭐⭐⭐ | Recommended |
| **gemma3:12b** | 12B | ⚡⚡ | ⭐⭐⭐⭐⭐ | Best quality |
| **llama3.1:8b** | 8B | ⚡⚡⚡ | ⭐⭐⭐⭐ | Very reliable |
| **gemma3:4b** | 4B | ⚡⚡⚡⚡ | ⭐⭐⭐ | Fast |

#### Output Format (JSON)

```json
{
  "title": "My Collection",
  "icon": "🎬",
  "type": "Films",
  "filename": "films.json",
  "categories": [
    {
      "id": 1,
      "name": "Science Fiction",
      "subcategories": [],
      "games": ["Blade Runner", "The Matrix"]
    },
    {
      "id": 2,
      "name": "Comedy",
      "subcategories": [],
      "games": ["Superbad", "The Hangover"]
    }
  ]
}
```

</details>

---


## 🗺 ToDo

- Extract Widget From Node : aiming at nodes using name, title or ID


---

## 📄 License

MIT License

---

## 👤 Author

**Tetsuoo**

---

## 🙏 Credits

- **Claude AI ❤** - AI assistant extraordinaire
- **ComfyUI** - Amazing node-based interface
- **Ollama** - Local LLM runtime
- **Krita** - Open-source digital painting software