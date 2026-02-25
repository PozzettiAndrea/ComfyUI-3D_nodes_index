# ComfyUI Functional

Functional programming primitives for ComfyUI graphs: define functions inline, call them multiple times, and build loops, recursion, and other control-flow constructs without leaving the node editor.

> ⚠️ This extension leans on a few hacky ComfyUI internals (scheduler hooks, coroutine runners, cache invalidation). Expect sharp edges and test workflows before relying on them in production pipelines.

- English docs: [`docs/usage.md`](./docs/usage.md) · [`docs/node-reference.md`](./docs/node-reference.md)
- 中文使用说明： https://duanyll.com/2025/9/25/ComfyUI-Functional/

![Defining a function in ComfyUI](https://img.duanyll.com/img/fa65de7f.png)

## Why ComfyUI-Functional?

- **Function definitions inside graphs** – Drop `Function Parameter` and `Function End` nodes to encapsulate any node subgraph. Call it repeatedly or pass it to other nodes just like a Python closure.
- **Reusable, composable control flow** – `Map`, `Fold`, `Nest`, `Select`, and friends let you describe loops and branching logic without custom Python code. Bring your own functions as inputs.
- **Remote function calls** – Execute parts of your workflow on other ComfyUI instances (different GPUs or machines) with `Call Remote Function`. Great for pipeline parallelism and avoiding repeated model loading/unloading overhead.
- **Side-effect helpers** – `Sow`, `Reap`, `Inspect`, and `Sleep` make it possible to log data, accumulate results, and debug execution order when building complex flows.
- **Interop with other packs** – Pairs especially well with [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling); use its `LIST` values whenever you pass arrays through the functional nodes.

## Installation

1. Install [ComfyUI](https://docs.comfy.org/get_started) and (optionally) [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).
2. Search for `Duanyll/comfyui_functional` inside ComfyUI-Manager and click install.
3. Manual alternative: clone this repository into `ComfyUI/custom_nodes` and restart ComfyUI.
4. Install [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling); convert ComfyUI Data Lists to `LIST` before feeding them into these nodes.
5. Load one of the JSON files under `example_workflows/` to see the nodes in action.

> 💡 `example_workflows/functional-nested-calls.json` mirrors the blog's nested function demo and is a great starting point for understanding how functions call other functions.

## Core Concepts

### Define a function

1. Add one `Function Parameter` node per argument. Rename them so the order is obvious.
2. Build any graph using those parameters.
3. Finish the graph with a `Function End` node. Each function returns exactly one value—wrap multiple outputs into a `LIST`.

### Call a function

Connect the `Function End` output into a `Call Function` node, wire its inputs in the same order, and use the return value anywhere in your workflow. You can reuse the same function instance across multiple Call Function nodes, or even feed the function back into itself for recursion. Always guard recursion with a termination condition to avoid infinite loops.

![Calling a function multiple times](https://img.duanyll.com/img/dfc6e532.png)

### Looping and branching with high-order nodes

Use the high-order nodes under `duanyll/functional/high_order` to iterate over lists or control execution:

- `Map`/`MapIndexed` to transform lists.
- `Fold` to accumulate state across a list.
- `Nest`/`NestWhile` to repeat a function a fixed number of times or until a predicate fails.
- `Select`/`TakeWhile` to filter values.
- `Comap` to fan a single input into multiple processing branches.

See [`docs/node-reference.md`](./docs/node-reference.md) for the full signature cheat sheet.

![Mapping across a list](https://img.duanyll.com/img/1459c201.png)

### Remote function calls

Replace `Call Function` with `Call Remote Function` to execute the function body on another ComfyUI instance:

- **Pipeline parallelism** – Distribute different stages of your workflow across multiple GPUs or machines.
- **Avoid model reloading** – Keep large models loaded on dedicated workers instead of swapping them in and out on a single GPU.
- **Shared memory optimization** – When calling functions on the same machine, enable shared memory to pass tensors without serialization overhead.

> ⚠️ Remote functions require the `capture` option on `Function End` to be **disabled**. Models and other non-serializable objects cannot be captured; instead, place model loaders inside the function body. This also means ComfyUI's cache works correctly for remote calls since node IDs stay consistent.

### Side effects and debugging

- **Sow/Reap** collect intermediate results during a run. Chain the `signal` sockets to enforce ordering whenever side effects matter.
- **Inspect** reads any value in the middle of the function body without forcing the graph to evaluate eagerly. Pair with `Sleep` if the output blinks too fast in the viewer.
- Whenever side effects are detected the extension disables ComfyUI's caching to keep the results honest; expect reruns to take longer than pure functional graphs.

![Collecting values with Sow and Reap](https://img.duanyll.com/img/f60c2562.png)

## Troubleshooting Cheatsheet

- **"Prompt has no outputs"** – You either forgot to call the function or an output still depends on `Function Parameter` without being routed through `Function End`.
- **Graph freezes** – Make sure you are passing `LIST` values (from Basic Data Handling) rather than ComfyUI's built-in Data List sockets.
- **Infinite loops** – Configure `NestWhile` predicates and `max_depth` caps, or add counters into your Fold bodies.
- **Stale debug output** – Ensure something depends on the `signal` coming out of `Inspect`; otherwise it will never execute.

## Example Workflows

```
example_workflows/
├── functional-map.json            # Mapping numeric transforms across a LIST
├── functional-list-param.json     # Multiple parameter inputs + LIST handling
├── functional-nested-calls.json   # Functions calling other functions
├── functional-recursion.json      # Recursive calls with a guard
├── functional-sow-reap.json       # Collecting values with Sow/Reap + Inspect
└── functional-inspect.json        # Inspect/Sleep techniques for debugging
```

Feel free to copy these into your own projects and adapt the prompt data to match your checkpoints and samplers.

## Development

To hack on the nodes locally:

```bash
cd comfyui_functional
pip install -e .[dev]
pre-commit install
```

The editable (`-e`) install allows ComfyUI to pick up changes immediately. Run the Ruff + pytest hooks via `pre-commit run --all-files` before submitting patches.

## Tests

Pytest suites live under `tests/`. Run them with `pytest` or rely on the GitHub Actions workflows that ship with this template (`build-pipeline.yml` for lint/tests, `validate.yml` for node-diff checks).

## Publishing to the Registry

Double-check the metadata under `[tool.comfy]` in `pyproject.toml`, set up an account on https://registry.comfy.org, and configure `REGISTRY_ACCESS_TOKEN` in your repo settings before enabling the provided publish workflow. See the [official instructions](https://docs.comfy.org/registry/publishing) for the full process.
