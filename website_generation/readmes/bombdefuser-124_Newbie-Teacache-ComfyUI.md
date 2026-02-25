# Newbie-Teacache-ComfyUI

# Working with woct0rdho lighter Newbie Implementation (https://github.com/woct0rdho/ComfyUI/tree/newbie) // Use the new node TeaCache (Lumina2)

# Didn't test the calculator but it should be working

Major parts of these projects were used as base and are still on the nodes:

https://github.com/spawner1145/CUI-Lumina2-TeaCache // Huge thanks to spawner1145 o/

https://github.com/comfyanonymous/ComfyUI/pull/11284 // Most of the info about how to properly make TeaCache work with NewBie came from here o/

Most of the code here was written with the help of multiple coding assistants (mainly Claude and Gemini).
These nodes contain a patched loader for using TeaCache with NewBie and a Coefficient Calculator that I used to get an _okayish_ coefficient.

Just place the "TeaCache (Newbie)" on your workflow and hook up the model to it. By default it uses the best coefficient I could find ([0, 0, 0, 4.11423217, 0.36885889]) and a speed-focused l1 value (-20s gen time on a 3060 12GB using the default models and res_multistep + linear_quadratic). You can set it between 0.3 (slowest, best quality) and 0.8 (fastest, lower quality).

The Coefficient Calculator is more of a testing node (I don't even know if it's optimal or not), mess with it if you want to.

