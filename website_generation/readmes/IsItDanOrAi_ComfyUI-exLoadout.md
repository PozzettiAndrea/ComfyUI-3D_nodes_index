# exLoadout – Excel Based Loadout Manager for ComfyUI 
![Logo](https://github.com/user-attachments/assets/4108d366-1306-4db4-b25c-56cae69e9957)


### What It Is

exLoadout is a suite of lightweight ComfyUI custom nodes that let you define and switch between full “loadouts” stored in an Excel sheet. A loadout could include any node inputs that expect string values—models (checkpoints, CLIP, VAE, ControlNets, LoRAs, UNets), numeric or text variables (CFG, sampler names, scheduler types, etc.)—all pulled from a row in your sheet. By selecting a row, you instantly apply all of its settings in your workflow, with built‑in support for editing and reading those cells right inside the UI.

![image](https://github.com/user-attachments/assets/3603c82d-c3cd-445e-b2f9-10e9aaf9c68c)

### UPDATES:
V1.1:
      
      * Security updates across all nodes.
      * exLoadoutSelector - Added random Loadout functionality.

### Installation

    Download or clone this repo, ensuring the ComfyUI-exLoadout folder is placed inside your ComfyUI/custom_nodes/ folder.

    Open a terminal (or Command Prompt) and navigate to the ComfyUI-exLoadout folder.

    Install required Python dependencies:

    pip install -r requirements.txt

    Launch ComfyUI as usual (python main.py or your normal shortcut).

## Nodes Overview

![image](https://github.com/user-attachments/assets/cbafb69d-d9d8-4ebd-939a-75c9f7774ff0)

### exLoadout Selector

    Inputs:
    • excel_path: Your .xlsx file name (in custom_nodes/ComfyUI-exLoadout/)
    • sheet_name: Excel sheet/tab name

    Output: Selected Loadout name (Column A string)

    Note: Run the workflow once to populate the dropdown

### exLoadoutA & exLoadoutG

    Access up to six columns of data per row (“Part 1”: A–F, “Part 2”: G–L)

    Inputs: excel_path, sheet_name, row_number or search_string

    Outputs: String values from each column, plus a combined Outputs value formatted for parsing (e.g., %A: … %B: …)

### exLoadoutReadColumn

    Inputs: excel_path, sheet_name, column_letter (A–L)

    Output: List containing a comma‑separated string of values from that column

### exLoadoutEditCell

    Inputs: excel_path, sheet_name, row_number or search_string, column_letter (A–L), new_value

    Output: Full row returned as a confirmation string (A1…L1 format)

    Function: Updates a specified cell value in the workbook and returns the row

### exLoadout Checkpoint Loader

    Inputs: excel_path, sheet_name, selected Loadout, clip_type

    Sets model/CLIP/VAE based on Columns B/C/D (exact filenames required) from Excel; will use defaults if cells are empty

    Outputs: MODEL, CLIP, VAE + summary string

## Sample Workflow

    Use exLoadout Selector to choose your desired loadout name.

    Feed that into exLoadout Checkpoint Loader to load model, CLIP, and VAE automatically.

    Optionally use other nodes to read/write spreadsheet data or inspect additional columns.

## Notes

    Exact filenames only—make sure to include file extensions in spreadsheet cells.

    Files must reside in these folders:

        models/checkpoints/

        models/clip/

        models/vae/

    You can search for the row via Column A through search_string or by direct row number.

    The summary strings (e.g., %A: X %B: Y) allow downstream parsing by other nodes or workflows.




