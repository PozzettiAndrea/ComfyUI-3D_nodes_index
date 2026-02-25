# ComfyUI Image Properties SG
View general image properties of image: Dimension, Resolution, Aspect Ratio, Tensor Size (including batch)        
Also basic Metadata like: Model, Seed, Steps, CFG, Sampler, Scheduler
<br>

#    ❗Attention❗
**Switch Node 2.0 OFF, If comfyUI version 0.3.76 or newer**
<br>

![dsf](https://github.com/user-attachments/assets/126e2de6-9181-435e-b7f1-d0ecd849ada4)

**Reason:** With new ComfyUI update it changed the frontend from Lite graph rendering to Vue with **nodes 2.0**.         
&emsp;&emsp;&emsp; &nbsp; So, now it requires rewriting and troubleshooting with about 2000 lines of code!      
&emsp;&emsp;&emsp; &nbsp; which i am not currently leaned towards into.

---
 ComfyUI Image Properties SGs Nodes Info
---

**Four nodes for four different purposes:**                 
            
**1. Load Image and View properties:**            
                 
**2. Preview Image and View properties:**              
               
**3. Passthrough node to view Image Properties**         

**4. Save Image Format Quality Properties**
<br>
<br>
# Update : New Node, annoying bugs fixed and missing features added    

**New Node : Save Image Format Quality Properties**     
<br>
This new node, when connected to VAE decode output, displays all the same info as Load Image and View Properties including Model, Seed, Steps, CFG, Sampler, Scheduler used. So display info depends upon where it is added in workflow.  

**This node also has various output formats and their quality and compression options, so you can save image as : PNG, JPEG, WEBP, BMP, TIFF**

*❗DO take a note that only PNG supports saving comfyUI workflow and image metadata*           
<br>
      
# Details:

https://github.com/user-attachments/assets/767710c8-7558-4d37-ad00-84c0076f5c26


<br>
<br>

# Bug Fixes and missing features added:
● Critical Bug fixed where Save Image Node was not saving workflow and Json even in PNG format!           
       
● **Load Image and View properties now also displays : Model, Seed, Steps, CFG, Sampler, Scheduler used (check attached gif)**       
But the additional info can only be displayed while running/executing single node or while running workflow

 ● Added mask edit and output to Load Image and View Properties node (didn't realize it was missing until I had a use for it, Oops!)

 ● Fixed properties info not retaining while switching workflows.         

 ● removed the annoying node auto resize bug everytime running the workflow instead of staying custom size
<br>
<br>

**1. Load Image and View properties:** Load image (both upload or drag and drop) and **without running workflow** view image properties directly      
You can view Image Dimensions, Resolution in MP, aspect ratio, Tensor Size.         
If you execute this single node or run workflow now you can also view: Model, Seed, Steps, CFG, Sampler, Scheduler used (check attached gif)      
<br>

![Load Image And View Properties](https://github.com/user-attachments/assets/06c2e3bd-3f58-4688-ab87-67c6b5c83b40)


<br>
<br>

**2. Preview Image and View properties:** General Preview Image node **with view properties** feature.
<br>

![preview image and view properties](https://github.com/user-attachments/assets/6b790f7e-5479-41b9-bd83-a1dba18c8b50)
<br>
<br>

**3. View Image Properties:** Simple image passthrough node to view image properties
<br>

![view image properties](https://github.com/user-attachments/assets/ff92c784-36f2-44fe-a6a1-b13ebce841db)
<br>
<br>

# Installation:   
<br>

**OPTION 1 :** If you have [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager):       
        
**1.** Click on Manager>Custom Nodes Manager           
            
**2.** you can directly search ComfyUI-Image_Properties_SG or my Username ShammiG and click install.           
              
**3.** Restart comfyUI from manager:     
<br> 

**OPTION 2 :** If you don't have comfyUI Manager installed:           
          
**1.** Open command prompt inside ComfyUI/custom_nodes directory.              
       
**2.** Clone this repository into your **ComfyUI/custom_nodes** directory:    
       
    git clone https://github.com/ShammiG/ComfyUI-Image_Properties_SG
      
**3.** **Restart ComfyUI**             
  Search and add the desired node to your workflow.
<br>
<br>

# Also checkout this node that Shows Clock in Cmd Console.
[ComfyUI-Show-Clock-in-CMD-Console-SG](https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG)
<br>

<img width="966" height="337" alt="Screenshot 2025-10-24 183720" src="https://github.com/user-attachments/assets/3741d65e-b2d6-46b0-b838-a1d71f21a8f4" />
<br>
<br>



# Appreciate and support my work on [Patreon](https://www.patreon.com/c/ShammiG)
<br>
<br>

**This was made possible with the help of Perplexity Pro : Claude 4.5 Sonet**      
   Big Shoutout to them.



