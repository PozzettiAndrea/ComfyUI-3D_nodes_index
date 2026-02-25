# comfyui_image_filters

This is a simple image filter library for ComfyUI. It requires no fancy requirements, simply using the basic
torch and numpy libraries. It is designed to be simple and easy to use. It is super helpful for hinting to 
the AI model that you want an image to be dark, with green light. Just feed it a darked, green image, with
0.7 - 0.9 denoise, and you'll get a darker, greener output.

All nodes take an image as input, and output an image.
The nodes also all take a mask as an optional input, if a mask is provided:
- And the masked_area is set to modify_unmasked, the image will be modified outside the mask
- And the masked_area is set to modify_masked, the image will be modified inside the mask

This way, you can easily take an image that is "ok except for the ___" and modify only the area you want to change.
This is built into ComfyUI (not part of this plugin), simply right-click on a Preview Image node, and Copy (Clipspace),
then make a Load Image node, and right-click that, and then Paste (Clipspace). You will now be able to right-click it,
and "Open in MaskEditor" to create a mask.
On Windows, Shift+Click-and-drag to zoom in and out, and Ctrl+click-and-drag to move the mask.
On OSX, try it out and let me know. I'm not rich enough to buy Apple hardware. haha.

## HSL vs HSV

![HSL vs HSV](docs/hsl_vs_hsv.png)

HSV is best when you want to adjust the brightness of the color, rather than the lightness of the color. 
For an intuitive example, if you have green, in HSV, if you brighten it, you will get "bright green". In HSL, if you lighten it, you will get "light green" (closer to white).

See the image above for a visual representation of the difference between HSL Lighten and HSV Brighten.

## Examples

With all of these examples, clicking and dragging the PNG file onto the
ComfyUI window will load the workflow that generated the image.

### Masking

All of the nodes support an optional mask input. If a mask is provided, the masked_area option will determine how the mask is used.
This can be very useful if you have an image that's OK, but you want to change one thing about it, and prompting isn't working for you.
For example, you have a picture of a green hill with a dark storm. If you want the hill to be darker, you can mask it out.
If you want the storm to be darker, you can mask out the sky. It's kind of annoying to draw two masks, so
you can use the same mask, and just change the masked_area option to toggle between grass and sky.

![Masking Workflow](docs/workflows/mask_workflow.png)

### HSL Nodes

#### Levels (RGB)

Similar to the HSL slider, this node allows you to adjust the levels of the image.
Adjusting a single color channel will adjust the lightness of the image only in that color,
for example, if you set a "midtones" value of 0.5 for the red channel, the image will be adjusted so that
it is more brightly red. This is very handy if you want a particular color to be more prominent in the image.

Options:
- "channel": The channel to adjust. "red", "green", "blue", or "all".

For example, you want a spooky haunted house that's glowing red. But whenever you put "red" in the prompt, the house is painted red. You want a house that's dark,
you don't want a red house, you want a red glow. But you can turn down the blue and green, and turn up the red.
![Levels (RGB) Workflow](docs/workflows/levels_rgb_workflow.png)


#### Levels (HSL)

Similar to the Photoshop Levels slider, this node allows you to adjust the levels of the image.

Options:
- "shadows": Any lightness value below this will be clipped to black. (0 - 1)
- "midtones": Applies a gamma correction to the midtones. Values above 2 will darken the image, values below 1 will lighten the image. (0 - 100)
- "highlights": Any lightness value above this will be clipped to white. (0 - 1)

For example, you want a dark landscape, you want it to be green, but stormy. The model can't quite get the lighting on the grass right.

- ![Levels (HSL) Workflow](docs/workflows/levels_hsl_workflow.png)

#### Darken (HSL)

Darkens the image.


Options:
- "factor": The amount to darken the image. Shifts the lightness value towards black, a value of 0.5 will adjust the image so that pure white is 50% gray. A value of 1 will make the image completely black. Negative values will lighten the image.

For example, you want a dark dungeon corridor, but the model always wants it to be SO BRIGHT.
![Darken (HSL) Workflow](docs/workflows/darken_hsl_workflow.png)

#### Lighten (HSL)

Lightens the image. Red will become "light red" (pink), rather than "bright red".

Options:
- "factor": The amount to lighten the image. Shifts the lightness value towards white, a value of 0.5 will adjust the image so that pure black is 50% gray. A value of 1 will make the image completely white. Negative values will darken the image.

For example, you want a scorching bright desert, but the model LOVES shadows. You don't mind shadows, but they shouldn't be pitch black.
![Lighten (HSL) Workflow](docs/workflows/lighten_hsl_workflow.png)

#### Saturate (HSL)

Saturates the image (adds color).

Options:
- "factor": The amount to saturate the image. A value of 0 will leave the image unchanged. A value of 1 will completely saturate the image. Negative values will desaturate the image.

For example, you want a girl riding through Hobbiton, it's so verdant and lush and green there, and the model wants to go for a different art style.
![Saturate (HSL) Workflow](docs/workflows/saturate_hsl_workflow.png)

#### Desaturate (HSL)

Desaturates the image (removes color).

Options:
- "factor": The amount to desaturate the image. A value of 0 will leave the image unchanged. A value of 1 will completely desaturate the image. Negative values will saturate the image.

For example, you want a girl sitting like a lump in Hobbiton during the Scouring of the Shire, but the model only knows the Shire from the movies,
because the model didn't read the books. So it makes a lush green Hobbiton, but you want it to be a bit more desaturated, to match the mood.
![Saturate (HSL) Workflow](docs/workflows/desaturate_hsl_workflow.png)

#### Rotate Hue (HSL)

Rotates the hue of the image. Imagine a color wheel, with red at 0, green at 120, and blue at 240. This node will rotate the hue of the image.
This represents a color wheel of light. With red+blue being the complimentary color to green, this means that with a rotation of 180 degrees, red will become cyan, and blue will become yellow.
This is a very powerful tool for color correction, and can be used to create a wide variety of effects.
It is extremely useful if a model can do X, but it can only do X with a certain color. 
This node can be used to change the color of the image to match the color that the model is trained on.
For example, if a LoRA can do green shirts really well, but struggles to do red shirts, you can rotate the hue of the image from green to red, and the model will be able to do red shirts.
Best used with a mask, since otherwise it will also rotate the colors of the person wearing the shirt. This may not be necessary, since some models are able to do odd colors of skin,

Options:
- "degrees": The amount to rotate the hue of the image. A value of 0 will leave the image unchanged. A value of 180 will rotate the hue 180 degrees. Negative values will rotate the hue in the opposite direction.

For example, you want a universe in a bottle, but when you want a YELLOW universe in the bottle, the model ALWAYS just generates HONEY. NO! You want a UNIVERSE. IN A BOTTLE! YELLOW!
![Rotate Hue (HSL) Workflow](docs/workflows/hue_hsl_workflow.png)

### HSV Nodes

HSV is best when you want to adjust the brightness of the COLOR, rather than the lightness of the image. For example, in HSL, a lightness value of 0.5 will make the image 50% gray.
In HSV, a value of 0.5 will make the image 50% of the original color. This is very useful for adjusting the brightness of a color, rather than the brightness of the image.
In HSV, if you make green brighter, it still remains green. In HSL, if you make green brighter, it becomes white.

#### Levels (HSV)

Similar to the Photoshop Levels slider, this node allows you to adjust the levels of the image.

Options:
- "shadows": Any lightness value below this will be clipped to black. (0 - 1)
- "midtones": Applies a gamma correction to the midtones. Values above 1 will darken the image, values below 1 will brighten the image. (0 - 100)
- "highlights": Any lightness value above this will be clipped to white. (0 - 1)

For example, you want a glowing spooky haunted house in the dead of the night, but the model always wants there to be a well lit mystery light source always from everywhere.
The reason you want to use HSV, is because you don't want to desaturate the image, you want to make it darker, but you want the color to remain the same.

![Levels (HSV) Workflow](docs/workflows/levels_hsv_workflow.png)

#### Darken (HSV)

Darkens the image.

Options:
- "factor": The amount to darken the image. Shifts the lightness value towards black, a value of 0.5 will adjust the image so that pure white is 50% gray. A value of 1 will make the image completely black. Negative values will lighten the image.

Same uses cases as HSL Darken, but with the added benefit of preserving the color of the image.

#### Brighten (HSV)

Brightens the image. Red will become "bright red", rather than "light red".

Options:
- "factor": The amount to brighten the image. Shifts the brightness value towards white, a value of 0.5 will adjust the image so that pure black is 50% gray. A value of 1 will make the image as bright as possible, while preserving color hue. Negative values will darken the image.

Same uses cases as HSL Lighten, but with the added benefit of preserving the color of the image.

#### Saturate (HSV)

Saturates the image (adds color).

Options:
- "factor": The amount to saturate the image. A value of 0 will leave the image unchanged. A value of 1 will completely saturate the image. Negative values will desaturate the image.

Same uses cases as HSL Saturate, but...honestly I think this might be the exact same thing. Use this if you are a fan of HSV over HSL!

#### Desaturate (HSV)

Desaturates the image (removes color).

Options:
- "factor": The amount to desaturate the image. A value of 0 will leave the image unchanged. A value of 1 will completely desaturate the image. Negative values will saturate the image.

Same uses cases as HSV Saturate, but...honestly I think this might be the exact same thing. Use this if you are a fan of HSV over HSL!

#### Rotate Hue (HSV)

Rotates the hue of the image. Imagine a color wheel, with red at 0, green at 120, and blue at 240. This node will rotate the hue of the image.
This represents a color wheel of light. With red+blue being the complimentary color to green, this means that with a rotation of 180 degrees, red will become cyan, and blue will become yellow.
This is a very powerful tool for color correction, and can be used to create a wide variety of effects.
It is extremely useful if a model can do X, but it can only do X with a certain color. 
This node can be used to change the color of the image to match the color that the model is trained on.
For example, if a LoRA can do green shirts really well, but struggles to do red shirts, you can rotate the hue of the image from green to red, and the model will be able to do red shirts.
Best used with a mask, since otherwise it will also rotate the colors of the person wearing the shirt. This may not be necessary, since some models are able to do odd colors of skin,

Options:
- "degrees": The amount to rotate the hue of the image. A value of 0 will leave the image unchanged. A value of 180 will rotate the hue 180 degrees. Negative values will rotate the hue in the opposite direction.

Same uses cases as HSL Rotate Hue, but...honestly I think this might be the exact same thing. Use this if you are a fan of HSV over HSL!

#### Test Workflow

This workflow shows every single node, in both masked and unmasked mode.

![Test Workflow](docs/workflows/image_filter_test_workflow.png)
