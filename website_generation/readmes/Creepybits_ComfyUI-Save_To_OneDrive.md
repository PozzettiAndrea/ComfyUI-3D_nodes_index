# ComfyUI-Save_To_OneDrive
Saves images directly to OneDrive  using Microsoft's free API service

## Save Image To OneDrive 

<img width="301" height="364" alt="image" src="https://github.com/user-attachments/assets/0cf213dc-510b-44b5-8e0c-3c9209bfddd6" />

___

## IMPORTANT  

If you don't know how to get the onedrive_msal_token from Microsoft, I have made a very detailed guide on how. The guide is available on my Patreon: [Save Image To OneDrive - Guide](https://www.patreon.com/posts/comfy-space-129775871?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)   

___

### INSTRUCTIONS  
This node and it's code is completely free to use. It should be noted that you will have to get your own **onedrive_msal_token** with Microsoft in order for the node to work preperly. The **onedrive_msal_token** are needed to give the node access to your OneDrive and to create folders as well as save images and videos.  

The node will create folders you specify in the node itself if they aren't already created in your OneDrive. 

**Folder structure**: Rootfolder/subfolder/subfolder  

**Filename prefix**: All images with have the same name, so if the prefix is for example "IMG" all your saved images will be named IMG.png (alternatively IMG.jpeg or IMG.webp)  

**File Format**: Format available is PNG, JPEG and WEBP  
