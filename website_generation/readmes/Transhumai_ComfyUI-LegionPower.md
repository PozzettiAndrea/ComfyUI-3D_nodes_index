# ComfyUI-LegionPower

**Execute ComfyUI workflows in separate worker instances for better GPU utilization and memory management.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## 🎯 What is LegionPower?

LegionPower allows you to **execute ComfyUI workflows in separate ComfyUI worker instances**, enabling:

- **Multi-GPU orchestration**: Run different workflows on different GPUs simultaneously
- **Memory isolation**: Kill worker instances to free VRAM from memory-hungry nodes (like ReActor)
- **Parallel execution**: Execute multiple workflows concurrently without blocking the main UI
- **Process isolation**: Crashes in worker workflows don't affect your main ComfyUI instance

Perfect for scenarios where you need to:
- Use ReActor or other VRAM-intensive nodes without permanent memory bloat
- Distribute workload across multiple GPUs
- Run long-running workflows without blocking your main workflow
- Test workflows in isolation

---

## 📦 Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "LegionPower"
3. Click Install
4. Restart ComfyUI

### Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Transhumai/ComfyUI-LegionPower.git
cd ComfyUI-LegionPower
pip install -r requirements.txt
```

Restart ComfyUI after installation.

---

## 🚀 Quick Start

### 1. Create a Worker Workflow

Create a workflow that will run in the worker instance. **It must contain**:
- **LegionImporter** node at the start (receives data from Master)
- Your processing nodes
- **LegionExporter** node at the end (sends results back)

**Example worker workflow:**
```
LegionImporter → ReActorRestoreFace → LegionExporter
```

Save this as `my_worker_workflow.json` in:
- `ComfyUI/user/default/ComfyUI-LegionPower/workflows/`

### 2. Create a Master Workflow

In your main ComfyUI workflow:

1. Add **Legion: Configuration** node
   - Configure the worker settings (usually defaults are fine)
   - Set `workflow:` to your worker workflow filename
   - Set `dry_run: false` for real execution

2. Add **Legion: Master** node
   - Connect your data to `input_1`, `input_2`, etc.
   - Connect the config from step 1

3. Use the outputs from Master node in your main workflow

**Example:**
```
LoadImage → Master.input_1
Config → Master.legion_config

Master.output_1 → SaveImage
```

---

## 🎮 Nodes Reference

### Legion: Configuration
**Purpose**: Configure worker instance settings

**Parameters**:
- `comfyui.port`: Port for worker (use `auto` for automatic assignment)
- `execution.dry_run`: Test mode without actual execution (default: `true`)
- `execution.asynch`: Run asynchronously (default: `false`)
- `execution.extra_args`: Additional CLI arguments for worker ComfyUI
- `workflow`: Filename of workflow to execute in worker

**Outputs**: `legion_config`

---

### Legion: Master (3/6/12 channels)
**Purpose**: Execute workflow in worker instance

**Inputs**:
- `legion_config` (required): Configuration from Legion: Configuration node
- `input_1` through `input_12`: Data to send to worker

**Outputs**:
- `legion_campaign`: Campaign handle for async workflows
- `output_1` through `output_12`: Results from worker

**Execution Modes**:
- **Sync** (`asynch: false`): Blocks until worker completes, returns results immediately
- **Async** (`asynch: true`): Returns immediately, use Legion: Join to get results later

---

### Legion: Importer (Worker-side)
**Purpose**: Receives data from Master workflow

**Inputs**:
- `data_exchange_root`: Automatically patched by Master (don't connect manually)

**Outputs**:
- `output_1` through `output_5`: Deserialized data from Master
- `data_exchange_root`: Pass-through for Exporter

**Usage**: Place at the start of worker workflow, connect outputs to your processing nodes

---

### Legion: Exporter (Worker-side)
**Purpose**: Sends results back to Master workflow

**Inputs**:
- `data_exchange_root`: Connect from Importer's output
- `input_1` through `input_5`: Data to send back to Master

**Outputs**: None (terminal node)

**Usage**: Place at the end of worker workflow, connect data you want to return

---

### Legion: Join Campaign
**Purpose**: Wait for async workflow completion and retrieve results

**Inputs**:
- `legion_campaign`: Campaign handle from Master node (async mode)

**Outputs**:
- `output_1` through `output_5`: Results from worker

**Usage**: Only needed for async workflows

---

### Legion: Join All Campaigns
**Purpose**: Wait for multiple async workflows to complete

**Inputs**:
- `campaign_1` through `campaign_4`: Campaign handles from multiple Master nodes

**Outputs**:
- `campaign_1` through `campaign_4`: Pass-through of completed campaigns

**Usage**: Synchronization point for multiple parallel workflows

---

### Legion: Warmupper
**Purpose**: Pre-start worker without executing workflow

**Inputs**:
- `legion_config`: Worker configuration

**Outputs**:
- `legion_campaign`: Warmed-up campaign handle

**Usage**: Optional - start worker in advance to reduce first-execution latency

---

## 💡 Usage Examples

### Example 1: Simple Face Restoration

**Worker workflow** (`face_restore.json`):
```
[LegionImporter] 
    ↓ output_1
[ReActorRestoreFace]
    ↓ image
[LegionExporter.input_1]
```

**Master workflow**:
```
[LoadImage] → [Master.input_1]
[Config]    → [Master.legion_config]

Config settings:
  workflow: face_restore.json
  dry_run: false
  asynch: false

[Master.output_1] → [SaveImage]
```

### Example 2: Async Processing

**Master workflow**:
```
[LoadImage] → [Master.input_1]
[Config]    → [Master.legion_config]

Config: asynch: true

[Master.legion_campaign] → [LegionJoin.legion_campaign]
[LegionJoin.output_1]   → [SaveImage]

// Continue main workflow while worker processes in background...
```

### Example 3: Multi-GPU Parallel Execution

```
GPU 0 (Master workflow):
[LoadBatch] → Split into images

GPU 1 (Worker 1 - port 8200):
[Master1.input_1] = images[0:5]
Config 1:
  port: 8200
  env_vars:
    CUDA_VISIBLE_DEVICES: "1"

GPU 2 (Worker 2 - port 8201):  
[Master2.input_1] = images[5:10]
Config 2:
  port: 8201
  env_vars:
    CUDA_VISIBLE_DEVICES: "2"

[JoinAll] waits for both workers
↓
[CombineResults] → [SaveVideo]
```

### Example 4: Memory-Optimized Worker

**For VRAM-intensive workflows (e.g., ReActor)**:
```yaml
Config:
  execution:
    env_vars:
      PYTORCH_CUDA_ALLOC_CONF: "max_split_size_mb:512"
      CUDA_VISIBLE_DEVICES: "1"
    extra_args: "--lowvram"
```

This configuration:
- Limits CUDA memory fragmentation
- Uses specific GPU
- Enables low VRAM mode

---

## ⚙️ Configuration Details

### Default Configuration Location

LegionPower stores configuration in:
```
ComfyUI/user/default/ComfyUI-LegionPower/
├── config.yaml                 # Global settings
├── default_legion_config.yaml  # Template for worker configs
├── workflows/                  # Worker workflow files
└── temp/                       # Temporary data exchange (auto-cleaned)
```

### Global Settings (`config.yaml`)

```yaml
ports:
  start_port: 8200      # First port for auto-assignment
  max_workers: 20       # Maximum concurrent workers

paths:
  workflows_roots:      # Where to find worker workflows
    - "{legion_runtime}/workflows"
  temp_root_dir: "{legion_runtime}/temp"

logging:
  level: INFO
```

### Worker Configuration Template

Edit `default_legion_config.yaml` to change defaults for new Configuration nodes:

```yaml
comfyui:
  type: local_process
  port: auto
  paths:
    comfyui_path:        # Leave empty for auto-detect
    python_executable:   # Leave empty for auto-detect

execution:
  dry_run: false         # Set to false for real execution
  asynch: false          # Set to true for async mode
  extra_args: ""         # e.g., "--gpu-only --preview-method auto"
  env_vars:              # Environment variables for worker
    # CUDA_VISIBLE_DEVICES: "0"
    # TORCH_COMPILE_DISABLE: "1"

workflow: my_workflow.json
```

---

## 🔧 Advanced Features

### Extra Command-Line Arguments

Pass additional arguments to worker ComfyUI instance:

```yaml
execution:
  extra_args: "--gpu-only --preview-method auto --vram-mode high"
```

Supports both string and list format:
```yaml
extra_args: ["--gpu-only", "--preview-method", "auto"]
```

### Environment Variables

Control worker environment with custom variables:

```yaml
execution:
  env_vars:
    CUDA_VISIBLE_DEVICES: "1"              # Use only GPU 1
    TORCH_COMPILE_DISABLE: "1"             # Disable torch compilation
    PYTORCH_CUDA_ALLOC_CONF: "max_split_size_mb:512"
```

**Common use cases**:
- **GPU Selection**: `CUDA_VISIBLE_DEVICES: "0"` or `"1,2"` for multi-GPU
- **Memory Management**: `PYTORCH_CUDA_ALLOC_CONF` for VRAM allocation
- **Compilation**: `TORCH_COMPILE_DISABLE: "1"` to disable torch.compile
- **Debugging**: `CUDA_LAUNCH_BLOCKING: "1"` for synchronous CUDA ops

### Worker Reuse

Workers are automatically reused for identical configurations:
- Same port = reuses existing worker
- `port: auto` creates new worker per config instance
- Workers stay alive between executions for faster subsequent runs

### Supported Data Types

Current serializers support:
- **Images**: Single image tensors and batches
- **Primitives**: int, float, str, bool

Coming soon:
- LATENT
- CONDITIONING  
- MODEL
- CLIP

---

## 🐛 Troubleshooting

### Worker fails to start

**Symptoms**: `Worker on port XXXX failed to start in time`

**Solutions**:
1. Check port is not already in use
2. Verify ComfyUI path is correct
3. Check worker has required custom nodes installed
4. Look at ComfyUI console for worker error messages

### No output from worker

**Symptoms**: `Output manifest not found`

**Solutions**:
1. Verify worker workflow has **LegionExporter** node
2. Check LegionExporter has inputs connected
3. Check worker workflow completed successfully (no errors in console)
4. Verify LegionExporter's `data_exchange_root` is connected from Importer

### Worker workflow errors

**Symptoms**: Errors in worker execution

**Solutions**:
1. Test workflow directly in worker instance (port 8200)
2. Verify worker has required models/checkpoints
3. Check custom nodes are installed in worker
4. Ensure data types match between Master and Worker

### Memory not freed

**Issue**: VRAM not released after worker execution

**Solution**: Workers stay alive for reuse. To force cleanup:
- Change worker config (e.g., increment port number)
- Restart ComfyUI
- Kill worker process manually (PID shown in console)

---

## 🎯 Roadmap

### v0.2 (Coming Soon)
- [ ] WebSocket-based execution (remove polling)
- [ ] Docker worker support
- [ ] Remote worker support (RunPod, Vast.ai)
- [ ] LATENT, CONDITIONING, MODEL serializers
- [ ] Worker pool with priority queue
- [ ] GPU affinity configuration

### v1.0 (Future)
- [ ] Web UI for worker management
- [ ] Workflow versioning
- [ ] Result caching
- [ ] Distributed execution across multiple machines
- [ ] Cloud worker auto-scaling

---

## 📄 License

Copyright 2024 Transhumai

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 💬 Support

- GitHub Issues: https://github.com/Transhumai/ComfyUI-LegionPower/issues
- Discord: [Coming Soon]

---

## 🙏 Credits

Created by [Transhumai](https://github.com/Transhumai)

Special thanks to the ComfyUI community!

---

**Note**: This is an MVP release. Some features are still in development. 
Report bugs and request features on our GitHub issues page!
