# ComfyUI Nox Prompter

Modular prompt-engineering tools for ComfyUI that turn cinematic ideas into production-ready text blocks, complete with palette controls, safety rails, and workflow guidance.

> **TL;DR**: Drop the folder into `ComfyUI/custom_nodes`, restart ComfyUI, and look for the **NoxPrompter** category. Need to verify the install? Run `python test_nodes.py` from this directory.

![Nox Prompter nodes in ComfyUI](https://github.com/user-attachments/assets/480a1bbc-fa04-4722-80bc-88f3ccc4918f)

## Highlights

- **20 purpose-built nodes** spanning builders, character design, wardrobe, lighting, camera direction, NSFW safeguards, streaming prompts, and pipeline organization.
- **Formula-driven Wan 2.2 builder** with curated motion, composition, and stylization vocabularies plus inline overrides and randomization; pair with Lighting Master for centralized lighting control.
- **Preset-friendly companions** – every major node supports save/load/list actions so you can build libraries of looks, poses, palettes, and camera moves.
- **Consistency tooling** – Narrative Weaver, Palette Mixer, Organizer, and Pipeline Combiner keep every fragment aligned, with automatic contradiction warnings.
- **Safety-first NSFW workflow** – mature prompts include baseline negatives, safety notes, and an NSFW AIO fusion node to merge designer + action outputs responsibly.
- **Single-script smoke test** – `test_nodes.py` exercises the entire suite, validating node registration, preset behaviors, and safety defaults before you hit render.

## Node Catalog

### Onboarding & Organization
- `NoxPromptUsageGuide` *(NoxPrompter/Guides)* – Generates quickstart or extended documentation (workflow steps, pairings, safety reminders) directly inside ComfyUI.
- `NoxPromptOrganizer` *(NoxPrompter/Utility)* – Collates fragments from multiple nodes into a readable, ordered prompt, highlights missing sections, and produces a checklist.

### Core Builder Stack
- `NoxPromptBuilder` *(NoxPrompter/Builders)* – Wan 2.2 style prompt assembler with basic/advanced formulas, keyword styling, randomization, preset storage, and pass-through inputs for Lighting Master and Camera Master outputs.
- `NoxPromptPaletteMixer` *(NoxPrompter/Companions)* – Produces palette override strings, custom keyword bundles, and usage notes from cinematic mood profiles.
- `NoxPromptNarrativeWeaver` *(NoxPrompter/Companions)* – Outputs subject, scene, motion, hook, and descriptor text blocks from archetype + tone selectors.
- `NoxPromptCombiner` *(NoxPrompter/Text)* – Blends up to three prompts via concatenate, alternate, blend, or weighted strategies.
- `NoxPromptEnhancer` *(NoxPrompter/Text)* – Adds emphasis, quality tags, and style packs (artistic, photorealistic, cinematic, fantasy, sci-fi, portrait) to any prompt.
- `NoxPromptAnalyzer` *(NoxPrompter/Analysis)* – Reports word count, complexity, detected style, sentiment, and optional quick critiques for the provided prompt.

### Character & Styling Suite
- `NoxPromptCharacterCreator` *(NoxPrompter/Characters)* – Builds lore-rich hero bios, story hooks, and prompt fragments with presetable archetypes and traits.
- `NoxPromptHumanDesigner` *(NoxPrompter/Characters)* – Adult anatomy guardrails plus detailed face, body, skin, eye, and pose descriptors with consent messaging.
- `NoxPromptWardrobeDesigner` *(NoxPrompter/Characters)* – Describes garments, materials, accessories, motion considerations, and styling notes for any wardrobe concept.

### Cinematic Direction
- `NoxPromptActionDirector` *(NoxPrompter/Direction)* – Crafts kinetic action prompts, summaries, and director notes with camera, tempo, props, and risk guidance.
- `NoxPromptCameraMaster` *(NoxPrompter/Direction)* – Aggregates shot size, lensing, motion, rigging, palette, and safety notes into a single camera prompt stream for Builder and Organizer nodes (**alias:** `NoxPromptCameraLanguage` for legacy graphs).
- `NoxPromptLightingMaster` *(NoxPrompter/Direction)* – Consolidates all lighting source, quality, and time-of-day palettes into one node and outputs lighting setups, mood notes, and technical rigging reminders for complex scenes.
- `NoxPromptCamz` *(NoxPrompter/Direction)* – Streaming-focused prompt generator with persona, stage, overlay, and safety mentions for creator economy workflows.

### Posing & Staging
- `NoxPromptPoseMaster` *(NoxPrompter/Posing)* – Directs all-ages pose direction with camera, lighting, set, and energy guidance plus baseline negatives and coaching reminders.

### NSFW Toolkit (Adults Only)
- `NoxPromptNSFWDesigner` *(NoxPrompter/NSFW)* – Safely assembles sensual prompts with wardrobe, pose, lighting, and explicitness controls plus baseline negatives.
- `NoxPromptNSFWPoseMaster` *(NoxPrompter/NSFW)* – Directs adult-only posing with camera, lighting, and heat controls while surfacing safety briefs and negative guidance.
- `NoxPromptNSFWActionDirector` *(NoxPrompter/NSFW)* – Produces choreography-focused NSFW action prompts, summaries, and consent-oriented safety notes.
- `NoxPromptNSFWAIO` *(NoxPrompter/NSFW)* – Fuses designer + action outputs into a single prompt/negative/safety stack while deduplicating keywords and warnings.

### Pipeline Assembly
- `NoxPromptPipelineCombiner` *(NoxPrompter/Pipeline)* – Weaves every module’s outputs into a production-ready master prompt, negative list, step order, and reference notes with contradiction detection.

## Installation

| Method | Steps |
| --- | --- |
| **ComfyUI Manager** | Search for **“Nox Prompter”**, click **Install**, restart ComfyUI. |
| **Git clone (recommended)** | `cd /path/to/ComfyUI/custom_nodes` → `git clone https://github.com/jamesk9526/ComfyNoxPrompter.git` → restart ComfyUI. |
| **Manual download** | Download ZIP → extract to `ComfyUI/custom_nodes/ComfyNoxPrompter/` → restart ComfyUI. |

After the restart, right-click the canvas and confirm a **NoxPrompter** category with the nodes listed above. If something is missing, see the [Troubleshooting](#troubleshooting) section.

## Quickstart Workflow

1. **Ask the Usage Guide** – Drop `NoxPromptUsageGuide`, set `detail_level = Extended`, and review the generated workflow and safety pointers in ComfyUI.
2. **Define your hero** – Chain `NoxPromptCharacterCreator → NoxPromptHumanDesigner → NoxPromptWardrobeDesigner` to lock identity, anatomy, and wardrobe language.
3. **Seed the narrative** – Use `NoxPromptNarrativeWeaver` for subject/scene/motion text, and `NoxPromptPaletteMixer` for palette overrides + keywords.
4. **Assemble the master prompt** – Feed the outputs into `NoxPromptBuilder` (Advanced Formula) and optionally enable `randomize_missing` with a seed for repeatable variations.
5. **Polish or enhance** – Run the builder result through `NoxPromptEnhancer` or `NoxPromptCombiner` to layer styles, emphasis, or alternate prompts.
6. **Add direction** – `NoxPromptActionDirector` and/or `NoxPromptLightingMaster` create dedicated camera + lighting clauses; `NoxPromptCamz` covers streaming personas.
7. **Safety-check NSFW work** – For mature scenes, route through `NoxPromptNSFWDesigner` and optionally `NoxPromptNSFWActionDirector`, then merge with `NoxPromptNSFWAIO`.
8. **Finalize and organize** – Use `NoxPromptPipelineCombiner` to merge every fragment into a single prompt package, then optionally tidy with `NoxPromptOrganizer` before sending to your sampler.

## Detailed Usage

### Builder & Companion Trio
- **Narrative Weaver → Palette Mixer → Prompt Builder** gives you richly described subject/scene/motion text plus cinematic palette overrides in seconds.
- Set `keyword_style` to **auto** for labeled clauses, **inline** for free-flow descriptions, or **compact** for dense Wan 2.2 strings.
- Turn on `randomize_missing` when dropdowns are left at “None”; the combination of curated vocabularies and seeded randomness is great for ideation batches.

### Character & Wardrobe Stack
- The character trio outputs three synchronized strings: a hero prompt, a formatted sheet, and story hooks. Feed the prompt into the Builder, keep the sheet for production notes, and park the hooks in your project management tool.
- `NoxPromptHumanDesigner` automatically appends adult-consent language and negative prompts. You can substitute your own copy via `consent_language` and `safety_addendum` fields.
- Wardrobe Designer exports the hero look, a bullet list of styling notes, and an accessories-only string. Route the prompt into the Builder or Combiner and hand the accessory list to your prop artist.

### Directional Nodes
- `NoxPromptPoseMaster` handles all-ages pose staging. It combines pose profiles, camera framing, lighting, set design, and energy cues, then outputs prompt/negative/brief/guidance strings with coaching and comfort reminders.
- `NoxPromptActionDirector` and `NoxPromptNSFWActionDirector` share a schema: defaults cover preset combos, while every control offers a “Custom Input” field when you need bespoke language.
- Lighting Master produces three parallel outputs (prompt, mood notes, technical notes). Feed the prompt to the Builder or Pipeline Combiner, and keep the technical notes for your lighting checklist.
- `NoxPromptCamz` focuses on creator economy scenarios (persona, stage theme, overlays). Disable `include_negative_baseline` if downstream automation already injects safety negatives.

### NSFW Flow (Adults Only)
- Keep `include_negative_baseline` and `include_safety_note` enabled unless you have verified policy tooling downstream. They block underage terms, coercion, non-consensual language, and extreme anatomy references by default.
- `NoxPromptNSFWPoseMaster` focuses on staging: it merges pose profiles with camera framing, lighting, heat, and explicitness controls, then outputs a dedicated prompt/negative/brief trio plus safety notes. Use it to lock pose direction before layering wardrobe or action cues.
- `NoxPromptNSFWActionDirector` adds choreography and consent beats. Hand its `action_prompt` to the Builder or Combiner, and archive the `safety_notes` for compliance logs.
- `NoxPromptNSFWAIO` merges designer + director outputs, deduplicates negatives, and ensures safety notes stay intact. It also accepts extra positives/negatives if you have studio-specific rules.

### Pipeline Assembly & Organization
- `NoxPromptPipelineCombiner` stitches builder output, character data, wardrobe pieces, narrative text, action notes, lighting cues, NSFW notes, and custom strings into a single master prompt. It also produces:
   - Aggregated negative list (merging builder, enhancer, NSFW baselines, etc.).
   - Pipeline order referencing every node used (matches the Usage Guide’s recommendations).
   - Reference notes grouped by theme (camera, motion, palette, safety) with contradiction warnings when descriptors disagree.
- `NoxPromptOrganizer` is perfect for presentation. Select a structure mode (Builder-first, Narrative-first, Lighting-first), and it will output a formatted prompt, a missing-section list, and a quick overview for review sessions.

### Preset Manager (Shared Behavior)
- Most nodes expose `preset_action` (`none`, `save`, `load`, `list`) and `preset_name`. These hook into the shared `PresetManager` to store JSON presets under `ComfyNoxPrompter/presets/<node_name>/`.
- Typical flow:
   1. Configure the node, set `preset_action = save`, choose a `preset_name`, and execute once.
   2. Switch to `preset_action = load` (or `list`) to recall the configuration on future runs.
- Presets are simple text files—commit them alongside your project or share them with teammates.

## Verification & Tests

Run the bundled regression script any time you update the repository or tweak presets:

```powershell
cd C:\Users\James\Documents\GitHub\ComfyNoxPrompter
python test_nodes.py
```

The script validates node registration, prompt outputs, preset save/load flows, safety baselines, and the pipeline sequence. All tests should pass before shipping to production pipelines.

## File Structure

```
ComfyNoxPrompter/
├── __init__.py                # ComfyUI entry point
├── NoxPromptNode.py           # Legacy aggregator with resilient imports
├── INSTALLATION.md            # Install cheat sheet
├── README.md                  # You are here
├── test_nodes.py              # Offline regression tests
├── examples/README.md         # Sample workflows and diagrams
├── noxprompter/               # Modular package (common utilities, constants, node modules)
└── LICENSE
```

## Troubleshooting

- **Nodes missing after restart** – Make sure the folder name is exactly `ComfyNoxPrompter`. Restart ComfyUI completely after copying or updating.
- **`ModuleNotFoundError: noxprompter`** – The aggregator now injects its path automatically, but if you renamed folders, ensure `NoxPromptNode.py` sits beside the `noxprompter/` package.
- **Preset files not saving** – Verify the process has write access to `ComfyNoxPrompter/presets`. Presets are stored per node (e.g., `presets/prompt_builder/<name>.json`).
- **Negative prompts missing safety terms** – Double-check the NSFW nodes’ baseline toggles and avoid trimming the negative string downstream.
- **Need examples** – See `examples/README.md` for wiring diagrams and step-by-step walkthroughs.

## Contributing & Support

- Open issues or feature ideas on the [GitHub tracker](https://github.com/jamesk9526/ComfyNoxPrompter/issues).
- Run `python test_nodes.py` before submitting a pull request so maintainers can reproduce your results quickly.
- For private questions or collaboration, feel free to open a discussion thread in the repository.

## License

Released under the MIT License. See `LICENSE` for full terms.

---

**Happy prompting! Build cinematic stories, stay consistent, and keep every node in sync.**
