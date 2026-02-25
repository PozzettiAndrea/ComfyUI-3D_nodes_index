# ComfyUI-EmbeddingPipelineAnalytics

## overview

this repo is to capture end-to-end data, metadata, and embeddings for ComfyUI workflows, specifically HunyuanVideo to start.

## goals

- creating more formalized datasets for open source projects and teams for analysis and/or downstream tasks, of which there are infinite experiments to explore
- giving more powerful analysis tools and data management tooling to non-developers in the community
- providing a feedback mechanism for analyzing embeddings vs. inputs

## features

as this will be maintained based on my own free time, the core will focus on the following:

*pipeline capture node that can:*

- capture embeddings and run metadata and data inputs / outputs from ComfyUI workflows (parameters, prompt, guidance, sampling, etc)
- store data in a structured format for analysis (parquet, jsonl)
- all inside comfyui

*analysis node that can:*

- analyze embeddings using different techniques
- provide insights into impact of different prompts (or lora finetuning captions) on end results (ie: for a given target generation, what captions need to be added, left out, expanded upon, reordered, reworded, restructured, etc)
- compare runs
- generate visualizations (UMAP, etc)
- produce structured reports
- all inside comfyui

## future / plans

- 'so what?' analysis / interpretation by enabling hooks into LLMs for analysis - fantastic way for those unfamiliar with working with embeddings to interpret and explore\
- integration with embedded SQL database, likely duckdb
- more intuitive comfyui nodes (first time building one, so learning as i go)
- avoiding overlap with other similar projects (ie: logging, observability) - this is primarily for embeddings analysis and capturing data (inputs/outputs/metadata) from comfyui pipelines in a structured way
- feedback from community for real use cases

## project code tree

```
ComfyUI-EmbeddingPipelineAnalytics/
├── core
│   ├── analyzers.py
│   ├── data_store.py
│   ├── __init__.py
│   └── pipeline_types
│       ├── base.py
│       ├── hunyuanvideo.py
│       ├── __init__.py
│       └── __pycache__
├── example_workflows
│   └── example_workflow.json
├── __init__.py
├── LICENSE
├── nodes.py
├── README.md
├── requirements.txt
└── tests
    ├── conftest.py
    ├── test_hunyuanvideo.py
    └── test_workflow.py
```
