# ComfyUI-GraphConstantFolder

- **Without:** *1 second "got prompt" delay*
- **With:** *0.1 second "got prompt" delay* 🤯

A server-side ComfyUI extension that rewrites the submitted prompt graph **before validation** to **constant-fold** switch/selector nodes and optionally **prune** now-unreachable branches.

This targets the common performance bottleneck in large workflows where ComfyUI’s prompt validation recursively traverses *linked upstream nodes* even when a conditional branch will not execute.

## Works best with

This extension is designed to be used in tandem with node packs that provide conditional routing:

- **Akatz-Loop-Nodes** — provides `LazySwitch`, `LazyIndexSwitch`, `LazyConditional`
	- https://github.com/akatz-ai/Akatz-Loop-Nodes
- **ComfyUI-KJNodes** — provides `LazySwitchKJ`
	- https://github.com/kijai/ComfyUI-KJNodes

It can also fold **non-lazy switch-like nodes** when their decision input resolves to a prompt-time constant.

## What it does

1. **Constant-folding:** if a switch decision is constant at prompt submission time, it rewires downstream links so consumers connect directly to the selected branch.
2. **Pruning (optional):** if `PRUNE=1`, it removes nodes that become unreachable upstream of the execution targets (output nodes or partial-execution targets).

> [!TIP]
> This extension does *not* change your workflow file on disk; it simply modifies the prompt dict sent to validation/execution.

## Folding targets

### Lazy switches
- `LazySwitch` / `LazySwitchKJ` (boolean `switch`, `on_true`, `on_false`)
- `LazyIndexSwitch` (integer `index`, `value0..valueN`)
- `LazyConditional` (`conditionN`, `valueN`, `else`)

### Switch-like nodes (non-lazy)
If a node exposes one of these exact input signatures, it is treated as a switch and can be folded when the decision is constant:

- `switch`, `on_true`, `on_false`
- `condition`, `if_true`, `if_false`
- `index` with `value0`, `value1`, ...

## Install

Copy this folder to:

```
ComfyUI/custom_nodes/ComfyUI-GraphConstantFolder
```

Restart ComfyUI. You should see:

```
[GraphConstantFolder] installed on_prompt handler (constant-fold: lazy switches + switch-like nodes)
```

## Configure

You can use either environment variables or the local config file.

### Environment variables

- `GRAPH_CONSTANT_FOLDER_ENABLED=1` (or `GCF_ENABLED=1`)
- `GRAPH_CONSTANT_FOLDER_PRUNE=1` (or `GCF_PRUNE=1`)
- `GRAPH_CONSTANT_FOLDER_DEBUG=1` (or `GCF_DEBUG=1`)
- `GRAPH_CONSTANT_FOLDER_VERBOSE=1` (or `GCF_VERBOSE=1`)

### Config file

Edit `graph_constant_folder_config.json` next to `graph_constant_folder.py`:

```json
{
	"ENABLED": 1,
	"DEBUG": 0,
	"VERBOSE": 0,
	"PRUNE": 1
}
```

Environment variables override the config.

## Extending constant resolution (safe)

By default, the extension resolves prompt-time constants through:

- literal values in the prompt JSON
- `Reroute`-like pass-through nodes
- constant/primitive/literal nodes (by class name match) **only when they have no linked inputs**

To extend the constant-source class matcher, set:

- `GRAPH_CONSTANT_FOLDER_CONST_CLASS_TYPES="(?i)(primitive|constant|literal|impact.*primitive|rgthree.*primitive)"`

This does not evaluate boolean logic (AND/OR/compare), so it remains conservative.

## Example output

```
[GraphConstantFolder] on_prompt: nodes=203, switch_candidates=23, foldable=11, prune=1, verbose=1
[GraphConstantFolder] rewrote nodes=20, pruned=105, dt_ms=4.36
Prompt executed in 0.06 seconds
```

Without the extension, the same ~200 node workflow incurs a "got prompt" delay of about 0.5 seconds.
