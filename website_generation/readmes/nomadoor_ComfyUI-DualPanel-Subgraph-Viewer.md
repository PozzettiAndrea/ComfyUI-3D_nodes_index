# ComfyUI Dual Panel Subgraph Viewer

[![日本語版](https://img.shields.io/badge/README-日本語版-gray.svg)](README_ja.md)


A frontend extension for ComfyUI that allows you to open and edit subgraphs in a right-hand panel, instead of replacing the main canvas.

---

> **Important**
>
> This extension is a **demonstration prototype**, created to explore the idea of viewing subgraphs in a dual-column layout.  
> It is **highly experimental and not intended for practical use**.  
> Stability and compatibility are not guaranteed, and crashes or rendering issues may occur.

---

## Overview

https://github.com/user-attachments/assets/ef51bdcf-4bef-4a71-bff0-f03aa01e661f
- Click the icon in the upper right corner of a Subgraph node, or double-click the node, to open the subgraph editor in a right-hand panel.  
- Drag the edge of the panel to change its width.  
- Click the `Close` button in the upper right corner of the panel to close it.

---

## Technical Limitations and Known Issues

- The double-click canvas menu uses the legacy implementation, as the Vue-based menu could not be integrated.
- Multi-text input fields (such as those in `CLIP Text Encode` nodes) are unavailable because the subgraph’s `LGraphCanvas` runs outside ComfyUI’s Vue component tree, preventing event binding and input initialization.
- Both the main and subgraph canvases can have nodes selected at the same time. When the mouse moves into the subgraph panel, selections in the main panel are cleared.
- Copy and paste shortcuts (`Ctrl + C / V`) do not work within the subgraph panel.
- The layout may momentarily break or render incorrectly while resizing the subgraph panel.
- Deleting a node inside a subgraph sometimes displays the message `Nothing Selected`.

---

## Disclaimer

This extension is an **experimental proof of concept**.  
It may stop working with future versions of ComfyUI.  
Use at your own risk and avoid deploying it in production environments.

