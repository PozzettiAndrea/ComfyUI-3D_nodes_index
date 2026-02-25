# ComfyUI Prompt Library

A collection of ComfyUI nodes for efficient prompt management and organization. Handle multi-line prompts with positive/negative separation, create prompt libraries, and extend prompts dynamically.

![grafik](https://github.com/user-attachments/assets/75f3b72e-13b3-4e3a-9b93-dbde5cc47308)

## Features

- **Double Prompt Format**: All nodes use a unified format where positive and negative prompts are separated by `---` (3-5 dashes)
- **Prompt Libraries**: Organize prompts in text files or directly in nodes
- **Smart Concatenation**: Intelligently combines prompts with proper punctuation
- **Comment Support**: Use `###` at line start for notes that won't be processed
- **Flexible Prepend/Append**: Add global settings before or after your prompts

## Nodes

### 🔤 Simple Prompt Library
Store multiple prompt projects directly in a text field within ComfyUI.
- **Projects**: Each project is separated by empty lines
- **Index**: Select which project to use (1, 2, 3, etc.)
- **Randomize**: Enable to randomly select a different project on each generation
- **Output**: Combined double prompt string and the used index

**Organizing Multiple Projects:**
You can store many different prompt variations or completely different scenes in one text field. Use `###` comments to number and label them for easy reference:

```
### 1 - Quality Base
masterpiece, best quality
---
worst quality, ugly

### 2 - Fantasy Portrait
portrait of an elf warrior, detailed armor, forest background
---
modern clothing, urban setting

### 3 - Sci-Fi Scene
futuristic cityscape, neon lights, flying vehicles
---
medieval, rustic, old fashioned

### 4 - Nature Photography
misty mountain sunrise, dramatic clouds
---

### 5 - Abstract Art
flowing colors, geometric patterns, surreal composition
---
realistic, photographic, literal
```

**Index Selection**: Set the index to 3 to use the "Sci-Fi Scene" project. The index directly corresponds to the project number (separated by empty lines).

**Random Mode**: Enable `randomize_index` to randomly pick between all available projects on each generation - perfect for exploring variations or creating diverse outputs.

![grafik](https://github.com/user-attachments/assets/bd140e38-8e21-4d97-95d7-2eefac7ec560)

### 📁 Prompt Library
File-based prompt management that reads `.txt` files containing complete scene descriptions.

**Setup:**
1. Navigate to `ComfyUI/models/prompts/`
2. Create folders for different themes/projects (e.g., `fantasy_rpg`, `cyberpunk_scenes`, `nature_photography`)
3. Add `.txt` files with complete scene descriptions
4. Files appear in the dropdown as `folder/filename`

**File Structure Example:**
```
ComfyUI/models/prompts/
├── fantasy_rpg/
│   ├── dungeon_exploration.txt    # Multiple dungeon variations
│   ├── tavern_scene.txt          # Different tavern scenarios
│   └── boss_battle.txt           # Various boss encounters
├── cyberpunk_scenes/
│   ├── neon_street.txt           # Street scene variations
│   └── hacker_hideout.txt        # Different hideout styles
└── nature_photography/
    ├── mountain_sunrise.txt       # Various mountain scenes
    └── forest_creek.txt          # Different forest moods
```

**Inside dungeon_exploration.txt:**
```
### 1 - Dark Corridor
ancient stone corridor, torchlight, moss covered walls, dripping water, medieval dungeon
---
modern elements, bright lighting, clean surfaces

### 2 - Treasure Room
golden treasures, ancient artifacts, mystical glow, dust particles in light rays
---
empty room, poor, modern items

### 3 - Monster Encounter
massive stone chamber, lurking shadows, glowing eyes in darkness, battle ready stance
---
peaceful, well lit, safe environment

### 4 - Puzzle Chamber
intricate mechanisms, mysterious symbols, blue magical energy
---

### 5 - Boss Arena
vast ceremonial hall, pillars of obsidian, lava flows, epic scale
---
small room, cramped space
```

**Key Features:**
- **Multiple Variations**: Each file can contain dozens of different scenes or variations
- **Mixed Content**: Combine related variations (different dungeon rooms) or completely different concepts in one file
- **Index Selection**: Use the index parameter to select specific scenes (e.g., index 4 = Puzzle Chamber)
- **Random Mode**: Enable `randomize_index` to randomly select from all projects in the file
- **Numbered Comments**: Use `### 1 - Name` format to easily identify which index corresponds to which project
- **Empty Negatives**: Leave negative prompts empty by having nothing after `---` (as shown in project 4)

### ➕ Prompt Extender
Add extensions to existing prompts from other nodes with flexible positioning.
- **Input**: Connect a double prompt from another node
- **Additions**: Define what to add in the text field
- **Prepend Mode**: Toggle to add extensions before (ON) or after (OFF) the input prompt
- **Output**: Combined result maintaining the double prompt format

**Usage Example:**
1. Connect Simple Prompt Library output → Prompt Extender input
2. Add extensions like:
   ```
   8k, professional photography
   ---
   lowres, amateur
   ```
3. With **Prepend Mode OFF** (default): Original + additions
4. With **Prepend Mode ON**: Additions + original (useful for global quality settings)

### 🎨 Double Prompt Encode
Convert double prompt text directly to CLIP conditioning.
- **Input**: Any text using the `---` separator format (requires connection from another node)
- **Output**: Separate positive and negative conditioning outputs
- Perfect for connecting prompt libraries directly to samplers

## Double Prompt Syntax

All nodes use this unified format:
```
positive prompt content here
---
negative prompt content here
```

- Everything above `---` → Positive prompt
- Everything below `---` → Negative prompt
- No separator → Everything becomes positive prompt
- **Empty negative allowed**: Leave blank after `---` for no negative prompt
- Separator must be on its own line (3-5 dashes: `---`, `----`, or `-----`)

**Valid Examples:**
```
# Full double prompt:
beautiful landscape, sunset
---
ugly, blurry

# Only positive prompt:
beautiful landscape, sunset

# Empty negative prompt:
beautiful landscape, sunset
---

# Even this works (only negative):
---
ugly, blurry
```

## Workflow Examples

### Scene-Based Workflow
1. Create a `ComfyUI/models/prompts/game_art/character_portraits.txt` file
2. Add multiple character descriptions separated by empty lines
3. In ComfyUI: **Prompt Library** → choose file and index → **Double Prompt Encode** → Sampler

### Modular Prompt Building with Global Settings
1. **Simple Prompt Library** (character/scene descriptions)
2. → **Prompt Extender** with Prepend Mode ON (add quality settings at the beginning)
3. → **Prompt Extender** with Prepend Mode OFF (add style details at the end)
4. → **Double Prompt Encode** → Sampler

### Global Settings Example
1. Simple Prompt Library: `warrior in armor --- modern clothing`
2. Prompt Extender (Prepend ON): `8k, professional photography --- lowres, amateur`
3. Result: `8k, professional photography, warrior in armor --- lowres, amateur, modern clothing`

## Tips

- **Comments**: Lines starting with `###` are ignored - perfect for notes and numbering projects
- **Project Numbering**: Use `### 1 - Project Name` format to keep track of which index selects which prompt
- **Organization**: 
  - One file can contain many variations of similar scenes
  - Or mix completely different concepts in one file
- **Random Exploration**: Use `randomize_index` to:
  - Use all variations automatically
  - Create diverse output sets
  - Find unexpected combinations
- **Empty Negatives**: Sometimes you don't need negative prompts - just leave the space after `---` empty
- **Prepend for Quality**: Use Prompt Extender with Prepend Mode ON to add consistent quality settings to all prompts
- **Chaining**: Connect multiple Prompt Extenders to layer details onto base scenes

## Installation

1. Clone to `ComfyUI/custom_nodes/`
2. Restart ComfyUI
3. Find nodes under "hexxacubic" category
