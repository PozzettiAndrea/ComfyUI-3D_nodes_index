# Negative-attention-for-ComfyUI-
Takes the difference in between the positive and negative conditioning at the cross attention.

This is an experiment.

Only tested with SDXL and SD 1.X.

Will not work with Flux (see bottom note).

This allows to:

- Get a negative influence without generating a negative prediction
- Let the unconditional prediction be unconditional
- Or doubling down by having the same done for the negative prediction (overblown results are to be expected unless using an anti-burn or low CFG scale)

In order to do this for now the negative conditioning is sneaked to the attention by being concatenated to the positive by using a special node.

![image](https://github.com/user-attachments/assets/c43caf96-8f43-4c1c-8813-9a70a646f3cd)

They are then split at the half before the cross attention.

Like any model patcher, it is to be plugged right after the model loader:

![image](https://github.com/user-attachments/assets/a27d9796-e563-4661-985e-4ee53c37ebb0)

An example workflow is provided.

## Example:

No modification:

![00022UI_00001_](https://github.com/user-attachments/assets/537999fd-a594-4eb9-ad60-28c4958172ea)

Difference in positive and negative conditionings:

![example workflow png](https://github.com/user-attachments/assets/471f2b3f-53be-41aa-a940-5ee3eacb57d5)

Difference in positive conditioning, negative conditioning empty:

![00023UI_00001_](https://github.com/user-attachments/assets/af14ad61-8640-42b8-82ef-143dded04f10)

No modification using empty negative conditioning:

![00025UI_00001_](https://github.com/user-attachments/assets/729bdeed-2dfe-4c87-923a-aa0eb5294e45)



## Note

I haven't managed to make this work with anything but SDXL / SD1.5

I did spend two hours looking for how to patch the equivalent of the cross attention for Flux but did not find how (like the keywords for the patch or something).

Any help appreciated!
