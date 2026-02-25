# ComfyUI Simple CSV Parser

A ComfyUI custom node that allows you to parse CSV files with positive and negative prompts.

## Features

- Drag and drop CSV files into ComfyUI's input directory
- Read prompts from CSV files line by line
- Toggle to enable/disable negative prompt column
- Outputs positive prompt, negative prompt, and total row count
- Navigate through rows using an index parameter

## Sample Workflow

![Sample Workflow](sample%20workflow%20screenshot.png)

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone <your-repo-url> ComfyUI-SimpleCSVParse
   ```

2. Restart ComfyUI

## Usage

### CSV File Format

Create a CSV file with two columns (header row is optional and will be auto-detected):

```csv
positive_prompt,negative_prompt
a beautiful landscape,"blurry, low quality"
a cute cat,"distorted, ugly"
a futuristic city,"dark, gloomy"
```

**Note:** If your prompts contain commas, wrap them in double quotes as shown above.

Or without headers:

```csv
a beautiful landscape,"blurry, low quality"
a cute cat,"distorted, ugly"
a futuristic city,"dark, gloomy"
```

### Using the Node

The node automatically detects which input method you're using. You can either select from a dropdown or enter a custom path.

#### Option 1: From Input Folder (Dropdown)
1. Place your CSV file in the ComfyUI `input` folder
2. Add the "Simple CSV Parser" node to your workflow
3. Select your CSV file from the `csv_from_folder` dropdown
4. Leave `csv_custom_path` empty
5. Set the index to choose which row to read (0 = first row)
6. Toggle "use_negative_prompt" on/off to include the negative prompt column
7. Connect the outputs to your prompt nodes

#### Option 2: From Custom Path
1. Add the "Simple CSV Parser" node to your workflow
2. Enter the full path to your CSV file in the `csv_custom_path` field
   - Mac/Linux example: `/Users/yourname/Desktop/prompts.csv`
   - Windows example: `C:\Users\yourname\Desktop\prompts.csv`
   - You can use `~` for your home directory: `~/Desktop/prompts.csv`
3. The `csv_from_folder` dropdown will be ignored if custom path is provided
4. Set the index and toggle as above
5. Connect the outputs to your prompt nodes

### Outputs

- **positive_prompt** (STRING): The positive prompt from the selected row
- **negative_prompt** (STRING): The negative prompt from the selected row (empty if toggle is off)
- **total_rows** (INT): Total number of rows in the CSV (useful for looping)
- **total_rows_string** (STRING): Total number of rows as text (for connecting to ShowText nodes)

## Example CSV

See `example.csv` for a sample file format.

## Notes

- The node automatically detects and skips header rows if they contain common headers like "positive", "positive_prompt", or "prompt"
- Index is 0-based (0 = first data row after any header)
- If the index exceeds the number of rows, an error message is returned
- Empty cells are handled gracefully
