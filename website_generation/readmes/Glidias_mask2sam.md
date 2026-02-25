# mask2sam
Mask to SAM2 segmentation

Converts any batch of grayscale MASK images consisting of any number of contiguous sets of masking shapes, (concave or convex or with holes) to a suitable "in-region" SAM2 (Segment-Anything 2) positive/negative point each. Ensures results are consistent given input vs output. By "suitable" point means the centroid within the largest area convex decomposed shape from the each masking shape itself. (Bayazit decomposition ensures the polygon fit is suitable for largest found convex portion of the polygon). Masking shapes can overlap each other (or by explicitly defining positive/negative shape pairs) by supplying seperate grayscale MASK images if needed be so these shapes don't occupy the same canvas.

Make sure your mask image inputs are lossless for this, to ensure exact intended colors are used as below:

- Black 0: Shape for positive point. (ie. Paint full black see-through transparent to indicate positive point)
- White 255: Do Nothing
- In-between ~(1 to 240): Shape for negative point (ie. Paint a faded translucent to indicate negative point)

The resulting outputs can be used for https://github.com/kijai/ComfyUI-segment-anything-2/ SAM2 segmentation


## MaskToPosNegPoints

- INPUT:
  - mask: A batch of masks to collect points.
  - individual_objects: Boolean to indicate if intending to feed into SAM2 process with "individual objects" mode turned on. For each mask in the batch, if this flagged is turned on and a specific mask happens to also contain negative points from in-between shapes, it will pair every positive shape point within that mask to the closest position marked by any negative shape point position within the same mask (if any). Thus, it's possible for multiple positive shapes to be paired to similar negative point positions if the nearest negative points for them are matching.

OUTPUT:
  - coordinates_positive:  String representing the json flat array of positive points in [{"x": ..., "y"...}] format collected across the entire batch
  - coordinates_negative: String representing the json flat array of negative points in [{"x": ..., "y"...}] format collected across the entire batch


## MaskToBBoxes

This one converts the mask shapes to bounding boxes in BBOX format to use for Kijac's SAM2 library

- INPUT:
  - mask: A batch of masks to collect bounding boxes.

OUTPUT:
  - bboxes
