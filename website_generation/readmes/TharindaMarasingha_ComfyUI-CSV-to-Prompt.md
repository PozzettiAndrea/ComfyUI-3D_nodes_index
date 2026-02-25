# ComfyUI CSV to Prompt Node
### Created by Tharinda Marasingha

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Node-green.svg)

A lightweight and efficient custom node for **ComfyUI** that allows you to load prompts directly from CSV files. It is specifically designed for **Bulk/Batch Image Generation**, allowing you to automate the creation of hundreds of images using a pre-defined list of prompts.

<img width="600" height="600" alt="Red and White Video Centric Coming Soon Instagram Post" src="https://github.com/user-attachments/assets/bb2e0d73-f6e6-46be-8fab-6962a39edefb" />


## ✨ Features

* **📂 Auto-Scan:** Automatically detects CSV files placed in the `csv_files` directory.
* **🔄 Bulk Mode:** Uses the generic `Seed` number to iterate through your CSV rows automatically.
* **⚡ Lightweight:** No heavy dependencies (pandas not required—uses standard Python).
* **🛡️ Robust:** Handles missing columns and empty files gracefully.

---

## 📥 Installation

### Method 1: ComfyUI Manager (Recommended)
1.  Open **ComfyUI Manager**.
2.  Select **"Install via Git URL"**.
3.  Paste the link to this GitHub repository.
4.  Restart ComfyUI.

### Method 2: Manual Installation
Navigate to your ComfyUI `custom_nodes` folder and run the following command:

```bash
cd ComfyUI/custom_nodes/
git clone (https://github.com/TharindaMarasingha/ComfyUI-CSV-to-Prompt.git) 
```

🛠️ Setup & Folder Structure
For the node to work, you must place your .csv files inside the csv_files folder located strictly within the node directory.

Correct Folder Structure:

```
ComfyUI/custom_nodes/ComfyUI-CSV-to-Prompt/
│
├── csv_files/            <-- PUT YOUR CSV FILES HERE
│   ├── my_prompts.csv
│   └── project_ideas.csv
│
├── __init__.py
├── csv_prompt_node.py
└── README.md

```
📝 CSV File Format
Your CSV file must have headers. The node specifically looks for columns named positive and negative.

Example input.csv:
```
positive,negative
"A futuristic city with flying cars, cyberpunk style","text, watermark, blurry"
"A cute cat sitting on a cloud, 4k, masterpiece","bad quality, distorted"
"Portrait of a warrior, realistic lighting","drawing, sketch, anime"

```
🚀 How to Use (Batch Generation)

This node allows you to generate images for every row in your CSV automatically without changing the prompt manually.

📂 **Step 1: Connect the Node**




Add Node: Double-click and search for CSV to Prompt (Category: Custom/CSV).

Select File: Choose your CSV file from the dropdown list.

Connect Outputs:

Connect positive_string to your CLIP Text Encode (Positive).

Connect negative_string to your CLIP Text Encode (Negative).



📂 **Step 2: Configure for Bulk Processing**




To make ComfyUI run through the list automatically:


On the CSV to Prompt node, ensure the seed widget is set to "increment" (this is usually the default).

Logic: Seed 1 loads Row 1, Seed 2 loads Row 2, etc.

Go to the ComfyUI Main Menu (floating bar on the right).

Set Batch count to the number of rows in your CSV (e.g., if you have 10 prompts, set Batch count to 10).

Click Queue Prompt.

esult: ComfyUI will run 10 times, generating a unique image for every prompt in your file!


<img width="711" height="482" alt="image" src="https://github.com/user-attachments/assets/afb01542-8c39-4998-afd1-3ea1f84ff00f" />

<img width="185" height="67" alt="image" src="https://github.com/user-attachments/assets/cd84ec44-2b89-4181-881d-365812cf2a71" />

<img width="676" height="117" alt="image" src="https://github.com/user-attachments/assets/5170459e-fd6c-4526-bfc2-e118ce619811" />




❓ **Troubleshooting**


"No CSV file found"

Ensure your file is inside the csv_files folder inside the custom node directory.

Click the "Refresh" button on the ComfyUI floating menu to reload the file list.

"Prompt has no outputs"

This error means your workflow is incomplete. Ensure you have a Save Image or Preview Image node at the very end of your workflow.



👨‍💻 **Credits**

**Developed by Tharinda Marasingha**
