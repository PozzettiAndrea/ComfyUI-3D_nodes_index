# ComfyUI-Actual-Denoise
Simple ComfyUI nodes to set the actual amount of noise in img2img, ensuring consistent behavior when changing schedulers.

## Installation
+ Use `Custom Nodes Manager > Install via Git URL` in ComfyUI-Manager
+ Or clone the repository into `custom_nodes/` manually (there are no external dependencies, so that's all)

## Usage
There are several ways to use these nodes:

1. simply connect `Actual Denoise` node to your KSampler, choose scheduler and choose actual_denoise.

   Be aware that actual_denoise and denoise are different values, so you need to use different values for it (see the next example)
   
<img width="971" height="707" alt="image" src="https://github.com/user-attachments/assets/1c8d795c-923e-4aee-94c5-d9a2295ebcd7" />

3. chain "Actual Denoise Inverse" and "Actual Denoise" to use usual denoise instead of actual_denoise.

   You can use any scheduler you're used to in the first Inverse node (that one will be used to map denoise into actual_denoise), and set scheduler you want to use right now in the second node
   
<img width="1304" height="690" alt="image" src="https://github.com/user-attachments/assets/067dfddc-01c8-46d9-b28a-25b8ef17dee0" />

4. use `(Step)` versions of the same nodes if you're using `KSampler (Advanced)` (`start_at_step`, `end_at_step` instead of `denoise`)

That way, when you change the scheduler but keep the `actual_denoise` value the same, the image will get the exact same amount of noise (unlike when you fix `denoise` directly).

## Explanation
### Short
Since different schedulers use different amount of noise on a certain step, different denoise values behave differently with different schedulers. 
So in order to simplify the img2img workflow and avoid manual denoise adjustments whenever you change schedulers, 
you can set `actual_denoise` (actual amount of noise) and then calculate `denoise` based on the scheduler you're using.

<img width="640" height="480" alt="showcase" src="https://github.com/user-attachments/assets/c645d1e7-6e50-48a0-a594-895cbd07252f" />

### Long
Suppose I generated an image with this basic txt2img workflow:

<img width="1815" height="885" alt="workflow (14)" src="https://github.com/user-attachments/assets/28a55a2b-b208-4f9d-95e1-aa211ca999f6" />
<img width="400" alt="ComfyUI_00043_" src="https://github.com/user-attachments/assets/8523df97-33a4-4e19-b05d-90d79959b868">

Then I want to do img2img to add some effects and fix some details. Here's the basic img2img workflow:

<img width="1858" height="899" alt="workflow (13)" src="https://github.com/user-attachments/assets/796d4213-5095-43bb-98e2-eddce922e001" />


So my original txt2img prompt was:
```
1girl,

amami haruka, idolmaster,

standing, singing, idol, looking at viewer, dynamic pose, outstretched arm, 

foreshortening, depth of field, blurry background, spotlight, 

official style,

absurdres, masterpiece, very aesthetic, best quality, very awa, very aesthetic, 
```

I'm adding these tags in order to add some effects and make lighting better:
```
vivid colors, saturated, glowstick, (sparkle:1.1), bokeh, light particles, light rays, (glowing eyes:0.95), (aura, green aura:1.2),
```

And also I add `dark` into negative prompt, because I noticed that it heavily impacts the model and the image tends to become much lighter.

After I've decided on prompts, I need to choose `denoise` value. I'll use the same sampler and scheduler for now. Here is what I get with different `denoise` values with `euler beta`:

<img width="1576" height="1786" alt="z" src="https://github.com/user-attachments/assets/3008b77a-2157-4b9e-aee4-206266d66580" />

Note how many green aura the model adds depending on the denoise, and how much it changes her hands. 
If my goal is to add some effects without changing the image too much (because I like how her hands look on the original image), 
the sweet spot would probably be around 0.55. Values >=0.65 change her left hand, while values <=0.45 don't add enough effects (0.6 makes the hand look malformed, so I choose 0.55 or 0.5).

Now suppose I want to change the scheduler (and optionally sampler). Let's use `uni_pc kl_optimal`:

<img width="1576" height="1786" alt="z" src="https://github.com/user-attachments/assets/b282d451-f0c4-4fe2-8e84-3292780b8a38" />

As you can see, now the same sweet spot would be around 0.6. Why is that? 
That happened because of how KSampler uses denoise value: it simply multiplies your number of steps by `1 / denoise` to get the total number of steps, 
and then starts the denoising process from `total_steps - steps` step. 
That's a common misconception that `denoise=0.5` means that it adds 50% to the image and starts the denoising process from that. 
The actual amount of added noise depends on the scheduler that is being used.

The scheduler defines the relationship between `step / total_steps` (percentage of steps) and the amount of noise on that step. 
Here's how you can see the actual plot (thanks to [KJNodes](https://github.com/kijai/ComfyUI-KJNodes)):

<img width="1414" height="507" alt="workflow (15)" src="https://github.com/user-attachments/assets/a8858f96-7e4c-4e69-b390-51b7598b5c7c" />

Here are plots for some schedulers (it might be difficult to see the difference just by looking at the graph):

<img width="808" height="484" alt="z" src="https://github.com/user-attachments/assets/3d120419-917e-4833-b1e5-ebf13dea0ddf" />

The effect might not seem relevant to you (0.5 vs 0.6), but in different img2img scenarios that would have a different effect. 
Personally, I always kept in mind something like "if I switch from simple to kl_optimal I need to also raise the denoise a bit".

So what's the solution? Of course you can manually adjust denoise whenever you vary the scheduler, 
but another solution is to choose not the `steps / total_steps`, but the actual amount of noise. 
Instead of setting `denoise` you can set `actual_denoise` (actual amount of noise) and then calculate `denoise` based on the scheduler you're using.

<img width="640" height="480" alt="showcase" src="https://github.com/user-attachments/assets/c645d1e7-6e50-48a0-a594-895cbd07252f" />
