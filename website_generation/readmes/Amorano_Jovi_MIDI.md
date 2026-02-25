<div align="center">

<picture>
  <source srcset="https://raw.githubusercontent.com/Amorano/Jovimetrix-examples/refs/heads/master/res/logo-jovi_midi.png">
  <img alt="ComfyUI Nodes for Reading and Processing data from MIDI devices" width="256" height="256">
</picture>

</div>

<div align="center">

<a href="https://github.com/comfyanonymous/ComfyUI">COMFYUI</a> Nodes for Reading and Processing data from MIDI devices

</div>

<div align="center">

![KNIVES!](https://badgen.net/github/open-issues/Amorano/Jovi_MIDI)
![FORKS!](https://badgen.net/github/forks/Amorano/Jovi_MIDI)

</div>

<!---------------------------------------------------------------------------->

# SPONSORSHIP

Please consider sponsoring me if you enjoy the results of my work, code or documentation or otherwise. A good way to keep code development open and free is through sponsorship.

<div align="center">

&nbsp;|&nbsp;|&nbsp;|&nbsp;
-|-|-|-
[![BE A GITHUB SPONSOR ❤️](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Amorano) | [![DIRECTLY SUPPORT ME VIA PAYPAL](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.com/paypalme/onarom) | [![PATREON SUPPORTER](https://img.shields.io/badge/Patreon-F96854?style=for-the-badge&logo=patreon&logoColor=white)](https://www.patreon.com/joviex) | [![SUPPORT ME ON KO-FI!](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/alexandermorano)
</div>

## HIGHLIGHTS

* `MIDI READER` Captures MIDI messages from an external MIDI device or controller
* `MIDI MESSAGE` Processes MIDI messages received from an external MIDI controller or device
* `MIDI FILTER` (advanced filter) to select messages from MIDI streams and devices
* `MIDI FILTER EZ` simpler interface to filter single messages from MIDI streams and devices
* `MIDI LOADER` Load MIDI files and convert their events into a ComfyUI parameter list

## UPDATES

**2025/05/04** @1.0.4:
* widget definitions formatted for clarity
* align names to Lexicon in comfy_cozy

**2025/04/14** @1.0.3:
* core supports switched to [cozy_comfyui](https://github.com/cozy-comfyui/cozy_comfyui)

**2025/03/08** @1.0.2:
* removed security scanner failures for in-line http links

**2025/03/01** @1.0.1:
* fixed all the year dates in readme since I have been writing 2024! =D

**2025/02/01** @1.0.1:
* cleanup pyproject for registry
* patched `MIDI FILTER EZ` to work for all filters not just the first found
* Filter ranges are:
* * Single numbers: "1, 2" (equals)
* * Closed ranges: "5-10" (between inclusive)
* * Open ranges: "-100" (less than or equal to 100)
* * Open ranges: "50-" (greater than or equal to 50)
* * 1, 5-10, 2
* * * would check == 1, == 2 and 5 <= x <= 10

**2025/02/01** @1.0.0:
* intial breakout from Jovimetrix

# INSTALLATION

## COMFYUI MANAGER

If you have [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed, simply search for Jovi_MIDI and install from the manager's database.

## MANUAL INSTALL
Clone the repository into your ComfyUI custom_nodes directory. You can clone the repository with the command:
```
git clone https://github.com/Amorano/Jovi_MIDI.git
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
