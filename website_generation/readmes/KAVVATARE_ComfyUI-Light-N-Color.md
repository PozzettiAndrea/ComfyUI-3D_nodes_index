<h1>ComfyUI-Light-N-Color</h1>

<p>A collection of utility nodes for ComfyUI that enhance your image generation workflow. This extension provides tools for image processing, file management, and workflow control.</p>

<h2>Features</h2>

<h3>Image Processing</h3>
<ul>
  <li><strong>Flux Lighting & Color</strong>: Advanced image processing node that allows you to:
    <ul>
      <li>Adjust brightness, contrast, and saturation</li>
      <li>Fine-tune RGB channel levels individually</li>
      <li>Apply depth of field effects with various blur types</li>
      <li>Control black, mid, and white levels for perfect tonal balance</li>
    </ul>
  </li>
</ul>

<h3>File Management</h3>
<ul>
  <li><strong>Load Input/Output Image</strong>: Enhanced image loader that:
    <ul>
      <li>Loads images from both input AND output directories</li>
      <li>Supports browsing through subdirectories</li>
      <li>Preserves directory structure during selection</li>
    </ul>
  </li>
</ul>

<h3>Workflow Control</h3>
<ul>
  <li><strong>Switcher Nodes</strong>: A set of utility nodes to control your workflow:
    <ul>
      <li><strong>ControlNet Switcher</strong>: Toggle between two ControlNet conditions</li>
      <li><strong>Image Switcher</strong>: Switch between two image inputs</li>
      <li><strong>Latent Switcher</strong>: Choose between two latent representations</li>
    </ul>
  </li>
</ul>

<h2>Installation</h2>

<ol>
  <li>
    <p>Clone this repository into your ComfyUI custom_nodes directory:</p>
    <pre><code>cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Light-N-Color.git</code></pre>
  </li>
  <li><p>Restart ComfyUI</p></li>
</ol>

<h2>Requirements</h2>

<ul>
  <li>ComfyUI</li>
  <li>Python packages: numpy, torch, opencv-python, pillow</li>
</ul>

<h2>License</h2>

<p>This extension is provided as-is, with no restrictions on use or modification. Feel free to adapt it to your needs.</p>

<p>Happy creating! Peace :)</p>

<h2>Update</h2>

<p>2025/08/04</p>

<p>Added auto_analysis mode that automatically adjusts the color and contrast to your own settings.</p>

<p><img src="./img/LightNColor_v2.png" alt="Updated_v2_image"></p>

<p><img src="./img/nodes_include.png" alt="Included Nodes"></p>
