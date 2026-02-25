# ComfyUI Archon Nodes

`comfyui-archon-nodes` is a consolidated ComfyUI custom-node suite that combines:

- resolution + prompt nodes
- Booru Roulette (Gelbooru-backed prompt/image metadata node)

## Included nodes

- `ScaleToBestFitResolution`
- `MegapixelsToBestFitResolution`
- `PromptTagAssembler`
- `MergeGeneralTags`
- `BooruRouletteNode`

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes
git clone <your-repo-url> comfyui-archon-nodes
```

2. Install Python dependencies in the same Python environment ComfyUI uses:

```bash
pip install -r ComfyUI/custom_nodes/comfyui-archon-nodes/requirements.txt
```

3. Restart ComfyUI.

## Registry auto-publish (GitHub Actions)

This repo includes `.github/workflows/publish-node.yml` to auto-publish new node versions to the Comfy Registry.

Required GitHub secret:

- `REGISTRY_ACCESS_TOKEN`: your Comfy Registry personal access token

Release flow:

1. Bump `version` in `pyproject.toml`
2. Commit + push to `main`
3. GitHub Action publishes that version to the registry

## Booru Roulette setup (Gelbooru account required)

`BooruRouletteNode` expects Gelbooru API credentials. Configure one of the two methods below.

### Option A: local config file

1. Copy:

`booru_roulette_config.json.example` -> `booru_roulette_config.json`

2. Edit `booru_roulette_config.json`:

```json
{
  "gelbooru_user_id": "YOUR_GELBOORU_USER_ID",
  "gelbooru_api_key": "YOUR_GELBOORU_API_KEY"
}
```

### Option B: environment variables

Set:

- `GELBOORU_USER_ID`
- `GELBOORU_API_KEY`

If both config file and env vars exist, config file values are used first.

## How to get Gelbooru credentials

1. Create/sign in to your Gelbooru account.
2. Open account settings/profile options where API credentials are shown.
3. Copy your user ID and API key into config (or env vars).

If credentials are missing, Booru Roulette raises a clear runtime error.

## Security notes

- `booru_roulette_config.json` is intentionally gitignored.
- Do not commit real API keys.
- If an API key was ever committed, rotate/revoke it in Gelbooru immediately.

## Credits

- Booru randomizer concept inspired in spirit by Inzaniak's Ranbooru node: https://github.com/Inzaniak/comfyui-ranbooru
