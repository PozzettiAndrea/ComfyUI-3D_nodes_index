# ComfyUI-Arrow-Key-Canvas-Navigation

This custom "node" for ComfyUI enables pan navigation of the canvas using the arrow keys, with a customizable pan speed in ComfyUI's Settings, under the "codecringebinge" subsection of the Settings Dialog's left panel.

**Note:**

-   There are specific cases in which the arrow keys intentionally will not pan the canvas, such as when a node with more than one image is selected (as the arrow keys should retain their standard behavior of cycling through said images), or when the canvas is blocked by another UI window (e.g. the Comfy Manager, Comfy Settings, the pythongosssss Image Gallery, modals, etc.).
-   If you encounter scenarios when the arrow keys are panning the canvas when they shouldn't (e.g. when a custom node opens a UI window blocking the canvas), you can report this in the GitHub Issues section of this repo and I might be able to exclude the UI windows in question via an update, or alternatively for a likely faster fix, you could identify a CSS class name for the window in question (e.g. by using your browser's Developer Tools), add its name to the `CANVAS_BLOCKING_UI_WINDOW_CLASSES` string constant in `arrow_key_canvas_navigation.js`, and then restart ComfyUI and refresh the page.

# Installation

## If using ComfyUI Manager:

1. Look for `ComfyUI-Arrow-Key-Canvas-Navigation`, confirm the author is `codecringebinge`, and install it.

## If installing manually:

1. Clone this repo into the `custom_nodes` folder.

# Thanks and cheers! 🍻
