# ComfyUI Turtle Graphics Demo

> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under construction.
> Parts of the node are still under development. There may therefore be
> minor differences between the node itself and the documentation for
> the node. The documentation is also not yet complete.</p>

## Get Started

<p align="justify">Turtle Graphics has some interesting features. This 
node makes use of these capabilities. The aim is to show how beautiful
graphics can be created with Turtle Graphics.</p>

<p align="justify">It will explained later how Turtle Graphics works.
It has to be noted that Turtle Graphics makes use of the Python package
Tkinter. In variations of this nodes one can think about different cases
where Turtle Graphics or/and Tkinter can be used.</p>

<p align="justify">As part of the development I could show that it is 
not necessary to save and load a Turtle Graphics for the later use. A
canvas created by Turtle Graphics can be streamed so it can be used as 
Pil image.</p> 

<p align="justify">The background of a Turtle Graphics image is by 
default white. This is completely independent from the background of 
the screen where the graphics is drawn. By use of Numpy this white 
background can be removed with a background of personal choice.</p> 

<p align="justify">If the background is exchanged by a black background 
it is also possible to remove this background and make the background
transparent.</p> 

<p align="justify">Step by step some more demos to the existing ones 
will be added. The settings will result in a broader range of graphics
creations.</p> 

<p align="justify">This node is intended for demonstration purposes,
but you can use this node for some interesting things. One example is
the creation of colourful QR codes.</p>  

## Introduction

<p align="justify">Over the years I have been working with Turtle 
Graphics again and again with longer breaks in between. When working
on masks for ComfyUI, the fastest way to create N-gons was to use
Turtle Graphics. So I started working with Turtle Graphics again.</p> 

## Main Goals of the Node

<p align="justify">One goal is to use the node as Turtle Graphics
demonstrator and to play with settings of a special demo.</p>

<p align="justify">Another goal is it to provide graphics to other
applications. One exaample will be given later.</p>

## Turtle Graphics

<p align="justify">Turtle Graphics was developed in the 60s of the
last century for learning and demonstration puposes. Turtle Graphics
is an implementation of the popular geometric drawing tools introduced
first in the programming language Logo developed 1967. In computer
graphics, Turtle Graphics are a special kind of vector graphics using
a relative cursor, which is called turtle upon a Cartesian co-ordinate 
system plane with x and y axis. The turtle itself has three attributes, 
which are the location, the orientation (or direction) and the pen. 
The pen has attributes too, which are color, width, and down and up 
state.</p>

## Turtle Graphics Implementations

Implementations of Turtle Graphics in programming languages can be found in:

* Logo
* Python
* Scratch
* Java
* JavaScript
* HTML5 Canvas
* C++
* Joy

## Turtle Graphics and Python

<p align="justify">In this node I made use of the special character 
of the Python module Turtle Graphics. As long one waits until the 
image is drawn everything is fine. If not it could be that the code
will  have a short confusion in form of a catched error in the
background.</p> 

<p align="justify">Turtle Graphics is using Tkinter for the windows
management. Starting a draw command Turtle Graphics is opening a (tkinter)
window for drawing. Within the node one can decide to show this window 
or not.</p> 

<p align="justify">One can decide to let a turtle or another shape drawing
the image. This can also be set in the node.</p> 

## Node Settings

<p align="justify">The node settings are largely self-explanatory.
Accordingly, I am currently only providing a few comments.</p>

### Turtle Graphics Circles Demo Node

#### Node Preview     

<p align="justify">Figure 1 shows a preview of the Turtle Graphics Circles Demo Node.</p>

![image](https://github.com/user-attachments/assets/faeb7fbd-e715-4a50-8116-1e39b7846d8d)

*Figure 1: Turtle Graphics Circles Demo node*

Graphic specific settings are:

+ circle_radius
+ number_rotations
+ rotation_angle
+ start_angle

#### Pseudo Code

<p align="justify">Following pseudo code describes
the movement of the turtle (in a loop) on the screen.</p>

<pre>
number_rotations = 36
circle_radius = 100
increment_angle = 10°

LOOP FOR i FROM 0 TO number_rotations STEP 1
    DRAW CIRCLE (circle_radius)
    ROTATE TURTLE RIGHT (increment_angle)
END LOOP
</pre>

<p align="justify">The following (colorful) image was created using the pseudo code settings.</p>

![ComfyUI_00622_](https://github.com/user-attachments/assets/1a5915cb-5414-40ff-8ef1-fcc6e5dccade)

*Figure 2: Image created using the pseudo code settings*

#### Graphics Examples

<p align="justify">Following images are drawn with the Turtle Graphics Circles demo node.</p>

  📎     | Column 1            | Column 2         |   Column 3  
:----: | :-------------------------: | :-------------------------: | :----------------------------------:
Row 1 | ![ComfyUI_00625_](https://github.com/user-attachments/assets/556e2767-1f63-4dfc-b604-84692a2c8ce3) | ![ComfyUI_temp_otckr_00032_](https://github.com/user-attachments/assets/412b17e0-63e2-42c2-b522-e27eff587049) | ![ComfyUI_temp_otckr_00034_](https://github.com/user-attachments/assets/5701d9a3-ce5f-4e99-acad-ef6af2ba044a)
Row 2 | ![ComfyUI_00567_](https://github.com/user-attachments/assets/f7430d8c-40f9-4a54-b618-6cd01c008366) | ![ComfyUI_00568_](https://github.com/user-attachments/assets/24673789-8419-4819-af23-0df8295a1f6b) | ![ComfyUI_00572_](https://github.com/user-attachments/assets/1d0a243b-5880-43e9-a5a9-7b767fc7bd04)
Row 3 | ![ComfyUI_00577_](https://github.com/user-attachments/assets/ffe93bbb-2247-4945-b74e-ae18b70e7479) | ![ComfyUI_00579_](https://github.com/user-attachments/assets/68e3a0e5-7690-46f9-ace9-5c2cd5fa72f6) | ![ComfyUI_00593_](https://github.com/user-attachments/assets/85e19ab0-032c-45f4-9609-ad22777359e1)

## Turtle Graphics Squares Demo

### Node Preview

<p align="justify">Figure 1 shows a preview of the Turtle Graphics Circles Demo Node.</p>

![image](https://github.com/user-attachments/assets/c45793e2-bb84-481c-a7b8-d3c155236783)

*Figure 3: Turtle Graphics Squares Demo*

Graphic specific settings are:

to do ..

#### Pseudo Code

<p align="justify">Following pseudo code describes
the movement of the turtle on the screen.</p>

<pre>
angle = 0°
increment_angle = 15°    
length = 10
increment_length = 2
number_rotations = 80

LOOP FOR i FROM 1 TO number_rotations STEP 1
    LOOP FOR j FROM 1 TO 4 STEP 1 
        MOVE TURTLE FORWARD (length)
        ROTATE TURTLE LEFT (90°)
    END LOOP
    ROTATE TURTLE LEFT (angle)
    angle = angle + increment_angle
    length = length + increment_length
END LOOP
</pre>

The following (colorful) image was created using the pseudo code settings.

![image](https://github.com/user-attachments/assets/8a16fdcd-0f90-44a9-a1eb-c440675daa0c)

Figure 4: Image created using the pseudo code settings

Graphic specific settings are:

to do ..

### Graphics Examples

  📎     | Column 1            | Column 2         |   Column 3  
:----: | :-------------------------: | :-------------------------: | :----------------------------------:
Row 1 | ![ComfyUI_temp_otckr_00021_](https://github.com/user-attachments/assets/5a59d225-7401-4864-8334-992170004991) | ![ComfyUI_temp_otckr_00004_ (4)](https://github.com/user-attachments/assets/0037b51f-3923-4183-b34e-de4f3d9b848b) | ![ComfyUI_temp_otckr_00005_ (8)](https://github.com/user-attachments/assets/794afeba-5f9d-401a-8af6-cbab965823a5)
Row 2 | ![ComfyUI_temp_otckr_00009_ (2)](https://github.com/user-attachments/assets/8ea38ed5-aaad-421a-86cb-cfc1cebe9a80) | ![ComfyUI_temp_otckr_00029_](https://github.com/user-attachments/assets/05e5340f-3653-40cc-bc53-9a14e44d366d) | ![ComfyUI_temp_otckr_00040_](https://github.com/user-attachments/assets/22fc1d80-6b72-4464-ae84-8e44dc7ad81f)
Row 3 | ![ComfyUI_temp_otckr_00011_ (4)](https://github.com/user-attachments/assets/6b7bdd90-3fae-4354-b16c-a728386028c7) | ![ComfyUI_temp_otckr_00022_](https://github.com/user-attachments/assets/aa7b63e4-08cb-4e01-845a-baf333d887c0) | ![ComfyUI_temp_otckr_00026_](https://github.com/user-attachments/assets/d62e2ff7-d561-42d6-b79a-f625ff5b0b67)

### Turtle Graphics Spiral Demo Node

### Node Preview

![image](https://github.com/user-attachments/assets/ec1a7d40-29fe-4cd2-8da5-b4b496dd75ce)

*Figure 5: Turtle Graphics Spiral Demo*

 📎     | Column 1            | Column 2         |   Column 3  
:----: | :-------------------------: | :-------------------------: | :----------------------------------:
Row 1 | ![ComfyUI_temp_otckr_00002_ (4)](https://github.com/user-attachments/assets/12ae4099-5ac6-43c8-9670-068cb63f3b98) | ![ComfyUI_temp_otckr_00008_ (2)](https://github.com/user-attachments/assets/c5c5a48b-01a3-4d50-8cc2-23baa3c01afe) | ![ComfyUI_temp_otckr_00021_ (1)](https://github.com/user-attachments/assets/c86751f2-4488-4f71-a61b-9b02b888a1a2)
Row 2 | ![ComfyUI_temp_otckr_00027_](https://github.com/user-attachments/assets/dfe7fedd-6cea-4725-9e0b-fe443b24db16) | ![ComfyUI_temp_otckr_00005_ (10)](https://github.com/user-attachments/assets/12786dce-22bb-419b-b766-5fa0126ab304) | ![ComfyUI_temp_otckr_00028_](https://github.com/user-attachments/assets/b5ef6459-3dcb-4f8e-a133-16fbbdfbcef7)
Row 3 | ![ComfyUI_00609_](https://github.com/user-attachments/assets/d3346d66-0cf8-4e33-b145-b2c77f7d3919) | ![ComfyUI_00605_](https://github.com/user-attachments/assets/ab666638-2332-46cb-ba46-920386f94740) | ![ComfyUI_00621_](https://github.com/user-attachments/assets/5842e885-ccdd-47be-a87c-16e0df2d424f)

#### Pseudo Code

Following pseudo code describes the movement of the turtle on the screen.

<pre>
angle = 45°    
max_length = 180
    
LOOP FOR i FROM 1 TO max_length STEP 1
        MOVE TURTLE FORWARD (i)
        ROTATE TURTLE LEFT (angle)
END LOOP
</pre>

The following (colorful) image was created using the pseudo code settings.

![image](https://github.com/user-attachments/assets/de487fe3-de7d-4bbf-b314-a65534b273c3)

### Turtle Graphics Circle Lobes Demo Node 

#### Node Preview

<p align="justify">Figure 1 shows the Turtle Graphics Circle Lobes Demo  
node. The settings for the graphics are fully parameterised.</p> 

![image](https://github.com/user-attachments/assets/d39e57b6-1b57-4032-bd29-d5b354c8255b)

*Figure 6: Turtle Graphics Circle Lobes Demo*

Graphic specific settings are:

to do ..

#### Pseudo Code

to do ...

#### Graphics Examples

  📎     | Column 1            | Column 2         |   Column 3  
:----: | :-------------------------: | :-------------------------: | :----------------------------------:
Row 1 | ![ComfyUI_temp_otckr_00005_ (7)](https://github.com/user-attachments/assets/5d3bcd8a-24ab-43d7-99e3-d29c0f38cef9) | ![ComfyUI_temp_otckr_00006_ (2)](https://github.com/user-attachments/assets/2db35f0b-4219-4007-afc3-856d729900d1) | ![ComfyUI_temp_otckr_00010_ (4)](https://github.com/user-attachments/assets/ef0e5a23-2228-4a34-863d-d2b0b47188cb)
Row 2 | ![ComfyUI_temp_otckr_00013_](https://github.com/user-attachments/assets/b03ca5e8-6a57-4665-b1fe-baa39944432a) | ![ComfyUI_temp_otckr_00015_ (1)](https://github.com/user-attachments/assets/62d14758-3954-4ed7-b204-0958ef0e0d41) | ![ComfyUI_temp_otckr_00016_](https://github.com/user-attachments/assets/b29f3a54-c7ec-477b-8d7f-f4aba416c81f)
Row 3 | ![ComfyUI_temp_tvbxm_00010_ (1)](https://github.com/user-attachments/assets/673a92f0-5dce-4e6f-a101-339f44379435) | ![ComfyUI_temp_tvbxm_00013_](https://github.com/user-attachments/assets/e495cab7-a1dd-4bfb-8061-d4a8b9d8f8ba) | ![ComfyUI_temp_tvbxm_00016_](https://github.com/user-attachments/assets/b7435ed4-1b19-47ca-9232-bb3e63946da9)

### Turtle Graphics Concate Lines Demo Node 

#### Node Preview

![image](https://github.com/user-attachments/assets/cf429848-f707-4e31-91be-6c5375c9cfc9)

*Figure 7: Turtle Graphics Concate Lines Demo*

Graphic specific settings are:

#### Pseudo Code

Following pseudo code describes the movement of the turtle on the screen.

<pre>
number_rotations = 300
angle = 75°

LOOP FOR i FROM 1 TO number_rotations STEP 1
    MOVE TURTLE FORWARD (i)
    ROTATE TURTLE RIGHT (angle)
END LOOP
</pre>

The following (colorful) image was created using the pseudo code settings.

![image](https://github.com/user-attachments/assets/356faf2b-c0f1-4d4c-b1e7-76bfda831655)
 
#### Graphics Examples 

 📎     | Column 1            | Column 2         |   Column 3  
:----: | :-------------------------: | :-------------------------: | :----------------------------------:
Row 1 | ![ComfyUI_00532_](https://github.com/user-attachments/assets/b92000cc-ad23-42f7-8f84-dd010fc80465) | ![ComfyUI_00533_](https://github.com/user-attachments/assets/c6506e49-a2f4-45b9-a8b0-42bacc099c4f) | ![ComfyUI_00535_](https://github.com/user-attachments/assets/83e88c59-4ec6-4cf3-adc5-a6b16686b68b)
Row 2 | ![ComfyUI_00536_](https://github.com/user-attachments/assets/250ef0d0-fd64-4c17-93b5-0b154b86e88b) | ![ComfyUI_00540_](https://github.com/user-attachments/assets/ab326ec6-f8a4-47ff-8fff-caf9d3ffe20e) | ![ComfyUI_00545_](https://github.com/user-attachments/assets/ada442e1-2579-45b3-adbc-df5bb84eb22a)
Row 3 | ![ComfyUI_00556_](https://github.com/user-attachments/assets/3247fa60-a514-495c-b599-688cad35aec3) | ![ComfyUI_00557_](https://github.com/user-attachments/assets/5e277ed6-4b3f-4555-ad19-7a3f99de3017) | ![ComfyUI_00561_](https://github.com/user-attachments/assets/713bafee-595a-4756-b1d2-702e40964d65)

## Real Life Example

### Workflow Preview

<p align="justify">Please note that this is a example, which
might not be working. Creating such colorful and working QR 
Codes need some fine tuning. The Difference in contrast between
forground color and background color must be 20 % in difference.
One needs for compositing an image which fulfills this. This can 
be reached by try and error. If a QR code scanner is reading the 
created image it works, otherwise not.</p>

![image](https://github.com/user-attachments/assets/047ef65d-6c86-4002-9b81-1e70e1b4ef8e)

### Example Images

  📎     | Turtle Graphics           | QR Code                     |   AI Image  
:----: | :-------------------------: | :-------------------------: | :-------------------------:
Images | ![ComfyUI_temp_voxnf_00024_ (1)](https://github.com/user-attachments/assets/6af4e8ba-3c52-4180-87a3-63b99bf749e7) | ![ComfyUI_temp_mzxdj_00009_](https://github.com/user-attachments/assets/1193ebc7-988f-4541-bbd9-3a790bad1e9b) | ![image](https://github.com/user-attachments/assets/663965d3-965d-4cd2-a1f5-66fed257abcb)

## Known Problems

### Tkinter Crash

<p align="justify">Tkinker crashes under unknown circumstances.
In general this can be resolved by restarting ComfyUI.</p>

### ComfyUI Crash

<p align="justify">Sometimes following error occures, when
closing to often a Turtle Graphics windows while Turtle
Graphics is still drawing.</p>

<pre>
RuntimeError: main thread is not in main loop
Tcl_AsyncDelete: async handler deleted by the wrong thread
</pre>  

<p align="justify">In general this can be resolved by restarting
ComfyUI.</p>

## Open Questions

<p align="justify">In real-life use of the node, a few questions
have arisen that require clarification. As long as I am using a
square format the resulting image is with or without upscaling in
his quality good. I used a landscape format and the image became 
blurry. It became even more blurred by changing the background.</p>

## Open Issues

<p align="justify">Opening and closing of a Turtle Graphics 
window or start and stop of a Turtle Graphics object is not
working as expected.</p>

## To-Do

<p align="justify">I need nodes where I can move the 
starting point of the Turtle Graphics from the center 
of the drawing area by offset values for x and y.</p>

# References

[1] https://docs.python.org/3/library/turtle.html

<hr width="100%" size="2">

## Donation

<p align="justify">If you like what I present here, or if it helps you,
or if it is useful, you are welcome to donate a small contribution. Or
as you might say: Every TRON counts! Many thanks in advance! :smiley:
</p>

<p align="left">${\textnormal{\color{navy}Tron}}$</p>

```
TQamF8Q3z63sVFWiXgn2pzpWyhkQJhRtW7
```
<p align="left">${\textnormal{\color{navy}Doge}}$</p>

```
DMh7EXf7XbibFFsqaAetdQQ77Zb5TVCXiX
```
<p align="left">${\textnormal{\color{navy}Bitcoin}}$</p>

```
12JsKesep3yuDpmrcXCxXu7EQJkRaAvsc5
```
<p align="left">${\textnormal{\color{navy}Ethereum}}$</p>

```
0x31042e2F3AE241093e0387b41C6910B11d94f7ec
```
