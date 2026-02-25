## ComfyUI-FDG
Implementation of [Guidance in the Frequency Domain Enables High-Fidelity Sampling at Low CFG Scales](https://arxiv.org/abs/2506.19713) for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Thanks to the FDG researchers for making their code public.

FDG improves image quality at low guidance scales and avoids the drawbacks of high CFG scales by design.

Paper: https://arxiv.org/abs/2506.19713




## Usage

To use FDG, just place the `FDGNode` (located in the advanced/model category) in front of the `KSampler` node in your workflow.

Basically disables cfg values ​​within KSampler.

Testing on SDXL only.

## Inputs

- `guidance_scale_high`: Guidance scale for high-frequency details.
- `guidance_scale_low`: Guidance scale for low-frequency structures.
- `levels`: Number of pyramid levels for frequency decomposition. For levels higher than 2, it operates using linear interpolation for each frequency.
- `fdg_steps`:  Number of initial steps where FDG is applied before switching to CFG. Beyond this threshold, the cfg value from the KSampler node takes effect. When cfg equals 1, the guidance_scale_high value is used. If the threshold exceeds the total number of steps, FDG is automatically applied to all steps.

## Citation

If you use this implementation in your research, please cite the original paper:
```
@misc{sadat2025guidance,
    title={Guidance in the Frequency Domain Enables High-Fidelity Sampling at Low CFG Scales},
    author={Seyedmorteza Sadat and Tobias Vontobel and Farnood Salehi and Romann M. Weber},
    year={2025},
    eprint={2506.19713},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
