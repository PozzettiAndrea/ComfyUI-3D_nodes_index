# CreateMarkdownImage ComfyUI node

This project generates an image from Markdown text using `imgkit` and `wkhtmltoimage`. It automatically scales the text to fit within the specified image dimensions.

## 🔧 Installation

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Install `wkhtmltoimage`
This project requires `wkhtmltoimage`, which is part of `wkhtmltopdf`. You need to install it manually.

🔗 **Download `wkhtmltopdf` from:**  
👉 [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

**Make sure to add `wkhtmltoimage.exe` to your system PATH, or update the script with its full path.**

---

## 📌 How It Works
This script:
1. Converts Markdown text into HTML.
2. Renders the HTML into an image using `imgkit`.
3. Dynamically adjusts the font size to maximize readability.
4. Returns the image as a PyTorch tensor.

---

## 📊 Input Fields

| Field             | Type   | Description |
|------------------|--------|-------------|
| `md_text`        | String | Markdown text to be rendered into an image. Supports basic formatting (bold, italic, emojis). |
| `border_color`   | String | HEX color or HTML named color for the image border (e.g., `#FFFF00` for yellow). |
| `border_size`    | Int    | Border thickness in pixels. |
| `image_width`    | Int    | Width of the generated image in pixels. |
| `image_height`   | Int    | Height of the generated image in pixels. |
| `background_color` | String | HEX color or html color name (e.g., `"lightblue"`). |

---

## 🚀 Usage
```python
from create_markdown_image import CreateMarkdownImage

generator = CreateMarkdownImage()
image_tensor = generator.createmarkdownimage(
    md_text="**Hello World!** 🚀",
    border_color="#000000",
    border_size=2,
    image_width=800,
    image_height=200,
    background_color="white"
)
```
This will generate an image containing "Hello World! 🚀" with a **black border** and a **white background**.

---

## 🛠️ Troubleshooting
- If `imgkit` fails, ensure `wkhtmltoimage.exe` is installed and accessible.
- If text doesn't scale correctly, adjust the `image_width` and `image_height` fields.

---

## 📜 License
This project is licensed under the MIT License.