![サンプル](images/sample.png)

his script adds an Auto Batch Runner UI to ComfyUI.
Main features:


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

インストール  
cd /notebooks/ComfyUI/custom_nodes/  
git clone https://github.com/Boba-svg/ComfyUI-AutoBatchRunner.git  

