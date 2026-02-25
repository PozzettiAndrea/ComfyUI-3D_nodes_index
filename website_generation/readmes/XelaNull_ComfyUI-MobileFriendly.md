# ComfyUI-MobileFriendly

Comprehensive mobile UI enhancement for ComfyUI. Transforms the desktop-focused interface into a touch-friendly experience optimized for iPhone, iPad, and Android devices.

**Version:** 6.2

## Why Use MobileFriendly?

Vanilla ComfyUI on mobile has several pain points:
- **Cluttered UI**: Floating Run button box and horizontal action bar waste precious screen space
- **Accidental Browser Zoom**: Pinch gestures zoom the entire page instead of just the canvas
- **Tiny Touch Targets**: Context menus and buttons are too small for finger taps
- **Keyboard Pop-ups**: Zoom percentage input opens a keyboard instead of a slider
- **Hidden Sidebar**: The sidebar button blends in with other buttons

MobileFriendly solves all of these while preserving full functionality.

## Features

### 1. Clean Mobile Canvas

**Problem**: On mobile, you see a floating "Run" button box with drag handle and X button, plus a horizontal action bar at the top. These clutter the limited screen space.

**Solution**: MobileFriendly hides these elements on mobile/tablet while keeping all functionality accessible via the sidebar Menu button.

| Hidden Element | What It Is |
|---------------|-----------|
| `.actionbar-container` | Horizontal action bar at top |
| `.p-panel` with `.queue-button-group` | Floating Run/Queue button box |
| `.drag-handle` | Drag handle on floating panels |

**Critical Implementation Note**: We use **JavaScript-only hiding**, not CSS `display:none` rules. Early versions used CSS like `.comfy-menu { display: none }` which caused workflow tabs to disappear on iPhone (the tabs were nested inside hidden parent containers).

### 2. Workflow Tabs Preserved

**Problem**: CSS blanket hiding rules (e.g., `div.no-drag { display: none }`) accidentally hide workflow tabs on iPhone because tabs are nested inside these containers.

**Solution**: The `preserve()` function explicitly protects workflow tabs and their parent elements:

```javascript
const preserve = (el) => {
  // Protect workflow tabs (all variations)
  if (cls.includes('workflow-tab')) return true;
  if (cls.includes('p-togglebutton')) return true;
  if (el.closest('.workflow-tabs')) return true;
  // ...
};
```

Tested on: iPhone 13 Pro, iPad Pro, MacBook Safari

### 3. Distinctive Sidebar Menu Button

**Problem**: The MobileFriendly menu button looks identical to other sidebar buttons.

**Solution**: Cyan/teal gradient styling with glow effect, positioned at top of sidebar:

```css
.side-bar-button.mf-menu-button {
  background: linear-gradient(135deg, #00BCD4, #0097A7) !important;
  border: 2px solid #00E5FF !important;
  box-shadow: 0 0 8px rgba(0, 188, 212, 0.5) !important;
}
```

**Note**: The sidebar uses `flex-direction: column-reverse`, so we use `appendChild()` to place the button at the visual top.

### 4. Browser Zoom Prevention (Canvas Zoom Preserved)

**Problem**: Pinch gestures on mobile zoom the entire browser page, making the UI unusable. But we WANT pinch-to-zoom on the canvas.

**Solution**: Three-layer approach:

1. **Viewport Meta Tag**: `user-scalable=no, maximum-scale=1.0`
2. **CSS `touch-action`**:
   - `pan-x pan-y` on html/body (scroll but no zoom)
   - `none` on canvas (LiteGraph handles its own zoom)
3. **JavaScript Gesture Interception**: Blocks Safari gesture events except on canvas

```javascript
// Block multi-finger gestures except on canvas
document.addEventListener('touchmove', (e) => {
  if (e.touches.length > 1) {
    if (!target.closest('canvas')) {
      e.preventDefault();
    }
  }
}, { passive: false });
```

### 5. Touch-Friendly Zoom Slider

**Problem**: Tapping the zoom percentage in the bottom bar opens a keyboard for text input - unusable on mobile.

**Solution**: Intercept touch on zoom controls and show a floating slider overlay:

- Large touch-friendly slider (40px height)
- Live percentage display (24px bold text)
- Quick buttons: "Fit", "100%", "Close"
- Closes on tap outside

The slider controls `app.canvas.ds.scale` directly for real-time canvas zoom.

### 6. Compact UI Elements

#### Bottom Bar
- Max height: 48px (down from default)
- Reduced padding: 2px 4px
- Smaller font: 11px
- All elements max-height: 32px

#### Sidebar
- Width: 34px on mobile (down from 48px)
- Item height: 34px
- Gap: 1px between items
- Labels hidden on mobile

#### Workflow Tabs
- Min width: 60px (mobile), 50px (phone)
- Font size: 11px (mobile), 10px (phone)

### 7. Mobile Menu Sidebar Tab

Consolidates all essential controls into a single sidebar panel:

```
QUEUE
[−] [1] [+] [▶ Queue] [✕]
[📋 Queue/History]
[🔧 Manager] [📤 Share]

WORKFLOW
[💾 Save] [📂 Load]
[📄 New]  [🔄 Default]
```

**Queue Count Feature**: The [−] [+] buttons let you batch queue multiple generations (1-99).

### 8. Touch-Friendly Targets

Following Apple/Google guidelines (44px minimum):

| Element | Min Height |
|---------|-----------|
| Buttons | 44px |
| Inputs | 44px |
| Context menu items | 48px |
| Splitter gutters | 12px wide |

### 9. Progress Bar Mobile Styling

- Max width: 90vw
- Word wrap enabled
- Font size: 10-11px
- Centered text

### 10. iOS Safari Optimizations

- Input font size 16px (prevents auto-zoom on focus)
- Touch-friendly scrolling with momentum (`-webkit-overflow-scrolling: touch`)
- Disabled hover states on touch devices (prevents sticky hover)
- Tap feedback: `transform: scale(0.98)` on active

### 11. Long-Press to Move Nodes

**Problem**: On mobile, accidentally touching a node while scrolling the canvas would start dragging it, causing frustration and misplaced nodes.

**Solution**: Nodes require a 350ms long-press before they can be moved:

1. **Touch a node** - Nothing happens immediately (you can scroll freely)
2. **Hold for 350ms** - Phone vibrates, toast shows "✓ Move node"
3. **Drag to position** - Node follows your finger
4. **Release** - Drag mode disabled until next long-press

```javascript
// Implementation uses LiteGraph's allow_dragnodes property
app.canvas.allow_dragnodes = false;  // Default: disabled on mobile

// After 350ms long-press:
app.canvas.allow_dragnodes = true;   // Enable dragging
navigator.vibrate([50]);             // Haptic feedback
```

This prevents accidental node movement while preserving full drag functionality when intended.

### 12. Zoom Button (Mobile)

**Problem**: The native zoom percentage input opens a keyboard on mobile, making it difficult to adjust canvas zoom.

**Solution**: A dedicated "🔍 Zoom" button in the bottom bar opens a touch-friendly slider overlay:

- Large slider (40px height) for easy thumb control
- Live percentage display
- Quick buttons: "Fit", "100%", "Close"
- Range: 10% to 200%

## Installation

### Via ComfyUI Manager
Search for "MobileFriendly" in the ComfyUI Manager.

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/ComfyUI-MobileFriendly.git
```

Restart ComfyUI after installation.

## Configuration

The extension is enabled by default. To toggle:

1. Open ComfyUI Settings (gear icon)
2. Find "MobileFriendly: Enable compact mobile UI"
3. Toggle on/off as desired

## Breakpoints

| Breakpoint | Target Devices | Key Changes |
|------------|----------------|-------------|
| > 1024px | Desktop | Minimal changes (sidebar compacting only) |
| 768-1024px | Tablets | Reduced sidebar, hidden floating UI |
| 480-768px | Mobile landscape | Compact everything, zoom slider |
| < 480px | Mobile portrait | Full-screen modals, smallest UI |
| `pointer: coarse` | Any touch device | 48px touch targets, no hover |

## Debug Badge

On mobile devices, a green badge appears at bottom-left showing:

```
MF5.2 R:2 [actionbar,p-panel,tabs:3]
```

- `MF5.2`: Version number
- `R:2`: Number of elements hidden
- `[...]`: What was hidden + workflow tab count

This confirms the extension is loaded and working.

## Troubleshooting

### Workflow Tabs Missing on iPhone

This was fixed in v4.5. If tabs disappear:
1. Check you have version 4.5+ (see debug badge)
2. Clear browser cache completely
3. Force refresh (hold reload button on iPhone)

**Root Cause**: Earlier versions used CSS `display:none` on `.comfy-menu` and `div.no-drag` which accidentally hid parent containers of workflow tabs.

### Floating Run Button Still Visible

The JS hiding runs every 500ms for 30 seconds to catch Vue async renders. If still visible:
1. Check debug badge shows `R:` count > 0
2. Try refreshing the page
3. Check browser console for `[MobileFriendly]` logs

### Zoom Slider Not Appearing

The slider is only enabled on mobile (width <= 1024px or touch device). On desktop, the text input works normally.

## CSS Variables

```css
:root {
  --mf-sidebar-width: 40px;      /* Desktop sidebar width */
  --mf-sidebar-item-height: 44px; /* Desktop item height */
}

@media (max-width: 768px) {
  :root {
    --mf-sidebar-width: 34px;
    --mf-sidebar-item-height: 34px;
  }
}
```

## Compatibility

- ComfyUI 0.8.0+
- Works with: ComfyUI Manager, rgthree-comfy, Easy-Use, and other popular extensions
- Tested on: iOS Safari, Chrome Android, desktop browsers
- Tested devices: iPhone 13 Pro, iPad Pro, MacBook Safari

## Technical Details

### Two Menu Systems in ComfyUI

ComfyUI has two different menu systems:

| Menu Type | CSS Class | When Used |
|-----------|-----------|-----------|
| Old Floating Menu | `.comfy-menu` | Settings: "Use new menu" = "Disabled" |
| New Vue Menu | `.comfyui-body-top` | Settings: "Use new menu" = "Top" (default) |

MobileFriendly handles both by targeting the specific elements that should be hidden, not blanket parent containers.

### Mobile Detection

```javascript
const isMobile = () => {
  return window.innerWidth <= 1024 ||
         window.matchMedia('(pointer: coarse)').matches ||
         /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
};
```

### Key Files

- `web/js/mobilefriendly.js` - Main extension (all logic in single file)
- No Python backend required
- No dependencies beyond ComfyUI core

## Credits

Created for the ShoudieFuser project by Max with Claude and Samantha.

## Changelog

### v6.2
- Fixed zoom slider interception - now targets `[data-testid="zoom-controls-button"]`
- Added CSS to compact bottom-right floating controls bar (`.p-buttongroup`)
- Added debug logging for long-press-to-move troubleshooting
- Made long-press code more robust with fallback property names

### v6.1
- Increased vertical padding between sidebar icons
- Shifted sidebar down to avoid overlapping workflow tabs (`margin-top: 50px`)
- Fine-tuned sidebar button spacing (`margin: 2px 0`, `padding: 6px`)

### v6.0
- Cleaned up sidebar CSS, removed forced positioning
- Kept visibility forcing to prevent sidebar disappearing

### v5.9
- **Critical fix**: Forced sidebar visibility with `!important` CSS
- Added explicit `display: flex`, `visibility: visible`, `opacity: 1` to sidebar

### v5.8
- Added dedicated "🔍 Zoom" button in bottom bar (more reliable than interception)
- Disabled node toolbar CSS that was causing sidebar issues

### v5.7
- **New feature**: Long-press to move nodes on mobile
  - Must hold finger 350ms before node can be dragged
  - Haptic feedback (vibration) when drag enabled
  - Visual toast "✓ Move node" confirmation
  - Prevents accidental node movement while scrolling

### v5.6
- Restored sidebar padding (was too squished in v5.5)
- Rewrote zoom interception with event delegation
- Improved tab navigation arrow selectors

### v5.5
- Added workflow tab navigation arrows (left/right)
- Node toolbar compacting CSS (later disabled in v5.8)
- Auto-focus prevention for search inputs on iPhone
- Reduced logs panel font size to 9px

### v5.4
- More aggressive zoom slider interception
- Hidden keyboard shortcuts icon on mobile (not useful for touch)
- Fixed Queue/History button to close sidebar before opening panel
- Reduced sidebar to 28px height (later reverted in v5.6)

### v5.3
- Fixed Job Queue panel overflow on iPhone (was slightly too wide)
- Added `max-width: 100vw` and text truncation to queue table cells

### v5.2
- Fixed `isMobile()` scope issue (function was used before definition)

### v5.1
- Added mobile zoom slider overlay
- Reduced bottom bar height/padding
- Reduced sidebar vertical spacing

### v4.9
- Reordered sidebar menu (Manager/Share below Queue)
- Added progress bar mobile CSS

### v4.8
- Added browser zoom prevention (canvas zoom preserved)
- Removed CSS blanket hiding rules

### v4.5
- **Critical fix**: Workflow tabs now preserved on iPhone
- Switched to JS-only hiding with `preserve()` function

### v4.4
- Cyan/teal gradient styling for menu button
- Button positioned at top of sidebar

### v3.x
- Initial floating UI hiding attempts
- CSS-based approach (caused workflow tab issues)
