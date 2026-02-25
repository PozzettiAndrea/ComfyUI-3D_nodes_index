# CSV Wildcard Node for ComfyUI

A ComfyUI custom node that provides dynamic text substitution using wildcards and CSV files. Perfect for creating varied prompts with consistent relationships between terms.

## Installation

1. Navigate to your ComfyUI's custom_nodes directory
2. Clone this repository: `git clone https://github.com/illuminatianon/comfyui-csvwildcards.git`
3. Restart ComfyUI

## Usage

### Basic Structure

The node system provides two main ways to substitute text:

1. Simple wildcards: `{filename}` or `{directory/filename}`
2. CSV-based wildcards: `{csv:filename:column}` or `{csv:directory/filename:column}`

### Directory Organization

You can organize your wildcard files in the `data` directory using subdirectories of any depth:

```
data/
  # Direct files in root
  animal.txt              # Simple wildcard file
  monster.txt             # CSV wildcard file (can coexist with .txt)
  monster.csv
  monster/
    types.txt
    abilities.txt
  pokemon/
    gen1/
      types.txt
      moves.csv
      abilities.csv
    gen2/
      types.txt
      moves.csv
```

Key points about directory structure:
- Files can exist at any depth
- Both .txt and .csv files can be organized in directories
- A name can be used for all three: .txt, .csv, and directory:
  - `{name}` will use `name.txt` for simple wildcards
  - `{csv:name:column}` will use `name.csv` for CSV wildcards
  - `{name/file}` will look in the `name/` directory
- All three can be used in the same prompt:
  ```
  The {monster} saw a {csv:monster:color} creature in {monster/types}
  ```
- Use forward slashes (`/`) for subdirectories, even on Windows

### Simple Wildcards

Simple wildcards use text files where each line is a possible value. For example, `animal.txt`:
```
wolf
dragon
bear
tiger
```

Use these in your templates:
```
A {animal} with {texture} fur                     # Direct file reference
A {monster} with {monster/abilities}              # File and directory reference
A {pokemon/gen1/types} Pokemon                    # Deep path reference
```

### CSV Wildcards

CSV wildcards maintain relationships between related terms using CSV files with headers. Example `monster.csv`:
```csv
color,size,texture
red,large,scaly
blue,small,furry
green,medium,slimy
purple,tiny,rough
```

Use these in your templates:
```
The {csv:monster:color} creature was {csv:monster:size}                              # Direct file reference
A Pokemon with {csv:pokemon/gen1/moves:name} that causes {csv:pokemon/gen1/moves:effect}  # Deep path reference
```

Important: All references to the same CSV file in a single prompt will use values from the same row, maintaining consistency in your descriptions.

### Node Setup

1. Add a `CSVWildcardNode` to your workflow
2. Enter your prompt template in the text area
3. (Optional) Connect a seed value to control randomization
4. Connect the output to any node that accepts a string input (like a CLIP Text Encode node)

#### Inputs

- **prompt_template** (required): The text template containing wildcards to be substituted
- **seed** (optional): Integer value to control randomization
  - If connected, the same seed will always produce the same substitutions
  - If not connected, random values will be used each time
  - Useful for reproducing specific results or batch processing

### Example Templates

Basic wildcards:
```
A {animal} with {texture} skin and {appendage} appendages
```

CSV with relationships:
```
The {csv:monster:color} {animal}-like monster has {csv:monster:size} {appendage} with a {csv:monster:texture} texture
```

Mixed directory usage:
```
A {pokemon/gen1/types} Pokemon that knows {csv:pokemon/gen1/moves:name} which has {csv:pokemon/gen1/moves:power} power
```

## Tips

1. CSV files must have a header row
2. Column names in CSV files are case-insensitive
3. Spaces and special characters in column names are stripped
4. Missing wildcards will remain unchanged in the output (useful for debugging)
5. Always use forward slashes (`/`) for paths, even on Windows
6. Directory paths can be of any depth (e.g., `{folder/subfolder/file}`)

## Error Handling

- Missing files: The system will silently skip missing wildcard files
- Malformed CSV references: Invalid CSV placeholders will be left unchanged
- Empty files: Empty files will be treated as having no valid options
- Directory references: Must include explicit file path with forward slash
- Ambiguous names: Direct file matches take precedence over directories unless path is specified