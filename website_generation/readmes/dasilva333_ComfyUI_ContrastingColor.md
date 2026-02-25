# Contrasting Complementary Color Node

This node calculates a **contrasting complementary color** based on an input RGB color. The goal is to **ensure visibility and contrast** when overlaying text, UI elements, or graphical components against a given background color.

---

## 🎯 **Why Is This Useful?**

Choosing a **contrasting** yet **aesthetically complementary** color is a key principle in design, UI/UX, and data visualization. This node provides a simple way to **automatically generate colors** that:
- **Ensure readability** when placing text over a background.
- **Maintain a harmonious color scheme** by shifting hues instead of randomly picking high-contrast colors.
- **Work across light and dark backgrounds** by dynamically adjusting brightness.

### 📌 **Key Use Cases**
#### ✅ **Text & UI Design**
- If you have a **dark background**, this node will generate a **brighter complementary color** to maintain readability.
- If you have a **light background**, it will generate a **darker complementary color** to prevent excessive brightness.

#### ✅ **Data Visualization**
- Use this node to **generate contrasting colors** for charts, graphs, and labels that remain legible across different themes.

#### ✅ **Dynamic Theme Generation**
- Automatically adjust **button colors, text highlights, or UI accents** based on a user-defined background color.

---

## 🎨 **How It Works**
1. **Computes Relative Luminance**  
   - Determines if the input color is "light" or "dark" using an industry-standard luminance formula.

2. **Shifts the Hue by 180° (Complementary Color)**  
   - Converts RGB to HSV and rotates the hue by **180 degrees**.

3. **Adjusts Brightness Dynamically**  
   - If the input color is **dark**, the generated color will be **bright**.  
   - If the input color is **light**, the generated color will be **dark**.

4. **Returns a Hex Color Code**  
   - Output is always formatted as `#RRGGBB`, making it easy to integrate with any system requiring hex-based colors.

---

## 🖌️ **Examples**
### **1️⃣ Ensuring Text Visibility**
- **Background Color:** `#1F2A35` (Dark Blue-Gray)  
- **Generated Complementary Color:** `#FFCB54` (Warm Yellow)  
- ✅ This ensures **high contrast and readability** while maintaining a visually appealing color combination.

### **2️⃣ Dynamic UI Accent Coloring**
- If your UI theme allows users to **pick a background color**, this node can generate **automatically adjusted button and highlight colors**.
- Example:
  - **User selects:** `#E8F0FE` (Soft Blue Background)
  - **Generated Complementary Color:** `#734C00` (Rich Brown for Text or Buttons)

### **3️⃣ Graph & Chart Labels**
- When visualizing data over a color-coded heatmap, use this node to **calculate the best text color for different heatmap regions**.

---

## 🔍 **Node Location**
- **Category:** `utils`
- **Node Name:** `Contrasting Complementary Color`

This node provides an effortless way to maintain **perfect color contrast** dynamically, ensuring **both aesthetic balance and readability** in your designs.