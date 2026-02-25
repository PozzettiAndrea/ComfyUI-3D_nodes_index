# LucianoTools ComfyUI Suite

A collection of useful user interface extensions for ComfyUI to improve workflow and provide helpful feedback.

---
## Features

This suite currently several extensions which can be enabled or disabled independently from the settings panel:

#### 1. Batch Confirmation
- **Safety Check:** Before running a workflow with a batch size greater than 1, a confirmation dialog will appear.
- **Prevents Accidental Runs:** Avoids accidentally starting a long render queue that you didn't intend to run.
    <div align="center">
        <img src="https://github.com/user-attachments/assets/c7edc893-1991-4b6c-8e6f-8645b9f5e137" alt="Batch Confirmation" >
        <p>Batch Confirmation</p>
    </div>

#### 2. Path Display
- **File Path:** Shows the path of the output file for easy identification, both from the queue listing and on the preview.
- **Image Size:** Shows the dimensions of the image in pixels.
  
| Queue Listing                       | Full Preview                           |
| ----------------------------------- | ----------------------------------- |
| ![queue](https://github.com/user-attachments/assets/ac8fcaf9-a4c2-44f4-9653-b6bd58deced4) | ![full](https://github.com/user-attachments/assets/435f4a57-5203-4f44-99d4-b7a51eb0d30e) |

#### 3. Run Timer
- **Live Timer:** Shows a `MM:SS` timer next to the "Queue Prompt" button while a prompt is running.
- **Final Time:** Displays the final time with a success (✅) or error (❌) icon.
- **Run History:** Click the timer to see a history of the last 5 run times.
    <div align="center">
        <img src="https://github.com/user-attachments/assets/0b9ec2e7-18bf-4972-b77e-075a7bd8db0c" alt="Run Timer" >
        <p>Run Timer</p>
    </div>

---

## Installation

The recommended installation method is via the ComfyUI Manager.

1.  Ensure you have [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed.
2.  In ComfyUI, go to **Manager -> Install via Git URL**.
3.  Enter this repository's URL:
    ```
    https://github.com/ChristopherLuciano/ComfyUI-LucianoTools
    ```
4.  Click "Install" and restart ComfyUI when prompted.

## ⚠️ Troubleshooting Installation

If you see the error **`This action is not allowed with this security level configuration`** when trying to install, it means the ComfyUI Manager's security settings are blocking the installation. Here’s how to fix it.

**Step 1: Try Updating First**

First, try updating the ComfyUI Manager, as this often resolves the issue without further steps:
- Go to **Manager -> Update -> Update All**.
- Restart ComfyUI and try installing again.

**Step 2: Manually Adjust Security Level**

If updating doesn't work, you'll need to manually edit the Manager's configuration file.

1.  **Locate the `config.ini` file:**
    *   For **Manager v3.0+**, the file is usually at: `ComfyUI/user/default/ComfyUI-Manager/config.ini`
    *   For **older versions**, the file is usually at: `ComfyUI/custom_nodes/ComfyUI-Manager/config.ini`

2.  **Edit the `config.ini` file:**
    *   Open the file in a text editor (like Notepad or VS Code).
    *   Find the `[Manager]` section and change the `security_level` to `weak`.

    ```ini
    [Manager]
    security_level = weak
    ```

3.  **Save and Restart ComfyUI:**
    *   Save the changes to the file.
    *   Completely close and restart your ComfyUI server.

After restarting, you should be able to install the suite via the Git URL without any errors.

> **Security Note:** Lowering the security level carries a potential risk. Please ensure you only install extensions from trusted sources. You can change the setting back to `normal` after installation if you wish.

---

## Configuration

All extensions can be configured in the settings panel without needing to reload the UI.

1.  Click the **Settings** icon (⚙️) in the ComfyUI menu.
2.  Find the settings for **LucianoTools**:
    - `[✔] Run Timer`
    - `[✔] Path Display`
    - `[✔] Confirm Batch Run`
3.  Check or uncheck them as desired. The changes will apply instantly.

    <div align="center">
        <img src="https://github.com/user-attachments/assets/1146c72f-894a-44a2-ab5e-5786886e8c38" alt="Settings" >
        <p>Settings</p>
    </div> 

