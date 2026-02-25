# OpenImageIO for ComfyUI

Basic set of nodes for proper color management using [OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO)   
This is initially meant as a companion for a "private" fork of [ComfyUI for Nuke](https://github.com/vinavfx/ComfyUI-for-Nuke).

**Nodes:**
- Load Image (oiio)
- Colorspace Convert (oiio)
- Save Image (oiio)

## Installation

If you want to use a custom OCIO config, set the `OCIO` environment variable before starting ComfyUI.

```sh
pip install -r requirements.txt
```

## Features

- [x] Basic I/O with colorspace support.  
  *BMP, Cineon, DDS, DICOM, **DPX**, FITS, GIF, HDR/RGBE, HEIF/HEIC/AVIF, ICO, IFF, JPEG, JPEG-2000, JPEG XL, Movie formats (using ffmpeg), Null format, **OpenEXR**, OpenVDB, PNG, PNM / Netpbm, PSD, Ptex, RAW digital camera files, RLA, SGI, Softimage PIC, Targa, Term (Terminal), TIFF, Webp, Zfile*
- [x] Colorspace converter node
- [ ] Basic metadata reading/writting (and for formats that comfy support `prompt` & `extrapng_info`)
- [ ] DITs? Not sure how to properly translate that but maybe just force `sRGB (D60)` and add preview on nodes?


## Preview
![image](https://github.com/user-attachments/assets/a6c19322-787d-41ee-9932-545f71b457fb)

## Contribute / Feedback
Don't hesitate to PR or [open issues](https://github.com/melMass/comfy_oiio/issues/new/choose)

