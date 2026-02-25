# Factory Prompt Generator

> **🛡️ Safe for Work | GitHub Compliant | Professional AI Art Generation**

A comprehensive ComfyUI custom node suite for advanced **Safe for Work** prompt generation across all checkpoint types (Pony, SDXL, SD1.5, and more). This SFW edition is specifically designed for professional workflows, educational environments, and GitHub hosting compliance.

## 🎯 Overview

The Factory Prompt Generator SFW Edition provides a tag-based prompt generation system with emphasis controls, multi-character positioning, and comprehensive negative prompt management. Every component has been carefully curated to ensure **family-friendly, professional-grade content** suitable for all audiences.

## ✨ Key Features

- **🔒 100% Safe for Work**: All content thoroughly reviewed for GitHub compliance
- **🎨 Professional Grade**: High-quality prompts for artistic and commercial use
- **🏭 Production Ready**: Built for professional AI image generation workflows
- **📚 Educational Friendly**: Safe for academic and learning environments
- **🌍 Universal Compatibility**: Works with all major checkpoint types
- **⚡ Performance Optimized**: Efficient JSON-based tag system

## 🏗️ Node Architecture

### 📝 Positive Generator: `FactoryPromptsPositive`
**Main SFW prompt generation node with emphasis system and categorical organization.**

#### Core Parameters
- **Quality Level**: `high`, `medium`, `varied` - Professional quality controls
- **Source Style**: `anime`, `cartoon`, `realistic`, `photorealistic`, `furry`, `mixed`
- **Character Count**: `1girl`, `2girls`, `3girls`, `1boy`, `2boys`, etc.
- **Include Artist**: Boolean toggle for artist style inclusion
- **Seed**: Reproducible random generation for consistent results

#### Character Features (SFW)
- **Hair**: Color, length, style (50+ appropriate options each)
- **Eyes**: Color variations (25+ natural options)
- **Skin**: Color diversity (15+ inclusive options)
- **Body**: Tasteful body type categorization
- **Expression**: Positive emotional states and facial expressions

#### Pose System (Family-Friendly)
- **SFW Poses**: Standing, sitting, action poses, casual positions
- **Dynamic Poses**: Athletic movements, artistic positioning
- **Social Poses**: Appropriate group interactions and activities

#### Multi-Character System (Appropriate Interactions)
- **Two Character**: Friendly, casual, social interactions
- **Three Character**: Group dynamics and collaborative positioning
- **Group Character**: Team activities and ensemble scenarios
- **Individual Actions**: Character-specific appropriate actions

#### Clothing System (Tasteful & Diverse)
Comprehensive clothing structure with appropriate options:
- **School Uniform**: Traditional academic wear
- **Casual Wear**: Everyday appropriate clothing
- **Formal Wear**: Professional and elegant business attire
- **Traditional Wear**: Cultural and historical clothing
- **Fantasy Wear**: Appropriate fictional and costume elements
- **Sports Wear**: Athletic and fitness clothing
- **Accessories**: Tasteful items and jewelry

#### Environment & Location
- **Indoor Locations**: Libraries, offices, schools, cafes, homes
- **Outdoor Locations**: Parks, gardens, cityscapes, nature scenes
- **Weather Conditions**: Sunny, rainy, snowy, cloudy atmospheres
- **Time Periods**: Modern, historical, futuristic settings
- **Special Effects**: Professional lighting and atmospheric elements

#### Technical Controls
- **Camera Shots**: Professional photography angles and framing
- **Art Styles**: Various artistic techniques and mediums
- **Lighting**: Professional lighting setups and natural illumination
- **Composition**: Industry-standard composition techniques
- **Color Schemes**: Professional color theory applications

### 🎚️ Emphasis System
**Professional weight control using industry-standard bracket notation.**

#### Emphasis Levels
- `low`: `(tag)` - Subtle emphasis
- `medium`: `tag` - Standard weight (default)
- `high`: `((tag))` - Strong emphasis
- `very_high`: `(((tag)))` - Maximum emphasis

#### Emphasis Categories
- **Character Emphasis**: Physical features and characteristics
- **Pose Emphasis**: Positioning and activities
- **Clothing Emphasis**: Attire and accessories
- **Location Emphasis**: Environmental elements
- **Art Style Emphasis**: Technical and artistic elements

### 🚫 Negative Generators (Content Safety)

#### `FactoryPromptsNegative`
**Professional negative prompt generation with SFW enforcement.**
- **Quality Control**: Prevents low-quality artifacts and issues
- **Safety Filters**: Automatically includes SFW content filters
- **Professional Standards**: Maintains appropriate content boundaries

#### `FactoryPromptsNegativeCategorized`
**Advanced negative control with professional quality standards.**

##### Quality & Technical
- **Base Quality**: Fundamental quality improvements
- **Enhanced Quality**: Professional-grade standards
- **Technical Cleanup**: Artifact and distortion removal

##### Content Safety
- **SFW Enforcement**: Automatic inappropriate content filtering
- **Professional Standards**: Workplace and educational appropriateness
- **Content Boundaries**: Maintains family-friendly generation

## 🔧 Technical Implementation

### JSON-Based Tag System
- **Curated Content**: All tags reviewed for SFW compliance
- **Modular Structure**: Organized categories in `factory_tags.json`
- **Safe Defaults**: Family-friendly fallbacks for all categories
- **GitHub Compliant**: Meets platform content policies

### Content Safety Features
- **Automatic SFW Filtering**: Built-in content appropriateness
- **Professional Standards**: Suitable for workplace environments
- **Educational Safe**: Appropriate for academic settings
- **Platform Compliant**: Meets GitHub and major platform policies

### Performance & Compatibility
- **Universal Checkpoint Support**: Works with all model types
- **ComfyUI Native**: Seamless integration with ComfyUI
- **Memory Efficient**: Optimized for production workflows
- **Error Resilient**: Robust handling with graceful degradation

## 📦 Installation

1. Clone or download to your ComfyUI custom nodes directory:
   ```bash
   git clone [repository-url] ComfyUI/custom_nodes/Factory-Prompts_comfyui/
   ```

2. Restart ComfyUI

3. Look for "Factory Prompts" nodes in the node browser under "Prompt Factory" category

## 🚀 Usage Examples

### Basic Professional Portrait
```
Quality: high
Source: realistic
Character: 1girl
Hair Color: brown
Pose: standing
Expression: confident
Clothing: formal_top (blazer)
Location: office
```

### Educational/Academic Scene
```
Character Count: 2girls
Setting: library
Activity: studying
Pose: sitting
Expression: focused
Clothing: casual_top (sweater)
Lighting: natural
```

### Creative/Artistic Generation
```
Art Style: oil_painting
Character: 1boy
Setting: outdoor (garden)
Pose: contemplative
Lighting: golden_hour
Color Scheme: warm
Art Style Emphasis: high
```

## 📊 Output Format

### Positive Prompt
Generates professionally formatted, comma-separated prompts with proper emphasis brackets applied to maintain appropriate content standards.

### Selection Summary
Detailed breakdown of all selected options with emphasis levels for complete workflow documentation and reproducibility.

## 🛡️ Content Safety & Compliance

### GitHub Platform Compliance
This SFW edition has been specifically designed to meet GitHub's Terms of Service and content policies:

- **✅ No Sexually Explicit Content**: All inappropriate material removed
- **✅ Family-Friendly**: Suitable for all age groups
- **✅ Professional Standards**: Appropriate for workplace environments
- **✅ Educational Safe**: Perfect for academic and learning settings
- **✅ Platform Compliant**: Meets major platform content guidelines

### Content Standards
- **Professional**: Suitable for commercial and business use
- **Educational**: Appropriate for schools and training environments
- **Inclusive**: Respectful representation across all categories
- **Positive**: Focuses on constructive and uplifting content

## 💼 Professional Use Cases

- **Commercial Art**: Product photography, marketing materials
- **Educational Content**: Training materials, academic projects
- **Portfolio Development**: Professional artwork and demonstrations
- **Client Work**: Safe, appropriate content for any client base
- **Public Presentations**: Suitable for any audience or setting

## 🔧 Technical Requirements

- **ComfyUI**: Latest version recommended
- **Python**: 3.8+ 
- **Dependencies**: JSON support (built-in)
- **Storage**: Minimal footprint with efficient tag loading

## 📄 License & Terms

This project is provided for educational, artistic, and commercial use within appropriate professional standards. All content has been curated to maintain family-friendly, workplace-appropriate standards.

## 🤝 Contributing

Contributions that maintain SFW standards and professional quality are welcome. All submissions must align with the project's commitment to appropriate, family-friendly content.

## 📞 Support

For technical issues, feature requests, or content guidelines, please refer to the project documentation or open an issue in the repository.

---

**🏭 Professional. Safe. Powerful.**
*The Factory Prompt Generator SFW Edition - Where creativity meets responsibility.*



