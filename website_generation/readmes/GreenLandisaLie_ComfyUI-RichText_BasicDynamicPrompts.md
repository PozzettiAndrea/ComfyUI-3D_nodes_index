## ComfyUI-RichText_BasicDynamicPrompts
A node with basic Dynamic Prompts support that uses javascript to simulate a Rich Text textbox.

<img width="1074" height="1834" alt="1" src="https://github.com/user-attachments/assets/f549e109-dae0-4201-810a-07dd54d19200" />


# Changelog
- v3.2.0
  - Support for native Comfyui Ctrl+Enter command
  - Fixed comments within multi-line combinations not being ignored

- v3.1.0
  - Added a 'Toggle SpellCheck' button - very useful to spot typos
  - CTRL + Left Mouse Click on a non-red LoRA pattern -> opens Windows Explorer at that lora's location with it pre-selected. Does the equivalent of that for MacOS and Linux.

- v3.0.0
  - Fixed major copy/paste bugs introduced in comfyui-frontend-package==1.30.2

- v2.7.2
  - Fixed a minor bug that was caused by having medium/large comments within normal comments and/or large comments within medium ones.

- v2.7.1
  - Fixed a bug in lora pattern regex that caused problems when user starts writing a lora pattern before already writen lora patterns.

- v2.7.0
  - CTRL + Left Mouse Click on a Yellow wildcard -> opens the file with your default text editor (Notepad++ recommended)

- v2.6.0
  - Wildcard patterns now become red when pointing to a .txt file that does not exist

- v2.5.2
  - Bug fix: Lora Preview Tooltips are no longer case sensitive

- v2.5.1
  - [Lora Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) preview tooltips now show up on Lora patterns even if they are within comments 

- v2.5.0
  - Placing the mouse over Lora patterns will now display a preview tooltip with an image/video IF you have [willmiao/ComfyUI-Lora-Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) installed and its managing your loras.

- v2.0.0
  - Adjust Font Size with CTRL + Mouse Wheel Up/Down 
  - Wildcards now support sub-directories like so: '\_\_Folder1\Folder2\filename\_\_'
  - Added LORA loading from prompt support and it supports up to 2 model/clip

- v1.1.0
  - hardcoded font case to white instead of foreground var to prevent possible conflicts whith custom ComfyUI Themes
  - fixed mouse wheel up/down overriding default's ComfyUI behavior
  - TAB key now adds 4 consequent spaces

- v1.0.0
  - Initial release
