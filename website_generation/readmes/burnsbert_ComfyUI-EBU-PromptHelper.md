# ComfyUI-EBU-PromptHelper

A collection of custom nodes for ComfyUI designed to enhance and manipulate prompts for image generation. These can be very useful for constructing workflows that randomize a prompt along a theme to have a lot of variety from generation to generation without having to hand generate prompts.

These nodes provide a suite of utilities for generating random color palettes, modifying and randomizing text, sampling lists, loading file contents, formatting datetime strings, and even creating abstract weather descriptions along with a randomly generated year, season, and time of day.

These work great with LLM custom nodes like my ComfyUI_EBU_LMStudio package.

See the included workflow `flux_example_ebu_prompthelper.json` for usage examples.

## Features

- **Random Color Palette Generation:**
  Generate diverse color palettes from multiple types (analogous, art house, chaotic, complementary, compound, split complementary, tetradic, triadic) with options to prefer or avoid certain color families. Color families can be customized via `color_data.py`.

- **Prompt Text Replacement:**
  Replace targeted substrings in prompts using customizable patterns. Multiple words can be specified with a delimiter (|).

- **Prompt Randomization:**
  Randomly replace substrings in a prompt with options from a list. The list can be delimited by newlines, commas, or semi-colons.

- **String Combination:**
  Combine two strings using a custom join string, with empty strings handled gracefully.

- **List Sampling and Consumption:**
  Randomly sample items from a multi-line list with optional numbering, plus functionality to consume list items one at a time.

- **File Loading:**
  Load the contents of a file as a string using UTF-8 encoding for easy prompt import and template management.

- **Current Date/Time Generation:**
  Retrieve the current datetime in multiple formats, useful for timestamping or dynamic prompt generation.

- **Season, Weather, and Time-of-Day Generation:**
  Generate abstract datetime and weather descriptions with advanced options for skewing the random selection of both year and time-of-day.

 - **Truncate at Substring:**
  Truncate a string before or after a substring

## Installation

1. **Copy Files:**
   Place the entire `ComfyUI-EBU-PromptHelper` directory into your `ComfyUI/custom_nodes/` directory.

2. **Dependencies:**
   - Ensure you have Python 3.11 or newer
   - Make sure ComfyUI is installed and updated

3. **Restart ComfyUI:**
   After copying the files and verifying your dependencies, restart ComfyUI to load the custom nodes.

## Nodes

### EBU PromptHelper Random Color Palette

Generates random color palettes using several possible generation methods. One method is randomly chosen from the enabled options.

**Inputs:**
- `include_analogous_palettes` (BOOLEAN): Include analogous palettes
- `include_art_house_palettes` (BOOLEAN): Include art house palettes
- `include_chaotic_palettes` (BOOLEAN): Include chaotic palettes
- `include_complementary_palettes` (BOOLEAN): Include complementary palettes
- `include_compound_palettes` (BOOLEAN): Include compound palettes
- `include_split_complementary_palettes` (BOOLEAN): Include split complementary palettes
- `include_tetradic_palettes` (BOOLEAN): Include tetradic palettes
- `include_triadic_palettes` (BOOLEAN): Include triadic palettes
- `palette_size` (STRING): "3 colors", "4 colors", or "5 colors"
- `prefer_color_family` (STRING): e.g., "None", "Reds", "Blues", etc.
- `avoid_color_family` (STRING): e.g., "None", "Neutrals", etc.
- `seed` (INT): Random seed (0 for non-deterministic)

**Returns:**
- `palette_string` (STRING): Comma-separated color names
- `color1` ... `color5` (STRING): Individual colors
- `palette_type` (STRING): The palette method used
- `hex_values` (STRING): Comma-separated hex codes

### EBU PromptHelper Replace

Replaces occurrences of one or more target words in a prompt with a specified replacement string.

**Inputs:**
- `prompt_text` (STRING): Input prompt text
- `word_to_replace` (STRING): Target word(s) to replace (use | as delimiter for multiple)
- `replace_with` (STRING): Replacement text
- `case_sensitive` (BOOLEAN): Whether to match case when replacing

**Returns:**
- `updated_prompt_text` (STRING): The modified prompt

### EBU PromptHelper Randomize

Replaces a target substring with a randomly selected option from a list.

**Inputs:**
- `prompt_text` (STRING): Input prompt text
- `word_to_replace` (STRING): Target substring to replace (you can include multiple strings to match separated by |, e.g. 'red|blue|yellow')
- `replacement_options` (STRING): List of possible replacements
- `random_seed` (INT): Seed for random selection
- `case_sensitive` (BOOLEAN): Whether to match case when replacing
- `delimit_options_with` (STRING): How to split options - "newlines", "commas", or "semi-colons"

**Returns:**
- `updated_prompt_text` (STRING): The modified prompt
- `word_selected` (STRING): The chosen replacement


**Weighted Options:**
- Prefix any option with `N>>` (where `N` is an integer) to weight it `N` times. So '3>>>red' would be the same as listing 'red' 3 times.

**Returns:**
- `updated_prompt_text` (STRING): The modified prompt.
- `word_selected` (STRING): The chosen replacement.

### EBU PromptHelper Combine Two Strings

Combines two strings using a specified join string.

**Inputs:**
- `str1` (STRING): First string
- `str2` (STRING): Second string
- `join_str` (STRING): String used to join (default: "\n\n")

**Returns:**
- `combined` (STRING): The joined result

### EBU PromptHelper List Sampler

Samples random items from a list, with optional numbering.

**Inputs:**
- `list` (STRING): Newline-separated list of items
- `seed` (INT): Random seed
- `number_of_elements` (INT, optional): Number of items to sample (default: 10)
- `number_sampled_list` (BOOLEAN): Whether to number the output list

**Returns:**
- (STRING): Sampled items as a newline-separated string

### EBU PromptHelper Load File as String

Loads file contents as a string using UTF-8 encoding.

**Inputs:**
- `directory` (STRING): File directory path
- `file_name` (STRING): Name of file to load

**Returns:**
- (STRING): File contents or empty string on error

### EBU PromptHelper Current DateTime

Returns the current date/time in various formats.

**Returns:**
- `date` (STRING): e.g., "February 10, 2025"
- `time` (STRING): e.g., "1:15pm"
- `datetime` (STRING): e.g., "2025-02-10 1:15:33pm"
- `datetime_for_filename` (STRING): e.g., "2025-02-10_13-15-33"

### EBU PromptHelper Consume List Item

Selects and removes an item from a list while updating a prompt.

**Inputs:**
- `word_to_replace` (STRING): Target substring to replace (you can include multiple strings to match separated by |, e.g. 'red|blue|yellow')
- `list` (STRING): Newline-separated list of options
- `seed` (INT): Random seed
- `prompt_text` (STRING, optional): Input prompt text

**Returns:**
- `updated_prompt_text` (STRING): Modified prompt
- `word_selected` (STRING): Selected list item
- `revised_list` (STRING): Remaining list items

### EBU PromptHelper Season Weather Time-Of-Day

Generates random datetime and weather descriptions.

**Inputs:**
- `year_from` (INT): Start year
- `year_to` (INT): End year
- `time_from` (STRING): Start time (e.g., "6:00am")
- `time_to` (STRING): End time (e.g., "7:00pm")
- `random_seed` (INT): Random seed
- `year_skew` (STRING): How to bias year selection
- `time_of_day_skew` (STRING): How to bias time selection

**Returns:**
- `when` (STRING): Full datetime description (e.g., "early morning during early winter of 2020")
- `when_no_year` (STRING): Description without year (e.g., "early morning during early winter")
- `weather` (STRING): Weather description

### EBU PromptHelper Truncate

This node modifies an input prompt by truncating it at the first occurrence of a specified substring. It offers options to remove everything either **before** or **after** the substring, with the choice to include or exclude the substring itself in the deletion. This is particularly useful for dynamically trimming a prompt based on a specific marker.

#### Inputs

- **prompt** (STRING): The input prompt text (multiline supported).
- **substring** (STRING): The target substring to search for within the prompt.
- **delete_option** (STRING): Dropdown selection with two options:
  - **delete before**: Removes all text that appears before the substring.
  - **delete after**: Removes all text that appears after the substring.
- **inclusive** (BOOLEAN): Toggle that determines whether the substring itself is removed:
  - **True**: The substring is removed along with the text.
  - **False**: The substring is preserved.

#### Returns

- **modified_prompt** (STRING): The prompt after the specified truncation has been applied.

#### Examples

1. **Example 1: Delete before (inclusive)**

   - **Input:**
     - `prompt`: `"Hello world, welcome to the party!"`
     - `substring`: `"welcome"`
     - `delete_option`: `"delete before"`
     - `inclusive`: `True`
     
   - **Output:**  
     `" to the party!"`  
     
     *Explanation:* Everything before and including `"welcome"` is removed.

2. **Example 2: Delete before (non-inclusive)**

   - **Input:**
     - `prompt`: `"Hello world, welcome to the party!"`
     - `substring`: `"welcome"`
     - `delete_option`: `"delete before"`
     - `inclusive`: `False`
     
   - **Output:**  
     `"welcome to the party!"`  
     
     *Explanation:* Only the text before `"welcome"` is removed; the substring remains.

3. **Example 3: Delete after (inclusive)**

   - **Input:**
     - `prompt`: `"The meeting will start at 3pm, please be on time."`
     - `substring`: `"at 3pm"`
     - `delete_option`: `"delete after"`
     - `inclusive`: `True`
     
   - **Output:**  
     `"The meeting will start "`  
     
     *Explanation:* Everything after and including `"at 3pm"` is removed.

4. **Example 4: Delete after (non-inclusive)**

   - **Input:**
     - `prompt`: `"The meeting will start at 3pm, please be on time."`
     - `substring`: `"at 3pm"`
     - `delete_option`: `"delete after"`
     - `inclusive`: `False`
     
   - **Output:**  
     `"The meeting will start at 3pm"`  
     
     *Explanation:* Only the text after `"at 3pm"` is removed; the substring remains.

This node integrates seamlessly with other EBU PromptHelper nodes, allowing you to fine-tune and manipulate prompt text dynamically.


## Requirements
- ComfyUI
- Python 3.11 or newer

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the ComfyUI team for all that you do!
- Thank you to the community making so many great custom nodes available, you've inspired me to try to do likewise.

### EBU PromptHelper Character Describer Female

Randomly generates a detailed facial description of a female character. Extremely imperfect and limited but will help you spin up quicky for colorful descriptions.

**Inputs:**
- `seed` (INT): Random seed (0 for non-deterministic).
- `eyes_enabled`, `nose_enabled`, `mouth_enabled`, `lips_enabled`, `face_shape_enabled`, `brow_enabled`, `ears_enabled`, `cheekbones_enabled`, `cheeks_enabled`, `chin_enabled`, `skin_enabled`, `makeup_enabled`, `neck_enabled`, `accessories_enabled` (BOOLEAN): Toggles for including each feature category. Makeup and accessories are off by default.

**Returns:**
- `face_description` (STRING): Multi-line description broken down by enabled categories.
- `hair_style` (STRING): Randomly selected hairstyle from STYLE_OPTIONS.
- `hair_color` (STRING): Randomly selected natural hair color from COLOR_OPTIONS.
- `facial_expression` (STRING): Descriptive facial expression.

---

### EBU PromptHelper Character Describer Male

Randomly generates a detailed facial and hair description of a male character with optional facial hair.  Extremely imperfect and limited but will help you spin up quicky for colorful descriptions.

**Inputs:**
- `seed` (INT): Random seed (0 for non-deterministic).
- `eyes_enabled`, `nose_enabled`, `mouth_enabled`, `face_shape_enabled`, `brow_enabled`, `ears_enabled`, `cheeks_and_cheekbones_enabled`, `cheekbones_enabled`, `chin_enabled`, `skin_enabled`, `neck_enabled`, `accessories_enabled` (BOOLEAN): Toggles for including each feature category. Cheeks and cheekbones can be combined. Neck and accessories are off by default.

**Returns:**
- `face_description` (STRING): Multi-line description broken down by enabled categories.
- `hair_style` (STRING): Randomly selected hairstyle from MALE_HAIR_STYLE_OPTIONS.
- `hair_color` (STRING): Randomly selected natural hair color from MALE_HAIR_COLOR_OPTIONS.
- `facial_hair` (STRING): Randomly selected facial hair style from MALE_FACIAL_HAIR_OPTIONS.
- `facial_expression` (STRING): Descriptive facial expression.

---
