# ComfyUI Text Line Selector Node

The **Line Selector Node** allows you to process multiline text one line at a time, with intelligent control over how the line index advances after each generation. This is particularly useful for:

- Batch processing multiple prompts
- Cycling through different parameters or settings
- Processing lists of data entries sequentially or randomly
- Creating dynamic workflows that iterate through text-based inputs

### Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| **multiline_text** | STRING (multiline) | The input text containing multiple lines |
| **line_index** | INT | Line number to extract (1 = first line, 2 = second line, etc.) |
| **control_after_generate** | SELECTION | How to modify the index after generation |

#### Control After Generate Options:
- **fixed**: Keep the same line index (no change)
- **increment**: Move to the next line (wraps to first line after the last)
- **decrement**: Move to the previous line (wraps to last line before the first)
- **randomize**: Select a random line (avoids repeating the current line when possible)

### Outputs

| Output | Type | Description |
|--------|------|-------------|
| **selected_line** | STRING | The extracted line of text |
| **index** | INT | The line index used |

### Installation

1. Copy the entire folder to your ComfyUI custom nodes directory:
   ```
   ComfyUI/custom_nodes/line_selector_node/
   ```

2. Restart ComfyUI to load the new node

3. The node will appear in the **utils** category in ComfyUI's node browser as "Text Line Selector"

### Important Usage Notes

**The `control_after_generate` functionality is only triggered once per batch.**

Due to the way ComfyUI caches node execution results within a batch, this means that all batch items will use the same line.

- ✅ **Correct**: Set Batch Count to 1, click "Run" multiple times to progress through lines
- ❌ **Incorrect**: Set Batch Count > 1 expecting different lines per batch item
