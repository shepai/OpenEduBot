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
Coming soon
### battery options
There are two battery options that you can take to powering your robot. The Pico uses 3.3v whereas the motor driver requires a minimum of 5V. Using 4AA batteries we can produce over 5V and make the motors operate well. However, we cannot power the Pico directly from that as we risk damaging it. The simple solution is to run two separate battery packs, one with three AAs and one with four. As long as the ground is concocted this will function.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/two batteries.png" width="50%" >

The second option is more eloquent and less "clunky" which makes use of a voltage regulator. This steps down the voltage to a suable 3.3V for the Pico, and runs everything off of the same battery. We should always show caution using the same battery with robotics as motors can have a high current draw, causing the main controller to shut down/ reboot.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/volatageReg.png" width="50%" >

### Cheaper

### More compact and less working



## Programming
Pre-written examples can be found:
- Example.py
- obstacle avoid.py
- All the files within the folder Braitenberg

These files use different sensors, so make sure you have purchased the correct sensors and wired them to the specified pins for each. This is explained in the comments of each python file.

The EduBot.py found in [library](https://github.com/shepai/OpenEduBot/Library) must be uploaded in the same directory as your main code on the Raspberry Pi Pico.

We have used the [Thonny IDE](https://thonny.org/). Once downloaded this software allows you to connect to the Raspberry Pi Pico. Simply go to the bottom right corner of the window, and select an interpreter. We are using the Raspberry Pi Pico. Raspberry Pi have a [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) on getting set up with the Pico.

Once all connected you can load one of our examples in and click run. The robot will run this code while the USB is attached. To make it mobile, save the example as main.py on the Pico device, and it will run on boot.
