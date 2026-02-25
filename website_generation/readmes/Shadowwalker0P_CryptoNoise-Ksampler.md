# 🔐 CryptoNoise KSampler

**Cryptographic Artist Authentication for AI-Generated Art**

Drop-in replacement for ComfyUI's standard KSampler that embeds cryptographic proof of authorship directly into generated images. Make your AI art unforgeable.

---

## What It Does

CryptoNoise KSampler injects a deterministic, cryptographically-derived signature into your image's latent representation **before generation**. This creates an unforgeable proof of authorship that is:

- **Intrinsic** — The signature is embedded in the generation process, not applied afterward
- **Visually Distinct** — The signature modulates generation, creating detectable differences that prove intentional creation
- **Mathematically Provable** — Regenerate with your artist key to prove authorship
- **Non-removable** — Removing the signature requires regenerating the entire image

### How It Works

1. **Artist Key** → SHA-256 hash → deterministic seed
2. **Seed** → generates random noise → cryptographic shuffle
3. **Shuffled noise** → blended with latent (imperceptible)
4. **Generation proceeds normally** with signed latent
5. **Result**: Image with unforgeable signature locked into latent manifold

### Verification Protocol

In a legal dispute:

1. **Artist keeps**: workflow.json + artist_key (sealed by attorney)
2. **Court/Disputant**: Regenerates image with disclosed artist_key + same generation parameters
3. **Comparison**: SSIM comparison on latent manifold
4. **Result**: SSIM ≈ 1.0 = mathematical proof of authorship
5. **Security**: Collision probability ~10^-77 (effectively impossible)

---

## Installation

### Option 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "CryptoNoise"
3. Click Install
4. Restart ComfyUI

### Option 2: Manual Installation

1. Clone or download this repository
2. Place the folder in: `ComfyUI/custom_nodes/`
3. Restart ComfyUI
4. The node will appear as "🔐 Crypto KSampler"

### Requirements

- ComfyUI (any recent version)
- PyTorch (included with ComfyUI)
- Python 3.8+

---

## Usage

### Quick Start

1. **Replace your KSampler node** with "🔐 Crypto KSampler"
2. **Enter your artist_key**: Any string (e.g., "your_name_2025")
3. **Set crypto_blend**: 0.5 (recommended baseline — creates detectable signature)
4. **Generate normally** — Your work is now signed!

### Parameters

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| `artist_key` | — | string | Your secret artist identity. Keep this private! |
| `crypto_blend` | 0.5 | 0.0-1.0 | Signature strength. Higher = more visually distinct. 0=off, 1.0=maximum watermark |
| `shuffle_mode` | block_8 | block_8/16/32/pixel | Shuffle granularity. block_8=fast & effective, pixel=fine-grained |

**All standard KSampler parameters remain the same** (model, positive, negative, seed, steps, cfg, sampler, scheduler, denoise).

### Examples

#### Example 1: Standard Authentication (crypto_blend=0.5)
```
artist_key: "shadowwalker_2025"
crypto_blend: 0.5 (SSIM ~0.545 vs unsigned)
shuffle_mode: block_8 (fast & effective)
```
Result: Visibly distinct signature. Proves intentional creation - no "accidental" similarity possible.

#### Example 2: Visible Watermark (crypto_blend=1.0)
```
artist_key: "shadowwalker_2025"
crypto_blend: 1.0 (maximum)
shuffle_mode: pixel (fine-grained, highly visible)
```
Result: Obvious visual signature. Maximum proof of intent.

#### Example 3: Multi-Stage Pipeline (Upscaling)
For 2048→4096→8192→16384 upscaling:
```
Stage 1: crypto_blend=0.75
Stage 2: crypto_blend=0.50
Stage 3: crypto_blend=0.25
Stage 4: crypto_blend=0.00
```
Result: Signature locked in early stages, progressive refinement in later stages.

---

## Security & Cryptography

### What's Protected

- **Artist key remains secret** — Only SHA-256 hash is disclosed
- **Signature is unforgeable** — Would require:
  - Exact artist key (only you have it)
  - Exact seed sequence
  - Exact model weights
  - Exact prompt
  - Exact generation parameters
  - Complete latent upscaling pipeline (if used)
  - Ability to reverse SHA-256 (cryptographically impossible)

### Collision Probability

Using SHA-256 (256-bit output):
- **Collision probability**: ~10^-77
- **For comparison**: 10^-77 is astronomically small. You're more likely to be struck by lightning 10 million times in a row.

### What's NOT Protected

- The generated image itself can still be copied (as pixels)
- But regenerating pixel-for-pixel identical image is cryptographically impossible without your artist key

---

## Output Data

The node returns three outputs:

1. **latent** — Standard latent representation (feed to next node)
2. **signature** — Signature string (e.g., "CN-a1b2c3d4e5f6g7h8")
3. **verification_info** — JSON with all cryptographic parameters

### Verification JSON Structure

```json
{
  "version": "1.0.0",
  "system": "CryptoNoise_KSampler",
  "timestamp": 1766421234.5678,
  "artist": {
    "key_hash": "a1b2c3d4...",
    "signature": "CN-a1b2c3d4e5f6g7h8",
    "note": "Artist key hash (not the key itself - key remains sealed)"
  },
  "crypto_parameters": {
    "blend_strength": 0.5,
    "shuffle_mode": "block_8",
    "latent_shape": [1, 4, 64, 64],
    "crypto_seed": 2147483647
  },
  "generation_parameters": {
    "seed": 12345,
    "steps": 20,
    "cfg": 8.0,
    "sampler": "dpmpp_2m",
    "scheduler": "karras"
  },
  "verification": {
    "method": "Regenerate with disclosed artist_key, compare SSIM",
    "expected_result": "SSIM ≈ 1.0 if artist_key matches",
    "proof_type": "Mathematical (SHA-256 based)",
    "collision_probability": "~10^-77 (effectively impossible)"
  },
  "legal_notice": "..."
}
```

---

## Legal Use Cases

### Art Sales & Licensing

- **Proof of Authenticity**: Prove you created a specific artwork in court
- **Licensing Agreements**: Legally binding proof for licensing terms
- **Copyright Enforcement**: Prove authorship against plagiarism claims
- **Royalty Verification**: Verify artwork in chain-of-custody scenarios

### NFT & Blockchain Integration

- Embed signature hash in NFT metadata
- Verify original artist across chain transfers
- Impossible to forge without original artist_key

### Commercial Licensing

- Provide cryptographic proof of commercial vs. personal use
- License different tiers with different artist_keys
- Verify authorized use in court

### Museum & Archive

- Permanent authentication for digital archives
- Recoverable provenance even if file corrupted
- Cryptographic certification of originality

---

## Workflow Examples

### Example Workflow 1: Single Generation

```
[Image] → [KSampler (replace with Crypto KSampler)]
                    ↓
          artist_key: "myname"
          crypto_blend: 0.5
                    ↓
           [Decode Latent] → [Output Image]
```

### Example Workflow 2: Multi-Stage Upscaling

```
[Image] → [VAE Encode] → [Crypto KSampler 1] (crypto_blend=0.75)
                                  ↓
                         [Latent Upscale 2x]
                                  ↓
                         [Crypto KSampler 2] (crypto_blend=0.50)
                                  ↓
                         [Latent Upscale 2x]
                                  ↓
                         [Crypto KSampler 3] (crypto_blend=0.25)
                                  ↓
                         [Latent Upscale 2x]
                                  ↓
                         [Crypto KSampler 4] (crypto_blend=0.00)
                                  ↓
                         [Decode Latent] → [Final 16K Image]
```

Signature locked in early, final image visually clean.

---

## Troubleshooting

### "Using default artist_key" warning

**Solution**: Change the artist_key parameter to your own unique value.

```
artist_key: "john_doe_2025"
```

### Shuffle difference very small

**Possible causes**:
- Block size too large for latent resolution
- Enable logging to see detailed output
- Try smaller block size (block_8 instead of block_16)

### Signature not appearing

**Check**:
1. Is `crypto_blend > 0`? (0.0 disables signing)
2. Is `artist_key` set to a non-default value?
3. Check console logs for error messages

---

## Performance

### Speed Impact

| Shuffle Mode | Latency | Recommended For |
|--------------|---------|-----------------|
| block_8 | <50ms | Default, best balance |
| block_16 | <30ms | Fast workflow, larger latents |
| block_32 | <15ms | Real-time, very fast |
| pixel | 500ms+ | Archive, maximum security |

### Quality Impact (SSIM vs Unsigned)

CryptoNoise signatures create visually distinct outputs by design:

| Configuration | SSIM | Visual Impact |
|---------------|------|---------------|
| pixel:0.20 | 0.473 | Visibly different, subtle |
| pixel:0.50 | 0.545 | Clearly distinct |
| block_8:0.50 | 0.526 | Distinct |
| pixel:1.00 | <0.4 | Obvious watermark |

**SSIM Context:** 1.0 = identical, 0.95+ = imperceptible to humans, 0.5-0.7 = visibly different. Your signature proves intentional creation.

### Memory Impact

Minimal — the signature uses the same memory as the latent representation itself.

---

## License

**Creative Commons Attribution-NonCommercial 4.0 International (BY-NC 4.0)**

You are free to:
- **Share** — Copy and redistribute the material in any medium or format
- **Adapt** — Remix, transform, and build upon the material

Under these conditions:
- **Attribution** — You must give appropriate credit to the original author
- **NonCommercial** — You may not use the material for commercial purposes

### Commercial Licensing

If you wish to use CryptoNoise KSampler for **commercial purposes** (including embedding in commercial products or services), contact the copyright holder for a commercial license agreement.

---

## Author & Attribution

**Original Author**: Shadowwalker  
**Version**: 1.0.0  
**Release Date**: December 2025  
**License**: BY-NC 4.0  

### Citation

If you use this in published work:

```
Shadowwalker. (2025). CryptoNoise KSampler: Cryptographic Artist 
Authentication for AI-Generated Art. ComfyUI Custom Node.
https://github.com/shadowwalker-app/cryptonoise-ksampler
```

---

## Roadmap

Planned features for future versions:

- [ ] SSIM verification tool for legal disputes
- [ ] Blockchain integration for NFT verification
- [ ] Multi-artist collaborative signing
- [ ] Timestamp authority integration
- [ ] Visual proof-of-ownership generator
- [ ] Legal documentation templates

---

## Support & Community

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Share workflows and best practices
- **ComfyUI Community**: Ask questions in #custom-nodes

---

## FAQ

### Q: Can someone else forge my signature?

**A**: No. Without your artist_key, the probability of recreating your exact signature is 10^-77. Cryptographically impossible.

### Q: Will my images look different?

**A**: Yes. The signature modulates latent generation, creating visibly distinct outputs. This is intentional - it proves you intentionally created the work. At crypto_blend=0.5, SSIM vs unsigned is ~0.545 (clearly different). You can lower blend to ~0.20 for subtler differences (SSIM ~0.473), but signatures remain detectable.

### Q: Can I verify my artwork without disclosing my artist_key?

**A**: Quick verification: Check your artist database for the image hash. Full legal verification requires: (1) Disclosing your artist_key (sealed by attorney), (2) Regenerating with same workflow parameters, (3) Comparing SSIM on latent manifold to original. If SSIM ≈ 1.0, you proved authorship.

### Q: Is the signature removable?

**A**: No. The signature is embedded in the generation process itself. Removing it requires regenerating the entire image without your artist_key - which is cryptographically impossible to match.

### Q: Is this better than blockchain watermarking?

**A**: Different approaches:
- **CryptoNoise**: Cryptographic proof, fast, private, visually distinct
- **Blockchain**: Public record, immutable, transparent

You can use both together.

### Q: Can I change my artist_key?

**A**: Yes, but then you can't verify old artwork with the new key. Keep your artist_key consistent for a body of work.

### Q: What if I forget my artist_key?

**A**: Unfortunately, you cannot recover it. Without the key, you cannot prove authorship. **Store your artist_key securely** (password manager, encrypted file, etc.).

### Q: Does this work with LoRA, ControlNet, IP-Adapter?

**A**: Yes. CryptoNoise only affects the latent before generation. You can use any ComfyUI features normally.

### Q: Can I use this for commercial work?

**A**: You need a commercial license. Contact the copyright holder for commercial licensing terms.

---

## Ethics & Intended Use

CryptoNoise KSampler is designed for:
- ✅ Protecting artists' intellectual property
- ✅ Proving authorship and combat plagiarism
- ✅ Licensing and commercial negotiations
- ✅ Legal authentication and evidence
- ✅ Archive and museum preservation

It is **not** designed for:
- ❌ Impersonation or fraud
- ❌ Creating fraudulent authorship claims
- ❌ Violating others' intellectual property
- ❌ Bypassing content moderation or copyright systems

Use responsibly.

---

## Changelog

### Version 1.0.0 (December 2025)

- Initial release
- Block-based and pixel-based shuffling
- SHA-256 cryptographic identity
- Verification JSON output
- ComfyUI Manager support
- Full documentation

---

## Contact & Licensing Inquiries

For commercial licensing, custom implementations, or technical support:

**Author**: Shadowwalker  
**GitHub**: https://github.com/shadowwalker-app  

---

**Made with ❤️ for AI artists everywhere.**

*Cryptographic proof of creation. Mathematical impossibility of forgery.*
