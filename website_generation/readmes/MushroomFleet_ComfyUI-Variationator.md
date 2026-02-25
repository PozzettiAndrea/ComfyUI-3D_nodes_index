# ComfyUI Variationator

**Advanced Multi-Dimensional Prompt Variation System for ComfyUI**

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/MushroomFleet/ComfyUI-Variationator)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Transform your prompts across 12 variation dimensions with 240 pre-defined modifiers and 19 custom ComfyUI nodes.

---

## 🎯 What is Variationator?

Variationator is a comprehensive prompt orchestration system for ComfyUI that enables you to create controlled, diverse variations of your prompts across multiple dimensions:

- 🎨 **240 Pre-defined Modifiers** - Expertly crafted variations across 12 dimensions
- 🔧 **19 Custom Nodes** - From single modifiers to batch generation
- 🚀 **Zero Dependencies** - Works immediately after installation
- 📚 **Fully Documented** - Complete reference for all modifiers and nodes

---

## ✨ Key Features

### 12 Variation Dimensions

Each dimension contains 20 carefully designed modifiers (20 × 12 = 240 total):

| Dimension | Description | Modifiers |
|-----------|-------------|-----------|
| **Lighting** | Time of day, lighting conditions | Sunrise, Golden Hour, Blue Hour, Night (DRY/WET) |
| **Seasonal** | Four seasons with atmospheric variations | Spring bloom, Summer heat, Autumn colors, Winter frost |
| **Location** | Environmental settings | Urban, Rural, Interior, Coastal, Desert, Mountain |
| **Weather** | Atmospheric conditions | Clear, Cloudy, Rain, Snow, Fog, Storm |
| **Mood** | Emotional and atmospheric tone | Energetic, Calm, Mysterious, Luxurious, Epic |
| **Camera** | Photography techniques | Lens types, Angles, Shot types, Depth of field |
| **Color Grading** | Color palettes and tonal adjustments | Warm, Cool, Desaturated, Vibrant, Cinematic |
| **Action** | Dynamic states and contexts | Motion, Scenarios, Interactions, Presentations |
| **Era** | Time periods and historical contexts | 1920s-1990s, Modern, Futuristic, Steampunk |
| **Detail** | Detail levels and focus control | Ultra-detailed, Soft, Minimalist, Photorealistic |
| **Composition** | Framing and compositional techniques | Rule of thirds, Symmetry, Negative space |
| **Distance** | Spatial relationships and proximity | Macro, Portrait distance, Aerial view, Vertical positions |

### 19 ComfyUI Nodes

**Single Modifier Nodes (11)** - One for each dimension
- Apply precise modifiers with ID control (1-20)
- Append or replace mode
- Mix and match across dimensions

**Style Nodes (2)**
- Style Transform - 10+ built-in styles + custom
- Multi-Style Layer - Stack up to 3 styles

**Batch Nodes (2)**
- Batch Variation Generator - Up to 10 variations
- Preset Collection - Optimized sets (commercial, artistic, etc.)

**Utility Nodes (4)**
- Modifier Info - Look up modifier details
- Prompt Combiner - Join text segments
- Random Modifier - Seed-controlled randomization
- Smart Variation (NLP) - Natural language control

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Variationator"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/MushroomFleet/ComfyUI-Variationator.git
```

Restart ComfyUI. All nodes will appear under **"Prompt Orchestration"** category.

---

## 🚀 Quick Start

### Your First Variation

1. Add a text node with your base prompt: `"Sports car on highway"`
2. Add **Lighting Modifier (Single)** node from Prompt Orchestration
3. Set `modifier_id` to `7` (Golden Hour)
4. Connect and run

**Result:** `"Sports car on highway, golden hour, warm low-angle side-light, clear sky"`

### Common Use Cases

**Day/Night Cycle**
```
Use: Batch Variation Generator
Input: "Modern building"
Custom IDs: "1,7,11,18" (Sunrise, Golden Hour, Night, Blue Hour Wet)
Output: 4 time-of-day variations
```

**Style Exploration**
```
Use: Style Transform
Input: "Vintage motorcycle"
Styles: cyberpunk, noir, impressionist
Output: Same subject in different artistic styles
```

**Multi-Dimensional Scene**
```
Stack: Lighting #7 → Location #14 → Mood #13 → Camera #12
Creates: Complex, layered scene with professional look
```

**Random Discovery**
```
Use: Random Modifier
Input: "City street"
Seed: 12345
Output: Reproducible random lighting variation
```

---

## 📖 Documentation

### Comprehensive Guides

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[NODE_REFERENCE.md](NODE_REFERENCE.md)** - Complete guide to all 18 nodes
- **[MODIFIER_REFERENCE.md](MODIFIER_REFERENCE.md)** - All 220 modifiers documented

### Quick References

**Most Popular Modifiers:**
- Lighting #7 - Golden Hour (warm, dramatic)
- Lighting #18 - Blue Hour Wet (moody, reflections)
- Seasonal #12 - Mid Autumn (rich colors)
- Weather #10 - Steady Rain (atmospheric)
- Mood #13 - Luxurious Elegance (premium)

**Preset Collections:**
- `key_moments` - Portfolio-ready dramatic shots
- `commercial` - Professional product photography
- `artistic` - Creative exploration with styles
- `full_day_cycle` - Complete 24-hour progression
- `wet_night` - Dramatic low-light scenes

---

## 🎨 Examples

### Example 1: Product Photography

```
Base: "Luxury watch on pedestal"
Nodes: Preset Collection (preset="commercial")

Outputs:
→ Late morning, high-sun hard light
→ Midday, crisp hard sunlight  
→ Golden hour, warm low-angle
→ Night, clean highlights
```

### Example 2: Artistic Variations

```
Base: "Mountain landscape"
Pipeline: Lighting #7 → Seasonal #12 → Style "cyberpunk"

Output: Mountain landscape with golden hour lighting,
        autumn colors, transformed to cyberpunk aesthetic
        with neon and high-tech elements
```

### Example 3: Batch Testing

```
Base: "Portrait subject"
Batch: All lighting modifiers (category="all")

Outputs 20 variations: Sunrise through Night,
                        perfect for A/B testing
```

### Example 4: Smart Natural Language

```
Base: "Street scene"
Smart Variation: "make it golden hour wet road cyberpunk style"

Output: Automatically applies multiple appropriate modifiers
        based on natural language intent
```

---

## 🔧 Technical Details

### Architecture

```
ComfyUI-Variationator/
├── __init__.py              # Main loader
├── nodes/                   # 18 custom nodes
│   ├── lighting_node.py
│   ├── seasonal_node.py
│   ├── [9 more modifier nodes]
│   ├── style_node.py
│   ├── batch_node.py
│   └── utility_nodes.py
├── modifiers/              # 220 modifier definitions
│   ├── lighting_modifiers.py
│   ├── seasonal_modifiers.py
│   └── [9 more modifier types]
└── core/                   # Orchestration engine
    ├── orchestrator.py
    ├── modifiers.py
    └── singleton.py
```

### Node Categories

All 18 nodes appear in ComfyUI under **"Prompt Orchestration"**:

**Single Modifiers:**
- Lighting Modifier (Single)
- Seasonal Modifier (Single)
- Location Modifier (Single)
- Weather Modifier (Single)
- Mood Modifier (Single)
- Camera Modifier (Single)
- Color Grading (Single)
- Action Modifier (Single)
- Era Modifier (Single)
- Detail Modifier (Single)
- Composition (Single)

**Style & Effects:**
- Style Transform
- Multi-Style Layer

**Batch Generation:**
- Batch Variation Generator
- Preset Collection

**Utilities:**
- Modifier Info
- Prompt Combiner
- Random Modifier
- Smart Variation (NLP)

### Modifier System

**DRY/WET Categorization** (Lighting, Seasonal, Weather):
- **DRY**: Clear conditions, universal use, bright
- **WET**: Low-light, wet surfaces, reflections, dramatic

**Tags System:**
Every modifier has searchable tags for filtering and discovery.

---

## 💡 Tips & Best Practices

### ✅ Do's

- **Start Simple**: Use 1-2 modifiers initially
- **Stack Wisely**: Combine 2-4 modifiers for coherent results
- **Use Presets**: Try preset collections for proven combinations
- **Preserve Base**: Keep `preserve_base=True` in most cases
- **Explore Dimensions**: Try modifiers from different dimensions together

### ❌ Don'ts

- **Over-Modify**: Don't stack 10+ modifiers (prompts become chaotic)
- **Ignore DRY/WET**: These categories create contrast - use both!
- **Skip Documentation**: Check Modifier Info node or references
- **Forget Seeds**: Use Random Modifier seed for reproducible results

---

## 🔬 Advanced Usage

### Combining Dimensions

Create rich, complex scenes by stacking modifiers from different dimensions:

```
Lighting + Seasonal + Weather + Mood + Camera
    =
Professional, atmospheric, technically precise prompts
```

### Custom Workflows

1. **Parallel Variations** - One base, multiple dimension paths
2. **Sequential Refinement** - Progressive enhancement through nodes
3. **A/B Testing** - Batch generator for comparison sets
4. **Random Exploration** - Seed-based discovery workflows

### Node Chaining

All nodes output STRING type, making them fully compatible with:
- Standard ComfyUI text/prompt nodes
- Other custom prompt manipulation nodes
- Save/load text operations
- Any STRING input in your workflow

---

## 📊 Use Case Matrix

| Use Case | Recommended Nodes | Typical Output Count |
|----------|------------------|---------------------|
| Product Photography | Preset Collection ("commercial") | 4-6 variations |
| Artistic Portfolio | Batch + Style Transform | 10+ variations |
| Time-of-Day Study | Batch ("all" or "custom") | 4-20 variations |
| Style Exploration | Multi-Style Layer | 1-3 variations |
| Quick Experimentation | Smart Variation (NLP) | 1 variation |
| Random Discovery | Random Modifier | 1 variation (repeatable) |
| Professional Workflow | Single Modifiers (stacked) | 1 precise variation |

---

## 🐛 Troubleshooting

**Q: Prompts too long?**
- Use `preserve_base=False` on some modifiers
- Apply fewer modifiers
- Focus on essential dimensions only

**Q: Variations look similar?**
- Mix DRY and WET categories
- Combine modifiers from different dimensions
- Add Era or Style transforms for uniqueness

**Q: Can't find right modifier?**
- Use Modifier Info node to browse
- Check MODIFIER_REFERENCE.md
- Try Smart Variation with natural language

**Q: Random node gives same result?**
- Change the seed value
- Verify category selection (all/dry/wet)

**Q: Smart Variation not working?**
- Use specific keywords from modifier descriptions
- Try simpler, more direct language
- Combine multiple recognized terms

---

## 🗺️ Roadmap

### Current Version: 2.0.0

**Implemented:**
- ✅ 11 variation dimensions
- ✅ 220 pre-defined modifiers
- ✅ 18 custom ComfyUI nodes
- ✅ Batch processing capabilities
- ✅ Style transformation system
- ✅ Natural language support
- ✅ Comprehensive documentation

### Future Considerations

- Additional modifier dimensions
- User-defined custom modifiers
- Workflow templates
- Enhanced NLP capabilities
- Community modifier sharing

---

## 🤝 Contributing

We welcome contributions! Areas where you can help:

- **New Modifiers**: Propose additions to any dimension
- **Documentation**: Improve guides and examples
- **Bug Reports**: File issues with details
- **Workflow Examples**: Share your creative workflows
- **Feature Requests**: Suggest new capabilities

Please file issues or pull requests on GitHub.

---

## 📄 License

MIT License - Free for commercial and personal use.

See [LICENSE](LICENSE) file for full details.

---

## 🙏 Support

If you find Variationator helpful:

- ⭐ Star the repository
- 🐛 Report bugs via GitHub Issues
- 💡 Share your workflows and creations
- 📢 Spread the word in the ComfyUI community

**Donations:**

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)

---

## 📚 Citation

### Academic Citation

If you use this in research or projects, please cite:

```bibtex
@software{comfyui_variationator,
  title = {ComfyUI Variationator: Multi-Dimensional Prompt Variation System},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI-Variationator},
  version = {2.0.0}
}
```

---

## 🔗 Links

- **GitHub**: https://github.com/MushroomFleet/ComfyUI-Variationator
- **Documentation**: See QUICKSTART.md, NODE_REFERENCE.md, MODIFIER_REFERENCE.md
- **Issues**: https://github.com/MushroomFleet/ComfyUI-Variationator/issues
- **ComfyUI**: https://github.com/comfyanonymous/ComfyUI

---

## 📈 Version History

### Version 2.0.0 (Current)
- Complete system redesign with 11 dimensions
- 220 modifiers (up from 20)
- 18 nodes (up from 9)
- Added: Seasonal, Location, Weather, Mood, Camera, Color Grading, Action, Era, Detail, Composition dimensions
- Enhanced: Style system with multi-style layering
- Added: Smart Variation (NLP) for natural language
- Added: Random Modifier with seed control
- Comprehensive documentation overhaul

### Version 1.0.0
- Initial release
- 20 lighting modifiers
- 9 basic nodes
- Style transformation system

---

**Ready to transform your prompts? Install Variationator and start creating!**

For detailed guides, see:
- [Quick Start Guide](QUICKSTART.md) - Get started in 5 minutes
- [Node Reference](NODE_REFERENCE.md) - Complete node documentation
- [Modifier Reference](MODIFIER_REFERENCE.md) - All 220 modifiers detailed

---

*Created with ❤️ by Drift Johnson for the ComfyUI community*
