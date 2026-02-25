<p align="center">
  <img src="./web/assets/Dark_Usgromana-Gallery.png" width="220" />
</p>
# ComfyUI-Usgromana-Gallery

A comprehensive image gallery extension for ComfyUI that provides advanced image management, metadata editing, NSFW content filtering, real-time file monitoring, and a full-featured file explorer.

## Overview

ComfyUI-Usgromana-Gallery transforms ComfyUI's output directory into an interactive, feature-rich image gallery. It offers a modern web-based interface for browsing, organizing, rating, and managing generated images with support for user permissions, content filtering, extensive metadata management, and a Windows Explorer-style file browser.

### Key Capabilities

- **Image Gallery Viewing**: Browse all images in your ComfyUI output directory with thumbnails and full-screen viewing
- **File Explorer**: Navigate your output directory with multiple view modes (Details, Small Icons, Medium Icons, Large Icons, Tiles)
- **Metadata Management**: View and edit comprehensive image metadata including prompts, workflow data, generation parameters, and custom tags
- **Rating System**: Rate images with a 5-star system that persists across sessions
- **NSFW Content Filtering**: Integrates with ComfyUI-Usgromana NSFW API to automatically filter content based on user permissions
- **File Management**: Rename, delete, move, and organize files and folders directly from the interface
- **Real-time Updates**: Automatically detects and displays new images as they are generated
- **Batch Operations**: Download or delete multiple images at once
- **Advanced Viewing**: Zoom and pan functionality for detailed image inspection
- **Window Management**: Pin/unpin the gallery window, move and resize it, with click-through support when unpinned
- **Theme Support**: Dark and light themes with automatic text color adaptation

---

## Features

### 1. Image Gallery Grid

The main gallery view displays all images from your ComfyUI output directory in a responsive grid layout.

**Features:**
- Thumbnail grid with configurable sizes (small, medium, large)
- Star ratings displayed on each image (when enabled)
- Click any image to open the detailed view
- Search functionality to filter images by filename, model, or prompt
- Rating filter to show only images above a certain rating threshold
- Real-time updates when new images are generated

**How to Use:**
1. Click the gallery button in ComfyUI's action bar to open the gallery
2. Browse images in the grid view
3. Use the search bar to find specific images
4. Adjust the rating filter slider to show only highly-rated images
5. Click any image thumbnail to view it in detail

### 2. File Explorer

A full-featured file explorer that lets you navigate and manage your output directory with multiple view modes inspired by Windows File Explorer.

**Features:**
- **Multiple View Modes**:
  - **Details View**: List view with file names, sizes, and metadata
  - **Small Icons**: Compact icon view with thumbnails
  - **Medium Icons**: Medium-sized icon view with thumbnails
  - **Large Icons**: Large icon view with thumbnails
  - **Tiles View**: Tile view with thumbnails and file information
- **Breadcrumb Navigation**: Navigate through folder hierarchy with clickable breadcrumbs
- **Image Thumbnails**: Automatic thumbnail generation for image files in icon/tile views
- **Folder Management**: Create, rename, and delete folders
- **File Operations**: Rename and delete files directly from the explorer
- **Drag and Drop**: Move files and folders by dragging them to new locations
- **Theme-Aware**: Text colors automatically adapt to light/dark themes

**How to Use:**
1. Click the folder/viewer button in the gallery header to switch to explorer mode
2. Use the view mode buttons (☰ Details, ⊞ Icons, ⊟ Tiles) to change the display style
3. Double-click folders to navigate into them
4. Double-click image files to open them in the detailed view
5. Use breadcrumbs to navigate back to parent folders
6. Drag files or folders to move them to different locations
7. Hover over items to reveal action buttons (rename, delete)

**View Mode Details:**
- **Details View**: Traditional list view showing file names, sizes, and icons in a single column
- **Icon Views**: Grid layout with image thumbnails (or emoji icons for non-images) and file names below
- **Tiles View**: Larger grid items with thumbnails, file names, and file sizes

### 3. Detailed Image View

The detailed view provides a full-screen experience for viewing and managing individual images.

**Features:**
- Full-resolution image display
- Side thumbnails for previous/next navigation
- Keyboard navigation (Arrow keys, Escape)
- Zoom and drag mode for detailed inspection
- Quick action buttons (metadata, open in new tab, zoom, close)
- Folder-aware navigation when opened from explorer

**How to Use:**
1. Click an image in the grid or explorer to open the detailed view
2. Use arrow keys or click side thumbnails to navigate between images
3. Click the "+" button to enable zoom mode, then:
   - Use mouse wheel to zoom in/out (zooms toward cursor position)
   - Click and drag to pan when zoomed in
4. Press Escape or click the "✖" button to close

### 4. Window Management (Pin/Unpin)

Control the gallery window's position and behavior with pin/unpin functionality.

**Features:**
- **Pin/Unpin Button**: Toggle between pinned and unpinned states
- **Pinned Mode**: Window is centered with a backdrop shadow, cannot be moved
- **Unpinned Mode**: 
  - Window can be dragged by the header
  - Window can be resized using the corner resize handle
  - Backdrop shadow is removed
  - Clicks pass through to the underlying ComfyUI workflow (click-through)
  - Window position and size are saved and restored
- **Click-Through**: When unpinned, interact with ComfyUI workflow while gallery is open

**How to Use:**
1. Click the pin button (📌) in the gallery header
2. When unpinned (📍), drag the header to move the window
3. Drag the bottom-right corner to resize the window
4. Click the pin button again to pin the window back to center
5. When unpinned, you can interact with the ComfyUI workflow behind the gallery

**Benefits:**
- Monitor images being generated in real-time while working on workflows
- Manage your photo directory without interrupting your workflow
- Position the gallery window anywhere on your screen for optimal workflow

### 5. Moveable Settings and Filter Windows

Settings and filter panels can be moved around the screen for better workflow management.

**Features:**
- Drag the header to move the settings window
- Drag the header to move the filter panel
- Windows stay within viewport bounds
- Shared color scheme between settings and filter windows
- Theme-aware styling

**How to Use:**
1. Open the settings or filter panel
2. Click and drag the header to move the window
3. Position it where it's most convenient for your workflow

### 6. Metadata Panel

The metadata panel displays comprehensive information about each image and allows editing for authorized users.

**Displayed Information:**
- **File Information**: Width, height, format, MIME type, file size, modification date
- **Generation Parameters**: Steps, CFG scale, seed, sampler, scheduler, model
- **Prompts**: Positive prompt, negative prompt, full prompt
- **Workflow Data**: Complete workflow JSON (if available)
- **User Metadata**: Rating (1-5 stars), tags (as colored pills), display name
- **NSFW Status**: Content warning badge if image is marked as NSFW

**How to Use:**
1. Open an image in the detailed view
2. Click the "ⓘ" button to open the metadata panel
3. View all available metadata
4. For admins: Click the pencil icon next to editable fields to modify them
5. Press Enter to save changes, Escape to cancel

### 7. Rating System

Rate images with a 1-5 star system that persists across sessions.

**Features:**
- Click stars directly on grid images to set rating
- Click stars in the metadata panel to set rating
- Ratings are stored in both metadata files and image EXIF data
- Filter images by minimum rating threshold
- Ratings sync between grid and metadata views

**How to Use:**
1. Click the star rating on any image (grid or metadata panel)
2. The rating is saved automatically
3. Use the rating filter slider to show only images above a certain rating
4. Ratings are visible in both the grid overlay and metadata panel

### 8. Tagging System

Add and manage tags for organizing your images.

**Features:**
- Add multiple tags per image (comma-separated)
- Tags displayed as colored pills in the metadata panel
- Tags stored in image metadata and JSON files
- Tags written to image EXIF data for Windows Properties compatibility

**How to Use:**
1. Open the metadata panel for an image
2. Click the pencil icon next to "Tags"
3. Enter tags separated by commas (e.g., "portrait, high-quality, anime")
4. Press Enter to save
5. Tags will appear as colored pills below the field

### 9. NSFW Content Filtering

Automatic content filtering based on user permissions and NSFW detection.

**Features:**
- Integrates with ComfyUI-Usgromana NSFW API
- Automatically detects NSFW content in images
- Filters images based on user permissions (admin, authenticated, guest)
- Manual NSFW tagging available for admins
- Content warning badges in metadata panel
- Respects user's SFW enforcement settings

**How to Use:**
- **Automatic**: NSFW filtering happens automatically based on your user account
- **Manual Tagging** (Admin only):
  1. Open the metadata panel for an image
  2. Click the "Mark as NSFW" button
  3. Confirm the action
  4. The image will be tagged and filtered accordingly

**Requirements:**
- ComfyUI-Usgromana extension must be installed
- NSFW API must be available and properly configured
- User permissions must be set up in ComfyUI-Usgromana

### 10. File Management

Comprehensive file and folder management directly from the gallery interface.

**File Operations:**
- **Rename Files** (Admin only):
  1. In explorer view, hover over a file and click the rename button (✏️)
  2. Or open metadata panel and click the pencil icon next to "File"
  3. Enter the new filename (without extension)
  4. Press Enter to save

- **Delete Files** (Admin only):
  1. In explorer view, hover over a file and click the delete button (🗑️)
  2. Or open metadata panel and scroll to bottom and click "🗑️ Delete Image"
  3. Confirm the deletion

- **Move Files/Folders**:
  1. In explorer view, drag a file or folder
  2. Drop it onto a folder or the file list area
  3. The item will be moved to the new location

**Folder Operations:**
- **Create Folder**: Click "+ New Folder" button in explorer toolbar
- **Rename Folder**: Hover over folder and click rename button (✏️)
- **Delete Folder**: Hover over folder and click delete button (🗑️)
- **Move Folder**: Drag and drop folder to new location

**Note**: File rename and delete operations are only available to administrators.

### 11. Zoom and Drag Mode

Inspect images in detail with zoom and pan functionality.

**Features:**
- Zoom range: 0.5x to 5.0x
- Mouse wheel zoom toward cursor position
- Click and drag to pan when zoomed in
- Smooth transitions and visual feedback
- Automatically resets when switching images or closing the view

**How to Use:**
1. Open an image in the detailed view
2. Click the "+" button in the top-right corner
3. Use mouse wheel to zoom in/out (zooms toward cursor position)
4. When zoomed in, click and drag to pan around the image
5. Click "+" again to disable zoom mode

### 12. Batch Operations

Perform operations on multiple images at once.

**Batch Download:**
1. Select multiple images using Ctrl/Cmd+Click
2. Click the batch download button
3. All selected images will be downloaded as a ZIP file

**Batch Delete (Admin only):**
1. Select multiple images using Ctrl/Cmd+Click
2. Click the batch delete button
3. Confirm the deletion
4. All selected images will be permanently deleted

### 13. Settings and Configuration

Customize the gallery behavior through the settings panel.

**Available Settings:**
- **Theme**: Dark or light mode (with automatic text color adaptation)
- **Thumbnail Size**: Small, medium, or large
- **Show Rating in Grid**: Toggle star rating overlay on grid images
- **Enable Drag**: Allow dragging images from the grid
- **Show Dividers**: Group images by folder, date, or alphabetically
- **Sort By**: Name, time, size, or pixels
- **File Extensions**: Configure which image formats to display
- **Real-time Updates**: Enable/disable automatic file monitoring

**How to Access:**
1. Open the gallery
2. Click the settings/gear icon
3. Adjust settings as desired
4. Settings are saved automatically

### 14. Real-time File Monitoring

Automatically detect and display new images as they are generated.

**Features:**
- Watches the output directory for new files
- Automatically adds new images to the gallery
- Supports both native file system events and polling fallback
- Configurable file extensions to monitor

**Requirements:**
- `watchdog` Python package (optional but recommended)
- If watchdog is not available, polling mode is used automatically

**Installation:**
```bash
pip install watchdog
```

---

## Advanced Features and Requirements

### Admin-Only Features

Several features require administrator privileges - ComfyUI-Usgromana extension must be installed:

**Admin Features:**
- Edit metadata fields (filename, display name, tags, prompts, parameters)
- Rename image files
- Delete images (single or batch)
- Mark images as NSFW manually
- Create, rename, and delete folders

**How to Become Admin:**
- Your user account must have `is_admin: true` in ComfyUI-Usgromana user configuration
- OR your user must be in the "admin" group
- OR your user must have `can_edit: true` permission

**Checking Admin Status:**
- If you see pencil icons next to fields in the metadata panel, you have admin access
- If fields are read-only and no pencil icons appear, you do not have admin access

### NSFW API Integration

The gallery integrates with ComfyUI-Usgromana's NSFW API for content filtering.

**Requirements:**
1. ComfyUI-Usgromana extension must be installed
2. NSFW API must be available and properly configured
3. User permissions must be set up in ComfyUI-Usgromana

**What It Does:**
- Automatically detects NSFW content in images
- Filters images based on user permissions
- Blocks NSFW images for users with SFW restrictions
- Allows manual NSFW tagging for administrators
- Displays content warnings in the metadata panel

**If NSFW API is Not Available:**
- Gallery will still function normally
- NSFW filtering will be disabled
- All images will be visible to all users
- Manual NSFW tagging will not be available

### Metadata Persistence

Metadata is stored in multiple locations for reliability:

**Storage Locations:**
1. **JSON Files** (in extension's `data` directory):
   - `metadata.json`: User-edited metadata (tags, display names, ratings)
   - `ratings.json`: Legacy ratings storage (merged with metadata)
   - `settings.json`: Gallery settings

2. **Image Files** (embedded in image metadata):
   - PNG text chunks: Rating, Tags, Title, NSFW status
   - XMP metadata: For Windows Properties compatibility
   - EXIF data: Where supported

**Benefits:**
- Metadata survives file moves (if using relpath)
- Visible in Windows File Properties
- Compatible with other image management tools
- Redundant storage ensures data safety

### Theme System

The gallery supports dark and light themes with automatic text color adaptation.

**Features:**
- **Dark Theme**: Dark backgrounds with light text
- **Light Theme**: Light backgrounds with dark text
- **Automatic Text Colors**: Text colors automatically adapt based on theme
- **Theme Persistence**: Theme preference is saved and restored
- **Consistent Styling**: All UI elements (explorer, settings, filter panels) share theme colors

**How to Change Theme:**
1. Open the settings panel
2. Select "Dark" or "Light" from the Theme dropdown
3. Theme is applied immediately and saved automatically

---

## Troubleshooting

### Gallery Not Loading

**Symptoms**: Gallery button doesn't appear or clicking it does nothing.

**Solutions:**
1. Check browser console for JavaScript errors (F12)
2. Verify the extension is properly installed in `custom_nodes/ComfyUI-Usgromana-Gallery`
3. Restart ComfyUI server
4. Clear browser cache and reload the page
5. Check that `__init__.py` is loading without errors in the ComfyUI console

### Images Not Appearing

**Symptoms**: Gallery opens but shows no images.

**Solutions:**
1. Verify images exist in ComfyUI's output directory
2. Check that file extensions match your settings (default: .png, .jpg, .jpeg, .webp, .gif, .bmp)
3. Check browser console for API errors
4. Verify the output directory path is correct
5. Try refreshing the gallery (close and reopen)

### File Explorer Not Working

**Symptoms**: Explorer view doesn't load or shows errors.

**Solutions:**
1. Check browser console for JavaScript errors
2. Verify you have proper file system permissions
3. Try switching back to grid view and then to explorer again
4. Check that the backend API is responding (check Network tab in browser dev tools)
5. Restart ComfyUI server

### Window Pin/Unpin Issues

**Symptoms**: Window can't be moved or resized when unpinned.

**Solutions:**
1. Ensure you've clicked the pin button to unpin the window (should show 📍 icon)
2. Try dragging from the header area (not buttons)
3. Check browser console for JavaScript errors
4. Try pinning and unpinning again
5. Clear browser cache and reload

### NSFW Filtering Not Working

**Symptoms**: NSFW images visible to users who shouldn't see them, or all images blocked.

**Solutions:**
1. Verify ComfyUI-Usgromana extension is installed
2. Check that NSFW API is available (look for "[Usgromana-Gallery] NSFW API available" in console)
3. Verify user permissions in ComfyUI-Usgromana configuration
4. Check console for NSFW API errors
5. If API is not available, filtering is disabled (expected behavior)

### Metadata Not Saving

**Symptoms**: Changes to metadata don't persist after closing the gallery.

**Solutions:**
1. Verify you have admin permissions (check for pencil icons)
2. Check browser console for API errors
3. Verify the `data` directory exists and is writable
4. Check ComfyUI console for backend errors
5. Try saving again - some fields may require admin access

### Ratings Not Showing

**Symptoms**: Star ratings don't appear on grid images.

**Solutions:**
1. Check gallery settings - ensure "Show rating overlay in grid" is enabled
2. Verify ratings are being saved (check metadata panel)
3. Refresh the gallery
4. Check that `ratings.json` or metadata contains rating data

### Real-time Updates Not Working

**Symptoms**: New images don't appear automatically.

**Solutions:**
1. Check settings - ensure "Enable real-time updates" is enabled
2. Install `watchdog` package: `pip install watchdog`
3. If watchdog is not available, polling mode should work automatically
4. Try manually refreshing the gallery
5. Check ComfyUI console for file monitoring errors

### Performance Issues

**Symptoms**: Gallery is slow to load or navigate.

**Solutions:**
1. Reduce thumbnail size in settings
2. Disable real-time updates if not needed
3. Use rating/search filters to reduce visible images
4. Check for large numbers of images (consider organizing into subfolders)
5. NSFW checks are cached - first load may be slower

### Admin Features Not Available

**Symptoms**: Can't edit metadata, rename files, or delete images.

**Solutions:**
1. Verify your user account has admin privileges in ComfyUI-Usgromana
2. Check that `is_admin: true` or `can_edit: true` is set in your user configuration
3. Verify you're logged in (not a guest user)
4. Check browser console for permission errors
5. Restart ComfyUI server after changing user permissions

### Metadata Panel Not Opening

**Symptoms**: Clicking metadata button does nothing or panel doesn't appear.

**Solutions:**
1. Check browser console for JavaScript errors
2. Try closing and reopening the detailed view
3. Verify the image has loaded completely
4. Check that metadata API endpoint is responding (check Network tab)
5. Refresh the page and try again

### Zoom/Drag Mode Not Working

**Symptoms**: "+" button doesn't enable zoom or drag doesn't work.

**Solutions:**
1. Ensure you've clicked the "+" button to enable zoom mode (button should highlight)
2. Try scrolling the mouse wheel over the image
3. Ensure you're zoomed in (>1.0x) before trying to drag
4. Check browser console for JavaScript errors
5. Try disabling and re-enabling zoom mode

---

## Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone <repository-url> ComfyUI-Usgromana-Gallery
   ```

2. Install optional dependencies (recommended for real-time file monitoring):
   ```bash
   pip install watchdog
   ```

3. Restart ComfyUI server

4. The gallery button should appear in ComfyUI's action bar

---

## Requirements

### Required
- ComfyUI (latest version)
- Python 3.8+
- PIL/Pillow (usually included with ComfyUI)

### Optional but Recommended
- `watchdog>=3.0.0` - For efficient real-time file monitoring
- ComfyUI-Usgromana extension - For NSFW content filtering

### For Advanced Features
- **Admin Access**: Requires ComfyUI-Usgromana user configuration with admin privileges
- **NSFW Filtering**: Requires ComfyUI-Usgromana extension with NSFW API enabled

---

## Data Storage

All gallery data is stored in the extension's own directory structure:

```
ComfyUI-Usgromana-Gallery/
├── data/
│   ├── metadata.json    # User-edited metadata
│   ├── ratings.json     # Legacy ratings (merged with metadata)
│   └── settings.json    # Gallery settings
```

**Note**: Data files are stored separately from image files to keep the output directory clean. Metadata is also embedded in image files for portability.

**Window State Storage:**
- Window position, size, and pin state are stored in browser localStorage
- State persists across sessions when window is unpinned

---

## Keyboard Shortcuts

- **Arrow Left/Right**: Navigate between images in detailed view
- **Escape**: Close detailed view or metadata panel
- **Enter**: Save changes when editing metadata fields
- **Escape** (while editing): Cancel changes to metadata fields

---

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

Modern browsers with JavaScript ES6+ support required.

---

## Support and Contributing

For issues, feature requests, or contributions, please refer to the project repository.

---

## License

[Add your license information here]
