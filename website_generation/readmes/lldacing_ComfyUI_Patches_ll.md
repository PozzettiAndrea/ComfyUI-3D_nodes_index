[中文文档](README_CN.md)

Add some hooks method. Such as: `TeaCache` and `First Block Cache` for `PuLID-Flux` `Flux` `HunYuanVideo` `LTXVideo` `MochiVideo` `WanVideo`.

Need upgrade ComfyUI Version>=0.3.17

## Preview (Image with WorkFlow)
![save api extended](example/workflow_base.png)

Working with `PuLID` (need my other custom nodes [ComfyUI_PuLID_Flux_ll](https://github.com/lldacing/ComfyUI_PuLID_Flux_ll))
![save api extended](example/PuLID_with_teacache.png)


## Install

- Manual
```shell
    cd custom_nodes
    git clone https://github.com/lldacing/ComfyUI_Patches_ll.git
    # restart ComfyUI
```

## Nodes
- FluxForwardOverrider
  - Add some hooks method support to the `Flux` model
- VideoForwardOverrider
  - Add some hooks method support to the video model. Support `HunYuanVideo`, `LTXVideo`, `MochiVideo`, `WanVideo`
- DitForwardOverrider
  - Auto add some hooks method for model (automatically identify model type). Support `Flux`, `HunYuanVideo`, `LTXVideo`, `MochiVideo`, `WanVideo`
- ApplyTeaCachePatch
  - Use the `hooks` provided in `*ForwardOverrider` to support `TeaCache` acceleration. Support `Flux`, `HunYuanVideo`, `LTXVideo`, `MochiVideo`, `WanVideo`
  - In my test results, the video quality is not good after acceleration for `MochiVideo`
- ApplyTeaCachePatchAdvanced
  - Support `start_at` and `end_at`
- ApplyFirstBlockCachePatch
  - Use the `hooks` provided in `*ForwardOverrider` to support `First Block Cache` acceleration. Support `Flux`, `HunYuanVideo`, `LTXVideo`, `MochiVideo`, `WanVideo`
  - In my test results, the video quality is not good after acceleration for `MochiVideo`
- ApplyFirstBlockCachePatchAdvanced
  - Support `start_at` and `end_at`

## SpeedUp reference
### TeaCache (rel_l1_thresh value)
|              | Original | 1.5x | 1.8x | 2.0x |
|--------------|----------|------|------|------|
| Flux         | 0        | 0.25 | 0.4  | 0.6  |
| HunYuanVideo | 0        | 0.1  | -    | 0.15 |
| LTXVideo     | 0        | 0.03 | -    | 0.05 |
| MochiVideo   | 0        | 0.06 | -    | 0.09 |
| WanVideo     | 0        | -    | -    | -    |

Note: "-" indicates small speedup, low quality or untested. WanVideo's different models have different acceleration effects.

### First Block Cache (residual_diff_threshold value)
|              | Original | 1.2x | 1.5x | 1.8x |
|--------------|----------|------|------|------|
| Flux         | 0        | -    | -    | 0.12 |
| HunYuanVideo | 0        | -    | 0.1  | -    |
| LTXVideo     | 0        | 0.05 | -    | -    |
| MochiVideo   | 0        | -    | 0.03 | -    |
| WanVideo     | 0        | -    | 0.05 | -    |

Note: "-" indicates small speedup, low quality or untested.


## Thanks

[TeaCache](https://github.com/ali-vilab/TeaCache)  
[ParaAttention](https://github.com/chengzeyi/ParaAttention)  
[Comfy-WaveSpeed](https://github.com/chengzeyi/Comfy-WaveSpeed)
