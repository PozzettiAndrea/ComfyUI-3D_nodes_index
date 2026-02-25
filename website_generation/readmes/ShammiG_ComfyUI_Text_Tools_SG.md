# ComfyUI Text Tools SG

#    ❗Attention❗
**Switch Node 2.0 OFF, If comfyUI version 0.3.76 or newer**
<br>

![dd](https://github.com/user-attachments/assets/93e17ceb-225d-4121-9e97-a81bf0b734f7)

**Reason:** With new ComfyUI update it changed the frontend from Lite graph rendering to Vue with **nodes 2.0**.         
&emsp;&emsp;&emsp; &nbsp; So, now it requires rewriting and troubleshooting with about 2000 lines of code!      
&emsp;&emsp;&emsp; &nbsp; which i am not currently leaned towards into.

---
Text Tools Nodes Info
---
**Text Editor node with Markdown editing** plus **quick shortcuts**, **Text Viewer node**, with extra features plus **Text Merge, Text Save and Load Text from anywhere** nodes.       
**Also supports json and md formats**    
<br>
<img width="1861" height="932" alt="Text tools all nodes screenshot" src="https://github.com/user-attachments/assets/47a3f3f4-d546-455f-9036-7ca10312f1ce" />
<br>

A little set of basic Text related nodes:            
● Text Tools **Editor**-SG        
● Text Tools **Viewer**-SG          
● Text Tools **Load Text Json md**-SG         
● Text Tools **Load Text json md From Anywhere (FilePath)**-SG         
● Text Tools **Merge Text**-SG        
● Text Tools **Merge Text Multi**-SG       
● Text Tools **Save Text json md File**-SG                           
<br>
<img width="1452" height="1016" alt="Text Tools all nodes" src="https://github.com/user-attachments/assets/0e2ef49c-141f-4a45-9fe4-27ae107cb4c7" />
<br>

**Text Editor** and **Text Viewer** nodes have these **added features:**
<br>
**Useful Buttons:**        
🌙 &emsp;Day / Night Theme         
Aa &emsp;Change Font Size (6-72)           
Ⓜ️&emsp;Toggle Markdown Preview      
🪶 &emsp;Toggle Editing          
🗑️ &emsp;Delete all text          
📋 &emsp;Copy all / selected text to clipboard          
☑️ &emsp;Select all text          
📄 &emsp;Paste from clipboard          
🔍 &emsp;Search and highlight word/s          
🎯 &emsp;Filter Lines          
💾 &emsp;Save / Export File            
&nbsp;{}&nbsp; &emsp;Toggle Pretty Json    
↔️&emsp;Toggle Text Wrap 
<br>
<img width="1358" height="901" alt="Screenshot 2025-12-02 191306" src="https://github.com/user-attachments/assets/e19ffd7f-a3ca-4212-b285-46f53086c1ad" />
<br>

**Quick Markdown Editing Shortcuts:**     
<br>
⊞&nbsp; &emsp;Insert Table           
**B**&nbsp; &emsp;**Bold Selected Text**            
*I* &nbsp; &emsp; ***Italic*** *Selected Text*         
~~S~~&nbsp; &emsp; Strikethrough ~~Selected Text~~           
<>&emsp;`inline code`     
**{}**&nbsp; &emsp; Code Block      
          
**H**&nbsp;&emsp; Heading / Title    

●&nbsp; &emsp;Bullet Points  

**1.**&nbsp; &emsp;Auto Numbered List 

🔗&nbsp;&emsp;Hyperlink    

 **"**&nbsp; &emsp; Quote Text 
 
---
     
-&nbsp; &emsp; Horizontal rule 

---
<br>
 
 <br>

● **Load Text from anywhere**: Load text, Json, markdown file from anywhere.         
Right-click the file in File Explorer and select 'Copy as path' and paste in the box above. 
<br>

● **Merge Text Multi:** Merge **upto 5** text inputs or entered custom text in a box.
< br>

● **Both text merge** nodes also have a custom separator( eg. separate the text to be joined with comma ,)               
and custom order of apperance support and enable / disable option (no need to disconnect noodles / strings)   
<br>
<br>
# Installation:   
<br>

**OPTION 1 :** If you have [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager):       
        
**1.** Click on Manager>Custom Nodes Manager           
            
**2.** you can directly search ComfyUI_Text_Tools_SG **OR** my Username **ShammiG** and click install.           
              
**3.** Restart comfyUI from manager: 
<br>

***TIP!*** Make sure your node cache is updated (it will be already if you haven't changed settings)
<br> 

**OPTION 2 :** If you don't have comfyUI Manager installed:           
          
**1.** Open command prompt inside ComfyUI/custom_nodes directory.              
       
**2.** Clone this repository into your **ComfyUI/custom_nodes** directory:    
       
    git clone https://github.com/ShammiG/ComfyUI_Text_Tools_SG
      
**3.** **Restart ComfyUI**             
  Search and add the desired node to your workflow.
<br>
<br>

● **This node uses markdown library of [Markdown-it](https://github.com/markdown-it/markdown-it)**
<br>

# Also checkout my other nodes: 
[ComfyUI Simple Readable Metadata-SG](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG))
<br>

View Image Metadata of ComfyUI as well as of ForgeUI or Automatic 1111 generated images in Easily Readable Format
<br>

<img width="1464" height="953" alt="er" src="https://github.com/user-attachments/assets/d4d61233-d112-4d9d-a28a-062069e053a5" />
<br>
<br>

[ComfyUI-Show-Clock-in-CMD-Console-SG](https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG)
<br>

This comfyUI node automatically intializes at startup and displays the clock timestammp in CMD console when Process starts and ends.
<br>

<img width="1124" height="963" alt="gf" src="https://github.com/user-attachments/assets/963cf6be-6870-47df-a655-2a2a01164cdf" />
<br>


# Appreciate and support my work on [Patreon](https://www.patreon.com/c/ShammiG)
<br>
<br>

**This was made possible with the help of Perplexity Pro : Claude 4.5 Sonnet and Gemini 3 Pro**      
   Big Shoutout to them.

 
