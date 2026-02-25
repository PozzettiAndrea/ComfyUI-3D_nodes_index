# ComfyKit Custom Nodes

## LoraStackFiveSimple (LoRA S5)

Accepts 5 LoRAs to blend and a weight value to apply. It applies the same
weight to both the Model and CLIP as I never found myself with an obvious
positive result when desyncing them. Does not mean it cannot, I just do not
and therefore did this to save screen space on the home view of the workflow.

![lora1](https://github.com/user-attachments/assets/ef028970-74af-4d44-a514-745823c509f4)

## Typecaster
### (CLIP, Conditioning, Image, Latent, Model, VAE)

Recasts the input as typed output without doing anything to it. This helps with workflows where one node can output "anything" and send it to a node that can take "anything". These type of nodes often struggle the first time a workflow is loaded in the browser as their wiring accepts anything but may not notice what kind of anything it had until you queue a job once and let it fail.

In code it would be the same as being like `emptyLatent = (Latent)emptyLatent;`


![casters](https://github.com/user-attachments/assets/f6fcff9b-22a1-41bf-82c1-adf6a7cfd3cd)


