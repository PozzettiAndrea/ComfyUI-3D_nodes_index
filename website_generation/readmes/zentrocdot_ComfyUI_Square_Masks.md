# ComfyUI_Square_Masks

> [!IMPORTANT]  
> <p align="justify">🚧 This documentation is still under construction.
> Parts of the node are still under development. There may therefore be
> minor differences between the node itself and the documentation for
> the node. The documentation is also not yet complete.</p>

## Preface

<p align="justify">The node in its current form is the result of tests
that I carried out with it during the course of the day. I had to change
parts of the code again and again.</p>

## Motivation

<p align="justify">I was looking for a node with the funcionality of this 
node some time ago and despite an intensive search I couldn't find it. So
I programmed it myself based on my experience. From a mathematical point of
view, this node was more demanding than the nodes before.</p>

## Challenge

<p align="justify">It turned out to be a challenge that a source image can
be larger than 512 x 512 pixels. In the penultimate version of the node, I
had steps in the edges of the mask and the transitions were not sharp.</p>

## Node Preview

### Preview

![Bildschirmfoto vom 2025-02-12 21-13-33](https://github.com/user-attachments/assets/449f477f-f330-4ab0-b91c-406fb907261f)

### Settings

#### Settings Itself

<p align="justify">The node consists of three important parts, the input and
output connectors and the settings.</p>

The settings are

+ sides
+ scale

#### sides

The sides is the number of sides of a n-gon. It can start with 3 for a triangle
and can go up in steps of one. If one goes direction infinity one will get a circle
or something which looks like a circle.

#### scale

With scale one can scale the n-gon up or down.

## Example Preview

![Bildschirmfoto vom 2025-02-12 21-01-24](https://github.com/user-attachments/assets/de5882b0-8853-4bf1-a924-21a100e9da78)

## Open questions

<p align="justify">Even after a few tests, I'm still not sure whether a mask
generally has to have a variable size. What I do know is that the programmed
procedure works.</p>
