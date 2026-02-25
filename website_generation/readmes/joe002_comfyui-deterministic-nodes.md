# ComfyUI Deterministic Nodes

Batch-invariant inference nodes for **guaranteed reproducibility** in ComfyUI.

## The Problem

**temperature=0 is NOT enough for determinism.**

The real culprit is **batch-size variance**. Same prompt, same seed, different batch sizes = different outputs.

## The Solution

These nodes enforce **batch_size=1** processing with fixed RNG states, guaranteeing:

```
Same seed + Same prompt = Identical output (ALWAYS)
```

Based on [ThinkingMachines batch-invariant-ops research](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/).

## Nodes (all in `JI/Reproducible` category)

| Display Name | What It Does |
|--------------|--------------|
| **Locked Sampler** ⟳ | Same seed = same output, every time |
| **Output Matcher** | Verify your outputs match exactly |
| **Expert Selector** | Pick the right AI model for your task |
| **Multi-Pass Refiner** | Refine in 3 stages (coarse → detail) |
| **Memory Recall** | Retrieve context from 4-tier memory |

### Locked Sampler ⟳
Guarantees identical outputs with the same seed:
- Forces `batch_size=1` internally (the secret sauce)
- Resets RNG for each item
- Disables GPU auto-tuning variance
- Outputs proof checksum

### Output Matcher
Verify reproducibility with configurable tolerance:
- `exact`: Byte-for-byte match
- `epsilon_1e-6`: Allow tiny floating-point variance
- `epsilon_1e-4`: Allow small floating-point variance
- `structural`: Shape and dtype match only

### Expert Selector
Pick the right AI model automatically:
- Hash-based selection (consistent every time)
- Supports up to 4 expert models
- Same input = same expert (ALWAYS)

### Multi-Pass Refiner
Refine in stages (like render passes):
- Stage 1: Coarse pass
- Stage 2: Refinement
- Stage 3: Detail
- Different seed per stage for diversity within determinism

### Memory Recall
Retrieve context from 4-tier memory:
- Hot: GPU VRAM (active)
- Warm: System RAM (recent)
- Cold: NVMe (historical)
- Archive: Network (full)

## Installation

Copy to ComfyUI custom_nodes:
```
ComfyUI/custom_nodes/ComfyUI-DeterministicNodes/
```

Restart ComfyUI.

## Usage

### Reproducibility Workflow

```
[Model] --> [Locked Sampler] --> [Output Matcher] --> [Output]
                   |                      |
                   +-- seed=42 ----------+
                   |                      |
                   +-- checksum ---------+-- verify on next run
```

### Multi-Model Workflow

```
[Prompt] --> [Expert Selector] --> [Selected Model] --> [Locked Sampler]
                  |
                  +-- expert_0: General
                  +-- expert_1: Code
                  +-- expert_2: Domain
                  +-- expert_3: Math
```

### Context-Aware Workflow

```
[Query] --> [Memory Recall] --> [Prompt with Context] --> [Model]
                  |
                  +-- hot_only: Fast, GPU cache
                  +-- hot_warm: Recent context
                  +-- all_tiers: Full history
```

## Technical Details

### Why Batch-Invariance Matters

```
Batch=1:  "The answer is 42"
Batch=4:  "The answer is 41"  <-- DIFFERENT!
Batch=8:  "The answer is 43"  <-- DIFFERENT!
```

GPU parallel operations have floating-point accumulation order variance.
Different batch sizes = different accumulation order = different results.

### The Fix

1. Process items one at a time (`batch_size=1`)
2. Reset RNG before each item (`seed + item_index`)
3. Disable cuDNN auto-tuning (`cudnn.benchmark=False`)
4. Use deterministic algorithms (`torch.use_deterministic_algorithms(True)`)

## Framework Integration

These nodes integrate with:
- **ECHO 2.0**: 4-tier context memory → Memory Recall
- **CSQMF-R1**: Expert routing → Expert Selector
- **Nemotron**: Cascade refinement → Multi-Pass Refiner
- **ThinkingMachines**: Batch-invariant inference → Locked Sampler

## License

**Dual-licensed under AGPL-3.0 and Commercial licenses.**

| Use Case | License | Requirements |
|----------|---------|--------------|
| Open source projects | AGPL-3.0 | Release derivatives under AGPL-3.0 |
| Personal/educational | AGPL-3.0 | Attribution required |
| SaaS/proprietary | Commercial | [Contact for license](mailto:joseph@josephibrahim.com) |

See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) for commercial terms.

**Why dual-license?** Batch-invariant inference and deterministic routing are novel contributions. AGPL ensures community improvements flow back while commercial licensing enables proprietary use.

## Author

Joseph Ibrahim - VFX Lighting TD
- Portfolio: [josephibrahim.com](https://josephibrahim.com)
- Commercial inquiries: joseph@josephibrahim.com

---

*Determinism is not optional. It's a requirement.*
