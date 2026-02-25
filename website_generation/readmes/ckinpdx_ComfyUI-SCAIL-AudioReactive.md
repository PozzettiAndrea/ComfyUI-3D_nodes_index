# ComfyUI-SCAIL-AudioReactive

Generate audio-reactive SCAIL pose sequences for character animation without requiring input video tracking. Now supports **Multi-Character Choreography**, **AIST++ Motion Capture Dance Data**, and **CMU Motion Capture Library**.

## What it does

Creates SCAIL-compatible 3D skeleton pose renders driven by audio analysis. Instead of extracting poses from a driving video, this generates poses procedurally using:

1. **Beat detection** — Poses hit on musical beats
2. **Multi-Character Sync** — Orchestrate groups with Unison, Mirror, or Random interactions
3. **Physics Simulation** — Momentum, drag, and "Sticky Feet" constraints for grounded motion
4. **Auto-Rigging** — Automatically corrects "non-neutral" reference poses (e.g., character starting with foot up)
5. **Dynamic Scaling** — Adjusts movement amplitude based on character size/distance to prevent collisions
6. **AIST++ Dance Library** — Real motion capture dance data from professional dancers across 10 genres
7. **CMU Motion Library** — 2500+ general motion capture sequences (walk, run, jump, sports, interactions, and more)

## Nodes

### Audio Analysis
- **SCAILAudioFeatureExtractor** — Extracts per-frame RMS, bass, mid, treble, and onset features.
- **SCAILBeatDetector** — Detects beats, downbeats, and tempo from audio using librosa.

### Base Pose Generation
- **SCAILBasePoseGenerator** — Procedurally create 1 to 5 skeletons (T-pose, Active Idle) with adjustable spacing.
- **SCAILPoseFromDWPose** — Extract base poses from reference images. Supports **1:1 fidelity** for multiple characters (detects everyone in the image, no cloning).

### Animation
- **SCAILBeatDrivenPose** — The Choreographer. Generates physics-based dance sequences.
  - Supports **Interaction Modes** (Mirror, Unison, Random).
  - Handles **Anti-Jelly Bone** constraints to keep limbs rigid.
  - Includes **80+ Dance Poses** (Hip Hop, Rock, Pop, etc.)
- **SCAILAlignPoseToReference** — Align generated pose sequence to match reference position/scale.

### AIST++ Dance Library
Real motion capture data from the AIST++ dataset — professional dancers performing choreographed routines across 10 genres. Auto-downloads from HuggingFace on first use.

**Chunk-Based (Reactive):**
- **SCAILAISTLibraryLoader** — Loads the chunked dance library (~220MB, auto-downloads).
- **SCAILAISTBeatDance** — Beat-triggered chunk selection based on audio energy.
  - Mix multiple genres (break, pop, lock, etc.)
  - Energy-aware: low/mid/high energy chunks matched to audio
  - Chunks chain for longer sequences
  - **Note:** Can be janky at transitions since chunks are cut at velocity minimums, not perfect phrase boundaries. Good for variety and reactivity, less smooth than full sequences.
- **SCAILAISTChunkPreview** — Preview individual chunks by genre/energy.

**Full Sequence (Smooth):**
- **SCAILAISTFullLoader** — Loads full dance sequences (~200MB, auto-downloads).
- **SCAILAISTFullSequence** — Plays complete choreographed dances.
  - Single genre dropdown (no mixing)
  - Smooth, continuous motion from real performances
  - **Note:** Can feel repetitive if you recognize the source choreography. Best for shorter generations or when you want authentic, uncut dance motion.

**Available Genres:** break, pop, lock, waack, krump, house, street_jazz, ballet_jazz, la_hip_hop, middle_hip_hop

### CMU Motion Capture Library (NEW)
General motion capture from Carnegie Mellon University — 2548 motions across 16 categories including walking, running, jumping, dancing, sports, climbing, and two-person interactions. Auto-downloads from HuggingFace on first use (~660MB).

- **SCAILCMULibraryLoader** — Loads the CMU motion library.
  - Source: HuggingFace or local path
  - Auto-downloads on first use
- **SCAILCMUMotion** — Plays a single motion sequence. Chain multiple for choreographed sequences.
  - Category selection (walk, run, jump, dance, fight, sports, etc.)
  - Random or specific motion selection
  - Loop modes: none, loop, ping_pong
  - Proper locomotion drift (character moves across frame)
  - Chainable: connect pose_sequence_out → pose_sequence_in for multi-motion sequences
  - Frame count auto-calculated from motion length

**Available Categories:** walk (955), run (114), jump (165), dance (150), fight (70), sports (114), climb (31), interact (47), sit (32), crouch (7), gesture (17), swim (24), getup (18), fall (3), balance (2), misc (799)

**Two-Person Motions:** 55 paired interactions (handshakes, partner dances, etc.) with matching motion files.

### Rendering
- **SCAILPoseRenderer** — Render pose sequence to SCAIL-style 3D cylinder images.
- **SCAILPosePreview** — Visualize extracted audio features.
- **SCAILBeatPreview** — Visualize detected beats and energy.

## Installation

1. Clone to your ComfyUI custom_nodes folder:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/ckinpdx/ComfyUI-SCAIL-AudioReactive
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

Motion libraries download automatically on first use:
- AIST++ chunks: ~220MB
- AIST++ full sequences: ~200MB  
- CMU motions: ~660MB

## Parameters

### SCAILBasePoseGenerator
- `character_count` — Generate 1 to 5 procedural skeletons side-by-side.
- `spacing` — Distance between characters in world units.

### SCAILBeatDrivenPose

**Interaction & Style:**
- `dance_style`:
    - **auto**: Selects moves based on audio energy levels.
    - **hip_hop, rock, disco, etc**: Forces specific genre move sets.
- `interaction_mode`:
    - **unison**: All characters perform the exact same move at the same time.
    - **mirror**: Characters swap Left/Right moves based on the leader (Center/Left).
    - **random**: Every character picks a distinct move from the style bucket.
- `energy_style` — auto/low/medium/high.
- `motion_smoothness` — Higher = floatier/smoother. Lower = snappier/robotic.
- `anticipation` — Number of frames to start moving *before* the beat hits.

**Audio Modulation:**
- `groove_amount` — Intensity of the continuous hip sway/figure-8 loop.
- `bass_intensity` — Bass → vertical bounce (scaled to body size).
- `treble_intensity` — Treble → arm/hand jitter.

### SCAILAISTBeatDance (Chunk Mode)
- `sync_dancers` — All dancers do same moves (true) or independent (false).
- `genre_*` toggles — Enable/disable each of the 10 dance genres.
- `transition_frames` — Frames to blend between chunks (smooths transitions).
- `chunks_per_beat` — Chain consecutive chunks (1=0.5s, 2=1s, etc.).
- `energy_sensitivity` — How strongly audio energy affects chunk selection.

### SCAILAISTFullSequence (Full Sequence Mode)
- `genre` — Single genre dropdown.
- `transition_frames` — Frames to blend from reference pose to dance start.
- `start_beat` — Which beat in the source to start from (0=beginning).

### SCAILCMUMotion (CMU Motion)
- `category` — Motion category (walk, run, jump, dance, fight, sports, etc.).
- `selection_mode` — Random from category or specific motion ID.
- `motion_id` — Specific motion ID when using "specific" mode (e.g., "02_01").
- `transition_frames` — Frames to blend from previous pose/sequence.
- `loop_mode` — none (play once), loop (restart), ping_pong (reverse at end).
- `target_fps` — Output frame rate (source is 120fps, scaled to target).
- `scail_pose` — Optional reference pose for positioning/scaling.
- `pose_sequence_in` — Optional input from previous motion node for chaining.

**Outputs:**
- `pose_sequence` — Connect to next CMU Motion node or directly to Pose Renderer.
- `frame_count_out` — Total frames (useful for setting generation length).
- `motion_info` — Description of selected motion.

### SCAILPoseFromDWPose
- **Note:** This node strictly extracts what is detected in your reference image. It does not clone characters. To animate 3 people, you need a reference image with 3 people.

## Multi-Character Tips

If you are using a reference image with multiple people (e.g., a band or dance troupe), you must ensure your **Upstream DWPose/OpenPose Detector** actually finds them all.

1. **Resolution:** Set upstream detector resolution to **1024** or higher for group shots.
2. **Model:** Use **`dw-ll_ucoco.onnx`** (NOT the 384 variant) for the pose model, and **`yolo_nas_l_fp16.onnx`** or **`yolox_x.onnx`** for the BBox detector. Standard `yolox_l` often misses people in complex poses (e.g., arms touching) or back rows.
3. **Max People:** Ensure the upstream node allows `max_people > 1` (if using OpenPose).

## Motion Library Comparison

| Feature | Procedural | AIST++ Chunks | AIST++ Full | CMU Motion |
|---------|------------|---------------|-------------|------------|
| Motion Quality | Synthetic | Real mocap | Real mocap | Real mocap |
| Variety | 80+ poses | ~44k chunks | ~1400 sequences | 2548 motions |
| Categories | Dance only | 10 dance genres | 10 dance genres | 16 categories |
| Audio Reactivity | High | Medium | Low | None |
| Transitions | Smooth | Can be janky | Smooth | Smooth |
| Locomotion | Stationary | Stationary | Stationary | **Full drift** |
| Two-Person | No | No | No | **55 pairs** |
| Best For | Rhythmic loops | Reactive dance | Cinematic dance | Walking, actions, interactions |

## Workflow Examples

### CMU Motion Chain (Walk → Run → Jump)
```
[CMU Library] → [CMU Motion: walk] → [CMU Motion: run] → [CMU Motion: jump] → [Pose Render]
                      ↓                    ↓                    ↓
                 scail_pose          pose_sequence_in     pose_sequence_in
                 (from DWPose)
```

### Audio-Reactive Dance
```
[Audio] → [Beat Detector] → [AIST Beat Dance] → [Pose Render]
              ↓                    ↑
         [Feature Extractor]   [AIST Library]
```

## Technical Details

### "Sticky Feet" Physics
The custom `MotionDynamics` engine uses variable drag coefficients. Ankles have **0 drag** and **2x stiffness**, forcing them to snap to the floor position unless a specific dance move lifts them. This prevents the "floating" effect common in procedural animation.

### Neutral Structure Initialization (Auto-Rigging)
If your reference image has a character standing on one leg or mid-stride, the system calculates a mathematical "Neutral Standing" skeleton based on their bone lengths. The physics engine then interpolates from the Reference Pose -> Neutral Pose -> Dance Move, preventing the character from getting stuck in their initial pose (e.g., keeping one foot in the air).

### Scale-Aware Movement
Movements are normalized based on the character's torso length. A small character in the background will perform smaller absolute movements than a character in the foreground, maintaining correct perspective and preventing characters from colliding.

### CMU Locomotion Drift
Unlike AIST++ which keeps dancers in place, CMU motions preserve the original movement trajectory. A walking motion will actually move the character across the frame. The drift is accumulated frame-by-frame and persists through chained sequences, allowing for continuous locomotion paths.

### AIST++ Data Processing
The AIST++ dance data is converted from COCO 17-keypoint format to OpenPose 18-keypoint format for SCAIL compatibility. Chunks are cut at velocity minimums (natural pauses in movement) rather than fixed intervals to preserve move integrity. Energy tagging uses velocity + acceleration metrics, calculated per-genre to account for style differences (krump is naturally higher energy than house).

### CMU Data Processing
CMU BVH files are converted to OpenPose 18-keypoint NPY format at 120fps. The first 5 frames (T-pose calibration) are automatically skipped. Joint mapping preserves left/right orientation for correct rendering.

## Credits

- SCAIL: [zai-org/SCAIL](https://github.com/zai-org/SCAIL)
- Taichi renderer from [zai-org/SCAIL-Pose](https://github.com/zai-org/SCAIL-Pose)
- ComfyUI integration: [kijai/ComfyUI-SCAIL-Pose](https://github.com/kijai/ComfyUI-SCAIL-Pose)
- Beat detection: [librosa](https://librosa.org/)
- Expanded Pose Library: Discord user **NebSH**

## Legal & Licensing

This software downloads and processes third-party datasets. Users are responsible for complying with the attribution requirements of these licenses when publishing generated content.

### 1. CMU Motion Capture Database

- **Source:** [mocap.cs.cmu.edu](http://mocap.cs.cmu.edu)
- **License:** Free for use (including commercial), but requires citation.
- **Required Citation:**
  > "The data used in this project was obtained from mocap.cs.cmu.edu. The database was created with funding from NSF EIA-0196217."

### 2. AIST++ Dataset

- **Source:** [Google Research AIST++](https://google.github.io/aistplusplus_dataset/)
- **License:** CC-BY 4.0 International
- **Terms:** Commercial use allowed. Modification allowed. Redistribution allowed.
- **Required Attribution:** You must give appropriate credit to the original researchers (Li et al., ICCV 2021) in your derived works (videos/images).

### Disclaimer

The authors of SCAIL-AudioReactive are not responsible for end-user license violations. This tool is provided "AS IS" without warranty of any kind. Access to the datasets is facilitated for research and creative toolchain integration; no ownership of the raw data is claimed.
