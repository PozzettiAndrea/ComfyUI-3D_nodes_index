# More Math

Adds math nodes for numbers and types which do not need it. I got inspired by was_extras node.

## WARNING This node is not compatible to ComfyUI-Impact-Pack and ComfyUI-Ovi which forces older antlr version via omegaconf

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Clone this repository into `ComfyUI/custom_nodes`.
1. open command prompt/terminal/bash in your comfy folder
1. activate environment `./venv/Scripts/activate`
1. go to more_math folder `cd ./custom_nodes/more_math/`
1. install requirements `pip install -r requirements.txt`
1. Restart ComfyUI.

You can also get the node from comfy manager under the name of More math.

## Features

- functions and variables in math expressions
- Conversion between INT and FLOAT; INT and BOOLEAN; AUDIO and IMAGE (red - real - strenght of cosine of frequency; blue - imaginary - strenght of sine of frequency; green - log1p of amplitude - just so it looks good to humans)
- Nodes for FLOAT, CONDITIONING, LATENT, IMAGE, MASK, NOISE, AUDIO, VIDEO, MODEL, CLIP, VAE, SIGMAS and GUIDER
- Vector Math: Support for List literals `[v1, v2, ...]` and operations between lists/scalars/tensors
- Custom functions `funcname(variable,variable,...)->expression;` they can be used in any later defined custom function or in expression. Shadowing inbuilt functions do not work. **Be careful with recursion. There is no stack limit. Got to 700 000 iterations before I got bored.**
- Custom variables `varname=expression;` They can be used in any later assigment or final expression.
- Support for **indexed assignment**: `a[i, j, ...] = expression;`. Supports multidimensional tensors and nested lists.
  - **Scalar Filling**: If the assigned value has only 1 element (scalar, 1-element list/tensor), it fills the entire selected slice.
  - **Rank Matching**: Automatically squeezes leading ones from the value to match the rank of the target slice (e.g., assigning a 4D tensor with `dim0=1` to a 3D slice).
- Support for control flow statements including `if/else`, `while` loops, blocks `{}`, and `return` statements. `if`/`else`/`while` do not work like ternary operator or other inbuilts. They colapse tensors and list to single value using any.
- Support for stack. Stack survives between field evaluations and can be passed around using stack connection.
  - Usefull in GuiderMath node to store variables between steps.
- comments `#...` and `/*...*/`

### Control Flow Statements

- **If/Else**: `if (condition) statement [else statement]`
- **While Loops**: `while (condition) statement`
- **Blocks**: `{ statement1; statement2; ... }`
  - New variables defined in blocks are isolated and don't leak to outer scope
  - Modifications to existing variables persist to outer scope
- **Return Statements**: `return [expression];`
  - Early return from functions or top-level expressions
- **For Loops**: `for (variable in expression) statement`
  - Iterates over elements of a list or a tensor (along dimension 0)
- **Break/Continue**: `break;`, `continue;`
  - Control loop execution (works in `while` and `for` loops)

## Operators

- Math: `+`, `-`, `*`, `/`, `%`, `^`, `|x|` (norm/abs)
- Boolean: `<`, `<=`, `>`, `>=`, `==`, `!=`
  (`false = 0.0`, `true = 1.0`)
- Bitwise Shifts: `<<`, `>>` (left shift, right shift)
- Indexing: `x[i]` or `x[i, j, ...]` - Selects a sublist (if index count < number of dimensions) or value at position.
- Lists: `[v1, v2, ...]` (Vector math supported, mostly usefull in `conv` and `permute`)
  - You can also use lists to do math with input tensor (image, noise, conditioing, latent, audio) which results in batched output as long as batch size is different to list size.
  - print_shape(a) = torch.Shape[1,1024,1024,3]; b = a*[0,0.2,-0.3]; print_shape(b) = torch.Shape[3,1024,1024,3]
  - You can &lt;operator&gt; batched tensor with another tensor which is not batched (dim[0] = 1) - the non batched tensor will be duplicated along batch dimension
  - In imageMath node you can use 3 element list to specify a color of image. You cannot use any imput tensor, doing so will result in behaviour in subpoint 1 in list
- **Length Mismatch Handling**: All math nodes (except Model, Clip, Vae which default to broadcast) include a `length_mismatch` option to handle inputs with different batch sizes, sample counts, or list lengths. The target length is determined by the **maximum length** among all provided inputs (`a`, `b`, `c`, `d`).
  - `do nothing`: dones **no validation** on input
  - `tile`: Repeats shorter inputs to match the maximum length.
  - `error` (Default): Raises a `ValueError` if any input lengths differ.
  - `pad`: Shorter inputs are padded with zeros to match the maximum length.

## Functions

### Basic Math

- `abs(x)` or `|x|`: Absolute value. For **float** `abs(x)` and `|x|` are the same. For **tensor** `abs(x)` calculates element-wise absolute value and for `|x|` it calculates L2 norm (euclidean norm).
- `sqrt(x)`: Square root.
- `ln(x)`: Natural logarithm (base e).
- `log(x)`: Logarithm base 10.
- `exp(x)`: Exponential function (e^x).
- `pow(x, y)`: Power function (x^y).
- `floor(x)`: Rounds down to nearest integer.
- `ceil(x)`: Rounds up to nearest integer.
- `round(x)`: Rounds to nearest integer.
- `fract(x)`: Returns the fractional part of x (x - floor(x)).
- `sign(x)`: Returns -1 for negative, 1 for positive, 0 for zero.
- `gamma(x)`: Gamma function.
- `dist(x1, y1, x2, y2)` or `distance`: Euclidean distance between points (x1, y1) and (x2, y2).
- `clamp(x, min, max)`: Constrains x to be between min and max.
- `step(x, edge)`: Returns 1.0 if x ≥ edge, else 0.0.

### Trigonometric

- `sin(x)`, `cos(x)`, `tan(x)`: Trigonometric functions.
- `asin(x)`, `acos(x)`, `atan(x)`: Inverse trigonometric functions.
- `atan2(y, x)`: Arctangent of y/x, handling quadrants.

### Hyperbolic

- `sinh(x)`, `cosh(x)`, `tanh(x)`: Hyperbolic functions.
- `asinh(x)`, `acosh(x)`, `atanh(x)`: Inverse hyperbolic functions.

### Machine Learning / Activation

- `relu(x)`: Rectified Linear Unit (max(0, x)).
- `gelu(x)`: Gaussian Error Linear Unit.
- `softplus(x)`: Softplus function (log(1 + e^x)).
- `sigm(x)`: Sigmoid function (1 / (1 + e^-x)).
- `softmax(x, dim)`: Softmax normalization along specified dimension (converts to probabilities).
- `softmin(x, dim)`: Softmin normalization along specified dimension (inverse softmax).

### Interpolation

- `smoothstep(x, edge0, edge1)`: Hermite interpolation between edge0 and edge1.
- `smootherstep(x, edge0, edge1)`: Quintic interpolation (Perlin's improved smootherstep).
- `cubic_ease(a, b, t)` or `cubic`: In-Out Cubic interpolation between `a` and `b`.
- `sine_ease(a, b, t)` or `sine`: In-Out Sine interpolation between `a` and `b`.
- `elastic_ease(a, b, t)` or `elastic`: In-Out Elastic interpolation between `a` and `b`.
- `lerp(a, b, t)`: Linear interpolation: `a + (b - a) * w`.

### Aggregates & Tensor Operations

- `tmin(x, y)`: Element-wise minimum of x and y.
- `tmax(x, y): Element-wise maximum of x and y.
- `smin(x, ...)`: Scalar minimum. Returns the single smallest value across all input tensors/values.
- `smax(x, ...)`: Scalar maximum. Returns the single largest value across all input tensors/values.
- `sum(x)`: Sum of all elements.
- `mean(x)`: Mean value of all elements.
- `std(x)`: Standard deviation of all elements.
- `var(x)`: Variance of all elements.
- `median(x)`: Median value of all elements.
- `mode(x)`: Mode (most common value) of all elements.
- `quartile(x, k)`: Returns the k-th quartile (k=0 for min, 1 for 25th, 2 for 50th, 3 for 75th, 4 for max).
- `percentile(x, p)`: Returns the p-th percentile (p is 0-100).
- `quantile(x, q)`: Returns the q-th quantile (q is 0-1).
- `dot(a, b)`: Dot product of two tensors (flattens inputs to 1D) or lists.
- `moment(x, a, k)`: Returns the k-th moment of x centered around a.
- `topk(x, k)`: Returns a tensor with the **top K largest** values preserved at their original positions (others zeroed). For lists, returns the top K largest items sorted descending. (uses magnitude for complex numbers).
- `botk(x, k)`: Returns a tensor with the **bottom K smallest** values preserved at their original positions (others zeroed). For lists, returns the bottom K smallest items sorted ascending. (uses magnitude for complex numbers)
- `topk_ind(x, k)` or `topk_indices: Returns the **indices** of the top K largest values in the flattened tensor.
- `botk_ind(x, k)` or `botk_indices`: Returns the **indices** of the bottom K smallest values in the flattened tensor.
- `sort(x)`: Sorts elements in ascending order along the last dimension.
- `argsort(x)` or `argsort(x, descending)`: Returns the **indices** that would sort the tensor/list. Optional second parameter for descending order.
- `argmin(x)`: Returns the **index** of the minimum value in the flattened tensor/list.
- `argmax(x)`: Returns the **index** of the maximum value in the flattened tensor/list.
- `unique(x)`: Returns **unique elements** from tensor/list in sorted order.
- `tnorm(x)`: Tensor normalisation. Normalises x (L2 norm along last dimension).
- `snorm(x)`: The same as |x| for tensors.
- `swap(tensor, dim, index1, index2)`: Swaps two slices of a tensor along a specified dimension.
- `cossim(a, b)`: Computes cosine similarity between a and b along last dimension.
- `flip(x, dims)`: Flips tensor along specified dimensions. `dims` can be scalar or list.
- `cov(x, y)`: Compute covariance between x and y.
- `append(a, b)`: Appends `b` to `a`. If inputs are lists, it concatenates them. If inputs are tensors, it concatenates them along dim 0.
- `any(x)`: Returns 1.0 if any element in `x` is non-zero (True), else 0.0.
- `all(x)`: Returns 1.0 if all elements in `x` are non-zero (True), else 0.0.
- `cumsum(x)`: Returns the cumulative sum of elements along the batch dimension (dim 0).
- `cumprod(x)`: Returns the cumulative product of elements along the batch dimension (dim 0).
- `tensor(shape,value)`: Createss a tensor of given shape filled with value. Value can be omittend and defaults to zero.
- `flatten(value)`: Flattens a tensor to 1D. If input is list, it flattens nested lists into a single list.
- `shape(value)` : Returns the shape of a tensor as a tensor. If input is a list, returns lenght of the list as 1 value tensor. For numbers it returns empty tensor.
- `overlay(base, overlay, offset)`: Replaces a rectangular region of `base` with `overlay` starting at `offset`. Areas outside the base tensor are ignored. Overlay is cropped if it extends beyond the base tensor.
- 
### Advanced Tensor Operations

- `map(tensor, c1, ...)`: Remaps `tensor` using source coordinates.
  - Up to 3 coordinate mapping functions can be provided which map to the last (up to 3) dimensions of the tensor. Rest uses identity mapping.
- `ezconvolution(tensor, kw, [kh], [kd], k_expr)` or `ezconv`: Applies a convolution to `tensor`. Automatically permutes tensor to try to make it work with various inputs without the need to permute manually.
  - `k_expr` can be a math expression (using `kX`, `kY`, `kZ`) or a list literal.
- `convolution(tensor, kw, [kh], [kd], k_expr)` or `conv`: Applies a convolution to `tensor`. Does not perform automatic permutations. Expects standard PyTorch layout `(Batch, Channel, Spatial...)`.
  - `k_expr` can be a math expression (using `kX`, `kY`, `kZ`) or a list literal.
- `get_value(tensor, position)`: Retrieves a value from a tensor at the specified N-dimensional position (provided as a list or tensor). Uses the formula `pos0*strides[0] + pos1*strides[1] + ...` to find the linear index.
- `crop(tensor, position, size)`: Extracts a sub-tensor of specified `size` starting at `position` (both provided as lists/tensors). Areas outside the input tensor are filled with zeros.
- `permute(tensor, dims)` or `perm`: Rearranges the dimensions of the tensor. (e.g., `perm(a, [2, 3, 0, 1])`)
- `reshape(tensor, shape)` or `rshp`: Reshapes the tensor to a new shape. (e.g., `rshp(a, [S0*S1, S2, S3])`)
- `blur(x, sigma)` or `gaussian`: Applies a Gaussian blur with given `sigma` along last two or spatial dimensions (toggleable by optional parameter) - default use last 2 dimensions.
- `edge(x)`: Applies a Sobel edge detection filter along the last two dimension or spatial dimensions (Height and Width) - can be selected by optional value (0 or missing = use last 2 dimensions).
- `batch_shuffle(tensor, indices)` or `shuffle` or `select`: Reorders or gathers slices along the 0th dimension of a tensor based on a list of indices. (e.g., `shuffle(V0, [0, 0, 1])` repeats the first frame twice and then the second).
- `matmul(a, b)`: Matrix multiplication. For 1D vectors, performs dot product. For 2D+ tensors, performs standard matrix multiplication following NumPy rules.
- `cross(a, b)`: Computes the cross product (vector product) of two 3D vectors. Both inputs must have last dimension = 3. Returns a vector perpendicular to both inputs.

### Optical Flow

- `rife(img1, img2, [tiling_size, iterations, multi_scale])`: Calculates optical flow from `img1` to `img2` using RAFT.
  - `img1`, `img2`: Images or video frames [B, H, W, C].
  - `tiling_size`: (Optional) Size of tiles for high-res images. Default is `0` (auto-tile if > 2MPx). Supports fractions (e.g., `0.5`).
  - `iterations`: (Optional) Number of flow updates (default: 12).
  - `multi_scale`: (Optional) Whether to use a global pass for large movements (default: false (0)).
  - **Returns**: Flow vectors [B, H, W, 2].
- `motion_mask(flow)`: Generates an occlusion/motion mask from optical flow vectors.
  - `flow`: Flow vectors [B, H, W, 2].
  - **Returns**: Mask [B, H, W] in range [0, 1].
- `flow_to_image(flow)` or `flow_view(flow)`: Converts flow vectors to an RGB image for visualization.
  - `flow`: Flow vectors [B, H, W, 2].
  - **Returns**: RGB image [B, H, W, 3].
- `flow_apply(image, flow)` or `apply_flow(image, flow)`: Warps an image using optical flow vectors.
  - `image`: Image [B, H, W, C].
  - `flow`: Flow vectors [B, H, W, 2] from `rife()`.
  - **Returns**: Warped image [B, H, W, C].

### FFT (Tensor Only)

- `fft(x)`: Fast Fourier Transform (Time to Frequency).
- `ifft(x)` or `ifft(x, shape)`: Inverse Fast Fourier Transform (Frequency to Time), optional shape argument.
- `angle(x)`: Returns the element-wise angle (phase) of the complex tensor.

### Utility

- `print(x)`: Prints the value of x to the console and returns x.
- `print_shape(x)` or `pshp`: Prints the shape of x to the console and returns x.
- `pinv(x)`: Computes the permutation inverse of list. If `permute(i,x) = j`, then `permute(j,pinv(x)) = i`.
- `range(start, end, step)`: Generates a list of values from start (inclusive) to end (exclusive) with given step.
- `nan_to_num(x, nan_value, posinf_value, neginf_value)` or `nvl`: Replaces NaN and infinite values in tensor with specified values.
- `remap(v, i_min, i_max, o_min, o_max)`: Remaps value `v` from input range `[i_min, i_max]` to output range `[o_min, o_max]`.
- `timestamp()` or `now`: Returns current UNIX timestamp (precision to microseconds, can be different on other systems)
- `count(x)` or `length(x)` or `cnt(x)`: Returns the length of a list or the size of the first dimension of a tensor.

### Random Distributions

Generates random noise with default shape of aither first input or maximum of input sizes, depending on node setting.

- `random_normal(seed,[shape])` or `randn` or `noise`: generates a random tensor with normal distribution (var=1, mean=0).
- `random_uniform(seed,[shape])` or `rand`: generates a random tensor with uniform distribution [0, 1).
- `random_exponential(seed, lambda,[shape])` or `rande`: generates a random tensor with exponential distribution.
- `random_cauchy(seed, median, sigma,[shape])` or `randc`: generates a random tensor with Cauchy distribution.
- `random_log_normal(seed, mean, std,[shape])` or `randln`: generates a random tensor with log-normal distribution.
- `random_bernoulli(seed, p,[shape])` or `randb`: generates a random tensor with Bernoulli distribution. Parameter `p` is the probability of getting 1, can be aither float or tensor. If p is tensor, shape is ignored.
- `random_poisson(seed, lambda,[shape])` or `randp`: generates a random tensor with Poisson distribution. Lambda can be either float or tensor.
- `random_gamma(seed, shape, scale,[shape])` or `randg`: generates a random tensor with Gamma distribution. Shape parameter (α) controls the shape, scale parameter (θ) controls the scale.
- `random_beta(seed, alpha, beta,[shape])` or `randbeta`: generates a random tensor with Beta distribution in range [0, 1]. Alpha and beta are shape parameters.
- `random_laplace(seed, loc, scale,[shape])` or `randl`: generates a random tensor with Laplace (double exponential) distribution. Useful for L1 regularization and robust statistics.
- `random_gumbel(seed, loc, scale,[shape])` or `randgumbel`: generates a random tensor with Gumbel distribution. Used in Gumbel-softmax trick for neural networks.
- `random_weibull(seed, scale, concentration,[shape])` or `randw`: generates a random tensor with Weibull distribution. Used in reliability analysis and survival modeling.
- `random_chi2(seed, df,[shape])` or `randchi2`: generates a random tensor with Chi-squared distribution. Degrees of freedom `df` controls the shape. Sum of squared normal distributions.
- `random_studentt(seed, df,[shape])` or `randt`: generates a random tensor with Student's t distribution. Has heavier tails than normal distribution, useful for robust noise. As `df` increases, approaches normal distribution.

### Noise Generation

- `perlin(seed, scale, [octaves,[offset, [shape]]])` or `perlin_noise`: generates Perlin noise. `scale` controls the frequency of the noise, `octaves` adds additional layers of noise,  `offset` offsets the noise pattern, `shape` controls the output shape (default is determined by node inputs and settings).
- `plasma(seed, scale, [octaves,[offset, [shape]]])` or `turbulence` or `plasma_noise`: generates Plasma noise. Same parameters as perlin noise.
- `voronoi(seed, scale, [jitter], [offset], [shape])` or `voronoi_noise`: generates Voronoi noise. `scale` controls the frequency of the noise, `jitter` adds randomness to the cell boundaries, `offset` offsets the noise pattern, `shape` controls the output shape (default is determined by node inputs and settings).

### Bitwise Operations

Bitwise operations work with scalars, tensors, and lists, preserving bit patterns (especially important for floats where bit patterns are preserved, not values converted).

#### Shift Operators
- `a << b`: Left shift operator. Shifts bits of `a` left by `b` positions.
- `a >> b`: Right shift operator. Shifts bits of `a` right by `b` positions.


#### Bitwise Functions
- `band(a, b)` or `bitwise_and(a, b)`: Bitwise AND. Returns bits set in both operands.
- `bor(a, b)` or `bitwise_or(a, b)`: Bitwise OR. Returns bits set in either operand.
- `bxor(a, b)` or `bitwise_xor(a, b)`: Bitwise XOR. Returns bits set in exactly one operand.
- `bnot(a)` or `bitwise_not(a)`: Bitwise NOT. Inverts all bits in the operand.
- `bitcount(a)`, `popcount(a)`, or `popcnt(a)`: Count set bits. Returns the number of set bits (1s) in the binary representation as a float.



### Stack

- `stack_push(id, value)`: Pushes value to stack with id.
- `stack_pop(id)`: Pops value from stack with id.
- `stack_get(id)`: Gets value from stack with id.
- `stack_clear(id)`: Clears stack with id.
- `stack_has(id)`: Checks if stack with id exists.

## Variables

- **Common variables (except FLOAT, MODEL, VAE and CLIP)**:
  - `D{N}` - position in n-th dimension of tensor (for example D0, D1, D2, ...)
  - `S{N}` - size of n-th dimension of tensor (for example S0, S1, S2, ...)
  - `V{N}` - value input (for example V0, V1, V2, ...) - input type
  - `V` - list of value inputs
  - `F{N}` - float input (for example F0, F1, F2, ...) - float type
  - `F` - list of float inputs
  - `Fcnt` or `F_count`: Number of float inputs.
  - `Vcnt` or `V_count`: Number of value inputs.
  - `depth`: Current recursion depth (0 at top level)
- **common inputs** (legacy):
  - `a`, `b`, `c`, `d`
- **Extra floats** (legacy):
  - `w`, `x`, `y`, `z`
- **INSIDE IFFT**
  - `F` or `frequency_count` – frequency count (freq domain, iFFT only)
  - `F` or `frequency_count` - frequency count (freq domain, iFFT only)
  - `K` or `frequency` - isotropic frequency (Euclidean norm of indices, iFFT only)
  - `Kx`, `Ky`, `K_dimN` - frequency index for specific dimension
  - `Fx`, `Fy`, `F_dimN` - frequency count for specific dimension
- **IMAGE and LATENT**:
  - `C` or `channel` - channel of image
  - `X` - position X in image. 0 is in top left
  - `Y` - position Y in image. 0 is in top left
  - `W` or `width` - width of image. y/width = 1
  - `H` or `height`- height of image. x/height = 1
  - `B` or `batch` - position in batch
  - `T` or `batch_count` - number of batches
  - `N` or `channel_count` - count of channels
- **IMAGE KERNEL**:
  - `kX`, `kY` - position in kernel. Centered at 0.0.
  - `kW`, `kernel_width` - width of kernel.
  - `kH`, `kernel_height` - height of kernel.
  - `kD`, `kernel_depth` - depth of kernel.

- **AUDIO**:
  - `B` or 'batch' - position in batch
  - `N` or `channel_count` - count of channels
  - `C` or `channel` - channel of audio
  - `S` or `sample` – current audio sample
  - `S` or `sample` - current audio sample
  - `T` or `sample_count` - audio lenght in samples
  - `R` or `sample_rate` - sample rate

- **VIDEO**
  - refer to `IMAGE and LATENT` for visual part (but `batch` is `frame` and `batch_count` is `frame_count`)
  - refer to `AUDIO` for sound part
- **NOISE**
  - refer to `IMAGE and LATENT` for most variables
  - `I` or `input_latent` - latent used as input to generate noise before noise is generated into it
- **GUIDER**
  - refer to `IMAGE and LATENT`
  - `sigma` - current sigma value
  - `seed` - seed used for noise generation
  - `steps` - total number of sampling steps
  - `current_step` - current step index (0 to steps)
  - `sample` - tensor input to guider or output from sampling

- **CONDITIONING, SIGMAS and FLOAT**
  - no additional variables
- **MODEL, CLIP and VAE**
  - `L` or `layer` - a position of layer from beginning of object
  - `LC` or `layer_count` - a count of layers
- **Constants**: `e`, `pi`
