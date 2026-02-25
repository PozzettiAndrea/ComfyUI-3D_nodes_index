# ComfyUI Show Clock in CMD Console SG


Simple node that **automatically intializes** at ComfyUI startup and shows a timestamp for tasks. **No extra dependencies needed**.            
This eliminates the need to add a Node to every workflow.           
          
<img width="1905" height="70" alt="Screenshot 2025-10-06 120952" src="https://github.com/user-attachments/assets/47838bc9-3b5c-4fa5-9880-51e6cd0eb37c" />
<br>
<br>

**Shows 24H clock time in CMD Console** when :
**Process starts**, Process **ends**, if Process is **interrupted** (both through UI and with Ctrl+C) and if Process **fails**.       

Also useful when there are several processes in queue and you want to find out at what specific time did certain process started or ended.         
        
**Color coded** for easier viewing, this also makes it easier finding any earlier interruptions or Processes in console.
                  
Processing time is displayed in **Minutes and seconds even if process takes less than 10 minutes** (By default, comfyUI shows only in seconds if processing takes less than 10 minutes.)           

               
**General :**         
          
<img width="1904" height="225" alt="proccesing begins and fisnished" src="https://github.com/user-attachments/assets/4c1128f0-25d7-4eeb-8371-b6f344a2796c" />
<br>
<br>

**When Interrupted with ComfyUI :**         
          
<img width="1896" height="144" alt="manual interrupt comfy" src="https://github.com/user-attachments/assets/04bebfaf-349e-411e-a83a-6c94d51b2d19" />
<br>
<br>

**When Interrupted from console with Ctrl+C :**          
              
<img width="1897" height="99" alt="console interrupt" src="https://github.com/user-attachments/assets/ffa8c97d-b558-4b0b-936d-c21235f8d6f6" />
<br>
<br>

**If processing fails for some reason :**          
            
<img width="1903" height="106" alt="fails" src="https://github.com/user-attachments/assets/1c8b1e84-9c40-48c1-b31a-23d382a63ed1" />
<br>
<br>

# Update:
Now the startup message appears below the server address to keep track of when comfyUI is restarted :         
           
<img width="1099" height="131" alt="dg" src="https://github.com/user-attachments/assets/e1b956af-1136-499e-9afb-af4a35e01d90" />

# Installation:

**OPTION 1 :** If you have [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager):        
          
**1.** Click on Manager>Custom Nodes Manager        
           
**2.** You can directly search ComfyUI-Show-Clock-in-CMD-Console-SG and click install.           
            
**3.** Restart comfyUI from manager and you will see this message in console:     

<img width="1905" height="70" alt="Screenshot 2025-10-06 120952" src="https://github.com/user-attachments/assets/47838bc9-3b5c-4fa5-9880-51e6cd0eb37c" />

<br>
<br> 

**OPTION 2 :** If you don't have comfyUI Manager installed:           
          
**1.** Open command prompt inside ComfyUI/custom_nodes directory.              
       
**2.** Clone this repository into your **ComfyUI/custom_nodes** directory:    
       
    git clone https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG.git  
      
**3.** **Restart ComfyUI**   
      
That's it. You will see the message during comfyUI startup in console:       
              
<img width="1905" height="70" alt="Screenshot 2025-10-06 120952" src="https://github.com/user-attachments/assets/47838bc9-3b5c-4fa5-9880-51e6cd0eb37c" />

<br>
<br>
      
# Also checkout these nodes for Showing Image Properties
[ComfyUI-Image_Properties_SG](https://github.com/ShammiG/ComfyUI-Image_Properties_SG.git)
<br>

![Screen Recording 2025-10-25 210725 (2)](https://github.com/user-attachments/assets/0725c002-edff-441e-ac71-1e51d3c28af8)


<br>
<br>  

# Also checkout this node that Shows times for Only VAE Decode on Cmd Console.
[ComfyUI-VAE-Timestamp-Clock-SG](https://github.com/ShammiG/ComfyUI-VAE-Timestamp-Clock-SG)
<br>
<br>

# Appreciate and support my work on [Patreon](https://www.patreon.com/c/ShammiG)
<br>
<br>
      
**This was made possible with the help of Perplexity Pro : Claude 4.0 Sonet**      
   Big Shoutout to them.
