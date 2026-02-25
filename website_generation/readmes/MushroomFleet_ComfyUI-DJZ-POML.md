# Zenkai-POML for ComfyUI

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green)](https://github.com/comfyanonymous/ComfyUI)
[![POML](https://img.shields.io/badge/POML-Expert-blue)](https://microsoft.github.io/poml/latest/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Bring Microsoft's POML (Prompt Orchestration Markup Language) to your ComfyUI workflows! Create structured, reusable, and powerful prompts with visual node-based editing.

## 🚀 Quick Start

### Prerequisites

- **ComfyUI installed and working**
- **Python 3.8+ (same as ComfyUI)**
- **pip package manager**

### Installation

1. **Navigate to ComfyUI custom nodes directory**
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. **Create Zenkai-POML folder**
   ```bash
   mkdir Zenkai-POML
   cd Zenkai-POML
   ```

3. **Download node files**
   - Copy `__init__.py` → save as `__init__.py`
   - Copy `zenkai_poml.py` → save as `zenkai_poml.py`
   - Copy `requirements.txt` → save as `requirements.txt`

4. **Install dependencies** ⚠️ **CRITICAL STEP**
   ```bash
   # Standard installation (optimized requirements)
   pip install -r requirements.txt
   
   # Optional: For development/testing
   pip install -r requirements-dev.txt
   
   # Minimal fallback (limited features)
   pip install poml
   ```

5. **Restart ComfyUI**
   - Close ComfyUI completely
   - Restart the application
   - Check console for "🚀 Zenkai-POML nodes loaded successfully!"

### Dependency Levels

| Level | Installation | Features Available |
|-------|-------------|-------------------|
| **Optimized** | `pip install -r requirements.txt` | All core POML features: official SDK, data processing, PDF/Excel, images, JSON validation |
| **Development** | `pip install -r requirements-dev.txt` | Additional tools for testing, enhanced processing, ML libraries |
| **Minimal** | `pip install poml` | Official POML SDK only (basic functionality) |
| **Fallback** | No dependencies | Basic parsing with limited features |

**✅ Recommended**: Use the optimized requirements.txt for the best balance of features and installation simplicity.

### First Use

1. **Add POML Processor Node**
   - Right-click → Add Node → Zenkai/POML → POML Processor
   
2. **Connect to OpenRouter**
   - POML Processor `rendered_prompt` → OpenRouter `text` input
   
3. **Test with Sample**
   ```xml
   <poml>
   <role>You are an AI assistant specialized in {{ domain }}.</role>
   <task>Help the user understand {{ topic }} in simple terms.</task>
   <output-format>Use clear explanations with examples.</output-format>
   </poml>
   ```

## 🎯 Node Reference

### ZenkaiPOMLProcessor

**Main processing node that converts POML markup to rendered prompts**

**Inputs:**
- `poml_template` (STRING, required): POML markup text
- `render_mode` (COMBO, required): 
  - `standard`: Clean, natural prompt rendering
  - `optimized`: Structured format with clear sections  
  - `debug`: Detailed breakdown with component labels
- `variables_json` (STRING, optional): JSON object with template variables
- `max_length` (INT, optional): Maximum prompt length (0 = no limit)

**Outputs:**
- `rendered_prompt` (STRING): Final prompt text ready for LLM
- `metadata` (STRING): JSON with parsing info and statistics

### ZenkaiPOMLTemplate  

**Template library with pre-built POML patterns**

**Inputs:**
- `template_name` (COMBO): Select from built-in templates
  - Analysis
  - Creative Writing  
  - Technical Documentation
  - Customer Support
  - Data Analysis
- `template_variables` (STRING): JSON with template-specific variables

**Outputs:**
- `poml_template` (STRING): Ready-to-use POML template

## 💡 Usage Examples

### Basic Prompt Enhancement

**Traditional Prompt:**
```
You are a helpful assistant. Explain quantum computing simply.
```

**POML Version:**
```xml
<poml>
<role>You are a physics educator with a gift for simple explanations.</role>
<task>Explain quantum computing to a {{ audience }} audience.</task>
<example>
  <input>What is quantum computing?</input>
  <o>Quantum computing is like having a super-calculator that can try many solutions at once, instead of one at a time like regular computers.</o>
</example>
<output-format>Use analogies and avoid jargon. Keep under {{ max_words }} words.</output-format>
</poml>
```

**Variables JSON:**
```json
{
  "audience": "high school student", 
  "max_words": 150
}
```

### Data Analysis Workflow

```xml
<poml>
<role>You are a business intelligence analyst.</role>
<task>Analyze the sales performance data and identify trends.</task>
<table title="Q4 Sales Data">
Region | Q1 | Q2 | Q3 | Q4
North  | 150k | 180k | 165k | 210k  
South  | 220k | 195k | 235k | 260k
East   | 180k | 175k | 190k | 185k
West   | 250k | 280k | 275k | 295k
</table>
<output-format style="format: executive-summary">
Provide: Key Insights, Performance Trends, Regional Analysis, Recommendations.
</output-format>
</poml>
```

### Creative Writing with Templates

1. **Use ZenkaiPOMLTemplate node**
2. **Select "Creative Writing"**  
3. **Set variables:**
   ```json
   {
     "genre": "science fiction",
     "content_type": "short story opening",
     "theme": "AI consciousness",
     "tone": "mysterious",
     "length": "200 words",
     "style": "literary",
     "audience": "adult readers"
   }
   ```

## 🔄 Workflow Patterns

### Pattern 1: Enhanced Single Prompt

```
Text Input → POML Processor → OpenRouter → Output
```

**Use Case:** Transform plain prompts into structured, optimized versions

### Pattern 2: Template-Based Generation

```
POML Template → POML Processor → OpenRouter → Multiple Outputs
```

**Use Case:** Consistent prompt formatting across different scenarios

### Pattern 3: Multi-Variant Testing

```
Same Context → Multiple POML Templates → Batch Processing → Compare Results
```

**Use Case:** A/B test different prompt structures and styles

### Pattern 4: Dynamic Content Integration  

```
File Input → POML Processor (with data) → OpenRouter → Analysis
```

**Use Case:** Incorporate external documents or data into prompts

### Pattern 5: Conversational Workflows

```
POML Template → Context Injection → Multi-Turn Chain → Refined Outputs
```

**Use Case:** Build sophisticated conversation flows with consistent prompting

## 🎨 Advanced Features

### Variable Templating

**Dynamic Role Assignment:**
```xml
<role>You are a {{ profession }} with {{ years }} years of experience in {{ specialty }}.</role>
```

**Conditional Content:**
```xml
<task>
{{ base_task }}
{{ expertise_level == 'expert' ? 'Include technical details and citations.' : 'Keep explanations simple.' }}
</task>
```

### Multi-Modal Integration

```xml
<poml>
<role>You are a visual content analyst.</role>
<task>Analyze the provided image and data together.</task>
<img src="chart.png" alt="Sales performance bar chart showing quarterly trends" />
<table title="Raw Data">
  <!-- table content -->
</table>
<output-format>Correlate visual and numerical insights.</output-format>
</poml>
```

### Template Libraries

**Create reusable patterns:**
```xml
<!-- Base Analysis Template -->
<poml>
<role>You are a {{ domain }} analyst.</role>
<task>Analyze {{ subject }} focusing on {{ aspects }}.</task>
<output-format style="format: {{ report_type }}; verbosity: {{ detail_level }}">
Present findings with actionable insights.
</output-format>
</poml>
```

## 🔧 Troubleshooting

### Installation Issues

**Problem: Nodes Don't Appear After Installation**

1. **Check console output when starting ComfyUI:**
   ```bash
   python main.py
   # Look for Zenkai-POML loading messages or errors
   ```

2. **Verify file structure:**
   ```
   ComfyUI/custom_nodes/Zenkai-POML/
   ├── __init__.py          ✅ Required
   ├── zenkai_poml.py       ✅ Required  
   ├── requirements.txt     ✅ Required
   └── README.md           📝 Optional
   ```

3. **Check dependencies installation:**
   ```bash
   cd ComfyUI/custom_nodes/Zenkai-POML
   pip install -r requirements.txt
   ```

**Problem: Import/Dependency Errors**

| Error Message | Solution |
|--------------|----------|
| `ModuleNotFoundError: No module named 'poml'` | `pip install poml` |
| `ModuleNotFoundError: No module named 'pandas'` | `pip install pandas` |  
| `ModuleNotFoundError: No module named 'PyPDF2'` | `pip install PyPDF2` |
| `ModuleNotFoundError: No module named 'PIL'` | `pip install Pillow` |
| `ModuleNotFoundError: No module named 'requests'` | `pip install requests` |

**Problem: POML Features Not Working**

The node provides graceful degradation. Check the `metadata` output to see which features are available:

```json
{
  "dependencies_status": {
    "poml": true,           // Official POML SDK
    "pandas": false,        // Advanced table processing  
    "pypdf2": true,         // PDF document support
    "pillow": false,        // Image processing
    "requests": true,       // External data fetching
    "jsonschema": false     // JSON validation
  },
  "features_available": {
    "official_poml_sdk": true,
    "advanced_tables": false,
    "pdf_processing": true,
    "image_processing": false,
    "external_data": true,
    "json_validation": false
  }
}
```

### POML Syntax Issues

**Problem: Parsing Errors**

1. **Check XML syntax:**
   - All tags must be properly closed: `<role>...</role>`
   - Use self-closing for empty tags: `<img src="file.png" />`
   - Escape special characters: `&lt;` `&gt;` `&amp;`

2. **Test with minimal example:**
   ```xml
   <poml>
   <role>Assistant</role>
   <task>Help user</task>  
   </poml>
   ```

3. **Use debug mode:**
   - Set render_mode to "debug"
   - Check metadata for parsing details

**Problem: Variables Not Working**

1. **Check JSON syntax:**
   ```json
   {
     "user_name": "Alice",
     "topic": "AI",
     "max_words": 150
   }
   ```

2. **Verify variable names match template:**
   ```xml
   <role>You are helping {{ user_name }} learn about {{ topic }}.</role>
   ```

3. **Check metadata for variable status:**
   ```json
   "variables_used": ["user_name", "topic", "max_words"]
   ```

### Performance Issues

**Problem: Slow Processing**

1. **Optimize templates:**
   - Reduce nested loops and conditionals
   - Use simpler variable substitutions
   - Limit data file sizes

2. **Check dependency status:**
   - Official POML SDK is faster than fallback parser
   - pandas processing is more efficient for large tables
   - Consider file size limits for documents/tables

**Problem: Memory Usage**

1. **Limit data size:**
   - Use `max_length` parameter to truncate output
   - Process large files externally before POML
   - Split large tables into smaller chunks

### Common Solutions

| Problem | Quick Fix |
|---------|-----------|
| Empty output | Ensure POML has `<role>` and `<task>` |
| Variables not substituting | Check JSON syntax and variable names |
| Table not loading | Verify file path and install pandas |
| PDF not processing | Install PyPDF2: `pip install PyPDF2` |
| Performance slow | Use "optimized" render mode |
| Features missing | Check metadata dependencies_status |

### Dependency Verification Script

Create `test_dependencies.py` to check your installation:

```python
def check_dependencies():
    deps = {}
    
    try:
        import poml
        deps['poml'] = '✅ Available'
    except ImportError:
        deps['poml'] = '❌ Missing - pip install poml'
    
    try:
        import pandas
        deps['pandas'] = '✅ Available'  
    except ImportError:
        deps['pandas'] = '❌ Missing - pip install pandas'
        
    try:
        import PyPDF2
        deps['PyPDF2'] = '✅ Available'
    except ImportError:
        deps['PyPDF2'] = '❌ Missing - pip install PyPDF2'
        
    try:
        from PIL import Image
        deps['Pillow'] = '✅ Available'
    except ImportError:
        deps['Pillow'] = '❌ Missing - pip install Pillow'
    
    for name, status in deps.items():
        print(f"{name}: {status}")

if __name__ == "__main__":
    check_dependencies()
```

Run with: `python test_dependencies.py`

## 🚀 Performance Tips

### Optimization Strategies

1. **Template Reuse**: Create base templates and modify with variables
2. **Render Mode Selection**: Use "optimized" for structured LLM input
3. **Length Limits**: Set max_length for token budget control
4. **Variable Preprocessing**: Prepare complex data outside the node

### ComfyUI Integration

1. **Caching**: ComfyUI caches node outputs - leverage for repeated prompts
2. **Batching**: Process multiple variations efficiently
3. **Workflow Optimization**: Group POML processing early in pipeline
4. **Memory Management**: Use length limits for large templates

## 📊 Comparison: Before vs After

| Aspect | Plain Text Prompts | POML Enhanced |
|--------|-------------------|---------------|
| **Structure** | Unorganized text blob | Semantic components |
| **Reusability** | Copy-paste with manual edits | Template + variables |
| **Consistency** | Varies with manual writing | Standardized format |
| **Data Integration** | Manual text insertion | Native data components |
| **Maintainability** | Difficult to update | Modular components |
| **Testing** | Hard to A/B test variations | Easy template swapping |
| **Collaboration** | Unclear prompt structure | Self-documenting markup |

## 🤝 Contributing

Found a bug or want to add features?

1. **Report Issues**: Describe the problem with example POML
2. **Feature Requests**: Explain the use case and expected behavior  
3. **Code Contributions**: Fork, implement, test, and submit PR
4. **Template Sharing**: Contribute useful POML templates

## 📚 Resources

### Learn POML
- [Official POML Documentation](https://microsoft.github.io/poml/latest/)
- [POML Research Paper](https://arxiv.org/abs/2508.13948) 
- [GitHub Repository](https://github.com/microsoft/poml)

### ComfyUI Resources
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [Custom Node Development](https://docs.comfy.org/essentials/custom_node_overview)
- [Workflow Sharing](https://comfyworkflows.com/)

### Community
- [POML Discord](https://discord.gg/poml)
- [ComfyUI Reddit](https://reddit.com/r/comfyui)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

**Ready to revolutionize your ComfyUI prompt workflows? Install Zenkai-POML and experience the power of structured prompt engineering!** 🚀
