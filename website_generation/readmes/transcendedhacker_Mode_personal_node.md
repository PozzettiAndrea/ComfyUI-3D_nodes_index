# Mode_personal_node

A structured prompt-generation engine for SDXL and Flux diffusion models, implemented as a ComfyUI custom node.

## Overview

This system provides deterministic, schema-driven prompt assembly for image generation workflows. It separates engine logic, structural contracts, and content libraries to ensure long-term maintainability and extensibility without code modification.

The architecture is designed for:
- Users new to diffusion models seeking predictable, safe defaults
- Advanced users requiring explicit control over composition and intent
- Researchers building reproducible image generation pipelines
- Community contributors extending content libraries without engine changes

## Design Principles

**Separation of Concerns**: Engine, schema, and libraries are strictly independent. Content expansion never requires engine modification.

**Explicit Intent Modeling**: Exposure level and camera relationship are declared via intent flags with safe defaults (clothed, facing camera). Explicit content is opt-in only.

**Token Priority Ordering**: Prompt blocks assemble in priority order (structural → atmospheric → technical) to respect model token weighting behavior.

**Schema-Driven Validation**: All libraries conform to a declarative schema contract, enabling safe human authorship and extension.

**Deterministic Behavior**: No randomness, no hidden logic. Identical inputs produce identical outputs.

## Architecture

The system consists of three independent layers:

**Engine Layer** (`engine/composer.py`): A deterministic Python interpreter that loads schema contracts, processes conforming library data, and assembles prompts according to model-specific ordering constraints. Contains no domain knowledge or hardcoded categories.

**Schema Layer** (`schema/connector.json`): A declarative contract defining dropdown blocks, ordering rules, intent flags, addon merge policies, weighting, and fallback behaviors. Evolves only when structural requirements change.

**Library Layer** (`libraries/*.json`): Pure JSON datasets containing selectable options organized by schema-defined blocks. Content-only, with no logic, weights, or UI directives.

## Installation

1. Clone or download this repository
2. Place the entire folder in `ComfyUI/custom_nodes/`
3. Restart ComfyUI

No additional dependencies required beyond ComfyUI's base environment.

## Usage

The node provides dropdown selectors for each schema-defined block. Select options to compose prompts, or choose "None" to skip blocks entirely.

**Basic Workflow**:
1. Select target model (SDXL or Flux)
2. Choose library (determines available options)
3. Select from dropdowns for each compositional element
4. Optional: Add custom text via the custom input field
5. Generated prompt outputs to the prompt field

**Intent Flags** (when implemented): Exposure level and camera relationship must be explicitly set. Defaults are: covered clothing, facing camera orientation.

**Addon Support** (when implemented): Each dropdown supports local addon text that modifies only that block's output inline.

## Extending Libraries

Libraries are human-editable JSON files. To add options:

1. Open the target library file in `libraries/`
2. Add entries alphabetically within the relevant block
3. Follow the format: `"Option Name": "prompt text describing this option"`
4. Save and restart ComfyUI

Example:
```json
"hair_color": {
  "Ash Blonde": "with ash blonde hair",
  "Auburn": "with auburn hair",
  "New Color": "with new color hair"
}
```

Libraries automatically sort alphabetically. The "None" option is always first.

## Attribution and Provenance

Generated prompts may optionally include a non-rendering comment for provenance tracking:

```
# Generated using Mode_personal_node — CC BY-NC 4.0
```

This comment is optional and may be removed by users. Attribution is enforced through licensing and documentation, not through technical restrictions.

## License and Usage Rights

This software is licensed under CC BY-NC 4.0. You may use, modify, and distribute it for personal, educational, and research purposes. You may generate and sell images created using this software. Commercial use of the software itself (resale, paid distribution, product bundling) is not permitted. Attribution is required. See LICENSE for full terms.

## Project Status

This is a finalized, production-ready system. Future development will focus on additional libraries and optional schema extensions, never on engine redesign.

## Contributing

Community-contributed libraries are welcome. All libraries must:
- Conform to the schema contract in `schema/connector.json`
- Contain content only (no logic, weights, or UI directives)
- Use alphabetically sorted entries
- Include metadata (name, version, description)

Submit libraries via pull request with validation tests included.

## Technical Documentation

For schema specification, library format, and engine implementation details, see the source code directly or examine `schema/connector.json` for the structural contract.
