his script adds an Auto Batch Runner UI to ComfyUI. Main features:

  ** This ComfyUI_AutoBatchRunner is a custom node that has been left unused due to a naming error. Please use the official name ComfyUI-AutoBatchRunner. **  
https://github.com/Boba-svg/ComfyUI-AutoBatchRunner

Automatically loads on startup.

Fixed control panel in the top-right corner with:

A numeric input for run count.

Start (Q) and Stop (S) buttons.

Reads settings from auto_runner_config.json (default: 20 runs, 2-second interval).

Runs app.queuePrompt() repeatedly at set intervals.

Supports keyboard shortcuts:

Shift+Q → Start auto-run

Shift+S → Stop auto-run

In short, it automates multiple prompt runs in ComfyUI with simple UI controls and hotkeys.
