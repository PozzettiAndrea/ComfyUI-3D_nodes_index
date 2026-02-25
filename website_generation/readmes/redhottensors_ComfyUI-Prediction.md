# ComfyUI-Prediction
Fully customizable Classifier Free Guidance for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

![Avoid and Erase Workflow](examples/avoid_and_erase.png)

Copyright 2024 by @RedHotTensors and released by [Project RedRocket](https://huggingface.co/RedRocket).

# Installation
Clone this repo into ``ComfyUI/custom_nodes`` or use [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

(Optional) If you want beautiful teal PREDICTION edges like the example apply [patches/colorPalette.js.patch](https://raw.githubusercontent.com/redhottensors/ComfyUI-Prediction/main/patches/colorPalette.js.patch) to ``ComfyUI/web/extensions/core/colorPalette.js``.

# Usage
All custom nodes are provided under <ins>Add Node > sampling > prediction</ins>. An example workflow is in ``examples/avoid_and_erase.json``.

Follow these steps for fully custom prediction:
1. You will need to use the <ins>sampling > prediction > Sample Predictions</ins> node as your sampler.
2. The *sampler* input comes from <ins>sampling > custom_sampling > samplers</ins>. Generally you'll use **KSamplerSelect**.
3. The *sigmas* input comes from <ins>sampling > custom_sampling > schedulers</ins>. If you don't know what sigmas you are using, try **BasicScheduler**. (NOTE: These nodes are **not** in the "sigmas" menu.)
4. You'll need one or more prompts. Chain <ins>conditioning > CLIP Text Encode (Prompt)</ins> to <ins>sampling > prediction > Conditioned Prediction</ins> to get started.
5. After your prediction chain, connect the result to the *noise_prediction* input of your **Sample Predictions** node.

Some utility nodes for manipulating sigams are provided under <ins>Add Node > sampling > custom_sampling > sigmas</ins>.

# Predictors

## Primitive Nodes
All other predictions can be implemented in terms of these nodes. However, it may get a little messy.

### Conditioned Prediction
Evaluates your chosen model with a prompt (conditioning). You need to pick a unique conditioning name like "positive", "negative", or "empty".

The names are arbitrary and you can choose any name, but the names may eventually interact with ControlNet if/when it's implemented.

### Combine Predictions
Operates on two predictions. Supports add (+), subtract (-), multiply (*), divide (/), [vector projection](https://en.wikipedia.org/wiki/Vector_projection) (proj), [vector rejection](https://en.wikipedia.org/wiki/Vector_projection) (oproj), min, and max.

``prediction_A <operation> prediction_B``

### Scale Prediction
Linearly scales a prediction.

``prediction * scale``

### Switch Predictions
Switches from one prediction to another one based on the timestep sigma. Use <ins>sampling > custom_sampling > sigmas > Select Sigmas</ins> to create a sub-ranges of timestep sigmas.

``prediction_B when current_sigma in sigmas_B otherwise prediction_A``

### Scaled Guidance Prediction
Combines a baseline prediction with a scaled guidance prediction using optional standard deviation rescaling, similar to CFG.

Without ``stddev_rescale``: ``baseline + guidance * scale``<br>
With ``stddev_rescale``: [See §3.4 of this paper.](https://arxiv.org/pdf/2305.08891.pdf) As usual, start out around 0.7 and tune from there.

### Characteristic Guidance Prediction
Combines an unconditioned (or negative) prediction with a desired, conditioned (or positive) prediction using a [characteristic correction](https://arxiv.org/pdf/2312.07586.pdf).

``cond``: Desired conditioned or positive prediction. This prediction should not be independent of the unconditioned prediction.<br>
``uncond``: Unconditioned or negative prediction.<br>
``fallback``: Optional prediction to use in the case of non-convergence. Defaults to vanilla CFG if not connected.<br>
``guidance_scale``: Scale of the independent conditioned prediction, like vanilla CFG.<br>
``history``: Number of prior states to retain for Anderson acceleration. Generally improves convergence speed but may introduce instabilities. Setting to 1 disables Anderson acceleration, which will require a larger max_steps and smaller log_step_size to converge.<br>
``log_step_size``: log<sub>10</sub> learning rate. Higher values improve convergence speed but will introduce instabilities.<br>
``log_tolerance``: log<sub>10</sub> convergence tolerance. Higher values improve convergence speed but will introduce artifacts.<br>
``keep_tolerance``: A multiplier greater than 1 relaxes the tolerance requirement on the final step, returning a mostly-converged result instead of using the fallback.<br>
``reuse_scale``: A multiplier greater than 0 retains a portion of the prior correction term between samples. May improve convergence speed and consistency, but may also introduce instabilities. Use with caution.<br>
``max_steps``: Maximum number of optimizer steps before giving up and using the fallback prediction.<br>
``precondition_gradients``: Precondition gradients during Anderson acceleration. This is strongly recommended, but may decrease result quality in specific cases where the gradients are reliably well-conditioned.

This node is extremely expensive to evaluate. It requires four full model evaluations plus two full evaluations for each optimizer step required.
It's recommended that you use the **Switch Predictions** node to skip CHG on the first timestep as convergence is unlikely and to disable it towards the end of sampling as it has marginal effect.

## Prebuilt Nodes

### Switch Early/Middle/Late Predictions
Convienence node similar to a three-way **Switch Predictions** node, where the number of ``early_steps`` and ``late_steps`` can be specified directly.

The whole applicable ``sigmas`` schedule should be provided to the node, and the schedule must be unambiguous when split. (Restart schedules can often be ambiguous.)

### Interpolate Predictions
Linearly interpolates two predictions.

``prediction_A * (1.0 - scale_B) + prediction_B * scale_B``

### CFG Prediction
Vanilla Classifier Free Guidance (CFG) with a positive prompt and a negative/empty prompt. Does not support CFG rescale.

``(positive - negative) * cfg_scale + negative``

### Perp-Neg Prediction
Implements https://arxiv.org/abs/2304.04968.

``pos_ind = positive - empty; neg_ind = negative - empty``<br>
``(pos_ind - (neg_ind oproj pos_ind) * neg_scale) * cfg_scale + empty``

### Avoid and Erase Prediction (v2)
Implements a modification of the Perp-Neg algorithm that avoids moving in the direction of the negative guidance.
The result is a guidance vector that should be recombined with the empty prediction using the **Scaled Guidance Prediction** node or addition in preparation for **Characteristic Guidance Prediction**.

``pos_ind = positive - empty; neg_ind = negative - empty``<br>
``pos_ind oproj neg_ind - (neg_ind oproj pos_ind) * erase_scale``

# Sigma Utilities
These utility nodes are provided for manipulating sigmas for use with the **Switch Predictions** node. These nodes are under <ins>sampling > custom_sampling > sigmas</ins>.

One important thing to keep in mind is that ComfyUI SIGMAS lists contain the ending output sigma, even though the model is not evaulated at this sigma.
So, a 30-step full denoising schedule actually contains 31 sigmas (indexed 0 to 30), with the final sigma being ``0.0``.

### Select Sigmas
This node is an alternative to the **Split Sigmas** built-in node. It allows you to specify the specific ``sigmas`` to ``select`` by 0-based index as a comma seperated list.

Ranges are supported with ``[start]:[end]`` syntax. The ending bound is exclusive and negative indices are supported, which index from the end of the list. Both start and/or end may be ommitted.

As a convienience, instead of specifing a list, you may specify ``mod <N>`` to select every N'th sigma. You can use this to easily alternate between prediction strageies.

If ``chained`` is disabled, the final sigma in the input list will be dropped. If you're chaning **Select Sigmas** nodes, you should enable ``chained`` in almost all cases.

If a specified index is out of range, it is ignored.

Examples, assuming a 10-timestep schedule with sigmas ``10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0``:

```
select: 0, 1, 2        chained: false  => 10, 9, 8
select: 0, 1, 3:6, -2  chained: false  => 10, 9, 7, 6, 5, 2
select: mod 2          chained: false  => 9, 7, 5, 3, 1
select: mod 3          chained: false  => 8, 5, 2
select: 100, 0, -100   chained: false  => 10

select: 5:             chained: false  => 5, 4, 3, 2, 1
select: :5             chained: false  => 10, 9, 8, 7, 6
select: :              chained: false  => 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

select: -1             chained: false  => 1
select: -1             chained: true   => 0
select: -1:-4          chained: true   => 0, 1, 2
```

### Split At Sigma
Similar to the built in **Split Sigmas** node, this node splits a list of sigmas based on the *value* of the sigma instead of the index.
This node takess a monotonically decreasing list of ``sigmas``, and splits at the earliest sigma which is less than or equal to the specified ``sigma``.

This node is primarily useful in setting up refiner models without having to reverse engineer the timestep schedule for differing numbers of steps.

### Log Sigmas
Prints the provided list of ``sigmas`` to the text console, with an optional ``message`` prefix to differentiate nodes. This is useful for debugging workflows.

If the sigmas list and message don't change, ComfyUI will not evaluate the node and so nothing will be printed.

# Limitations
ControlNet is not supported at this time.

Regional prompting may work but is totally untested.

Any other advanced features affecting conditioning are not likely to work.

# License
The license is the same as ComfyUI, GPL 3.0.
