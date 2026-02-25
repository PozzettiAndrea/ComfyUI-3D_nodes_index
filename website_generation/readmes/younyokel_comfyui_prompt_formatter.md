<div align="center">
  <img src="/assets/demo.gif" alt="Demonstration" width="480">
</div>

# ComfyUI Prompt Formatter

This is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that provides tools to clean, optimize, and format text prompts. It includes features like converting tags, aligning brackets, and applying weights to prompts.

## About

This project is a direct equivalent of [sd_extension-prompt_formatter](https://github.com/younyokel/sd_extension-prompt_formatter) but specifically designed for ComfyUI. This project is a fork of [uwidev's sd_extension-prompt_formatter](https://github.com/uwidev/sd_extension-prompt_formatter).

## Features

### Prompt Formatter Node(s)

- **CLIP Text Encode (Prompt Formatter)**: Equivalent to ComfyUI's `CLIP Text Encode`.
- **Prompt Formatter (Only Text)**: Similar to above, but returns `STRING` instead of `CONDITIONING`.

These nodes feature the following buttons:

#### 💫 Format Prompt
A "magic button" that optimizes the text in the input field:
- Removes mismatched brackets (`()`, `[]`).
- Aligns commas, brackets, and spacing for better consistency.
- Applies weights to bracketed text (e.g., `((word))` might become `(word:1.21)` if `BRACKET2WEIGHT` is enabled in `settings.json`).
- Removes duplicate tags within the prompt.

#### ✒️ Convert Tags
Converts **Danbooru-style tags** (e.g., `tag_name` with underscores) into a standard **comma-separated format** (e.g., `tag name,`), considering the `CONV_SPACE_UNDERSCORE` setting in `settings.json` and filtering based on `blacklisted_tags.txt`.

#### ⏪ Undo Last Change
Reverts the *last action* (either Format Prompt or Convert Tags) performed using the buttons on that specific node instance.

---

### Append String Node

This node appends a second string (`string2`) to a first string (`string1`), with following options:
- `comma`: Add a comma and space between the combined strings.
- `dedupe`: Prevent adding tags from `string2` if they already exist in `string1`.

---

## Configurations (`settings.json`)

The formatter's behavior can be customized via the `settings.json` file. Available options are described below:

| **Option**              | **Description**                                                        | **Values**                                                     | **Default**                |
|-------------------------|------------------------------------------------------------------------|----------------------------------------------------------------|----------------------------|
| `BRACKET2WEIGHT`        | Converts multiple brackets into weights.                                | `true`, `false`                                                | `true`                     |
| `COLLAPSE_LINEBREAKS`   | Collapses consecutive line breaks to remove empty lines.                | `true`, `false`                                                | `true`                    |
| `CONV_SPACE_UNDERSCORE` | Controls conversion between spaces and underscores in tags.             | `"None"`, `"Spaces to underscores"`, `"Underscores to spaces"` | `"None"`                   |
| `BLACKLIST_FILE`        | Path to the blacklist file for tag filtering.                          | *String (file path)*                                             | `"blacklisted_tags.txt"`   |

### Default Blacklist

```
tagme .*text .*bubble onomatopoeia dialogue
.*(artwork) watermark signature 20\d\d
```

The blacklist file (`blacklisted_tags.txt`) contains regular expression patterns used to filter out unwanted tags during tag conversion (✒️). Each line may include multiple patterns separated by spaces. Tags matching any of these patterns will be excluded.

## Installation

1. Clone this repository into your `custom_nodes` directory of **ComfyUI**:
   ```bash
   git clone https://github.com/younyokel/comfyui_prompt_formatter.git
   ```

2. Restart ComfyUI server.