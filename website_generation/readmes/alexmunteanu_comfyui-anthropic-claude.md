# Anthropic Claude for ComfyUI

A ComfyUI node that uses Claude to generate optimized prompts for 25+ image and video models. 31 built-in templates for FLUX, Runway, Kling, Veo, Wan, Luma, Seedance, Qwen, Nano Banana, and others. Save your own templates, track every run with searchable execution history, and monitor costs.

![anthropic_claude](./node.png)

## What It Does

- **Text and vision**: send text prompts with optional images to any Claude model
- **31 built-in templates**: pre-written instructions for popular AI video/image models (generation and editing)
- **Save your own templates**: create and reuse custom instruction sets
- **Execution history**: searchable log of every run with cost tracking, favorites, and one-click settings restore
- **Model selection**: auto-fetched from the Anthropic API
- **Extended thinking**: Claude's chain-of-thought reasoning with configurable budget
- **Cost tracking**: token usage and USD cost after every run
- **Live API status**: colored dot in the footer shows Claude API health in real time
- **Seed-based caching**: fixed seed reuses the cached response, randomize forces a new one
- **API error recovery**: if the API key is missing or invalid, a modal lets you paste a new key and retry without restarting

## Install

Open **ComfyUI Manager**, search for "Anthropic Claude", and install.

Manual install and full setup: [Getting Started](docs/getting-started.md)

## Links

- [Getting Started](docs/getting-started.md): install, API key setup, first run
- [Usage Guide](docs/usage.md): all inputs, templates, history, vision, extended thinking, caching
- [Troubleshooting](docs/troubleshooting.md): common errors and fixes
