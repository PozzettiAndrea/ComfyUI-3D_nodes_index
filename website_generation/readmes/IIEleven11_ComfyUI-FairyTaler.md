# FairyTaler Storyboard Nodes

Custom nodes that will take your conversation and turn it into 3 consecutive scenes. Meant to be used with SillyTavern but it works as a standalone too.
## Installation

1. git clone this in your custom_nodes folder ``` git clone https://github.com/IIEleven11/ComfyUI-FairyTaler.git ```
2. Restart ComfyUI
3. The nodes will appear under the "FairyTaler/Storyboard" category


## Use Case
1. I have an example workflow in this repo. load that up.
2. It's setup to work with silly tavern. just get the image generation extension and upload this workflow to it.
3. You can use it without silly tavern if you want just need to input your own %prompt%
4. You can swap models too, this whole process is somewhat heavy because it requires flux for its text understanding.

## Output
- Should look like this. Its still not perfect, we need a model better at understanding NLP. Make sure you put realistic in the constants or it will do whatever it wants.
- ![image](https://github.com/user-attachments/assets/bec75b33-b485-4eed-b529-e76ad66a7d82)

## Nodes

### 1. SceneParser
**Purpose**: Parses Ollama text output into 3 separate scene descriptions

**Inputs**:
- `ollama_text` (STRING): The text output from an Ollama Generate node
- `debug` (enable/disable): Enable debug printing
- `scene_constants` (STRING, optional): Consistent character/setting details to add to each scene
- `constants_position` (beginning/end/both): Where to place the constants in each scene
- `constants_format` (natural/tags/descriptive): How to format the constants

**Outputs**:
- `scene_1`, `scene_2`, `scene_3` (STRING): Individual scene descriptions with constants applied
- `extracted_constants` (STRING): Constants automatically extracted from LLM output

### 2. SceneToConditioning
**Purpose**: Converts scene text to CLIP conditioning for use with sampling nodes

**Inputs**:
- `scene_text` (STRING): A scene description
- `clip` (CLIP): CLIP model for text encoding
- `debug` (enable/disable): Enable debug printing

**Outputs**:
- `conditioning` (CONDITIONING): CLIP conditioning for the scene

### 3. ThreeSceneGenerator
**Purpose**: Generates placeholder images for 3 scenes (for testing/demo)

**Inputs**:
- `scene_1`, `scene_2`, `scene_3` (STRING): Scene descriptions
- `model`, `clip`, `vae`: Standard ComfyUI model inputs
- Various generation parameters (width, height, steps, cfg, seed, etc.)
- `debug` (enable/disable): Enable debug printing

**Outputs**:
- `image_1`, `image_2`, `image_3` (IMAGE): Generated placeholder images

### 4. StoryboardCompositor
**Purpose**: Combines 3 images into a single storyboard layout

**Inputs**:
- `image_1`, `image_2`, `image_3` (IMAGE): The 3 scene images
- `layout` (vertical/horizontal/grid): How to arrange the images
- `spacing` (INT): Pixels between images
- `background_color` (STRING): Background color name
- `add_labels` (enable/disable): Add "Scene 1", "Scene 2", "Scene 3" labels
- `debug` (enable/disable): Enable debug printing

**Outputs**:
- `storyboard` (IMAGE): Combined storyboard image

~5. FairyTalerStoryboard (All-in-One)~ **BROKEN**
**Purpose**: Complete storyboard creation from Ollama text

**Inputs**:
- `ollama_text` (STRING): The text output from an Ollama Generate node
- Layout and styling options (same as StoryboardCompositor)
- `image_1`, `image_2`, `image_3` (IMAGE, optional): If provided, creates visual storyboard
- `scene_constants` (STRING, optional): Consistent character/setting details
- `constants_position` (beginning/end/both): Where to place the constants
- `constants_format` (natural/tags/descriptive): How to format the constants

**Outputs**:
- `scene_1`, `scene_2`, `scene_3` (STRING): Parsed scene descriptions with constants
- `storyboard` (IMAGE): Combined storyboard (visual if images provided, text-based if not)
- `extracted_constants` (STRING): Constants automatically extracted from LLM output

## Scene Constants Feature

The **Scene Constants** feature ensures character and setting consistency across all three scenes by automatically adding specified details to each scene description.

### 🤖 Automatic Constant Extraction (NEW!)

The nodes now automatically extract constants from LLM output! Simply ask your LLM to include constants in its response using any of these formats:

**Supported Formats:**
- `Constants: [your constants here]`
- `Scene Constants: [your constants here]`
- `Character Description: [your constants here]`
- `For consistency across all scenes: [your constants here]`
- Bullet points with `• Character:`, `• Setting:`, etc.
- `Note: For consistency throughout all scenes, maintain: [your constants here]`

**Example LLM Prompt:**
```
"Transform this roleplay text into 3 scenes for a storyboard. Also provide scene constants for character and setting consistency.

Constants: 1 girl around 25 years old, homeless looking, at a cabin in the woods, gloomy and country aesthetic

Scene 1: [scene description]
Scene 2: [scene description]
Scene 3: [scene description]"
```

### Manual Constants (Fallback)

### Example Usage:
- **Scene Constants**: `"1 girl around 25 years old, homeless looking, at a cabin in the woods, gloomy and country aesthetic"`
- **Position**: `beginning` - Adds constants at the start of each scene
- **Format**: `natural` - Adds proper punctuation for natural flow

### Position Options:
- **beginning**: Constants appear at the start of each scene
- **end**: Constants appear at the end of each scene  
- **both**: Constants appear at both beginning and end (for maximum consistency)

### Format Options:
- **natural**: Adds commas/periods for natural sentence flow
- **tags**: Raw format without additional punctuation
- **descriptive**: Formats as complete sentences with periods

### Example Results:
**Original Scene**: `"A girl sits on the front steps slaughtering time."`

**With Constants** (beginning, natural): 
`"1 girl around 25 years old, homeless looking, at a cabin in the woods, gloomy and country aesthetic, A girl sits on the front steps slaughtering time."`

## Example Workflow

### Basic Workflow:
1. **Ollama Generate** → `ollama_text`
2. **SceneParser** (with scene_constants) → `scene_1`, `scene_2`, `scene_3`
3. **CLIP Text Encode** (3x) → `conditioning_1`, `conditioning_2`, `conditioning_3`
4. **KSampler** (3x) → `latent_1`, `latent_2`, `latent_3`
5. **VAE Decode** (3x) → `image_1`, `image_2`, `image_3`
6. **StoryboardCompositor** → `storyboard`

### Simplified Workflow:
1. **Ollama Generate** → `ollama_text`
2. **FairyTalerStoryboard** (with scene_constants) → `scene_1`, `scene_2`, `scene_3`, `storyboard`
3. Use the scene descriptions with your preferred image generation workflow
4. Connect the generated images back to **FairyTalerStoryboard** for final composition

## Tips

1. **For best results**: Use the individual nodes for maximum control over the image generation process
2. **For quick testing**: Use the FairyTalerStoryboard all-in-one node
3. **Scene Constants**: Essential for character consistency - include age, appearance, setting, and style
4. **Layout options**: 
   - Vertical: Scenes stacked top to bottom
   - Horizontal: Scenes side by side
   - Grid: 2x2 layout with 3 scenes
5. **Debug mode**: Enable to see parsing details and troubleshoot issues
