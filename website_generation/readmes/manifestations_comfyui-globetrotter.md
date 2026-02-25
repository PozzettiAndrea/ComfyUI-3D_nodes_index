# ComfyUI Globetrotter Nodes

A comprehensive collection of custom ComfyUI nodes for generating culturally diverse AI image prompts. This project features a fully data-driven architecture with gender-aware attire filtering, comprehensive body part coverage, and intelligent prompt generation optimized for AI image models.

## ✨ Key Features

### 🌍 **Cultural Diversity & Authenticity**
- **Multi-Country Support**: Dynamic nodes for countries with extensive cultural data
- **Regional Variations**: Detailed appearance options for different regions within countries
- **Cultural Context**: Activities, festivals, landmarks, and traditional colors
- **Authentic Attire**: Culturally accurate clothing options with detailed descriptions

### 👕 **Advanced Attire System**
- **Gender-Aware Filtering**: Clothing options automatically filter based on selected gender
- **Comprehensive Body Coverage**: Support for 18+ body parts including:
  - **Arms**: Forearm, Hands, Palms, Upper_Arm, Wrists
  - **Head**: Head, Chin, Ears, Forehead, Hair, Nose
  - **Legs**: Legs, Ankles, Feet
  - **Upper_Body**: Upper_Body, Chest, Shoulders
  - **Waist**: Waist area clothing
- **Rich Descriptions**: Each attire item includes detailed descriptions for AI prompt generation
- **Smart Randomization**: Intelligent random selection with contextual awareness

### 🤖 **AI-Optimized Prompt Generation**
- **Multiple Prompt Styles**: AI-friendly, creative, artistic, technical, and balanced modes
- **Smart Defaults**: Intelligent parameter combinations that work well together
- **Contextual Suggestions**: Weather-activity and emotion-setting pairings
- **Technical Enhancements**: Quality keywords, composition rules, and lighting optimization
- **LLM Integration**: Optional prompt rewriting with local language models

### 🎛️ **Intuitive Controls**
- **Simplified UI**: Clear, logical control grouping with helpful tooltips
- **Universal Options**: Every dropdown includes "none" and "random" options
- **Smart Randomization**: Four levels of randomization (off, light, moderate, full)
- **Reproducible Results**: Seed-based consistency for repeatable outputs
- **Gender-Aware Interface**: Attire options automatically filtered by gender selection

### 📊 **Data-Driven Architecture**
- **Fully Modular**: All data stored in organized JSON files
- **Zero Hardcoding**: No attire, cultural, or prompt data in Python code
- **Easy Extension**: Add new countries, body parts, or attire by updating JSON files
- **Robust Loading**: Error-tolerant JSON loading with graceful fallbacks

## 📁 Project Structure

```
comfyui-globetrotter/
├── data/                          # Organized data files
│   ├── attire/                    # Clothing and accessories by body part
│   │   ├── arms/                  # Forearm, hands, palms, upper_arm, wrists
│   │   ├── head/                  # Head, chin, ears, forehead, hair, nose
│   │   ├── legs/                  # Legs, ankles, feet
│   │   ├── upper_body/            # Upper_body, chest, shoulders
│   │   └── waist/                 # Waist area clothing
│   ├── appearance/                # Regional appearance data
│   ├── poses/                     # Country-specific poses
│   ├── cultural/                  # Cultural activities, festivals, landmarks
│   ├── config/                    # System configuration
│   │   ├── gender_config.json     # Gender mapping and filtering rules
│   │   └── prompt_config.json     # Prompt generation settings
│   ├── generation/                # AI prompt optimization
│   │   ├── smart_defaults.json    # Intelligent default combinations
│   │   ├── contextual_suggestions.json  # Context-aware suggestions
│   │   └── ai_prompt_structure.json     # AI-optimized prompt structure
│   ├── ui/                        # User interface data
│   │   ├── dynamic_node_options.json    # UI dropdown options
│   │   ├── weather_moods.json           # Atmospheric conditions
│   │   └── complementary_colors.json    # Color palette suggestions
│   ├── styles/                    # Artistic and photographic styles
│   └── prompts/                   # LLM prompt templates
├── globetrotter_nodes/            # Core Python modules
│   ├── dynamic_nodes.py           # Main dynamic node generation
│   ├── ollama_llm_node.py         # LLM integration node
│   └── text_combiner_node.py      # Text utility node
└── requirements.txt               # Python dependencies
```

## 🚀 Installation

1. **Clone the repository** into your ComfyUI `custom_nodes` directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone <repository-url> comfyui-globetrotter
   ```

2. **Install dependencies** (optional but recommended for full features):
   ```bash
   cd comfyui-globetrotter
   pip install -r requirements.txt
   ```

3. **Restart ComfyUI** to load the new nodes.

## 💡 Usage

### Dynamic Country Nodes

Each country automatically gets its own node (e.g., "India Attire") with comprehensive options:

#### **Core Parameters**
- **Age**: Young adult, Adult
- **Gender**: Female, Male (with automatic attire filtering)
- **Region**: Country-specific regions (e.g., Java, Punjab, Rajasthan)
- **Hair Style**: Generic options + region-specific defaults
- **Emotion**: Confident, Serene, Joyful, Contemplative, etc.

#### **Attire Selection** (Gender-Filtered)
Individual dropdowns for each body part with culturally appropriate options:
- **Arms**: Forearm decorations, hand accessories, wrist jewelry
- **Head**: Headwear, face decorations, ear accessories
- **Upper Body**: Traditional tops, chest accessories, shoulder pieces
- **Lower Body**: Traditional bottoms, leg wear, foot attire
- **Waist**: Belts, sashes, waist decorations

#### **Cultural Context**
- **Poses**: Traditional and cultural poses
- **Cultural Elements**: Festivals, activities, traditions
- **Settings**: Markets, temples, landmarks, urban areas
- **Atmosphere**: Weather, lighting, mood combinations

#### **Advanced Controls**
- **Detail Level**: Basic, Detailed, Cinematic, Artistic, Photorealistic
- **Composition**: Rule of thirds, Centered, Close-up, Wide shot, etc.
- **Prompt Optimization**: AI-friendly, Creative, Technical, Artistic, Balanced
- **Randomization**: Off, Light, Moderate, Full (with smart contextual choices)
- **Custom Elements**: LoRA triggers, custom prompts
- **Experimental**: AI-powered prompt rewriting (requires transformers library)

### Example Attire JSON Structure

#### `data/attire/upper_body/in.json`
```json
{
  "country": "IN",
  "body_part": "upper_body",
  "attires": [
    {
      "name": "Saree Blouse",
      "type": "clothing",
      "description": "A fitted upper garment worn under a saree, often short-sleeved or sleeveless, and tailored to match the saree.",
      "material": ["cotton", "silk", "synthetic"],
      "region": ["Nationwide"],
      "gender": ["female"],
      "occasion": ["daily wear", "wedding", "festival"]
    },
    {
      "name": "Kurta",
      "type": "clothing",
      "description": "A loose-fitting, long tunic worn by both men and women, often paired with churidar or jeans.",
      "material": ["cotton", "silk", "linen"],
      "region": ["Nationwide"],
      "gender": ["male", "female", "unisex"],
      "occasion": ["daily wear", "casual", "formal"]
    }
  ]
}
```

#### `data/appearance/in.json`
```json
{
  "country": "IN",
  "regions": [
    {
      "name": "Punjab",
      "description": "People from Punjab. Features include wheat-colored to medium brown skin and strong facial structure.",
      "skin_tone": "wheat-colored to medium brown",
      "hair": "black, thick and wavy"
    },
    {
      "name": "South India",
      "description": "People from Tamil Nadu, Kerala, Karnataka, and Andhra Pradesh. Features include dark to very dark skin.",
      "skin_tone": "dark to very dark brown",
      "hair": "black, thick and curly"
    }
  ]
}
```

### Gender-Aware Attire Filtering

The system automatically filters attire options based on the selected gender:

- **Female**: Shows items with `gender: ["female"]` or `gender: ["unisex"]`
- **Male**: Shows items with `gender: ["male"]` or `gender: ["unisex"]`
- **Validation**: Inappropriate combinations are automatically skipped during prompt generation

### Utility Nodes

#### **Text Combiner Node**
- Combines multiple text inputs into a single formatted string
- Useful for complex prompt construction workflows

#### **Ollama LLM Node**
- Advanced prompt enhancement using local Ollama language models
- Includes artistic styles, camera settings, lighting options
- Dynamic loading of style configurations from JSON files

### Smart Prompt Generation

#### **AI-Optimized Output Examples**

**AI-Friendly Mode:**
```
Highly detailed, best quality, rule of thirds composition, A young adult female from Punjab, India, with a confident expression, wearing Saree Blouse: A fitted upper garment worn under a saree, often short-sleeved or sleeveless, and Churidar: Traditional fitted trousers, atmosphere: golden hour
```

**Creative Mode:**
```
Rule of thirds composition, Highly detailed, A young adult female from the Punjab region of India, wearing Saree Blouse: A fitted upper garment worn under a saree and Churidar: Traditional fitted trousers, with a confident expression, color palette: warm earth tones, golden natural colors, atmosphere: golden hour
```

## 🔧 Adding New Content

### Adding a New Country

1. **Create country entry** in `data/countries.json`:
   ```json
   {
     "name": "Country Name",
     "code": "cc",
     "flag": "🇨🇨"
   }
   ```

2. **Add appearance data** in `data/appearance/cc.json`:
   ```json
   {
     "country": "cc",
     "regions": [
       {
         "name": "Region Name",
         "description": "Physical description",
         "skin_tone": "skin tone description",
         "hair": "hair description"
       }
     ]
   }
   ```

3. **Create attire files** in appropriate body part directories:
   - `data/attire/head/cc.json`
   - `data/attire/upper_body/cc.json`
   - `data/attire/legs/cc.json`
   - etc.

4. **Add cultural context** (optional):
   - `data/poses/cc.json`
   - `data/cultural/cc.json`

5. **Restart ComfyUI** to load the new country node.

### Adding New Attire Items

1. **Edit the appropriate JSON file** (e.g., `data/attire/head/in.json`)
2. **Add new attire object**:
   ```json
   {
     "name": "Attire Name",
     "type": "clothing",
     "description": "Detailed description for AI prompts",
     "material": ["cotton", "silk"],
     "region": ["Region1", "Region2"],
     "gender": ["male", "female", "unisex"],
     "occasion": ["daily wear", "formal", "festival"]
   }
   ```
3. **Restart ComfyUI** to load the new options.

### Extending Body Part Coverage

1. **Create new directory** under `data/attire/` (e.g., `accessories/`)
2. **Add country-specific JSON files** with the new `body_part` field
3. **System automatically detects** and includes new body parts in UI

## ⚡ Advanced Features

### Experimental LLM Rewriting
- **Toggle Option**: Each node includes `experimental_llm_rewrite` 
- **Local Models**: Uses Hugging Face `distilgpt2` model when available
- **Smart Filtering**: Automatic repetition detection and removal
- **Length Control**: Output length limits based on prompt optimization mode
- **Graceful Fallback**: Silently skips if dependencies are missing

### Intelligent Randomization
- **Smart Random Mode**: Context-aware random selections
- **Seed Control**: Fixed, increment, decrement, or system random
- **Contextual Pairing**: Weather-activity and emotion-setting combinations
- **Optimal Defaults**: Age-gender combinations that work well together

### Prompt Optimization Modes

| Mode | Purpose | Style |
|------|---------|-------|
| **AI-Friendly** | Stable Diffusion, FLUX | Quality keywords first, clear structure |
| **Creative** | Artistic generation | Narrative flow, artistic language |
| **Technical** | Professional workflows | Precise technical terms |
| **Artistic** | Fine art creation | Museum-quality descriptions |
| **Balanced** | General purpose | Mix of technical and creative |

### Configuration System

#### `data/config/gender_config.json`
```json
{
  "gender_mappings": {
    "male": ["male", "unisex"],
    "female": ["female", "unisex"],
    "non-binary": ["unisex"]
  }
}
```

#### `data/config/prompt_config.json`
```json
{
  "technical_enhancements": {
    "detailed": "8k resolution, highly detailed",
    "cinematic": "professional photography, cinematic lighting"
  },
  "detail_prefixes": {
    "ai_friendly": {
      "detailed": "highly detailed, best quality, "
    }
  }
}
```

## 🛠️ Technical Details

### Dynamic Node Generation
- **Factory Pattern**: Nodes created programmatically for each country
- **Closure-Based**: Input types capture country-specific data
- **Memory Efficient**: Data loaded once and cached
- **Error Tolerant**: Graceful handling of missing files

### Gender Validation System
- **Runtime Filtering**: Attire validated during prompt generation
- **File Discovery**: Automatic detection of correct attire file paths
- **Cross-Reference**: Body part mapping across directory structure
- **Fallback Options**: Safe defaults when validation fails

### Data Loading Architecture
- **Lazy Loading**: JSON files loaded only when needed
- **Caching**: Frequent data cached in memory
- **Error Recovery**: Default values for missing files
- **Validation**: Schema checking for critical fields

## 📋 Requirements

### Core Dependencies
```
torch>=1.9.0              # PyTorch for tensor operations
torchvision>=0.10.0        # Computer vision utilities
transformers>=4.0.0        # Hugging Face transformers (for LLM features)
requests>=2.25.0           # HTTP requests for Ollama API
```

### Optional Dependencies
```
accelerate                 # Faster model loading
safetensors               # Secure tensor serialization
```

**Installation:**
```bash
pip install -r requirements.txt
```

### System Requirements
- **Python**: 3.8 or higher
- **ComfyUI**: Latest version recommended
- **Memory**: 4GB+ RAM for LLM features
- **Storage**: ~50MB for full dataset

## 🤝 Contributing

### Guidelines
1. **Follow JSON Schema**: Maintain consistent data structure
2. **Cultural Sensitivity**: Ensure authentic and respectful representation
3. **Test Additions**: Verify new content works across gender combinations
4. **Documentation**: Update relevant documentation for new features

### Code Style
- **Python**: Follow PEP 8 conventions
- **JSON**: Use 2-space indentation
- **Comments**: Document complex logic and cultural context

### Pull Request Process
1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-country`)
3. Add your changes with appropriate tests
4. Update documentation
5. Submit pull request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Cultural Consultants**: For authentic attire and cultural information
- **ComfyUI Community**: For feedback and feature requests
- **Open Source Libraries**: Transformers, PyTorch, and other dependencies
- **Contributors**: Everyone who has helped expand the cultural database

## 📞 Support

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)
- **Documentation**: This README and inline code comments

---

**Made with ❤️ for the ComfyUI community**
