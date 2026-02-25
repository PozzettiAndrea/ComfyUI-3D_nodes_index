# ComfyUI S3 Image Nodes

A powerful ComfyUI extension that enables seamless integration with AWS S3 storage for reading and saving images directly within your ComfyUI workflows. This extension eliminates the need for manual file transfers by providing direct S3 connectivity for your image processing pipelines.

## 📸 See It In Action

![ComfyUI S3 Image Connect Custom Nodes Demo](workflow-example.png)
*ComfyUI workflow showing S3 nodes in action*

## 🚀 What This Project Does

This ComfyUI extension provides two custom nodes that enable direct interaction with AWS S3 storage:

- **Read images directly from S3** using flexible, user-defined paths
- **Save processed images directly to S3** with automatic timestamping
- **Custom S3 path input** - specify any S3 object key directly in the interface
- **Automatic image processing** including EXIF orientation correction and format standardization

### 📸 Supported Image Formats

The extension supports the following single-frame image formats:
- `.png` - Portable Network Graphics
- `.jpg` / `.jpeg` - JPEG images
- `.bmp` - Bitmap images
- `.webp` - WebP images
- `.tiff` - Tagged Image File Format

> **⚠️ Important Note**: This extension processes images as **RGB only** and does not support alpha channels or masks. All images are converted to 3-channel RGB format during processing.

## 📦 Installation

### 1. Clone the Repository

Navigate to your ComfyUI custom nodes directory and clone this repository:

```bash
# Navigate to ComfyUI custom nodes directory
cd /ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/lakkiy/ComfyUI-RWImageS3.git

# Navigate into the project directory
cd ComfyUI-RWImageS3
```

### 2. Install Dependencies

Install the required Python packages using pip. If you're using a virtual environment, make sure to activate it first:

```bash
# If using virtual environment, activate it first
# source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate     # On Windows

# Install dependencies from requirements.txt (recommended)
pip install -r requirements.txt

# Or install manually with specific versions
pip install boto3 numpy pillow python-dotenv torch
```

### 3. Configure AWS Credentials

Edit the `.env` file with your AWS configuration:

```env
# AWS credentials
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-bucket-name
```

### 4. Set Up S3 Bucket Structure

> **✨ New in v2.0**: Flexible folder structure! You can now organize your images in any folder structure you prefer.

Recommended S3 bucket organization:
```
your-bucket-name/
├── images/           # Your source images (any structure)
│   ├── photos/
│   ├── datasets/
│   └── temp/
└── output/          # Processed images will be saved here
```

**Note**: With the updated ReadImageFromS3 node, you can specify any S3 object key directly in the ComfyUI interface.

### 5. Restart ComfyUI

Restart ComfyUI to load the new custom nodes. The nodes will appear in the `image` category.

## 🧩 Available Nodes

### 1. Read Image From S3

**Category**: `image`
**Node Name**: `Read Image From S3`

> **🆕 Updated in v2.0**: Now supports custom S3 paths!

This node loads images directly from any location in your S3 bucket into ComfyUI workflows.

#### Features:
- **✨ Custom S3 path input**: Specify any S3 object key directly in the interface
- **S3 object validation**: Automatically checks if the specified file exists
- **EXIF orientation correction**: Automatically rotates images based on EXIF data
- **Format standardization**: Converts all images to RGB format for consistent processing
- **Tensor normalization**: Outputs properly normalized tensors in [0, 1] range

#### Inputs:
- **s3_key** (text): Full S3 object key path (e.g., "photos/vacation/beach.jpg")

#### Outputs:
- **IMAGE**: PyTorch tensor of shape `[1, H, W, 3]` with RGB values normalized to [0, 1]

#### Usage:
1. Upload images anywhere in your S3 bucket
2. Add the "Read Image From S3" node to your workflow
3. Enter the full S3 object key in the text field (e.g., "my-folder/image.png")
4. Connect the output to other image processing nodes

#### Example S3 Paths:
- `photos/2024/vacation.jpg`
- `datasets/training/sample001.png`
- `input/test.webp`
- `temp/processed_image.bmp`

---

### 2. Save Image To S3

**Category**: `image`
**Node Name**: `Save Image To S3`

This node saves processed images from ComfyUI workflows directly to your S3 bucket's output folder.

#### Features:
- **Automatic timestamping**: Appends timestamp to filenames for uniqueness
- **PNG format**: Saves images in lossless PNG format
- **Pass-through output**: Returns the original image tensor for downstream nodes
- **S3 key tracking**: Provides the S3 location of saved files
- **Batch handling**: Supports both batched `[1, H, W, 3]` and unbatched `[H, W, 3]` tensors

#### Inputs:
- **image** (IMAGE): PyTorch tensor containing the image data to save
- **filename_prefix** (STRING): Base name for the saved file (default: "output_image")

#### Outputs:
- **IMAGE**: The same input tensor (unchanged, for connecting to preview nodes)
- **STRING**: S3 key of the uploaded file (e.g., "output/prefix_20240604123456.png")

#### Usage:
1. Connect an image tensor from any image processing node
2. Set a descriptive filename prefix
3. The node will save the image to S3 and return both the image and S3 location
4. Connect the image output to PreviewImage or other nodes as needed

## 🔧 Configuration Details

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | Your AWS access key ID | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Your AWS secret access key | `wJalrXUtnFEMI/K7MDENG/...` |
| `AWS_REGION` | AWS region for your S3 bucket | `us-east-1` |
| `S3_BUCKET_NAME` | Name of your S3 bucket | `my-comfyui-bucket` |

### S3 Permissions Required

Your AWS credentials need the following S3 permissions:
- `s3:ListBucket` - To list available images
- `s3:GetObject` - To download images from input folder
- `s3:PutObject` - To upload processed images to output folder

Example IAM policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}
```

## 🎯 Example Workflow

Here's a typical workflow using these S3 nodes:

1. **Upload source images** to any folder in your S3 bucket
2. **Add "Read Image From S3"** node and enter the S3 path (e.g., "photos/my-image.jpg")
3. **Apply image processing** nodes (upscaling, filtering, etc.)
4. **Add "Save Image To S3"** node to save the result
5. **Optional**: Connect to PreviewImage to see the result in ComfyUI
6. **Check your S3 `output/` folder** for the processed images

### 🆕 What's New in v2.0:
- **Flexible S3 paths**: No longer restricted to `input/` folder
- **Direct path input**: Type any S3 object key directly in the interface
- **Better validation**: Real-time S3 object existence checking
- **Requirements.txt**: Pinned dependency versions for stable installation

## 🐛 Troubleshooting

### Common Issues:

**"S3 object not found or inaccessible"**
- Verify the S3 object key path is correct (e.g., "folder/image.png")
- Check that the image has a supported file extension
- Ensure your AWS credentials have `s3:GetObject` permission
- Verify the file exists in your S3 bucket

**"Failed to download from S3"**
- Verify your AWS credentials are correct
- Check that your AWS region matches your S3 bucket's region
- Ensure your credentials have `s3:GetObject` permission

**"Failed to upload to S3"**
- Verify your credentials have `s3:PutObject` permission
- Check that your S3 bucket exists and is accessible
- Ensure the output folder exists in your bucket

**"S3 key cannot be empty" or validation errors**
- Make sure to enter a valid S3 object key in the text field
- Verify your `.env` configuration is correct
- Check ComfyUI console for detailed error messages

## 📋 Requirements

- **ComfyUI** (latest version recommended)
- **Python 3.8+**
- **AWS Account** with S3 access
- **Dependencies**: boto3, torch, pillow, python-dotenv, numpy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 🙋‍♂️ Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the ComfyUI console for error messages
3. Open an issue on GitHub with detailed information about your problem

---

**Made with ❤️ for the ComfyUI community**
