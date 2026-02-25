# ComfyUI-JK-TextTools

Text and data manipulation nodes for ComfyUI, with emphasis on JSON processing, detection workflows, and bbox visualization.

## Features

- **Text Manipulation:** Split, join, and index delimited strings with type casting
- **JSON Processing:** Format and query JSON data with wildcard filtering
- **Detection Workflows:** Extract and visualize bounding boxes from detection results
- **Mask Generation:** Convert bboxes and segmentations to masks for image processing
- **Segmentation Support:** Process SEGS format from SAM3 with filtering and union capabilities
- **Mask to BBox Conversion:** Convert masks back to bounding boxes for chaining workflows

## Installation

### Via ComfyUI Manager (Recommended)
*(When published)*
1. Open ComfyUI Manager
2. Search for "JK-TextTools"
3. Click Install

### Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Nakamura2828/ComfyUI-JK-TextTools.git
   ```

3. Restart ComfyUI

## Nodes

### Text Manipulation

#### String Index Selector
Extract a single element from a delimited string by index - perfect for loop workflows.

**Inputs:**
- `text` (STRING): The delimited string to split
- `delimiter` (STRING): Character(s) to split on (default: `,`)
- `index` (INT): Which item to extract (0-based by default)
- `output_type` (STRING/INT/FLOAT): Type to cast result to
- `strip_whitespace` (BOOLEAN): Remove leading/trailing spaces
- `zero_indexed` (BOOLEAN, optional): Use 0-based indexing

**Outputs:**
- `selected_item`: The extracted item (typed)
- `item_count` (INT): Total number of items

**Example:**
```
Input: "10,25,42,100", delimiter: ",", index: 2, output_type: INT
Output: 42 (as integer)
```

#### String Splitter
Split a delimited string into a typed list with optional casting.

**Inputs:**
- `text` (STRING): The delimited string
- `delimiter` (STRING): What to split on
- `output_type` (STRING/INT/FLOAT): Type to cast items to
- `strip_whitespace` (BOOLEAN): Clean up items
- `remove_empty` (BOOLEAN, optional): Remove empty strings

**Outputs:**
- `string_list` (LIST): List of typed items
- `item_count` (INT): Number of items

**Features:**
- Type casting to STRING, INT, or FLOAT
- Escape sequence support (`\n`, `\t`, `\r`)
- Empty string handling
- Grid icon displays correctly (OUTPUT_IS_LIST working)

#### List Index Selector
Extract an item from a list by index with type preservation.

**Inputs:**
- `list_input` (*): Any list (connect from String Splitter)
- `index` (INT): Which item to extract
- `zero_indexed` (BOOLEAN): 0-based or 1-based indexing

**Outputs:**
- `selected_item`: The selected item (type-preserving)
- `list_length` (INT): Total list size

#### String Joiner
Join list items into a delimited string.

**Inputs:**
- `list_input` (*): Any list
- `delimiter` (STRING): String to insert between items (supports escape sequences)

**Outputs:**
- `joined_string` (STRING): The combined string
- `item_count` (INT): Number of items joined

**Escape Sequences:** Supports `\n`, `\t`, `\r`, `\\`

### JSON Processing

#### JSON Pretty Printer
Format JSON strings with proper indentation for readability.

**Inputs:**
- `json_string` (STRING): Raw JSON to format
- `indent` (INT): Number of spaces for indentation (0-8)
- `sort_keys` (BOOLEAN, optional): Alphabetically sort object keys

**Outputs:**
- `formatted_json` (STRING): Pretty-printed JSON
- `is_valid` (BOOLEAN): Whether JSON is valid
- `error_message` (STRING): Error details if invalid

**Example:**
```
Input: [{"detect_result":[{"class":"DOG","score":0.9}]}]
Output: (formatted with indentation and newlines)
```

#### Detection Query
Query detection results with class filtering, score thresholds, and wildcards.

**Inputs:**
- `json_string` (STRING): JSON containing detection results
- `class_filter` (STRING): Class name with wildcards (default: `*`)
- `min_score` (FLOAT, optional): Minimum confidence score
- `max_results` (INT, optional): Maximum results to return
- `categorization_field` (STRING, optional): Field name to extract

**Outputs:**
- `filtered_json` (STRING): Filtered results as JSON
- `match_count` (INT): Number of matches
- `detection_list` (LIST): Individual detections for iteration
- `bbox_list` (LIST): List of bboxes for visualization
- `categorization_value` (*): Extracted field value
- `is_valid` (BOOLEAN): Whether JSON is valid
- `error_message` (STRING): Error details if invalid

**Wildcard Examples:**
- `CLASS1_LABEL` → Exact match
- `CLASS1_*` → All CLASS1 subclasses
- `*_LABEL` → All ending with _LABEL
- `*` → All detections

**Use Case:** Filter detections, extract bboxes for visualization

### BBox and Mask Operations

#### Detection to BBox
Extract bounding box from a detection object.

**Inputs:**
- `detection` (STRING): JSON string of detection object
- `bbox_key` (box/bbox): Which key contains the bbox

**Outputs:**
- `bbox` (BBOX): Bounding box in format `[[x, y, width, height]]`
- `x`, `y`, `width`, `height` (INT): Individual components
- `class_name` (STRING): Detection class
- `score` (FLOAT): Confidence score

**Format:** Works with detection objects containing `"box": [x, y, w, h]` or `"bbox": [x, y, w, h]`

#### JSON to BBox
Convert JSON bbox arrays to BBOX format with coordinate system conversion.

**Inputs:**
- `json_string` (STRING): JSON array of bboxes (e.g., from SAM3 Segmentation)
- `input_format` (XYXY/XYWH): Format of bboxes in JSON
- `output_format` (XYXY/XYWH): Format to output

**Outputs:**
- `bboxes` (LIST of BBOX): Converted bboxes in format `[[[x,y,w,h]], ...]`
- `bbox_count` (INT): Number of bboxes

**Coordinate Formats:**
- **XYXY**: Two corners `[x1, y1, x2, y2]` - used by SAM3 and other models
- **XYWH**: Corner + dimensions `[x, y, width, height]` - standard format

**Example Input (SAM3 format):**
```json
[[245.3, 167.8, 512.6, 389.2], [100.0, 200.0, 300.0, 400.0]]
```

**Use Case:** Convert bbox output from nodes like TBG SAM3 Segmentation to work with mask generation nodes

#### BBox to Mask
Convert a single bounding box to a binary mask. Simple 1:1 conversion.

**Inputs:**
- `bbox` (BBOX): Single bbox `[[x, y, w, h]]`
- `width` (INT): Image width
- `height` (INT): Image height
- `invert` (BOOLEAN, optional): Invert mask (bbox black, rest white)

**Outputs:**
- `mask` (MASK): Binary mask for the bbox

**Features:**
- Simple single bbox → single mask conversion
- When connected to OUTPUT_IS_LIST sources, ComfyUI automatically iterates
- Handles both wrapped `[[x,y,w,h]]` and unwrapped `[x,y,w,h]` formats
- Automatic coordinate clamping to image bounds

**Use Case:** Single bbox to mask conversion. For multiple bboxes with union/combined mask, use BBoxes to Mask instead.

#### BBoxes to Mask ⭐ RECOMMENDED
Convert a list of bounding boxes to binary masks with union functionality.

**Inputs:**
- `bboxes` (*): List of bboxes from Detection Query or JSON to BBox
- `width` (INT): Image width
- `height` (INT): Image height
- `invert` (BOOLEAN, optional): Invert mask (bbox black, rest white)

**Outputs:**
- `combined_mask` (MASK): Union of all bboxes in one mask
- `individual_masks` (LIST of MASK): One mask per bbox
- `bbox_count` (INT): Number of bboxes processed

**Features:**
- Properly creates union mask (combined_mask) from multiple bboxes
- Individual masks for per-bbox processing
- Automatic coordinate clamping to image bounds
- Handles both wrapped and unwrapped bbox formats

**Format:** Accepts `[[[x,y,w,h]], [[x,y,w,h]], ...]` from Detection Query's bbox_list output or JSON to BBox

#### Mask to BBox ⭐ NEW
Convert a binary mask to a bounding box.

**Inputs:**
- `mask` (MASK): Binary mask tensor

**Outputs:**
- `bbox` (BBOX): Bounding box in format `[[x, y, width, height]]`
- `x`, `y`, `w`, `h` (INT): Individual integer coordinates

**Features:**
- Converts mask to tight bounding box
- Uses 0.5 threshold for float masks
- Floors all coordinates to integers
- Handles batched masks (uses first mask)
- Handles irregular shapes (L-shapes, non-convex masks)
- Returns [0,0,0,0] for empty masks

**Use Case:** Convert mask outputs (from detector nodes that output masks instead of proper BBOX type) to bbox format. Can chain output to other bbox nodes like BBox to SAM3 Query.

**Example:**
```
Mask (256x256)
  ↓
Mask to BBox
  ↓
bbox: [[50, 60, 100, 80]]
x: 50, y: 60, w: 100, h: 80 (all INT)
  ↓
BBox to SAM3 Query (chainable)
```

#### SEGs to Mask
Convert SEGS (segmentation results) to binary masks with filtering and union capabilities.

**Inputs:**
- `segs` (SEGS): Segmentation results from TBG SAM3 Segmentation or similar nodes
- `label_filter` (STRING, optional): Wildcard pattern for label filtering (default: `*`)
- `min_confidence` (FLOAT, optional): Minimum confidence threshold (0.0-1.0, default: 0.0)
- `min_area_percent` (FLOAT, optional): Minimum mask area as percentage of image (0.0-100.0, default: 0.0)
- `sort_order` (default/x_then_y/y_then_x/confidence_high_to_low, optional): Order segments deterministically
- `union_same_labels` (BOOLEAN, optional): Combine segments with same label (default: True)
- `invert` (BOOLEAN, optional): Invert mask (mask areas black, rest white)

**Outputs:**
- `combined_mask` (MASK): Union of all filtered segments
- `individual_masks` (LIST of MASK): One mask per label (when union enabled) or per segment
- `labels_info` (LIST of STRING): Label and confidence info (e.g., "person_0: 0.95")
- `seg_count` (INT): Number of masks returned

**SEGS Format:**
```python
((height, width), [SEG(...), SEG(...), ...])
```

Each SEG object contains:
- `cropped_mask`: numpy array with mask data
- `crop_region`: [x1, y1, x2, y2] placement coordinates
- `label`: string label (e.g., "person_0")
- `confidence`: float confidence score

**Features:**
- **Label Filtering:** Use wildcards to filter by label (`person_*`, `*_LABEL`, etc.)
- **Confidence Filtering:** Remove low-confidence segments
- **Area Filtering:** Remove tiny masks below percentage threshold (e.g., 5.0 for 5% of image)
- **Union Same Labels:** Combines all segments with same label into one mask (default)
  - Uses max confidence score for combined segments
  - Example: 3x "person_0" segments → 1 "person_0" mask
- **Deterministic Sorting:** Order segments by position (x_then_y or y_then_x)
- **Robust Handling:** Gracefully handles None cropped_masks and invalid data

**Wildcard Examples:**
- `*` → All segments (default)
- `person_*` → All person detections
- `*_0` → All first instances of each class
- `dog` → Exact match only

**Sort Order Options:**
- `default` → Keep original order from SEGS
- `x_then_y` → Left-to-right, then top-to-bottom
- `y_then_x` → Top-to-bottom, then left-to-right
- `confidence_high_to_low` → Sort by confidence score (highest first) ⭐ NEW

**Use Case:** Convert SAM3 segmentation results to masks for image processing workflows

#### SEGs to SAM3 Query ⭐ NEW
Convert SEGS segmentation format to SAM3 Selector query formats.

**Inputs:**
- `segs` (SEGS): Segmentation results from TBG SAM3 Segmentation or similar nodes

**Outputs:**
- `box_query` (STRING): JSON array with bounding box for SAM3 Selector `[{"x1": 10, "y1": 20, "x2": 100, "y2": 150}]`
- `point_query` (STRING): JSON array with weighted centroid `[{"x": 55, "y": 85}]`

**Features:**
- Generates both box and point queries for SAM3 Selector node
- Weighted centroid calculation for accurate point queries
- Handles multiple segments with union masks
- Coordinates clamped to image bounds
- Works with both ImpactPack and TBG SAM3 SEGS formats
- Handles numpy array and tensor masks
- Returns empty arrays `[]` for invalid inputs

**Use Case:** Chain SEGS segmentation output to SAM3 Selector for iterative refinement or re-segmentation.

**Example Workflow:**
```
TBG SAM3 Segmentation
  ↓
segs output → ((512, 512), [SEG(...), SEG(...), ...])
  ↓
SEGs to SAM3 Query
  ↓
box_query: [{"x1": 100, "y1": 200, "x2": 300, "y2": 400}]
point_query: [{"x": 200, "y": 300}]
  ↓
TBG SAM3 Selector
  - box_coords: box_query
  - point_coords: point_query
  ↓
Refined segmentation
```

**Example Workflow:**
```
TBG SAM3 Segmentation
    ↓
segs output → ((512, 512), [SEG(...), SEG(...), ...])
    ↓
SEGs to Mask
  - label_filter: "person_*"
  - min_confidence: 0.7
  - min_area_percent: 5.0
  - union_same_labels: True
    ↓
combined_mask → Mask of all detected persons
individual_masks → One mask per unique person
labels_info → ["person_0: 0.95", "person_1: 0.87"]
```

## Workflow Examples

### Example 1: Frame Number Extraction (Original Use Case)
```
VHS Node → "10,25,42,100"
    ↓
String Index Selector
  - delimiter: ","
  - index: 2 (from loop)
  - output_type: INT
    ↓
Output: 42 (as integer)
    ↓
Save Image: "frame_42.png"
```

### Example 2: Detection Visualization
```
Detection JSON
    ↓
JSON Pretty Printer (format for readability)
    ↓
Detection Query
  - class_filter: "DOG_*"
  - min_score: 0.7
    ↓
bbox_list output → [[[x,y,w,h]], [[x,y,w,h]], ...]
    ↓
BBoxes to Mask
  - width: 512
  - height: 512
    ↓
combined_mask → Apply to original image
individual_masks → Process each detection separately
```

### Example 2b: SAM3 Segmentation to Mask
```
TBG SAM3 Segmentation Node
    ↓
boxes output (JSON) → "[[x1,y1,x2,y2], [x1,y1,x2,y2], ...]"
    ↓
JSON to BBox
  - input_format: XYXY
  - output_format: XYWH
    ↓
bboxes output → [[[x,y,w,h]], [[x,y,w,h]], ...]
    ↓
BBoxes to Mask
  - width: 1024
  - height: 1024
    ↓
combined_mask → Apply to original image
```

### Example 3: Typed List Processing
```
"10,25,42,100"
    ↓
String Splitter
  - output_type: INT
    ↓
[10, 25, 42, 100] (actual integers)
    ↓
List Index Selector
  - index: 2
    ↓
Output: 42 (as int, not string)
    ↓
Can connect directly to nodes expecting INT
```

### Example 4: Multi-line Text Processing
```
Multiline Text Input
    ↓
String Splitter
  - delimiter: \n
    ↓
List of lines
    ↓
String Joiner
  - delimiter: ", "
    ↓
Comma-separated output
```

## Development

### Running Tests
```bash
# Individual tests
python tests/test_string_splitter.py

# All tests at once
python tests/run_all_tests.py
```

### Requirements
- Python 3.10+
- ComfyUI
- PyTorch (for mask generation)

See `requirements.txt` for development dependencies.

## Technical Notes

### BBox Format
Standard format used throughout: `[[x, y, width, height]]`
- Single bbox: `[[100, 200, 50, 75]]`
- Multiple bboxes: `[[[x1,y1,w1,h1]], [[x2,y2,w2,h2]], ...]`
- Coordinates are XYWH (top-left corner + dimensions)

**Alternative Coordinate Systems:**
- **XYXY**: Two corners `[x1, y1, x2, y2]` - used by some detection models (SAM3, etc.)
- **XYWH**: Corner + dimensions `[x, y, width, height]` - our standard format
- Use JSON to BBox node to convert between these formats

### OUTPUT_IS_LIST
Nodes using OUTPUT_IS_LIST show grid icon in ComfyUI and output items for iteration:
- String Splitter: `string_list`
- List Index Selector: receives lists
- Detection Query: `detection_list`, `bbox_list`
- BBoxes to Mask: `individual_masks`

### Type Preservation
List Index Selector preserves input types:
- String list → Returns strings
- Int list → Returns ints
- Float list → Returns floats

## Compatibility

### Cross-Package Support
- **Works with:** ImpactPack (with type converter if needed)
- **Works with:** KJNodes BBox Visualizer
- **Works with:** TBG SAM3 Segmentation (via JSON to BBox node for bboxes, SEGs to Mask for segmentations)
- **Works with:** Standard ComfyUI mask nodes

**Verified Workflows:**
- TBG SAM3 → JSON to BBox → BBoxes to Mask ✅
- TBG SAM3 → SEGs to Mask (full SEGS support) ✅

## Roadmap

### Current Features ✅
- [x] Text splitting and joining with type casting
- [x] List indexing with type preservation
- [x] JSON formatting and validation
- [x] Detection querying with wildcards and bbox extraction
- [x] BBox extraction from detection objects
- [x] JSON bbox array conversion with XYXY/XYWH support
- [x] Mask generation from bboxes (union and individual)
- [x] SEGS segmentation to mask conversion with filtering and union
- [x] Escape sequence support
- [x] Comprehensive test suite (95%+ coverage)

### Future Enhancements
- [ ] CSV Parser node
- [ ] JSONPath query support
- [ ] Regular expression nodes
- [ ] Additional bbox formats (XYXY, center-based)
- [ ] Mask operations (union, intersection, difference)
- [ ] String templating/formatting

## License

MIT License

## Author

John Knox (Nakamura2828)

## Contributing

Issues and pull requests welcome!

## Support

If you find these nodes useful, please star the repository on GitHub!

## Changelog

### v1.2.0 (2026-01-18)
- **NEW: Mask to BBox Node** - Convert masks to bounding boxes
  - Converts binary masks to BBOX format in XYWH coordinates
  - Outputs both BBOX type and individual x,y,w,h as INT values
  - Uses 0.5 threshold for float masks
  - Handles batched masks (uses first), irregular shapes, empty masks
  - All coordinates floored to integers
  - 12 comprehensive test cases
  - Use case: Convert mask outputs to bbox format for chaining to other nodes
- **NEW: SEGs to SAM3 Query Node** - Convert SEGS to SAM3 Selector queries
  - Generates box_query (bounding box) and point_query (centroid) for SAM3 Selector
  - Weighted centroid calculation for accurate point queries
  - Handles multiple segments with union masks
  - Full ImpactPack and TBG SAM3 compatibility
  - 12 comprehensive test cases covering all features
  - Use case: Chain SEGS segmentation to SAM3 Selector for iterative refinement
- **ENHANCED: SEGs to Mask Node** - Added confidence sorting
  - New sort_order option: "confidence_high_to_low"
  - Sorts output masks by confidence score (highest first)
  - Handles numpy array confidence values (ImpactPack compatibility)
  - Updated tests: 18 test cases (was 17)

### v1.1.0 (2026-01-17)
- **NEW: SEGs to Mask Node** - Convert SEGS segmentation format to masks
  - Full support for TBG SAM3 Segmentation node output
  - Wildcard label filtering (fnmatch patterns)
  - Confidence threshold filtering (min_confidence)
  - Area percentage filtering (min_area_percent) to remove tiny masks
  - Deterministic sorting options (default/x_then_y/y_then_x)
  - Union same labels feature (combines segments with same label, uses max confidence)
  - Invert mode support
  - 4 outputs: combined_mask, individual_masks (list), labels_info (list), seg_count
  - Comprehensive tests: 16 test cases covering all features
  - Robust handling of None masks and invalid data

### v1.0.1 (2026-01-17)
- **BBox to Mask Refactored:** Simplified to single bbox → single mask converter
  - Removed combined_mask output (use BBoxes to Mask for union functionality)
  - Renamed individual_masks output to just "mask"
  - Removed OUTPUT_IS_LIST - works as standard 1:1 converter
  - ComfyUI now iterates automatically when connected to list sources
  - Updated tests: 14 test cases validating simplified behavior
  - No longer marked EXPERIMENTAL - clean, focused implementation

### v1.0.0 (2026-01-17)
- Initial release with 10 working nodes (now 11 with SEGs to Mask in v1.1.0)
- **Text Manipulation (4 nodes):**
  - String Index Selector, String Splitter, List Index Selector, String Joiner
  - Full type casting support (STRING/INT/FLOAT)
  - Escape sequence support
- **JSON Processing (2 nodes):**
  - JSON Pretty Printer with validation
  - Detection Query with wildcard filtering and bbox extraction
- **BBox & Mask Operations (4 nodes):**
  - Detection to BBox - Extract from detection objects
  - JSON to BBox - Convert JSON arrays with XYXY/XYWH conversion
  - BBoxes to Mask - Create union and individual masks (RECOMMENDED)
  - BBox to Mask - Simple 1:1 bbox to mask converter
- Comprehensive test suite (95%+ coverage)
- Full documentation (README.md + CLAUDE.md)
- Verified integrations with SAM3, KJNodes, ImpactPack