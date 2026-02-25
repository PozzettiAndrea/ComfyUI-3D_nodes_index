# CosyVoice2 for ComfyUI
ComfyUI_NTCosyVoice is a plugin of ComfyUI for Cosysvoice2
## install plugin
```angular2html
git clone https://github.com/muxueChen/ComfyUI_NTCosyVoice.git
```
## Install dependency packages
```angular2html
cd ComfyUI_NTCosyVoice
pip install -r requirements.txt
```
## download models
```angular2html
python downloadmodel.py
```
## Install ttsfrd (Optional)
Notice that this step is not necessary. If you do not install ttsfrd package, we will use WeTextProcessing by default.
```angular2html
cd pretrained_models/CosyVoice-ttsfrd/
unzip resource.zip -d .
pip install ttsfrd_dependency-0.1-py3-none-any.whl
pip install ttsfrd-0.4.2-cp310-cp310-linux_x86_64.whl
```