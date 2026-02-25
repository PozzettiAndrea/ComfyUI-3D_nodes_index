Readme.md

Workflow Guide: Extracting Model Metadata

This workflow begins with running Model_Lister_with_paths.ps1, which lists all available model files along with their paths. Use this output to copy-paste the file paths into each node above for metadata extraction.

You can preload requirements if you like.
.\ComfyUI_windows_portable\python_embeded\python.exe -m pip install -r requirements.txt
(For Windows ComfyUI Portable as an example)

Simply copy from the mocel_list.txt file and paste it into one or all nodes above. Connect the String Outputs from anyone of the three nodes to the string input connector of the Display String Node.

Click RUN and wait. As you progess to Enahnced and Advanced nodes, the data extraction times will increase. Also, for large models, expect log extraction times. Please be patient and let the workflow finish.

1️⃣ Model Metadata Reader
Purpose:

Extract basic metadata from models in various formats, including Safetensors, Checkpoints (.ckpt, .pth, .pt, .bin).

Provides a structured metadata report for supported model formats.

Detects the model format automatically and applies the correct extraction method.

How It Works: ✔ Reads metadata from Safetensors models using safetensors.safe_open(). ✔ Extracts available keys from Torch-based models (ckpt, .bin, .pth). ✔ Returns structured metadata when available, otherwise reports unsupported formats. ✔ Logs errors in case extraction fails.

Use this node for a quick overview of model metadata without deep metadata parsing.

2️⃣ Enhanced Model Metadata Reader
Purpose:

Extract deep metadata from models, including structured attributes and raw text parsing.

Focuses heavily on ONNX models, using direct binary parsing to retrieve metadata without relying on the ONNX Python package.

How It Works: ✔ Reads ONNX files as raw binary, searching for readable metadata like author, description, version, etc. ✔ Extracts ASCII-readable strings directly from the binary file if structured metadata isn't available. ✔ Provides warnings when metadata is missing but still displays raw extracted text. ✔ Enhanced logging for debugging failed extractions and unsupported formats.

This node is ideal for ONNX models, offering both metadata and raw text extraction for deeper insights.

3️⃣ Advanced Model Data Extractor
Purpose:

Extract structured metadata and raw text together from various model formats.

Supports Safetensors, Checkpoints (.ckpt, .pth, .bin, .gguf, .onnx).

How It Works: ✔ Extracts metadata for Safetensors using direct access to model properties. ✔ Retrieves Torch model metadata such as available keys. ✔ Attempts raw text extraction from the binary file using character encoding detection (chardet). ✔ Limits raw text output for readability while keeping detailed extraction logs.

This node provides both metadata and raw text from models, making it the most comprehensive extraction tool in the workflow.

🚀 Final Notes
Run Model_Lister_with_paths.ps1 first, then copy a model path into each node.

Use ModelMetadataReader for quick metadata lookup.

Use EnhancedModelMetadataReader for deep metadata parsing, especially for ONNX models.

Use AdvancedModelDataExtractor for full metadata + raw text extraction.