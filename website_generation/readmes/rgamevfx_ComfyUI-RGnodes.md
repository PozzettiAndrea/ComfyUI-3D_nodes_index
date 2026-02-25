# VFX and video utility nodes. Avoiding opening other apps/clearing other caches. 

---

<img width="1307" height="621" alt="Screenshot 2026-01-21 201006" src="https://github.com/user-attachments/assets/cd0d7c4f-e1bc-415c-ac7d-652f271cf835" />

---


### 🎞️ VACE Inpaint Keyframe Insert

 Insert frames into an image sequence, and clear the mask on that frame.
 Chain multiple nodes to add >5

  [Make sure inputs are same size]



### 🎞️ Mask Range Doctor 

  Turn mask sequences on or off with white (1.0) or black (0.0). Simple comma , and dash - range syntax to define range


### 🎞️ VACE Clip Doctor - fix frames, edit video in specific frame ranges

  Specify the frame range to fill frames for VACE (Solid grey image, solid white mask). Uses the same comma , and dash - range syntax for precise frame control. Perfect for fixing and filling frames.


### 🎞️ VACE Video Splice - for transitions, clip extensions, and edits (mix any video or image input)
  Splice two video sequences together by overlaying sequence2 at a specified frame offset, fills empty frames with grey for VACE. Preserves input masks and fills gaps with white masks. (Use offset to adjust time between clips/duration of the edit) 

<img width="1634" height="820" alt="Screenshot 2026-01-22 033417" src="https://github.com/user-attachments/assets/f98a1601-f605-4796-a3fd-708ffe79d94e" />


---



### Installation


### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/rgamevfx/ComfyUI-RGnodes.git
```






Special thanks to:

\- https://github.com/TrentHunter82/TrentNodes

\- https://github.com/drozbay/ComfyUI-WanVaceAdvanced
