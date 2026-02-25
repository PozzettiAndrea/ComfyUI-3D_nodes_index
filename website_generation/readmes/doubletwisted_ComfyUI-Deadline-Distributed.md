# ComfyUI-Deadline-Distributed

**Deadline-specific fork** of distributed image generation for ComfyUI using Thinkbox Deadline render farm.

> **Note**: This is a specialized fork of the original ComfyUI distributed rendering system, specifically adapted for Deadline render farm integration.

Check out a quick demo showing how ComfyUI can play nice with Deadline. Please check out the video:
<p align="center"> <a href="https://youtu.be/NFmIvEoEPiU"> <img src="https://img.youtube.com/vi/NFmIvEoEPiU/maxresdefault.jpg" alt="ComfyUI x Deadline: Leverage Your GPUs" /> </a> </p>

## Dependencies

This plugin requires **[ComfyUI-Deadline-Plugin](https://github.com/doubletwisted/ComfyUI-Deadline-Plugin)** to be installed first for basic Deadline submission functionality.

### Installation Order:
1. Install **[ComfyUI-Deadline-Plugin](https://github.com/doubletwisted/ComfyUI-Deadline-Plugin)** (standalone Deadline submission)
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/doubletwisted/ComfyUI-Deadline-Plugin.git
   ```
2. Install **ComfyUI-Deadline-Distributed** (distributed rendering via Deadline)
   ```bash
   cd ComfyUI/custom_nodes  
   git clone <this-repository-url>
   ```

## Deadline-Specific Features

- **Deadline Worker Management**: Automatic worker registration via Deadline jobs
- **Deadline Job Integration**: Master-worker coordination through Deadline render farm
- **Deadline Progress Reporting**: Status updates through Deadline Monitor
- **Distributed Seed Generation**: Coordinate seed distribution across Deadline workers
- **Worker Result Collection**: Automatic image collection from Deadline workers

## Usage

1. Set up workers via Deadline job submission
2. Use the Distributed Control Panel to monitor Deadline workers
3. Add `DistributedSeed` and `DistributedCollector` nodes to your workflow
4. Submit jobs using `DeadlineSubmit` node (from ComfyUI-Deadline-Plugin)

## Architecture

- **Master**: Orchestrates workflow distribution via Deadline and collects results
- **Deadline Workers**: Execute workflow segments on render farm nodes
- **Deadline Integration**: Complete worker lifecycle management through Deadline

---

*This fork is specifically designed for Deadline render farms and includes Deadline-specific optimizations and integrations not found in the original distributed rendering implementation.*
