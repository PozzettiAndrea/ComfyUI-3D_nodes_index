# comfyui_gr85 – Custom Nodes for ComfyUI

This repository provides a small collection of GR85-flavoured custom nodes for ComfyUI. It includes utilities for working with image dimensions, randomization, prompt manipulation, and seed utilities.

The implementation is being migrated from the legacy `INPUT_TYPES` / `RETURN_TYPES` API to the modern `comfy_api.latest` schema-based API (`io.ComfyNode`, `define_schema`, `execute`, and `ComfyExtension`).

Currently **Simple Wildcard Picker** has been migrated fully to the new API; other nodes still use the classic style.

---

## Node overview

### Resolution helpers

- **GR85_ImageDimensionResizer**  (`ImageDimensionResizer`, category `GR85/Resolution`)
  - Computes new width/height based on a selected target resolution while preserving the original pixel count and aspect ratio.

- **GR85_ImageSizer**  (`ImageSizer`, category `GR85/Resolution`)
  - Rescales to a target aspect ratio with orientation (`original` / `landscape` / `portrait`) and snaps the result to a given tolerance (e.g. multiples of 16).

- **GR85_ImageSizerAll**  (`ImageSizerAll`, category `GR85/Resolution`)
  - Takes a pixel budget and aspect ratio components and returns new dimensions that match the pixel count and orientation, adjusted to a given tolerance.

- **GR85_RandomRatio**  (`RandomRatio`, category `GR85/Resolution`)
  - Given two width/height pairs, samples a random aspect ratio between their ratios and returns it as integer width/height components.

### Prompt helpers

- **GR85_SeedBasedOutputSelector**  (`SeedBasedOutputSelector`, category `GR85/Prompt/Selection`)
  - Selects one string from up to 10 inputs based on a seed. Only non-`None` inputs are considered, and the seed is used with modulo to choose the index.

- **GR85_SimpleWildcardPicker**  (`SimpleWildcardPicker`, category `GR85/Prompt/Wildcards`)
  - **New implementation (v3 API):**
    - Implemented as an `io.ComfyNode` using `define_schema` and `execute`.
    - Inputs:
      - `prompt` (multiline string)
      - `seed` (integer)
    - Behavior: expands `{a|b|c}`-style wildcards (with support for nested braces) using a seeded RNG so results are reproducible.

- **Tag injector nodes**  (all classic API for now, category `GR85/Prompt/Tags`)
  - **TagInjectorSingle** – injects a single tag into a template using placeholder names like `__elements__`.
  - **TagInjectorDuo** – same idea, but for two tags (e.g. `elements` and `stuff`).
  - **TagInjectorLarge** – larger template that injects multiple semantic placeholders such as `__location__`, `__weather__`, `__style__`, etc.

### Random / utility nodes

- **GR85_NextSeed**  (`NextSeed`, category `GR85/Random/Seed`)
  - Given a seed, produces a new random seed in the full 64‑bit range.

- **GR85_RandomFloat**  (`RandomFloat`, category `GR85/Random/Numbers`)
  - Generates a random float in `[min_value, max_value]`, with configurable decimal precision, seeded for reproducibility.

- **GR85_RandomInt**  (`RandomInt`, category `GR85/Random/Numbers`)
  - Generates a random integer in `[min_value, max_value]`, seeded for reproducibility.

---

## Architecture and loading

This extension supports both:

- **Legacy discovery** via `NODE_CLASS_MAPPINGS` / `NODE_DISPLAY_NAME_MAPPINGS` in `__init__.py` (for most nodes).
- **Modern discovery** via `comfy_api.latest` and a `ComfyExtension` entrypoint (for `SimpleWildcardPicker`).

The root `__init__.py` provides:

- `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS` for the classic nodes.
- `GR85Extension(ComfyExtension)` with:
  - `get_node_list()` returning the list of new `io.ComfyNode` nodes.
- `async def comfy_entrypoint()` which ComfyUI calls to load the extension.

---

## Migration guide

### 1. Simple Wildcard Picker

**What changed**

- Previously, `SimpleWildcardPicker` was a classic custom node defined with:
  - `INPUT_TYPES`
  - `RETURN_TYPES`, `RETURN_NAMES`, `FUNCTION`, `CATEGORY`
  - Registration via `NODE_CLASS_MAPPINGS["GR85_SimpleWildcardPicker"]` in `__init__.py`.
- That **legacy implementation and registration have been removed**.
- A new implementation now exists:
  - Class: `SimpleWildcardPicker(io.ComfyNode)` in `nodes/prompt/simple_wildcard_picker.py`.
  - Schema: `define_schema()` using `io.Schema`, `io.String.Input`, `io.Int.Input`, `io.String.Output`.
  - Execution: `execute()` returns an `io.NodeOutput`.
  - Registration: via `GR85Extension.get_node_list()` and `comfy_entrypoint()`.
  - Node ID: still `GR85_SimpleWildcardPicker` (no `v3` suffix), display name `"Simple Wildcard Picker"`.

**Behavior compatibility**

- The wildcard expansion logic has been preserved:
  - Same `{a|b|c}` syntax.
  - Nested braces are supported.
  - A seeded RNG (`Random(seed)`) is used for reproducible choices.
- The internals were refactored into a helper function (`_process_wildcards`) used by the new `execute()` method.

**Impact on existing workflows**

- Graphs that reference node ID `GR85_SimpleWildcardPicker` should continue to work, but they now use the new schema-based node.
- Code or tooling that relied on:
  - `NODE_CLASS_MAPPINGS["GR85_SimpleWildcardPicker"]`, or
  - the legacy `INPUT_TYPES`/`FUNCTION` shape of `SimpleWildcardPicker`

  will need to be updated to work with the new `io.ComfyNode` API and extension-based discovery.

**How to update custom integrations**

- Instead of importing and introspecting the legacy class, treat it as a standard `io.ComfyNode`:
  - Use its schema via `SimpleWildcardPicker.define_schema()`.
  - Expect `execute(prompt, seed)` to be a classmethod returning `io.NodeOutput`.
- Do **not** rely on `NODE_CLASS_MAPPINGS` for this node anymore; it is no longer present there.

### 2. Other nodes (classic API)

- All other GR85 nodes still use the classic:
  - `INPUT_TYPES`
  - `RETURN_TYPES` / `RETURN_NAMES`
  - `FUNCTION` / instance methods
  - `NODE_CLASS_MAPPINGS` / `NODE_DISPLAY_NAME_MAPPINGS`
- They will continue to behave as before.

**Planned direction**

- Over time, these nodes can be migrated in the same style as `SimpleWildcardPicker`:
  - Introduce an `io.ComfyNode` implementation with `define_schema` + `execute`.
  - Register it via `GR85Extension.get_node_list()`.
  - Optionally remove the old mapping entry once you are comfortable with the migration.

If you want to migrate another specific node (e.g. `GR85_SeedBasedOutputSelector` or one of the latent utilities), follow the same pattern as `SimpleWildcardPicker` and update the extension’s `get_node_list()` accordingly.
