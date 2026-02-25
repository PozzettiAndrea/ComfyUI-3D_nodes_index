# ComfyUI Testing (Artify)

ComfyUI Testing is a lightweight Artify custom node pack for building and previewing XYZ parameter sweeps.

## Included nodes

- `XYZ Plot (Artify)`
  - Node id: `ArtifyXYZPlot`
  - Category: `Artify/Testing`
  - Directly lets you pick graph widget inputs for X/Y/Z axes from dropdowns on the node.
  - Queues X/Y/Z parameter sweeps and saves outputs into `output/<folder_name>` with `result.json`.
  - Existing output folders are automatically archived before each new run.
- `XYZ Viewer (Artify)`
  - Node id: `ArtifyXYZViewer`
  - Category: `Artify/Testing`
  - In-node HTML viewer with:
    - labeled X/Y matrix grid when `result.json` is available
    - simple flat image grid fallback for plain image folders

## Install

### Method 1: ComfyUI `custom_nodes` folder

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ArtifyGames/comfyui-testing.git
```

Install dependencies (if needed in future):

```bash
python -m pip install -r requirements.txt
```

Restart ComfyUI and refresh the browser page.

## Typical flow

1. Add `XYZ Plot (Artify)`.
2. Choose `input_x`, `input_y`, and optional `input_z` from the node dropdowns.
3. Set `value_x`, `value_y`, and optional `value_z`.
4. Connect `XYZ Plot (Artify)` output to `XYZ Viewer (Artify)`.
5. Run the workflow.

## Value format

- Use semicolon-separated values in each axis field.
- Example:
  - `value_x`: `6.5; 7.0; 7.5`
  - `value_y`: `20; 30; 40`
  - `value_z`: `Euler; Heun`
- `input_x` pairs with `value_x`, `input_y` pairs with `value_y`, and `input_z` pairs with `value_z`.
- If you do not want a Z axis, leave `input_z` as `none` and leave `value_z` empty.

## Output folder presets

- `output_folder_name` supports preset tokens.
- Default value:
  - `%date:yyMMdd%_X_%inputx_node_title%_%inputx_widget_name%_Y_%inputy_node_title%_%inputy_widget_name%_Z_%inputz_node_title%_%inputz_widget_name%`
- Supported tokens:
  - `%date:...%` where `...` can include `yyyy`, `yy`, `MM`, `dd`, `HH`, `mm`, `ss`
  - `%inputx_node_title%`, `%inputx_widget_name%`
  - `%inputy_node_title%`, `%inputy_widget_name%`
  - `%inputz_node_title%`, `%inputz_widget_name%`
- If Z is not used, Z tokens resolve to empty and the trailing Z suffix is automatically removed.

## Load existing folders

In `XYZ Viewer (Artify)`:

- Use `Load Folder` to pick a local folder in-browser.
- The viewer also auto-loads folders produced by connected `XYZ Plot (Artify)` runs.
- Use `Export Grid Image` to save a merged grid image with headers/legend.

If the folder contains `result.json`, the viewer renders the labeled matrix.
If not, it renders a simple image grid.

## License

See `LICENSE`.
