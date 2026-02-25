# comfy-hires-color-adjust
Adjust the color of image before hires.fix

## How to use

1. Download this extension and place it in custom_nodes/
2. Get the node via Custom/Hires/HiresColorAdjustmentNode
3. Connect this after upscaling and do the rest of hires.fix
4. Have fun!

## Options
* Each parts are separated into **Highlights**, **Middles** and **Shadows**
* All of them have **Red**, **Green**, **Blue**, **Brightness** and **Contrast**
* Red, Green and Blue defaults to _0_, can go up to _100_ and below to _-100_
  Each color corresponds to the opposite color when they have below 0
  * **Red < - > Cyan  
    Green < - > Magenta  
    Blue < - > Yellow**
* Brightness and Contrast defaults to _1.0_, can go up to _10.0_ and below to _0.0_
