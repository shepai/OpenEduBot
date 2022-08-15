
# WheelBot CircuitPython
The WheelBot2 chassis can be implemented using a number of different dc motor controlled chassis. The one we have used was purchased from the [Pi Hut](https://thepihut.com/products/adafruit-mini-3-layer-round-robot-chassis-kit-2wd-with-dc-motors). For electronics it required the following items:
- [PiMaker](https://thepihut.com/products/maker-pi-rp2040)
- One 4xAA battery holder
- Ultrasound range finders (optional)
- IR light sensors (optional)
- Light sensitivity sensors (optional)
- AA batteries 4

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/Robot.jpg" width="50%" >

## Building the chassis
Firstly you will need to get the following parts. These parts can be found in the excel spreadsheet "costs.xlsx". It approximately costs £50 a robot. The more you build, the cheaper they become.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/CP_partList.PNG" width="50%" >

### Wiring

The wiring of the motors and battery needs to be in motors 3 and 4 for the library to be compatible. You may want to strip the ends of the wires off on the motors if it cannot be directly screwed into the robotics board.
The sensor inputs can be changed to any analogue pin, if you wish to add more then they can be used.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/CP_wiring.PNG" width="50%" >

### Step 1
Mount both of the motors on the chassis, using the side plates within the two rectangular slots on the chassis will keep the motors in place. This is the point that you can mount your chosen sensors for the lower level. If you are working with light sensors, this level is ideal.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/step1.PNG" width="50%" >

### Step 2
Mount the main controller, make sure you have soldered some L-shaped pins underneath the Robotics board if you wish to use GPIO pins to interface with sensors. If you are using more HATs than just the robotics board, you may want to consider using Step 3 as your second layer.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/CP_step2.PNG" width="50%" >

### Step 3
It is ideal to have the batteries on the top, so they can be easily changed without having to unscrew the chassis.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/CP_step3.PNG" width="50%" >


## Programming

The physical robot makes use of sensors and two motors. We can attach a USB to it and upload the code.

## Using a different IDE
Using a specific IDEs can be simpler for using MicroPython. [Thonny IDE](https://thonny.org/) is a simple IDE for uploading programs to the Raspberry Pi Pico. Once you have set up the IDE we can start [programming the board](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Step 1
Download the robot control library from [Github](https://raw.githubusercontent.com/shepai/OpenEduBot/main/Library/EduBot_CP.py) and have handy in a folder.

### Step 2
You will need to connect the robot to your device via USB. Make sure you have Thonny IDE up. In the bottom right corner you should be able to select the interpreter for the IDE. We want Generic CircuitPython.
