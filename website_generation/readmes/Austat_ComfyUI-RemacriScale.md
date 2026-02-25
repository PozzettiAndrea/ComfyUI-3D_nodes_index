# ComfyUI-RemacriScale
Using Remacri upscaler, upscale a video using one of three providers supported by onnx and then downscale.

<img width="315" height="128" alt="image" src="https://github.com/user-attachments/assets/8d4fc74a-b646-4094-b2d7-3214f261f50e" />


Installation

Method 1: Clone the Repository Navigate to your ComfyUI custom_nodes directory. Run:

git clone https://github.com/Austat/ComfyUI-RemacriScale

cd ComfyUI-RemacriScale

pip install -r requirements.txt

Download needed onnx - files to your ComfyUI or custom models/upscale_models/ - folder.

Restart ComfyUI.

First upscaling run will take longer time as each used resolution needs it's own TensorRT engine. Consequent runs after that are considerably faster, as they use the previously created timing cache. With nVidia 5090 RTX, it took 30 minutes to build a engine for 1280 x 720 resolution.

Supported methods are:

           "TensorrtExecutionProvider",
            "CUDAExecutionProvider",
            "ROCmExecutionProvider",
            "CPUExecutionProvider"

<details>
  <summary>Details about TensorRT timing cache and engine (aka tactic timing data)</summary>

## What the TensorRT timing cache is
* The timing cache is a small binary file that stores tactic timing data — basically, TensorRT’s internal measurements of which GPU kernels are fastest for each layer of your model.

* When TensorRT builds an engine, it tries many possible implementations (“tactics”) for each operation. This can take a long time, especially at high resolutions.

* The timing cache is a way to save the results of that expensive search so TensorRT doesn’t need to repeat it.

## How the timing cache is created
* You run the model with TensorRT for the first time at a specific resolution.

* TensorRT benchmarks many tactics internally.

* If timing‑cache is enabled and the path exists, TensorRT writes a file containing the best tactics it found.

* Next time you run the model at the same resolution, TensorRT loads the timing cache and skips the benchmarking phase.

* This makes engine building much faster and more stable.

## Why we generate a separate timing cache per resolution
* TensorRT’s tactic choices depend heavily on the input shape.
* A 720×1280 input and a 480×832 input produce different optimal kernels.

* If you reuse the same timing cache for different resolutions, TensorRT may:

* ignore the cache

* or pick suboptimal tactics

* or fail to build the engine entirely

By naming the cache file like:

* trt_timing_cache_720x1280.bin

* …we guarantee that:

* each resolution gets its own optimized tactic set

* engine builds are faster

* TensorRT is more stable

* high‑resolution builds (like 1280×720) succeed reliably

## Why this matters

Without a timing cache:

* TensorRT must benchmark everything from scratch

* high‑resolution builds may fail due to timeouts or memory spikes

* engine builds take much longer

* ORT may fall back to CPU if TRT fails

## With a timing cache:

* engine builds are faster

* memory usage is more predictable

* TensorRT becomes much more stable

* Repeated runs at the same resolution are nearly instant First upscaling run will take longer time as each used resolution needs it's own TensorRT engine. Runs after that one are considerably faster as they use the previously created timing cache.

