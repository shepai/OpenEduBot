# WheelBot
The WheelBot chassis can be implemented using a number of different dc motor controlled chassis. The one we have used was purchased from the [Pi Hut](https://thepihut.com/products/adafruit-mini-3-layer-round-robot-chassis-kit-2wd-with-dc-motors). For electronics it required the following items:
- Raspberry Pi Pico
- Motor driver (L298N)
- A selection of jumper wires
- One 4xAA battery holder
- One 3xAA battery holder or some form of [voltage regulator](https://thepihut.com/products/dc-dc-automatic-step-up-down-power-module-2-5-15v-to-3-3v-600ma)
- Ultrasound range finders (optional)
- IR light sensors (optional)
- Light sensitivity sensors (optional)
- AA batteries (between 4-6 depending on your battery option)

You should be able to build a working one of these for approx £30-£50 each depending on bulk buy and how much you are willing to solder.  

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/wheelBot.jpg" width="50%" >


## Building the chassis

### battery options
There are two battery options that you can take to powering your robot. The Pico uses 3.3v whereas the motor driver requires a minimum of 5V. Using 4AA batteries we can produce over 5V and make the motors operate well. However, we cannot power the Pico directly from that as we risk damaging it. The simple solution is to run two separate battery packs, one with three AAs and one with four. As long as the ground is concocted this will function.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/two batteries.png" width="75%" >

The second option is more eloquent and less "clunky" which makes use of a voltage regulator. This steps down the voltage to a suable 3.3V for the Pico, and runs everything off of the same battery. We should always show caution using the same battery with robotics as motors can have a high current draw, causing the main controller to shut down/ reboot.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/volatageReg.png" width="75%" >


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
- obstacle avoid.py
- All the files within the folder Braitenberg

These files use different sensors, so make sure you have purchased the correct sensors and wired them to the specified pins for each. This is explained in the comments of each python file.

The EduBot.py found in [library](https://github.com/shepai/OpenEduBot/Library) must be uploaded in the same directory as your main code on the Raspberry Pi Pico.

We have used the [Thonny IDE](https://thonny.org/). Once downloaded this software allows you to connect to the Raspberry Pi Pico. Simply go to the bottom right corner of the window, and select an interpreter. We are using the Raspberry Pi Pico. Raspberry Pi have a [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) on getting set up with the Pico.

Once all connected you can load one of our examples in and click run. The robot will run this code while the USB is attached. To make it mobile, save the example as main.py on the Pico device, and it will run on boot.
