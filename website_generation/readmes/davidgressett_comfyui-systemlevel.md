# CartesianCSVNode for ComfyUI

This custom node allows you to load data from one or more CSV files, then feed that data into subsequent nodes in a ComfyUI workflow. The node can:

1. **Parse up to 5 images, 10 text fields, 10 string fields, 5 integers, and 5 floats** per row.
2. **Handle multiple CSVs either via concatenation or a cartesian product** (combinatorial expansion).
3. **Preserve the native size of each image file** (no forced resizing).
4. **Increment or select rows** (with a `reset` switch and row index override).

In the case of one csv file, it's simple: load one row of data (images, strings, numbers, etc) together. Advance to the next row.
If you run a big batch of enqueues, you'll process multiple rows.

In the case of many csv files, the node can make combinations; for example you can see every example of a combination of character, background, pose (even a controlnet image), lighting info (maybe a gradient image or part of a prompt), all combined together. Define these elements in separate csv files, and the node automatically combines them for use in the workflow.

In the examples subfolder of the custom node, an example workflow "csvcartesianexample.json" is provided to demonstrate.
---

## How It Works

- Each line in the `csv_files` input is considered a **group**.
- If a single line contains multiple comma-separated CSV paths, those files are **concatenated** (they must share the same column names).
- If there are multiple lines, the node creates a **cartesian product** across those groups. This is helpful for combining poses, styles, or any other data from separate CSV files.


> **Note**: The node automatically merges column data of rows in the cartesian product. Conflicts in column names cause an error (i.e., you can't reuse the exact same column type/index in multiple spreadsheets).

---

## Installation

1. check out the repository into a folder custom_nodes/comfyui_systemlevel  
2. Restart ComfyUI.

---

## Usage in a ComfyUI Workflow

1. **Add the Node**  
   In the ComfyUI interface, search for **"CartesianCSVNode"** under **"SystemLevel/Complex Input"**.  

2. **Inputs**  
   - **`csv_files`** (multiline string):  
     - **One line** with **one CSV path** = one spreadsheet.  
     - **One line** with **multiple comma-separated CSV paths** = concatenated spreadsheet.  
     - **Multiple lines** = cartesian product across lines.
   - **`reset`** (boolean): When checked, re-start from the first row and re-parse files.
   - **`row_index`** (int): If `-1`, the node auto-increments rows each time it executes. If you set a specific integer (e.g. `3`), it will load that row and then keep incrementing from there.  
   - **`show_combined_text`** (boolean): If checked, outputs a debug string containing all combined rows.

3. **Outputs**  
   The node outputs:  
   - 5 **Images** (`Image 0` to `Image 4`)  
   - 10 **Text** fields (`Text 0` to `Text 9`) - the inputs are paths to txt files, outputs are the loaded strings. 
   - 10 **Strings** (`String 0` to `String 9`)  
   - 5 **Integers** (`Number 0` to `Number 4`)  
   - 5 **Floats** (`Float 0` to `Float 4`)  
   - **Row Count** (the total rows in the combined dataset)  
   - **Combined Rows** (a big debug string of all rows, if `show_combined_text` is True)  
   - **No More** (boolean, `True` if the next step would exceed the row count)  
   - **Last Row** (the current row index we just used)  
   - **Next Row** (the row index the node will use next)

---

## Example 1: Single Spreadsheet

Suppose you have a CSV file named `single_data.csv`:

S_0_promptA,S_1_promptB,I_0_controlimage

Hello World,This is example text,images/example01.jpg 

Prompt part A,Prompt part B,images/example02.jpg


> - **`S_0`** and **`S_1`** are string columns.  
> - **`I_0`** is the first image column.  
> - You can also have `T_0..T_9` (paths to text files, loaded for you), `N_0..N_4` (int), and `F_0..F_4` (float) columns if needed.
> - As shown, you can add your own description to each column name after another '_'

**Node Setup**:

1. In the node's `csv_files` field, simply put the path to your CSV:
C:\path\to\single_data.csv

2. **Optional**: Check `reset` if you want to start over from the first row.  Uncheck it to allow progression to the next row.
3. Connect `Image 0` to the subsequent node that expects an image, and connect `Text 0`/`Text 1` to relevant text fields in your workflow.

Each time you hit **Queue** (or run the pipeline), the node will advance to the next row:
- Row 1 => `S_0 = "Hello World"`, `S_1 = "This is example text"`, `I_0` = the loaded `images/example01.jpg`  
- Row 2 => `S_0 = "Prompt part A"`, and so on...

---

## Example 2: Multiple Spreadsheets for Variations (Cartesian Product)

Imagine you have **two** separate CSV files:

1. `poses.csv`:
S_0_pose 
poseA 
poseB 
poseC


2. `styles.csv`:
S_1_style 
styleX 
styleY


If you provide these paths on **two separate lines**, like:
C:\path\to\poses.csv 
C:\path\to\styles.csv

the node will create a cartesian product of 3×2 = 6 rows:

| S_0_pose         | S_1_style        |
|------------------|------------------|
| poseA            | styleX           |
| poseA            | styleY           |
| poseB            | styleX           |
| poseB            | styleY           |
| poseC            | styleX           |
| poseC            | styleY           |



Each CSV references different columns (like `S_0`, `S_1`, or `T_0`, etc.) so they can combine gracefully.

---

## Example 3: Concatenate CSVs on a Single Line

Suppose you have two files with **the same columns**:

C:\path\to\lightingA.csv
C:\path\to\lightingB.csv

Both might look like this, each with columns `S_0, N_0, T_0`, etc.  

If you put them **on the same line** separated by a comma:
C:\path\to\lightingA.csv, C:\path\to\lightingB.csv

the node will **concatenate** them into one larger spreadsheet. The row count is `rowsA + rowsB`. This is useful if you want to unify multiple partial CSVs that share the same columns.

---

## Example 4: Mixing Concatenation and Cartesian Product

You can combine these features:

- Line 1: `lightingA.csv, lightingB.csv` (meaning *concatenate* these two CSVs into a single set of rows)
- Line 2: `styles.csv`
- Line 3: `prompts.csv`

Now you end up with a cartesian product among the 3 lines, but each line might itself be a concatenation of multiple CSVs. That yields flexible ways to combine data:

1. **Line 1** = big spreadsheet (all lighting)
2. **Line 2** = styles
3. **Line 3** = prompts

Overall row count = (lighting A + lighting B) × styles × prompts.

---

## Column Naming

Remember that columns must follow the pattern:

- `I_0..I_4` → up to 5 images  
- `T_0..T_9` → up to 10 text file fields  
- `S_0..S_9` → up to 10 string fields  
- `N_0..N_4` → up to 5 integers  
- `F_0..F_4` → up to 5 floats  

You can add a description to a column name of your choosing with another '_', eg 'S_0_styles'

When loaded, these columns map to the outputs labeled:
- **Image 0** .. **Image 4**  
- **Text 0** .. **Text 9**  
- **String 0** .. **String 9**  
- **Number 0** .. **Number 4**  
- **Float 0** .. **Float 4**  

If columns collide across different CSVs, the node will raise an error (unless you intentionally rename them in each CSV so they don't conflict).

---

## Tips & Troubleshooting

1. **Empty CSV or Zero Rows**  
   If the final combined spreadsheet is empty (e.g., missing files or no valid data), the node returns placeholder images and zero/empty fields.

2. **`row_index`** usage  
   - By default (`-1`), each call increments the row index (wrapping around).  
   - Set to a specific integer to jump to that row.

3. **Check `show_combined_text`** if you want to see a big debug printout of all rows. This can be helpful for diagnosing unexpected merges.

4. **Large Combination**  
   Using many lines with large CSVs on each line can lead to a **huge** cartesian product. Plan accordingly.

---

## Conclusion

With `CartesianCSVNode`, you can drive complex ComfyUI workflows with CSV-based data. You can combine, concatenate, or increment across rows for any data-driven pipeline, such as generating variations of prompts, images, or numeric parameters.

Feel free to open an issue or pull request if you have questions or improvements!
