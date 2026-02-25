# 🛡️ ComfyUI Workflow Backup

A custom node for **ComfyUI** that allows you to backup your current workflow (API format) and all the models used in it to a specific destination (Local or External Drives).

## ✨ Features

* **💾 Full Backup:** Saves the workflow `.json` and copies all necessary models (Checkpoints, LoRAs, VAEs, etc.).
* **🔒 Enterprise Security:** Includes a path sanitizer and a whitelist system to prevent unauthorized file system access.
* **📂 External Drive Support:** Safely backup to USB drives, NAS, or secondary hard drives using the whitelist configuration.
* **📊 Analysis Mode:** Preview which files will be copied and the total size before executing the backup.
* **🌎 Bilingual:** Output logs available in English and Spanish.

## ⚙️ Configuration (Crucial Step!)

To comply with strict security standards, this node **blocks write access to external drives by default**. 

To allow backups to external drives (e.g., `D:/`, `E:/`, `/mnt/`), you **must** create a configuration file manually:

1.  Go to the node directory: `ComfyUI/custom_nodes/ComfyUI-Workflow-Backup/`
2.  **Workflows Path:** Paste the **specific folder** where your `.json` workflows are located (e.g., `ComfyUI/user/default/workflows`).
    * *⚠️ Tip: Do not use the root `ComfyUI` folder, or the node will try to scan system files and show warnings.*
3.  Add the allowed root folders inside using the JSON format below.

**Example `extra_paths.json`:**
```json
{
    "allowed_paths": [
        "D:/ComfyUI_Backup",
        "E:/MyExternalDrive",
        "/mnt/backups"
    ]
}
```
⚠️ Note: If extra_paths.json is missing or the destination path is not whitelisted, 
the node will force the backup to be saved inside the standard ComfyUI/output/workflow_backups folder.
## 📦 Installation
**Via ComfyUI Manager:**
* Search for `Workflow Backup` in the Manager and click **Install**.

**Manual Installation:**
1. Go to your `custom_nodes` folder.
2. Run: `git clone https://github.com/zavatmotion/ComfyUI-Workflow-Backup.git`
3. Restart ComfyUI.

## 🚀 How to Use

### 📺 Video Tutorials

**1. Basic Usage (No configuration needed)**
*Use this if you only want to save backups inside your ComfyUI folder.*

https://github.com/user-attachments/assets/502004be-94ce-4043-ab9d-86ed68728625

**2. Advanced: How to use External Drives**
*Use this if you want to save backups to your Desktop, USB, or other drives.*

https://github.com/user-attachments/assets/9d6b9ce8-e808-40e4-af72-b0944a21a312

**Quick Start:** You can load the included `Models-Backup.json` workflow file to get started immediately.

1. Add the node **"Workflow Backup"** (Category: `utils/backup`).
2. **Workflows Path:** Paste the **specific folder** where your `.json` workflows are located (e.g., `ComfyUI/user/default/workflows`).
   * *⚠️ Tip: Do not use the root `ComfyUI` folder to avoid scanning system files.*
3. **Backup Destination:** Choose where to save the backup.
   * *Remember: If you want to use an external drive, you must add it to `extra_paths.json` first.*
4. **Mode:**
   * `ANALYSIS_ONLY`: Checks files and calculates size (Safe mode).
##  Support & Feedback

If you find a bug or have a suggestion, please [Open an Issue](https://github.com/zavatmotion/ComfyUI-Workflow-Backup/issues) here on GitHub.   
   * `EXECUTE_BACKUP`: Performs the actual copy.

---
*Created by [zavatmotion](https://github.com/zavatmotion)*
