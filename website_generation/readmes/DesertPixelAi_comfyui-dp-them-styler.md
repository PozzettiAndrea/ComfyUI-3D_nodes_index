# ComfyUI DP Dynamic Random Styler

A dynamic theme-based prompt generator for ComfyUI that creates versatile, random prompts optimized for face swap workflows.

## Features

- **Dynamic Theme Loading**: Automatically loads themes from the `data/` folder
- **Face Swap Optimized**: All prompts start with "photo of" and include "bare face, looking at camera"
- **Flexible Age Input**: Accepts numeric age and auto-converts to categories (child, teenager, young adult, adult, middle aged, elderly)
- **Gender Support**: Configurable gender selection (male, female, random)
- **Generation Modes**: Fixed (consistent results) or Randomize (new combinations each time)
- **Extensive Themes**: 29+ pre-built themes including Overwatch, Cyberpunk, Star Wars, and more

## Node Inputs

- **theme**: Select from available theme folders
- **generation_mode**: "fixed" (consistent) or "randomize" (random combinations)
- **gender_selection**: "male", "female", or "random"
- **age** (optional): Numeric age input (0-120, default: 25)

## Node Outputs

- **prompt**: Generated positive prompt
- **negative**: Generated negative prompt (if available)
- **theme_info**: Preview information about the selected theme
- **selected_theme**: Name of the currently selected theme

## Folder Structure

```
data/
├── Theme Name/
│   ├── base_prompt.txt          # Main template with {placeholders}
│   ├── theme_art_style.txt      # 1 detailed art style that capture the theme style for all theme images
│   ├── color_theme.txt          # 20+ color combinations
│   ├── costume_design.txt       # 20+ costume/outfit designs
│   ├── background_and_atmosphere.txt # 20+ background settings
│   ├── pose.txt                 # 20+ pose descriptions
│   └── negative.txt             # 1 Negative prompt template for all theme images
```

## Placeholders

### Global Placeholders (work in all themes):
- `{gender}`: male/female (from node input)
- `{age}`: exact age number (from node input) 
- `{age_category}`: auto-converted age category

### Theme-Specific Placeholders:
Any `.txt` file in a theme folder becomes a `{placeholder}`:
- `{theme_art_style}`, `{color_theme}`, `{costume_design}`, etc.

## Example Base Prompt Template

```
photo of a {gender} Overwatch hero, {age_category}, bare face, looking at camera, {pose}, wearing {costume_design} in {color_theme}, {background_and_atmosphere}, {theme_art_style}, solo scene
```

## Creating Custom Themes

1. Create a new folder in `data/` with your theme name
2. Add `base_prompt.txt` with your template using placeholders
3. Add any number of `.txt` files with 20 items each (one per line)
4. Optionally add `negative.txt` for negative prompts
5. The node will automatically detect and load your new theme

## Requirements

- Designed for SDXL models
- Optimized for face swap workflows
- Semi-realistic output (not flat 2D)
- Solo scenes only (no multiple people)

## Installation

Place in your ComfyUI `custom_nodes` folder and restart ComfyUI. 