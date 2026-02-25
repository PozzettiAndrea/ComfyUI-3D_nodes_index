> [!IMPORTANT]
> Delete the Set node after using to ensure that the URL is not saved within any workflow or image metadata.

# ComfyUI-DiscordWebhook
A very simple Discord webhook integration node for ComfyUI that lets you post images and text.

# Usage
On first use, you will need to use the "Set Discord Webhook" node to set your webhook URL. Create a blank workflow and add the two nodes from the Discord category for Set and Use Discord Webhook.

Connect them together and you should see a test image sent to your Discord channel if you configured your webhook correctly.
![InitialSetup](https://github.com/user-attachments/assets/17f6d333-612f-44fa-9814-b5144104eefb)
![SetupResult](https://github.com/user-attachments/assets/fc4bfde1-81c1-4302-95ac-5d7540b26d98)

Delete the Set node after using to ensure that the URL is not saved within any workflow or image metadata.

# How to Create a Webhook URL
https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks

# Installation: 
> [!NOTE]  
> Recommended to install ComfyUI-Manager and then search for and install this extension from within the manager: https://github.com/ltdrdata/ComfyUI-Manager?tab=readme-ov-file#installation
# 

Clone or download this repo into your ComfyUI/custom_nodes folder.


![image](https://github.com/user-attachments/assets/71450181-a788-4fc7-ad5f-236c994100c1)
![image](https://github.com/user-attachments/assets/eb5a0bc5-1c7f-4aec-9bb6-e7a11de946b8)


# Modules: 
> [!IMPORTANT]  
> Install discord_webhook[async] module with pip.
#

# For Windows:
.\python_embeded\python.exe -s -m pip install --upgrade discord_webhook[async]

Ex. custom_launcher.bat
```
.\python_embeded\python.exe -s -m pip install --upgrade discord_webhook[async]
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build
pause
```

# For Linux:

./bin/python -s ./bin/pip install --upgrade discord_webhook[async]

Ex. custom_launcher.sh
```
./bin/python -s ./bin/pip install --upgrade discord_webhook[async]
./bin/python -s ./main.py
pause
```
# License
> [!IMPORTANT]
> Most of my work is under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (See the included LICENSE or visit (https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html#SEC1)
> <br></br>
> In summary, you may make modifications and derivatives of this work as long as:
>
> + The work is licensed under LGPLv2.1
> 
> + The source is made freely available
> 
> + You link back to my original source
> 
> + My original copyright notices are preserved without modification
> 
> + Any files modified carry prominent notices stating that you changed the files and the date of any change.

> [!NOTE]
> ### Distributing this work in it's entirety and without modfication such as in a pack or content delivery system is perfectly fine and is not subject to the scope of this license.
