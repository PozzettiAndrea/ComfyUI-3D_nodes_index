# PromptCollapse

A prompt generation system that manages relationships between prompt components to maintain logical consistency. Integrates with ComfyUI as a custom node.

## Overview

PromptCollapse builds prompts by selecting components based on their inferred relationships.
Each component has its own set of parameters that are only valid within the component execution context.
Component might be purely abstract, meaning that it won't produce any prompt fragments at all, but would coordinate other components instead.

## Usage

A minimalistic example can be found in "components/sky.yaml".

## ComfyUI Integration

The system provides a custom node with the following inputs:

- **Prompt**: Initial component tags (comma-separated)
- **Components Directory Path**: Component library directory
- **Reload on Generation**: Toggle component reloading
- **Seed**: Random seed for component selection
