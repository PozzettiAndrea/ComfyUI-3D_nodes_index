# 📂 LoadLoopImagesFromDir - ComfyUI Node  
A **ComfyUI** custom node for **loading images sequentially** from a directory.  

<img src="node.png" width="50%">


## 🔹 Features  
- Loads **one image per call**, automatically moves to the next.  
- **Loops back** to the first image when reaching the end.  
- Supports **.jpg, .jpeg, .png, .webp** formats.  
- **Extracts masks** from images with alpha channels.  
- Returns a **torch tensor image, mask, and file path**.  

---

## 🛠 Node Inputs  
| Name         | Type    | Default  | Description |
|-------------|--------|---------|-------------|
| `directory` | String | `""`    | Path to folder with images. |
| `load_always` | Boolean | `False` | Forces reload every call. |

## 📤 Node Outputs  
| Name       | Type        | Description |
|-----------|------------|-------------|
| `IMAGE`   | Tensor     | Loaded image as a torch tensor. |
| `MASK`    | Tensor     | Mask (alpha channel) or blank mask. |
| `FILE PATH` | String  | Full path to the loaded image. |

---

## 🔄 How It Works  
1. **Reads all valid images** in the directory.  
2. **Sorts** the list alphabetically.  
3. **Loads the next image** each time the node runs.  
4. **Loops back** to the first image when reaching the end.  
5. **Returns the image, mask, and path.**  

---

## 🏗 Installation  
1️⃣ **Make sure ComfyUI is installed.**  
2️⃣ Clone this node in the `custom_nodes` folder.  
   ```
   git clone https://github.com/alessandrozonta/Comfyui-LoopLoader.git
   ```
3️⃣ Restart ComfyUI.  

---

## ⚠️ Errors & Debugging  
- **Directory not found** → Check the folder path.  
- **No images found** → Ensure there are valid image files.  
- **Mask is empty** → Only images with alpha channels will have masks.  

---

## 🔧 License & Contributions  
- **License:** GPL-3.0  
- **Contribute:** Open a pull request!  
- **Issues:** Report bugs on GitHub.  
