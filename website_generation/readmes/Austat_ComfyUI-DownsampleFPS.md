# ComfyUI-DownsampleFPS
## A node for ComfyUI to downsample framerate ie. from 48 to 24.

<img width="294" height="203" alt="image" src="https://github.com/user-attachments/assets/b0467347-4307-48f8-86d2-3ee55300d781" />


## Methods available:

"Frame dropping"

"Frame blending (CPU)"

"Optical flow (CPU)"

"Motion compensated (CPU)"

## Installation

Method 1: Clone the Repository
Navigate to your ComfyUI custom_nodes directory.
Run:

   git clone https://github.com/Austat/ComfyUI-DownsampleFPS

Restart ComfyUI.

Here’s the mental map you can keep - Each method is fast and really isn't resource hog. Computational time is usually in seconds (100 seconds lenght video takes five seconds on 32 cores):

<details>
  <summary>Details about each method</summary>

### 1.	Frame dropping
   
   o	Just picks certain original frames.
   
   o	No blending, no flow, nothing.
   
   o	Fastest. Sharpest individual frames. Choppy motion.
'''

### 2.	Frame blending
   
   o	Averages neighboring frames.
   
   o	No motion understanding.
   
   o	Removes harsh stutter at the price of ghosting.


### 3.	Optical flow
   
   o	Computes motion.
   
   o	Warps frame1 halfway to frame2.
   
   o	Can generate intermediate-looking frames but prone to warpy artifacts when flow fails.


### 4.	Motion compensated
   
   o	Computes motion.
   
   o	Warps both frame1 forward and frame2 backward.
   
   o	Blends warped frames for a more symmetric and robust mid-frame.


### By visual result

•	If you care about absolute sharpness, don’t mind choppiness: Use Frame dropping.

•	If you want fewer artifacts and can accept mild ghosting: Use Frame blending.

•	If you want smoother motion and can tolerate potential warping artifacts: Use Optical flow.

•	If you want best motion-aware quality within CPU Farneback: Use Motion compensated — your most advanced method here.


### By failure modes

•	Dropping:

o	Fails by being visually choppy. No weird artifacts, just temporal roughness.

•	Blending:

o	Fails via ghosting — double exposures and soft blur.

•	Optical flow:

o	Fails via weird warping/stretching, especially around edges or fast motion.

•	Motion compensated:

o	Fails similarly to optical flow, but blending two warped views sometimes hides the worst of it.

