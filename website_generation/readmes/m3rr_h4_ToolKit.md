# h4 Toolkit — Comprehensive Operations Manual { WORK IN PROGRESS - NOT BEING TRACKED CURRENTLY - SHELVED PROJECT FOR NOW }
# SEE h4_Live instead (It doesn't do exactly the same things, but operates on a similar idea and philosophy- check it out) 
> Hyper-observable, cyberpunk-themed quality-of-life boosts for ComfyUI. This README is the definitive companion for installing, running, and mastering the **h4 Toolkit** nodes. Every control, feature, and internal safeguard is documented below.

---

## Table of Contents

1. [Project Snapshot](#project-snapshot)
2. [Installation & Environment](#installation--environment)
3. [Quick Start](#quick-start)
4. [Node Deep Dives](#node-deep-dives)
	1. [The Engine — `h4_PlotXY`](#the-engine--h4_plotxy)
	2. [Axis Driver — `h4_AxisDriver`](#axis-driver--h4_axisdriver)
	3. [Debug-a-Tron 3000 — `h4_DebugATron3000`](#debug-a-tron-3000--h4_debugatron3000)
	4. [Debug-a-Tron Router — `h4_DebugATronRouter`](#debug-a-tron-router--h4_debugatronrouter)
    5. [Debug Console — `h4_DebugATron3000Console`](#debug-console--h4_debugatron3000console)
    6. [Seed Broadcaster — `h4_SeedBroadcaster`](#seed-broadcaster--h4_seedbroadcaster)
    7. [The Varianator — `h4_Varianator`](#the-varianator--h4_varianator)
    8. [Execution Logger — `h4_ExecutionLogger`](#execution-logger--h4_executionlogger)
5. [Go Plus Ultra Diagnostics](#go-plus-ultra-diagnostics)
6. [UI Companion (`js/h4_ui.js`)](#ui-companion-jsh4_uijs)
7. [Tips & Best Practices](#tips--best-practices)
8. [Operational Playbooks](#operational-playbooks)
9. [Troubleshooting & Support](#troubleshooting--support)
10. [Development Notes](#development-notes)
11. [Release Intel & Versioning](#release-intel--versioning)
12. [Appendix: Function Index](#appendix-function-index)
13. [License](#license)

---

## Project Snapshot

| Artifact | Value |
| --- | --- |
| **Toolkit Version** | `1.3.0` |
| **Engine (h4_PlotXY) Version** | `1.3.0` |
| **Axis Driver Version** | `0.6.0` |
| **Debug Nodes Version** | `2.1.0` |
| **Last Updated** | October 2025 |
| **Supported Platform** | ComfyUI (Windows/Linux/macOS) |
| **Language Stack** | Python 3.10+ (nodes), JavaScript (UI overlay) |

### Key Pillars

- **The Engine (`h4_PlotXY`)** — production-grade sampler/grid orchestrator with plan matrices, LoRA layering, preview publishing, and labelled outputs.
- **Axis Driver (`h4_AxisDriver`)** — advanced axis configuration node with visual UI for building test matrices. Supports checkpoints, LoRAs, prompts, samplers, and parameter sweeps with model dropdowns.
- **Debug-a-Tron Suite** — real-time diagnostics nodes operating in monitor/passthrough modes, capable of deep latent inspection and branch-aware routing.
- **UI Enhancements** — dynamic sockets, contextual tooltips, orientation controls, and a polished Go Plus Ultra toggle experience.
- **Debug Console & Logging Utilities** — the `h4_DebugATron3000Console` output-node renders cyberpunk HTML telemetry, while `h4_ExecutionLogger` mirrors activity straight to the ComfyUI log stream.
- **Workflow Utilities** — `h4_SeedBroadcaster` keeps samplers in sync with deterministic seed streams, while `h4_Varianator` riffs on existing latents with profile-driven denoise windows, prompt jitter, and optional GO PLUS ULTRA telemetry.

### October 2025 Recovery Recap

| Area | What We Fixed or Added | Status |
| --- | --- | --- |
| Lost Nodes | Pulled `h4_SeedBroadcaster`, `h4_DebugATron3000Console`, and `h4_ExecutionLogger` back from git history, rebuilt their tooltips, colour palettes, and class registrations. | ✅ Restored |
| Axis Driver Label Layout | Border mode was just repainting the overlay. Rewrote the grid annotation pipeline so `border` truly adds top and left gutters, carries custom axis titles, and honours background swatches. | ✅ Working |
| Overlay Styling | Added palette helpers so overlay labels respect custom font size, family, colour, and background opacity from the Driver. | ✅ Working |
| LoRA Safety Checks | Embedded checkpoint/LoRA “family” inference so the Engine warns (and stops) when a mismatched LoRA is applied to the wrong base model. | ✅ Working |
| Preview + Logging Nodes | Reintroduced HTML console output, added execution log mirroring, and ensured all nodes are exported in `NODE_CLASS_MAPPINGS` for ComfyUI discovery. | ✅ Working |
| Tests | Manual smoke runs inside ComfyUI after each change. No automated test harness yet. | ⚠️ Follow-up |

> We intentionally left the old sampler compatibility shim in place while adding the new guards. Nothing was removed, so earlier workflows stay compatible.

---

## Installation & Environment

### Prerequisites

- ComfyUI checkout with write access to `custom_nodes/`
- Python 3.10 or 3.11 (mirrors ComfyUI baseline)
- Git (recommended) or manual download capabilities

### Dependency Footprint

`h4_Plot/__init__.py` auto-verifies and installs the following when missing:

- `colorama`
- `numpy`
- `torch`

> **Tip:** For air-gapped setups, install these manually into the ComfyUI environment first.

### Installation Steps

1. Navigate to the ComfyUI `custom_nodes` directory.
2. Clone or extract the toolkit:

	```powershell
	git clone https://github.com/m3rr/h4_ToolKit.git
	```

3. Restart ComfyUI. On launch, the toolkit prints a neon status banner enumerating loaded nodes.

### Optional Verification

Run a syntax gate to ensure your environment recognises the toolkit:

```powershell
python -m py_compile h4_Plot/nodes.py
```

Successful execution (exit code `0`) confirms the nodes file is syntax-tight for your interpreter.

---

## Quick Start

1. Drop **The Engine** node (`h4 : The Engine (Simple Sampler+Plot)`) into your ComfyUI graph.
2. Wire in prompts, sampler defaults, and (optionally) external latents or checkpoints.
3. Add **Debug-a-Tron 3000** downstream of any signal bundle you want to observe; flip `mode` to `monitor` during prototyping.
4. Kick off a run. Watch the ComfyUI console for colour-coded logs describing every stage.
5. Enable **GO PLUS ULTRA?!** when you need latent snapshots, anomaly detection, previews, JSON reporting, or model fingerprinting.
6. For dual-branch graphs (e.g., diffuser vs. refiner), insert the **Debug-a-Tron Router** to mirror and audit both branches simultaneously.
7. Bolt on the **Seed Broadcaster**, **Varianator**, and **Execution Logger** when orchestrating multi-node grids: broadcast a single seed anchor, spin off guided variations (Varianator needs the Engine's `latent` + `model` + `vae` outputs, and the `clip` handle if you want prompt-driven features), and keep a human-readable audit trail in the console.

> **Workflow Pro-Tip:** Start with Debug-a-Tron disabled to validate your graph, then activate GO PLUS ULTRA for targeted forensic passes.

### Wiring Cheat Sheet

```
 Axis Driver Triplet                     Core Sampler                     Debug Fan-Out                    Seed Sync
 ┌────────────────────┐       ┌──────────────────────────┐       ┌──────────────────────────┐        ┌────────────────────┐
 │ h4_AxisDriver (X) │─┐     │ h4_PlotXY "The Engine"   │─▶ IMG │ h4_DebugATron3000        │─▶ …    │ h4_SeedBroadcaster │─▶ seed ➜ connect to every sampler
 └────────────────────┘ │     │  axis_x / axis_y / axis_z│─▶ LAT │ h4_DebugATron3000Console │─▶ …    └────────────────────┘
 ┌────────────────────┐ │     │  prompts / schedulers    │─▶ JSON│ h4_ExecutionLogger       │─▶ log  (one output, unlimited links)
 │ h4_AxisDriver (Y) │─┼────▶ │  accepts model / latent  │      │ h4_DebugATronRouter      │─▶ dual
 └────────────────────┘ │     │  optional legacy widgets │      │                            
 ┌────────────────────┐ │     └──────────────────────────┘      └──────────────────────────┘
 │ h4_AxisDriver (Z) │─┘
 └────────────────────┘
```

Swap any block on the right for your usual sampler/output nodes. The Seed Broadcaster now emits a single seed output you can multi-wire to every sampler that needs to stay in sync, while the Execution Logger happily watches whatever you plug into its optional slots.

---

## Node Deep Dives

### The Engine — `h4_PlotXY`

**Purpose:** A full-stack sampler orchestrator that builds plan matrices, applies LoRAs, invokes samplers safely across ComfyUI versions, and outputs both per-image tensors and an annotated grid.

**In Plain Words:** Point it at a checkpoint (or plug one in), tell it what you want to vary across the grid, and it will churn through every combo while keeping logs, previews, and safety rails in place.

#### Feature Rundown

- Builds X/Y grids from prompts, samplers, CFG, steps, seeds, LoRAs, schedulers, or any mix you throw at it.
- Auto-loads checkpoints, VAEs, CLIPs, and LoRAs; respects anything you manually connect instead.
- Writes the plan name directly onto each tile, and now supports Driver-driven border layouts.
- Generates previews during the run when preview helpers are available, otherwise keeps quiet with a single warning.
- Keeps the last model/clip/vae/latent/prompt bundle so you can chain downstream nodes without rebuilding state.
- Detects mismatched LoRAs by comparing “family” metadata and refuses to apply the wrong weight set.

#### Inputs & Widgets

| Control | Description |
| --- | --- |
| `seed` | Base RNG seed. Axis plans can override per-cell values. |
| `steps` | Default sampler steps (integer). |
| `cfg` | Classifier-free guidance scale. |
| `denoise` | Denoise strength. Lower values adhere to input latent. |
| `clip_skip` | CLIP layer skip count; gracefully no-ops when the model lacks the hook. |
| `sampler_name` | Default sampler selection; axis presets can swap per cell. |
| `scheduler_name` | Noise schedule curve. |
| `width` / `height` | Dimensions for latent creation when no latent input is provided. |
| `checkpoint` | Baseline checkpoint to load. Select `<none>` to disable (requires model input). |
| `vae_name` / `clip_text_name` / `clip_vision_name` | Override modules. `<none>` disables, `<checkpoint>` uses model's built-in version. |
| `positive_prompt` / `negative_prompt` | Base prompts; axis plans can append fragments via newline tokens. |
| `x_axis_mode` / `x_axis_values` | Row axis configuration (prompt, sampler, scheduler, CFG, steps, denoise, seed, LoRA, etc.). |
| `y_axis_mode` / `y_axis_values` | Column axis configuration, identical presets to the X axis. |

Optional inlets include `model`, `clip`, `clip_vision`, `vae`, generic/positive/negative conditioning payloads, `latent`, `image`, and `mask` tensors. When supplied, The Engine respects them; otherwise it provisions defaults.

**Outputs at a Glance:**

| Outlet | What You Get |
| --- | --- |
| `Images` | All individual renders stacked along the batch axis. |
| `Grid_Image` | One big panel with labels on every tile (border layout adds top/left gutters). |
| `Model` / `CLIP` / `VAE` | Handles for the final combo used, ready for downstream reuse. |
| `Latent` | Deep copy of the last latent dictionary so you can carry on editing. |
| `Positive` / `Negative` | Conditioning lists cloned from the last run. |

#### Execution Pipeline

1. **Plan Construction** — Axis descriptors are parsed into `AxisDescriptor` dataclasses, each capturing checkpoint swaps, prompt suffixes, LoRAs, and overrides.
2. **Model Acquisition** — `get_model_bundle` fetches the checkpoint trio (UNet, CLIP, VAE). LoRAs are layered via `_apply_loras` with trace logging per injection.
3. **Latent Strategy** — `_prepare_latent` either clones incoming latents, encodes images, or fabricates an empty latent with the configured width/height.
4. **Sampler Invocation** — `_run_sampler` collaborates with `_invoke_sampler_with_compatibility` to adapt kwargs based on the active sampler signature. Sigma schedules are precomputed and reshaped to match device placement.
5. **Preview Publishing** — `_get_preview_handlers` picks the best decode/publish pair (preferring `latent_preview`, falling back to ComfyUI helpers or direct VAE decoding) and pushes JPEG snapshots mid-run.
6. **Grid Assembly** — `compose_image_grid` and `annotate_grid_image` stitch decoded tensors into a labelled panel. Annotations capture plan labels (e.g., `sampler: dpmpp_2m_sde | cfg: 6`).
7. **Output Packaging** — Returns a stacked tensor of individual images, the labelled grid, final model/clip/vae handles, the last latent, and positive/negative conditioning suitable for downstream reuse.

#### Unique Safeguards

- **Signature-Aware Shim:** `_invoke_sampler_with_compatibility` introspects the sampler function, renaming/dropping kwargs to match modern ComfyUI expectations. If a required parameter is still missing, it retries with raw kwargs so upstream errors carry context.
- **Sigma Generator Hardening:** All calls to `calculate_sigmas` are wrapped to supply only the keyword parameters it expects. Missing information results in logged warnings instead of hard crashes.
- **Clip-Skip Gracefulness:** `_set_clip_skip` hunts for the `set_clip_skip` hook across wrapped models, logging once if none is found.
- **Preview Fallbacks:** When `latent_preview` is unavailable, Engine falls back to direct VAE decoding. The toolkit warns once and continues without flooding logs.
- **GPU Cache Discipline:** If CUDA is detected, the Engine clears the cache after each plan to reduce VRAM spikes.

#### Operating The Engine

1. Configure baseline sampler settings (seed, steps, cfg, denoise).
2. Choose axis presets—example: `X Axis = sampler`, `Y Axis = cfg` with respective value lists.
3. Populate prompts or connect upstream conditioning.
4. Optionally connect a latent/image pair to start from a pre-existing source.
5. Execute the workflow. Inspect the console for per-plan logs and verify the annotated grid output.
6. Chain downstream to Debug-a-Tron nodes for post-run introspection.

---

### Axis Driver — `h4_AxisDriver`

**Purpose:** Visual axis configuration node that generates structured test matrices for The Engine. Provides dropdown-based model selection, preset management, and legacy string output compatibility.

**In Plain Words:** Instead of typing comma-separated values, you click through a friendly UI, pick what each axis should vary, and the Driver feeds clean JSON straight into the Engine.

#### Overview

The Axis Driver replaces manual string entry for axis configurations with a rich UI featuring:
- **Three Axis Slots** (X, Y, Z) with preset selection
- **Model Dropdowns** for checkpoints, LoRAs, VAE, and CLIP models
- **Visual Item Management** with add/remove buttons
- **Style Configuration** panel for grid label customization
- **Dual Output** (structured JSON + legacy string format)

#### Wiring to The Engine

**Stupid-Simple Wiring:** Just connect X to X, Y to Y, Z to Z. That's it!

```
┌─────────────────────┐
│   Axis Driver       │
│   (h4_AxisDriver)   │
├─────────────────────┤
│ X: lora axis        │ ──→ axis_x
│ Y: cfg sweep        │ ──→ axis_y  
│ Z: (unused)         │ ──→ axis_z
└─────────────────────┘
           │
           │ Wire outputs directly to Engine inputs
           ↓
┌─────────────────────┐
│   The Engine        │
│   (h4_PlotXY)       │
├─────────────────────┤
│ axis_x_payload      │ ←── X axis from Driver
│ axis_y_payload      │ ←── Y axis from Driver
│ axis_z_payload      │ ←── Z axis from Driver (reserved)
└─────────────────────┘
```

**No Manual Mode Matching Required!** When you wire the Driver outputs to the Engine's axis inputs, the preset and configuration are automatically transferred. The manual `x_axis_mode` and `x_axis_values` widgets are ignored when Driver payloads are connected.

**Benefits:**
- ✅ No duplicate configuration
- ✅ No sync errors between nodes
- ✅ Driver is the single source of truth
- ✅ Change presets in Driver, Engine follows automatically

#### Supported Presets

| Preset | Description | UI Element | Example Values |
| --- | --- | --- | --- |
| `none` | Axis disabled | - | - |
| `prompt` | Prompt variations | Textarea | "cyberpunk style", "anime art" |
| `checkpoint` | Model swaps | **Dropdown** | "xl/illustriousXL_v1.safetensors" |
| `lora` | LoRA tests | **Dropdown + Strength** | "anime_style@0.8" |
| `vae` | VAE variations | **Dropdown** | "vae-ft-mse-840000-ema" |
| `clip` | CLIP encoder tests | **Dropdown** | "clip-vit-large" |
| `clip_vision` | Vision CLIP tests | **Dropdown** | "clip-vision-g" |
| `sampler` | Sampler comparison | Dropdown | "euler", "dpmpp_2m_sde" |
| `scheduler` | Scheduler tests | Dropdown | "karras", "exponential" |
| `cfg` | CFG scale sweep | Number input | 2.5, 4.0, 6.0 |
| `steps` | Step count tests | Number input | 20, 30, 40 |
| `denoise` | Denoise strength | Number input | 0.5, 0.75, 1.0 |
| `seed` | Seed variations | Number input | 8008135, 313378008135 |

#### Model Dropdown Features

When using `checkpoint`, `lora`, `vae`, `clip`, or `clip_vision` presets:

✅ **Automatic Model Discovery**  
- Fetches from ComfyUI's native API (`/object_info`)
- Works with **Stability Matrix** folder structures
- Works with **standard ComfyUI** installations
- Includes all configured model paths and subfolders

✅ **Smart Caching**  
- Models loaded once per session
- Alphabetically sorted for easy browsing
- Custom values preserved with "(custom)" label

✅ **LoRA Extras**  
- Strength slider (0-2.0, default 0.75)
- Persists per-item configuration

#### UI Controls

**Per-Axis Card:**
- **Preset Dropdown** — Choose what this axis tests
- **Add Item Button** — Create new entry
- **Item Rows** — Each with:
  - Label input (friendly name)
  - Value input (model dropdown or number/text)
  - Strength slider (LoRA only)
  - Remove button

**Global Controls:**
- **Show JSON** — Toggle raw configuration view
- **Axis Styling** — Collapsible panel for grid label customization
  - Font size, family, color
  - Background opacity
  - Label positioning
  - Custom axis labels

#### Grid Label Layout Modes

The styling deck now ships with a **Label Layout** selector that dictates how The Engine annotates its composite grid:

- `overlay` — Classic on-image badges. Labels float inside each tile with translucent backplates, ideal for quick inspection runs.
- `border` — Allocates a canvas margin and renders axis headers along the top (X) and left (Y). Use this to export clean comparison charts without obscuring pixels.
- `none` — Suppresses all labelling. Pick this when downstream tooling (e.g. PowerPoint, Notion) handles callouts for you.

Every Axis Driver payload carries the chosen layout to The Engine. When no layout is provided, the Python defaults continue to fall back to `overlay` for backward compatibility.

#### Configuration Format

**JSON State Structure:**
```json
{
  "axes": [
    {
      "slot": "X",
      "preset": "lora",
      "items": [
        {
          "label": "Anime Style",
          "value": "styles/anime_v2.safetensors",
          "strength": 0.8,
          "overrides": {}
        }
      ]
    }
  ],
  "style": {
    "font_size": 22,
    "font_family": "DejaVuSans",
    "font_colour": "#FFFFFF"
  }
}
```

**Legacy String Output:**  
Also emits newline-separated values for backward compatibility with existing workflows.

#### Node Size Behavior

The Axis Driver uses **fixed sizing** to prevent layout issues:
- Starts at default size (560x580)
- Manual resize works normally via corner drag
- No automatic growth from button interactions
- Content scrolls internally if needed

#### Best Practices

1. **One Driver Per Axis** — Use separate Axis Driver nodes for X, Y, and Z axes
2. **Match Presets** — Ensure Engine's axis mode matches the Driver's preset
3. **Test Incrementally** — Start with 2-3 items per axis before building large grids
4. **Use Labels** — Descriptive labels appear in grid annotations
5. **Save Configurations** — JSON can be copied/shared between workflows

#### Troubleshooting

| Issue | Solution |
| --- | --- |
| **Models not appearing in dropdown** | Check console for asset loading logs. Ensure models are in standard ComfyUI/Stability Matrix folders. |
| **Engine shows errors** | Verify axis mode matches driver preset (e.g., both set to "lora"). |
| **Custom value not working** | Ensure exact path/name matches ComfyUI's expectations. Check console for loading errors. |
| **Node layout issues** | Manually resize node to preferred dimensions. Size is saved per-node. |

---

### Debug-a-Tron 3000 — `h4_DebugATron3000`

**Purpose:** High-visibility inspector that mirrors signals while streaming structured logs. Designed for rapid troubleshooting of conditioning mismatches, latent anomalies, and model wiring.

```
 Upstream Model / Sampler ──▶ h4_DebugATron3000 ──▶ Downstream Workflow
            │                             │
            │                             ├─ Console logs + optional JSON/preview artefacts
            └─ Optional conditioning/latent/image lines map 1:1 to the node's slots
```

#### Modes

- `monitor` — Outputs `None` for every slot but leaves logging/diagnostics active (perfect for non-invasive tapping).
- `passthrough` — Clones incoming payloads (with type-aware deep copies) and forwards them downstream while logging.

#### Slot Catalogue

| Slot | Type | Behaviour |
| --- | --- | --- |
| `model_in` | MODEL | Diffusion model handle; used for VAE fallback and fingerprinting. |
| `clip_in` | CLIP | Text encoder payload. |
| `clip_vision_in` | CLIP_VISION | Optional vision CLIP branch. |
| `vae_in` | VAE | Explicit VAE connection. If absent, node harvests VAE from the model payload. |
| `conditioning_in` | CONDITIONING | Generic list/dict of conditioning entries. |
| `conditioning_positive_in` | CONDITIONING | Positive branch; flagged when missing if diagnostics enabled. |
| `conditioning_negative_in` | CONDITIONING | Negative branch; flagged similarly. |
| `latent_in` | LATENT | Latent dict or tensor. Snapshots/anomaly checks focus here. |
| `image_in` | IMAGE | Image batch for logging. |
| `mask_in` | MASK | Optional mask tensor. |

#### Console & Telemetry

Each connected slot produces a multi-line summary:

- Object descriptor (type, label, file name).
- Tensor stats (shape, dtype, device, min/max/mean/std).
- Conditioning previews (first three entries, prompt snippets).
- Warnings when conditioning branches are absent or empty.

#### Go Plus Ultra Arsenal

All toggled via boolean/string widgets inside the node (see [Go Plus Ultra Diagnostics](#go-plus-ultra-diagnostics) for details):

- Latent snapshots (first/mid/last)
- Preview image generation + optional disk caching
- JSON session logs (`debugatron_ultra_*.json`)
- Conditioning gap callouts
- Token previews (first entries per branch)
- Latent anomaly detection (NaN/Inf/high std/extreme magnitude)
- Model fingerprinting (SHA-1 digest of state_dict metadata)
- Custom watch expressions evaluated against the slot context
- Artefact caching toggle to persist or discard preview outputs

#### Internal Architecture Highlights

- **Metadata-Driven Wiring:** Slot definitions, tooltips, fallbacks, and display names originate from class attributes, enabling subclass overrides without code duplication.
- **Context Snapshotting:** All inputs + GO PLUS ULTRA flags are captured into a dictionary for JSON logging and watch expression evaluation.
- **Safe Cloning:** `_clone_payload_safely` selects the correct deep-copy routine per slot type so passthrough mode never mutates inbound payloads.
- **Watch Expression Sandbox:** Evaluates user expressions with access to `torch`, `np`, and slot variables while blocking Python builtins for safety.

#### Usage Flow

1. Drop the node into your graph where visibility is needed.
2. Choose `monitor` during early prototyping to prevent downstream disruptions.
3. Flip GO PLUS ULTRA to `True` and enable desired diagnostics once the graph is stable.
4. Inspect console output and optional JSON/preview artefacts after each run.

---

### Debug-a-Tron Router — `h4_DebugATronRouter`

**Purpose:** Mirrors the Debug-a-Tron feature set for dual-stream pipelines, duplicating every slot with explicit branch suffixes (`_a`, `_b`). Ideal for diffuser/refiner splits, text/image dual tracks, or comparative conditioning paths.

```
 Branch A payloads ──┐
                    │      ┌───────────────────────────────┐
 Branch B payloads ─┼────▶ │ h4_DebugATronRouter (A / B)    │ ──▶ Branch A passthrough
                    │      │  logs and GO PLUS ULTRA per   │ ──▶ Branch B passthrough
 Extra sensors ─────┘      │  branch, still in one node     │
                           └───────────────────────────────┘
```

#### Branch Slots

Each base inlet/outlet from the console node becomes two slots:

| Slot | Label | Notes |
| --- | --- | --- |
| `model_in_a` / `_b` | Branch A/B · Model | Allows independent model handles per branch. |
| `conditioning_positive_in_a` / `_b` | Branch A/B · Positive | Diagnostics track branch-specific conditioning health. |
| `latent_in_a` / `_b` | Branch A/B · Latent | Snapshots and anomaly checks annotate the originating branch. |
| … | … | All other slots follow the same pattern. |

#### Branch Intelligence

- **Per-Branch Summaries:** The router aggregates connection counts per branch and appends a human-readable report (e.g., `Branch A: 8/10 connected; missing -> Branch A · CLIP`).
- **Targeted VAE Fallbacks:** Each branch VAE inlet falls back to its corresponding model branch.
- **Passthrough-first Philosophy:** Default `mode` is `passthrough`, ensuring branch parity during live runs without extra configuration.
- **Branch-aware Diagnostics:** Latent snapshots, preview filenames, anomaly messages, and conditioning warnings all reference branch labels.

#### Operation

1. Insert the router where two lanes should be evaluated in parallel.
2. Leave `mode` in `passthrough` for branch mirroring, or switch to `monitor` if you only need telemetry.
3. Enable GO PLUS ULTRA to capture branch-tagged snapshots and JSON logs.
4. Consult console output for immediate branch health status.

---

### Debug Console — `h4_DebugATron3000Console`

**Purpose:** Output-node variant of the Debug-a-Tron that renders a neon HTML dossier while still mirroring payloads downstream. Ideal for live-stream overlays, QA reports, or storing a run transcript inside the ComfyUI workflow file.

```
 h4_DebugATron3000 ──▶ h4_DebugATron3000Console ──▶ downstream sockets (MODEL / VAE / etc.)
                             │
                             └─ html_log (STRING) ready for SavePrompt/Note nodes
```

#### Display Modes & Themes

- `display_mode` — `console_only`, `html_only`, or `both` depending on whether you need raw stdout, HTML, or a combination.
- `color_scheme` — curated palettes (`dark`, `light`, `matrix`, `cyberpunk`) to match your monitoring surface.
- `verbosity` — dial between `minimal`, `normal`, `verbose`, and `trace` to expand the detail level inside the HTML card.
- `show_timestamps` — toggle millisecond-precise stamps per slot update.

#### Inputs & Outputs

| Widget | Description |
| --- | --- |
| `mode` | Inherits `monitor`/`passthrough` routing from the base node. |
| `display_mode` | Controls whether HTML is generated, console logs are emitted, or both. |
| `color_scheme` | Palette selector for the rendered report. |
| `verbosity` | Governs how many tensor stats/metadata rows are included. |
| `show_timestamps` | Adds timeline markers to each section of the HTML log. |

| Output | Type | Contents |
| --- | --- | --- |
| `html_log` | `STRING` | Self-contained HTML snippet (embed-ready) summarising the run. |
| Remaining outputs | Mirror `h4_DebugATron3000` | All downstream sockets receive the same cloned payloads as the base node. |

#### Workflow

1. Drop the Console node near the end of your graph (it is an output node).
2. Select a colour scheme and desired verbosity.
3. Run your workflow. The HTML report appears in the right-hand panel; save it, embed it, or attach to bug reports.
4. Optional: pipe the HTML string into file-write nodes or custom Python for automated archiving.

---

### Seed Broadcaster — `h4_SeedBroadcaster`

**Purpose:** Deterministic seed generator with fixed, increment, or random modes. One output, unlimited fan-out—connect the pin to every sampler that needs to stay synchronized.

```
 h4_SeedBroadcaster ──▶ seed output ──▶ sampler A / sampler B / The Engine / …
```

#### Controls

| Widget | Description |
| --- | --- |
| `seed` | Anchor value. Used directly in `fixed` mode and as the manual override for other modes. |
| `mode` | Switch between `fixed`, `increment`, or `random`. |
| `increment_step` | Amount added whenever increment mode advances. Ignored in other modes. |
| `auto_advance` | When enabled, the node advances itself every execution (increments or rolls a new random). Disable to hold the current seed until you press **Randomize** or edit the value manually. |
| `random_digits` | Number of digits (1-12) to use when auto-generating random seeds. |

The UI also exposes a **Randomize** button beside the seed field (thanks to the `js/h4_ui.js` helper). Use it to roll a new seed instantly—perfect for `auto_advance = False` workflows.

#### Usage Tips

- Fan the output to as many samplers as you like; ComfyUI lets you multi-wire a single integer output.
- Toggle `auto_advance` off when you want to generate/approve seeds manually between runs.
- In increment mode, the node logs every emitted seed so you can track the sequence even when the UI anchor stays at the start value.
- Changing modes or editing the anchor seed resets the internal pointer so the next emission starts exactly where you expect.
- Pair with Execution Logger to capture the seed history alongside tensor metadata.

---

### The Varianator — `h4_Varianator`

**Purpose:** Rapid variation generator that reuses an existing latent, model bundle, and prompts to produce tightly scoped riffs.

**In Plain Words:** Feed it a latent (or Engine output), pick a denoise profile, and The Varianator will spin up a stack of alternates—complete with deterministic seeds, optional prompt jitter, and GO PLUS ULTRA telemetry when you need receipts.

```
Engine output ──▶ latent/model/clip/vae ──▶ h4_Varianator ──▶ stacked variations + latent batch
```

#### Quick Start Cheat Sheet

1. Wire The Engine's `latent`, `model`, and `vae` outputs into the matching Varianator sockets (all three are required). Bring the `clip` handle if you plan to re-encode prompts, enable jitter, or blend styles.
2. Set `variation_count` (start with 3) and choose a `variation_profile` (`moderate` is the safest first pass).
3. Pick a `seed_mode`: use `fixed` for gentle tweaks, `increment` for bracketed takes, or `random` for chaotic-but-repeatable variety.
4. Configure `prompt_jitter_*` or `style_mix_*` only when a CLIP handle or conditioning inputs are present; fallbacks in the widget panel rely on that encoder.
5. Optionally flip **GO PLUS ULTRA?!** to collect JSON/PNG artefacts, then run and inspect the `variations`, `latent_batch`, and `summary` outputs.

> TL;DR: one latent in, multiple polished riffs out with the full audit trail attached.

#### Feature Highlights

- **Profile-driven denoise bands** — `minimal`, `moderate`, and `major` map to curated 0.30–0.55 denoise windows so you can explore subtle-to-bold rewrites without guessing numbers.
- **Deterministic seed choreography** — choose `fixed`, `increment`, or `random` (anchored to `base_seed`), and the node logs every run so you can reproduce favourites later or restart a sequence midstream.
- **Prompt jitter & style mixing** — append weighted prompt fragments per variation or blend in a secondary conditioning stream/prompt with a single ratio slider, all guarded by CLIP-aware fallbacks.
- **CLIP-aware safeguards** — the node insists on a CLIP handle whenever it needs to re-encode text (prompt jitter, style mix, or prompt fallbacks) to prevent half-baked conditioning.
- **GO PLUS ULTRA hooks** — flip the switch to emit JSON dossiers and optional PNG previews for every variation (perfect for audits or sharing).

#### Inputs & Widgets

| Widget | Description |
| --- | --- |
| `variation_count` | How many alternates to render (1–16). Each run clones the provided latent, so upstream branches remain untouched. |
| `variation_profile` | Picks the denoise window. `minimal` enforces gentle edits, `major` allows aggressive remixing. |
| `seed_mode` | `fixed` reuses `base_seed`, `increment` walks upward per variation, `random` draws a deterministic sequence from the same anchor. |
| `base_seed` | Anchor seed used by the selected mode. |
| `steps` / `cfg` | Shared sampler parameters for every variation. |
| `sampler_name` / `scheduler_name` | Denoiser + schedule pair applied to each run. |
| `go_ultra` | Reveals diagnostics settings and enables JSON/preview capture. |
| `prompt_jitter_enabled` | When true, appends weighted prompt fragments for each variation. |
| `prompt_jitter_strength` | Default ± window when custom token ranges are omitted. |
| `prompt_jitter_tokens` | Optional token list (`token|min|max` per line) used by the jitter logic. |
| `style_mix_enabled` | Toggles blending against a secondary conditioning or prompt. |
| `style_mix_ratio` | Mix amount (0 = pure base prompt, 1 = pure style source). |
| `base_positive_prompt` / `base_negative_prompt` | Fallback text prompts used when conditioning inputs are absent or when prompt jitter/style mix requires re-encoding. |
| `style_mix_prompt` / `style_mix_negative_prompt` | Optional prompt strings when no style conditioning input is wired. |
| `ultra_json_log` / `ultra_cache_artifacts` | Control whether GO PLUS ULTRA writes JSON/PNG artefacts to disk. |

Mandatory connectors: `model`, `vae`, and `latent_in` (cloned straight from The Engine or another sampler). Optional sockets accept `clip`, `positive_in`, `negative_in`, plus style-conditioning fallbacks (`style_positive_in`, `style_negative_in`). Bring the CLIP handle or positive conditioning whenever you enable prompt jitter, style mixing, or rely on text fallback prompts.

#### Variation Profiles at a Glance

| Profile | Denoise Window | Best For |
| --- | --- | --- |
| `minimal` | 0.30–0.40 | Gentle pose tweaks, lighting nudges, fine colour work |
| `moderate` | 0.40–0.50 | Costume swaps, expression changes, medium restyles |
| `major` | 0.50–0.55 | Bold remixes, new compositions, aggressive camera moves |

Even the hottest profile caps at 0.55 so you retain recognisable structure instead of starting from noise.

#### Seed Modes in Plain English

| Mode | Behaviour | When to Use |
| --- | --- | --- |
| `fixed` | Every variation reuses `base_seed`; denoise alone defines the drift. | Img2img refinement, “keep the pose but adjust the vibe” scenarios. |
| `increment` | Seeds walk upward (`base_seed`, `base_seed + 1`, …). | Storyboards, iterative takes, pick-the-best-of-three workflows. |
| `random` | Deterministic PRNG seeded by `base_seed`; looks random but logs every roll. | Spray-and-pray ideation that you can still reproduce later via the summary log. |

#### Outputs

- `variations` (`IMAGE`) — Batch of decoded images (one per variation).
- `latent_batch` (`LATENT`) — Stack of latent tensors mirroring the image batch.
- `summary` (`STRING`) — Human-readable log enumerating seeds, denoise values, jitter tokens, and any saved artefact paths.

#### Workflow

1. Feed the node a latent (e.g., Engine output) plus the model/clip/vae handles you want to reuse.
2. Optionally connect positive/negative conditioning; otherwise provide fallback prompts for re-encoding.
3. Pick a denoise profile, seed mode, and variation count to define the exploration envelope.
4. Enable prompt jitter or style mix when you need extra texture across the batch.
5. (Optional) Flip **GO PLUS ULTRA?!** to emit JSON logs and preview PNGs for archival.
6. Run the workflow and inspect the stacked outputs or the text summary to cherry-pick favourites.

#### GO PLUS ULTRA Notes

When diagnostics are enabled the node records every variation (seed, denoise, jitter weights) in a timestamped JSON file and, when configured, saves the decoded preview PNGs alongside it. Artefacts land in `ComfyUI/temp/h4_varianator_ultra/` by default.

#### Prompt Jitter Format Example

```
# token|min|max — weights are additive
dramatic lighting|0.15|0.30
studio backlight|0.10|0.20
sparkle particles|0.00|0.18
```

Leave the list empty and the node instead applies ±`prompt_jitter_strength` around the base prompt for each variation.

#### Style Mix Recipes

- Wire a secondary conditioning payload into `style_positive_in`, set `style_mix_ratio` to `0.35`, and you get a 65/35 blend with the base prompt.
- No extra conditioning? Provide `style_mix_prompt` / `style_mix_negative_prompt` strings and the node encodes them with the incoming CLIP handle.
- Pair style mixing with `prompt_jitter_enabled` for controlled chaos: jitter keeps subtle differences, mix drags in the second style language.

---

### Execution Logger — `h4_ExecutionLogger`

**Purpose:** Lightweight console mirror that prints every connected payload with shape/type metadata, then returns a summarised string for downstream archiving.

```
 any payloads ──▶ h4_ExecutionLogger ──▶ log_summary (STRING)
  │                 │
  └─ optional slots └─ Console lines with types, shapes, and friendly labels
```

#### Inputs

| Widget | Description |
| --- | --- |
| `log_level` | Choose between `INFO`, `DEBUG`, or `WARNING` for emitted log lines. |
| `prefix` | Custom tag prepended to every message (`[EXEC]` by default). |
| `show_types` | When enabled, prints Python type names for each payload. |
| `show_shapes` | Adds tensor shapes and conditioning lengths to the console output. |

Optional sockets accept all common ComfyUI payloads (model, clip, vae, conditioning ±, latent, image, plus scalar/string taps). Leave unconnected slots empty—no noise is generated.

#### Output

- `log_summary` — Markdown-friendly plain text recapping the execution count and key metrics (tensor mins/maxes, conditioning lengths, scalar values).

#### Deployment Patterns

1. Drop Execution Logger at the tail of a complex graph; toggle `show_shapes` to confirm tensor agreements between branches.
2. Pair with the Console node: HTML handles stakeholder reporting, Execution Logger keeps the CLI loud for rapid iteration.
3. Feed `log_summary` into a note-taking node or custom webhook to maintain a run ledger.

---

## Go Plus Ultra Diagnostics

All Debug-a-Tron variants share the same control deck. Each toggle corresponds to a dedicated diagnostic routine inside `h4_DebugATron3000.route`.

| Control | Default | Effect |
| --- | --- | --- |
| `GO PLUS ULTRA?!` | `False` | Gatekeeper switch; when off, advanced widgets are physically removed from the UI and diagnostics are skipped. |
| `Snapshot: first step` | `True` | Capture the earliest latent tensor available. |
| `Snapshot: midpoint` | `False` | Capture the midpoint frame when history exists. |
| `Snapshot: final step` | `True` | Capture the most recent latent tensor. |
| `Generate preview image` | `True` | Decode snapshots into RGB previews whenever a VAE is connected. |
| `Write JSON session log` | `True` | Persist diagnostics to JSON (timestamped). |
| `Highlight missing conditioning` | `True` | Emit warnings when conditioning branches are absent/empty. |
| `Preview conditioning tokens` | `False` | Print first three token fragments per conditioning branch. |
| `Check for latent anomalies` | `True` | Scan tensors for NaN/Inf/extreme stats. |
| `Fingerprint attached models` | `False` | Hash model `state_dict` metadata for provenance tracking. |
| `Custom watch expression` | `""` | Python expression evaluated against slot context (`torch`/`np` available). |
| `Persist preview artifacts` | `True` | Keep preview PNG/JSON on disk (`False` deletes after logging). |

Artefacts land in the ComfyUI temp directory under `h4_debugatron_ultra`. Filenames include snapshot labels and branch suffixes.

---

## UI Companion (`js/h4_ui.js`)

The JavaScript extension auto-loads when the toolkit is present. Responsibilities include:

- **Widget Enhancement** — Applies descriptive placeholders/tooltips to Engine prompts, samplers, schedulers, etc.
- **Go Ultra UX** — Removes advanced widgets when GO PLUS ULTRA is disabled and restores them (with ordering intact) when re-enabled. Collapsed and expanded heights are preserved for consistent layout.
- **Axis Styling Bridge** — Keeps the Driver and Engine defaults in sync (including the new `label_layout` selector for overlay/border/none label modes).
- **Orientation Toggle** — Adds a dropdown to Debug-a-Tron nodes allowing horizontal or vertical layout; recalculates size on the fly.
- **Dynamic Sockets** — Maintains eight wildcard sockets per node, auto-typing based on connected links and spawning fresh blanks when needed.
- **Event Hooking** — Intercepts `onNodeCreated` and `onConnectionsChange` to inject the above enhancements without modifying core ComfyUI files.

No configuration is required—simply ensure ComfyUI can read assets beneath `h4_Plot/js/`.

---

## Tips & Best Practices

### Understanding Seed Behavior in Grids

**⚠️ CRITICAL:** The Engine's seed control affects EVERY cell in your grid differently depending on the mode!

| Seed Mode | Behavior | Use Case |
| --- | --- | --- |
| **`fixed`** | Uses the exact same seed for every grid cell | ✅ **img2img/high-res fix workflows** — maintains base composition across variations |
| **`increment`** | Seed + 1 for each cell (8008135, 8008136, 8008137...) | Testing with controlled variation |
| **`randomize`** | Completely random seed for each cell | ⚠️ **txt2img only** — creates entirely different images |

**Common Mistake:** Using `randomize` with img2img/latent input + low denoise (0.55) still produces **completely different images** because each cell gets a different seed! The denoise value is ignored when the seed changes.

**Solution:** When refining existing images (img2img workflow):
1. Set seed mode to **`fixed`**
2. Use the same seed as your input image
3. Now denoise works as expected: 0.55 denoise = 45% original + 55% variation

**Example Workflow:**
```
Initial Generation:
  KSampler → seed: 8008135, denoise: 1.0
  ↓
Refinement Pass:
  KSampler → seed: 8008135, denoise: 0.6
  ↓
Grid Testing (The Engine):
  seed: 8008135 (FIXED mode!)
  denoise: 0.55
  → Now you get variations that preserve the base image!
```

### Optimal Denoise Values

| Denoise | Effect | Best For |
| --- | --- | --- |
| **0.0 - 0.3** | Minimal changes, mostly detail refinement | Final polish, style transfer |
| **0.4 - 0.7** | ✅ **Sweet spot** for img2img/high-res fix | Balanced variation while keeping composition |
| **0.8 - 0.95** | Major changes, partial recomposition | Creative reinterpretation |
| **1.0** | Complete regeneration | txt2img generation |

### Wiring Best Practices

**Driver → Engine Wiring:**
```
✅ CORRECT:
  Driver.axis_x → Engine.axis_x_payload
  Driver.axis_y → Engine.axis_y_payload
  Driver.axis_z → Engine.axis_z_payload

❌ WRONG:
  Driver.axis_x → Engine.x_axis_values (string input)
  Mixing Driver outputs with manual mode dropdowns
```

**When to Use Manual vs Driver:**
- **Use Driver:** Complex multi-item axes, model sweeps, LoRA testing
- **Use Manual:** Quick single-axis tests, simple prompt variations

### Model Dropdown Tips

**Checkpoint Selection:**
- `<none>` — Error (no checkpoint loaded)
- `<checkpoint>` — N/A (checkpoint is required)
- **Actual models** — Use the dropdown to select

**VAE/CLIP Selection:**
- `<none>` — Uses nothing (can cause errors if required)
- `<checkpoint>` — ✅ **Default** — Uses the VAE/CLIP from the loaded checkpoint
- **Specific models** — Override with custom VAE/CLIP

**LoRA Strength:**
- `0.0` — LoRA disabled (still loaded but has no effect)
- `0.5` — Subtle effect
- `0.75` — ✅ **Default** — Balanced
- `1.0` — Full strength
- `1.5 - 2.0` — Exaggerated (can cause artifacts)

### Grid Composition Strategy

**Axis Assignment:**
- **X Axis (columns)** — Use for parameters you want to compare side-by-side (samplers, LoRAs)
- **Y Axis (rows)** — Use for parameters that define categories (CFG values, prompts)
- **Z Axis** — Reserved for future 3D grid support

**Grid Size Management:**
```
Small grids (2×2 to 4×4):   Fast iteration, broad testing
Medium grids (5×5 to 6×6):  Balanced detail vs time
Large grids (8×8+):         Comprehensive testing (slow!)

Memory usage: Rows × Columns × Model Size × Steps
Example: 6×6 grid = 36 images generated!
```

### Latent Input Workflows

**Three Ways to Provide Input:**

1. **Empty Latent (txt2img):**
   ```
   EmptyLatentImage → Engine.latent_in
   Result: Fresh generation at Engine's width/height
   ```

2. **Image Input (img2img):**
   ```
   LoadImage → Engine.image_in
   Result: Engine encodes to latent, then refines
   ```

3. **Latent Input (high-res fix/refinement):**
   ```
   KSampler → LatentUpscale → Engine.latent_in
   Result: Engine uses latent directly (no encoding)
   ```

**⚠️ Important:** When using latent/image input with denoise < 1.0, **ALWAYS use `fixed` seed mode** to preserve the base image!

### Axis Driver UI Tips

**Adding Items:**
1. Select preset from dropdown
2. Click "Add item"
3. Enter label (displays in grid)
4. Enter/select value (actual parameter)
5. Repeat for more test values

**Preset-Specific Tips:**
- **Checkpoint axis:** Use for A/B model testing
- **LoRA axis:** Test different LoRAs or strength values
- **Prompt axis:** Each item's value field supports full multi-line prompts
- **CFG/Steps axis:** Use incremental values (2.5, 5.0, 7.5 or 20, 30, 40)
- **Sampler axis:** Compare euler vs dpmpp_2m_sde vs others

**Show JSON Button:**
- Always forces a save before displaying
- Use to verify your configuration
- Copy-paste for sharing setups

### Prompt Engineering for Grids

**Using Prompt Axis:**
```json
{
  "label": "Quality: High",
  "value": "masterpiece, ultra-detailed, extreme detail, best quality, 8k, uhd"
}
{
  "label": "Quality: Low", 
  "value": "low quality, bad quality, draft"
}
```

**Combining with Base Prompt:**
```
Engine positive_prompt: "1girl, portrait, indoor"
+ Prompt axis value: "cinematic lighting, dramatic"
= Final prompt: "1girl, portrait, indoor, cinematic lighting, dramatic"
```

### Performance Optimization

**Memory Management:**
- Use `bypass_engine: true` to pass through without generating grid (testing wiring)
- Start with small grids (2×3) before scaling up
- Close other GPU applications before large grids
- The Engine clears CUDA cache between cells automatically

**Speed Tips:**
- Lower steps for iteration (20 steps vs 40)
- Use faster samplers for testing (euler, euler_ancestral)
- Disable preview generation in Debug-a-Tron during batch runs
- Use `denoise < 1.0` with latent input for faster refinement passes

### Common Workflows

**1. Sampler Comparison:**
```
X Axis: sampler (euler, dpmpp_2m_sde, dpmpp_2m, uni_pc)
Y Axis: cfg (4.0, 6.0, 8.0)
Result: 4×3 grid = 12 images testing sampler×CFG combinations
```

**2. LoRA Testing:**
```
X Axis: lora (LoRA A @ 0.75, LoRA B @ 0.75, LoRA C @ 1.0)
Y Axis: prompt ("anime style", "realistic", "painterly")
Result: 3×3 grid = 9 images testing LoRA×style combinations
```

**3. High-Res Fix Grid:**
```
Initial Generation:
  KSampler (steps: 40, cfg: 7, denoise: 1.0, seed: 8008135)
  ↓
Upscale:
  LatentUpscale (2x)
  ↓
Refinement Grid:
  Engine (seed: 8008135 FIXED, denoise: 0.55)
  X Axis: sampler (test different refinement samplers)
  Y Axis: cfg (find optimal refinement CFG)
```

**4. A/B Model Testing:**
```
X Axis: checkpoint (modelA.safetensors, modelB.safetensors)
Y Axis: prompt (various test prompts)
Z Axis: unused
Result: Compare how different models interpret same prompts
```

### Debug-a-Tron Pro Tips

**When to Use Monitor vs Passthrough:**
- **Monitor:** Diagnostic runs, troubleshooting, logging only
- **Passthrough:** Normal operation with optional logging

**GO PLUS ULTRA Use Cases:**
- Enable when tracking down NaN/Inf in latents
- Disable during production runs (saves disk space)
- Use `Watch expression` for custom tensor queries

**Preview Images:**
- Preview latents to verify they look reasonable
- Check for noise patterns, color shifts, or blank images
- Previews saved to `ComfyUI/temp/h4_debugatron_ultra/`

---

## Operational Playbooks

### Scenario A — Baseline Grid Generation

1. Configure Engine with prompts, sampler defaults, and axis presets (e.g., X axis = sampler, Y axis = CFG).
2. Leave Debug-a-Tron nodes disconnected for the initial smoke test.
3. Run once to verify outputs and labelled grid.
4. Introduce Debug-a-Tron 3000 post-run to inspect conditioning payloads; enable GO PLUS ULTRA for latent previews if discrepancies appear.

### Scenario B — Dual-Branch Diffusion

1. Duplicate your sampler branch (e.g., base diffuser vs. refiner) leading into separate pipelines.
2. Feed both into Debug-a-Tron Router, aligning branch A/B sockets accordingly.
3. Review branch summaries in the console; missing feeds are highlighted instantly.
4. Use JSON logs to archive branch-specific diagnostics alongside experiment metadata.

### Scenario C — Latent Forensics

1. Run Engine with GO PLUS ULTRA disabled to reproduce an anomaly.
2. Enable GO PLUS ULTRA on Debug-a-Tron 3000, toggle `Snapshot: final step`, `Generate preview image`, and `Check for latent anomalies`.
3. Re-run. Inspect console warnings and saved PNG/JSON artefacts in `h4_debugatron_ultra` to determine the fault.

---

## Troubleshooting & Support

| Symptom | Remedy |
| --- | --- |
| **Sampler rejects kwargs** | Ensure you are on the latest ComfyUI build; the compatibility shim adapts known signatures, but bleeding-edge changes may require toolkit updates. | 
| **Preview images missing** | Confirm a VAE is connected or that the model exposes a decodable VAE. If GO PLUS ULTRA caching is disabled, expect previews to be ephemeral. |
| **Conditioning warnings** | Check upstream graph wiring; the debugger flags empty conditioning lists to prevent silent CFG issues. |
| **Watch expression errors** | Expressions execute in a restricted environment; avoid referencing `__builtins__`. Console logs will echo the exception. |
| **UI widgets shift** | The UI script intentionally removes Go Ultra controls when disabled. Re-enable the toggle to restore them. |

If issues persist, gather console logs (the toolkit prints namespace-prefixed entries like `[h4 Toolkit::h4_DebugATron3000]`) and open a GitHub issue.

---

## Development Notes

- `_invoke_sampler_with_compatibility`, `_extract_model_sampling`, and `_ensure_ultra_directory` are prime extension points when aligning with future ComfyUI changes.
- Slot metadata is centralised; subclass overrides only need to redefine `SLOT_DEFINITIONS`, `SLOT_TOOLTIPS`, `VAE_MODEL_FALLBACKS`, and `BRANCH_DISPLAY_NAMES`.
- The router inherits `route` directly from the base class—branch behaviour is purely data-driven.
- JavaScript enhancements rely on standard ComfyUI extension hooks and do not monkey-patch core libraries.

### Local Validation Cycle

1. Modify Python modules.
2. Run `python -m py_compile h4_Plot/nodes.py`.
3. Optionally execute targeted ComfyUI workflows for runtime assurance.

---

## Release Intel & Versioning

- Update `TOOLKIT_VERSION`, `PLOT_NODE_VERSION`, and `DEBUG_NODE_VERSION` in `h4_Plot/nodes.py` when shipping releases.
- Document major changes inside `h4_Plot/docs/h4_toolkit_brief.html` (already acts as the canonical change log and architecture brief).
- Consider tagging Git releases aligned with version constants for traceability.

---

## Appendix: Function Index

| Module | Key Functions/Classes | Summary |
| --- | --- | --- |
| `h4_Plot/nodes.py` | `h4_PlotXY`, `h4_DebugATron3000`, `h4_DebugATronRouter`, `_invoke_sampler_with_compatibility`, `_collect_latent_snapshots`, `_tensor_anomalies`, etc. | Core logic for sampling, diagnostics, and metadata-driven routing. |
| `h4_Plot/js/h4_ui.js` | `toggleUltraWidgets`, `ensureDynamicSockets`, `applyOrientationLayout`, extension registration | UI/UX companion for nodes. |
| `h4_Plot/__init__.py` | `ensure_dependencies`, status banner, node exports | Dependency bootstrap and ComfyUI integration. |

| `h4_Plot/docs/h4_toolkit_brief.html` | HTML dossier | Narrative architecture and remediation history. |


