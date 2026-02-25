# ComfyUI-Adept-Sampler

Advanced custom samplers and schedulers for ComfyUI, ported from the Stable Diffusion WebUI reForge extension.

> **Also available for SD WebUI reForge:** [nawka12/adept-sampler](https://github.com/nawka12/adept-sampler)

## Features

### Samplers (3)

| Sampler | Description |
|---------|-------------|
| **Adept Solver** | Hybrid **Predictor-Corrector** pipeline using Adams-Bashforth integration (DEIS) with UniPC correction steps and dynamic thresholding |
| **Adept Ancestral Solver** | **Enhanced Euler Ancestral** with phase-dependent step sizing, adaptive noise injection (Eta), and context-aware derivative corrections |
| **AkashicSolver v2** | **SA-Solver** (Stochastic Adams) implementation integrated with **SMEA** (Sinusoidal Multipass) interpolation for high-res coherence |

### Schedulers (17+)

| Category | Schedulers |
|----------|-----------|
| **Anime-Optimized** | AOS-V (v-prediction), AOS-ε (epsilon), AkashicAOS (Continuous Power-Function) |
| **Research-Based** | AYS-SDXL (Align Your Steps), JYS (Jump Your Steps), SNR-Optimized |
| **General Purpose** | Entropic, Cosine-Annealed, LogSNR-Uniform, Constant-Rate |
| **Experimental** | Stochastic, Jittered-Karras, Tanh Mid-Boost, Exponential Tail |

## Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone or copy this repository:
   ```bash
   git clone https://github.com/nawka12/ComfyUI-Adept-Sampler.git
   # OR copy the folder directly
   ```

3. Restart ComfyUI

## Usage

### Using Schedulers

Connect a scheduler node to generate custom sigma schedules:

```
[Load Checkpoint] → [Adept Scheduler (AOS-V)] → [SamplerCustom] → [VAE Decode]
                                                      ↑
                                               [Sampler Node]
```

### Using Samplers

Connect a sampler node to use custom sampling algorithms:

```
[Load Checkpoint] → [BasicScheduler] → [SamplerCustom] → [VAE Decode]
                                             ↑
                                [Adept Solver Sampler]
```

## Node Reference

### Scheduler Nodes

All scheduler nodes take a `MODEL` input and output `SIGMAS`.

| Node | Parameters |
|------|------------|
| **Adept Scheduler (AOS-V)** | steps |
| **Adept Scheduler (AOS-ε)** | steps |
| **Adept Scheduler (AkashicAOS)** | steps |
| **Adept Scheduler (Entropic)** | steps, power |
| **Adept Scheduler (JYS)** | steps |
| **Adept Scheduler (AYS-SDXL)** | steps |
| **Adept Scheduler (Stochastic)** | steps, noise_type, noise_scale, base_schedule |
| **Adept Scheduler (Advanced)** | steps, scheduler (dropdown), entropic_power |

### Sampler Nodes

All sampler nodes output `SAMPLER` for use with SamplerCustom.

| Node | Key Parameters |
|------|----------------|
| **Adept Solver Sampler** | order (1-3), use_corrector, detail enhancement options |
| **Adept Ancestral Sampler** | eta, s_noise, adaptive_eta, phase_noise, enhanced_derivative |
| **AkashicSolver v2** | tau (0-1), eta, s_noise, order, adaptive_eta, smea_strength, ndb_strength (High-Frequency Injection) |

## Recommended Settings

### For v-prediction models (e.g., SDXL)
- Scheduler: **AOS-V** or **AYS-SDXL**
- Sampler: **Adept Solver** (order=2, corrector=on)

### For epsilon-prediction models
- Scheduler: **AOS-ε**
- Sampler: **Adept Ancestral** (eta=1.0, adaptive_eta=on)

### For EQ-VAE models (e.g., AkashicPulse)
- Scheduler: **AkashicAOS**
- Sampler: **AkashicSolver v2** (tau=0.5, order=2) - *Uses SA-Solver to manage stochasticity in smooth latent spaces*
- **Important**: Use external rescaleCFG (0.7) for best results

## Credits

Original reForge extension and algorithms developed for Stable Diffusion WebUI.
Ported to ComfyUI as custom nodes.

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

### License Summary

**Permitted:** Commercial use, Modification, Distribution, Patent use, Private use

**Requirements:** License and copyright notice, State changes, Disclose source, Same license

**Limitations:** No Liability or Warranty

### Why GPL-3.0?

This license ensures compatibility with Stable Diffusion WebUI reForge and its ecosystem, while protecting the open-source nature of the project.

Full license text: https://www.gnu.org/licenses/gpl-3.0.html
