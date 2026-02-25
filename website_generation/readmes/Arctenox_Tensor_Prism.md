# Tensor Prism - ComfyUI Node Pack

## Developer Notes
IMPORTANT: You might have to do a regular ModelMergeSDXL for the block layer merging, since I don't know if it works or not for V1.6.5+ Previous versions before 1.6.0 were deleted due to me realizing some of them were just copy-paste because I was tired but the current is what the node pack is supposed to be I made sure of it.

My First ComfyUI Node Pack, sort of vibe-coded with Gemini 2.5 Flash and Claude 4. Feel free to publish the models you make and link them to me I'd like to be able to see the models, and see what they're about to see if I need to add more nodes or if the nodes are good and make really good quality checkpoint models. This is also a node pack for those familiar with merging models.

# TensorPrism ComfyUI Node Pack

Advanced model merging and enhancement nodes for ComfyUI, providing sophisticated techniques for blending, enhancing, and manipulating Stable Diffusion models with GPU-optimized memory management.

**Author**: Arctenox  
**Version**: 1.7.0  
**License**: GPL-3.0

## 📧 Contact & Support

- **Discord**: https://discord.gg/UVXPdkgedh
- **GitHub**: [@Arctenox](https://github.com/Arctenox)
- **Issues**: [GitHub Issues](https://github.com/Arctenox/Arctenoxs-Essentials_ComfyUI/issues)
- **CivitAI**: https://civitai.com/user/Arctenox
---
## Installation

### Method 1: Git Clone
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/Arctebix/Tensor_Prism.git
```
or
```bash
cd ComfyUI/custom_nodes/
https://github.com/Arctebix/Tensor_Prism
```

### Method 2: ComfyUI Manager
1. Open ComfyUI Manager
2. Search for "Tensor Prism"
3. Click Install

### Method 3: Manual Installation (OPTIONAL)
1. Download this repository
2. Place the folder in your `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

## Features

### Core Merging Nodes

- **Main Merge**: Advanced model merging with multiple interpolation methods (linear, slerp, cosine, directional, frequency, stochastic)
- **Prism**: Fast spectral merging with frequency-based blending techniques including spectral blend, frequency bands, magnitude weighting, adaptive mixing, and harmonic merging
- **Layered Blend**: Component-specific blending with separate controls for text encoder, UNet blocks, and time embeddings
- **SDXL Block Merge**: Granular control over individual SDXL UNet blocks with support for TIES merging and add difference methods
- **SDXL Advanced Block Merge**: GPU-optimized block merging with intelligent memory management for any GPU size (including 12GB and smaller cards)
- **Noise Injection Merge** (NEW in 1.7.0): Controlled noise injection during merging to escape local optima and discover emergent capabilities
  - **7 Noise Patterns**: Gaussian, Uniform, Structured, Layer-Scaled, Adaptive, Perlin, Gradient
  - **Minimal Overhead**: No significant memory or performance impact
  - **Focus Controls**: Target specific layers (attention, MLP) for noise injection
  - **Layer-Aware Scaling**: Automatic depth-based noise scaling with decay
  - **Norm Preservation**: Maintains tensor norms for stability
  - **Reproducible**: Seed-based random generation for consistent results

### Advanced Tensor Merging

- **Weighted Tensor Merge [Advanced]**: Sophisticated tensor-level merging with:
  - **6 Blend Modes**: Linear, Sigmoid, Cosine, Exponential, Logarithmic, Smoothstep
  - **Curve Power Control**: Adjust blend curve intensity for fine-tuned transitions
  - **Layer Scaling**: Uniform, depth-progressive, shallow-bias, or deep-bias scaling
  - **Preserve Extremes**: Option to keep 0/1 mask values unchanged
  - **Noise Injection**: Add subtle noise to break symmetry and create variations
  - **Smart Layer Detection**: Automatically detects and scales per-layer

### Smart Model Analysis & Merging

- **Analyze Model Weights**: Intelligent analysis of two models to calculate optimal per-block weights
  - **5 Optimization Methods**: Combined, Similarity, Variance, Gradient Magnitude, Entropy
  - **Configurable Targets**: Set target mean weights and standard deviations
  - **Weight Smoothing**: Apply smoothing to reduce variance across blocks
  - **Auto-Detection**: Automatically detect optimal merge ratios
  - **Memory Efficient**: CPU-based calculations to avoid GPU conflicts
  
- **Apply Merge Recipe**: Apply analyzed recipes to merge models with precision
  - **Recipe-Based Merging**: Use recipes from analysis for consistent results
  - **Multiple Merge Methods**: Weighted sum or add difference
  - **Strength Control**: Fine-tune recipe application strength
  - **Block-Level Precision**: Per-block weight application

### Model Analysis Tools (NEW in 1.6.0)

- **Model Analyzer**: Comprehensive model analysis and inspection
  - **Three Depth Levels**: Quick, Standard, or Deep analysis modes
  - **Architecture Analysis**: Examine block structure, layer counts, and component breakdown
  - **Statistical Analysis**: Parameter magnitudes, sparsity, distribution metrics
  - **Memory Profiling**: Detailed memory usage by component
  - **Model Comparison**: Side-by-side comparison of two models for merge compatibility
  - **Smart Recommendations**: Get merge suggestions based on model characteristics
  - **JSON Export**: Export analysis data for external processing
  
- **Model Comparator**: Quick compatibility checker for merging
  - **Fast Comparison**: Instant compatibility assessment
  - **Similarity Score**: Quantitative measure of model similarity
  - **Merge Recommendations**: Automatic suggestions based on similarity
  - **Simple Output**: Boolean compatibility flag for workflow logic

### Advanced Selection Nodes

- **Intelligent Tensor Selector**: Smart tensor-by-tensor selection between models based on various metrics
- **Competitive Model Selector**: Multi-model competition to select best tensors from multiple candidates

### Conversion and Processing Nodes

- **Epsilon/V-Pred Converter**: Pure converter between V-Prediction and Epsilon prediction types with configurable conversion strength and smart layer targeting

### Advanced Mask System

- **Model Mask Generator**: Create sophisticated masks for selective model merging with layer-based, block-based, attention-only, feedforward-only, custom patterns, random sparse, and depth gradient options
- **Weighted Mask Merge**: Apply masks to control where and how models are blended with tensor-level precision
- **Model Key Filter**: Memory-efficient filtering of model parameters with batch processing for large models
- **Mask Blender**: Combine multiple masks with various blending modes (Add, Multiply, Max, Min, Linear Blend, Exponential Blend)

### CLIP & VAE Processing

- **Advanced CLIP Merge**: Sophisticated CLIP merging with multiple interpolation methods:
  - **Linear**: Standard interpolation
  - **SLERP**: Spherical Linear Interpolation for smooth blending
  - **Cosine**: Cosine-based smooth transitions
  - **Weighted Average**: Magnitude-based weighting
  - **Spectral Blend**: Frequency domain blending with separate magnitude/phase control
  - Layer-specific bias controls for attention, feedforward, embedding, and normalization layers
  - Norm preservation options for maintaining model stability

- **VAE Merge**: Blend VAE models with various interpolation methods

### Model Transformation

- **Model Weight Modifier**: Memory-efficient weight modification with operations like multiply, add, set value, clamp magnitude, and scale max absolute value
- **Model Enhancer**: Advanced model enhancement capabilities

## Usage

### Basic Model Merging
Use the **Main Merge** node to blend two models with various interpolation methods:
- Connect two MODEL inputs
- Adjust merge ratio (0.0 = Model A only, 1.0 = Model B only)
- Choose merging method based on your needs:
  - **Linear**: Standard interpolation
  - **SLERP**: Spherical interpolation for smoother blending
  - **Cosine**: Smoother transitions with cosine curve
  - **Directional**: Vector-based interpolation
  - **Frequency**: FFT-based frequency domain blending
  - **Stochastic**: Random pattern-based merging

### Noise Injection Merging (NEW in 1.7.0)
Use the **Noise Injection Merge** node to inject controlled noise during merging, helping escape local optima and discover emergent capabilities:

1. **Connect Models**: Connect two MODEL inputs to merge
2. **Set Base Merge Ratio**: Start with 0.5 for balanced merging
3. **Choose Noise Pattern**: Select based on your goals:
   - **Gaussian**: Standard random noise (good general purpose)
   - **Uniform**: Even distribution (more controlled randomness)
   - **Structured**: Block patterns (maintains coherence)
   - **Layer-Scaled**: More noise in deeper layers (progressive exploration)
   - **Adaptive**: Noise based on similarity (high similarity = more noise)
   - **Perlin**: Smooth noise (organic variations)
   - **Gradient**: Directional noise (guided exploration)
4. **Adjust Noise Strength**: Start low (0.02-0.05) and increase if needed
5. **Target Layers** (Optional):
   - Enable `focus_attention` to target attention mechanisms
   - Enable `focus_mlp` to target feedforward layers
   - Leave both off to affect all layers
6. **Fine-tune** (Optional):
   - `layer_scaling_factor`: How much to increase noise in deeper layers (1.5 default)
   - `noise_decay`: How quickly noise decreases per layer (0.9 default)
   - `adaptive_threshold`: Similarity threshold for adaptive mode (0.3 default)
   - `preserve_norms`: Keep tensor magnitudes stable (recommended: True)

**Best Practices**:
- Start with **Gaussian** pattern and 0.03-0.05 strength for experimentation
- Use **Layer-Scaled** when you want deeper layers more affected
- Use **Adaptive** when models are very similar and need differentiation
- Use **Structured** for maintaining coherent patterns
- Enable `focus_attention` for style/content changes
- Enable `focus_mlp` for feature extraction changes
- Set seed for reproducible experiments

### Model Analysis Workflow (NEW)

1. **Analyze a Single Model**:
   - Connect model to **Model Analyzer** node
   - Choose analysis depth (Quick/Standard/Deep)
   - Enable desired analysis sections:
     - Architecture info (blocks, layers, components)
     - Layer statistics (magnitudes, sparsity)
     - Memory usage breakdown
   - Review comprehensive report with merge recommendations

2. **Compare Two Models**:
   - Connect both models to **Model Analyzer**
   - Connect second model to `compare_with` input
   - Get similarity scores and compatibility assessment
   - Receive recommendations based on model differences

3. **Quick Compatibility Check**:
   - Use **Model Comparator** for instant yes/no compatibility
   - Get similarity score for merge planning
   - Make workflow decisions based on compatibility boolean

**Example Workflow**:
```
[Load Model A] → [Model Analyzer] → [Read report]
                       ↓
              [Decide merge method]
                       ↓
[Load Model B] → [Main Merge/Prism] → [Output]
```

### Advanced Tensor Merging
The **Weighted Tensor Merge [Advanced]** node provides sophisticated control:

1. **Choose Blend Mode**:
   - **Linear**: Standard interpolation
   - **Sigmoid**: Smooth S-curve for natural transitions
   - **Cosine**: Smooth cosine interpolation
   - **Exponential**: Accelerating/decelerating curves
   - **Logarithmic**: Compressed dynamic range
   - **Smoothstep**: Hermite interpolation

2. **Adjust Curve Power**: Control the intensity of non-linear curves (0.1 to 5.0)

3. **Layer Scaling Options**:
   - **Uniform**: Same influence across all layers
   - **Depth Progressive**: Increasing influence in deeper layers
   - **Shallow Bias**: More influence in early layers
   - **Deep Bias**: More influence in late layers

4. **Optional Enhancements**:
   - **Preserve Extremes**: Keep 0/1 mask values unchanged
   - **Noise Injection**: Add 0-10% noise for variation

### Smart Model Analysis Workflow

1. **Analyze Models**:
   - Use **Analyze Model Weights** node with two models
   - Choose optimization method (Combined recommended for general use)
   - Set global alpha as starting point (0.5 default)
   - Adjust optimization strength (0.8 = trust analysis heavily)
   - Receive recipe with per-block weights

2. **Apply Recipe**:
   - Connect recipe to **Apply Merge Recipe** node
   - Choose merge method (weighted_sum or add_difference)
   - Adjust strength to scale the recipe (1.0 = full recipe)
   - Get optimally merged model

**Example Workflow**:
```
[Model A] ──┐
           [Analyze Model Weights] → [Recipe] → [Apply Merge Recipe] → [Merged Model]
[Model B] ──┘                                         ↑
                                               [Model A, Model B]
```

### Spectral Merging with Prism
The **Prism** node offers advanced frequency-domain merging:
- **Spectral Blend**: Basic frequency-based merging
- **Frequency Bands**: Separate low/high frequency control
- **Magnitude Weighted**: Blend based on parameter magnitudes
- **Adaptive Mix**: Similarity-aware blending
- **Harmonic Merge**: Sign-based harmonic blending

### Mask-Based Merging
Create precise masks to control merging at the tensor level:

1. **Generate Mask**: Use **Model Mask Generator** to create mask based on:
   - Layer ranges
   - Block types
   - Attention/feedforward components
   - Custom patterns
   - Random sparsity
   - Depth gradients

2. **Filter Keys**: Use **Model Key Filter** for targeted parameter selection

3. **Blend Masks**: Combine multiple masks with **Mask Blender**

4. **Apply Mask**: Use **Weighted Mask Merge** to apply mask during merging

### CLIP Merging
Use **Advanced CLIP Merge** for sophisticated text encoder merging:
- Choose interpolation method (SLERP recommended for quality)
- Apply layer-specific biases:
  - Attention bias: Affects cross-attention layers
  - Feedforward bias: Affects MLP layers
  - Embedding bias: Affects token/position embeddings
  - Normalization bias: Affects layer norms
- Enable preserve_norms for stability
- Use spectral_blend for frequency domain merging

### Prediction Type Conversion
Use **Epsilon/V-Pred Converter** when working with mixed prediction types:
- Set input_pred_type (current model type)
- Set output_pred_type (desired type)
- Adjust conversion_strength (1.0 = full conversion)
- Critical layers (output blocks, final layers) get stronger conversion
- Secondary layers get gentler conversion

## Available Nodes

| Node | Category | Description |
|------|----------|-------------|
| Main Merge | Tensor_Prism/Core | Advanced interpolation methods |
| Prism | Tensor_Prism/Core | Spectral frequency-domain merging |
| Layered Blend | Tensor_Prism/Core | Component-specific blending |
| SDXL Block Merge | Tensor_Prism/Merge | Granular SDXL block control |
| SDXL Advanced Block Merge | Tensor_Prism/Merge | GPU-optimized block merging |
| Weighted Tensor Merge [Advanced] | Tensor_Prism/Advanced | Sophisticated tensor merging with blend modes |
| Analyze Model Weights | Tensor_Prism/Advanced | Intelligent merge optimization |
| Apply Merge Recipe | Tensor_Prism/Advanced | Recipe-based precision merging |
| Model Analyzer | Tensor_Prism/Analysis | Comprehensive model analysis |
| Model Comparator | Tensor_Prism/Analysis | Quick compatibility checker |
| Intelligent Tensor Selector | Tensor_Prism/Advanced | Smart tensor-by-tensor selection |
| Competitive Model Selector | Tensor_Prism/Advanced | Multi-model tensor competition |
| Epsilon/V-Pred Converter | Tensor_Prism/Convert | Pure prediction type conversion |
| Advanced CLIP Merge | Tensor_Prism/CLIP | Sophisticated CLIP merging with multiple methods |
| VAE Merge | Tensor_Prism/VAE | VAE blending |
| Model Mask Generator | Tensor_Prism/Mask | Create structural masks |
| Weighted Mask Merge | Tensor_Prism/Mask | Apply masks to merging |
| Model Key Filter | Tensor_Prism/Mask | Filter model parameters |
| Mask Blender | Tensor_Prism/Mask | Combine multiple masks |
| Model Weight Modifier | Tensor_Prism/Transform | Direct weight manipulation |
| Model Enhancer | Tensor_Prism/Transform | Model enhancement |

## Memory Management

The TensorPrism pack includes advanced memory management features:

- **Automatic GPU Detection**: Optimizes for your specific GPU memory
- **Adaptive Batch Sizes**: Adjusts processing based on available memory
- **Precision Selection**: Automatic FP16/FP32 based on memory constraints
- **Progressive Cleanup**: Aggressive garbage collection for low-memory systems
- **CPU Fallback**: Automatic fallback when GPU memory is insufficient
- **Memory Context Managers**: Automatic cleanup and resource management
- **Threshold-Based Processing**: Memory usage monitoring with configurable limits
- **Device Safety**: All tensor operations ensure same-device calculations to prevent CUDA/CPU conflicts

### Recommended Settings by GPU:
- **24GB+ (RTX 4090, etc.)**: Use default settings, batch size 50+
- **12GB (RTX 4070 Ti, etc.)**: Set memory limit to 8GB, enable auto precision, batch size 30-50
- **8GB (RTX 4060 Ti, etc.)**: Set memory limit to 6GB, force CPU for large merges, batch size 10-30
- **6GB and below**: Use CPU processing for best stability, enable aggressive cleanup

## Requirements

- ComfyUI
- PyTorch >= 1.12.0
- NumPy >= 1.21.0
- psutil >= 5.8.0 (for memory management)

## Tips and Best Practices

1. **Analyze Before Merging**: Use Model Analyzer to understand your models before attempting complex merges
2. **Check Compatibility**: Use Model Comparator for quick compatibility checks
3. **Start Conservative**: Begin with lower merge ratios (0.3-0.7) and adjust based on results
4. **Use SLERP for Dissimilar Models**: When merging very different models, SLERP often produces better results
5. **Leverage Spectral Methods**: Frequency domain merging can preserve details better than linear methods
6. **Use Masks for Precision**: Create masks to merge only specific model components
7. **Memory Management**: Monitor memory usage and adjust batch sizes for your hardware
8. **Experiment with Spectral Parameters**: Different frequency biases can dramatically change results
9. **Layer-Selective Merging**: Use depth gradients for smooth transitions through model layers
10. **Prediction Type Awareness**: Use the Epsilon/V-Pred converter when working with models of different prediction types
11. **CLIP Merging Strategy**: Use spectral blend for CLIP when preserving text understanding is critical
12. **Conversion Strength**: Start with 1.0 conversion strength and adjust if results seem over/under-converted
13. **Layer-Specific CLIP Control**: Use attention/feedforward bias to fine-tune CLIP behavior for specific use cases
14. **Smart Analysis First**: For complex merges, use Analyze Model Weights first to find optimal ratios
15. **Blend Mode Selection**: Use sigmoid/cosine for smooth transitions, exponential for dramatic changes
16. **Layer Scaling Strategy**: Use depth-progressive for fine-tuning influence, shallow-bias for style preservation
17. **Recipe Reuse**: Save successful merge recipes as text files for reproducible results
18. **Deep Analysis Mode**: Use Deep analysis when planning very complex or experimental merges
19. **Read Recommendations**: The Model Analyzer provides tailored suggestions based on your specific models
20. **Noise Injection for Exploration**: Use Noise Injection Merge when standard merges produce overly similar results or to discover unexpected capabilities
21. **Start with Low Noise**: Begin with 0.02-0.05 noise strength and increase gradually - too much noise destroys coherence
22. **Adaptive Noise for Similar Models**: When merging highly similar models, use adaptive noise pattern to force differentiation
23. **Layer-Scaled for Deep Effects**: Use layer-scaled noise when you want deeper layers to explore more variations
24. **Preserve Norms**: Keep norm preservation enabled for stability unless specifically experimenting with magnitude changes
25. **Reproducible Noise Experiments**: Always set a seed for noise injection to reproduce successful merges

## Troubleshooting

- **Memory Issues**: Reduce batch sizes, lower memory limits, or enable CPU fallback
- **Poor Results**: Try different merging methods or adjust spectral parameters
- **Compatibility**: Ensure models are the same architecture (SDXL with SDXL, etc.)
- **Slow Performance**: Check if you're accidentally using CPU when GPU is available
- **Artifacts**: Try more conservative merge ratios or use SLERP for smoother blending
- **Prediction Type Issues**: Use the Epsilon/V-Pred converter for automatic type conversion
- **CLIP Problems**: Use preserve_norms=True and lower merge ratios for CLIP stability
- **Conversion Artifacts**: Reduce conversion strength or use pure converter instead of block merge
- **Device Conflicts**: v1.5.0+ fixes "expected tensors on same device" errors - update if you see these
- **Smart Merger Issues**: Ensure both models are compatible architecture and same size
- **Analysis Failures**: Ensure sufficient system RAM for model analysis (models stay on GPU, analysis on CPU)

## Performance Tips

- **Batch Size**: Larger batches are more efficient but use more memory
- **Precision Mode**: FP16 saves memory but may affect quality on some operations
- **Memory Cleanup**: Enable aggressive cleanup for systems with limited RAM
- **Device Selection**: Let the system auto-detect optimal device unless you have specific needs
- **CLIP Memory**: CLIP merging is less memory-intensive than UNet merging
- **Conversion vs Merging**: Pure conversion uses less memory than block-level merge+convert
- **Smart Analysis**: CPU-based analysis prevents GPU memory conflicts during optimization
- **Recipe Reuse**: Save and reuse successful merge recipes for consistency
- **Quick Analysis**: Use Quick mode for routine checks, Deep mode for important merges
- **Analysis Caching**: Model Analyzer results can guide multiple merge attempts

## License

GPL-3.0 License - https://www.gnu.org/licenses/gpl-3.0.en.html

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Changelog

### Version 1.7.1
- Fixed the Advanced Clip Merge and Model Enhancer Node.
- Fixed Mask Blender

### Version 1.7.0
- **NEW**: Noise Injection Merge node for emergent capability discovery
  - 7 noise patterns: Gaussian, Uniform, Structured, Layer-Scaled, Adaptive, Perlin, Gradient
  - Minimal overhead design (no significant memory or performance impact)
  - Focus controls for targeting specific layer types (attention, MLP)
  - Layer-aware scaling with automatic depth-based noise adjustment
  - Adaptive noise generation based on tensor similarity
  - Norm preservation for stability
  - Reproducible experiments with seed control
- **IMPROVED**: Consolidated file structure for better maintainability
- **UPDATED**: Enhanced __init__.py with 21 production-ready nodes
- **ENHANCED**: Comprehensive documentation for all merging strategies

### Version 1.6.5
- **FIXED**: Corrected file upload issues from v1.6.0
- **VERIFIED**: All node files properly included in repository
- **CONFIRMED**: Model Analyzer and Model Comparator fully functional
- All features from v1.6.0 should be present

### Version 1.6.0
- **NEW**: Model Analyzer node for comprehensive model analysis
  - Three analysis depths: Quick, Standard, Deep
  - Architecture analysis (blocks, layers, components)
  - Statistical analysis (magnitudes, sparsity, distributions)
  - Memory profiling by component
  - Model comparison for merge compatibility
  - Smart recommendations based on model characteristics
  - JSON export for external processing
- **NEW**: Model Comparator node for quick compatibility checks
  - Fast similarity scoring
  - Boolean compatibility output
  - Merge recommendations based on similarity
  - Workflow-friendly outputs
- **IMPROVED**: Node organization with new Analysis category
- **REMOVED**: Fine-tuning placeholder nodes (replaced with practical analysis tools)
- **UPDATED**: Documentation with analysis workflow examples
- **ENHANCED**: Better merge planning through pre-merge analysis

### Version 1.5.0
- **FIXED**: Device conflict errors - all tensor operations now ensure same-device calculations
- **NEW**: Weighted Tensor Merge [Advanced] node with sophisticated blending modes
  - 6 blend modes: linear, sigmoid, cosine, exponential, logarithmic, smoothstep
  - Curve power control for fine-tuned transitions
  - Layer scaling: uniform, depth-progressive, shallow-bias, deep-bias
  - Preserve extremes option and noise injection
  - Smart layer detection and per-layer scaling
- **NEW**: Analyze Model Weights node for intelligent merge optimization
  - 5 optimization methods: combined, similarity, variance, gradient magnitude, entropy
  - Configurable target weights and standard deviations
  - Weight smoothing and auto-detection features
  - Memory-efficient CPU-based analysis
- **NEW**: Apply Merge Recipe node for recipe-based merging
  - Multiple merge methods: weighted sum, add difference
  - Strength control for recipe application
  - Block-level precision merging
- **IMPROVED**: Enhanced device safety across all nodes
- **IMPROVED**: Better memory management in analysis nodes
- **IMPROVED**: Separated basic and advanced tensor merge nodes for clarity
- **REMOVED**: Checkpoint Reroute + Notes node (redundant functionality moved to Arctenox's Essentials and Updated)

### Version 1.2.0
- Added **Advanced CLIP Merge** node with multiple interpolation methods and layer-specific controls
- Added **Epsilon/V-Pred Converter** node for pure prediction type conversion
- Enhanced **SDXL Advanced Block Merge** with improved memory management and context managers
- Improved **Weighted Mask Merge** with tensor-level precision control
- Added spectral blending capabilities to CLIP merging
- Enhanced memory management with automatic GPU/CPU fallback
- Improved layer identification and targeting for prediction type conversion
- Better mathematical accuracy in conversion factors

### Version 1.1.0
- GPU-optimized memory management
- Cross-platform compatibility (CUDA/MPS/CPU)
- Bunch of Bug Fixes
- Addition of 3 Nodes

### Version 1.0.0
- Initial release
- Core merging nodes with advanced interpolation methods
- Advanced mask system with filtering and blending
- Spectral analysis and frequency-domain merging
- Support for SDXL models with granular block control
- Model weight modification tools

## Credits

Developed by Arctenox with heavy assistance from Gemini 2.5 Flash and Claude 4 meaning this was mostly Vibe Coded.

## Support

If you create interesting models using TensorPrism, feel free to share them! Feedback helps improve the node pack.
