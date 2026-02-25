# ComfyUI-MaskBatchPermutations
Provides two nodes, Permute Mask Batch and Combinatorial Detailer.

## Permute Mask Batch
Passing a mask batch (e.g. out of [SEGS to Mask Batch](https://github.com/ltdrdata/ComfyUI-Impact-Pack)) will return a new mask batch representing all the possible combinations of the included masks. So, a mask batch with two masks, "A" and "B, will return a new batch containing an empty mask, an empty mask & A, an empty mask & B, and an empty mask & A & B.

### example workflow
![An image embedding a workflow showing this node being used with a mask batch with three items.](workflow_example.png)
This image contains an embedded workflow.

## Combinatorial Detailer
Similar to Permute Mask Batch but accepts a mask batch, a base image, and then a batch of candidate images (for example, the batched outputs of several separate detailer passes using different prompts or seeds). Provides a batch of images representing the possible combinations of the base image, masks and candidates. Be advised that this can create very large batches - a set of masks representing three regions and with two candidate images will generate (2 + 1)<sup>3</sup> combinations (27) as each mask area will present with either the base image, or one of the two candidates.

### example workflow
In this example, I have given both detailers deliberately divergent prompts to make it clearer in the example output what is going on.
![An image embedding a workflow showing this node being used with a mask batch with three items and two candidates.](workflow_combi.png)

# why?
"Automatic" face detailing without direct operator intervention usually works well, but occasionally it wrecks an otherwise good face. Instead of having to hand compose them back together in something like GIMP and fix the metadata, I decided to create this instead.
