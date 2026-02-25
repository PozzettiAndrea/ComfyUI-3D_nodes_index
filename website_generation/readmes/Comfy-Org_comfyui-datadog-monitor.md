# ComfyUI Datadog Monitor

Background extension that automatically enables comprehensive Datadog APM tracing and profiling for ComfyUI. No UI nodes - runs entirely in the background.

## Features

- **Automatic Full Instrumentation**: Uses `ddtrace.auto` to instrument 77+ Python libraries
- **Memory Profiling**: Heap allocation tracking and memory growth detection
- **CPU Profiling**: Function-level CPU usage and hot path identification
- **Distributed Tracing**: Automatic trace correlation across all operations
- **Zero Configuration**: Works automatically when installed - no nodes to add
- **Background Only**: No UI nodes, runs entirely in the background

## What Gets Traced

When this node is installed, Datadog automatically traces:
- HTTP requests (model downloads, API calls)
- File I/O operations (model loading, image saves)
- Database operations
- Subprocess launches
- Async operations
- Thread creation and locks
- And 70+ more integrations

## Installation

1. Install in your ComfyUI custom_nodes directory:
```bash
cd custom_nodes
git clone https://github.com/Comfy-Org/comfyui-datadog-monitor
cd comfyui-datadog-monitor
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export DD_ENV=production
export DD_SERVICE=comfyui-inference
export DD_VERSION=1.0.0
export DD_AGENT_HOST=localhost  # Your Datadog agent host
```

3. Restart ComfyUI - profiling starts automatically

## How It Works

This extension uses `ddtrace.auto` which must be imported before any other imports. When ComfyUI loads this extension, it:
1. Imports `ddtrace.auto` to enable full instrumentation
2. Configures service tags for proper APM organization
3. Starts continuous profiling in the background

No nodes appear in the UI - everything runs automatically in the background.

## Memory Monitoring

While the DDTrace profiler handles detailed memory profiling, the Go sidecar handles:
- Memory limit enforcement (via ulimit)
- OOM detection (exit code 137)
- Automatic restart on OOM
- Job failure tracking


## Environment Variables

- `DD_ENV`: Environment name (default: production)
- `DD_SERVICE`: Service name (default: comfyui-inference)
- `DD_VERSION`: Service version (default: 1.0.0)
- `DD_PROFILING_ENABLED`: Enable profiling (default: true via ddtrace.auto)
- `DD_LOGS_INJECTION`: Inject trace IDs into logs (default: true)
- `DD_TRACE_SAMPLE_RATE`: Trace sampling rate 0-1 (default: 1)
- `DD_AGENT_HOST`: Datadog agent hostname (default: localhost)

## Viewing in Datadog

1. **APM**: See all traces under the service name you configured
2. **Profiler**: View memory and CPU profiles in the Profiler tab
3. **Logs**: Correlated with trace IDs for easy debugging

## OOM Debugging

When debugging OOM issues, look for:

1. **Memory Profile Timeline**: Shows memory growth over time
2. **Top Allocators**: Functions allocating the most memory
3. **Trace Flamegraphs**: See which operations use most memory
4. **Correlated Logs**: Jump from high memory moments to logs

The Go sidecar will:
- Enforce memory limits (default 64GB)
- Detect OOM (exit code 137)
- Auto-restart ComfyUI
- Mark jobs as failed in database

## Performance Impact

- **Minimal overhead**: ~1-3% CPU overhead from profiling
- **No expensive operations**: No object scanning or gc.get_objects() calls
- **Sampling-based**: Profiler samples rather than instruments every call

## Troubleshooting

**DDTrace fails to start**: Check if Datadog agent is running and accessible.

**No data in Datadog**: Verify DD_AGENT_HOST points to your Datadog agent.

**Import error**: Make sure `ddtrace` is installed: `pip install ddtrace`

## License

MIT