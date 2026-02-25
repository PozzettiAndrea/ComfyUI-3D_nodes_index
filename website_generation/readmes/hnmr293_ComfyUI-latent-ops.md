# ComfyUI-latent-ops

[日本語 ver.](./README_ja.md)

A collection of nodes for manipulating `LATENT` in ComfyUI.

All nodes are added under `hnmr/latent_ops`.

# Nodes

| Name | Function |
| --- | --- |
| AssertDims | Verify that the input `LATENT` has the specified number of dimensions |
| AssertShape | Verify that the input `LATENT` has the specified shape |
| LatentOperationNormalizeAlongAxis | Normalize along a specific axis |
| LatentOperationNormalize | Normalize across the entire tensor |
| LatentOperationLayerNorm | Apply layer normalization |
| LatentOperationInstanceNorm | Apply instance normalization |
| LatentOperationNormalizeMinMax | Normalize between minimum and maximum values |
| LatentOperationNormalizePercentile | Normalize based on percentiles |
| LatentOperationSigmoid | Apply sigmoid function |
| LatentOperationHardSigmoid | Apply hard sigmoid function |
| LatentOperationLogistic | Apply logistic function |
| LatentOperationTanh | Apply tanh function |
| LatentOperationHardTanh | Apply hard tanh function |
| LatentOperationSinh | Apply sinh function |
| LatentOperationCosh | Apply cosh function |
| LatentOperationReLU | Apply ReLU function |
| LatentOperationReLU6 | Apply ReLU6 function |
| LatentOperationLeakyReLU | Apply LeakyReLU function |
| LatentOperationELU | Apply ELU function |
| LatentOperationSELU | Apply SELU function |
| LatentOperationCELU | Apply CELU function |
| LatentOperationGELU | Apply GELU function |
| LatentOperationSiLU | Apply SiLU function |
| LatentOperationHardSwish | Apply HardSwish function |
| LatentOperationMish | Apply Mish function |
| LatentOperationSoftplus | Apply Softplus function |
| LatentOperationSoftmax | Apply Softmax function |
| LatentOperationSoftmin | Apply Softmin function |
| LatentOperationSoftsign | Apply Softsign function |
| LatentOperationReshape | Change the shape of `LATENT` |
| LatentOperationSlice | Extract a portion of `LATENT` |
| LatentOperationRoll | Shift `LATENT` |
| LatentOperationAddBroadcast | Add values with broadcasting |
| LatentOperationMulBroadcast | Multiply values with broadcasting |
| LatentOperationFill | Fill with specified value |
| LatentOperationAdd | Add another `LATENT` |
| LatentOperationMul | Multiply by another `LATENT` |
| LatentOperationClamp | Limit values with upper and lower bounds |
| LatentOperationClampMin | Limit values with lower bound |
| LatentOperationClampMax | Limit values with upper bound |
| LatentOperationApplyCFG | Apply CFG adjustment |
| LatentOperationSplitCFG | Split CFG into conditional and unconditional parts |
| LatentOperationInterpolate | Interpolate between two `LATENT` tensors |
| Latent01ToImage | Convert `LATENT` in 0-1 range to image |
| Latent11ToImage | Convert `LATENT` in -1 to 1 range to image (`z = x * 0.5 + 0.5`) |
| GetSigma | Get σ at a specific index from SIGMAS |
