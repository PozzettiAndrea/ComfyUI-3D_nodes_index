# ComfyUI ASCII Art Nodes

A collection of custom nodes for ComfyUI that enable the creation of various ASCII art effects, from static images to complex, colorized typing animations and video conversions.

## Features

This suite includes the following nodes:

1.  **ASCII Art Generator (Static):** Converts a single image into a static ASCII art image.
2.  **ASCII Typing Animation Generator:** Creates an animation of an image's ASCII art being typed out in a single color.
3.  **Color ASCII Typing Animation:** Similar to the above, but each typed character takes on the color from the corresponding part of the original image.
4.  **Realistic Color ASCII Typing Animation:** Enhances the "Color ASCII Typing Animation" with a flashing cursor for a more realistic typing effect.
5.  **Video to Color Static ASCII Art:** Converts an input video (batched images) into an ASCII art video where the ASCII characters are fixed (based on the first frame), but their colors change according to the video content.
6.  **Video to Dynamic Color ASCII Art:** Converts an input video into an ASCII art video where both the ASCII characters and their colors change frame-by-frame based on the video content.
7.  **Two-Pass Color Typing (Concurrent):** An animation where ASCII characters are typed. As new characters appear in an initial color, previously typed characters concurrently transition to their image-sampled colors.
8.  **Sequential Two-Pass Color Typing:** An animation where the entire ASCII art is first typed out in an initial color, and then a second pass "colors in" the characters with their image-sampled colors.

## Installation

1.  **Download/Clone:**
    * Place the `ComfyUI_ASCIINodes` folder (containing all the `.py` node files and the `__init__.py`) into your `ComfyUI/custom_nodes/` directory.
    * Alternatively, you can use `git clone <repository_url>` into your `custom_nodes` directory if this project is hosted on a Git platform.

2.  **Install Dependencies:**
    * Navigate to the `ComfyUI/custom_nodes/ComfyUI_ASCIINodes/` directory in your terminal or command prompt.
    * Ensure your ComfyUI Python environment is active.
    * Run the following command to install the required Pillow library:
        ```bash
        pip install -r requirements.txt
        ```
        (The `requirements.txt` file should contain `Pillow>=9.0.0`).

3.  **Restart ComfyUI:** After installation, restart your ComfyUI instance for the new nodes to be recognized.

You should find the nodes in the ComfyUI menu, typically under categories like "image/art", "image/animation", or "video/art".

## Nodes Overview & Parameters

Most nodes share a common set of parameters for ASCII generation and appearance. Unique parameters are noted for specific nodes.

### Common Parameters (for most image-to-ASCII nodes):

* `image` (IMAGE): The input image.
* `char_width` (INT): The desired width of the ASCII art in characters. The height is usually calculated proportionally. Higher values mean more detail.
* `font_path` (STRING): Path to a `.ttf` or `.otf` font file (e.g., `cour.ttf`, `/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf`). Monospaced fonts like Courier New, DejaVu Sans Mono, Consolas, etc., are highly recommended for the best ASCII art appearance.
* `font_size` (INT): The size of the font used to render the ASCII characters.
* `ascii_charset` (STRING): A string of characters used to represent different brightness levels, typically ordered from visually sparse/light to dense/dark. You can experiment with different charsets.
* `background_color` (STRING): The background color of the output ASCII image(s) (hex format, e.g., `#000000` for black).
* `invert_brightness_mapping` (BOOLEAN): If `True`, lighter areas of the input image will use characters from the end of the `ascii_charset` (typically denser characters), and darker areas will use characters from the beginning. Default is `False`.

---

### 1. ASCII Art Generator (Static)

* **Display Name:** `ASCII Art Generator (Static)`
* **Category:** `image/art`
* **Functionality:** Converts a single input image into one static ASCII art image. The output image will have the same dimensions as the input image, with the rendered ASCII art scaled to fit.
* **Unique Parameters:**
    * `text_color` (STRING): The uniform color for all ASCII characters (hex format, e.g., `#FFFFFF`).
* **Output:** `ascii_image` (IMAGE)

---

### 2. ASCII Typing Animation Generator

* **Display Name:** `ASCII Typing Animation Generator`
* **Category:** `image/animation`
* **Functionality:** Takes a single image and generates a sequence of frames depicting its ASCII art being typed out character by character.
* **Unique Parameters:**
    * `text_color` (STRING): The uniform color for the typed ASCII characters.
    * `chars_per_frame` (INT): Number of new ASCII characters revealed in each animation frame.
* **Output:** `animated_ascii_frames` (IMAGE batch) - Suitable for video/GIF creation nodes.

---

### 3. Color ASCII Typing Animation

* **Display Name:** `Color ASCII Typing Animation`
* **Category:** `image/animation`
* **Functionality:** Similar to the basic typing animation, but each typed character takes its color from the corresponding area of the original input image.
* **Unique Parameters:**
    * `chars_per_frame` (INT): Number of new characters revealed per frame.
* **Output:** `colored_animated_ascii_frames` (IMAGE batch)

---

### 4. Realistic Color ASCII Typing Animation

* **Display Name:** `Realistic Color ASCII Typing Animation`
* **Category:** `image/animation`
* **Functionality:** Builds upon the "Color ASCII Typing Animation" by adding a flashing cursor at the current typing position.
* **Unique Parameters:**
    * `chars_per_frame` (INT)
    * `cursor_char` (STRING): The character to use for the cursor (e.g., `_`, `|`).
    * `cursor_blink_frames` (INT): Number of animation frames each cursor blink state (on/off) lasts.
    * `cursor_color` (STRING): Color of the flashing cursor.
* **Output:** `realistic_animated_ascii_frames` (IMAGE batch)

---

### 5. Video to Color Static ASCII Art

* **Display Name:** `Video to Color Static ASCII Art`
* **Category:** `video/art`
* **Functionality:** Converts an input video (batched images) to an ASCII art video. The ASCII *characters* are determined from the first frame and remain static throughout. The *color* of these static characters changes frame-by-frame based on the input video.
* **Input:** `video_frames` (IMAGE batch)
* **Output:** `ascii_video_frames` (IMAGE batch)

---

### 6. Video to Dynamic Color ASCII Art

* **Display Name:** `Video to Dynamic Color ASCII Art`
* **Category:** `video/art`
* **Functionality:** Converts an input video to ASCII art where *both* the ASCII characters and their colors are dynamically updated for each frame based on the video's content.
* **Input:** `video_frames` (IMAGE batch)
* **Output:** `dynamic_ascii_video_frames` (IMAGE batch)

---

### 7. Two-Pass Color Typing (Concurrent)

* **Display Name:** `Two-Pass Color Typing (Concurrent)`
* **Category:** `image/animation`
* **Functionality:** Creates an animation from a single image. As new ASCII characters are typed in an `initial_text_color`, previously typed characters concurrently transition to their image-sampled colors. Includes a flashing cursor.
* **Unique Parameters:**
    * `initial_text_color` (STRING): The color for characters when they first appear.
    * `chars_per_frame` (INT): Controls how many "new" characters appear in initial color (and thus, how many previous ones get their final color) per frame.
    * `cursor_char`, `cursor_blink_frames`, `cursor_color`.
* **Output:** `two_pass_animated_frames` (IMAGE batch)

---

### 8. Sequential Two-Pass Color Typing

* **Display Name:** `Sequential Two-Pass Color Typing`
* **Category:** `image/animation`
* **Functionality:** Creates an animation from a single image in two distinct phases:
    1.  The entire ASCII art is typed out using `initial_text_color` with a cursor.
    2.  A pause (configurable).
    3.  The ASCII characters are then "re-typed" or "colored in" with their image-sampled colors, also with a cursor effect.
* **Unique Parameters:**
    * `initial_text_color` (STRING)
    * `chars_per_frame` (INT): Controls speed for both typing passes.
    * `cursor_char`, `cursor_blink_frames`, `cursor_color`.
    * `pause_frames_between_passes` (INT): Number of static frames to pause between the two typing passes.
* **Output:** `sequential_two_pass_frames` (IMAGE batch)

## Usage Tips

* **Fonts:** For the classic ASCII art look, always use a **monospaced font** (e.g., Courier New, Consolas, DejaVu Sans Mono, Monaco). Provide the full path to the font file if it's not in a standard system location.
* **`char_width`:** This parameter significantly impacts the detail of the ASCII art and the processing time for animations. Start with smaller values (e.g., 80-120) and increase as needed.
* **`ascii_charset`:** The choice and order of characters in the charset can dramatically alter the look. Experiment with different sets. The default provided is a good starting point.
* **Animation Output:** The animation nodes output a batch of images. You will need other ComfyUI nodes (e.g., "Video Combine" from extensions like VideoHelperSuite, or "Save Animated WebP/GIF" nodes) to convert this batch into a playable video or animated image file.
* **Performance:** Generating animations with many characters or many frames can be computationally intensive. Adjust `char_width` and `chars_per_frame` to manage performance.

## Troubleshooting

* **Node Not Appearing:** Ensure the custom node folder is correctly placed in `ComfyUI/custom_nodes/` and that ComfyUI has been restarted. Check the ComfyUI console for any error messages during startup related to this custom node package.
* **Font Errors:** If you see errors related to fonts or if the text doesn't render correctly, double-check the `font_path`. Ensure the font file exists at that path and is a valid `.ttf` or `.otf` file that Pillow can read.
* **Missing Dependency:** If you get import errors for `PIL` or `Pillow`, ensure you've run `pip install -r requirements.txt` in the correct Python environment.

Enjoy creating ASCII art with ComfyUI!
