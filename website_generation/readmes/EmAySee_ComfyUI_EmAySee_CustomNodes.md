# **EmAySee Custom Nodes for ComfyUI**

A specialized collection of ComfyUI custom nodes designed to solve specific workflow bottlenecks, improve organization, and bridge the gap between AI generation and logic-based automation.

## **🖼️ Image & Vision Processing**

### **EmAySee Repaint KSampler**

A specialized KSampler designed for inpainting and repainting tasks. It intelligently handles image masks by inverting them (mapping white to "keep" and black to "change") and combining original latents with initial noise to provide a more stable starting point for the sampling process.

### **Save Image (EmAySee)**

An advanced image saving node with deep customization. It allows for complex filename construction using prefixes, postfixes, and timestamps (YYYYMMDDHHMMSS). It also ensures that EXTRA\_PNGINFO and metadata are correctly preserved in the final output.

### **EmAySee Qwen Pixel Aligner**

Designed specifically for VLM (Vision Language Model) workflows like Qwen-VL. It intelligently resizes images to a target longest edge (784px–2240px) while snapping the final dimensions to a 112px grid. This ensures maximum compatibility and performance without distorting aspect ratios.

### **EmAySee Gemini Image Gen**

A powerful integration node that brings Google's **Gemini 2.0 Flash** and **Imagen 3** models directly into your workflow. It handles prompt execution and batch generation, allowing you to use high-end cloud-based generation alongside local models.

### **EmAySee Conditional Resize**

A logic-gated upscaler. It only triggers a resize if the input image's longest side is smaller than your defined threshold, preventing redundant upscaling and saving processing time.

### **EmAySee Pad Image For Outpainting**

Adds padding to the Left, Top, Right, or Bottom of an image and generates a corresponding mask for the padded areas. Perfect for outpainting workflows that require specific canvas expansion.

### **EmAySee Aspect Ratio Calculator**

Eliminates guesswork when resizing. Provide an image and a target height, and the node outputs the precise width required to maintain the original aspect ratio perfectly.

### **EmAySee Image Get Size**

A simple utility that extracts and outputs the Width and Height of an input image as integers.

### **EmAySee Dimension Swapper**

A streamlined utility for switching between Portrait and Landscape orientations. It allows you to swap Width and Height values with a single toggle.

### **EmAySee Image Preview & Passthrough**

* **Image Preview Passthrough:** Displays a high-speed temp preview of the image at any point in your workflow without stopping the execution chain.  
* **Image Passthrough:** A standard utility to route image data while allowing you to rename labels for cleaner organization.

## **🎭 Masking & Detailer Tools**

### **Multi Mask to BBOX**

Extracts a combined bounding box (X, Y, Width, Height) from up to 10 different mask inputs. It finds the outer bounds of all visible areas, allowing you to crop or detail multiple masked regions simultaneously.

### **EmAySee Box to Mask**

Converts bounding box coordinates (X, Y, Width, Height) directly into a mask. It can derive dimensions from a reference image, providing a surgically precise way to target regions for Adetailer or Inpainting.

### **EmAySee Mask Combiner**

A robust merging tool that takes up to 20 mask inputs and combines them into one using a logical "Max" operation. It handles mismatched mask sizes by scaling them to the largest input.

## **🧮 Math & Logic**

### **EmAySee Math Expression**

Evaluates a mathematical string expression (e.g., max(w, h) \* 1.5) using input variables. Supports common functions like abs, round, pow, and math constants.

### **EmAySee Multiplier Node**

Features a float slider (1.0 \- 2.0) and two integer fields. It outputs the two integers multiplied by the slider value, useful for scaling dimensions proportionally.

### **EmAySee Toggle to Integer**

A simple logic gate that converts a boolean toggle into one of two user-defined integers (e.g., Output 50 if ON, 0 if OFF).

### **EmAySee Greater Than (Float)**

Compares two floats and outputs an Integer 1 (True) or 0 (False).

### **EmAySee Checkbox to Float**

Converts a UI checkbox (Boolean) into a float (1.0 or 0.0).

### **EmAySee Dynamic Range Slider**

Calculates a precise float between a Min and Max value based on a percentage (0.0 to 1.0) with an optional quantization step.

## **🎲 Randomization & Selection**

### **EmAySee Random LoRA Loader**

Connect up to 10 LoRAs with individual activation toggles. The node randomly selects and loads one of the active LoRAs into your model/clip chain based on a seed.

### **EmAySee Random String Selector Suite**

* **Random String Selector (2-4 Choice):** Picks a random string from a small set of inputs.  
* **Random String Selector (Max-20):** High-capacity selection for complex variations.  
* **Probability String Selector:** Picks between two strings based on a weighted probability (0.0 to 1.0).

### **EmAySee Random Integer from List (Vroom Edition)**

Selects a random integer from a string list or range (e.g., 1, 2, 4-6, 50). Supports seeding and includes a "Use System Time" toggle for per-run randomization.

### **EmAySee Random Integer from Toggles**

Features 20 slots with premade labels. It randomly selects the index of any active toggle, letting you build visual "feature menus" in your UI.

### **EmAySee String Selectors (Manual)**

* **Integer String Selector (Max-20):** Use a slider to manually switch between different prompt inputs.  
* **REALLY Unique String Selector:** A dropdown menu interface for routing text between two inputs.  
* **Pose Option Selector:** A 5-slot slider interface designed for switching between pose or style descriptions.

## **✍️ Text & LLM Utilities**

### **EmAySee Submit to Oobabooga API (Advanced)**

Interfaces with local Oobabooga text-generation-webui instances.

* **Thinking Parser Variants:** Specifically designed for reasoning models (DeepSeek). It splits the \<think\> tags and internal chain-of-thought from the final clean text, outputting both separately.  
* **API Key Support:** Includes variants with Authorization headers for secured instances.

### **EmAySee Var Text Replacer**

A robust template engine. It takes a block of text and replaces up to 10 dynamic placeholders (%var1% to %var10%) with the strings provided to its input ports.

### **EmAySee Tag Pruner**

A cleaning utility that takes a prompt and a secondary list of "bad tags." It filters the prompt, removing any matches from the removal list while cleaning up extra commas and whitespace.

### **EmAySee LLM Output Cleaner**

A post-processing node that strips out \<think\> blocks and extra whitespace from chatty model responses.

### **EmAySee Text Combiner**

A high-capacity input node that accepts up to 50 separate text strings and joins them into a single list with line returns.

### **EmAySee Remove Duplicates (V2)**

Deduplicates comma-separated strings (tags/keywords). Includes a toggle to either preserve the original order or sort results alphabetically.

### **EmAySee String Tuple Input**

Converts multiline text into a Python string tuple, required for certain advanced node inputs.

### **EmAySee Float To Text**

Converts numerical float data into a formatted string template (prefix:value:suffix).

### **EmAySee Metadata Formatter**

Parses LoRA metadata JSON strings into a clean, human-readable format, stripping ss\_ prefixes for easier review.

## **🌐 System & File Utilities**

### **EmAySee Two-Step LoRA Loader**

Decouples LoRA selection from the application process.

* **LoRA Name Selector:** A dropdown that outputs the selected LoRA name as a string.  
* **LoRA Applier:** Accepts a string input for the name, allowing you to route names through logic nodes before finally loading them.

### **EmAySee Lora File Picker**

Scans your LORA directories and provides a searchable dropdown. Outputs both the simple filename and the absolute full system path.

### **EmAySee Save Text to File**

Saves any string input to a .txt file in the ComfyUI output directory. Supports subfolders and automatic filename sanitization.

### **EmAySee Host Pinger**

Pings a hostname or IP address. Outputs 1 if reachable and 0 if down, allowing your workflow to adapt to server availability.

### **EmAySee Get Model Path**

Extracts the raw file system path from a ComfyUI Model object.

### **EmAySee Date Time Filename String**

Generates a unique timestamp string (YYYYMMDDHHMMSS) down to the tenth of a second for unique identifiers.

## **🚀 Installation**

1. Navigate to your ComfyUI custom\_nodes directory.  
2. Clone this repository:  
   git clone \[https://github.com/YourUsername/EmAySee\_Nodes.git\](https://github.com/YourUsername/EmAySee\_Nodes.git)

3. Install dependencies:  
   pip install requests google-genai

4. Restart ComfyUI.

## **💻 Requirements**

* torch  
* Pillow  
* requests (For Oobabooga nodes)  
* google-genai (For Gemini nodes)