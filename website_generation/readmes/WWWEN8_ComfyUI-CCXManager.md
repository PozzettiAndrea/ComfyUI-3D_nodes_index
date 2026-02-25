# ComfyUI-CCXManager
## <a href="./README.md">English</a> >> <a href="./README_ZH.md">中文版</a>
<div align="center">
<img width="1002" height="748" alt="a111aeda-03ba-4d81-aff4-45690be0777d" src="https://github.com/user-attachments/assets/cc730d43-ca7c-47a3-bafe-21cdc872cfae" />
<br>
  <p><strong>SD-PPP Plugin Update Assistant - Automatically manages Photoshop-side plugin updates</strong></p>
</div>

CCXManage is an auxiliary node specifically developed for the SD-PPP plugin.

Users who have previously used the SD-PPP node found it very troublesome. When the ComfyUI side of the SD-PPP node was upgraded, the Photoshop side required a more complex manual installation of the plugin, causing the SD-PPP to not be able to use the latest features of the Photoshop-side plugin in a timely manner, resulting in a poor experience. Especially since the SD-PPP node is updated at a very high frequency, because the SD-PPP node developers, in order to better improve the node, receive feedback on BUGs or suggested features from the community and group testers, and they work hard to fix BUGs or update features at the first opportunity. A big thumbs up to the SD-PPP node developers!!!

- ✅ Automatically remembers settings and restarts ComfyUI to automatically detect SD-PPP updates
- ✅ Supports running both SD-PPP node version 1.0 and version 2.0 simultaneously
- ✅ Supports downloading CCX from websites for updates
- ✅ Has intelligent detection functionality, only runs when SD-PPP has updates
- ✅ Provides visual operation information, displaying operation status in the ComfyUI console
- ✅ Add Comfyui side automatic update SDPPP node
- ✅ Latest feature: Automatic creation of installation directory folder function (Good news for those who haven't installed SD-PPP yet, run this workflow, and your SD-PPP will be fully automatically installed and subsequently maintained and updated)

> **Note:** Only supports locally deployed ComfyUI, not cloud-based ComfyUI

## 🛠️ Installation Requirements

1. Photoshop software installed (version ≥ 24)
2. The latest version of the SD-PPP node installed on the ComfyUI side
3. Requires proxy network support

## 📦 Installation Methods

### Method 1: Install via ComfyUI Manager
Search for "ComfyUI-CCXManager" in ComfyUI Manager and install it

### Method 2: Git Clone (Recommended)
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/WWWEN8/ComfyUI-CCXManager.git
```

### Method 3: Manual Installation
1. Download the ZIP file of this project
2. Extract it to the `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

## 🚀 Usage Instructions

The CCXManage node has 3 nodes:
Photoshop side automatic update SDPPP2.0/
Photoshop side automatic update SDPPp1.0/
Comfyui side automatic update SDPPP

### source_type selection input:

1. url: (Recommended) Network download, default is fine

2. local_path: Install local .CCX file, .CCX file is usually in the static folder under the SD-PPP installation directory, copy the .CCX path to the target_path box, not recommended

Example:

Photoshop side automatic update SDPPP1.0 node: Fill in "H:\ComfyUI\custom_nodes\sd-ppp\static\sd-ppp_PS.ccx" in the target_path box, note that the path ends with sd-ppp_PS.ccx

Photoshop side automatic update SDPPP2.0 node: Fill in "H:\ComfyUI\custom_nodes\sd-ppp\static\sd-ppp2_PS.ccx" in the target_path box, note that the path ends with sd-ppp2_PS.ccx

### source_path input:

Input the .CCX download website, keep the default download website, no need to modify

1. Photoshop side automatic update SDPPP1.0, node default website: https://gitee.com/zombieyang/sd-ppp/raw/main/static/sd-ppp_PS.ccx
 
2. Photoshop side automatic update SDPPP1.0, node default website: https://gitee.com/zombieyang/sd-ppp/raw/main/static/sd-ppp2_PS.ccx

### target_path input:

1. Photoshop side automatic update SDPPP1.0 node, input: sd-ppp_PS file path, such as:
<img width="700" height="285" alt="1" src="https://github.com/user-attachments/assets/47077615-98b7-4e40-b40a-009653a4101d" />
   
2.Photoshop side automatic update SDPPP2.0 node, input: sd-ppp2_PS file path, as follows:

<img width="745" height="234" alt="2" src="https://github.com/user-attachments/assets/a88f9c69-2b0b-420e-995c-c2e1c3efb3f8" />

github_repo_url input:
Detects the latest updates in GitHub repositories, enter the repository URL. Once an update is detected in the SD-PPP side node, activate and restart ComfyUI to run CCXManager for automatic updates. If there is no update, restarting will not run CCXManager for updates. Keep default, do not modify

Default SD-PPP node repository: https://github.com/zombieyang/sd-ppp.git

### auto_run_on_restart select input:
enable means to enable, automatically runs on ComfyUI restart, enabling the Photoshop plugin synchronization update feature. (Default)

disable means to disable, does not run on ComfyUI restart, disabling the Photoshop plugin synchronization update feature.

After enabling, you need to run it once for it to take effect. The next time ComfyUI restarts, the Photoshop plugin will automatically sync updates (same for disable)

### Partners who have previously installed Photoshop can also set it up to run this way:

<img width="427" height="801" alt="EN-1" src="https://github.com/user-attachments/assets/ed4eda7d-5bbb-466f-b511-805c71464231" />

After running the node, the console will display the running information as follows (you can also see the console running information after ComfyUI restart):

<img width="992" height="199" alt="93a36210-5723-4959-bd90-ebb561810540" src="https://github.com/user-attachments/assets/cc375204-2c64-416b-91b8-b4d96b4cf710" />

Check in Photoshop software whether the plugin is installed successfully


### Notes:
1.SDPPP plugin update assistant 1.0 latest node, target_path corresponds to "sd-ppp_PS file path"

2.SDPPP plugin update assistant 2.0 latest node, target_path corresponds to "sd-ppp2_PS file path"

3.If the installation path changes, re-change the path in the node settings, it will take effect after running the node

4.If the CCXManage node has functional updates that cause it to fail, please reconfigure the inputs according to the node's requirements

5.To check for SD-PPP node updates, you need to enable a proxy network to use it; without a proxy network, you can try to use local_path local CCX file to set as an alternative

6.Choose the installation path carefully, as updates will clear the contents of files in the path. Do not enter installation paths randomly for operations to avoid accidentally deleting important files

### 👨‍💻 Developer Information
Author: WWWEN8
GitHub: https://github.com/WWWEN8/ComfyUI-CCXManager
Issue feedback: Please submit an Issue in the GitHub repository
📄 License
This project is licensed under the MIT License - see the LICENSE file for details





















