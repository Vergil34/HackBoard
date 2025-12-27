# ButtonBox
Hack Club Blueprint Starter Project. This is my first time working in-depth with creating a PCB or CADing something to actually bring it to life, so it was definitely a fun experience. I plan to use this as a small button box for sim racing, but it can probably be easily reprogrammed to be a regular macro pad.

<img src=assets/whole.png alt="Whole" width="800"/>


## Features:
- 3D printed case. I did something pretty simple since I'm new to cadding
- 128x32 OLED Display, because why not?
- 2 SK6812 MINI-E LEDs just for some lights
- 4 keys

## CAD
Held together with 4 M3x16mm screws +  4x M3x5mx4mm heatset inserts, the pcb doesnt have too much space to move around, so I didn't mount it with a screw. 2 pieces for the print, top cover, and bottom holder.

<img src=assets/Final.png alt="Final" width="500"/>

Used Fusion 360, hooray for school accounts

## PCB
Used KICAD, and wasnt as complicated as I thought it was gonna be originally.

Schematic:

<img src=assets/sch.png alt="Schematic" width="500"/>

PCB:

<img src=assets/PCB.png alt="PCB" width="500"/>

## Firmware

I used KMK for everything. I was originally planning to do QMK, but I felt like it would take too long to get the custom profile approved (Im doing this way too late)

-OLED screen will display date and time, a small clock wouldn't be a bad addition to my setup
-4 Keys that will be bound to a key on my regular keyboard and then be used to turn things like the headlights of a car, or if I want to turn onthe wipers, etc in game. Can be very easily changed by programming. To be finalized when I get the box built. 

##BOM: 
The parts needed:
- 4x Cherry MX-Switches
- 4x DSA Keycaps
- 1x 0.91" 128x32 OLED Display
- 1x XIAO RP2040
- 1x Case (2 printed parts)
- 4x M3x5mx4mm heatset inserts
- 4x M3x16mm screws

##Extra Stuff
I'm not sure where I was supposed to put this, but I do need a soldering kit. Thanks!

