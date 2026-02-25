# 🧮 CalculatorPro - Node Suite for ComfyUI

![image](https://github.com/user-attachments/assets/cf39b1c5-1440-4541-95d1-c01dd5c96776)

A comprehensive suite of utility nodes for ComfyUI, designed to perform scientific calculations, data type conversions, and complex unit conversions directly within your workflows.

This project was born from a simple idea: to integrate powerful and flexible calculation tools into the core of image generation, enabling unprecedented control and automation.

![image](https://github.com/user-attachments/assets/b4903740-acf8-4000-80e8-49eb28f9a812)


---

## ✨ Features

This suite includes a diverse range of nodes, all organized under the main **`CalculatorPro`** category in ComfyUI.

### Sub-category: `Math`

*   **🧮 Scientific Calculator**: A powerful three-input (`a`, `b`, `c`) tool capable of performing a wide range of operations:
    *   Basic arithmetic (`+`, `-`, `*`, `/`).
    *   Power (`^`), modulo (`mod`).
    *   Trigonometric functions (`sin`, `cos`, `tan`).
    *   Square root, logarithm, absolute value, rounding.
    *   Comparisons (`min`, `max`).

### Sub-category: `Converters`

*   **🔧 Universal Converter**: The Swiss Army knife of data conversion. Provide any input (`FLOAT`, `INT`, `STRING`, or `BOOLEAN`) and get all four types as output.
*   **💱 Manual Rate Converter**: Perfect for currency conversions or any other calculation based on a custom rate. Multiply or divide an amount by an exchange rate.
*   **📏 Length Converter**: Convert between dozens of units, from millimeters to parsecs, including feet, inches, and nautical miles.
*   **⚖️ Mass Converter**: Easily switch from grams to tons, including pounds, ounces, and even stones.
*   **💧 Volume Converter**: Convert liters, cubic meters, gallons, pints, and even kitchen units like tablespoons.
*   **💾 Data Converter**: Clearly distinguish between SI units (megabyte, 10⁶) and binary units (mebibyte, 2²⁰), from bit to petabyte.
*   **⏱️ Time Converter**: Convert seconds to years, including hours, months, and even Planck time.

---

## 🛠️ Installation

### Method 1: Git Clone (Recommended)

1.  Open a terminal or command prompt.
2.  Navigate to the `custom_nodes` folder of your ComfyUI installation.
    ```bash
    cd /path/to/your/ComfyUI/custom_nodes/
    ```
3.  Clone this repository:
    ```bash
    git clone https://github.com/orion4d/Calculator_Pro.git
    ```
    *(Don't forget to replace `https://YOUR_GITHUB_URL_HERE.git` with your repository's actual URL!)*
4.  Restart ComfyUI.

### Method 2: Manual

1.  Click the green `<> Code` button at the top of this page, then `Download ZIP`.
2.  Extract the contents of the ZIP archive.
3.  Place the resulting folder (e.g., `scientific_calculator`) into the `custom_nodes` folder of your ComfyUI installation.
4.  Restart ComfyUI.

---

## 🚀 Usage Examples

The power of these nodes lies in their ability to dynamically drive other parts of your workflow.

### Example 1: Controlling a KSampler Parameter

Use the **Scientific Calculator** to compute a value (e.g., `1 / 3` to get `0.333...`). Connect the `result` (FLOAT) output to the `denoise` input of a `KSampler` for precise control.

### Example 2: Calculating Image Dimensions

Use the **Calculator** to determine a width and height (e.g., `width = 1024`, `height = width * 0.75`). Then, use the **Universal Converter** to convert the `FLOAT` results to `INT` and connect them to the `width` and `height` inputs of an `Empty Latent Image` node.

### Example 3: Converting for Prompts

Use the **Length Converter** to convert `1.80` (meters) to `Pied (ft)`. Connect the `output_str` to a node that assembles prompts to dynamically add "a 5.9-foot tall man" to your text.

## 📄 License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.
<div align="center">

<h3>🌟 <strong>Show Your Support</strong></h3>

<p>If this project helped you, please consider giving it a ⭐ on GitHub!</p>

<p><strong>Made with ❤️ for the ComfyUI community</strong></p>

<p><strong>by Orion4D</strong></p>

<a href="https://ko-fi.com/orion4d">
<img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me A Coffee" height="41" width="174">
</a>
