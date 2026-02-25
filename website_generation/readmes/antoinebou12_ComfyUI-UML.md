# ComfyUI-UML

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Comfy Registry](https://img.shields.io/badge/Comfy_Registry-comfyui--uml-blue)](https://registry.comfy.org/publishers/antoinebou12/nodes/comfyui-uml)
[![Workflow Tests](https://github.com/antoinebou12/ComfyUI-UML/actions/workflows/workflow-tests.yml/badge.svg)](https://github.com/antoinebou12/ComfyUI-UML/actions/workflows/workflow-tests.yml)
[![Publish to Comfy registry](https://github.com/antoinebou12/ComfyUI-UML/actions/workflows/publish-node.yml/badge.svg)](https://github.com/antoinebou12/ComfyUI-UML/actions/workflows/publish-node.yml)

[![GitHub stars](https://img.shields.io/github/stars/antoinebou12/ComfyUI-UML)](https://github.com/antoinebou12/ComfyUI-UML/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/antoinebou12/ComfyUI-UML)](https://github.com/antoinebou12/ComfyUI-UML/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/antoinebou12/ComfyUI-UML)](https://github.com/antoinebou12/ComfyUI-UML/watchers)

<p align="center">
  <img src="icon.png" alt="ComfyUI-UML" width="128" height="128">
</p>

ComfyUI custom nodes for rendering diagrams (Mermaid, PlantUML, Graphviz, etc.) via [Kroki](https://kroki.io) or local renderers.

<img width="2164" height="987" alt="image" src="https://github.com/user-attachments/assets/c9fc5efa-ebd5-47ea-b5ab-86ac03dd92b5" />


## Table of contents

- [Features](#features)
- [Installation](#installation)
- [Updating](#updating)
- [Usage](#usage)
- [Testing](#testing)
- [Development](#development)
- [Workflows](#workflows)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Author](#author)
- [Publishing](#publishing-to-the-comfy-registry)

**Documentation:** [docs/](docs/) — usage, Kroki formats, workflows, testing, publishing, node reference.

## Features

- **Kroki (web)**: Many diagram types via the Kroki API. No local setup.
- **28 Kroki diagram types** and **output formats** (png, svg, jpeg, pdf, txt, base64) per type; validated against [Kroki's support matrix](https://docs.kroki.io/kroki/diagram-types).
- **Diagram options**: Optional JSON for quality/theme (e.g. GraphViz scale, Mermaid/PlantUML/D2 theme). See [Kroki diagram options](https://docs.kroki.io/kroki/setup/diagram-options/).
- **Shareable Kroki URL** and **built-in viewer** (zoom, Save to ComfyUI, copy link).
- **ComfyUI_Viewer**: For **iframe embedding of a Kroki URL**, use the viewer in embed mode: `viewer.html?embed=1&url=...` or the Diagram Viewer URL node’s **viewer_url_iframe** output (connect **kroki_url** from UML Render to Diagram Viewer URL). The Diagram Viewer URL node also shows a **live diagram preview** inside the node when **kroki_url** is set.
- **Local Mermaid**: Backend "local" + [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) for offline SVG/PNG; optional theme.
- **Local Graphviz**: Optional when the `graphviz` Python package is installed.

See [docs/Usage.md](docs/Usage.md) and [docs/KrokiFormats.md](docs/KrokiFormats.md) for details.

## Installation

**From Comfy Registry (recommended):**

```bash
comfy node install comfyui-uml
```

**Manual:**

1. Clone or copy this folder into `ComfyUI/custom_nodes/`.
2. Install dependencies: `pip install -r requirements.txt` or `uv sync`.
3. **Optional** — Local Mermaid: Node.js + `cd scripts && npm install`. PNG: `pip install cairosvg`. SVG preview in node: `pip install cairosvg`. Dynamic widget visibility: `pip install comfy-dynamic-widgets` (or extras from pyproject.toml).

## Updating

After updating (Manager, git pull, or manual), **restart ComfyUI** so nodes and web assets load. Other nodes failing to update are independent; retry that node and restart.

## Usage

Add the **UML Render (Mermaid/PlantUML/etc)** node (category: UML). Choose **backend** (web/local), **diagram_type**, enter **code**, and set **output_format** (png, svg, jpeg, pdf, txt, base64 — validated per type). Optional **diagram_options** JSON for Kroki.

Full usage, outputs, viewer, and LLM workflow: [docs/Usage.md](docs/Usage.md). Diagram type × format table: [docs/KrokiFormats.md](docs/KrokiFormats.md).

## Testing

CI runs [comfy-test](https://github.com/PozzettiAndrea/comfy-test) on push/PR to `main`. See [docs/Testing.md](docs/Testing.md) for config ([comfy-test.toml](comfy-test.toml)) and adding workflows.

## Development

To run linting and formatting on commit (JSON and Python):

1. Install dev dependencies: `pip install -e ".[dev]"` or `uv sync --extra dev`.
2. Install pre-commit hooks: `pre-commit install`.

Pre-commit will format JSON (key order preserved) and run Ruff (lint + format) on Python. To run on all files: `pre-commit run --all-files`.

## Workflows

- **uml_single_diagram_only.json** — One UMLDiagram node (no links).
- **uml_single_node.json** — Single UMLDiagram + Diagram Viewer URL (kroki_url). Use this if you see "missing nodes" or queue errors with a pasted workflow.
- **uml_mermaid.json** — Mermaid example: one UMLDiagram + Diagram Viewer URL (kroki_url).
- **uml_plantuml.json** — PlantUML example: one UMLDiagram + Diagram Viewer URL (kroki_url).
- **uml_llm_ollama.json** — LLM (Ollama) → Kroki: LLMPromptEngine → LLMCall → UMLDiagram → UMLViewerURL.

To regenerate the workflow files and check that format lists stay in sync, run `python scripts/generate_all_diagrams_workflow.py` (no arguments).

Full list, loading tips, and format: [docs/Workflows.md](docs/Workflows.md). Workflow format and normalizer: [docs/WorkflowFormat.md](docs/WorkflowFormat.md).

## License

MIT. See repository license.

## Author

**antoinebou12** — [GitHub](https://github.com/antoinebou12) · [Comfy Registry publisher](https://registry.comfy.org/publishers/antoinebou12)

## Publishing to the Comfy Registry

Publishing runs when `pyproject.toml` changes on `main`/`master`. See [docs/Publishing.md](docs/Publishing.md) for token setup and troubleshooting.
