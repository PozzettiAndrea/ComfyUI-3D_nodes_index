# ComfyUI-SkeletonRetarget

![Demo Offset](Offset.gif)

A custom node pack for ComfyUI that aligns and retargets skeletal pose data from a driving video sequence to match the body proportions and position of a reference image. This enables consistent motion transfer for AI video generation (e.g., AnimateDiff, Vid2Vid) by eliminating pose mismatch issues.

## 🌟 Features

-   **Pose Extraction**: Convert standard pose keypoints (from DWPose/OpenPose estimators) into high-precision skeleton tensors.
-   **Intelligent Tracking**: Built-in simple person tracking to follow a specific subject across video frames.
-   **Automatic Retargeting**: Compute scale and rotation transforms to map a driving skeleton to a reference skeleton using configurable anchors (Hips, Shoulders, Torso, etc.).
-   **Vectorized Transformation**: Fast, GPU-accelerated application of transforms to entire pose sequences.
-   **Visualization**: Render retargeted skeletons back to OpenPose-style control images with correct coloring and topology (supports COCO-18, BODY-25, and COCO-133).

## 📦 Installation

1.  Navigate to your ComfyUI custom nodes directory:
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/cedarconnor/ComfyUI-Skeletonretarget.git
    ```
3.  Restart ComfyUI.

## 🛠️ Usage Workflow

### Basic Retargeting Pipeline

1.  **Extract Reference Skeleton**:
    -   Load your **Reference Image**.
    -   Pass it through a **DWPose Estimator** (or similar).
    -   Connect the output validation `pose_keypoint` to the `ExtractSkeletonFromPose` node.

2.  **Extract Driving Skeleton Sequence**:
    -   Load your **Driving Video**.
    -   Pass it through the estimator.
    -   Connect output to `ExtractSkeletonFromPose`.
    -   *Tip: Use `person_selection="track"` if there are multiple people.*

3.  **Compute Transform**:
    -   Add `ComputeRetargetTransform` node.
    -   Connect **Reference Skeleton** (from step 1) and **Driving Skeleton** (from step 2).
    -   Select `anchor_mode` (e.g., `hips` or `auto`).
    -   Enable `enable_scale` to match proportions.

4.  **Apply Transform**:
    -   Add `ApplyRetargetTransform` node.
    -   Connect the **Driving Skeleton Sequence** and the **Transform** (from step 3).

5.  **Visualize / Export**:
    -   Add `SkeletonToOpenPoseImage` node.
    -   Connect the **Retargeted Sequence**.
    -   Set desired resolution (e.g., 512x512 or match your video).
    -   Connect the output `IMAGE` to a Preview or Video Combine node, or use it as input for ControlNet.

## 🧩 Nodes

### Extraction
-   **`Extract Skeleton From Pose`**:
    -   `pose_data`: Input from DWPose/OpenPose.
    -   `track`: Enable temporal coherence for video.

### Transform
-   **`Compute Retarget Transform`**:
    -   Calculates the offset, scale, and rotation between two skeletons.
    -   `anchor_mode`: Determines which body part is used as the center of alignment.
-   **`Apply Retarget Transform`**:
    -   Applies the calculated transform to a sequence of skeletons.
    -   `bounds_mode`: Options to clamp or handle points going off-screen (`none`, `clamp`, `scale_to_fit`).

### Visualization
-   **`Skeleton To OpenPose Image`**:
    -   Renders the skeleton data into the colorful OpenPose format expected by ControlMaps.
    -   Supports `COCO-133` (Hands/Face), `COCO-18`, and `BODY-25`.

## 🤝 License

MIT License.
