# ComfyUI-DenoiseChooser

![Image of the node](https://i.imgur.com/RlR6q2w.png)  
[Use case](https://imgur.com/e8ncI1s)

In my personal workflow I frequently swap between using a empty latent image and an upscaled image, which meant changing the denoise value each and every time I swap which got old fast  
This automatically chooses the appropiate denoise value depending on if the latent is empty or not

It gets placed under 'advanced' in the 'Add Node' menu

### What does it do?
The latent gets passed straight through unaltered, if it's empty (i.e from a "Empty Latent Image" node) FLOAT outputs the first value, otherwise it outputs the second value

#### Bonus feature
It accept both values between 0-1 and 1-100. If it's greater than 1 then it gets divided by a hundred. So 0.75 and 75.0 gives the same output