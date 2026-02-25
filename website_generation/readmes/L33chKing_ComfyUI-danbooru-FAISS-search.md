<p align="center">
  <img src="nodes.png" alt="Danbooru FAISS Search & Style Similarity" width="640" />
</p>

# Danbooru FAISS Search & Style Similarity (ComfyUI Nodes)

High‑quality Danbooru similarity search and learned style similarity retrieval for ComfyUI. Combines image & tag embeddings with flexible weighting and negative prompt control, plus a separate HNSW index–based style matcher.

## Features

- Fast FAISS search over Danbooru 2022 embedding index 
- Hybrid tag embedding: ONNX text encoder + hash fallback
- Image + tag blending strategies 
- Post metadata/tags/url/id retrieval 
- Auto danbooru image fetching (api/html)
- Danbooru Style similarity node 

## Installation

Place this folder inside `ComfyUI/custom_nodes/` then install Python deps

```
pip install -r requirements.txt
```

 resource files (indexes, style embeddings/checkpoints) are downloaded automatically

## Nodes Overview

| Node | Purpose |
|------|---------|
| `DanbooruImageSearch` | Multi-image semantic retrieval from Danbooru index using combined image/tag positive & negative logic. Returns images + direct (or fallback) URLs + aggregated IDs. |
| `GetDanbooru` | Fetch a single post by URL (API + HTML fallback) with optional resizing (`zoom`). |
| `TagPrompt` | Normalize / dedupe / sort / limit a tag string for clean input to search nodes. |
| `StyleSimilarity` | Style-based nearest-neighbour search over large learned embedding set (gustproof). Supports checkpoint versioning and optional similarity overlay. |

## Danbooru Lookup Parameters

| Parameter | Type / Values | Default | Purpose |
|-----------|---------------|---------|---------|
| download_size | preview, thumbnail, large, full | preview | Choose which size variant to request (falls back if unavailable). |
| max_images | int [1–50] | 4 | Maximum images to return (search + download budget base). |
| positive_image | IMAGE (optional) | – | Image embedding used as positive semantic anchor. |
| negative_image | IMAGE (optional) | – | Image embedding subtracted (avoid similar look). |
| positive_prompt | STRING (tags/text) | "" | Comma‑separated Danbooru tags or free text for positive semantics. |
| negative_prompt | STRING (tags/text) | "" | Tags / text to push away (subtract). |
| api_username / api_key | STRING | "" | Optional Danbooru credentials (higher rate limits). |
| model_type | clip, siglip | clip | Backbone for text/image tag processing. Requires matching `clip_models/{model_type}_text.onnx` for ONNX tag embeddings. |
| tag_embedding_mode | auto, hash_only, onnx_only | auto | How tag vectors are built (ONNX multi‑hot vs hash fallback). |
| combine_strategy | Balanced, Stepwise de-overlap | Balanced | Vector combination mode (see combination notes below). |
| tag_new_info_only | bool | False | Removes tag components already present in image vector (orthogonalizes tag vectors). |
| reduce_negative_overlap | bool | False | Projects negative components away from positive mixture to avoid over‑cancellation. |
| idf_weight_tags | bool | False | Apply IDF weighting from tag frequency file (`selected_tags.csv`). |
| fetch_mode | auto, api, html | auto | Metadata retrieval path (API→HTML fallback or forced). |
| extra_api_search | int [0–1000] | 0 | Additional recovery attempts for failed posts (expands candidate fetch). |
| debug | bool | False | Verbose internal logging. |
| image_weight | float [0–4] | 1.0 | Weight applied to image embeddings before combination. |
| tag_weight | float [0–4] | 1.0 | Weight applied to tag embeddings before combination. |

### Embedding Combination (Core Logic)

| Strategy | Internal Name | Behavior |
|----------|---------------|----------|
| Balanced | balanced_diff | L2‑normalize positive (image+tags) and negative sides separately, then subtract and renormalize. |
| Stepwise de-overlap | stepwise_deoverlap | Sequentially add positives and subtract negatives, orthogonalizing at each step to reduce component overlap. |

Optional modifiers:
- tag_new_info_only: orthogonalize tag vectors against image basis (adds only new semantic info)
- reduce_negative_overlap: project negative vectors off the positive mixture (less semantic washout)

### Tag Embedding Modes

| Mode | Behavior | When to Use |
|------|----------|-------------|
| auto | Try ONNX multi‑hot (if model + tag index available), blend hash vectors for unknown tags, fallback to pure hash. | Default robust path. |
| hash_only | Deterministic SHA‑256 based 1024‑D vectors per tag (stable, no external model). | Offline or minimal setup. |
| onnx_only | Only real tags via ONNX multi‑hot. Unknown tags ignored; if encoder missing returns None. | Highest fidelity (requires `clip_text.onnx` + `selected_tags.csv`). |

## Style Similarity Parameters

| Parameter | Type / Values | Default | Purpose |
|-----------|---------------|---------|---------|
| input_image | IMAGE / batch | – | Query image(s) whose style embedding(s) are computed. |
| max_images | int [1–100] | 4 | Number of nearest style matches to return. |
| model_version | v0.2, v0.3 | v0.3 | Select checkpoint (downloaded on first use). |
| download_size | preview, thumbnail, large, full | preview | If API lookup succeeds (not disabled), choose size variant. |
| overlay_similarity | bool | False | Renders raw squared L2 distance text onto each returned image. |
| disable_api | bool | True | Skip MD5→post metadata/API upgrade (keeps original CDN URLs). |

### Style Retrieval Notes
- HNSW index persisted after first build (`style_hnsw_raw.index`).
- Distances shown are raw squared L2 (lower = closer style).
- Query embeddings coerced to index dimension if mismatch (padding/truncation + renorm).


## Attribution

- [SmilingWolf](https://huggingface.co/spaces/SmilingWolf/danbooru2022_embeddings_playground)  – Danbooru embeddings
- [gustproof](https://huggingface.co/spaces/gustproof/style-similarity/tree/main) – Style similarity model
- ComfyUI project & community