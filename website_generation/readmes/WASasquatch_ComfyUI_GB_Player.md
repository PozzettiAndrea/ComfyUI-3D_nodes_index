
# ComfyUI Game Boy Player

![](screenshot.png)

Embeds a self-contained Game Boy Advance emulator UI inside a ComfyUI node.

This project vendors a static build of the web emulator UI based on [gba.js.org](https://gba.js.org), so it can run offline inside ComfyUI.

## Install

- **Option A (git clone)**
  - Clone this repo into:
    - `ComfyUI/custom_nodes/ComfyUI_GB_Player`

- **Option B (Manager)**
  - Open Manager and install **ComfyUI_GB_Player**

- **Option C (zip)**
  - Download the repo as a zip.
  - Extract it to:
    - `ComfyUI/custom_nodes/ComfyUI_GB_Player`

Restart ComfyUI after installing.

## Usage

- **Add the node**
  - In ComfyUI, add the node:
    - `ComfyGameBoyPlayer`

- **Load a ROM**
  - The emulator UI is inside the node.
  - Use the emulator's menu to load a GBA bios, and `.gba` ROM.

## Notes

- **UI-only node**
  - This node is a UI/embed node. It does not currently produce ComfyUI image outputs.

- **Offline / vendored web assets**
  - The emulator assets are shipped in this repo under:
    - `web/gba/`
  - To prevent ComfyUI from auto-loading vendored third-party JavaScript as extensions, vendored `.js` files are renamed to:
    - `.js.txt`

- **ComfyUI theme integration**
  - The ComfyUI web extension posts theme tokens to the iframe, and the embedded player applies them via CSS variables.
  - Message types used:
    - `was-gba-theme`
    - `was-gba-request-theme`

## Troubleshooting

- **The player UI doesn’t update after changes**
  - Do a hard refresh in your browser:
    - `Ctrl+F5`
  - Or clear browser cache for the ComfyUI site.

- **Node appears but iframe is missing/blank**
  - Open DevTools Console and look for errors.
  - Confirm the iframe path resolves:
    - `extensions/ComfyUI_GB_Player/gba/player/index.html`

- **Iframe seems misaligned during zoom/pan**
  - Make sure you’re running the latest `web/comfy_gameboy_player.js` from this repo.
  - If you have multiple copies installed, remove old versions from other `custom_nodes` folders.

## Credits / License

- Emulator UI: GBA Online (`gba.js.org`) (vendored static build)
- Emulator core: IodineGBA (vendored; see `web/gba/iodineGBA/`)
- This repository includes third-party components under their respective licenses (see files under `web/gba/`).
