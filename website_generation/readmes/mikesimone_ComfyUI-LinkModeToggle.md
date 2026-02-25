# LinkModeToggle — ComfyUI link render mode hotkeys + button

[![ComfyUI Manager](https://img.shields.io/badge/Available%20on-ComfyUI%20Manager-blue.svg)](https://github.com/Comfy-Org/ComfyUI-Manager)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/mikesimone/LinkModeToggle)](https://github.com/mikesimone/LinkModeToggle/releases)

**Install:** ComfyUI-Manager → “Custom Nodes” → search **Link Mode Toggle**



**Make the canvas readable at a glance.** LinkModeToggle adds:

* **Hotkeys:** `F8` or `Ctrl+K` to cycle **Spline → Linear → Straight**
* **Toolbar button:** a small bottom-right canvas button (next to Fit/Zoom/Minimap) with a mini badge showing the current mode
* **Persistence:** remembers your last mode per browser (localStorage)

Designed for the modern ComfyUI frontend (v1.31+), but falls back gracefully on older LiteGraph builds.

---

## Why?

Complex graphs look like spaghetti when every link’s a spline. Straight/linear links reduce visual noise and help you route with intent. Toggling on demand beats digging through menus.

### Straight 

<img width="1210" height="1200" alt="image" src="https://github.com/user-attachments/assets/e5a66ec1-7128-4da0-89fb-7f08d6192c44" />


### Linear 

<img width="1612" height="1329" alt="image" src="https://github.com/user-attachments/assets/3c532442-e9a4-4c77-9ccd-47e64a4438e3" />


### Spline 

<img width="1567" height="1352" alt="image" src="https://github.com/user-attachments/assets/616dcc6e-31e7-4fd2-8cb3-ee0bb2e25395" />


As you can tell, there's pros and cons to the different types of render when it comes to figuring out where an input or an output is connected, and, as of now, only clicking on an INPUT will highlight the entire path; clicking an output does nothing. *That's not frustrating at all.*

So, with a handy-dandy little icon in the corner like this:

<img width="477" height="266" alt="image" src="https://github.com/user-attachments/assets/83dc074b-5bc9-46f0-bf09-3bb28a93b804" />


Instead of clicking "Comfy > Settings > LiteGraph" then scrolling down, finding the dropdown box, and selecting a mode,  you just click the icon and switch it. 

I dunno, maybe it's just me. Clearly, there wasn't *much* demand for it before I wrote this, but I'm getting use out of it, and I hope you do, too.


---

## Features

* Zero server changes — pure front-end extension
* **Hotkeys:** `F8`, `Ctrl+K`
* **UI button:** docks into the standard bottom-right canvas control group
* Smart compatibility: tries multiple internal APIs (`setLinkRenderMode`, `links_render_mode`, `render_curved_links`) for different Comfy/LiteGraph builds

---

## Install

Use **ComfyUI-Manager** or manual:

### Manager

* Open *ComfyUI-Manager* → **Install from URL** → paste:

  ```
  https://github.com/YOUR_GITHUB_USERNAME/LinkModeToggle
  ```
* Restart ComfyUI

### Manual

```
ComfyUI/
└─ custom_nodes/
   └─ LinkModeToggle/
      ├─ __init__.py
      └─ web/
         ├─ index.js
         ├─ index.css
         └─ extensions/
            └─ linkmode-toggle.js
```

Restart ComfyUI and hard-refresh the browser (Ctrl+F5).

---

## Usage

* Press **F8** or **Ctrl+K** to cycle modes.
* Click the **curve icon** button in the bottom-right canvas controls.
* The tiny badge shows **S/L/S** for Spline/Linear/Straight.
* Your choice persists across reloads.

---

## Uninstall

Remove `custom_nodes/LinkModeToggle` and restart ComfyUI.

---

## Troubleshooting

* No button? Hard-refresh (**Ctrl+F5**) and ensure `web/index.js` imports `./extensions/linkmode-toggle.js`.
* Button floating? We fall back to a bottom-right floating dock if the toolbar isn’t detected (some forks/themes). It’ll still work.
* Console check:

  ```js
  app?.extensions?.LinkModeToggle
  ```

---

## License

MIT © Mike Simone

Minor doc tweak 2025-11-08T17:26:17

