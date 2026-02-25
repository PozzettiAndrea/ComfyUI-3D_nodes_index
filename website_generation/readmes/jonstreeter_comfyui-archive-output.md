# ComfyUI Archive Output

A comprehensive ComfyUI custom node for organizing and optimizing your generated images. Archive output files into date-structured folders and convert PNG images to JPEG/WebP with full workflow metadata preservation, saving 85-95% disk space.

## Features

### Archive Management
- **UI Button Integration**: Easy one-click archiving directly from the ComfyUI interface
- **Settings Panel**: Configure archive behavior through a convenient settings dialog
- **Date-based organization**: Files are organized by their modification date (YYYY-MM-DD)
- **Structure preservation**: Maintains original subdirectory structure within archives
- **Flexible filtering**: Skip hidden files and specific file extensions
- **Folder exclusions**: Automatically skips `database` folders and system folders (starting with `_`)
- **Automatic cleanup**: Removes empty directories after archiving
- **Persistent Settings**: Your preferences are saved and remembered
- **Backward Compatible**: Also includes a workflow node for automation

### Image Compression (NEW!)
- **PNG to JPEG/WebP conversion**: Reduce file sizes by 85-95% while preserving quality
- **Workflow metadata preservation**: Maintains ComfyUI workflow data in EXIF tags
- **Drag-and-drop restore**: Load workflows from compressed images ⚠️ **Requires [ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver) extension**
- **Configurable quality**: Adjust compression quality (70-100%, default 90%)
- **Format options**:
  - **JPEG**: Lossy compression, widely supported, good for final outputs
  - **WebP**: Lossy compression with better quality/size ratio, supports lossless mode
- **Safe operation**: Option to keep original files until you verify quality
- **Batch processing**: Convert all PNG files in your output directory at once
- **Smart fallback**: Handles large workflows with automatic fallback strategy

## Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Archive Output"
3. Click Install

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/jonstreeter/comfyui-archive-output.git
   ```

3. Install dependencies:
   ```bash
   cd comfyui-archive-output
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

### Optional: For Workflow Restoration from Compressed Images

To restore workflows by dragging compressed JPEG/WebP images into ComfyUI, install **ComfyUI-Image-Saver**:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/alexopus/ComfyUI-Image-Saver.git
```

Without this extension, compressed images will still be viewable but won't restore workflow data when dragged into ComfyUI.

## Usage

### Using the Settings Panel (Primary Method)

1. **Open Settings**: Click the gear/settings icon in ComfyUI (bottom right corner)

2. **Navigate to Archive Output**: In the settings panel, expand the "Archive Output" section

3. **Configure Settings** (Optional):
   - **Archive Folder Name**: Name of the archive folder (default: "Archive")
   - **Skip Hidden Files**: Skip files starting with `.` (default: enabled)
   - **Skip File Extensions**: Comma-separated list of file extensions to skip (default: `.py,.js,.bat,.sh,.json,.yaml,.yml`)
   - **Skip Folders**: Comma-separated list of folder names to skip (default: `database`). Folders starting with `_` are always skipped.

4. **Execute Archive**:
   - In the "Archive Output" > "Actions" section, click the "📦 Archive Now" button
   - A progress dialog will appear
   - When complete, you'll see a summary of files moved, skipped, and any errors

### Using Image Conversion

The image conversion feature allows you to reduce disk space usage by converting PNG files to JPEG or WebP format while preserving ComfyUI workflow metadata.

1. **Open Settings**: Click the gear/settings icon in ComfyUI

2. **Configure Compression** (under "Archive Output" > "Compression Settings"):
   - **Target Folder**: (Optional) Specify folder to compress
     - Leave empty for main output folder
     - Enter relative path like `Archive` or `Archive/2025-01-15`
     - Or absolute path like `G:/AIART/output/Archive`
   - **Include Subdirectories**: Process all subdirectories recursively (default: enabled)
     - When enabled, processes all PNG files in all nested folders
     - Includes Archive folders (no folders are skipped)
   - **Compression Quality**: Adjust quality slider (70-100%, default 90%)
     - 90%: Recommended - visually lossless for most images, ~90% space savings
     - 95%: Higher quality, slightly larger files
     - 85%: More aggressive compression, smaller files
   - **Output Format**: Choose WebP or JPEG
     - **WebP (Recommended/Default)**: Better compression ratio, full metadata support, no size limits, supports lossless mode
     - JPEG: Lossy compression, more widely compatible, but EXIF metadata limited to 65KB
   - **Delete Original PNG**: ⚠️ Warning - This is irreversible!
     - Keep disabled until you verify compressed images meet your needs

3. **Execute Compression**:
   - In the "Archive Output" > "Actions" section, click the "🗜️ Compress Now" button
   - A **real-time progress dialog** appears showing:
     - Animated progress bar with percentage
     - Current file being processed
     - Files compressed so far
     - Running space savings total
     - **Cancel button** to stop at any time
   - When complete (or cancelled), you'll see a summary:
     - Number of files compressed
     - Space savings (MB and percentage)
     - Metadata preservation status (full/partial/none)

4. **View Results**:
   - Original PNGs are converted to .jpg or .webp files in the same location
   - Workflow metadata is embedded in EXIF tags
   - **To restore workflows**: Install [ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver), then drag compressed images into ComfyUI
   - If "Delete Original PNG" was enabled, PNG files are removed after successful compression

#### Compression Results Example

**Typical Savings:**
- 100 images @ 5MB each (PNG) → 500 MB total
- After compression (JPEG 90%) → 50 MB total
- **Space saved: 450 MB (90% reduction)**

#### Metadata Preservation

The compression feature preserves ComfyUI workflow data using EXIF metadata:

- **Full workflow preserved**: Both workflow and prompt data (most common for simple/medium workflows)
- **Workflow only**: Workflow preserved, prompt removed due to size limits
- **No metadata**: Workflow too large for JPEG EXIF (65KB limit)
  - Solution: Use WebP format for better metadata support
  - Or keep original PNG for very complex workflows

#### Tips for Best Results

1. **Start with "Delete Original PNG" disabled** - Verify quality first
2. **Use WebP format (default)** - Better compression and no metadata size limits
3. **Use 90% quality** - Sweet spot between quality and file size
4. **Test drag-and-drop** - Verify workflow restoration works before mass compression
5. **Archive first, compress second** - Organize files before compressing for easier management
6. **Large batches**: Progress bar updates in real-time, you can cancel anytime if needed
7. **Tens of thousands of images?** - The process handles it! Just click compress and monitor progress
8. **Compress archived files**: Set Target Folder to `Archive` to compress all your archived PNGs
9. **Compress specific date**: Set Target Folder to `Archive/2025-01-15` to compress just one day's images

### Archive Structure

Files are organized by modification date:

```
output/
  Archive/
    2025-01-15/
      image_001.png
      image_002.png
    2025-01-16/
      subfolder/
        image_003.png
```

### Using the Workflow Node (Advanced)

For automation, a workflow node is also available:

**Node Inputs:**
- `trigger`: Any type - Connect any node output to trigger the archive process
- `enabled`: Boolean (default: True) - Enable/disable archiving
- `archive_folder_name`: String (default: "Archive") - Name of the archive folder
- `skip_hidden_files`: Boolean (default: True) - Skip files starting with `.`
- `skip_extensions`: String - Comma-separated list of file extensions to skip
- `skip_folders`: String (default: "database") - Comma-separated list of folder names to skip (`_*` folders are always skipped)

**Node Outputs:**
- `status`: String - Summary of the archive operation

## Configuration

### Skip Extensions

You can customize which file types to skip during archiving. By default, these extensions are skipped:
- `.py` - Python files
- `.js` - JavaScript files
- `.bat` - Batch files
- `.sh` - Shell scripts
- `.json` - JSON files
- `.yaml`, `.yml` - YAML files

To modify, edit the `skip_extensions` parameter with a comma-separated list.

### Skip Folders

The archiver automatically skips:
1. The **Archive** folder itself
2. Any folder named `database` (configurable)
3. Any folder starting with `_` (e.g., `_preview`, `_system`)

You can customize specific folder names to exclude using the `skip_folders` parameter.

### Archive Folder Location

The archive folder is created inside your ComfyUI output directory. You can customize the folder name using the `archive_folder_name` parameter.

## Notes

- Files are **moved** (not copied) to the archive
- If a file with the same name already exists in the archive, it will be skipped
- The archive folder itself is never processed to prevent recursive archiving
- Empty directories are automatically removed after archiving

## Requirements

### Core Requirements
- ComfyUI
- Python 3.8+
- Pillow (PIL) - Usually included with ComfyUI
- piexif >= 1.1.3 - For EXIF metadata handling (compression feature)

Dependencies are automatically installed via `requirements.txt`.

### Optional (for Workflow Restoration)
- **[ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver)** - Required to restore workflows from compressed JPEG/WebP images by drag-and-drop
  - Without this: Compressed images are viewable but won't restore workflow data
  - With this: Drag compressed images into ComfyUI to restore the original workflow

## Troubleshooting

### Settings Don't Appear
1. Restart ComfyUI completely
2. Hard refresh browser: `Ctrl + Shift + R` (Windows/Linux) or `Cmd + Shift + R` (Mac)
3. Check browser console (F12) for errors

### Compression Errors
- Ensure `piexif` is installed: `pip install piexif`
- Check ComfyUI console for detailed error messages
- Verify PNG files are not corrupted

### Archive Folder Not Created
- Check write permissions on the output directory
- Verify the archive folder name doesn't contain invalid characters

## Credits

- **Compression methodology** inspired by [ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver) by alexopus
- **Metadata preservation** uses EXIF embedding technique from ComfyUI-Image-Saver

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or feature requests, please visit the [GitHub Issues page](https://github.com/jonstreeter/comfyui-archive-output/issues).
