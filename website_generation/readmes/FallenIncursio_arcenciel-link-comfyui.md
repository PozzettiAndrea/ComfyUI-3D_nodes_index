# ArcEnCiel Link - ComfyUI Extension

Bring your ArcEnCiel models straight into ComfyUI with one click. Includes
Link Key auth, remote worker control, inventory sync, and sidecar generation.

---

## Release Notes (latest)

- Updated onboarding to a **Connect-first** flow: with the extension installed and local UI running, open ArcEnCiel Link panel on [arcenciel.io](https://arcenciel.io) and click **Connect**.
- Documented auto-detect behavior for local endpoints: `127.0.0.1` / `localhost` on ports `7860`, `7861`, `7801`, `8000`, `8501`.
- Added explicit **Custom endpoint** fallback guidance for non-standard host/port setups.
- Corrected queue/progress wording: status is shown in the **ArcEnCiel Link panel** and local worker logs.
- Updated credential messaging: **Link Key (`lk_...`) is primary**; **API key is legacy/deprecated** for current websocket flow.
- Added ComfyUI Registry/Manager install path as preferred option (manual `custom_nodes` remains supported) and clarified bridge-based control/default port behavior.

---

## Features

- One-click download from ArcEnCiel model cards.
- Model-aware routing for checkpoints, LoRAs, VAEs, and embeddings.
- Background worker with retry back-off, disk-space guard, and SHA-256 verification.
- Inventory sync so ArcEnCiel can skip models already installed locally.
- Optional preview PNG, `.arcenciel.info`, and HTML quick-view sidecars.

---

## Installation (ComfyUI)

### Preferred: ComfyUI Registry / Manager

1. Open ComfyUI Manager.
2. Search for **ArcEnCiel Link** (publisher `fallenincursio`) and install from the registry.
3. Restart ComfyUI.

### Manual fallback (`custom_nodes`)

1. Clone into:

```text
ComfyUI/custom_nodes/ArcEnCielLink
```

2. Install dependencies in the ComfyUI venv (Windows example):

```text
ComfyUI\venv\Scripts\python.exe -m pip install -r ComfyUI\custom_nodes\ArcEnCielLink\requirements.txt
```

3. Restart ComfyUI.

---

## First-time setup (Connect-first)

1. Start ComfyUI with the extension installed.
2. On [arcenciel.io](https://arcenciel.io) open the **ArcEnCiel Link panel**, create/select a **Link Key (`lk_...`)**, then click **Connect**.
3. ArcEnCiel connects through the local bridge endpoint (default `http://127.0.0.1:8000`).
4. If your bridge uses a custom host/port, assign it manually in ArcEnCiel Link panel via **Find WebUIs** -> **Custom...**.
5. Fallback: set credentials in `ComfyUI/user/arcenciel-link/config.json`.

Note: there is no native ComfyUI settings panel yet; the bridge + config file handle local control.

---

## Credentials and security

- **Link Key (`lk_...`) is the primary credential** for the current ArcEnCiel worker websocket flow.
- API key fields remain for legacy/self-hosted compatibility, but Link Keys are recommended for active setups.
- Config path:

```text
ComfyUI/user/arcenciel-link/config.json
```

Default schema:

```json
{
  "base_url": "https://link.arcenciel.io/api/link",
  "link_key": "",
  "api_key": "",
  "enabled": false,
  "min_free_mb": 2048,
  "max_retries": 5,
  "backoff_base": 2,
  "save_html_preview": false,
  "allow_private_origins": false,
  "bridge_port": 8000
}
```

Environment overrides:

- `ARCENCIEL_LINK_URL` - base API URL.
- `ARCENCIEL_LINK_KEY` - Link Key (`lk_...`).
- `ARCENCIEL_API_KEY` - API key (legacy).
- `ARCENCIEL_DEV=1` - allow HTTP endpoints and private origins for testing.

---

## How to use

- Press Download on any ArcEnCiel model card.
- Queue/progress state is visible in the ArcEnCiel Link panel and ComfyUI/worker logs.
- Inventory sync runs periodically and duplicate downloads are skipped.

---

## Local API surface

- GET `/arcenciel-link/ping`
- POST `/arcenciel-link/toggle_link`
- GET `/arcenciel-link/folders/{kind}`
- POST `/arcenciel-link/generate_sidecars`

---

## Advanced configuration

- `min_free_mb`, `max_retries`, and `backoff_base` live in config.json.
- `save_html_preview` enables HTML quick-views next to model files.
- `allow_private_origins` permits non-arcenciel origins for local testing.
- `bridge_port` changes the local bridge listen port (default `8000`).

---

## Troubleshooting

| Symptom                                            | Fix                                                                                                                                                                                                |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Worker stays offline                               | Use a valid Link Key and click Connect from the ArcEnCiel Link panel.                                                                                                                              |
| Connect only works after manual endpoint selection | ArcEnCiel auto-detect scans `127.0.0.1` and `localhost` on ports `7860`, `7861`, `7801`, `8000`, `8501`. If your Comfy bridge is on another port, assign the endpoint manually with **Custom...**. |
| Browser reports private network blocked            | Accept the browser PNA prompt or enable `allow_private_origins` for local testing.                                                                                                                 |
| Download stuck at 0%                               | Check disk space and write permissions.                                                                                                                                                            |
| Repeated SHA256 mismatch                           | Usually network instability or a bad mirror.                                                                                                                                                       |
| API key no longer connects worker                  | API keys are legacy; use a Link Key for current ArcEnCiel websocket auth.                                                                                                                          |
