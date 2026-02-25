# ComfyUI-WordEmbeddings

Word embedding utility nodes for **ComfyUI**. Load a pre-trained embedding model, explore neighbors, do analogies, and project any token/phrase onto **1D/2D/3D semantic axes** with human‑readable summaries.

> 🔎 Built around classic static embeddings (e.g., GloVe, word2vec). Great for quick semantic experiments inside ComfyUI.

---

## Installation

1. Clone or copy this folder into your ComfyUI `custom_nodes/` directory, for example:
   ```bash
   ComfyUI/custom_nodes/ComfyUI-WordEmbeddings
   ```
2. Ensure dependencies are available (ComfyUI portable often already includes NumPy):
   ```bash
   pip install gensim numpy
   ```
3. Restart ComfyUI.

> The **pretrained loader** uses `gensim.downloader`. On first use it will download the selected model into your local `gensim-data` cache.

---

## Quick Start

1. **Load** a model:
   - **WordEmbeddings: Loader** (pretrained dropdown), or
   - **WordEmbeddings: Local Loader** (point to a `.kv` / word2vec `.bin` / `.txt` file).
2. **Connect** the `we_model` output into any of the analysis nodes below (Neighbors / Equation / Axis / Axis2D / Axis3D / Centrality).
3. **Run** and read the numeric outputs and/or the human‑readable **summary** string.

---

## Nodes Overview

### 1) Loaders

#### **WordEmbeddings: Loader**
- **Inputs**: `model_name` (dropdown of `gensim.downloader` models; default `glove-wiki-gigaword-50`)
- **Outputs**: `WE_MODEL`
- **Purpose**: Fetch a known pretrained embedding from the internet the first time, then cache.

#### **WordEmbeddings: Local Loader**
- **Inputs**:
  - `path` (string to local embedding file)
  - `format` (`auto|kv|word2vec_bin|word2vec_text`)
  - `label` (string prefix for display)
- **Outputs**: `WE_MODEL`
- **Purpose**: Load your own embeddings from disk.

---

### 2) Exploration & Algebra

#### **WordEmbeddings: Explorer**
- **Inputs**: `we_model`, `word`, `k`
- **Outputs**: `words_csv`, `debug_csv`
- **Purpose**: Top‑k nearest neighbors for a single word.

#### **WordEmbeddings: Interpolator**
- **Inputs**: `we_model`, `word_a`, `word_b`, `stops`, `topn`, `method (slerp|lerp)`
- **Outputs**: `words_csv`, `debug_txt`
- **Purpose**: Walk between two words on the unit sphere and list representative samples along the path.

#### **WordEmbeddings: Equation**
- **Inputs**: `we_model`, `expression` (e.g., `king - man + woman`), `k`, `topn_pool`, `normalize_terms`, `allow_inputs`
- **Outputs**: `words_csv`, `debug_txt`
- **Purpose**: Classic embedding arithmetic / analogies with lightweight parser.

#### **WordEmbeddings: Token Neighbors**
- **Inputs**: `we_model`, `word`, `k`
- **Outputs**: `words_csv`, `cosines_csv`
- **Purpose**: Same as Explorer but cosine scores separated for easy wiring.

---

### 3) Axis Projections (Core)

> Axes are written **`left|right`**. Each side may contain **comma‑separated synonyms** to define a pole mean. Example:
>
> - `man,boy,he,him,his,father,brother,husband | woman,girl,she,her,hers,mother,sister,wife`
>
> Inputs also accept **phrases** when `token_can_be_phrase=true` (we average the unit vectors of the words).

#### **WordEmbeddings: Token Axis** (1D)
- **Inputs**: `we_model`, `token`, `axis`, `token_can_be_phrase`, `lowercase`, `neutral_eps`
- **Outputs**:
  - `x` *(FLOAT in [-1,1]; + means toward left pole)*
  - `cos_left` *(FLOAT)*
  - `cos_right` *(FLOAT)*
  - `summary` *(STRING)*
- **What it means**:
  - `x` is the projection of the token onto the axis direction.
  - `cos_left/right` are cosine similarities to each pole mean (how much the token “resonates” with each pole independently).
  - `summary` blends **polarity** (from `x`) and **confidence** (from `cos_*`) into a plain‑English sentence.

#### **WordEmbeddings: Token Axis 2D**
- **Inputs**: `we_model`, `token`, `axis1`, `axis2`, `token_can_be_phrase`, `lowercase`, `neutral_eps`
- **Outputs**:
  - `x`, `y` *(FLOATs)*
  - `summary` *(STRING)*
  - `x_cos_left`, `x_cos_right`, `y_cos_left`, `y_cos_right` *(FLOATs)*
- **What it means**: Two independent semantic meters. Useful for 2D plotting or UI overlays.

#### **WordEmbeddings: Token Axis 3D**
- **Inputs**: `we_model`, `token`, `axis1`, `axis2`, `axis3`, `token_can_be_phrase`, `lowercase`, `neutral_eps`
- **Outputs**:
  - `x`, `y`, `z` *(FLOATs)*
  - `summary` *(STRING)*
  - `x_cos_left`, `x_cos_right`, `y_cos_left`, `y_cos_right`, `z_cos_left`, `z_cos_right` *(FLOATs)*
- **What it means**: Three meters → place a word in a simple 3D semantic space (e.g., **gender**, **temperature**, **royalty**).

> The 2D/3D nodes **can ignore weak axes** in their summaries (thresholded by `neutral_eps`) so the text focuses on strong signals.

---

### 4) Centrality

#### **WordEmbeddings: Token Centrality**
- **Inputs**: `we_model`, `word`
- **Outputs**:
  - `centrality` *(FLOAT in [-1,1])*
  - `norm` *(FLOAT)*
  - `summary` *(STRING)*
- **What it means**:
  - Computes the **cosine similarity** between the token (unit‑length) and the corpus‑wide **mean direction**.
  - Rough intuition: high positive = **very generic / frequent‑ish semantic direction**; negative = **off‑center / unusual**.
  - `norm` is the raw vector length (some embeddings store frequency-ish info in norms; take with caution).

---

## Example Axes (copy/paste)

- **Gender**  
  `man,boy,he,him,his,father,brother,husband | woman,girl,she,her,hers,mother,sister,wife`

- **Temperature**  
  `hot,warm,heat,boiling | cold,cool,freezing,ice`

- **Royalty / Status**  
  `royal,king,queen,prince,noble | common,commoner,peasant,ordinary`

- **Formality**  
  `formal,proper,polite | casual,slang,informal`

Feel free to tailor axes to your domain—adding 3–10 good synonyms per side usually stabilizes results.

---

## Interpreting the Numbers (cheat sheet)

- **Cosine similarity** (`cos_*`): how strongly the token points toward a pole. Range `[-1, 1]`.  
  - `~0.7+` → strong affinity; `~0.3–0.6` → moderate; `<0.2` → weak.
- **Projection** (`x`, `y`, `z`): signed position along the axis. Positive = more **left**, negative = more **right**.
- **Neutrality**: if `|x| < neutral_eps` (default `0.08`), we call it **about equal** in the summary.

---

## Tips & Caveats

- **Static embeddings** reflect biases of their training data. Be thoughtful when choosing axes (especially sensitive ones).
- Different models (e.g., `glove-6B-300`, `word2vec-google-news-300`) will give different absolute values and neighbors.
- If a **phrase** is used, the node averages unit vectors of its words. This is a simple, fast heuristic.
- `norm` (in Centrality) isn’t universally meaningful across models; use it comparatively **within the same model** only.
- If a pole side has **no in‑vocab words**, the related axis (or cosine) will be reported as unavailable / neutral in summaries.

---

## Development

- The code is intentionally **dependency‑light** (just `gensim` + `numpy`).
- We cache the **global mean direction** per model in memory to avoid recomputation.
- Axis internals:
  1. Compute **unit‑mean** vector per pole (averaged synonyms).
  2. Axis direction `a = unit(left_mean - right_mean)` (or single‑sided fallback).
  3. Projection `x = token_unit · a` and per‑pole `cos_left/right = token_unit · pole_mean`.
  4. Generate human summary from polarity (`x`) + confidence (`cos_*`) with thresholds.

---

## Acknowledgements

- Built on top of **Gensim**: https://radimrehurek.com/gensim/
- Inspired by classic “**king − man + woman ≈ queen**” style analogies and axis‑projection demos.
