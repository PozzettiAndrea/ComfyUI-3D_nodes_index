# 📘 UmiAI Wildcard Processor

[![Join Discord](https://img.shields.io/badge/Discord-Join%20Umi%20AI-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/9K7j7DTfG2)

**A Complete Logic Engine for ComfyUI Prompts.**

UmiAI transforms static prompts into dynamic, context-aware workflows. It introduces **Persistent Variables**, **Advanced Boolean Logic**, **Native LoRA Loading**, **Local LLM Integration**, **Vision Models**, and **External Data Fetching** directly into your prompt text box—all in a single, powerful ComfyUI node.

> 💡 **Note:** If your workflow has issues after updating, right-click the UmiAI Node and select **Fix Node (Recreate)** to reset it with correct default values.

---

## 🔄 Recent Updates

**Streamlined Node Structure:**
- Consolidated full and lite nodes into a unified `UmiAIWildcardNode`
- Disabled many specialized nodes by default (can be re-enabled in `__init__.py`)
- Core functionality remains: wildcard processing, LoRA loading, logic engine, variables

**New Features:**
- **Prompt Files (`__@filename__`)**: Load entire file content instead of random lines
- **Tag Autocomplete**: Forge-style tag suggestions from CSV files in `autocomplete-tags/` folder (enabled by default)
- **Settings-Based Features**: Toggle LLM/Vision, Danbooru API, and tag autocomplete via `umi_settings.json`

**Active Nodes:** UmiAIWildcardNode, UmiSaveImage, UmiModelManager, UmiModelSelector

---

## ✨ Key Features

### 🔋 Prompt Processing & Logic
* **🔀 Advanced Logic Engine:** Full support for `AND`, `OR`, `NOT`, `XOR`, and `( )` grouping. Use it to filter wildcards or conditionally change prompt text.
* **🧠 Persistent Variables:** Define a choice once (`$hair={Red|Blue}`) and reuse it (`$hair`) anywhere to ensure consistency across your prompt.
* **🧩 Defaults + Debug:** Use `${var|fallback}` for null-safe variables and `$debug={0|1}` for quick diagnostics.
* **🎲 Dynamic Wildcards:** Replace `__tagname__` with random selections from text files, with support for weighted ranges (`1-3$$tagname`).
* **🔄 Random Choices:** Use `{option1|option2|option3}` to randomly pick variants within your prompt.
* **📊 Weighted Choices:** Use `{25%Red|75%Blue}` for precise probability control over random selections.
* **💬 Comment Support:** Add `//` or `#` comments to document your complex prompts without affecting output.

### ✨ Editor Features
* **🎨 Syntax Highlighting:** Real-time color coding:
  - Green: Wildcards (`__tag__`), Prompt files (`__@file__`)
  - Blue: YAML tags (`<[tag]>`)
  - Yellow: Dynamic choices (`{a|b}`)
  - Gold: Range wildcards (`__2-4$$tag__`)
  - Purple: Variables (`$var`)
  - Cyan: Conditionals (`[if:]`)
  - Teal: Functions (`[shuffle:]`, `[clean:]`)
  - Orange: LoRAs (`<lora:>`)
  - Magenta: BREAK keyword
  - Red: Negatives (`**neg**`)
* **🔍 Prompt Linting:** Automatic error detection with expandable error panel. Click the lint bar to see all issues.
* **🔧 Syntax Fix:** Click Fix buttons to automatically repair broken syntax (brackets, wildcards, YAML tags).
* **🧹 Auto-Clean:** Toggle button to automatically clean up spaces, commas, and format BREAK keywords.
* **🧪 Debug Summary:** Set `$debug={1}` to auto-prepend a compact `<<DBG ...>>` line with seed/run and last pick info (disable with `$debug_summary=0`).
* **🧭 Trace Mode:** Set `$trace={1}` to include provenance (`<<TRACE ...>>`) like branch, source, and variable origins (disable with `$trace_summary=0`).
* **💡 Smart Autocomplete:** Type trigger characters for suggestions:
  - `__` → Wildcard files (random line from file)
  - `__@` → Prompt files (entire file content)
  - `<[` → YAML tags
  - `<lora:` → LoRA models
  - `$` → Variables from globals.yaml
  - After comma/space → Tag suggestions from autocomplete-tags CSV files (enabled by default, requires CSV files in `autocomplete-tags/` folder)
* **👁️ Wildcard Preview:** Hover over any `__wildcard__` to see its contents.

### 🤖 AI-Powered Features (Optional)
* **👁️ Vision Models (Optional):** Use `[VISION: custom instruction]` to describe images with local AI models (JoyCaption Alpha-2, LLava-1.5). Enable with `enable_llm_features` in settings.
* **🧠 Integrated Local LLM (Optional):** Turn simple tag lists into rich natural language descriptions using `[LLM: tag soup]` syntax (Qwen 2.5, Dolphin-Llama3.1). Enable with `enable_llm_features` in settings.
* **🎨 Danbooru Integration (Optional):** Type `char:character_name` to automatically fetch visual tags from the Danbooru API with configurable filtering. Enable with `enable_danbooru_features` in settings.
* **⚙️ Temperature Control:** Separate temperature controls for vision and text LLM models for precise output tuning.

### 🎯 LoRA Management
* **🔋 Native LoRA Loading:** Type `<lora:filename:1.0>` directly in the text. The node patches the model internally—no external LoRA Loader nodes required.
* **📦 LoRA Browser (Ctrl+L):** Visual grid browser with preview images, search, strength slider, and one-click insertion.
* **🌐 CivitAI Integration:** Fetch metadata, preview images, and trigger words from CivitAI with batch or per-card fetch buttons.
* **🛠️ Z-Image Support:** Automatically detects and fixes Z-Image format LoRAs (QKV Fusion) on the fly.
* **📊 LoRA Metadata Extraction:** Automatically pulls training tags from LoRA safetensors files for enhanced prompting.
* **💾 LRU Caching:** Efficient LoRA memory management with configurable cache limits.

### 🖼️ Browser Panels
* **📦 LoRA Browser (Ctrl+L):** Browse, search, and insert LoRAs with CivitAI metadata and preview images.
* **🖼️ Image Browser (Ctrl+I):** Booru-style gallery for generated images with metadata extraction and prompt copying.
* **💾 Preset Manager (Ctrl+P):** Save and load complete node configurations instantly.
* **📜 Prompt History (Ctrl+H):** Automatic tracking of all prompts with search and one-click restore.
* **🏷️ YAML Tag Manager (Ctrl+Shift+Y):** Analyze and export your YAML tag database.
* **📝 File Editor (Ctrl+E):** Edit wildcards and YAML files directly in ComfyUI.

### 📁 Data & File Support
* **📊 CSV Data Injection:** Load spreadsheet data (.csv) and map columns to variables (e.g., $name, $outfit) for complex character handling.
  - Namespaced CSV helpers: `$csv_name`, `$csv_outfit` (toggle via `csv_namespace`).
* **📝 Multiple File Formats:** Support for TXT (line-by-line lists), YAML (structured cards with metadata), and CSV (tabular data).
  - YAML helpers from tag logic: `$yaml_title`, `$yaml_tags`, `$yaml_description` (toggle via `yaml_namespace`).
* **🌍 Global Presets:** Automatically load variables from `wildcards/globals.yaml` into *every* prompt.
* **🗂️ Hierarchical YAML:** Support for nested category structures with Prefix/Suffix systems.

### 🎨 Advanced Controls
* **📏 Resolution Control:** Set `@@width=1024, height=1536@@` inside your prompt to control image dimensions contextually.
* **➖ Scoped Negatives:** Use `--neg:` anywhere; quote to include commas (`--neg:"lowres, low quality"`) or escape commas (`lowres\\, low quality`).
* **🔁 Recursive Processing:** Iterative prompt refinement with cycle detection (max 50 passes).
* **🎯 Seeded Determinism:** Reproducible random selections via seed control for consistent results.
* **🧭 RNG Streams:** Optional deterministic sub-streams per tag/scope (toggle `rng_streams`, use `$rng_scope` to group or `__@scope:tag__` per pick).
* **⚙️ Settings Manager:** Access settings via multiple locations:
  - **Sidebar Control Panel:** Click the UmiAI icon in ComfyUI's sidebar to open the Umi Control Panel, then click "⚙ Settings"
  - **Menu Button:** Click "⚙ UmiAI Settings" in ComfyUI's top menu bar
  - **Manual Edit:** Edit `umi_settings.json` directly in the custom node folder
  
  Available settings (all controlled globally, no per-node widgets):
  - `use_folder_paths`: Show wildcards as `__Series/MyFile__` instead of `__MyFile__`
  - `csv_namespace`: Add `$csv_` prefixed variables for CSV columns
  - `yaml_namespace`: Add `$yaml_` prefixed variables for YAML entries
  - `rng_streams`: Use deterministic RNG streams per scope/tag
  - `auto_clean`: Auto-clean output prompts (remove extra commas/spaces, fix BREAK formatting)
  - `error_lint`: Show detailed error messages (`<<ERROR_...>>`) instead of user-friendly warnings (`[...]`)
  - `lint_cleaner_enabled`: Enable/disable the prompt linting UI bar at bottom of text widget (disabled by default)
  - `enable_llm_features`: Enable LLM/Vision features (adds image input, vision_model, refiner_model, temperatures, max_tokens, custom_system_prompt, update_llama_cpp button)
  - `enable_danbooru_features`: Enable Danbooru API integration (adds danbooru_threshold, danbooru_max_tags parameters)
  - `enable_tag_autocomplete`: Enable tag autocomplete from CSV files (default: true)
  - `enable_debug_output`: Enable/disable console debug output (warnings, errors, processing info) (default: false)
* **🧷 Aliases:** Add `aliases.yaml` in any wildcards folder to map wildcard/LoRA aliases.

---

## 📦 Active Nodes

This custom node package has been streamlined to focus on core functionality. The following nodes are currently active:

### Core Nodes (Always Available)
* **UmiAIWildcardNode / UmiAIWildcardNodeLite**: Unified wildcard processor with full logic engine, LoRA loading, and prompt processing
* **UmiSaveImage**: Enhanced image saving with metadata
* **UmiModelManager**: Download and manage recommended models
* **UmiModelSelector**: Model selection helper
* **UmiTextBypass**: Conditional passthrough node that can bypass downstream nodes based on wildcard phrase matches

### Disabled Nodes (Hidden from Menu)
The following nodes are disabled by default but can be re-enabled by uncommenting imports in `__init__.py`:
* UmiPoseGenerator
* UmiEmotionGenerator
* UmiEmotionStudio
* UmiCharacterCreator
* UmiSpriteGenerator
* UmiDatasetGenerator
* UmiPositionControl
* UmiVisualCameraControl

### Optional Modules (Disabled by Default)
* `umi_utilities` - Character system, sheet tools, QWEN encoder
* `bgrm` - Background removal utilities
* `camerangle` - 3D camera angle selector

**Note:** Most advanced features (character consistency, pose library, camera control, dataset generation) were originally in separate nodes but are now integrated into the main wildcard processor or disabled to simplify the node list.

---

## ✅ UmiTextBypass (Conditional Bypass)

Use this node to **conditionally skip downstream nodes** based on phrases found in the generated prompt. It's useful for optional steps like background removal, post-processing, or alternate branches.

**How it works:**
- In **UmiAIWildcardNode**, set `bypass_phrases` (comma-separated).
- It outputs `bypass_matches` (JSON list of booleans).
- In **UmiTextBypass**, connect `bypass_matches` → `matched_list` and set `match_index`.
- When the selected match is false, downstream nodes are bypassed (via frontend toggle / next-run behavior).

**Example use case:** Only run Remove Background when the prompt includes "simple background".

**Wiring diagram (simplified):**
```text
[UmiAIWildcardNode]
  - bypass_phrases: "simple background, studio"
  -> bypass_matches ---------------------------+
                                              |
                                              v
                                      [UmiTextBypass]
                                       - matched_list
                                       - match_index: 0
                                       - passthrough_type: IMAGE
                                              |
                                              v
                                      [Remove Background]
```

---

## 🛠️ Installation

### Method 1: Manual Install (Recommended)
1.  Navigate to your `ComfyUI/custom_nodes/` folder.
2.  Clone this repository:
    ```bash
    git clone https://github.com/Tinuva88/Comfy-UmiAI
    ```
3.  **⚠️ IMPORTANT:** Rename the folder to `ComfyUI-UmiAI` if it isn't already.
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  **(Optional) Autocomplete Tags:** For Danbooru/E621-style tag autocomplete, place CSV files in the `autocomplete-tags/` folder inside the custom node directory. The node will load these tags for autocomplete suggestions when typing prompts. This feature is **enabled by default** (disable with `"enable_tag_autocomplete": false` in `umi_settings.json`).
6.  **Restart ComfyUI** completely.

### Method 2: ComfyUI Manager
* **Install via Git URL:** Copy the URL of this repository and paste it into ComfyUI Manager.

### Optional: Utilities Node (sheet tools, QWEN, dataset helpers)
**Note:** The utilities node (`umi_utilities`) is currently disabled by default. These features include:
- Sheet tools (RMBG2, sheet cropper, mask utilities)
- QWEN detailer/encoder
- Dataset helpers
- Character manager
- Pose/Emotion/Scene nodes
- Camera control

To enable these nodes, uncomment the relevant imports and node registrations in `__init__.py`.

### Optional: Local LLM Support
LLM and Vision features are **disabled by default**. To enable:
1. Edit `umi_settings.json` in the custom node folder
2. Set `"enable_llm_features": true`
3. Restart ComfyUI

When enabled, the node will automatically download and install `llama-cpp-python` when you first use these features. The installer detects your CUDA version and installs the appropriate build (CUDA 11.7, 11.8, 12.1, 12.4, or CPU).

You can disable auto-updates in the node settings if you prefer manual installation.

---

### Updating

**Node giving you a strange issue after updating? Right click the node and press "Fix Node (recreate)" and it'll repopulate with correct default values**

## 🔌 Wiring Guide (The "Passthrough" Method)

The UmiAI node acts as the "Central Brain". You must pass your **Model** and **CLIP** through it so it can apply LoRAs automatically.

### 1. The Main Chain
* Connect **Checkpoint Loader (Model & CLIP)** → **UmiAI Node (Inputs)**.
* Connect **UmiAI Node (Model & CLIP Outputs)** → **KSampler** or **Text Encode**.

### 2. Prompts & Resolution
* **Text Output** → `CLIP Text Encode` (Positive)
* **Negative Output** → `CLIP Text Encode` (Negative)
* **Width/Height** → `Empty Latent Image`

### 3. Vision Model Support (Optional)
* Connect an **Image Loader** → **UmiAI Node (Image Input)** to enable vision features.

> **⚠️ Setting up Resolution Control:**
> To let the node control image size (e.g., `@@width=1024@@`), right-click your **Empty Latent Image** node and select **Convert width/height to input**, then connect the wires.
<img width="883" height="194" alt="wvQeZXNUmL" src="https://github.com/user-attachments/assets/f6018158-297b-45a1-9593-2ce751e8cf38" />

---

## ⚡ Syntax Cheat Sheet

| Feature | Syntax | Example |
| :--- | :--- | :--- |
| **Load LoRA** | `<lora:name:str>` | `<lora:pixel_art:0.8>` |
| **Random Choice** | `{a\|b\|c}` | `{Red\|Blue\|Green}` |
| **Weighted Choice** | `{25%A\|75%B}` | `{25%Red\|75%Blue}` |
| **Logic (Prompt)** | `[if Logic : True \| False]` | `[if red AND blue : Purple \| Grey]` |
| **Logic (Wildcard)**| `__[Logic]__` | `__[fire OR (ice AND magic)]__` |
| **Operators** | `AND`, `OR`, `NOT`, `XOR` | `[if (A OR B) AND NOT C : ...]` |
| **Variables** | `$var={opts}` | `$hair={Red\|Blue}` |
| **Local Variables** | `$@var=...` | `[if $style: $@tone=soft; $@tone lighting | neutral]` |
| **Default Value** | `${var\|fallback}` | `${style\|neutral}` |
| **Coalesce** | `coalesce($a,$b,"x")` | `coalesce($style,$theme,"neutral")` |
| **Equality Check** | `$var=val` | `[if $hair=Red : Fire Magic]` |
| **Require Var** | `[require:$var\|LABEL]` | `[require:$style\|STYLE]` |
| **Assert** | `[assert: cond \| LABEL]` | `[assert: $style \| STYLE_MISSING]` |
| **Warn** | `[warn: cond \| message]` | `[warn: $style==\"\" \| style empty]` |
| **Fail-Fast** | `$fail_fast=1` | `$fail_fast=1` |
| **Forbid Tags** | `[forbid: cond \| tag1, tag2]` | `[forbid: $style==clean \| grain]` |
| **Prefer Tags** | `[prefer: cond \| tag1, tag2]` | `[prefer: $style==clean \| crisp]` |
| **CSV Namespace** | `$csv_name` | `$csv_outfit` |
| **YAML Namespace** | `$yaml_title` | `$yaml_tags` |
| **Wildcards** | `__filename__` | `__colors__` |
| **Prompt Files** | `__@filename__` | `__@long_description__` |
| **Scoped RNG Wildcard** | `__@scope:tag__` | `__@style:colors__` |
| **Weighted Range** | `1-3$$filename` | `2-4$$accessories__` |
| **YAML Tags** | `<[tagname]>` | `<[Demihuman]>` |
| **Character** | `@@name:outfit:emotion@@` | `@@elena:casual:happy@@` |
| **Danbooru** | `char:name` | `char:tifa_lockhart` |
| **Vision AI** | `[VISION: instruction]` | `[VISION: describe the mood]` |
| **LLM Naturalize** | `[LLM: tags]` | `[LLM: 1girl, solo, beach]` |
| **Set Size** | `@@w=X, h=Y@@` | `@@width=1024, height=1536@@` |
| **Negative Prompt** | `--neg: text` | `portrait --neg:"blurry, low quality"` |
| **Comments** | `//` or `#` | `// This is a comment` |
| **Debug Toggle** | `$debug={0\|1\|2}` | `$debug={2}` |
| **Trace Toggle** | `$trace={0\|1\|2}` | `$trace={2}` |
| **RNG Scope** | `$rng_scope=group` | `$rng_scope=style` |

### ⌨️ Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| **Ctrl+L** | Open LoRA Browser |
| **Ctrl+I** | Open Image Browser |
| **Ctrl+P** | Open Preset Manager |
| **Ctrl+H** | Open Prompt History |
| **Ctrl+Shift+Y** | Open YAML Tag Manager |
| **Ctrl+E** | Open File Editor |
| **Ctrl+?** | Open Shortcuts & Syntax Reference |
| **Ctrl+M** | Open Model Manager |
| **Ctrl+Shift+B** | Fix syntax errors (in text field) |
| **ESC** | Close any panel |

---

## 🧠 Advanced Boolean Logic

UmiAI features a unified logic engine that works in both your **Prompts** and your **Wildcard Filters**.

### Supported Operators
* **AND**: Both conditions must be true.
* **OR**: At least one condition must be true.
* **NOT**: The condition must be absent/false.
* **XOR**: Only one condition can be true (Exclusive OR).
* **IN**: Check if a value is in a list or substring.
* **CONTAINS**: Check if left contains right.
* **MATCHES**: Regex match (case-insensitive).
* **STARTSWITH**: Prefix check.
* **ENDSWITH**: Suffix check.
* **()**: Parentheses for grouping complex logic.
* **Quotes + Comments**: Use `"multi word"` tags and `//` comments inside logic blocks.

### 1. Logic in Prompts (`[if ...]`)
You can change the text of your prompt based on other words present in the prompt (or variables).

Constraint helpers (optional sugar):
* `[require:$var|LABEL]` to emit `<<ERROR_MISSING:LABEL>>` when a variable is missing.
* `[assert: cond | LABEL]` to emit `<<ERROR_ASSERT:LABEL>>` when a condition fails.
* `[warn: cond | message]` to emit `<<WARN:message>>` when a condition is true (only in debug/trace).
* `[forbid: condition | tag1, tag2]` to push tags into the negative prompt when condition is true.
* `[prefer: condition | tag1, tag2]` to inject positive tags when condition is true.
* Local variables: use `$@var=...` inside a branch and `$@var` inside the same branch only.

```text
// Simple check: If 'red' AND 'blue' are present, output 'Purple'.
[if red AND blue : Purple | Grey]

// Variable check: If $char is defined as 'robot', add oil.
[if $char=robot : leaking oil | sweating]

// Elif chains
[if $style=retro : film grain
 elif $style=modern : clean lines
 else: neutral]

// Complex grouping
[if (scifi OR cyber) AND NOT space : futuristic city | nature landscape]

// Nested conditions
[if fantasy : [if magic AND NOT tech : wizard | knight | modern soldier]]

// Comments and quoted tags in logic
[if "ice mage" AND $style=="clean" // dev note
 : arcane frost | neutral]
```

### Quick Test Prompt
```text
$style={retro_film|modern_clean|vintage_35mm}
[if $style startswith "retro" : film grain, chromatic aberration
 elif $style contains "clean" : clean lines, minimal noise
 elif $style matches "35mm$" : halation, soft highlights
 else: neutral]
$style
```

### 2. Logic in Wildcards (`__[ ... ]__`)
You can search your Wildcards and YAML cards (Global Index) for entries that match specific tags.

```text
// Find characters tagged as both "Demihuman" and "Dark Skin"
__[Demihuman AND Dark Skin]__

// Find entries tagged "Fire" OR "Ice" but NOT "Water"
__[(fire OR ice) AND NOT water]__
```

---

## 🤖 AI-Powered Features (Optional)

**Enable these features:**
1. Edit `umi_settings.json`
2. Set `"enable_llm_features": true`
3. Restart ComfyUI

### 👁️ Vision Models (Image Captioning)

UmiAI can use local vision models to analyze images and generate descriptions automatically.

**Supported Models:**
* **JoyCaption Alpha-2**: High-quality image captioning
* **LLava-1.5**: General-purpose vision understanding

**Usage:**
```text
// Basic image description
[VISION: describe this image in detail]

// Custom instructions
[VISION: describe the character's outfit and pose]

// Combine with other features
A detailed illustration of [VISION: describe the character], $style style
```

**Setup:**
1. Enable LLM features in `umi_settings.json`
2. Connect an image to the UmiAI node's image input
3. Select a vision model from the dropdown (appears when enabled)
4. Use `[VISION: instruction]` tags in your prompt
5. The model runs on CPU to preserve GPU VRAM

**Settings (When Enabled):**
* **Vision Temperature**: Controls creativity (default 0.5)
* **Vision Max Tokens**: Limits description length

### 🧠 LLM Prompt Naturalizer

Turn "tag soup" (e.g., 1girl, solo, beach) into lush, descriptive prose using a local Large Language Model.

**Supported Models:**
* **Qwen2.5-1.5B (Fast)**: Low RAM usage, good for quick descriptions
* **Dolphin-Llama3.1-8B (Smart)**: Uncensored, follows complex instructions perfectly

**Usage:**
```text
// Convert tags to natural language
[LLM: 1girl, solo, standing, beach, sunset, happy expression]

// The LLM will output something like:
// "A lone girl stands on the beach at sunset, her face radiating happiness..."

// Mix with other features
[LLM: $char1, $outfit, $location] in the style of __ArtistNames__
```

**Setup:**
1. Enable LLM features in `umi_settings.json`
2. In the `llm_model` widget (appears when enabled), select "Download Recommended"
3. Choose your preferred model (Qwen for speed, Dolphin for quality)
4. Use `[LLM: tags]` syntax in your prompt

**Customization (When Enabled):**
* **Temperature**: Controls creativity (0.7 is standard, lower for literal, higher for creative)
* **Max Tokens**: Limits description length (600 = ~1 paragraph)
* **Custom System Prompt**: Override default behavior
  * Default: "Creative Writer" persona (flowery, descriptive)
  * Example: "You are a horror writer. Describe the tags in a terrifying way."

**Note:** The LLM automatically protects `<lora:...>` tags from being modified or removed.

---

## 🔋 LoRA & Z-Image System

You no longer need to chain multiple LoRA Loader nodes. UmiAI handles it internally.

### Basic Usage
Type `<lora:` to trigger the autocomplete menu with all available LoRAs.
```text
<lora:my_style_v1:0.8>
```

### Z-Image Auto-Detection
If you are using **Z-Image** LoRAs (which normally require special loaders due to QKV mismatch), UmiAI handles this automatically.
1.  Load the file using the standard syntax: `<lora:z-image-anime:1.0>`
2.  The node detects the key format and applies the **QKV Fusion Patch** instantly.

### LoRA Metadata Extraction
UmiAI automatically reads training tags embedded in LoRA safetensors files and can inject them into your prompt.

**Settings:**
* **LoRA Behavior**:
  * **Append**: Add training tags at the end
  * **Prepend**: Add training tags at the beginning
  * **Disabled**: Don't inject tags (manual control only)

### Dynamic LoRAs
You can use wildcards or logic to switch LoRAs per generation:
```text
// Randomly pick a style LoRA
{ <lora:anime_style:1.0> | <lora:realistic_v2:0.8> }

// Conditional LoRA loading
[if fantasy : <lora:medieval_v3:0.9> | <lora:scifi_tech:0.8>]

// Variable-based LoRA
$style={anime **styleA** | realistic **styleB**}
[if styleA : <lora:anime_lora:1.0>]
[if styleB : <lora:photo_lora:0.8>]
```

**Note:** LoRAs may use either their internal filename or their actual filename for matching.

### LoRA Caching
UmiAI uses LRU (Least Recently Used) caching to efficiently manage LoRA models in memory. The cache automatically handles:
* Loading LoRAs only when needed
* Removing old LoRAs when memory limits are reached
* Garbage collection for optimal memory usage

---

## 🎭 Character Consistency System (Disabled by Default)

**Note:** The following nodes are currently disabled. To enable, uncomment the relevant imports in `__init__.py`.

Maintain consistent character appearances across multiple generations with outfit and emotion variations.

### Character Folder Structure
```
ComfyUI-UmiAI/
  umi_utilities/
    characters/
      elena/
        profile.yaml      # Character definition
        reference.png     # Reference image for IP-Adapter
      kai/
        profile.yaml
        reference.png
```

### Inline Syntax (Still Works in Main Node)

Use the `@@character:outfit:emotion@@` syntax directly in your prompts:

```text
// Base character only
@@elena@@

// With outfit
@@elena:casual@@

// With outfit and emotion (full)
@@elena:casual:happy@@

// Combine with other features
A portrait of @@elena:formal:happy@@ in a garden, __ArtStyle__
```

The character syntax is processed by the main UmiAI Wildcard node even when the dedicated character nodes are disabled.

### Disabled Nodes (Uncomment in __init__.py to re-enable)

- **UmiAI Character Manager** - Single character prompt builder
- **UmiAI Character Batch Generator** - Generate all variations
- **UmiAI Sprite Export** - Organized output
- **UmiAI Character Info** - Profile debugging

---

## 🎬 Camera Control & Pose System (Disabled by Default)

**Note:** The following nodes are currently disabled. To enable, uncomment the relevant imports in `__init__.py`.

### Disabled Nodes

- **UmiAI Camera Control** - Slider-based azimuth/elevation/distance
- **UmiAI Visual Camera Control** - Interactive canvas widget
- **UmiAI Pose Library** - 30+ built-in poses
- **UmiAI Expression Mixer** - Blend emotions with weights
- **UmiAI Scene Composer** - Combine backgrounds, lighting, atmosphere

These features can be re-enabled by uncommenting the node registrations in the `__init__.py` file.

---

## 📊 LoRA Dataset Generation (Disabled by Default)

**Note:** The following nodes are currently disabled. To enable, uncomment the relevant imports in `__init__.py`.

### Disabled Nodes

- **UmiAI Dataset Export** - Kohya-compatible output
- **UmiAI Auto Caption** - Wrapper for external captioners
- **UmiAI Caption Enhancer** - Combine captions with character info
- **UmiAI Caption Generator** - Build captions from components

These features can be re-enabled by uncommenting the node registrations in the `__init__.py` file.

---

## 📦 Bundled Wildcards

UmiAI includes ready-to-use wildcards in the `wildcards/` folder. You can add your own .txt, .yaml, and .csv files to extend the system.

**Basic usage:**
```text
// Random line from file
__colors__

// Full file content
__@long_description__

// Weighted range (2-4 random lines)
__2-4$$accessories__

// YAML tag search
<[Demihuman AND Dark Skin]>
```

**Example prompts:**
```text
A portrait of a character with __emotions__ expression, __poses__, __backgrounds__, __lighting__

[LLM: __character_traits__, standing at __locations__]
```

---

## 🔧 Model Manager

The **UmiModelManager** node allows you to download recommended models directly in ComfyUI.

**Available in Node Menu:** UmiModelManager

### Available Categories:
- **LoRAs** - Style and character LoRAs
- **ControlNets** - Pose, depth, canny
- **Upscalers** - 2x and 4x models
- **LLMs** - Local language models (when LLM features enabled)

**Note:** If optional modules are enabled, additional model categories may appear.

---

## 🎥 Sample Workflows

Import ready-to-use workflows from the `sample workflow/` folder:

| Workflow | Description |
| :--- | :--- |
| `UmiAI-Sample.json` | Basic wildcard processing with LoRA loading |

**Note:** Example workflows for character system, camera control, and dataset generation are currently disabled. To use these features, re-enable the corresponding nodes in `__init__.py`.

---

## 📂 Creating Wildcards

UmiAI reads files from the `wildcards/` folder in your ComfyUI-UmiAI installation.

### 1. Simple Text Lists (.txt)
Create `wildcards/colors.txt`:
```text
Red
Blue
Green
Yellow
Purple
```
**Usage:** Type `__` to open autocomplete and select `__colors__`. Each generation will pick one random color.

**Weighted Ranges:**
```text
// Pick 2-4 random colors
__2-4$$colors__
```

### 1.5. Prompt Files - Full Text File Loading
The `__@filename__` syntax loads the **entire file content** as a single block of text, instead of picking a random line like wildcards do.

**Difference between wildcards and prompt files:**
- `__colors__` → Picks ONE random line from colors.txt
- `__@colors__` → Loads the ENTIRE contents of colors.txt

**Use Case:** Perfect for loading long, pre-written prompts or multi-paragraph descriptions.

Create `wildcards/fantasy_scene.txt`:
```text
A grand medieval castle stands atop a mountain peak,
surrounded by swirling clouds and ancient forests.
Dragons circle the towers as knights patrol the ramparts.
The setting sun casts golden light across the stone walls.
```

**Usage:** Type `__@` to open autocomplete and select `__@fantasy_scene__`. The entire file content will be inserted.

```text
// Load complete prompt file
__@fantasy_scene__

// Combine with other features
__@fantasy_scene__, in the style of __ArtStyles__, <lora:fantasy_v1:0.8>

// Use in conditionals
[if $theme=epic : __@fantasy_scene__ | __@modern_scene__]
```

**Note:** Prompt files use the same autocomplete menu as wildcards (showing all .txt files in the wildcards folder), but behave differently when processed.

### 2. Advanced Tag Lists (.yaml)
Create `wildcards/characters.yaml`:
```yaml
Character Name - Outfit:
  Description:
    - Brief description of the character and outfit
  Prompts:
    - 'First prompt variant with <lora:example:1.0> and tags'
    - 'Second prompt variant with different tags'
  Tags:
    - Category1
    - Category2
    - Trait1
    - Trait2
  Prefix:
    - Text to add before the selected prompt
  Suffix:
    - Text to add after the selected prompt
```

**Full Example:**
```yaml
2.5 Dimensional Temptation - Noa Base:
  Description:
    - Noa from the series '2.5 Dimensional Temptation' without a designated outfit
  Prompts:
    - '<lora:2.5D_Temptation:1> nonoa_def, Noa, blue eyes, black hair, short hair, sailor collar'
    - '<lora:2.5D_Temptation:1> nonoa_cos, Noa, blue eyes, blue hair, short hair, hair ornament'
  Tags:
    - 2.5 Dimensional Temptation
    - Noa
    - Human
    - White Skin
    - Lora
    - Girl Base
  Prefix:
    - masterpiece, best quality,
  Suffix:
    - highly detailed

A-Rank Party - Silk Outfit:
  Description:
    - Silk from the series 'A-Rank Party' wearing her canonical outfits
  Prompts:
    - '<lora:ARankParty_Silk:0.5> dark-skinned female, white hair, orange eyes, pointy ears, earrings, {swept bangs, french braid, long hair|high ponytail, swept bangs, long hair}, {SilkArcherOne, purple scarf, black jacket, long sleeves, black leotard, chest guard, red ribbon, leotard under clothes, underbust, highleg, white gloves, fur-trimmed shorts, white shorts, brown belt|SilkArcherTwo, beret, purple headwear, white ascot, cropped vest, white vest, sleeveless, elbow gloves, white gloves, vambraces, black leotard, leotard under clothes, highleg, fur-trimmed shorts, white shorts, red belt}'
  Tags:
    - A-Rank Party
    - Silk
    - Demihuman
    - Dark Skin
    - Colored Skin
    - Lora
    - Girl Outfit
  Prefix:
    -
  Suffix:
    -
```

**Usage with Tags:** Type `<` to open tag search and select `<[Demihuman]>` to randomly choose from any YAML entry with that tag.

**Tag Logic:**
```text
// AND: Both tags must be present
<[Demihuman AND Dark Skin]>

// OR: At least one tag
<[Fire OR Ice]>

// Complex logic
<[(Human OR Demihuman) AND NOT Robot]>
```

### 3. CSV Data Injection
Create `wildcards/characters.csv`:
```csv
name,outfit,hair,eyes
Alice,red dress,blonde,blue
Bob,suit,black,brown
Carol,armor,silver,green
```

**Usage:**
```text
// UmiAI automatically maps columns to variables
A portrait of $name wearing $outfit, with $hair hair and $eyes eyes
```

### 4. Global Presets
Create `wildcards/globals.yaml` to define variables that load automatically into every prompt:
```yaml
$quality: {masterpiece, best quality|high quality, detailed}
$artist: {artist1|artist2|artist3}
```

These variables are available in all prompts without needing to define them each time.

### 5. Tag Autocomplete (Danbooru/E621 Style)
UmiAI supports Forge-style tag autocomplete from CSV files, perfect for Danbooru/E621 tag databases.

**Note:** This feature is **enabled by default**. To disable, set `"enable_tag_autocomplete": false` in `umi_settings.json`.

**Setup:**
1. Place CSV files in the `autocomplete-tags/` folder inside the custom node directory
2. CSV format: One tag per line in the first column (other columns ignored)
3. Multiple CSV files are automatically merged

Example CSV (`autocomplete-tags/danbooru_tags.csv`):
```csv
1girl
solo
standing
beach
sunset
happy_expression
blue_eyes
long_hair
```

**Usage:**
- Type any text after a comma or space
- When you've typed 2+ characters, autocomplete suggestions appear
- Press Enter or click to insert the tag
- Supports fuzzy matching (type "longhair" to find "long_hair")

**Example in prompt:**
```text
masterpiece, 1gi[autocomplete suggests: 1girl]
1girl, so[autocomplete suggests: solo, socks, source_anime, ...]
1girl, solo, blu[autocomplete suggests: blue_eyes, blue_hair, blush, ...]
```

**Performance:**
- Autocomplete is query-based (filtered on the server)
- Only returns up to 50 matches per query
- Large tag databases (100k+ tags) load efficiently
- Tags are cached in memory after first load

**Note:** This is separate from Danbooru API integration (`char:character_name`). Tag autocomplete is purely local and works offline.

---

## 🎨 Danbooru Character Integration (Optional Feature)

Automatically fetch visual tags for characters from the Danbooru API.

**Enable this feature:**
1. Edit `umi_settings.json`
2. Set `"enable_danbooru_features": true`
3. Restart ComfyUI

### Basic Usage
```text
char:hatsune_miku
// Fetches: twintails, aqua_hair, aqua_eyes, headset, etc.

char:tifa_lockhart
// Fetches: black_hair, red_eyes, white_shirt, black_skirt, etc.
```

### Settings (When Enabled)
* **Danbooru Threshold**: Minimum tag score to include (higher = more relevant tags)
* **Max Danbooru Tags**: Maximum number of tags to fetch per character

### Tag Filtering
UmiAI automatically:
* Filters out overly generic tags
* Uses a blacklist to remove common/irrelevant tags
* Caches results locally to avoid repeated API calls
* Respects API rate limits

### Example
```text
// Combine with other features
$char={hatsune_miku|kagamine_rin|megurine_luka}
A portrait of char:$char in __ArtStyle__ style, $pose
```

**Note:** This is separate from the local tag autocomplete feature. Danbooru API integration fetches tags from the internet, while tag autocomplete uses local CSV files.

---

## 🎯 Advanced Techniques

### 1. Persistent Variables
Variables maintain their value throughout the entire prompt, ensuring consistency:

```text
// Define once
$hair={red|blue|green|purple}
$eyes={amber|emerald|sapphire}

// Use multiple times - same value everywhere
A girl with $hair hair and $eyes eyes,
wearing a $hair dress,
$hair theme,
[if $hair=red : fire magic | ice magic]
```

Local variables (branch-scoped):
```text
[if $style==clean : $@lens=sharp; clean light, $@lens focus | neutral]
```

Default/fallback values:
```text
${hair|brown}
${style|"neutral base"}
```

### 2. Compound Variables (Hidden Markers)
Pack multiple "keys" into one variable for complex logic:

```text
// Key 1: Visible text
// Key 2: LoRA trigger (**L1**)
// Key 3: Description trigger (**D1**)
$theme={Fire **L1** **D1**|Ice **L2** **D2**|Lightning **L3** **D3**}

// Use the theme (displays "Fire" but includes hidden **L1** **D1**)
$theme elemental magic

// Conditional LoRA loading (only sees L1, L2, L3)
[if L1: <lora:fire_element:0.8>]
[if L2: <lora:ice_element:0.8>]
[if L3: <lora:lightning_element:0.8>]

// Conditional descriptions (only sees D1, D2, D3)
[if D1: warm lighting, flames, ember particles]
[if D2: cold atmosphere, ice crystals, frost]
[if D3: electric sparks, storm clouds]
```

The `**hidden**` markers are automatically removed from the final output but remain available for logic checks.

### 2.1 Aliases (aliases.yaml)
Create an `aliases.yaml` in any wildcards folder:
```yaml
wildcards:
  vibe: styles/vintage_35mm
  skin: characters/skin_tones
loras:
  softfilm: filmgrain_soft_v2
```

### 3. Nested Conditionals
```text
$genre={fantasy **F**|scifi **S**|modern **M**}
$magic={yes **MAG**|no **NOMAG**}

[if F: [if MAG: wizard casting spells | knight with sword] |
[if S: [if MAG: psychic powers | high-tech weapons] |
[if M: modern city]]]
```

### 4. Dynamic Resolution
```text
$aspect={portrait **VERT**|landscape **HORZ**|square **SQ**}

// Set different sizes based on aspect ratio
[if VERT: @@width=768, height=1024@@]
[if HORZ: @@width=1024, height=768@@]
[if SQ: @@width=1024, height=1024@@]

A $aspect composition of...
```

### 4.1 Debug Summary
```text
$debug={1}  // level 1 summary
// Optional: disable the auto summary line
$debug_summary=0
```

### 4.2 Trace Mode
```text
$trace={1}  // level 1 summary
// Optional: disable the auto trace line
$trace_summary=0
```

### 5. Combining All Features
```text
// Variables
$char={__CharacterGirls__|__CharacterBoys__}
$style={anime **A**|realistic **R**|painterly **P**}
$location={beach|forest|city|mountains}

// LLM + Vision combo
[VISION: describe the lighting and mood] combined with [LLM: $char, standing, $location, $style style]

// Conditional LoRA
[if A: <lora:anime_style_v3:0.9>]
[if R: <lora:realistic_photo:0.8>]
[if P: <lora:oil_painting:1.0>]

// Dynamic size
@@width=1024, height=1344@@

// Danbooru character
Using visual traits from char:$char

// Logic-based details
[if beach: swimsuit, ocean waves, sunny |
[if forest: nature, trees, dappled sunlight |
[if city: urban, buildings, street |
[if mountains: peaks, clouds, hiking gear]]]]

// Negative
--neg: blurry, low quality, worst quality
```

---

## 🚀 Example Workflows

### Example 1: Compound Variables
```text
// Define complex theme variable
$theme={Fire **L1** **D1**|Ice **L2** **D2**}
$mood={Happy|Angry}
@@width=768, height=768@@

// Main prompt
(Masterpiece), char:hatsune_miku,
$theme theme.

// Logic-based LoRA loading
[if L1: <lora:fire_element_v1:0.8>]
[if L2: <lora:ice_concept:1.0>]

// Logic-based descriptions
[if D1: [if Happy: warm lighting | burning flames]]
[if D2: frozen crystal textures],

// Wildcards with weighted ranges
highlighted in __2$$colors__.

// Negative prompt
--neg: worst quality, lowres
```

### Example 2: Multi-Character Fashion Show
```text
$char1={__RandomGirls__}
$char2={__RandomGirls__}
$color1={__Colors__}
$color2={__Colors__}
$color3={__Colors__}
$color4={__Colors__}

A fullbody illustration of two girls standing together at a fashion show in the style of __ArtistNames__.
$char1 is wearing __RandomOutfit__ with a primary color of $color1 and a secondary color of $color2.
$char2 is wearing __RandomOutfit__ with a primary color of $color3 and a secondary color of $color4.
{Both girls are __SharedPose__|The girls are holding hands and smiling while __MiscPose__}.

The background is __Background__.

--neg: bad anatomy, extra limbs, blurry
```

### Example 3: Genre-Adaptive Workflow
```text
$genre={fantasy **F**|scifi **S**|cyberpunk **C**}
$character={warrior|mage|rogue|scientist|hacker}

// Genre-specific LoRAs
[if F: <lora:fantasy_rpg:0.9>]
[if S: <lora:scifi_concept:0.8>]
[if C: <lora:cyberpunk_2077:1.0>]

[LLM: $character, $genre setting, action pose, detailed]

// Genre-specific environment
[if F: medieval castle, magic particles, fantasy lighting |
[if S: space station, holographic displays, neon lights |
[if C: dystopian city, rain, neon signs, dark atmosphere]]]

@@width=1024, height=1344@@

--neg: low quality, bad hands, mutation
```

### Example 4: Vision-Enhanced Workflow
```text
// Feed an existing image to the node
[VISION: describe the character's appearance, outfit, and pose in detail]

// Enhance with LLM
[LLM: [VISION: describe the character], professional photography, studio lighting, high detail]

// Add style
in the style of __ArtistNames__, <lora:photorealistic_v2:0.7>

@@width=1024, height=1536@@
```

---

## 🔧 Node Settings Reference

### Input Parameters (Always Available)
* **text** (required): Your main prompt with UmiAI syntax
* **seed** (required): Random seed for reproducible results

### Optional Connections (Always Available)
* **model**: Model input for LoRA patching (passthrough)
* **clip**: CLIP input for LoRA patching (passthrough)
* **image**: Image input for vision models (only when LLM features enabled)

### LLM Settings (Only when `enable_llm_features: true`)
* **llm_model**: Select text model (Qwen/Dolphin) or "Download Recommended"
* **llm_temperature**: Text generation creativity (default: 0.7)
* **llm_max_tokens**: Maximum response length (default: 600)
* **llm_system_prompt**: Custom system prompt override
* **vision_model**: Select vision model (JoyCaption/LLava)
* **vision_temperature**: Vision generation creativity (default: 0.5)
* **vision_max_tokens**: Maximum vision response length
* **auto_update_llama_cpp**: Auto-install llama-cpp-python

### LoRA Settings (Always Available)
* **lora_behavior**: Append/Prepend/Disabled (tag injection mode)
* **lora_cache_limit**: Maximum cached LoRAs

### Danbooru Settings (Only when `enable_danbooru_features: true`)
* **danbooru_threshold**: Minimum tag relevance score
* **max_danbooru_tags**: Maximum tags to fetch per character

### Other Settings (Always Available)
* **resolution_control**: Enable/disable `@@width@@` syntax

### Output Parameters (Always Available)
* **model**: Model with LoRAs applied
* **clip**: CLIP with LoRAs applied
* **text**: Processed positive prompt
* **negative_text**: Generated negative prompt
* **width**: Extracted or default width
* **height**: Extracted or default height
* **lora_info**: Metadata from loaded LoRAs

### Settings Manager

Access settings via multiple locations:
- **Sidebar Control Panel:** Click the UmiAI icon in ComfyUI's sidebar, then click "⚙ Settings"
- **Menu Button:** Click **"⚙ UmiAI Settings"** in ComfyUI's menu bar
- **Manual Edit:** Edit `umi_settings.json` directly

All settings are controlled globally (no per-node widgets). Changes take effect immediately without restarting.

Example `umi_settings.json`:
```json
{
  "use_folder_paths": false,         // Show wildcard folder paths
  "csv_namespace": true,              // Add $csv_ variables
  "yaml_namespace": true,             // Add $yaml_ variables
  "rng_streams": false,               // Deterministic RNG per scope
  "auto_clean": true,                 // Auto-clean prompts (remove extra commas/spaces)
  "error_lint": false,                // Show detailed error messages vs warnings
  "lint_cleaner_enabled": false,      // Show lint UI banner
  "enable_llm_features": false,       // Enable LLM/Vision features
  "enable_danbooru_features": false,  // Enable Danbooru API integration
  "enable_tag_autocomplete": true,    // Enable tag autocomplete from CSV files
  "enable_debug_output": false        // Enable debug output in console
}
```

---

## 🎓 Tips & Best Practices

### Performance Optimization
* Use LLM features on CPU to preserve GPU VRAM for image generation
* LoRA caching automatically manages memory—increase cache limit if you use many LoRAs
* Vision models are slower—only use when needed
* Use weighted ranges (`2-4$$tags`) instead of multiple wildcards for variety

### Prompt Organization
* Use comments (`//`) to document complex prompts
* Group related logic together
* Define all variables at the top of your prompt
* Use globals.yaml for frequently-used variables

### Debugging
* Check the console output for processing details
* Use simple prompts first, then add complexity
* Test logic conditions individually before combining
* Verify wildcard files are in the correct folder

### Common Pitfalls
* Don't forget to pass Model/CLIP through the node for LoRA support
* Ensure wildcard filenames match exactly (case-sensitive)
* Close brackets/parentheses in logic expressions
* Use `|` (pipe) for choice separators, not commas
* Remember that `**hidden**` markers affect logic but not output

---

## 🔄 Processing Pipeline

Understanding the order of operations helps build complex prompts:

1. **Comment Stripping**: Remove `//` and `#` comments
2. **Load Globals**: Import variables from `wildcards/globals.yaml`
3. **Iterative Processing** (up to 50 passes):
   - Vision tag replacement (`[VISION]`)
   - LLM tag replacement (`[LLM]`)
   - Variable assignment (`$var={...}`)
   - Variable substitution (`$var`)
   - Wildcard replacement (`__tag__`)
   - Random choices (`{a|b|c}`)
   - Danbooru character fetching (`char:name`)
4. **Conditional Logic**: Apply `[if]` statements
5. **Prefix/Suffix**: Add from YAML metadata
6. **Negative Prompts**: Collect `--neg:` entries
7. **Cleanup**: Remove duplicates, extra commas, spaces
8. **LoRA Extraction**: Parse and load LoRAs
9. **Settings Extraction**: Parse `@@width@@` and `@@height@@`
10. **Output Generation**: Return all processed data

---

## 🆘 Troubleshooting

### LoRAs Not Loading
* Ensure Model and CLIP are connected to the UmiAI node inputs
* Check LoRA filename matches exactly (use autocomplete)
* Verify LoRA files are in ComfyUI's lora folder

### Autocomplete Not Working
* Restart ComfyUI after installation
* Check browser console for JavaScript errors
* Verify `js/umi_wildcards.js` exists in the node folder

### Vision/LLM Features Not Available
* Models download automatically on first use
* Check console for download progress
* Ensure internet connection for HuggingFace downloads
* Verify you have sufficient RAM/disk space

### Wildcards Not Found
* Check files are in `ComfyUI-UmiAI/wildcards/` folder
* Verify file extensions (`.txt`, `.yaml`, `.csv`)
* Use autocomplete to see available wildcards
* Check console for file loading errors

### Logic Not Working
* Verify all brackets are closed: `[if A : B | C]`
* Check operator spelling: `AND`, `OR`, `NOT`, `XOR` (case-sensitive)
* Test simple conditions first before nesting
* Use parentheses for complex expressions

### Node Errors After Update
* Right-click node → "Fix Node (Recreate)"
* Check for breaking changes in update notes
* Clear browser cache
* Restart ComfyUI

---

## 🏗️ Technical Details

### Architecture
* **Language**: Python 3 backend, JavaScript frontend
* **Dependencies**: PyYAML, Requests, PyTorch, SafeTensors
* **Optional**: llama-cpp-python, huggingface-hub
* **Integration**: Native ComfyUI custom node

### File Structure
```
ComfyUI-UmiAI/
├── __init__.py              # ComfyUI registration & API routes
├── nodes.py                 # Main processing engine
├── nodes_lite.py            # Lite node implementation
├── shared_utils.py          # Shared utilities
├── requirements.txt         # Python dependencies
├── umi_settings.json        # Feature toggle settings
├── README.md                # This file
├── js/
│   ├── umi_wildcards.js     # Frontend autocomplete UI
│   └── syntax_highlight.js  # Syntax highlighting
├── autocomplete-tags/       # CSV files for tag autocomplete (optional)
│   └── [your_tags.csv]      # Place Danbooru/E621 CSVs here
├── cache/                   # Cached Danbooru data
├── sample workflow/
│   └── UmiAI-Sample.json    # Example workflow
└── wildcards/               # Your wildcard files
    ├── globals.yaml         # Global variables
    └── [your files here]
```

### API Endpoints
* `GET /umiapp/wildcards`: Returns all available wildcards, YAML tags, and LoRAs (JSON)
* `GET /umiapp/autocomplete/tags?query=<search>&limit=50`: Returns filtered autocomplete tags from CSV files (JSON)

### Core Classes
* `UmiAIWildcardNode`: Main ComfyUI node
* `TagLoader`: File indexing and loading
* `TagSelector`: Random/seeded selection
* `TagReplacer`: Wildcard substitution
* `DynamicPromptReplacer`: Choice syntax handling
* `ConditionalReplacer`: Boolean logic evaluation
* `VariableReplacer`: Variable management
* `DanbooruReplacer`: API integration
* `LoRAHandler`: Model patching and caching
* `VisionReplacer`: Image captioning
* `LLMReplacer`: Text naturalization
* `NegativePromptGenerator`: Negative collection

---

## 💬 Community & Support

Join the **Umi AI** Discord server to share workflows, get help, and see what others are creating!

👉 **[Join our Discord Server](https://discord.gg/9K7j7DTfG2)**

### Contributing
Found a bug? Have a feature request? Open an issue on GitHub!

### Credits
Created and maintained by the Umi AI team.

**Special Thanks:**
* **VNCCS**: For the inspiration behind the Character System, Emotion Studio, and Project Folder structure.
* **NickPittas**: For the `camerangle` 3D Camera Angle Selector implementation.

---

## 📄 License

Check the repository for license information.

---

**Happy Prompting! 🎨✨**
