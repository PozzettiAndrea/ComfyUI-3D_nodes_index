# babydjacNODES

Custom ComfyUI nodes for prompting, analysis, latent setup, LoRA loading, taglist tools, and utility workflows.

## Install

1. Clone this repository into `ComfyUI/custom_nodes/` as `babydjacNODES`.
2. Restart ComfyUI after Python changes.
3. Hard-refresh the browser after JavaScript changes.

## Node Index

Total nodes: **25**

### `babydjacNODES/Analyze`

- **Grok Flux Prompt Optimizer** (`GrokFluxPromptOptimizer`): Optimizes an existing Flux prompt from image context and user edit instructions. ([docs](docs/nodes/GrokFluxPromptOptimizer.md))
- **Grok Image Describer Pro** (`NSFWGrokDescriberPro`): Returns expanded descriptive prompt outputs from an image and instruction set. ([docs](docs/nodes/NSFWGrokDescriberPro.md))

### `babydjacNODES/Latents/Interactive`

- **Latent Size Controller** (`InteractiveEmptyLatent`): Creates an empty latent with interactive resolution controls (graph/histogram UI + model-aware presets). ([docs](docs/nodes/InteractiveEmptyLatent.md))

### `babydjacNODES/Loaders`

- **LoraFcKingLoader** (`LoraFcKingLoader`): Loads and stacks multiple LoRA files on top of a base model and CLIP, in slot order. ([docs](docs/nodes/LoraFcKingLoader.md))

### `babydjacNODES/Prompting`

- **Qwen Image Prompter** (`QwenImagePrompter`): Generates image prompts using a Qwen-style prompt strategy and formatting. ([docs](docs/nodes/QwenImagePrompter.md))

### `babydjacNODES/Prompting/Flux`

- **Flux Dual Prompt Node (Grok)** (`FluxDualPromptNode`): Calls Grok to produce dual Flux prompts (short CLIP-style + long descriptive prompt). ([docs](docs/nodes/FluxDualPromptNode.md))
- **Flux Lambda Prompter** (`FluxLambdaPrompter`): Uses a Lambda-hosted model endpoint to generate refined Flux prompt pairs. ([docs](docs/nodes/FluxLambdaPrompter.md))
- **Flux Lifestyle Prompt Node** (`FluxLifestylePromptNode`): Enhances lifestyle photo prompts through Grok for Flux-focused generation. ([docs](docs/nodes/FluxLifestylePromptNode.md))
- **Flux Prompt Builder** (`FluxPromptBuilder`): Constructs Flux-ready positive and negative prompts using local templates and safety controls. ([docs](docs/nodes/FluxPromptBuilder.md))

### `babydjacNODES/Prompting/PonyXL`

- **Grok PonyXL Prompter** (`GrokPonyXLPrompter`): Analyzes an input image with Grok Vision and returns PonyXL-style prompt/negative tags. ([docs](docs/nodes/GrokPonyXLPrompter.md))
- **Grok to PonyXL Prompt** (`NSFWGrokToPonyXL`): Transforms freeform prompt text into PonyXL-friendly positive/negative/tag outputs. ([docs](docs/nodes/NSFWGrokToPonyXL.md))

### `babydjacNODES/Prompting/WAN-2.2`

- **WAN 2.2 Prompt Studio** (`WAN22PromptStudioNode`): Generates WAN 2.2 oriented prompt sets for video/image workflows. ([docs](docs/nodes/WAN22PromptStudioNode.md))

### `babydjacNODES/Prompting/Z-Image`

- **Z-Image Prompt Engineer** (`ZImagePromptEngineer`): Builds a structured Z-Image prompt with positive/negative text and generation settings. ([docs](docs/nodes/ZImagePromptEngineer.md))
- **Z-Image Turbo Prompt Engineer** (`ZImageTurboPromptEngineer`): Fast prompt builder for Z-Image Turbo workflows with simplified controls. ([docs](docs/nodes/ZImageTurboPromptEngineer.md))

### `babydjacNODES/Taglists`

- **Safe Tag List Prompt** (`SafeTagListPromptNode`): Converts tag lists into cleaner prompt text with safety-oriented defaults. ([docs](docs/nodes/SafeTagListPromptNode.md))
- **Taglist Prompt** (`TagListPromptNode`): Direct tag list prompt node that inherits the SafeTagListPromptNode behavior. ([docs](docs/nodes/TagListPromptNode.md))
- **Template Driven Taglist** (`TemplateDrivenTagListPromptNode`): Builds prompt text from tag lists with a configurable template layer. ([docs](docs/nodes/TemplateDrivenTagListPromptNode.md))

### `babydjacNODES/Utils`

- **Grok Prompt Fusion Pro** (`NSFWGrokFusionPro`): Combines and weights multiple prompt fragments with style presets and annotation output. ([docs](docs/nodes/NSFWGrokFusionPro.md))
- **HTTP JSON** (`HTTPJsonNode`): Makes HTTP requests and returns response text for API-backed workflows. ([docs](docs/nodes/HTTPJsonNode.md))
- **No-Repeat Picker** (`NoRepeatPickerNode`): Selects items from a multiline list while persisting no-repeat history. ([docs](docs/nodes/NoRepeatPickerNode.md))
- **Prompt Merge** (`PromptMergeNode`): Merges multiple tag lists with optional dedupe, case normalization, sorting, and truncation. ([docs](docs/nodes/PromptMergeNode.md))
- **Taglist Sanitizer** (`TaglistSanitizerNode`): Sanitizes tag lists (dedupe, lowercase, strip weights, sort). ([docs](docs/nodes/TaglistSanitizerNode.md))
- **Text Cache** (`TextCacheNode`): Small key/value text cache node with get/set/delete operations. ([docs](docs/nodes/TextCacheNode.md))
- **Weight Adjust** (`WeightAdjustNode`): Applies weight scaling rules across weighted and unweighted prompt tags. ([docs](docs/nodes/WeightAdjustNode.md))

### `babydjacNODES/Utils/Batching`

- **Prompt Rotator (Dynamic Batch)** (`DynamicPromptBatcher`): Collects prompt inputs into a list output for batched or rotating workflows. ([docs](docs/nodes/DynamicPromptBatcher.md))

## Notes

- Node colors are assigned by top-level category in the frontend extension.
- Several nodes call external APIs (xAI/Lambda/HTTP). Review your API keys and usage policies before production use.
- For node-by-node details, use the linked docs in `docs/nodes/.`
