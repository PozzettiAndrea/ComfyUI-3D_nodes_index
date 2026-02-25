# AB Wildcard - ComfyUI Wildcard Processor

**A powerful text processing engine for ComfyUI prompts.**

Pure **text processing** focused on: Wildcards, Variables, Conditional Logic, Tag Aggregation, Weighted Selection, and Deep Nesting.

---

## Features

* **Wildcards** — Load random entries from `.txt` and `.yaml` files
* **Dynamic Choices** — `{a|b|c}` random selection with range support
* **Variables** — Define once (`$var={...}`), reuse everywhere (`$var`)
* **Conditional Logic** — `[if condition : true | false]` with AND/OR/NOT/XOR
* **Tag Aggregation** — `<[Tag]>` to pick from YAML cards by tag
* **Global Presets** — Auto-load variables from `globals.yaml`

---

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/a-und-b/ComfyUI_AB_Wildcard.git
pip install -r ComfyUI_AB_Wildcard/requirements.txt
```

Restart ComfyUI.

---

## Wiring

This node is **pure text processing** — it takes text input and outputs processed text.

| Output | Connect To |
|--------|-----------|
| `text` | CLIP Text Encode or any other text input |

---

## Syntax Reference

### Wildcards

```text
__colors__              Pick random line from wildcards/colors.txt
__folder/file__         Supports subdirectories
__2$$colors__           Pick 2 random entries
__1-3$$colors__         Pick 1 to 3 random entries
```

### Random Choices

```text
{red|blue|green}        Pick one randomly
{2$$a|b|c|d}            Pick exactly 2
{1-3$$a|b|c|d}          Pick 1 to 3
{2$$ and $$a|b|c|d}     Pick 2, joined with " and " instead of ", "
{~a|b|c}                Sequential (seed-based, same seed = same pick)
{50%yes|no}             50% chance for "yes", else "no"
{5::red|3::blue|green}  Weighted choice (red=5, blue=3, green=1)
{a|{b|{c|d}}}           Nested choices (unlimited depth)
```

### Variables

```text
$color = {red|blue}     Define variable
$color                  Use variable (outputs "red" or "blue")
$color.clean            Replace _ and - with spaces
$color.upper            UPPERCASE
$color.lower            lowercase
$color.title            Title Case
```

### Conditional Logic

```text
[if red : fire theme | water theme]           If "red" in prompt
[if $var=fire : hot | cold]                   Variable equality
[if A AND B : both | not both]                AND logic
[if A OR B : either | neither]                OR logic
[if NOT dark : bright scene]                  NOT logic
[if (A OR B) AND NOT C : complex logic]       Grouping
```

### Tag Aggregation (YAML Cards)

```yaml
# In wildcards/chars.yaml
Fire Mage:
  Prompts:
    - "robed wizard, fire magic, flames"
  Tags:
    - mage
    - fire
```

```text
<[mage]>                Pick any entry tagged "mage"
<[mage AND fire]>       Pick entry with both tags
<[fire OR ice]>         Pick entry with either tag
```

### Utility Functions

```text
[shuffle: a, b, c, d]         Randomize order
[clean: text, , with, ,gaps]  Remove double commas/spaces
```

### Comments

```text
// This line is ignored
# This is also a comment
text here  // inline comment
```

---

## Wildcards Folder Structure

```
wildcards/
├── globals.yaml          # Auto-loaded variables
├── colors.txt            # Simple text list
├── styles.txt
├── examples/
│   ├── characters.yaml   # YAML cards with Tags
│   └── environments.yaml
└── PROMPT_TEMPLATES.txt  # Example prompts
```

### Text Files (.txt)

One entry per line:

```text
red
blue
green
```

### YAML Cards (.yaml)

```yaml
Card Name:
  Description:
    - Optional description
  Prompts:
    - "prompt text 1"
    - "prompt text 2"
  Tags:
    - tag1
    - tag2
  Prefix:
    - "prepended to prompt"
  Suffix:
    - "appended to prompt"
```

### Global Variables (globals.yaml)

```yaml
quality: masterpiece, best quality
style: cinematic lighting
```

These are available as `$quality`, `$style` in all prompts.

---

## Example Prompt

```text
// Variables for consistency
$creature = {dragon|phoenix|griffin}
$color = {red|blue|gold}

// Main prompt
__examples/quality__,
a majestic $creature with $color scales,
[if $color=red : fire breathing, flames | [if $color=blue : ice breath, frost | lightning crackling]],
__examples/lighting__,
{epic|dramatic|cinematic} composition

// Use character cards
<[warrior]> battling the $creature
```

---

## Tips

1. **Batch Generation** — Use ComfyUI's "Queue Batch" (not Latent batch size) for variations
2. **Hot Reload** — Click "Refresh Wildcards" button to reload files without restart
3. **Autocomplete** — Type `__` to trigger wildcard suggestions
4. **Debug** — Check the console for processing errors

---

## License

MIT

---

## Credits

This node is a heavily modified fork of [UmiAI](https://github.com/Tinuva88/Comfy-UmiAI).

**Changes from original**:
- **Removed**: LLM integration, LoRA handling, resolution control, negative prompt handling, API calls
- **Added**: Weighted selection syntax (`{5::red|3::blue}`), deep nesting support, custom separators (`{2$$ and $$a|b}`)
- **Refactored**: Pure text processing focus, single output node, streamlined codebase

Many thanks to the original UmiAI developers for the foundational wildcard processing architecture.
