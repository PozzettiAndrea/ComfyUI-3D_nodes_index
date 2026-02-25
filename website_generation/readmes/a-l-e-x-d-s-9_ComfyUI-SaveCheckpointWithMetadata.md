# ComfyUI-SaveCheckpointWithMetadata

Save `.safetensors` checkpoints with custom metadata and explicit filename behavior in ComfyUI.

- Write exactly the header you want via `metadata_json`.
- Optional `prompt_override` to replace the hidden PROMPT.
- Merge mode to include hidden `EXTRA_PNGINFO`.
- Filename modes:
  - `smart_counter`: first save uses unsuffixed `prefix.safetensors` if free, next saves continue from the next free counter without going backwards.
  - `no_counter_overwrite`: always write to `prefix.safetensors` and overwrite if it exists.

## Install

### ComfyUI Manager
1) Manager -> Install via Git URL -> paste:
```
https://github.com/a-l-e-x-d-s-9/ComfyUI-SaveCheckpointWithMetadata.git
```
2) Restart ComfyUI.

If Manager shows a security level error, either install manually or add your repo to the Manager catalog. See Troubleshooting below.

### Manual
```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/a-l-e-x-d-s-9/ComfyUI-SaveCheckpointWithMetadata.git
# optional deps
python3 -m pip install -r ComfyUI-SaveCheckpointWithMetadata/requirements.txt
# optional post-install hook
python3 ComfyUI-SaveCheckpointWithMetadata/install.py || true
```
Restart ComfyUI.

## Node location
- Category: `advanced/model_merging`
- Display name: `Save Checkpoint with Metadata`

## Quick start
1) Wire your `MODEL` (and optionally `CLIP`, `VAE`, `CLIP_VISION`) into the node.
2) Choose `filename_prefix`, for example `checkpoints/MyModel`.
3) Pick `filename_mode`:
   - `smart_counter` for automatic unique names.
   - `no_counter_overwrite` to always write `prefix.safetensors`.
4) Pick `metadata_mode`:
   - `replace` to write only your `metadata_json`.
   - `merge_minimal` to start with prompt plus optional `EXTRA_PNGINFO`, then apply `metadata_json`.
5) Fill `metadata_json` with a JSON object of header keys.
6) Optionally set `prompt_override` to replace the hidden PROMPT in merge mode.
7) Queue. Your checkpoint is saved in ComfyUI output directory under the resolved subfolder.

## Inputs

| Input | Type | Description |
|------|------|-------------|
| model | MODEL | The model to serialize into a `.safetensors` checkpoint. |
| filename_prefix | STRING | Subfolder and base name under ComfyUI output directory, for example `checkpoints/MyModel`. |
| filename_mode | DROPDOWN | `smart_counter` or `no_counter_overwrite`. See Filename behavior. |
| metadata_json | STRING (multiline) | JSON object of header keys to write. Values must be strings; non-strings are JSON-encoded for you. Example: `{"author":"Alex","training":{"epochs":80}}`. |
| metadata_mode | DROPDOWN | `replace`: write only `metadata_json`. `merge_minimal`: base header includes prompt and, optionally, `EXTRA_PNGINFO`, then your `metadata_json` overwrites or adds keys. |
| include_extra_pnginfo | BOOLEAN | Used only in `merge_minimal`. When on, copy keys from hidden `EXTRA_PNGINFO` into the base header. |
| prompt_override | STRING (multiline) | Optional override for the hidden PROMPT. Ignored in `replace`. In `merge_minimal`, becomes the base `prompt` unless you also set `prompt` in `metadata_json`. |
| clip | CLIP (optional) | Embed CLIP in the checkpoint. |
| vae | VAE (optional) | Embed VAE in the checkpoint. |
| clip_vision | CLIP_VISION (optional) | Embed CLIP_VISION in the checkpoint. |

Tip: To see tooltips, enable ComfyUI Settings -> Nodes -> Enable Tooltips.

## Filename behavior

- `smart_counter`
  - If `prefix.safetensors` does not exist, write there.
  - Otherwise continue with `prefix_00001_.safetensors`, `prefix_00002_.safetensors`, etc., starting from the next free index. If ComfyUI hints a large counter, we do not go backwards; we probe from `hint+1` upward.

- `no_counter_overwrite`
  - Always write to `prefix.safetensors`. If it exists, it is overwritten.

## Examples

### Replace-only header
- metadata_mode: `replace`
- metadata_json:
```json
{"author":"author","project":"Flux-Kontext","modelspec.architecture":"sdxl"}
```
- Result: header contains exactly those keys.

### Merge prompt and extra info, then override
- metadata_mode: `merge_minimal`
- prompt_override: paste your workflow JSON or plain text
- include_extra_pnginfo: on
- metadata_json:
```json
{"prompt":"OVERRIDE","author":"Alex","training":{"epochs":80}}
```

## Notes
- Safetensors metadata requires `dict[str, str]`. Non-strings are JSON-encoded by the node.
- This node does not follow the stock `--disable-metadata` flag. It writes exactly what you specify.
- Hidden inputs `PROMPT` and `EXTRA_PNGINFO` are provided by ComfyUI runtime. The node only reads them when `merge_minimal` is selected.

## Troubleshooting

### Manager shows: This action is not allowed with this security level configuration.
- Option A: Manual install by `git clone` into `ComfyUI/custom_nodes/`.
- Option B: Lower Manager `security_level` to `middle` or `weak` in its `config.ini`, then restart ComfyUI.
- Option C: Submit your repo to the ComfyUI-Manager catalog (`custom-node-list.json`) so it can be installed at normal security. Until the PR is merged, users can use Install via Git URL or manual install.

### I see `prefix_00001_.safetensors` even on the first save
- In `smart_counter` we prefer `prefix.safetensors` if it does not exist. If you still get a numbered file, ensure the output directory exists and that no file named `prefix.safetensors` is present.

### I want modelspec.* keys like the stock node adds
- Add them to `metadata_json` explicitly. Example:
```json
{"modelspec.architecture":"sdxl","modelspec.vision":"clip"}
```

## License
No.

## Credits
Author: alexds9
Inspired by ComfyUI stock saving logic but with explicit metadata and naming control.
