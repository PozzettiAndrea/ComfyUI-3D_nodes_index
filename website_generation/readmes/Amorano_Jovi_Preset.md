<div align="center">
<picture>
  <source srcset="https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/refs/heads/master/res/logo-jovi_preset.png">
  <img alt="Presets for ComfyUI Nodes with user persistance" width="384" height="384">
</picture>
</div>
<div align="center">
<a href="https://github.com/comfyanonymous/ComfyUI">COMFYUI</a> Presets for ComfyUI Nodes with user persistance<br><br>
</div>

<div align="center">

![KNIVES!](https://badgen.net/github/open-issues/Amorano/Jovi_Preset)
![FORKS!](https://badgen.net/github/forks/Amorano/Jovi_Preset)

</div>

<!---------------------------------------------------------------------------->

# SPONSORSHIP

Please consider sponsoring me if you enjoy the results of my work, code or documentation or otherwise. A good way to keep code development open and free is through sponsorship.

<div align="center">

&nbsp;|&nbsp;|&nbsp;|&nbsp;
-|-|-|-
[![BE A GITHUB SPONSOR ❤️](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Amorano) | [![DIRECTLY SUPPORT ME VIA PAYPAL](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/onarom) | [![PATREON SUPPORTER](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/joviex) | [![SUPPORT ME ON KO-FI!](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/alexandermorano)
</div>

## INSPIRATION

This is an idea I have had rumbling around since May 2024 and the first ComfyUI conference. I poorly assumed someone else would do it long before now. I finally got motivated by [fredconex](https://github.com/fredconex) after the excellent audio synth node work that was done, but was only using presets in the Equalizer.

## HIGHLIGHTS

* Simple right-click menu entry to add or use
* Presets are stored with your other ComfyUI configuration settings
* Easy removal with ctrl-click on entry

![image](https://github.com/user-attachments/assets/09f9e7e7-4fd1-48bc-91e0-8da90d214140)

![image](https://github.com/user-attachments/assets/a56b8a52-edda-4c1f-8af5-af7a9b0f814e)

![image](https://github.com/user-attachments/assets/98c26d0b-eb97-4a0c-860b-f0a59e9860cc)

## UPDATES

**2025/08/03** @1.0.5:
* clean up initialization in case its 100% missing

**2025/05/23** @1.0.4:
* when presetmanager was null, was crashing the right-click menu

**2025/05/23** @1.0.3:
* fixed non-error bug when nodes have no preset ability (output nodes)

**2025/05/17** @1.0.2:
* toast messages
* auto-updating panel

**2025/05/17** @1.0.1:
* added sidebar

**2025/05/13** @1.0.0:
* intial commit

# INSTALLATION

## COMFYUI MANAGER

If you have [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed, simply search for Jovi_Help and install from the manager's database.

## MANUAL INSTALL
Clone the repository into your ComfyUI custom_nodes directory. You can clone the repository with the command:
```
git clone https://github.com/Amorano/Jovi_Preset.git
```
You can then install the requirements by using the command:
```
.\python_embed\python.exe -s -m pip install -r requirements.txt
```
If you are using a <code>virtual environment</code> (<code><i>venv</i></code>), make sure it is activated before installation. Then install the requirements with the command:
```
pip install -r requirements.txt
```
# WHERE TO FIND ME

You can find me on [![DISCORD](https://dcbadge.vercel.app/api/server/62TJaZ3Z5r?style=flat-square)](https://discord.gg/62TJaZ3Z5r).
