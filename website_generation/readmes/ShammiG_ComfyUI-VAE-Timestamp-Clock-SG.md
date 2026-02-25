# ComfyUI VAE Timestamp Clock SG
Shows Total Time Taken Only for the VAE Decode. Also shows the Timestamps for VAE start/stop.              
Can be used with my Automatic Clock intiliazation node: [ComfyUI-Show-Clock-in-CMD-Console-SG](https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG)
                
Since VAE decode in video workflows takes so much time, whereas VAE decode of Image-only workflows takes only a few seconds, so it doesn't make sense to add it globally like the [ComfyUI-Show-Clock-in-CMD-Console-SG](https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG) node for every workflow.         

So this node kind had to be its own thing, add to any workflow you want without cluttering the Console too much.

<img width="1920" height="400" alt="pc" src="https://github.com/user-attachments/assets/ce2c4084-e95c-4950-b6b8-01fe536c0197" />
<br>
<br>    
      
So this has **two nodes**, First **[VAE Clock Start(Latent)-SG]** passes through latent data (every type, including tiled), the other **[VAE Clock Stop(Image)-SG]** passes through image data and calculates total time taken for VAE decode.         
       
<img width="1920" height="800" alt="vae decode" src="https://github.com/user-attachments/assets/b394d54b-801e-4d91-95a5-98d229d465c4" />


<img width="1772" height="750" alt="tiled decode" src="https://github.com/user-attachments/assets/c6e1d722-bac1-4a8d-8f18-4db226c00cde" />
<br>
<br>    

# Installation:
**1.** Clone this repository into your **ComfyUI/custom_nodes** directory:    
       
    git clone https://github.com/ShammiG/ComfyUI-VAE-Timestamp-Clock-SG.git  
      
**2.** **Restart ComfyUI and Refresh browser if already open**

**Add the two nodes** like shown in above images **in your workflow** and you will have console output next time you run workflow.       
<br>
<br>

# Do check out this node that shows Clock timestamps in CMD console     
 [ComfyUI-Show-Clock-in-CMD-Console-SG](https://github.com/ShammiG/ComfyUI-Show-Clock-in-CMD-Console-SG) 
<br>
<br>
<br>
**This was made possible with the help of Perplexity Pro : Claude 4.5 Sonet**      
   Big Shoutout to them.

        
