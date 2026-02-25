# HommageTools for ComfyUI

A comprehensive collection of utility nodes for ComfyUI that enhance your workflow with advanced text processing, image manipulation, workflow control, and AI pipeline optimization capabilities.

![GitHub](https://img.shields.io/github/license/ArtHommage/HommageTools)
![GitHub last commit](https://img.shields.io/github/last-commit/ArtHommage/HommageTools)

> **⚠️ DISCLAIMER: These nodes are perpetually in alpha status and highly experimental. They should NOT be used for production. The author reserves the right to alter or discontinue them without notice or warranty.**

## 🚀 Overview

HommageTools is designed to fill functionality gaps in ComfyUI with professional-grade utility nodes that follow best practices for performance and compatibility. Each node is carefully crafted to handle BHWC tensor formats correctly and includes proper error handling.

## 📋 Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/ArtHommage/HommageTools.git
   ```

3. Install requirements:
   ```bash
   cd HommageTools
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## 📦 Node Categories

### Text Processing Nodes

#### HT Regex (`HTRegexNode`)
Process text using regular expressions with pattern matching. This node applies regex pattern matching to input text, allowing for powerful text extraction and transformation capabilities.
- **Inputs**: Input text, regex pattern
- **Outputs**: Parsed text
- **Internal Mechanics**: Uses Python's `re` module to find all matches of the pattern within the input text. If multiple matches are found, it joins them with newlines.
- **Purpose**: Extract specific patterns from prompts, clean up text inputs, reformat text according to precise rules
- **Use Cases**: Extract specific data from structured text, filter out unwanted content, validate text formats

#### HT Parameter Extractor (`HTParameterExtractorNode`)
Extract labeled parameters from text strings with custom identifiers. This node parses structured text to find and extract specific labeled values using customizable delimiters.
- **Inputs**: Input text, separator, identifier, parameter label, clear parameters flag
- **Outputs**: Parsed text, label, value (as string/float/int)
- **Internal Mechanics**: Uses regex to locate parameters in the format `identifier[label=value]separator`. It can extract the specified parameter while optionally removing all parameter blocks from the output text.
- **Purpose**: Enables embedding control values directly in text prompts that can be extracted and used to control other nodes
- **Use Cases**: Parse control parameters embedded in prompts (like size, steps, or seed), extract metadata from text, create prompt templates with variable parts

#### HT Text Cleanup (`HTTextCleanupNode`)
Comprehensive text cleanup with configurable rules for formatting. This node performs multiple text normalization and cleanup operations to standardize text.
- **Inputs**: Input text, preservation options (period spacing, linebreaks), cleanup aggressiveness
- **Outputs**: Cleaned text
- **Internal Mechanics**: Applies a series of processing steps including whitespace normalization, punctuation cleanup, and multiple formatting passes. The node uses configurable rules to preserve specific formatting elements when desired.
- **Purpose**: Creates consistently formatted text for reliable prompt results, fixing common issues like double spaces, inconsistent line breaks, and messy punctuation
- **Use Cases**: Standardize prompt formats for consistent results, prepare text for processing by other nodes, clean up user inputs, normalize text from different sources

#### HT Dynamic Prompt (`HTDynamicPromptNode`)
Enhanced dynamic prompt generation with token limiting. This node expands dynamic prompt syntax into final prompts with wildcard substitution and variation handling.
- **Inputs**: Text template, seed, autorefresh option, whitespace handling, token limit, optional CLIP model
- **Outputs**: Generated prompt, token info, CLIP passthrough
- **Internal Mechanics**: Processes templates with wildcards (`__wildcard__`), variations (`{option1|option2}`), and other dynamic prompt syntax. Includes accurate token counting to avoid exceeding model limits.
- **Purpose**: Creates varied prompts from templates for exploration and batch processing
- **Use Cases**: Prompt variation for batch generation, automated prompt experimentation, consistent random prompt generation with reproducible seeds

### Image Processing Nodes

#### HT Surface Blur (`HTSurfaceBlurNode`)
Memory-efficient surface blur with tiled processing and GPU optimization. This node implements the popular Photoshop surface blur filter that smooths areas while preserving edges.
- **Inputs**: Image, radius, threshold
- **Outputs**: Blurred image
- **Internal Mechanics**: Processes images in tiles to minimize memory usage, using a sophisticated algorithm that calculates color and position weights based on the threshold value. For each pixel, it applies selective blurring that preserves edges based on color differences.
- **Purpose**: Provides high-quality, edge-aware blurring that's optimized for large images with proper BHWC tensor handling
- **Use Cases**: Skin smoothing while preserving details, noise reduction while preserving edges, creating soft backgrounds while maintaining subject clarity, texture cleaning

#### HT Downsample (`HTDownsampleNode`)
Downsamples images to smaller sizes with proper BHWC handling. This node provides efficient and high-quality image resizing with multiple interpolation options.
- **Inputs**: Image, target dimensions, interpolation method
- **Outputs**: Downsampled image
- **Internal Mechanics**: Carefully handles tensor format conversions, ensuring proper BHWC format throughout the process. Uses PyTorch's interpolation functions with antialiasing where appropriate and handles tensor permutation correctly for high-quality results.
- **Purpose**: Provides reliable downsampling that maintains image quality while reducing resolution, with proper tensor handling
- **Use Cases**: Reduce image size for previews or faster processing, create lower-resolution versions for multi-resolution workflows, prepare images for networks that require smaller inputs

#### HT Resolution Downsample (`HTResolutionDownsampleNode`)
Downsample images to target resolution while maintaining aspect ratio. This node focuses on creating consistently sized images by targeting a specific resolution for the longest edge.
- **Inputs**: Image, target long edge, interpolation
- **Outputs**: Downsampled image
- **Internal Mechanics**: Analyzes the input image to determine the longest edge, calculates a scale factor that will resize this edge to the target value, then applies the same scale factor to the other dimension to maintain aspect ratio. Uses proper BHWC tensor handling throughout.
- **Purpose**: Creates consistently sized images while preserving original proportions, allowing for standardized processing of varied inputs
- **Use Cases**: Consistent sizing for batches of differently sized images, preparing images for models with size constraints, reducing very large images to workable sizes while maintaining composition

#### HT Photoshop Blur (`HTPhotoshopBlurNode`)
Emulates various Photoshop blur filters with configurable parameters. This node provides a comprehensive collection of blur algorithms matching popular Photoshop effects.
- **Inputs**: Image, blur type (average, gaussian, motion, radial, zoom, lens, smart), radius, and type-specific parameters (sigma, angle, blade count, threshold, etc.)
- **Outputs**: Blurred image
- **Internal Mechanics**: Implements multiple blur algorithms including Gaussian, motion, radial/zoom, lens (bokeh), and smart blur with edge preservation. Each algorithm creates specialized convolution kernels and applies them efficiently with proper tensor handling.
- **Purpose**: Brings Photoshop-quality blur effects directly into the ComfyUI workflow without leaving the environment
- **Use Cases**: Creative effects like motion blur for movement, lens blur for depth of field simulation, radial/zoom blur for focus or speed effects, smart blur for noise reduction while preserving important details

#### HT Levels (`HTLevelsNode`)
Advanced image levels adjustment with reference matching. This node adjusts the tonal distribution of an image based on a reference image.
- **Inputs**: Source image, reference image, method (histogram match, luminance curve), strength
- **Outputs**: Processed image
- **Internal Mechanics**: For histogram matching, it calculates histograms and cumulative distribution functions (CDFs) for both source and reference images, then maps the source image's pixel values to match the reference image's distribution. The strength parameter controls how strongly the effect is applied.
- **Purpose**: Enables sophisticated color grading and matching between images within the ComfyUI environment
- **Use Cases**: Color grading to match a specific look, histogram matching between rendered and reference images, correcting flat or contrasty images, making multiple images from different sources look cohesive

#### HT Smart Resize (`HTResizeNode`)
Intelligent image resizing with aspect ratio preservation and BHWC handling. This node provides advanced resizing capabilities with multiple strategies for handling aspect ratio differences.
- **Inputs**: Divisibility options (8, 64), interpolation (nearest, linear, bilinear, bicubic, lanczos), scaling mode (short_side, long_side), crop/pad mode (center, top, bottom, left, right)
- **Outputs**: Resized image and latent
- **Internal Mechanics**: Properly handles both image and latent tensors in BHWC format, calculates target dimensions that maintain aspect ratio while ensuring divisibility by model requirements, and offers multiple strategies for scaling and handling aspect ratio differences through cropping or padding.
- **Purpose**: Provides precise control over image resizing while ensuring compatibility with model requirements like divisibility
- **Use Cases**: Prepare images for specific model requirements, resize while maintaining composition with intelligent cropping/padding, handle both images and latents with the same node, ensure consistent divisibility for stable diffusion models

#### HT Intel Denoiser (`HTOIDNNode`)
Enhanced Intel Open Image Denoise implementation with proper tensor handling. This node leverages Intel's AI-based denoising technology for high-quality noise reduction.
- **Inputs**: Image, strength, tile size
- **Outputs**: Denoised image
- **Internal Mechanics**: Initializes the OIDN device and filter, processes images in tiles to manage memory usage, and ensures proper tensor handling throughout the process. Uses an overlapping tile approach with blending to avoid seams. Allows strength adjustment to control the intensity of the denoising effect.
- **Purpose**: Provides AI-powered, industry-standard denoising capabilities directly within ComfyUI
- **Use Cases**: Clean up noisy AI-generated images, improve quality of renders, remove grain while preserving details, prepare images for further processing or final output

#### HT Scale By (`HTScaleByNode`)
Scales images by a factor with mask support and proper format handling. This node provides precise scaling with optional mask integration.
- **Inputs**: Image, scale factor, interpolation method, crop to mask flag, optional mask
- **Outputs**: Scaled image, scaled mask
- **Internal Mechanics**: Validates and normalizes input tensors to BHWC format, calculates target dimensions based on scale factor, and performs high-quality interpolation with format preservation. Can optionally crop to mask content before scaling for focused processing.
- **Purpose**: Provides precise control over image scaling with awareness of mask content areas
- **Use Cases**: Upscale or downscale by precise factors, focus scaling on masked regions, prepare images and masks together for further processing

#### HT Moiré Removal (`HTMoireRemovalNode`)
Removes moiré patterns from images with advanced frequency domain filtering. This node combines multiple filter techniques to eliminate interference patterns common in scanned or photographed images.
- **Inputs**: Image, filter strength and parameters, tile size mode, normalization options
- **Outputs**: Filtered image
- **Internal Mechanics**: Applies a combination of median filtering, Butterworth filtering, and notch filtering with tiled processing for memory efficiency. Uses global normalization for consistent results across tiles and includes proper overlap blending to avoid seams.
- **Purpose**: Eliminates moiré patterns that commonly appear when photographing or scanning images with fine patterns
- **Use Cases**: Clean up scanned illustrations, remove screen patterns from photographed displays, improve quality of digitized printed materials, prepare images for further AI processing

#### HT Save Image Plus (`HTSaveImagePlus`)
Enhanced image saving with multiple format support and metadata options. This node extends ComfyUI's image saving capabilities with advanced options and format support.
- **Inputs**: Images, output format (PNG, JPEG, TIFF), filename options, quality settings, mask (for alpha channel), text content (for accompanying text files), metadata controls
- **Outputs**: UI update with saved file info
- **Internal Mechanics**: Handles proper conversion between tensor formats and image formats, manages alpha channel integration from masks, supports embedding metadata in supported formats, and optionally creates accompanying text files with the same base name.
- **Purpose**: Provides comprehensive image saving capabilities beyond the basic options, with control over format, quality, metadata, and accompanying text
- **Use Cases**: Save images with custom metadata for workflow tracking, save in multiple formats for different purposes, include masks as alpha channels, add text notes or prompt information in accompanying files, control compression and quality settings

#### HT Detection Batch Processor (`HTDetectionBatchProcessor`)
Processes batches of detected regions with upscaling and post-processing. This node handles object detection results and applies processing to each region.
- **Inputs**: Image, detection model, processing parameters, scaling options
- **Outputs**: Processed image, cropped batch, scale information
- **Internal Mechanics**: Extracts detected regions from an image, applies optional bucket-based sizing to standardize dimensions, and processes each region with configurable parameters. Handles proper BHWC tensor format throughout.
- **Purpose**: Enables targeted processing of specific image regions based on detection results
- **Use Cases**: Upscale detected objects while leaving backgrounds untouched, apply different processing to different image elements, standardize detected elements to consistent sizes, batch process multiple detections efficiently

#### HT Gemini (`HTGeminiNode`)
Interface with Google's Gemini AI for text and image processing. This node provides access to Gemini's multimodal capabilities for content generation.
- **Inputs**: Model, system instructions, content, temperature, optional image, generation parameters
- **Outputs**: Generated text, status information
- **Internal Mechanics**: Connects to Google's Gemini API, handles proper authentication and API key management, processes inputs in BHWC format for images, and manages generation parameters for customized outputs.
- **Purpose**: Integrates Google's powerful Gemini AI models directly into ComfyUI workflows
- **Use Cases**: Generate descriptions of images, create captions, get creative writing based on visual inputs, generate code or analytical content based on images and text prompts

### Dimension Handling Nodes

#### HT Resolution (`HTResolutionNode`)
Recommends optimal image resolutions based on quality priorities. This node analyzes input dimensions and suggests standard resolutions that best match the aspect ratio.
- **Inputs**: Width, height, priority mode (minimize_loss, minimize_noise, auto_decide), use standard list flag, mode (crop, pad), optional custom resolutions
- **Outputs**: Width, height, scale factor, crop/pad info, detailed information, padding values
- **Internal Mechanics**: Calculates quality metrics for various standard resolutions based on the input dimensions and aspect ratio, then scores each option according to the selected priority mode. The scoring system considers aspect ratio preservation, pixel loss, and scaling factors to recommend the optimal resolution.
- **Purpose**: Takes the guesswork out of selecting resolutions by recommending optimal standard sizes that match the input's aspect ratio
- **Use Cases**: Find standard resolutions that match input aspect ratio, determine optimal size for training or inference, calculate required padding or cropping to fit standard sizes, prepare assets for specific output requirements

#### HT Dimension Formatter (`HTDimensionFormatterNode`)
Formats image dimensions into standardized strings with BHWC handling. This node creates consistent dimension strings from dimension values or image tensors.
- **Inputs**: Width, height, spacing character, optional image tensor
- **Outputs**: Formatted dimension string
- **Internal Mechanics**: Can extract dimensions directly from image tensors in BHWC format or use provided width/height values. Formats the dimensions using the specified spacing character for consistent presentation.
- **Purpose**: Creates standardized dimension strings for display, logging, or file naming
- **Use Cases**: Display image sizes in consistent format, create standardized filenames that include dimensions, generate dimension tags for prompts, maintain consistent formatting across a workflow

#### HT Dimension Analyzer (`HTDimensionAnalyzerNode`)
Analyzes image dimensions and returns long/short edge values. This node extracts and classifies dimensions from image tensors.
- **Inputs**: Image tensor
- **Outputs**: Long edge, short edge
- **Internal Mechanics**: Properly extracts height and width from image tensors in BHWC format, then determines which is the long edge and which is the short edge. Handles various tensor formats correctly.
- **Purpose**: Provides dimension analysis that can be used for conditional processing based on image orientation or size
- **Use Cases**: Dimension analysis for conditional processing, determine image orientation (landscape vs portrait), feed into nodes that require long/short edge information, drive conditional workflows based on image proportions

#### HT Training Size (`HTTrainingSizeNode`)
Calculates optimal training dimensions with proper BHWC tensor handling. This node determines the best dimensions for training images to optimize quality and performance.
- **Inputs**: Width, height, scaling mode (both, upscale_only, downscale_only), optional image tensor
- **Outputs**: Width, height, scale factor, requires_clipping
- **Internal Mechanics**: Analyzes input dimensions (either directly provided or extracted from an image tensor), then finds the optimal dimensions from a set of standard training sizes (512, 768, 1024). Uses the selected scaling mode to determine whether to allow upscaling, downscaling, or both. Calculates dimensions that maintain aspect ratio while fitting standard training sizes.
- **Purpose**: Takes the guesswork out of selecting training dimensions by automatically calculating optimal sizes
- **Use Cases**: Prepare images for ML training at optimal sizes, standardize dataset dimensions while preserving aspect ratios, determine if images need clipping to fit target dimensions, calculate the scale factor needed for resizing

#### HT Mask Dilate (`HTMaskDilationNode`)
Crops images to mask content and calculates scaling factors. This node focuses on extracting and processing the relevant content area defined by a mask.
- **Inputs**: Image, mask, scale mode (Scale Closest, Scale Up, Scale Down, Scale Max), padding
- **Outputs**: Dilated mask, cropped image, width, height, scale factor
- **Internal Mechanics**: Finds the bounding box of non-zero pixels in the mask, crops both the image and mask to this region (with optional padding), and calculates a scale factor to resize the cropped content to standard dimensions based on the selected scaling mode.
- **Purpose**: Focuses processing on the relevant content area defined by a mask, enabling more efficient and targeted operations
- **Use Cases**: Focus processing on masked regions, extract subjects from backgrounds, calculate appropriate scaling for masked content, prepare masked regions for further processing at optimal sizes

#### HT Multi Mask Dilate (`HTMultiMaskDilationNode`)
Detects and crops multiple regions from a mask with BHWC tensor handling. This node handles batch processing of multiple masked regions.
- **Inputs**: Image, mask, scale mode, padding, connectivity, max regions
- **Outputs**: Cropped masks, cropped images, widths, heights, scale factors, is multi-region flag, region count, region indices
- **Internal Mechanics**: Detects connected components in the mask, extracts each region with proper BHWC handling, and calculates appropriate scaling factors for each. Supports batched processing and produces aligned output batches.
- **Purpose**: Enables parallel processing of multiple detected regions within an image
- **Use Cases**: Extract multiple subjects from an image, process different regions with distinct parameters, prepare multiple regions for batch processing, isolate components of complex images

#### HT Tensor Info (`HTTensorInfoNode`)
Displays tensor shape information in BHWC format with detailed analysis. This node helps with debugging by providing comprehensive information about tensor dimensions and format.
- **Inputs**: Image tensor
- **Outputs**: Image (passthrough), shape info
- **Internal Mechanics**: Analyzes the input tensor to determine its format (BHWC or HWC), dimensions, and other properties. Produces a detailed text description of the tensor's properties while passing the tensor through unchanged.
- **Purpose**: Provides essential debugging information about tensors to help troubleshoot dimension and format issues
- **Use Cases**: Debug tensor dimensions and formats, verify tensor transformations, check batch size and channel count, monitor tensor changes throughout a workflow, help diagnose format compatibility issues

### Layer Management Nodes

#### HT Layer Collector (`HTLayerCollectorNode`) 
Collects images into a layer stack with BHWC format handling. This node builds a collection of image layers that can be exported as a layered file.
- **Inputs**: Image, layer name, mask (optional, for transparency), input stack (optional, for adding to existing stack)
- **Outputs**: Layer stack
- **Internal Mechanics**: Processes input images with proper BHWC format handling, integrates masks as alpha channels when provided, and maintains a stack of layers with metadata. Each layer is stored with its name and image data in a format ready for export.
- **Purpose**: Enables building complex multi-layer compositions that can be exported to professional editing software
- **Use Cases**: Build multi-layer compositions, separate generation elements into layers (background, subject, effects), combine multiple AI-generated elements with proper transparency, prepare compositions for professional editing

#### HT Layer Export (`HTLayerExportNode`)
Exports layer stack to PSD or TIFF format with full metadata. This node saves layered compositions to industry-standard file formats.
- **Inputs**: Layer stack, output path, format (psd, tiff)
- **Outputs**: None (file saved to disk)
- **Internal Mechanics**: Converts the layer stack into the appropriate format (PSD or TIFF), preserving layer names and transparency. For PSD export, it creates a proper Photoshop document with separate layers. For TIFF export, it creates a multi-page TIFF with layers. Handles proper color space and alpha channel management.
- **Purpose**: Provides professional export capabilities for complex compositions, enabling seamless workflow with external editing software
- **Use Cases**: Export composited images to editing software, save work with preserved layers for later editing, create assets for design workflows, preserve the full creative process with separated elements

#### HT Mask Validator (`HTMaskValidatorNode`)
Validates mask inputs and detects meaningful mask data. This node ensures masks are properly formatted and contain valid data for processing.
- **Inputs**: Threshold (minimum value to consider as masked), mask tensor
- **Outputs**: Has mask data flag, normalized mask
- **Internal Mechanics**: Validates mask tensor format, dimensions, and value range. Detects whether the mask contains meaningful data above the threshold. Normalizes mask format to a consistent representation (single channel, 0-1 range, proper BHWC format).
- **Purpose**: Ensures masks are valid before using them in downstream operations, preventing errors and unexpected results
- **Use Cases**: Verify mask quality before processing, validate user-provided masks, normalize masks from different sources to a consistent format, detect empty or invalid masks, determine if a conditional processing path should be taken based on mask content

### AI Pipeline Nodes

#### HT Sampler Bridge (`HTSamplerBridgeNode`)
Bridge node for converting string inputs to sampler selections. This node provides a flexible interface between text-based inputs and ComfyUI's sampler system.
- **Inputs**: Sampler name string
- **Outputs**: Compatible sampler object
- **Internal Mechanics**: Validates and normalizes sampler names, handling partial matches and case insensitivity. Converts the validated name into a proper sampler object that can be used by other nodes. Provides fallback to default samplers when invalid names are provided.
- **Purpose**: Enables dynamic sampler selection using string inputs, bridging the gap between text interfaces and ComfyUI's type system
- **Use Cases**: Dynamic sampler selection from text input, convert user inputs or extracted parameters to valid samplers, handle sampler selection from external sources, create interfaces that use plain text rather than dropdowns

#### HT Scheduler Bridge (`HTSchedulerBridgeNode`)
Bridge node for converting string inputs to scheduler selections. This node enables text-based control of sampling schedules.
- **Inputs**: Model, scheduler name string, steps string (number of steps), denoise string (denoising strength)
- **Outputs**: Sigmas tensor
- **Internal Mechanics**: Validates scheduler names with flexible matching, parses numeric inputs for steps and denoise strength, calculates appropriate sigmas tensor based on these parameters. Handles partial name matches and provides fallbacks for invalid inputs.
- **Purpose**: Enables flexible, string-based control of sampling schedules, bridging text interfaces with ComfyUI's scheduler system
- **Use Cases**: Dynamic scheduler configuration from text input, parameter extraction from prompts or UI, automation of scheduler settings, integration with external control systems that use text rather than specific types

#### HT Base Shift (`HTBaseShiftNode`)
Calculates base shift values for images with BHWC tensor handling. This node computes optimal shift parameters based on image dimensions.
- **Inputs**: Image width, height, max shift, base shift (optional image tensor)
- **Outputs**: Max shift, base shift
- **Internal Mechanics**: Calculates shift values using a formula that accounts for image dimensions. Can extract dimensions directly from image tensors in BHWC format or use provided width/height values. The formula adjusts shift values proportionally to image size for optimal results.
- **Purpose**: Provides optimized base shift parameters for stable diffusion based on image dimensions
- **Use Cases**: Dynamic shift parameter calculation based on image size, optimize image-to-image parameters automatically, calibrate generation settings for different resolutions

#### HT Seed (`HTSeedNode`)
Simple seed generator node with random seed capabilities. This node provides basic random seed generation with toggle options.
- **Inputs**: Seed, random seed flag, force random seed flag
- **Outputs**: Seed value
- **Internal Mechanics**: Handles fixed or random seeds with optional forcing for each execution. Uses a cryptographically strong random number generator for consistent, high-quality randomness.
- **Purpose**: Provides reliable and flexible seeding options for reproducible generation
- **Use Cases**: Basic seed management, togglable random seeding, seed control for testing and comparison

#### HT Seed Advanced (`HTSeedAdvancedNode`)  
Advanced seed generator with multiple modes and outputs. This node provides comprehensive seeding control for complex workflows.
- **Inputs**: Base seed, random options, seed mode (standard, fixed, iter_add, iter_mult, derived), mode-specific parameters, iteration count, text input
- **Outputs**: Seed, subseed, iteration_seed, seed_info
- **Internal Mechanics**: Implements multiple seeding modes including iteration-based and text-derived seeds. Calculates related subseeds for consistency and includes UI integration with seed updates.
- **Purpose**: Provides advanced seeding control for complex workflows with multiple related seeds
- **Use Cases**: Create sequences of related seeds, derive consistent seeds from text, iterate through seed sequences, generate matched seed/subseed pairs

### Utility and Control Nodes

#### HT Switch (`HTSwitchNode`)
Simple switch node that triggers once when activated.
- **Inputs**: Enabled flag
- **Outputs**: Trigger state
- **Internal Mechanics**: Maintains internal state to trigger only once when enabled, until disabled again. Prevents continuous triggering.
- **Purpose**: Provides controlled trigger signals for one-time operations
- **Use Cases**: One-time triggers for workflow control, prevent action repetition, create controlled event sequences

#### HT Status Indicator (`HTStatusIndicatorNode`)
Displays status indicators based on input values.
- **Inputs**: Any value input
- **Outputs**: Passthrough of input
- **Internal Mechanics**: Evaluates input values of any type to determine status (positive/negative). Sends status updates to the UI for visual indication while passing through the original input.
- **Purpose**: Provides visual feedback about node states or conditions
- **Use Cases**: Visual workflow status monitoring, condition display, process state visualization, debug visual indicators

#### HT Conversion (`HTConversionNode`)
Simple type conversion between string, integer, and float values.
- **Inputs**: String input
- **Outputs**: String, int, float conversions
- **Internal Mechanics**: Attempts to convert the input string to multiple types (int, float) while preserving the original string. Handles conversion errors gracefully.
- **Purpose**: Bridges different node types by converting between data formats
- **Use Cases**: Convert between data types for different nodes, extract numeric values from text, prepare values for type-specific nodes

#### HT Value Mapper (`HTValueMapperNode`)
Maps input labels to values using a configurable mapping list.
- **Inputs**: Mapping list, input value
- **Outputs**: String, float, int, boolean outputs
- **Internal Mechanics**: Parses a mapping list of label:value pairs, matches input against labels, and returns corresponding values in multiple formats. Includes specialized boolean interpretation.
- **Purpose**: Creates flexible mappings between user-friendly labels and processing values
- **Use Cases**: Translate between UI-friendly labels and processing values, create custom enumerations, implement lookup tables, simplify complex parameter selections

#### HT Flexible (`HTFlexibleNode`)
A flexible node that can handle any input/output type.
- **Inputs**: Any input, fallback type
- **Outputs**: Passthrough or fallback value
- **Internal Mechanics**: Automatically adapts to connected nodes' types, passing through any input value or providing a fallback of the specified type if no input is connected.
- **Purpose**: Provides maximum flexibility for dynamic workflows and experimentation
- **Use Cases**: Dynamic type handling, workflow organization, prototype development, conditional value selection

#### HT Inspector (`HTInspectorNode`)
Inspects and reports input types and values for debugging.
- **Inputs**: Any input
- **Outputs**: Passthrough of input
- **Internal Mechanics**: Analyzes the input to determine its type, shape, and content. Sends detailed information to the UI while passing through the original input unchanged.
- **Purpose**: Provides detailed runtime information about data flowing through the workflow
- **Use Cases**: Debug complex workflows and data flows, inspect tensor contents, verify data transformations, examine intermediate values

#### HT Widget Control (`HTWidgetControlNode`)
Controls widget values at the system level with targeting.
- **Inputs**: Mode, target widget, targeting options
- **Outputs**: None (affects UI state)
- **Internal Mechanics**: Injects values into ComfyUI's widget system to control UI elements programmatically. Supports targeting by class name or specific node ID.
- **Purpose**: Enables programmatic control of UI widgets for automation
- **Use Cases**: Programmatic control of UI widgets, workflow automation, dynamic interface adjustment, coordinated parameter changes

#### HT Splitter (`HTSplitterNode`)
Routes a single input to two possible outputs based on a condition.
- **Inputs**: Input value, condition
- **Outputs**: Output true, output false
- **Internal Mechanics**: Routes the input value to one of two outputs based on the boolean condition. Handles tensor formats correctly with proper BHWC preservation.
- **Purpose**: Creates conditional processing paths in workflows
- **Use Cases**: Conditional processing paths, A/B testing, branch selection, error handling paths

#### HT Node State Controller (`HTNodeStateController`)
Controls multiple node states with boolean flip capability.
- **Inputs**: Node IDs, default state, boolean input
- **Outputs**: Signal output (passthrough)
- **Internal Mechanics**: Sends state control commands to multiple target nodes based on node IDs. Supports conditional state flipping based on boolean input.
- **Purpose**: Provides centralized control over multiple nodes' active/mute states
- **Use Cases**: Toggle groups of nodes on/off, conditional workflow sections, A/B testing setups, workflow organization

#### HT Unmute All (`HTNodeUnmuteAll`)
Unmutes all nodes in the workflow with signal pass-through.
- **Inputs**: Optional signal input
- **Outputs**: Signal output (passthrough)
- **Internal Mechanics**: Identifies all nodes in the current workflow and sends commands to ensure they are all in active (unmuted) state.
- **Purpose**: Provides a quick way to reset all nodes to active state
- **Use Cases**: Reset workflow state, recover from experimental configurations, ensure full workflow execution

#### HT Null Value (`HTNullNode`)
Provides null/empty values for optional inputs.
- **Inputs**: Value type selection
- **Outputs**: Null value of specified type
- **Internal Mechanics**: Creates appropriately typed null/empty values based on the selected type. Enables clean workflow connections without data.
- **Purpose**: Provides properly typed empty values for optional inputs
- **Use Cases**: Provide empty inputs for optional node connections, create placeholder connections, disable certain processing paths

#### HT Console Logger (`HTConsoleLoggerNode`)
Prints custom messages to console with input passthrough.
- **Inputs**: Message, timestamp option, optional input
- **Outputs**: Passthrough of input
- **Internal Mechanics**: Formats and prints messages to the console with optional timestamps while passing through the input value unchanged.
- **Purpose**: Provides flexible logging capabilities for workflow debugging
- **Use Cases**: Debug logging, progress tracking, value inspection, execution sequence verification

### Model Management Nodes

#### HT Multi Model Loader (`HTDiffusionLoaderMulti`)
Loads multiple diffusion models from a text list with metadata extraction.
- **Inputs**: Model list, current index, weight dtype
- **Outputs**: Model, model name, model info
- **Internal Mechanics**: Parses a list of model names, loads the model at the specified index, and extracts detailed metadata from the model file. Supports special weight formats and optimizations.
- **Purpose**: Enables working with multiple models in a single workflow
- **Use Cases**: Batch processing with multiple models, model comparison, sequential model application, model metadata inspection

## 🔧 Advanced Usage Examples

### Layered Output Workflow
```
HTLayerCollectorNode (Background) → HTLayerCollectorNode (Subject) → HTLayerExportNode → PSD File
```

### Dynamic Resolution Adjustment
```
HTResolutionNode → HTResizeNode → KSampler → Output
```

### Text Parameter Extraction
```
HTParameterExtractorNode → HTValueMapperNode → Generation Parameters
```

### Image Analysis and Processing
```
Input Image → HTDimensionAnalyzerNode → HTSurfaceBlurNode → Output
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the ComfyUI community for their support and feedback
- Special thanks to all contributors who have helped improve this toolkit