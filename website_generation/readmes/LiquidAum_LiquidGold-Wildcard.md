# Wildcard Gold (ComfyUI)

Wildcard Gold is a ComfyUI text node that expands `<name>`-style tokens into lines from `custom_wildcards/*.txt` files, with recursive expansion, variable binding, and deterministic seeding. It is designed to work out of the box in any ComfyUI install without manual path configuration.

## Examples
Assume `ComfyUI/custom_wildcards/people.txt` contains two lines `Alice` and `Bob`, and `ComfyUI/custom_wildcards/pets/dogs.txt` contains `corgi`.

**Basic expansion**

```
Template: A portrait of <people>
Output:   A portrait of Alice
```

**Choose among files and bind a variable**

```
Template: <people|pets/dogs:1> smiles. <people|pets/dogs:1> holds a treat.
Output:   corgi smiles. corgi holds a treat.
```

**Nested expansion with missing policy**

```
Template: A <people> and <nonexistent:1> at sunset
Missing policy: empty
Output: A Bob and  at sunset
```


## Installing
- Place this repository in `ComfyUI/custom_nodes/LiquidGold-WildcardGold` (or any folder inside `custom_nodes`).
- Wildcard files live under `custom_wildcards/`:
  - `ComfyUI/custom_wildcards` (top-level)
  - Any `custom_nodes/**/custom_wildcards` directories (discovered recursively)
- Only `.txt` files are read; hidden folders and `__pycache__` are skipped.

## Node inputs/outputs
- **Category**: `text/Wildcard Gold`
- **Node name**: `🟡 Wildcard Gold`
- **Inputs**
  - `template` (`STRING`, multiline): The prompt template to expand.
  - `seed_mode` (`fixed` | `randomize`): Use the provided seed or generate a fresh one per run.
  - `seed` (`INT`): 64-bit seed used when `seed_mode` is `fixed`.
  - `max_passes` (`INT`): Maximum number of recursive passes when expanding nested tokens (default `3`).
  - `missing_policy` (`keep` | `empty` | `error`): How to handle tokens with no matching wildcard file.
- **Output**
  - `prompt` (`STRING`): Final expanded text.

## Token syntax
- `<name>` expands using `custom_wildcards/name.txt`.
- `<folder/name>` expands using a nested file, e.g., `custom_wildcards/folder/name.txt`.
- `<a|b|c>` chooses one of several wildcard files. Choices that do not exist are ignored; if none exist the missing policy applies.
- `<token:1>` (or any numeric suffix) binds the expansion for all matching tokens with the same key set and number so they stay consistent inside a single run.
- Tokens inside wildcard lines are expanded too, enabling recursive composition up to `max_passes` passes.

## Missing wildcards
- `keep`: leave the token untouched.
- `empty`: remove the token.
- `error`: raise an error that stops the node and reports which wildcard was missing.

## Seeding and determinism
- `seed_mode = fixed` uses the provided seed (masked to 64 bits) for deterministic choices.
- `seed_mode = randomize` draws a cryptographically strong random seed per run; the node is always treated as changed so ComfyUI re-executes it.

## Wildcard loading and caching
- Wildcards are resolved in order: the top-level `custom_wildcards` directory first, followed by every `custom_nodes/**/custom_wildcards` folder. Duplicate basenames are merged for convenience so `<person>` works across folders.
- The loader caches a hash of wildcard paths, mtimes, and sizes; the cache refreshes automatically when any tracked file changes.
- Each wildcard line is read as-is (UTF-8 with `errors="ignore"`) and blank lines are skipped.
