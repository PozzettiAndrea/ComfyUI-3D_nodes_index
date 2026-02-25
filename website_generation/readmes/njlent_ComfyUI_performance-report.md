# ComfyUI Execution Time Reporter

A comprehensive performance monitoring and analysis tool for ComfyUI workflows that tracks execution time, memory usage, and system resource utilization.

## 🚀 Features

### ⏱️ **Execution Time Tracking**
- **Precise timing** for each node in your workflow
- **Execution order** preservation with chronological numbering
- **Performance analysis** with nodes ranked by execution time
- **Overhead calculation** showing ComfyUI framework overhead

### 🧠 **Memory Monitoring**
- **GPU Memory (VRAM) tracking** - allocation changes and peak usage per node
- **System Memory (RAM) monitoring** - process and system-wide memory usage
- **Memory leak detection** - identify nodes that don't release memory properly
- **Peak usage identification** - find memory bottlenecks in your workflow

### 💻 **System Information**
- **Complete hardware profile** - CPU, RAM, GPU specifications
- **Software environment** - Python, PyTorch, CUDA, ComfyUI versions
- **Real-time resource usage** - CPU usage, memory availability
- **GPU details** - VRAM capacity, compute capability, current usage

### 📊 **Detailed Reports**
- **Execution timeline** with memory annotations
- **Performance rankings** sorted by duration
- **Memory analysis** with resource-intensive nodes highlighted
- **System overview** for reproducibility and debugging

## 📦 Installation

1. **Clone or download** this repository into your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/njlent/ComfyUI_performance-report
   ```

2. **Restart ComfyUI** - the node will be automatically loaded

3. **Dependencies** (usually already available in ComfyUI):
   - `psutil` - for system monitoring
   - `torch` - for GPU memory tracking (optional)
   - `comfy.model_management` - for ComfyUI integration (optional)

## 🎯 Usage

### Basic Usage
1. **Add the ExecutionTimeReporter node** to any workflow
2. **Run your workflow** - timing and memory tracking happens automatically
3. **Check the report** in `ComfyUI/output/reports/` after completion

### Advanced Usage
- **No connections required** - the node works independently
- **Multiple workflows** - each gets its own timestamped report
- **Memory optimization** - use reports to identify resource bottlenecks
- **Performance tuning** - compare different workflow configurations

## 📋 Report Format

### System Information Section
```
SYSTEM INFORMATION:
--------------------------------------------------------------------------------
Operating System: Windows 10
Architecture: AMD64
Processor: Intel64 Family 6 Model 142 Stepping 10, GenuineIntel
Python Version: 3.11.5 (CPython)
ComfyUI Version: 0.3.52
CPU Cores: 8 physical, 16 logical
CPU Usage: 45.2%
CPU Frequency: 2800 MHz (max: 4200 MHz)
System RAM: 32.0 GB total, 18.5 GB available (42.2% used)
PyTorch Version: 2.1.0
CUDA Version: 12.1
cuDNN Version: 8902
GPU Devices: 1
  GPU 0: NVIDIA GeForce RTX 4090
    VRAM: 24.0 GB
    Compute Capability: 8.9
    Multiprocessors: 128
    Current Usage: 2.34 GB allocated, 2.50 GB reserved
```

### Execution Timeline
```
EXECUTION TIMES (in execution order):
--------------------------------------------------------------------------------
# 1 Node   4:    1.726s - VHS_LoadVideo [GPU: +0.125GB, Peak: 2.341GB]
# 2 Node  14:    0.001s - Get resolution [Crystools]
# 3 Node   2:   16.430s - YoloSmartTracker_Video [GPU: +1.847GB, Peak: 4.188GB, RAM: +0.234GB]
# 4 Node  12:    0.003s - PreviewImage
# 5 Node   6:    3.972s - VideoCombineTiles_Advanced [GPU: -0.512GB, Peak: 3.676GB]
```

### Performance Analysis
```
PERFORMANCE ANALYSIS (sorted by duration, slowest first):
--------------------------------------------------------------------------------
 1. Node   2:   16.430s (65.2%) - YoloSmartTracker_Video
 2. Node   6:    3.972s (15.8%) - VideoCombineTiles_Advanced
 3. Node   8:    3.167s (12.6%) - VHS_VideoCombine
```

### Memory Analysis
```
MEMORY ANALYSIS:
--------------------------------------------------------------------------------
GPU Memory Changes (nodes with significant changes):
  Node   2:   +1.847GB - YoloSmartTracker_Video
  Node   4:   +0.125GB - VHS_LoadVideo
  Node   6:   -0.512GB - VideoCombineTiles_Advanced

Peak GPU Memory Usage (top nodes):
  Node   2:    4.188GB - YoloSmartTracker_Video
  Node   6:    3.676GB - VideoCombineTiles_Advanced
```

## 🔧 Technical Details

### Modular Architecture
- **`__init__.py`**: Main module initialization, imports nodes and monitoring system
- **`nodes.py`**: Contains the ExecutionTimeReporter node class and ComfyUI mappings
- **`monitoring.py`**: Core monitoring system with execution patching and report generation
- **Clean separation**: Easy to maintain, extend, and debug

### Memory Tracking
- **GPU Memory**: Uses `torch.cuda.memory_allocated()` and `torch.cuda.memory_reserved()`
- **Peak Detection**: `torch.cuda.reset_peak_memory_stats()` for per-node peak tracking
- **System Memory**: `psutil.Process().memory_info()` for process-specific tracking
- **Smart Filtering**: Only shows significant changes (>1MB GPU, >10MB RAM)

### Performance Impact
- **Minimal overhead** - typically <0.1% of total execution time
- **Non-intrusive** - doesn't modify your workflow logic
- **Memory efficient** - cleans up tracking data after report generation

### Compatibility
- **ComfyUI versions**: All recent versions
- **Operating Systems**: Windows, Linux, macOS
- **GPU Support**: NVIDIA CUDA, AMD ROCm (limited), CPU-only
- **Python versions**: 3.8+


### 📁 Output Location

Reports are saved to: `ComfyUI/output/reports/execution_report_YYYYMMDD-HHMMSS.txt`

## 💡 Best Practices

### Workflow Optimization
1. **Identify bottlenecks** - Focus on nodes taking >10% of total time
2. **Memory management** - Watch for nodes with large positive memory deltas
3. **Batch processing** - Compare single vs batch processing performance
4. **Model loading** - Track VRAM usage for different model combinations

### Performance Analysis
- **Compare configurations** - Test different settings and compare reports
- **Monitor trends** - Track performance changes over time
- **Resource planning** - Use memory stats to plan hardware requirements
- **Debugging** - Identify problematic nodes causing slowdowns or memory issues

## 📊 Example Use Cases

### 1. Video Processing Workflow
```
Typical bottlenecks found:
- Video loading: High I/O time
- AI processing: High GPU memory usage
- Encoding: High CPU usage
```

### 2. Image Generation Pipeline
```
Common patterns:
- Model loading: Initial VRAM spike
- Sampling: Consistent GPU usage
- Post-processing: CPU-intensive
```

### 3. Batch Processing Analysis
```
Scaling insights:
- Memory usage per batch size
- Processing time vs quality trade-offs
- Optimal batch sizes for your hardware
```

## 🐛 Troubleshooting

### Common Issues
1. **"No timing data found"** - Ensure the ExecutionTimeReporter node is in your workflow
2. **Missing GPU stats** - PyTorch with CUDA support required for GPU memory tracking
3. **Permission errors** - Check write permissions for the output/reports directory
4. **Incomplete reports** - Workflow must complete successfully for full report generation

### Debug Information
The node provides console output for debugging:
```
[ExecutionTimeReporter] Started tracking workflow abc123...
[ExecutionTimeReporter] Workflow completed - generating final report for 8 nodes...
[ExecutionTimeReporter] Report saved to: .../execution_report_20251008-231542.txt
```

### Performance Impact
- **Overhead**: Typically <0.1% of total execution time
- **Memory**: ~1-5MB additional RAM usage during tracking
- **Storage**: Report files are typically 5-50KB depending on workflow size
