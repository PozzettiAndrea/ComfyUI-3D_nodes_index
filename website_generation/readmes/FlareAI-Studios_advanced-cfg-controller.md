# Smart CFG Controller - Easy Mode! 🎛️

> **✨ NEW: Easy Mode Available!**  
> Use the **"🎛️ Smart CFG Controller (Easy Mode)"** node for a simple, preset-based experience with tooltips and clear explanations!

A powerful yet user-friendly ComfyUI node for intelligent CFG (Classifier-Free Guidance) control. Choose from easy presets or dive into advanced settings for complete control.

## 🚀 Quick Start Guide

### **Step 1: Choose Your Node**
- **🎛️ Smart CFG Controller (Easy Mode)**: User-friendly with presets and tooltips ⭐ **RECOMMENDED FOR BEGINNERS**
- **⚙️ Advanced CFG Controller (Expert)**: Full manual control for experts

### **Step 2: Pick a Preset** 
Just select from the **Preset** dropdown:

#### **🎨 Style Presets**
- **Vibrant Colors**: Punchy, saturated colors - great for landscapes and portraits
- **Smooth & Clean**: Polished, artifact-free results - perfect for professional work  
- **Sharp Details**: Maximum detail and crispness - ideal for architectural or technical images

#### **⚡ Speed Presets**
- **Speed Mode**: 2x faster generation with good quality
- **Maximum Speed**: 3x faster generation with acceptable quality

#### **✨ Quality Presets**  
- **Quality Boost**: Enhanced colors and contrast with moderate speed
- **Maximum Quality**: Best possible quality (slower generation)

#### **🧪 Experimental**
- **Experimental AI**: Latest AI techniques and enhancements

### **Step 3: Connect and Generate**
1. Connect your model to the node input
2. Connect the node output to your sampler  
3. Generate! The node will automatically optimize everything

## 📖 How to Use Each Feature

### **🎯 Quick Start Section**
- **Preset**: Choose a preset for instant results! Hover over the dropdown to see what each preset does
- **Enable Debug Logging**: Turn this on to see what the node is doing in the console

### **🤖 Adaptive CFG (Auto-Adjustment)**
This automatically adjusts your CFG strength based on what's in your image:
- **Disabled**: No auto-adjustment (use your sampler's CFG as-is)
- **Gentle**: Subtle adjustments - good for most images
- **Standard**: Balanced adjustments - **recommended for most users**
- **Aggressive**: Strong adjustments - for difficult prompts

### **⚡ Speed Optimization** 
Make generation faster by skipping expensive calculations:
- **Skip Negative Prompt**: Turn this ON for 2-3x speed boost
- **Fake Negative Method**: What to use instead of the real negative prompt
  - **Copy Positive (Fast)**: Good balance of speed and quality
  - **Use Zero (Fastest)**: Maximum speed, slight quality loss

### **🎨 Color & Contrast Enhancement**
Automatically enhance your colors:
- **Enable Color/Contrast Rescale**: Turn this ON for more vibrant colors
- **Rescale Target Intensity**: Higher = more vibrant (try 9-10 for punchy colors)

### **🔧 Color Drift Correction**
Prevent color shifts during generation:
- **Fix Color Drift**: Turn this ON if you notice color changes during generation

### **✨ Smooth Blending**
Make results smoother and more polished:
- **Enable Smooth Blending**: Turn this ON for smoother, less noisy results
- **Blending Strength**: Higher = smoother (but may reduce fine details)

### **🚀 Prompt Enhancement**
Boost how your positive prompt is processed:
- **Amplify Extremes**: Makes strong prompt elements even stronger
- **Smooth Values**: Softens prompt processing for gentler results
- **Spectral Normalization**: AI-based enhancement (experimental)

## 🎯 Recommended Settings for Different Use Cases

### **Portraits & People**
- Preset: **"Smooth & Clean"** or **"Vibrant Colors"**
- Enable Color/Contrast Rescale: ✅ ON
- Fix Color Drift: ✅ ON
- Enable Smooth Blending: ✅ ON

### **Landscapes & Nature**  
- Preset: **"Vibrant Colors"** or **"Sharp Details"**
- Enable Color/Contrast Rescale: ✅ ON
- Rescale Target Intensity: 9-10
- Positive Prompt Modifier: "Amplify Extremes"

### **Fast Previews & Testing**
- Preset: **"Speed Mode"** or **"Maximum Speed"**
- Skip Negative Prompt: ✅ ON
- Fake Negative Method: "Use Zero (Fastest)"

### **High Quality Final Images**
- Preset: **"Maximum Quality"**
- Skip Negative Prompt: ❌ OFF (for best quality)
- Enable Color/Contrast Rescale: ✅ ON
- Fix Color Drift: ✅ ON

### **Experimental & Artistic**
- Preset: **"Experimental AI"**
- Adaptive CFG Mode: "Spectral Analysis"
- Positive Prompt Modifier: "Spectral Normalization"
- Enable Performance Monitoring: ✅ ON (to see what's happening)

## 🔍 Understanding the Tooltips

Each setting has detailed tooltips (hover over the parameter name) that explain:
- What the setting does
- When to use it  
- What the different options mean
- Recommended values

**Pro Tip**: Always read the tooltips! They contain helpful explanations and recommendations.

## 🛠️ Available Nodes

### **Main Nodes**
- **🎛️ Smart CFG Controller (Easy Mode)**: User-friendly with presets ⭐ **START HERE**
- **⚙️ Advanced CFG Controller (Expert)**: Full manual control for experts

### **Utility Nodes**
- **🔧 CFG Post-Processing Only**: Just the color/contrast fixes without CFG changes
- **❌ CFG Controller Unpatch**: Remove CFG modifications from a model
- **🚫 Uncond Zero Controller**: Special negative prompt handling

### **Attention Modification Nodes** (Advanced)
- **🎯 Attention Modifier Parameters**: Fine-tune attention layers
- **💪 Attention Modifier Bruteforce**: Aggressive attention modification
- **🔗 Attention Modifier Concat**: Combine multiple attention modifications
- **⏭️ Attention Modifier Single Layer Bypass**: Skip specific attention layers
- **🌡️ Attention Modifier Single Layer Temperature**: Temperature control for attention

## 🚨 Troubleshooting

### **"My colors look washed out"**
✅ **Solution**: Enable **"Enable Color/Contrast Rescale"** and set **"Rescale Target Intensity"** to 9-10

### **"Generation is too slow"**  
✅ **Solution**: Use **"Speed Mode"** preset or enable **"Skip Negative Prompt"** with **"Use Zero (Fastest)"**

### **"Too many artifacts/noise"**
✅ **Solution**: Use **"Smooth & Clean"** preset or enable **"Enable Smooth Blending"**

### **"Colors keep shifting during generation"**
✅ **Solution**: Enable **"Fix Color Drift (Subtract Mean)"**

### **"I want more vibrant colors"**
✅ **Solution**: Use **"Vibrant Colors"** preset or enable **"Enable Color/Contrast Rescale"** with high **"Rescale Target Intensity"**

### **"Node not showing up"**
✅ **Solution**: 
1. Restart ComfyUI completely
2. Check the console for error messages
3. Make sure the node is in the `model_patches` category
4. Look for **"🎛️ Smart CFG Controller (Easy Mode)"**

## 💡 Pro Tips

1. **Start with presets**: Always try a preset first before manual adjustments
2. **Enable debug logging**: Turn on debug logging to see what the node is doing
3. **Read tooltips**: Hover over parameter names for detailed explanations  
4. **Test with simple prompts**: Try the node with basic prompts first
5. **One change at a time**: When customizing, change one setting at a time to see its effect
6. **Save working settings**: When you find settings you like, note them down for future use

## 🔧 Installation

1. Download/clone this repository to your ComfyUI `custom_nodes` folder
2. Restart ComfyUI
3. Look for **"🎛️ Smart CFG Controller (Easy Mode)"** in the `model_patches` category

## 📊 What's Different from Standard CFG?

Standard CFG uses a fixed strength value throughout generation. This node:

1. **Automatically adjusts** CFG strength based on image content
2. **Prevents over-saturation** that can wash out colors
3. **Speeds up generation** by skipping unnecessary calculations  
4. **Enhances colors** and fixes common issues automatically
5. **Provides presets** for different styles and use cases

The result: Better images with less trial and error!
