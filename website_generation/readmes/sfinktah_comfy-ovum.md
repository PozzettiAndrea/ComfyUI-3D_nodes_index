# Ovum

Some custom nodes for Comfy that I just couldn't live without.  Some have come
from other packages that were annoyingly hard to find, some have been improved
from other peoples' work who don't accept PR requests, some have been made
by me, and one has been made entirely by AI (but basically had to be rewritten
afterwards).

## Twin Connectors: SetTwinNodes and GetTwinNodes

![Twin Connectors: Set/Get screenshot](resources/set_dual_nodes.png)

A pair of graph-cleaning utility nodes designed to “tunnel” connections and reduce visual clutter without sacrificing clarity or type-safety.

Effortless to type one-handed: enter SETTW or GETTW to locate these nodes fast—so your right hand can stay on the mouse (because where else would your right hand be?)

All the functionality of Kijai's Set/Get nodes, easier to use than easyUse SetNodes, twice as many connections, and unbelievably more automated.

- SetTwinNodes accepts an arbitrary number (two... more coming soon) of inputs and exposes matching outputs, letting you collect and forward values by meaningful constant names rather than raw wires.
- GetTwinNodes presents matching outputs, selected via lightweight “constant” widgets. You pick the names you care about; the node provides outputs of the corresponding types.

What makes them useful:
- They work in subgraphs!
- ~Clean labels over raw types: when a link is attached, constants and slots can inherit human-friendly labels from the connected endpoints; titles are built from the chosen constants.~
- ~Provisional naming: when a Get node learns a name from a downstream connection that does not yet exist on any Set, it marks the constant with an asterisk to signal “choose a valid source later.” When the matching Set appears, the names reconcile automatically.~
- Works in either order: you can drop a Get first and wire it to a consumer; later, when a Set of the right type appears, the system can adopt the better name and update labels across the link.
- Sensible colorization: nodes can colorize based on the first two connected, typed slots to give fast visual feedback while keeping the graph readable.
- Serialization-safe: saved widget values and output types are respected on load; no surprise re-labelling. (Mostly)
- ~Ergonomic pairing: when you pick one constant and the system recognizes an associated partner, it can suggest or create the companion slot automatically; if it can’t, it still creates a second empty selector so you can complete the pair manually.~
- Tunneling without surprises: instant graphic feedback warns of setters with no getters.

How to use:
1. Drop a SetTwinNodes near your sources and connect any values you want to “publish.” Give each constant a clear name (e.g., width, height, start_image). The node mirrors types to its outputs and propagates names to matching Gets.
2. Drop a GetTwinNodes near your consumers and pick the same constant names to “subscribe.” If you connect the Get to a consumer before a matching Set exists, it will note your intent and reconcile once a suitable Set appears.
3. Rename safely: titles and labels follow your constants (sometimes); if a label equals its raw type (a “lame name”), later Set connections can adopt a better name from a compatible Get to keep the graph readable.
4. Toggle “Show connections” from the node menu to visualize virtual links between Sets and Gets without adding extra wires.

These nodes are meant to keep large graphs navigable while preserving intent through names, not just types. They are deliberately forgiving when you work top-down or bottom-up, and they do their best to stay out of your way once you’ve chosen the labels that make sense in your workflow.

## Python String Format

Turn multiple inputs into a single, neatly formatted string using Python’s `str.format` syntax. This node is ideal for building prompts, captions, file names, or any text that needs values injected at runtime.

What it does:
- Accepts a format template (fmt) and inserts values into placeholders like `{arg0}`, `{arg1}`, etc.
- Produces a single STRING output.
- Uses Python’s standard formatting rules, so you get powerful control over numbers, padding, alignment, and more.

Placeholders:
- Use `{arg0}` for the first input, `{arg1}` for the second, and so on.
- You can apply format specs: `{arg0:.2f}`, `{arg1:03d}`, `{arg2:^20}`, `{arg3!r}`.
- To show a literal curly brace, escape it: `{{` or `}}`.

New lines:
- Press Enter in the fmt field to insert real line breaks; the output will contain those line breaks exactly.
- You can also embed newline escapes: use `\n` for a single new line, or `\n\n` to insert a blank line.
- Mix placeholders and text across lines to build readable multi-line prompts or file names.

Examples:
- Multiline prompt with escape sequences:
  - fmt: `Positive: {arg0}\nNegative: {arg1}\nSteps: {arg2}`
  - Inputs: arg0 = "cozy cabin", arg1 = "low quality, blurry", arg2 = 30
  - Output:
        Positive: cozy cabin
        Negative: low quality, blurry
        Steps: 30
- Multiline using literal line breaks:
  - fmt:
        Title: {arg0}

        {arg1}
        Tags: {arg2}, {arg3}
  - Inputs: arg0 = "Autumn Forest", arg1 = "golden hour, volumetric light", arg2 = "forest", arg3 = "sunset"
  - Output:
        Title: Autumn Forest

        golden hour, volumetric light
        Tags: forest, sunset

Common recipes:
- Basic substitution:
  - fmt: `Prompt: {arg0}. Steps: {arg1}`
  - Inputs: arg0 = "A cozy cabin at night", arg1 = 30
  - Output: `Prompt: A cozy cabin at night. Steps: 30`
- Float precision:
  - fmt: `Score: {arg0:.2f}`
  - Inputs: arg0 = 0.98765
  - Output: `Score: 0.99`
- Zero-padded integers:
  - fmt: `Image_{arg0:04d}`
  - Inputs: arg0 = 7
  - Output: `Image_0007`
- Alignment and width:
  - fmt: `[{arg0:^10}]`
  - Inputs: arg0 = "OK"
  - Output: `[    OK    ]`
- Literal braces:
  - fmt: `Config: {{enabled: {arg0}}}`
  - Inputs: arg0 = true
  - Output: `Config: {enabled: true}`

Tips:
- Missing or empty inputs are gracefully replaced with the literal string "None" at format time, so your workflow keeps running even if something disconnects or a generator yields no value. This is a dramatic improvement over other formatting nodes that can kill your workflow right when it’s about to finish saving that super‑long video.
- Another bonus: non‑scalar inputs (lists, dictionaries, tuples, and custom objects) are kept as real Python objects rather than being flattened to JSON. That means you can index or key into them right in the format string.
- Robust error handling: if formatting fails (e.g., invalid format spec, out-of-range index, missing key/attribute), the node prints the error to the console and returns the error text as the output string instead of crashing your run.
- Numbers respect format specs; use them to avoid manual rounding or string tricks.
- If you need default values, provide them upstream (e.g., via a constant/text node) and wire them in.

Structured data (lists, dicts, tuples):
- Lists:
  - fmt: `Top tags: {arg0[0]}, {arg0[1]}, count={arg0[2]:02d}`
  - Inputs: arg0 = ["hdr", "sunset", 7]
  - Output: `Top tags: hdr, sunset, count=07`
- Dictionaries:
  - fmt: `User: {arg0[name]} (id={arg0[id]})`
  - Inputs: arg0 = {"name": "Riley", "id": 42}
  - Output: `User: Riley (id=42)`
- Tuples (or list-like sizes):
  - fmt: `Size: {arg0[0]}x{arg0[1]}`
  - Inputs: arg0 = (1024, 576)
  - Output: `Size: 1024x576`
- You can combine indexing with format specs:
  - fmt: `Mean: {arg0[1]:.2f}`
  - Inputs: arg0 = ["loss", 0.123456]
  - Output: `Mean: 0.12`

Use cases:
- Build dynamic prompts from multiple upstream nodes.
- Compose file names with counters, dates, or padded indices.
- Generate human-readable summaries that include numeric metrics.

## Timer

How long does the workflow spend in each node?

Somewhat rough around the edges with a number of confusing buttons and inputs (thankfully you can ignore them all), but a useful tool for timing and debugging.

![Timer: screenshot](resources/timer.png)

## Live Crop (interactive)

Visually crop, expand, and rotate an image with interactive guides rendered directly in the node.

- Inputs:
  - crop_top, crop_bottom, crop_left, crop_right (FLOAT [-1..1]):
    - Negative: crops that fraction of the original dimension from that side (e.g., -0.1 removes 10% from that edge).
  - image (IMAGE, optional), mask (MASK, optional): both are processed with the same operations; masks use white=255 for padding.
- Outputs: IMAGE, MASK
- UI: The node shows a preview of the incoming image(s) with red lines indicating where the crop will occur. Adjust the sliders or drag the guides (think: Photoshop rulers) to update.

Notes:
- When no image is connected, the node returns None; when connected, the preview is downscaled for responsiveness.
- Multiple images/batches supported, allowing you crop as you go: adjust the cropping for the second image, which will be the first image by the time the next workflow executes.

## Environment Bridge: Set Environment Variable and Get Environment Variable

### Browser Local Storage: Set LocalStorage and Get LocalStorage

Persist small strings in the browser between sessions without touching the server environment.

- Set LocalStorage: Writes a key/value into the browser's localStorage (strings only). Includes an optional passthrough to help enforce execution order. If overwrite=false and the key exists in localStorage, the value is left unchanged.
- Get LocalStorage: Reads a key from the browser's localStorage with a default fallback. Returns (value, exists).

Notes:
- Backend nodes cannot directly access the browser; the Set node triggers a frontend action to store the value using ComfyUI's UI-return channel. The Get node returns the provided default at execution time but is useful for coordinating UI state; use environment variables if you need true backend-readable values.
- Keys and values are stored as strings. If you need structures, encode/decode to JSON in the graph.

Publish and subscribe values anywhere in your workflow (and even across workflows) using the process environment as a lightweight, global message bus.

What they do:
- “Set Environment Variable” writes key/value pairs to the process environment. You can optionally thread a passthrough input/output to enforce execution order without altering data flow.
- “Get Environment Variable” reads a key from the environment with a fallback default. It is change-aware and will re-evaluate when the targeted variable changes.
- Together they enable out‑of‑band data routing without extra wires, allowing one‑to‑many fan‑out, late binding, and cross‑graph coordination.

Why it’s special:
- Global scope within the process: values are visible to all workflows running in the same Comfy session.
- “Virtual wires” without clutter: connect distant parts of a large graph through names, not links.
- Change detection: readers can refresh only when a variable’s value or existence actually changes, keeping runs fast and deterministic.
- Execution ordering: use the passthrough to place setting/getting in precise positions of your pipeline without affecting the payload being processed.

Patterns you can build:
- Publish/Subscribe hub:
  - Upstream nodes “publish” dimensions, models, seeds, or file paths with “Set Environment Variable.”
  - Downstream consumers “subscribe” with “Get Environment Variable” wherever they need the same value.
- Cross‑workflow handoff (inter‑workflow):
  - Use a stable variable name (e.g., PROJECT_PREFIX, ACTIVE_CHECKPOINT) so separate workflows launched in the same session share configuration.
- Pseudo‑feedback loops (intra‑workflow):
  - Emulate feedback by writing a value early and reading it later in the same run to condition subsequent steps, without creating illegal graph cycles.
- State and toggles:
  - Flip feature flags (e.g., USE_HIRES_FIX=true) to drive conditional branches or tool selection across multiple, otherwise unconnected nodes.
- Secrets and tokens:
  - Inject API keys, model licenses, or service endpoints at runtime; consumers read them on demand.
- One‑to‑many routing:
  - Publish once, consume everywhere—useful for common output directories, date stamps, or version tags.

Common recipes:
- Share a counter between runs:
  - Read COUNT with “Get Environment Variable” (default 0) → increment in your logic → write back with “Set Environment Variable” for the next run.
- Centralize paths:
  - Use “Set Environment Variable” with name=OUTPUT_DIR, value=/data/renders → multiple savers read OUTPUT_DIR to stay in sync.
- Switch models/tools globally:
  - Use “Set Environment Variable” with name=ACTIVE_MODEL, value=SDXL → routers or conditionals pick the right branch downstream.

Tips and caveats:
- Scope: values live only for the current process and its children; they do not persist after a restart.
- Collisions: environment space is shared; pick distinctive names or prefixes (e.g., OVUM_) to avoid clashes.
- Security: avoid printing secrets; prefer generic names and keep sensitive values out of saved screenshots or public logs.
- Consistency: environment variables are strings; encode complex data (e.g., JSON) explicitly if needed and decode where you read it.
- Ordering: use the passthrough to ensure “set before get” along your execution path; visual proximity doesn’t influence execution—connections do.

In short, “Set Environment Variable” and “Get Environment Variable” act like SetNode/GetNode with super powers: they can tunnel values across the graph, coordinate multiple consumers, and enable inter‑ and intra‑workflow value transfer—while staying simple, explicit, and robust.

## Halt Toggle Node

The **Halt Toggle** node is a versatile control node designed to bring simplified workflow execution halts to your projects.

### Key Features:
- **Flexible Halting:** Easily pause workflow execution when the `stop_now` condition is met.
- **Auto-Reset Capability:** The node can automatically reset itself after halting, allowing seamless continuation of the workflow in subsequent runs without manual intervention.
- **Delay Support:** Introduce a configurable delay (in milliseconds) before halting the workflow.
- **Passthrough Convenience:** The node forwards inputs, keeping graph wiring intuitive and maintaining data flow consistency when used as part of a larger workflow.
- **Detailed Feedback:** Provides outputs to indicate whether a stop was applied and if an auto-reset was triggered.

### How It Works:
When the `stop_now` input is set to true, the **Halt Toggle** node halts the workflow execution. However, if the **reset_after_stop** option is enabled, the halt will auto-disable for the next run, ensuring the workflow proceeds smoothly without requiring manual toggle adjustments.

### Use Case Example:
If you have a workflow that requires pausing at specific stages or debugging steps, the Halt Toggle node provides an elegant solution to stop execution conditionally and resume it dynamically in subsequent runs.

Enhance your workflow control with the Halt Toggle node, empowering you to build more robust and interactive systems effortlessly.

## Pystructure Data Nodes (complementary to ComfyUI-LogicUtils)

These nodes are complementary to the excellent collection at https://github.com/aria1th/ComfyUI-LogicUtils. They focus on list manipulation and small data utilities that pair well with logic/structure nodes from that set.

- List Slice
  - What it does: Returns a slice of an input list using JavaScript-like slice semantics.
  - Inputs:
    - py_list (LIST): The source list.
    - start (INT): Start index. Negative values count from the end. Clamped to bounds; default 0 if empty.
    - end (INT): End index (non-inclusive). Negative values count from the end. Clamped to bounds; defaults to list length if empty.
  - Output:
    - LIST: A new list containing the requested slice. If start >= end after normalization, returns an empty list.
  - Notes: Behavior mirrors JS slice for negative indices and boundary clamping; does not mutate the input list.

- List Splice
  - What it does: Splices into a list using JavaScript-like splice semantics: remove delete_count items starting at start and insert items from insert_list.
  - Inputs:
    - py_list (LIST): The target list (will be modified in place).
    - start (INT): Start index. Negative values count from the end. Clamped to valid positions.
    - delete_count (INT): Number of items to remove (clamped to remaining length; negatives treated as 0).
    - insert_list (LIST): Items to insert at the splice position (can be empty to perform pure deletion).
  - Outputs:
    - LIST (modified_list): The same list instance after splicing.
    - LIST (removed_elements): A list of the elements that were removed.
  - Notes: Mirrors JS semantics for start and delete_count; performs in-place mutation of py_list.

- Repeat Item
  - What it does: Produces a list containing the given item repeated count times.
  - Inputs:
    - item (any): Any value to repeat.
    - count (INT): Number of repetitions. Minimum 0; negatives are treated as 0.
  - Output:
    - LIST: [item, item, ..., item] repeated count times.
  - Notes: Non-mutating; useful for building lists of constants, seeds, file paths, or objects for batch operations.

- Reverse List
  - What it does: Returns a new list in reverse order.
  - Inputs:
    - py_list (LIST): The source list.
  - Output:
    - LIST: A new list with elements reversed.
  - Notes: Non-mutating; the input list is not modified.

- List Concat
  - What it does: Concatenates two lists similar to JS Array.concat.
  - Inputs:
    - list_a (LIST): First list.
    - list_b (LIST): Second list (optional; blank treated as empty).
  - Output:
    - LIST: New list of elements of list_a followed by elements of list_b.
  - Notes: Non-mutating.

- List IndexOf
  - What it does: Finds the first index of a value in a list like JS indexOf.
  - Inputs:
    - py_list (LIST): The list to search.
    - search_element (any): Value to find.
    - start (INT): Optional fromIndex; negative values count from end; blank -> 0.
  - Output:
    - INT: Index of the match; -1 if not found.

- List Join
  - What it does: Joins elements into a string like JS join.
  - Inputs:
    - py_list (LIST): Elements to join.
    - separator (STRING): Optional separator; blank/unspecified -> comma, empty string -> no separator.
  - Output:
    - STRING: Joined string.

- XRange
  - What it does: Python-like xrange/range iterator without generators. Outputs current value, full list, and a boolean flag for exhausted/looped.
  - Inputs:
    - stop (INT): End (exclusive). Required.
    - start (INT): Optional start; blank -> 0.
    - step (INT): Optional step; blank -> 1; cannot be 0; can be negative.
    - repeat (BOOLEAN): If true, wraps to the start (or end for negative step) when reaching the end; the flag output is true on the wrap iteration.
    - cursor (INT): Current index into the range; you can set/reset this manually to control which value is output.
    - advance (BOOLEAN): If true (default), increases cursor by 1 each evaluation so you can tick through values using Repeat/Trigger.
  - Outputs:
    - INT: current value at the cursor.
    - LIST: the full expanded list of values (range(start, stop, step)).
    - BOOLEAN: exhausted_or_looped — true when the range is exhausted (with repeat disabled) or when it loops (with repeat enabled).
  - Notes:
    - Negative steps are supported exactly like Python range. If the computed range is empty, the list is empty and the flag is true; current value returns 0.

## Open Output via Shell (secure)

When your video has finished generating, have VLC (or your default media player) open it automatically.

## Text Ovary (overlay text on images)

Text Ovary is a polished, in-house merge of the excellent TextOverlay node (sfinktah/comfyui-textoverlay) adapted for Ovum.

Why you’ll like it:
- Super simple: plug in an IMAGE and a STRING, pick a font, done.
- Looks great: fill + stroke with independent opacity to keep captions readable over any background.
- Precise placement: left/center/right, top/middle/bottom, with padding and x/y nudges.
- Multiline aware: sensible line spacing and alignment across lines.
- Batch-friendly: renders the same text across a whole batch efficiently.

Inputs:
- image (IMAGE)
- text (STRING, multiline)
- font_size (INT)
- font (choice from bundled fonts)
- fill_color_hex (STRING, e.g. #ffffff)
- stroke_color_hex (STRING)
- stroke_thickness (FLOAT, relative to font size)
- padding (INT)
- horizontal_alignment (left|center|right)
- vertical_alignment (top|middle|bottom)
- x_shift, y_shift (INT)
- line_spacing (FLOAT)
- stroke_opacity (FLOAT)

Output:
- IMAGE with the text composited

Tip: Pair with Python String Format to build captions dynamically from metadata or prompts.

Safely open your rendered media with the system’s default app—no fragile shell strings, no workflow‑stopping errors.

Why you’ll like it:
- Validates the path exists and is a regular file before trying to open it.
- Accepts only image/video types (via MIME detection) to avoid launching arbitrary files.
- Uses platform‑appropriate launchers:
  - Windows: start " <file> (handles spaces and the window‑title quirk).
  - macOS: open <file>
  - Linux: xdg-open <file>
- Secure by design: runs without a shell so spaces/quotes can’t break or inject commands.
- Non‑fatal: any failure returns an “[ERROR] …” string; your workflow keeps going.

Inputs:
- input (any, optional passthrough): helps enforce execution order; doesn’t alter your data.
- filename (STRING): full path to the image or video you want to open.

Output:
- STRING: a success message or an “[ERROR] …” detail you can log, display, or ignore.

Tips:
- Wire filename from your saver node to auto‑open the latest result.
- Works well with format/concat nodes to build paths dynamically.
- On headless systems, the open command may be unavailable; you’ll get a clear error message instead of a crash.

## Regex Nodes (ovum/regex)

A compact suite of regex utilities that mirror Python’s re API while being graph-friendly. They accept plain strings or lists and return structured results without crashing your run when there are no matches.

Highlights:
- Builders and matchers: re.compile flags, search, match, fullmatch, findall, finditer, split, sub, subn
- Match inspectors: view, span/start/end, group/groups/groupdict, select index, expand templates
- Escape helper: re.escape for safe literal matching

These nodes keep outputs list-aware to make it easy to fan out results downstream.

## CUDNN Toggle Ovum

Temporarily flip torch.backends.cudnn.enabled (and benchmark) on/off around a section of your graph. Useful for cases where disabling cuDNN speeds up certain ops (e.g., VAE Encode/Decode under ZLUDA). Returns the previous state so you can restore it later.

## Image List Loader + Folder Paths

Load a batch of images from a folder or an explicit list with optional regex/custom filtering, recursion, and sorting. Outputs images, masks, normalized file paths, callback payloads, embedded prompt/workflow info, and an ‘exhausted’ flag.
- Folder Paths: utility to retrieve common ComfyUI directories as normalized strings for wiring into other nodes.

## BigKnob (Widget)

A simple numeric knob with min/max clamping and precision rounding. Great as a human-friendly dial to drive parameters.

## LM Studio Prompt (Ovum/LLM)

Connect to an LM Studio server to generate text (optionally with an image for vision models). Supports prompt modes, wildcard expansion, dynamic model discovery, and optional auto-unload after inactivity.

## Workflow Helpers (Widgets to values)

- Widget To String (KJNodes): Read a widget from any node in your workflow and return its value as STRING (with smart float formatting).
- Workflow Widget To Any: Same idea, but returns the native type from a PROMPT&WORKFLOW input.
- Sync Sink (KJNodes): A no-op sink that forces upstream branches to complete before proceeding; handy for synchronizing flows.

## VHS Helper: Next Video Filename

Predict the next auto-numbered output base path that VHS VideoCombine will use (without writing files), so you can plan downstream file operations deterministically.

## Wildcard Processor (Escapable)

Powerful prompt preprocessor that supports wildcard files, date stamping, simple random ranges, and safe comment/markup stripping. Designed to play nicely with other Ovum text utilities.

## Does Kijai SetNode exist?

Checks your current workflow to see if a Kijai SetNode exists for a given Constant and is actually wired at input 0. Useful for conditionally enabling branches tied to KJNodes Set/Get patterns.

## Folder, Range, and Sequence Utilities

- XRange: A range-like tick node that outputs current value, full list, and an overflow/loop flag with optional repeat and reset behavior. Useful for counters and iteration control.


# Ovum

Some custom nodes for Comfy that I just couldn't live without.  Some have come
from other packages that were annoyingly hard to find, some have been improved
from other peoples' work who don't accept PR requests, some have been made
by me, and one has been made entirely by AI (but basically had to be rewritten
afterwards).

## Twin Connectors: SetTwinNodes and GetTwinNodes

![Twin Connectors: Set/Get screenshot](resources/set_dual_nodes.png)

A pair of graph-cleaning utility nodes designed to “tunnel” connections and reduce visual clutter without sacrificing clarity or type-safety.

Effortless to type one-handed: enter SETTW or GETTW to locate these nodes fast—so your right hand can stay on the mouse (because where else would your right hand be?)

All the functionality of Kijai's Set/Get nodes, easier to use than easyUse SetNodes, twice as many connections, and unbelievably more automated.

- SetTwinNodes accepts an arbitrary number (two... more coming soon) of inputs and exposes matching outputs, letting you collect and forward values by meaningful constant names rather than raw wires.
- GetTwinNodes presents matching outputs, selected via lightweight “constant” widgets. You pick the names you care about; the node provides outputs of the corresponding types.

What makes them useful:
- They work in subgraphs!
- ~Clean labels over raw types: when a link is attached, constants and slots can inherit human-friendly labels from the connected endpoints; titles are built from the chosen constants.~
- ~Provisional naming: when a Get node learns a name from a downstream connection that does not yet exist on any Set, it marks the constant with an asterisk to signal “choose a valid source later.” When the matching Set appears, the names reconcile automatically.~
- Works in either order: you can drop a Get first and wire it to a consumer; later, when a Set of the right type appears, the system can adopt the better name and update labels across the link.
- Sensible colorization: nodes can colorize based on the first two connected, typed slots to give fast visual feedback while keeping the graph readable.
- Serialization-safe: saved widget values and output types are respected on load; no surprise re-labelling. (Mostly)
- ~Ergonomic pairing: when you pick one constant and the system recognizes an associated partner, it can suggest or create the companion slot automatically; if it can’t, it still creates a second empty selector so you can complete the pair manually.~
- Tunneling without surprises: instant graphic feedback warns of setters with no getters.

How to use:
1. Drop a SetTwinNodes near your sources and connect any values you want to “publish.” Give each constant a clear name (e.g., width, height, start_image). The node mirrors types to its outputs and propagates names to matching Gets.
2. Drop a GetTwinNodes near your consumers and pick the same constant names to “subscribe.” If you connect the Get to a consumer before a matching Set exists, it will note your intent and reconcile once a suitable Set appears.
3. Rename safely: titles and labels follow your constants (sometimes); if a label equals its raw type (a “lame name”), later Set connections can adopt a better name from a compatible Get to keep the graph readable.
4. Toggle “Show connections” from the node menu to visualize virtual links between Sets and Gets without adding extra wires.

These nodes are meant to keep large graphs navigable while preserving intent through names, not just types. They are deliberately forgiving when you work top-down or bottom-up, and they do their best to stay out of your way once you’ve chosen the labels that make sense in your workflow.

## Python String Format

Turn multiple inputs into a single, neatly formatted string using Python’s `str.format` syntax. This node is ideal for building prompts, captions, file names, or any text that needs values injected at runtime.

What it does:
- Accepts a format template (fmt) and inserts values into placeholders like `{arg0}`, `{arg1}`, etc.
- Produces a single STRING output.
- Uses Python’s standard formatting rules, so you get powerful control over numbers, padding, alignment, and more.

Placeholders:
- Use `{arg0}` for the first input, `{arg1}` for the second, and so on.
- You can apply format specs: `{arg0:.2f}`, `{arg1:03d}`, `{arg2:^20}`, `{arg3!r}`.
- To show a literal curly brace, escape it: `{{` or `}}`.

New lines:
- Press Enter in the fmt field to insert real line breaks; the output will contain those line breaks exactly.
- You can also embed newline escapes: use `\n` for a single new line, or `\n\n` to insert a blank line.
- Mix placeholders and text across lines to build readable multi-line prompts or file names.

Examples:
- Multiline prompt with escape sequences:
  - fmt: `Positive: {arg0}\nNegative: {arg1}\nSteps: {arg2}`
  - Inputs: arg0 = "cozy cabin", arg1 = "low quality, blurry", arg2 = 30
  - Output:
        Positive: cozy cabin
        Negative: low quality, blurry
        Steps: 30
- Multiline using literal line breaks:
  - fmt:
        Title: {arg0}

        {arg1}
        Tags: {arg2}, {arg3}
  - Inputs: arg0 = "Autumn Forest", arg1 = "golden hour, volumetric light", arg2 = "forest", arg3 = "sunset"
  - Output:
        Title: Autumn Forest

        golden hour, volumetric light
        Tags: forest, sunset

Common recipes:
- Basic substitution:
  - fmt: `Prompt: {arg0}. Steps: {arg1}`
  - Inputs: arg0 = "A cozy cabin at night", arg1 = 30
  - Output: `Prompt: A cozy cabin at night. Steps: 30`
- Float precision:
  - fmt: `Score: {arg0:.2f}`
  - Inputs: arg0 = 0.98765
  - Output: `Score: 0.99`
- Zero-padded integers:
  - fmt: `Image_{arg0:04d}`
  - Inputs: arg0 = 7
  - Output: `Image_0007`
- Alignment and width:
  - fmt: `[{arg0:^10}]`
  - Inputs: arg0 = "OK"
  - Output: `[    OK    ]`
- Literal braces:
  - fmt: `Config: {{enabled: {arg0}}}`
  - Inputs: arg0 = true
  - Output: `Config: {enabled: true}`

Tips:
- Missing or empty inputs are gracefully replaced with the literal string "None" at format time, so your workflow keeps running even if something disconnects or a generator yields no value. This is a dramatic improvement over other formatting nodes that can kill your workflow right when it’s about to finish saving that super‑long video.
- Another bonus: non‑scalar inputs (lists, dictionaries, tuples, and custom objects) are kept as real Python objects rather than being flattened to JSON. That means you can index or key into them right in the format string.
- Robust error handling: if formatting fails (e.g., invalid format spec, out-of-range index, missing key/attribute), the node prints the error to the console and returns the error text as the output string instead of crashing your run.
- Numbers respect format specs; use them to avoid manual rounding or string tricks.
- If you need default values, provide them upstream (e.g., via a constant/text node) and wire them in.

Structured data (lists, dicts, tuples):
- Lists:
  - fmt: `Top tags: {arg0[0]}, {arg0[1]}, count={arg0[2]:02d}`
  - Inputs: arg0 = ["hdr", "sunset", 7]
  - Output: `Top tags: hdr, sunset, count=07`
- Dictionaries:
  - fmt: `User: {arg0[name]} (id={arg0[id]})`
  - Inputs: arg0 = {"name": "Riley", "id": 42}
  - Output: `User: Riley (id=42)`
- Tuples (or list-like sizes):
  - fmt: `Size: {arg0[0]}x{arg0[1]}`
  - Inputs: arg0 = (1024, 576)
  - Output: `Size: 1024x576`
- You can combine indexing with format specs:
  - fmt: `Mean: {arg0[1]:.2f}`
  - Inputs: arg0 = ["loss", 0.123456]
  - Output: `Mean: 0.12`

Use cases:
- Build dynamic prompts from multiple upstream nodes.
- Compose file names with counters, dates, or padded indices.
- Generate human-readable summaries that include numeric metrics.

## Timer

How long does the workflow spend in each node?

Somewhat rough around the edges with a number of confusing buttons and inputs (thankfully you can ignore them all), but a useful tool for timing and debugging.

![Timer: screenshot](resources/timer.png)

## Live Crop (interactive)

Visually crop, expand, and rotate an image with interactive guides rendered directly in the node.

- Inputs:
  - crop_top, crop_bottom, crop_left, crop_right (FLOAT [-1..1]):
    - Negative: crops that fraction of the original dimension from that side (e.g., -0.1 removes 10% from that edge).
  - image (IMAGE, optional), mask (MASK, optional): both are processed with the same operations; masks use white=255 for padding.
- Outputs: IMAGE, MASK
- UI: The node shows a preview of the incoming image(s) with red lines indicating where the crop will occur. Adjust the sliders or drag the guides (think: Photoshop rulers) to update.

Notes:
- When no image is connected, the node returns None; when connected, the preview is downscaled for responsiveness.
- Multiple images/batches supported, allowing you crop as you go: adjust the cropping for the second image, which will be the first image by the time the next workflow executes.

## Environment Bridge: Set Environment Variable and Get Environment Variable

### Browser Local Storage: Set LocalStorage and Get LocalStorage

Persist small strings in the browser between sessions without touching the server environment.

- Set LocalStorage: Writes a key/value into the browser's localStorage (strings only). Includes an optional passthrough to help enforce execution order. If overwrite=false and the key exists in localStorage, the value is left unchanged.
- Get LocalStorage: Reads a key from the browser's localStorage with a default fallback. Returns (value, exists).

Notes:
- Backend nodes cannot directly access the browser; the Set node triggers a frontend action to store the value using ComfyUI's UI-return channel. The Get node returns the provided default at execution time but is useful for coordinating UI state; use environment variables if you need true backend-readable values.
- Keys and values are stored as strings. If you need structures, encode/decode to JSON in the graph.

Publish and subscribe values anywhere in your workflow (and even across workflows) using the process environment as a lightweight, global message bus.

What they do:
- “Set Environment Variable” writes key/value pairs to the process environment. You can optionally thread a passthrough input/output to enforce execution order without altering data flow.
- “Get Environment Variable” reads a key from the environment with a fallback default. It is change-aware and will re-evaluate when the targeted variable changes.
- Together they enable out‑of‑band data routing without extra wires, allowing one‑to‑many fan‑out, late binding, and cross‑graph coordination.

Why it’s special:
- Global scope within the process: values are visible to all workflows running in the same Comfy session.
- “Virtual wires” without clutter: connect distant parts of a large graph through names, not links.
- Change detection: readers can refresh only when a variable’s value or existence actually changes, keeping runs fast and deterministic.
- Execution ordering: use the passthrough to place setting/getting in precise positions of your pipeline without affecting the payload being processed.

Patterns you can build:
- Publish/Subscribe hub:
  - Upstream nodes “publish” dimensions, models, seeds, or file paths with “Set Environment Variable.”
  - Downstream consumers “subscribe” with “Get Environment Variable” wherever they need the same value.
- Cross‑workflow handoff (inter‑workflow):
  - Use a stable variable name (e.g., PROJECT_PREFIX, ACTIVE_CHECKPOINT) so separate workflows launched in the same session share configuration.
- Pseudo‑feedback loops (intra‑workflow):
  - Emulate feedback by writing a value early and reading it later in the same run to condition subsequent steps, without creating illegal graph cycles.
- State and toggles:
  - Flip feature flags (e.g., USE_HIRES_FIX=true) to drive conditional branches or tool selection across multiple, otherwise unconnected nodes.
- Secrets and tokens:
  - Inject API keys, model licenses, or service endpoints at runtime; consumers read them on demand.
- One‑to‑many routing:
  - Publish once, consume everywhere—useful for common output directories, date stamps, or version tags.

Common recipes:
- Share a counter between runs:
  - Read COUNT with “Get Environment Variable” (default 0) → increment in your logic → write back with “Set Environment Variable” for the next run.
- Centralize paths:
  - Use “Set Environment Variable” with name=OUTPUT_DIR, value=/data/renders → multiple savers read OUTPUT_DIR to stay in sync.
- Switch models/tools globally:
  - Use “Set Environment Variable” with name=ACTIVE_MODEL, value=SDXL → routers or conditionals pick the right branch downstream.

Tips and caveats:
- Scope: values live only for the current process and its children; they do not persist after a restart.
- Collisions: environment space is shared; pick distinctive names or prefixes (e.g., OVUM_) to avoid clashes.
- Security: avoid printing secrets; prefer generic names and keep sensitive values out of saved screenshots or public logs.
- Consistency: environment variables are strings; encode complex data (e.g., JSON) explicitly if needed and decode where you read it.
- Ordering: use the passthrough to ensure “set before get” along your execution path; visual proximity doesn’t influence execution—connections do.

In short, “Set Environment Variable” and “Get Environment Variable” act like SetNode/GetNode with super powers: they can tunnel values across the graph, coordinate multiple consumers, and enable inter‑ and intra‑workflow value transfer—while staying simple, explicit, and robust.

## Halt Toggle Node

The **Halt Toggle** node is a versatile control node designed to bring simplified workflow execution halts to your projects.

### Key Features:
- **Flexible Halting:** Easily pause workflow execution when the `stop_now` condition is met.
- **Auto-Reset Capability:** The node can automatically reset itself after halting, allowing seamless continuation of the workflow in subsequent runs without manual intervention.
- **Delay Support:** Introduce a configurable delay (in milliseconds) before halting the workflow.
- **Passthrough Convenience:** The node forwards inputs, keeping graph wiring intuitive and maintaining data flow consistency when used as part of a larger workflow.
- **Detailed Feedback:** Provides outputs to indicate whether a stop was applied and if an auto-reset was triggered.

### How It Works:
When the `stop_now` input is set to true, the **Halt Toggle** node halts the workflow execution. However, if the **reset_after_stop** option is enabled, the halt will auto-disable for the next run, ensuring the workflow proceeds smoothly without requiring manual toggle adjustments.

### Use Case Example:
If you have a workflow that requires pausing at specific stages or debugging steps, the Halt Toggle node provides an elegant solution to stop execution conditionally and resume it dynamically in subsequent runs.

Enhance your workflow control with the Halt Toggle node, empowering you to build more robust and interactive systems effortlessly.

## Pystructure Data Nodes (complementary to ComfyUI-LogicUtils)

These nodes are complementary to the excellent collection at https://github.com/aria1th/ComfyUI-LogicUtils. They focus on list manipulation and small data utilities that pair well with logic/structure nodes from that set.

- List Slice
  - What it does: Returns a slice of an input list using JavaScript-like slice semantics.
  - Inputs:
    - py_list (LIST): The source list.
    - start (INT): Start index. Negative values count from the end. Clamped to bounds; default 0 if empty.
    - end (INT): End index (non-inclusive). Negative values count from the end. Clamped to bounds; defaults to list length if empty.
  - Output:
    - LIST: A new list containing the requested slice. If start >= end after normalization, returns an empty list.
  - Notes: Behavior mirrors JS slice for negative indices and boundary clamping; does not mutate the input list.

- List Splice
  - What it does: Splices into a list using JavaScript-like splice semantics: remove delete_count items starting at start and insert items from insert_list.
  - Inputs:
    - py_list (LIST): The target list (will be modified in place).
    - start (INT): Start index. Negative values count from the end. Clamped to valid positions.
    - delete_count (INT): Number of items to remove (clamped to remaining length; negatives treated as 0).
    - insert_list (LIST): Items to insert at the splice position (can be empty to perform pure deletion).
  - Outputs:
    - LIST (modified_list): The same list instance after splicing.
    - LIST (removed_elements): A list of the elements that were removed.
  - Notes: Mirrors JS semantics for start and delete_count; performs in-place mutation of py_list.

- Repeat Item
  - What it does: Produces a list containing the given item repeated count times.
  - Inputs:
    - item (any): Any value to repeat.
    - count (INT): Number of repetitions. Minimum 0; negatives are treated as 0.
  - Output:
    - LIST: [item, item, ..., item] repeated count times.
  - Notes: Non-mutating; useful for building lists of constants, seeds, file paths, or objects for batch operations.

- Reverse List
  - What it does: Returns a new list in reverse order.
  - Inputs:
    - py_list (LIST): The source list.
  - Output:
    - LIST: A new list with elements reversed.
  - Notes: Non-mutating; the input list is not modified.

- List Concat
  - What it does: Concatenates two lists similar to JS Array.concat.
  - Inputs:
    - list_a (LIST): First list.
    - list_b (LIST): Second list (optional; blank treated as empty).
  - Output:
    - LIST: New list of elements of list_a followed by elements of list_b.
  - Notes: Non-mutating.

- List IndexOf
  - What it does: Finds the first index of a value in a list like JS indexOf.
  - Inputs:
    - py_list (LIST): The list to search.
    - search_element (any): Value to find.
    - start (INT): Optional fromIndex; negative values count from end; blank -> 0.
  - Output:
    - INT: Index of the match; -1 if not found.

- List Join
  - What it does: Joins elements into a string like JS join.
  - Inputs:
    - py_list (LIST): Elements to join.
    - separator (STRING): Optional separator; blank/unspecified -> comma, empty string -> no separator.
  - Output:
    - STRING: Joined string.

- XRange
  - What it does: Python-like xrange/range iterator without generators. Outputs current value, full list, and a boolean flag for exhausted/looped.
  - Inputs:
    - stop (INT): End (exclusive). Required.
    - start (INT): Optional start; blank -> 0.
    - step (INT): Optional step; blank -> 1; cannot be 0; can be negative.
    - repeat (BOOLEAN): If true, wraps to the start (or end for negative step) when reaching the end; the flag output is true on the wrap iteration.
    - cursor (INT): Current index into the range; you can set/reset this manually to control which value is output.
    - advance (BOOLEAN): If true (default), increases cursor by 1 each evaluation so you can tick through values using Repeat/Trigger.
  - Outputs:
    - INT: current value at the cursor.
    - LIST: the full expanded list of values (range(start, stop, step)).
    - BOOLEAN: exhausted_or_looped — true when the range is exhausted (with repeat disabled) or when it loops (with repeat enabled).
  - Notes:
    - Negative steps are supported exactly like Python range. If the computed range is empty, the list is empty and the flag is true; current value returns 0.

## Open Output via Shell (secure)

When your video has finished generating, have VLC (or your default media player) open it automatically.

## Text Ovary (overlay text on images)

Text Ovary is a polished, in-house merge of the excellent TextOverlay node (sfinktah/comfyui-textoverlay) adapted for Ovum.

Why you’ll like it:
- Super simple: plug in an IMAGE and a STRING, pick a font, done.
- Looks great: fill + stroke with independent opacity to keep captions readable over any background.
- Precise placement: left/center/right, top/middle/bottom, with padding and x/y nudges.
- Multiline aware: sensible line spacing and alignment across lines.
- Batch-friendly: renders the same text across a whole batch efficiently.

Inputs:
- image (IMAGE)
- text (STRING, multiline)
- font_size (INT)
- font (choice from bundled fonts)
- fill_color_hex (STRING, e.g. #ffffff)
- stroke_color_hex (STRING)
- stroke_thickness (FLOAT, relative to font size)
- padding (INT)
- horizontal_alignment (left|center|right)
- vertical_alignment (top|middle|bottom)
- x_shift, y_shift (INT)
- line_spacing (FLOAT)
- stroke_opacity (FLOAT)

Output:
- IMAGE with the text composited

Tip: Pair with Python String Format to build captions dynamically from metadata or prompts.

Safely open your rendered media with the system’s default app—no fragile shell strings, no workflow‑stopping errors.

Why you’ll like it:
- Validates the path exists and is a regular file before trying to open it.
- Accepts only image/video types (via MIME detection) to avoid launching arbitrary files.
- Uses platform‑appropriate launchers:
  - Windows: start " <file> (handles spaces and the window‑title quirk).
  - macOS: open <file>
  - Linux: xdg-open <file>
- Secure by design: runs without a shell so spaces/quotes can’t break or inject commands.
- Non‑fatal: any failure returns an “[ERROR] …” string; your workflow keeps going.

Inputs:
- input (any, optional passthrough): helps enforce execution order; doesn’t alter your data.
- filename (STRING): full path to the image or video you want to open.

Output:
- STRING: a success message or an “[ERROR] …” detail you can log, display, or ignore.

Tips:
- Wire filename from your saver node to auto‑open the latest result.
- Works well with format/concat nodes to build paths dynamically.
- On headless systems, the open command may be unavailable; you’ll get a clear error message instead of a crash.

## Regex Nodes (ovum/regex)

A compact suite of regex utilities that mirror Python’s re API while being graph-friendly. They accept plain strings or lists and return structured results without crashing your run when there are no matches.

Highlights:
- Builders and matchers: re.compile flags, search, match, fullmatch, findall, finditer, split, sub, subn
- Match inspectors: view, span/start/end, group/groups/groupdict, select index, expand templates
- Escape helper: re.escape for safe literal matching

These nodes keep outputs list-aware to make it easy to fan out results downstream.

## CUDNN Toggle Ovum

Temporarily flip torch.backends.cudnn.enabled (and benchmark) on/off around a section of your graph. Useful for cases where disabling cuDNN speeds up certain ops (e.g., VAE Encode/Decode under ZLUDA). Returns the previous state so you can restore it later.

## Image List Loader + Folder Paths

Load a batch of images from a folder or an explicit list with optional regex/custom filtering, recursion, and sorting. Outputs images, masks, normalized file paths, callback payloads, embedded prompt/workflow info, and an ‘exhausted’ flag.
- Folder Paths: utility to retrieve common ComfyUI directories as normalized strings for wiring into other nodes.

## BigKnob (Widget)

A simple numeric knob with min/max clamping and precision rounding. Great as a human-friendly dial to drive parameters.  Totally untested.

## LM Studio Prompt (Ovum/LLM)

Connect to an LM Studio server to generate text (optionally with an image for vision models). Supports prompt modes, wildcard expansion, dynamic model discovery, and optional auto-unload after inactivity. 
**NOTE:** Since LM Studio does not actually support unloading models on request, this node requires you install the 
the LM Studio model "liquid/lfm2-1.2b" and set your automatic model unloading to the shortest possible period (60 seconds).

## LM Studio Unload (Ovum/LLM)

Force an immediate unload of the LM Studio model when an auto-unload timer is pending. This node cancels the repository’s shared unload timer (scheduled by LM Studio Prompt nodes) and triggers a tiny model switch on the LM Studio server to free VRAM sooner.

What it does:
- Cancels any pending auto-unload timer shared by all LM Studio nodes in this package.
- If a timer was active, it sends a minimal request to switch to the tiny model "liquid/lfm2-1.2b" so VRAM is released quickly.
- If no timer was active, it does nothing (and tells you so).
- Always passes its first input through unchanged so you can wire it inline without breaking your graph.

Inputs:
- any_input (ANY, passthrough)
- server_address (STRING, default: localhost)
- server_port (INT, default: 1234)

Outputs:
- any_output (ANY, passthrough of any_input)
- status (STRING) — human-readable summary: unloaded now, attempted but failed, or nothing to do.

Notes:
- Install the LM Studio model "liquid/lfm2-1.2b" for unloading to work as designed.
- All LM Studio requests from these nodes are serialized; the unload timer is suspended during requests and restarted after completion.

## Workflow Helpers (Widgets to values)

- Widget To String (KJNodes): Read a widget from any node in your workflow (works inside subgraphs, unlike KJNODE) and returns its value as a STRING
- Workflow Widget To Any: Same idea, but returns the native type from a PROMPT&WORKFLOW input.
- Sync Sink (KJNodes): A no-op sink that forces upstream branches to complete before proceeding; handy for synchronizing flows.

## VHS Helper: Next Video Filename

Predict the next auto-numbered output base path that VHS VideoCombine will use (without writing files), so you can plan downstream file operations deterministically.

## Wildcard Processor (Escapable)

Powerful prompt preprocessor that supports wildcard files, date stamping, simple random ranges, and safe comment/markup stripping. Designed to play nicely with other Ovum text utilities.

## Does Kijai SetNode exist?

Checks your current workflow to see if a Kijai SetNode exists for a given Constant and is actually wired at input 0. Useful for conditionally enabling branches tied to KJNodes Set/Get patterns.

## Folder, Range, and Sequence Utilities

- XRange: A range-like tick node that outputs current value, full list, and an overflow/loop flag with optional repeat and reset behavior. Useful for counters and iteration control.

---

## Additional nodes and utilities (not previously documented)

The following nodes are available in the root Python modules but were not yet described above. This section adds short, practical explanations so you can use them immediately.

### OS Path Utilities (ovum/path and ovum/path/os.path)
A set of small path helpers and thin wrappers over Python’s os.path functions.
- STRING to PATHLIKE (PurePath): Convert a path string to a pathlib.PurePath object for type-safe wiring.
- Backslashes → Forward: Convert Windows backslashes to forward slashes.
- os.path.abspath / expanduser / basename / dirname / split / splitext / join / exists / isfile / isdir …: Each node mirrors the corresponding os.path function and returns a normalized string. Many accept an optional path input jack so you can provide the value either as a widget or as a link.
- Most nodes include a forward_slashes option to normalize separators in the output.

### Casting helpers (ovum/data)
Lightweight type adapters that help you connect otherwise incompatible sockets.
- Blind Cast: Reinterpret any value as any type (passes value through unchanged). Exists in a single and list variant.
- Cast Pyobjects/List to Any: Treat a LIST as any type (*) while keeping list outputs list-shaped.
- Cast Any to Pyobjects/List: Accept any value and expose it explicitly as LIST (strings become [string]).

### More List utilities (Data)
Complements the Pystructure section with additional practical nodes.
- Unique List / Unique Batch: Remove duplicates while preserving order. Works with hashable and unhashable elements.
- String List Editor / String Batch Editor: Quickly build a list by typing one item per line in a multiline text box (blank lines ignored).
- From List Type / From Batch Type: Convert a LIST to tuple, set, dict (index→value), or dict from key/value pairs.
- List Extend / Batch Extend: Non‑mutating concatenation of two Python lists.

### Passthrough shapers (ovum)
A family of “do nothing” nodes that are useful for wiring and debugging.
- Passthru (single/multi/list variants): Forwards inputs unchanged while letting you explicitly control whether the input and/or output is treated as a list by the graph engine. Helpful when you need to satisfy list/non‑list expectations without changing your data.
- Pretty/Compact preview: Some variants include compact pretty‑printing of complex values in the UI to make debugging easier (no side effects on the data).

### Underscore.js method nodes (ovum/underscore)
**NOTE:** These are an absolute disaster to use in production. They are a WORK IN PROGRESS and are not recommended for use in workflows.
Graph wrappers for underscore3 (a Python port of Underscore.js). They let you chain collection utilities in Comfy.
- _.CHAIN and _.VALUE: Start a chain with an object (list/dict/etc.) and extract the final value.
- Method nodes: One node per Underscore method (map, filter, reduce, keys, values, uniq, flatten, zip, range, …). Each has two outputs: the updated chain and the immediate result of that method.
- Iteratee support: For iteratee‑style methods (e.g., map), you can either provide a simple function via UI inputs or supply an iteratee node class name to build a tiny subgraph automatically that runs per item and collects its chosen output.

### Load Image with Workflow + IMAGE_EX Context
File loader and context nodes that expose embedded prompt/workflow metadata along with images.
- Load Image with Workflow: Like core Load Image, but also extracts embedded prompt/workflow where present. Useful for round‑tripping images with their provenance.
- Load Image from Output with Workflow: Fetch a previously saved output image and parse its embedded metadata.
- IMAGE_EX Context: Pass through a single IMAGE_EX dict while optionally overriding image, mask, filepath, prompt, workflow, or edits.
- IMAGE_EX Context (List): Same as above but for lists. All provided list inputs must be the same length; outputs are lists of images/masks/paths/prompts/workflows/edits.

### Loop/Logic nodes (ovum/loop)
Tools for structured iteration and simple branching without illegal graph cycles.
- ForeachListBeginOvum + ForeachListEndOvum: I think I just stole these from easyUse to learn how they worked!
- MapStartOvum + MapEndOvum: Like Foreach but auto‑merges each per‑iteration result into an accumulator (typically a list) for you.

### Logic helpers (ovum/loop)
Small building blocks used with the loop nodes.
- IfElseOvum: Simple branch select; returns on_true or on_false based on a BOOLEAN input. Supports lazy inputs so only the chosen branch is evaluated.
- CompareOvum: Compare two values using ==, !=, <, <=, >, >= and return BOOLEAN.
- Convert any to INT and add 1 / subtract 1: Utility nodes (PlusOne / MinusOne) that coerce a value to INT and adjust by ±1.
- Uncachable List Copy (immutable): Forces a fresh copy of a list or the values of a dict every run so that Comfy treats it as changed (useful in loops).



## ComboMirror

Mirror the options from any combobox input and drive multiple targets with a single selection.

- What it does: Connect ComboMirror to a node input that uses a combo-box and it automatically adopts that list of options. Then feed ComboMirror’s output into any number of compatible combo inputs so they all share the same chosen value.
- Why it’s helpful: Keep several nodes in sync with one picker and reduce repetitive clicking.
- Outputs: COMBO (the selected value) and LIST (all available option strings mirrored from the target).
- How to select:
  - Manual: Pick from the mirrored options in the ComboMirror widget (default).
  - choice_index: Provide a non-negative index to force selection by index and disable manual picking.
  - choice_regex: Provide a string/regex to auto-pick. Matching order is:
    1) Regex search (re.search)
    2) Exact match (case-sensitive)
    3) Exact match (case-insensitive)
    4) Substring contains (case-insensitive)
  - If none of the above applies, the current widget value is used.
- How to use:
  1. Place ComboMirror near a node that has a combobox input (e.g., model, scheduler, sampler).
  2. Connect ComboMirror’s output to that input; the options will be mirrored into the ComboMirror widget.
  3. Pick a value once (or drive via choice_index/choice_regex) and wire the COMBO output to other matching combo inputs to keep them synchronized.

Notes:
- For advanced workflows the frontend also passes the raw options as a hidden string; the node returns those as the LIST output for inspection or debugging.



## VHS PNG deleter (VhsPngDeletingOvum)

Remove intermediate PNG frames produced by Video Helper Suite (VHS) from both your list of filenames and from disk.

- Category: ovum/workflow
- Display name: "VHS PNG deleter"
- Class name: VhsPngDeletingOvum

Inputs
- filenames (STRING)
  - Accepts a STRING, a list of STRINGs, or a tuple shaped like `(BOOLEAN, LIST[STRING])` as produced by some VHS nodes.
  - If a list or tuple is provided, the node will treat the inner list as a list of file paths.

Outputs
- filenames (STRING)
  - Mirrors the input structure:
    - If input was a list, returns a filtered list with .png items removed.
    - If input was a tuple `(flag, list)`, returns `(flag, filtered_list)` with the same flag preserved.
    - Otherwise returns the input unchanged.

Behavior
- For list inputs (or the list inside a supported tuple):
  - Removes any entries that end with the .png extension (case-insensitive).
  - Attempts to delete those .png files from the filesystem (silently ignores errors if a file cannot be removed).
  - Returns the remaining non-.png filenames.
- For non-list inputs, simply returns the input unchanged.

Example
```
(True,
  ['C:\\zluda\\comfyui-n\\output\\WanVideo2_2_T2V_VHS_01102.png',
   'C:\\zluda\\comfyui-n\\output\\WanVideo2_2_T2V_VHS_01102.mp4'])
```
becomes
```
(True,
  ['C:\\zluda\\comfyui-n\\output\\WanVideo2_2_T2V_VHS_01102.mp4'])
```

Notes
- This is useful after VHS video assembly steps when you want to clean up temporary PNG frames.


---

## Burn Notice

A small utility node for ephemeral text that should be consumed once and then disappear. It exposes a multiline STRING input and immediately returns it on execution, but the UI clears the field afterward. Optionally, the node can auto‑mute itself so it won’t execute again until you unmute it.

- Category: ovum/util
- Display name: "Burn Notice"
- Class name: BurnNoticeOvum

Inputs
- value (STRING, multiline)
  - Arbitrary text. This is returned as the output on execution. After execution completes, the UI clears this field so it doesn’t persist into the next run.
- mute_after (BOOLEAN, default: false)
  - When enabled, the frontend mutes the node after it runs (equivalent to LiteGraph mode = 2). This prevents the node from executing again until you manually unmute it from the node’s context menu.

Outputs
- value (STRING)
  - Exactly the text that was provided at execution time.

Behavior and notes
- The backend simply returns the provided string; all “erase after read” behavior is handled in the frontend extension.
- After onExecuted, the UI:
  - Sets the "value" widget to an empty string.
  - If mute_after is true, sets node.mode = 2 (mute) and marks the canvas dirty so the UI updates immediately.
- Practical uses: one‑shot messages, tokens, secrets, ad‑hoc parameters, or any text you intend to consume once and then remove from the workflow state.

---

## Colorize Graph

A frontend-only utility node that recolors all nodes in the current graph based on the type of the first input (if any),
else the first output. It uses the same color mapping SetTwinNodes, which is an extended version of Kijai's SetNode coloring scheme.

- Category: ovum
- Display name: "Colorize Graph"
- Node type: ColorizeGraph (frontend)

Buttons
- Apply Colors: Recolors every node according to the type heuristic described above.
- Undo: Restores all nodes to their original colors from before the last Apply Colors.

Notes
- Skips recoloring itself.
- Works entirely in the browser; no backend execution is involved.
- If you click Apply Colors multiple times, Undo restores the colors as they were before the first apply in that session.

---

## Get Setting (Ovum/Utils)

A lightweight utility node that reads a value from the workflow "settings" snapshot shared by the frontend. It lets you reference run-time settings (like user preferences or UI-level parameters) inside your graph without extra wiring.

- Category: ovum/utils
- Display name: "Get Setting"
- Python class: GetSettingOvum

What it does
- Exposes a COMBO selector of available setting keys (populated by the frontend).
- Returns the current value for the selected key (type is "*" to allow any type).
- Mirrors the resolved value into a read-only STRING field (value_out) for quick inspection.

Inputs
- setting (COMBO, required): The setting key to read. The options are populated by the frontend.

Optional/Hidden
- value_out (STRING, optional, readonly): Text view of the resolved value.
- extra_pnginfo (hidden): Provided by Comfy; used to obtain the workflow settings snapshot.

Output
- value (*): The actual setting value from the workflow settings object. If the key doesn’t exist, the node returns None.  The type of this output will change to match the type of the setting key.

Notes
- Prefers workflow.settings when present; otherwise falls back to workflow.extra.settings in the PNG workflow blob.
- The node does not mutate any data; it only reads.

---

## New Multi-type Dictionary

![New Multi-type Dictionary example](resources/new-multitype-dict.png)

Build a Python DICT from multiple dynamic inputs whose keys come from the input labels you set in the graph. Each input can accept any type, so you can mix simple scalars and complex objects in a single dictionary.

What it does
- Creates inputs named key-value-1, key-value-2, ... as you connect them. You can rename the visible label of each input; that label becomes the dictionary key.
- Supports any ComfyUI type on the value side (images, lists, dicts, numbers, strings, etc.). The node returns a single DICT containing one entry per connected input.
- Preserves your custom labels: once you change an input label away from its default, it won’t be auto‑overwritten by dynamic input maintenance.
- Works reliably with API runs: the frontend stores a mapping of input names to labels in the workflow extras so the Python backend knows your chosen keys at execution time.

How it works
- UI side (JS): The node manages dynamic inputs with the pattern key-value-n. When the last input becomes linked, a new empty input is added; when you disconnect, extra trailing empty inputs are trimmed. During graphToPrompt, the UI writes an array of [inputName, label] pairs into workflow.extra under the key `ovum.multi.dict:(<nodeId>)`.
- Backend (Python): At run time, the node reads that mapping from extra_pnginfo and builds the dictionary using the labels as keys and the connected input values as values. If a label is missing, it falls back to the input name.

Example (screenshot above)
- The top-left Get Setting outputs a complex DICT (type: HIDDEN in settings, displayed as JSON). Its link goes into the New Multi‑type Dictionary input whose label is set to disabledExtensions. That key stores the entire dict object under "disabledExtensions".
- The bottom-left Get Setting outputs a COMBO value (effectively an INT with value 2). Its link goes into the input labeled linkRenderMode. That key stores the integer 2 under "linkRenderMode".
- The resulting dictionary has two entries: {"disabledExtensions": <DICT>, "linkRenderMode": 2}.

Inputs
- key-value-n (*): Dynamic inputs that accept any type. Change the input label to set the dictionary key. The default label matches the input name (e.g., key-value-1) until you customize it.
- unique_id, extra_pnginfo, prompt (hidden): Standard Comfy plumbing; extra_pnginfo carries the label mapping from the UI.

Output
- dict (DICT): A dictionary with one entry per connected input using your labels as keys.

Tips
- Use meaningful labels like seed, strength, disabledExtensions to make the resulting dict self‑documenting.
- You can wire in non‑scalar values (lists, dicts, images); the node keeps their native types.

---

## Index of Node Classes

Below is an index of Python class names for nodes in this repository. Each entry links to the section in this README where the node or its family is documented; entries marked as "undocumented" currently have no dedicated section.

- AmdNvidiaIfElseOvum — undocumented
- AssertOvum — undocumented
- BigKnob — see BigKnob (Widget): #bigknob-widget
- BurnNoticeOvum — see Burn Notice: #burn-notice
- CUDNNToggleOvum — see CUDNN Toggle Ovum: #cudnn-toggle-ovum
- CastAnyToList — see Casting helpers: #casting-helpers-ovumdata
- CastListToAny — see Casting helpers: #casting-helpers-ovumdata
- ColorizeGraph — see Colorize Graph: #colorize-graph
- ComboMirrorOvum — see ComboMirror: #combomirror
- CommandExecNode — undocumented
- ConcatBatchesOvum — undocumented
- ConcatLists — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- ConcatListsOvum — see More List utilities (Data): #more-list-utilities-data
- ConvertAny2Dict — undocumented
- ConvertAny2List — undocumented
- ConvertAny2Set — undocumented
- ConvertAny2Tuple — undocumented
- CreateEmptyList — undocumented
- FolderPathsNode — see Image List Loader + Folder Paths: #image-list-loader--folder-paths
- ForeachListBeginOvum — see Loop/Logic nodes: #looplogic-nodes-ovumloop
- ForeachListEndOvum — see Loop/Logic nodes: #looplogic-nodes-ovumloop
- FromBatchTypeNodeOvum — undocumented
- FromListTypeNode — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- FromListTypeNodeOvum — see More List utilities (Data): #more-list-utilities-data
- GetByIndex — see More List utilities (Data): #more-list-utilities-data
- GetEnvVar — see Environment Bridge: #environment-bridge-set-environment-variable-and-get-environment-variable
- GetListLength — undocumented
- GetLocalStorage — see Browser Local Storage: #browser-local-storage-set-localstorage-and-get-localstorage
- GetSettingOvum — see Get Setting: #get-setting-ovumutils
- Ground — undocumented
- IfElseOvum — see Logic helpers: #logic-helpers-ovumloop
- ImageExContextListOvum — see Load Image with Workflow + IMAGE_EX Context: #load-image-with-workflow--image_ex-context
- ImageExContextOvum — see Load Image with Workflow + IMAGE_EX Context: #load-image-with-workflow--image_ex-context
- IndexOf — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- IndexOfBatchOvum — undocumented
- IndexOfOvum — see More List utilities (Data): #more-list-utilities-data
- JoinBatchOvum — undocumented
- JoinList — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- JoinListOvum — see More List utilities (Data): #more-list-utilities-data
- LMStudioPromptOvum — see LM Studio Prompt (Ovum/LLM): #lm-studio-prompt-ovumllm
- LMStudioUnloadOvum — see LM Studio Unload (Ovum/LLM): #lm-studio-unload-ovumllm
- ListExtend — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- ListExtendOvum — see More List utilities (Data): #more-list-utilities-data
- ListSlice — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- ListSliceOvum — see More List utilities (Data): #more-list-utilities-data
- ListSplice — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- ListSpliceOvum — see More List utilities (Data): #more-list-utilities-data
- LiveCrop — see Live Crop (interactive): #live-crop-interactive
- LoadImageFromOutputWithWorkflowOvum — see Load Image with Workflow + IMAGE_EX Context: #load-image-with-workflow--image_ex-context
- LoadImageWithWorkflowOvum — see Load Image with Workflow + IMAGE_EX Context: #load-image-with-workflow--image_ex-context
- LoadImagesListWithCallback — see Image List Loader + Folder Paths: #image-list-loader--folder-paths
- MakeFlatImageList — see More List utilities (Data): #more-list-utilities-data
- MakeFlatStringList — see More List utilities (Data): #more-list-utilities-data
- MapEndOvum — see Loop/Logic nodes: #looplogic-nodes-ovumloop
- MapStartOvum — see Loop/Logic nodes: #looplogic-nodes-ovumloop
- MinusOne — see Logic helpers: #logic-helpers-ovumloop
- NewMultiDictionaryOvum — see New Multi‑type Dictionary: #new-multi‑type-dictionary
- NextVideoFilenameOvum — see VHS Helper: Next Video Filename: #vhs-helper-next-video-filename
- OpenOutputViaShell — see Open Output via Shell (secure): #open-output-via-shell-secure
- OvumCombinePaths — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathAbspath — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathBasename — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathCommonPath — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathCommonPrefix — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathDirname — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathExists — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathExpanduser — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathExpandvars — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathGetAtime — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathGetCtime — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathGetMtime — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathGetSize — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathIsAbs — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathIsdir — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathIsfile — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathIslink — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathIsmount — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathJoin — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathLexists — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathNormCase — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathNormPath — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathRealpath — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathRelpath — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathSamefile — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathSplit — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathSplitAll — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathSplitdrive — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumOsPathSplitext — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumPathBackToForward — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumPathToPathLike — see OS Path Utilities: #os-path-utilities-ovumpath-and-ovumpathospath
- OvumReEscape — see Regex Nodes: #regex-nodes-ovumregex
- OvumReFindAll — see Regex Nodes: #regex-nodes-ovumregex
- OvumReFindIter — see Regex Nodes: #regex-nodes-ovumregex
- OvumReFlags — see Regex Nodes: #regex-nodes-ovumregex
- OvumReFullMatch — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatch — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchExpand — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchGroup — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchInfo — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchSelect — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchSpan — see Regex Nodes: #regex-nodes-ovumregex
- OvumReMatchView — see Regex Nodes: #regex-nodes-ovumregex
- OvumReSearch — see Regex Nodes: #regex-nodes-ovumregex
- OvumReSplit — see Regex Nodes: #regex-nodes-ovumregex
- OvumReSub — see Regex Nodes: #regex-nodes-ovumregex
- OvumReSubN — see Regex Nodes: #regex-nodes-ovumregex
- OvumWildcardProcessor — see Wildcard Processor (Escapable): #wildcard-processor-escapable
- PassthruInputAndOutputIsListOvum — see Passthrough shapers: #passthrough-shapers-ovum
- PassthruInputIsListOvum — see Passthrough shapers: #passthrough-shapers-ovum
- PassthruOutputIsListOvum — see Passthrough shapers: #passthrough-shapers-ovum
- PassthruOvum — see Passthrough shapers: #passthrough-shapers-ovum
- PlusOne — see Logic helpers: #logic-helpers-ovumloop
- PythonStringFormat — see Python String Format: #python-string-format
- RepeatItem — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- RepeatItemBatchOvum — undocumented
- RepeatItemOvum — see More List utilities (Data): #more-list-utilities-data
- ReverseBatchOvum — undocumented
- ReverseList — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- ReverseListOvum — see More List utilities (Data): #more-list-utilities-data
- SetEnvVar — see Environment Bridge: #environment-bridge-set-environment-variable-and-get-environment-variable
- SetLocalStorage — see Browser Local Storage: #browser-local-storage-set-localstorage-and-get-localstorage
- StringListEditor — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- StringListEditorOvum — see More List utilities (Data): #more-list-utilities-data
- SyncSinkOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- TextOvary — see Text Ovary (overlay text on images): #text-ovary-overlay-text-on-images
- Timer — see Timer: #timer
- UniqueList — see Pystructure Data Nodes: #pystructure-data-nodes-complementary-to-comfyui-logicutils
- UniqueListOvum — see More List utilities (Data): #more-list-utilities-data
- VhsPngDeletingOvum — see VHS PNG deleter: #vhs-png-deleter-vhspngdeletingovum
- WidgetToBooleanOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- WidgetToFloatOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- WidgetToIntOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- WidgetToStringOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- WorkflowWidgetToAnyOvum — see Workflow Helpers: #workflow-helpers-widgets-to-values
- XRangeNode — see Folder, Range, and Sequence Utilities: #folder-range-and-sequence-utilities