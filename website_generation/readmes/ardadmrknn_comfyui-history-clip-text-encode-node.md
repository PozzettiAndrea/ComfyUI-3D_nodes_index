# **ComfyUI Prompt History Node**

A custom node for ComfyUI that automatically saves your prompts, generated images, and workflow metadata into a browsable history, accessible directly from the node.

This node is designed to replace the standard "CLIP Text Encode" node. It performs the same function while adding powerful history-tracking features in the background.

## **Features**

* **Automatic History:** Saves your prompt every time a workflow is executed.  
* **Thumbnail Capture:** Automatically captures the first generated image and links it to your prompt.  
* **Workflow Metadata:** Saves a snapshot of your workflow (node setup, seeds, models, etc.) with each prompt.  
* **In-UI History Browser:** A "View History" button on the node opens a modal to browse all saved prompts.  
* **Favorites:** Mark your best prompts as "favorites" and filter to see only them.  
* **History Management:** Delete unwanted prompts or just their thumbnails directly from the modal.  
* **Smart Naming:** Automatically creates separate history files based on your workflow's file name.

## **Installation**

### **Option 1: Using ComfyUI Manager (Recommended)**

1. (Yakında) Bu repo ComfyUI Manager listesine eklendiğinde, buradan aratıp yükleyebilirsiniz.  
2. (Şimdilik) ComfyUI Manager \-\> "Install via Git" seçeneğini kullanın.  
3. Şu URL'i yapıştırın: https://github.com/YOUR\_USERNAME/ComfyUI-PromptHistory.git  
4. "Install"a tıklayın ve ComfyUI'ı yeniden başlatın.

### **Option 2: Manual (Git Clone)**

1. ComfyUI ana dizininize gidin.  
2. custom\_nodes klasörüne girin: cd ComfyUI/custom\_nodes/  
3. Bu repoyu klonlayın:  
   git clone \[https://github.com/YOUR\_USERNAME/ComfyUI-PromptHistory.git\](https://github.com/YOUR\_USERNAME/ComfyUI-PromptHistory.git)

4. ComfyUI'ı yeniden başlatın.

## **Usage**

1. In ComfyUI, add a new node: Add Node \> Utilities \> Prompt History (CLIP Text Encode).  
2. Use this node exactly as you would use a normal CLIP Text Encode node (i.e., connect your CLIP model and text input).  
3. The history\_name field will auto-fill from your workflow's filename. You can change it to group prompts manually.  
4. Run your workflow. The prompt and (eventually) the first generated image will be saved.  
5. Click the **"View History"** button on the node to open the modal and browse your saved prompts.
