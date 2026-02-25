# ComfyUI-TiledVaeLite
Tiled VAE decode node for ComfyUI

Faster than the ComfyUI core tiled VAE decode node, and less clutter to the node tree than the LTXV package. This adds only one node under the latent category.

Modifications compared to the original LTXV tiled VAE decode node:
* Progress bar
* Defaults are now 2x2 tiles and overlap 4 units (32 or 64 pixels); max tiles increased from 6x6 to 8x8
* Actual logging instead of `print` so it doesn't mess up the ComfyUI bottom panel log
* Compacted formatting of the log messages and added time measurements per tile and total
* Improved tile size calculation so that the last tiles are never larger than first, to avoid OOM late in the process

Can be useful for decoding large video latents such as those of Wan 2.2 5B TI2V or HunyuanVideo 1.5 both of which have big and slow VAEs, or any large image, with low VRAM.

---

An example of decoding a 704x704 video of 121 frames with the Wan 2.2 VAE, using a GTX 970.

Settings are 3x3 tiles with overlap 4 (64 pixels):
```
Using pytorch attention in VAE
Using pytorch attention in VAE
VAE load device: cuda:0, offload device: cpu, dtype: torch.float32
Processing VAE decode tile at row 0, col 0:  Position: (0:272, 0:272), Size: 272x272
Requested to load WanVAE
loaded partially; 1292.06 MB usable, 1184.06 MB loaded, 1503.99 MB offloaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 84.51 seconds
Processing VAE decode tile at row 0, col 1:  Position: (208:480, 0:272), Size: 272x272
loaded partially; 1290.06 MB usable, 1182.06 MB loaded, 1506.00 MB offloaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 82.05 seconds
Processing VAE decode tile at row 0, col 2:  Position: (416:704, 0:272), Size: 288x272
0 models unloaded.
Unloaded partially: 55.84 MB freed, 1126.21 MB remains loaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 85.51 seconds
Processing VAE decode tile at row 1, col 0:  Position: (0:272, 208:480), Size: 272x272
loaded partially; 1280.24 MB usable, 1172.22 MB loaded, 1515.96 MB offloaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 81.23 seconds
Processing VAE decode tile at row 1, col 1:  Position: (208:480, 208:480), Size: 272x272
loaded partially; 1288.06 MB usable, 1180.06 MB loaded, 1508.06 MB offloaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 81.23 seconds
Processing VAE decode tile at row 1, col 2:  Position: (416:704, 208:480), Size: 288x272
0 models unloaded.
Unloaded partially: 84.08 MB freed, 1095.97 MB remains loaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 85.53 seconds
Processing VAE decode tile at row 2, col 0:  Position: (0:272, 416:704), Size: 272x288
loaded partially; 1117.18 MB usable, 1009.18 MB loaded, 1678.88 MB offloaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 84.90 seconds
Processing VAE decode tile at row 2, col 1:  Position: (208:480, 416:704), Size: 272x288
0 models unloaded.
Unloaded partially: 37.14 MB freed, 972.04 MB remains loaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 85.62 seconds
Processing VAE decode tile at row 2, col 2:  Position: (416:704, 416:704), Size: 288x288
0 models unloaded.
Unloaded partially: 162.01 MB freed, 810.03 MB remains loaded, 108.00 MB buffer reserved, lowvram patches: 0
  Time: 93.08 seconds
VAE total decode time: 765.83 seconds
Prompt executed in 00:13:11
```
This prompt execution time includes initial loading of the VAE model from disk to memory.

Compare to decoding the same video latent with the default `VAE Decode (Tiled)` node with tile_size 288, overlap 64 and temporal_size 128 (thus no temporal tiling):
```
0 models unloaded.
Unloaded partially: 864.03 MB freed, -54.00 MB remains loaded, 108.00 MB buffer reserved, lowvram patches: 0
Prompt executed in 00:15:59
```
This was executed directly after running the previous TiledVaeLite decode so the VAE was already in memory.
