# Militant Hitchhiker's Switchblade Pack (v1.3)

Militant Hitchhiker's Switchblade Pack is a set of multi-function custom nodes for ComfyUI, covering text processing, prompt enhancement, model analysis/quantisation, and advanced scheduling/sampling.

This release reflects Switchblade v1.3 (as initialised in the loader) and includes new nodes for GOD/ARC/ODE EMA, Flux quant, and a Groq-powered prompt enhancer.

## Installation

1. Open a terminal/PowerShell.
2. Navigate to your ComfyUI `custom_nodes` directory.
3. Clone the repo:
   ```bash
   git clone https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack.git
   ```
4. Restart ComfyUI.

Notes
- The Groq node will auto-install the `groq` Python package on first run if missing.
- Loaded modules are defined in `__init__.py` and a `nodes.log` file is written at startup for quick discovery.

## Configuration (Groq)

If you plan to use the Groq API Prompt Enhancer, set your API key and optional default system prompt in `modules/groq_config.json`.

- `api_key`: your Groq API key
- `system_prompt`: optional default system prompt used unless overridden per-node

You can also provide an `override_system_prompt` input on the node to temporarily replace the default.

## Nodes

### Text Processing

#### Text Appender (`TextAppender_v2`)
Concatenate up to five text inputs; control how they’re joined and optionally append the result to a file in ComfyUI’s output directory.

- Inputs (optional): `text1`..`text5`, `input_delimiter` (e.g. `\n`), `output_delimiter` (e.g. `\n`), `output_file` ("none" to disable)
- Output: `STRING` (the concatenated text)
- Category: `MilitantAI/Switchblade/Text Processing`

Typical use
1. Provide any of `text1`..`text5`.
2. Use `\n` to represent newlines for delimiters.
3. Set `output_file` to a filename to append the result; otherwise it only returns the text.

#### Prompt Generator (Dictionary) (`IntegratedRandomPromptGenerator`)
Randomly selects one item from up to four dictionary files and joins them.

- Dictionaries folder: `ComfyUI/input/Dictionaries` (recursively scanned)
- Inputs: `dict1_file`..`dict4_file` (or "none"), `enable_dict1`..`enable_dict4`, `dict1_delimiter`..`dict4_delimiter` (default `;`), `output_delimiter` (default `, `), `seed`
- Output: `STRING`
- Category: `MilitantAI/Switchblade/Text Processing`

Tip: Use `;` as the default item delimiter inside your `.txt` dictionaries.

#### Groq API Prompt Enhancer (`GroqAPIPromptEnhancer`)
Send text to Groq chat models to enhance prompts.

- Models: `gemma2-9b-it`, `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`
- Inputs: `model`, `text`, optional `override_system_prompt`
- Output: `STRING` (enhanced text)
- Config file: `modules/groq_config.json`
- Category: `MilitantAI/Switchblade/Text Processing`

### Model Insight and Utilities

#### Model Analyser (`ModelAnalyserNode`)
Analyses a model’s state dict and returns a JSON summary.

- Input: `model`
- Output: `STRING` (JSON: structure, size, blocks, dtypes, totals)
- Category: `MilitantAI/Switchblade/Model Merging`

#### Flux Quant Node (`FluxQuantNode`)
Converts the model’s tensors to a selected precision, analyses them, and saves the processed model to ComfyUI’s output directory.

- Inputs: `model`, `precision` (`auto`, `float32`, `float16`, `bfloat16`, `float8_e5m2`, `float8_e4m3fn`)
- Output: `STRING` (analysis JSON; also prints save status)
- Saved file name: `<ckpt_or_unknown>_<precision>.safetensors`
- Category: `MilitantAI/Switchblade/Model Merging`

### Generation (Schedulers and Samplers)

#### ARC Scheduler (`ARC Scheduler`)
Deterministic, gently warped descendent schedule; returns `SIGMAS` suitable for advanced samplers.

- Inputs: `model`, `steps`, `denoise`
- Output: `SIGMAS`
- Category: `MilitantAI/Switchblade/Generation`

#### GOD Scheduler (Advanced)
Produces a baseline descending `SIGMAS` schedule (high → low) with denoise control.

- Inputs: `model`, `steps`, `denoise`
- Output: `SIGMAS`
- Category: `MilitantAI/Switchblade/Generation`

#### GOD Sampler (Advanced)
Returns a `SAMPLER` wrapping a GOD-Flow sampler with synergy-adapted step behaviour.

- Output: `SAMPLER`
- Category: `MilitantAI/Switchblade/Generation`

#### GOD Sampler (Advanced) Ext.
Like the GOD Sampler (Advanced) but with a `god_strength` control.

- Inputs: `god_strength`
- Output: `SAMPLER`
- Category: `MilitantAI/Switchblade/Generation`

#### ODE EMA Sampler
Detail-aware ODE sampler with EMA-stabilised cone shaping and late-step detail emphasis.

- Inputs: `stats_downsample`, `detail_gain_max`, `detail_power`, `detail_schedule_power`
- Output: `SAMPLER`
- Category: `MilitantAI/Switchblade/Generation`

### Typical Wiring Examples

- Use `GOD Scheduler (Advanced)` or `ARC Scheduler` → connect to `KSampler (Advanced)` `sigmas` input.
- Use `GOD Sampler (Advanced)` or `GOD Sampler (Advanced) Ext.` → connect to `SamplerCustom` `sampler` input.
- Use `ODE EMA Sampler` → connect to `SamplerCustom` `sampler` input.
- Use `Flux Quant Node` and `Model Analyser` → connect their `model` input to your loaded model.
- Use `Text Appender` and `Prompt Generator (Dictionary)` for pre/post text tasks in your workflow.

## Contributing

Contributions are welcome! Please open an issue or PR on the [GitHub repository](https://github.com/MilitantHitchhiker/MilitantHitchhiker-SwitchbladePack).

## Changelog

v1.3
- Added: `GOD Scheduler (Advanced)`, `GOD Sampler (Advanced)`, `GOD Sampler (Advanced) Ext.`, `ODE EMA Sampler`.
- Added: `ARC Scheduler` for deterministic ARC-warped schedules.
- Added: `Flux Quant Node` for precision conversion + analysis + save.
- Added: `Groq API Prompt Enhancer` with `modules/groq_config.json` config.
- Updated: `Text Appender` now uses `input_delimiter` and `output_delimiter` and writes to ComfyUI output when `output_file` is set.
- Updated: `Prompt Generator (Dictionary)` defaults to `;` as item delimiter and scans `ComfyUI/input/Dictionaries` recursively.
- Renamed: `arc_lr_scheduler.py` → `ARC_scheduler.py`.
- Note: `model_save.py` (Save Flux Model v2) exists but is disabled in `__init__.py` in this release.

## License

MIT