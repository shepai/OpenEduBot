# WheelBot
The WheelBot chassis can be implemented using a number of different dc motor controlled chassis. The one we have used was purchased from the [Pi Hut](https://thepihut.com/products/adafruit-mini-3-layer-round-robot-chassis-kit-2wd-with-dc-motors). For electronics it required the following items:
- Raspberry Pi Pico
- [Robotics Hat](https://thepihut.com/products/robotics-board-for-raspberry-pi-pico)
- One 4xAA battery holder
- Ultrasound range finders (optional)
- IR light sensors (optional)
- Light sensitivity sensors (optional)
- AA batteries 4

You should be able to build a working one of these for approx £30-£50 each depending on bulk buy and how much you are willing to solder. This robot is very similar to the WheelBot robot, but with one key difference - which is the robotic hat. This hat is more expensive than using a motor driver but much more compact for the chassis. Additionally, it has an inbuilt voltage regulator so both the Pico and hat can be powered from one battery holder.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/wheelBot2.jpg" width="50%" >

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/newRobot.jpg" width="25%" >

This page has instructions to build the first chassis, but the second chassis can be built in a similar way. The motor and ball assembly remains the same.

The Pico can be flashed with circuitPython should you need access to libraries such as [ulab](https://docs.circuitpython.org/en/latest/shared-bindings/ulab/index.html) (cp variant of numpy)

The robot can use the Kitroniks motor driver and the Kitroniks robotics board. Selecting between either of them can be done in the library [(See documentation)](https://github.com/shepai/OpenEduBot/tree/main/Library)

## Building the chassis
Firstly you will need to get the following parts. These parts can be found in the excel spreadsheet "costs.xlsx". It approximately costs £50 a robot. The more you build, the cheaper they become.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/partList.PNG" width="50%" >

### Wiring

The wiring of the motors and battery needs to be in motors 3 and 4 for the library to be compatible. You may want to strip the ends of the wires off on the motors if it cannot be directly screwed into the robotics board.
The sensor inputs can be changed to any analogue pin, if you wish to add more then they can be used.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/wiring.PNG" width="50%" >

### Step 1
Mount both of the motors on the chassis, using the side plates within the two rectangular slots on the chassis will keep the motors in place. This is the point that you can mount your chosen sensors for the lower level. If you are working with light sensors, this level is ideal.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/step1.PNG" width="50%" >

#### Step 1.1 - Roller ball wheel
Mount the roller ball wheel inserting the screws from the bottom. If using sensors, mount the L-shaped bracket along with the roller ball wheel.

#### Step 1.2 - Light Sensors
Mount the light sensors to the L-brackets using a small standoff to offset the sensors.

#### Step 1.3 - 2nd Layer standoffs
Attach 4 long standoffs in the corners of the 2nd layer, along with 2 small standoffs to mount the main controller board.

### Step 2
Mount the main controller, make sure you have soldered some L-shaped pins underneath the Robotics board if you wish to use GPIO pins to interface with sensors. If you are using more HATs than just the robotics board, you may want to consider using Step 3 as your second layer.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/step2.PNG" width="50%" >

### Step 3
It is ideal to have the batteries on the top, so they can be easily changed without having to unscrew the chassis.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/step3.PNG" width="50%" >

#### Step 3.1 Wiring
Wire the motors into the motor controller connections on the main controller. Left/Right motor connections are interchangable in the software so do not worry about mixing them.

#### Step 3.2 Battery Wiring
Attach the battery connector into the Power BLK+RED connections on the main controller.

#### Step 3.3 Sensor Wiring
If using sensors, wire them up to the servos pins on the main controller, a single wire from the sensors should be connected to the L-shaped GPUIO pins that were soldered on the underside for the controller.

### Step 4 - 3rd Layer
Mount the battery holder using a 2 double ended threaded pieces and 4 screws. Then mount the 3rd layer to the 4, 2nd layer standoffs. Then attach the battery connector to the holder.

## Programming

The physical robot makes use of sensors and two motors. We can attach a USB to it and upload the code.

## Using a different IDE
Using a specific IDEs can be simpler for using MicroPython. [Thonny IDE](https://thonny.org/) is a simple IDE for uploading programs to the Raspberry Pi Pico. Once you have set up the IDE we can start [programming the board](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

### Step 1
Download the robot control library from [Github](https://raw.githubusercontent.com/shepai/OpenEduBot/main/Library/EduBot.py) and have handy in a folder.

### Step 2
You will need to connect the robot to your device via USB. Make sure you have Thonny IDE up. In the bottom right corner you should be able to select the interpreter for the IDE. We want Raspberry Pi Pico MicroPython.

<img src="https://projects-static.raspberrypi.org/projects/getting-started-with-the-pico/725a421f3b51a5674c539d6953db5f1892509475/en/images/thonny-micropython-pico-menu.png" width="35%" >

The software will ask you to install firmware for the Pico. Install it.

<img src="https://projects-static.raspberrypi.org/projects/getting-started-with-the-pico/725a421f3b51a5674c539d6953db5f1892509475/en/images/thonny-install-micropython-pico.png" width="35%" >

The shell should then show it is connected to the Pico. Try entering the following in the shell:

```
print("Hello, world!")
```

This code is compiling on the Pico board. Any code they you write and run will now be uploading to the device.


### Step 3
Open the downloaded EduBot.py in the Thonny IDE, and then go to File>Save As and a prompt will come up asking whether to install on the device or computer. Resave the file on the device with the same name. We do this so we can control the chassis hardware.

Pre-written examples can be found:
- Example.py

The EduBot.py found in [library](https://github.com/shepai/OpenEduBot/Library) must be uploaded in the same directory as your main code on the Raspberry Pi Pico.

We have used the [Thonny IDE](https://thonny.org/). Once downloaded this software allows you to connect to the Raspberry Pi Pico. Simply go to the bottom right corner of the window, and select an interpreter. We are using the Raspberry Pi Pico. Raspberry Pi have a [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) on getting set up with the Pico.

Once all connected you can load one of our examples in and click run. The robot will run this code while the USB is attached. To make it mobile, save the example as main.py on the Pico device, and it will run on boot.

## Troubleshooting
There are some problems that you may come into contact with, especially if this is your first time to electronics. We have tried to list as many here as we can. If your problem is not listed, please see [issues](https://github.com/shepai/OpenEduBot/issues) and if there still isn't an answer feel free to raise one yourself!

### The board wont connect to USB
Firstly, make sure your USB device works for data transmission. Check your wiring and make sure there is no short circuiting. If this is all fine, consider having the battery switched on while you make contact with the board. We suspect there is an issue with the current being supplied to the device and it not being seen by the PC.

### The sensors aren't working
Check your wiring, also make sure the sensors are not touching the motor pins or conducting where they should not.

### The motors are turning the wrong way
There are two ways to solve this, hardware or software. Firstly make sure that the motors are wired the same. Red Black Red Black should be the pattern going in to the device. Within the examples, you can change the motors to be from "f" to "r" or vice versa.

### The motors are not turning at allow
Make sure the motors are both in the motor 2 and motor 4 sockets. The board should be on and your code running. Solder over the outside of the motor wire tips if you can, this prevents short circuiting.

### The light detecting robot is moving away from Light
This is likely because your sensors are the wrong way round. Try changing the pins physically or switching the pins in the code.
