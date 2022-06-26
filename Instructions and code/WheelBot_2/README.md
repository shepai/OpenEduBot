# WheelBot
The WheelBot2 chassis can be implemented using a number of different dc motor controlled chassis. The one we have used was purchased from the [Pi Hut](https://thepihut.com/products/adafruit-mini-3-layer-round-robot-chassis-kit-2wd-with-dc-motors). For electronics it required the following items:
- Raspberry Pi Pico
- [Robotics Hat](https://thepihut.com/products/robotics-board-for-raspberry-pi-pico)
- One 4xAA battery holder
- Ultrasound range finders (optional)
- IR light sensors (optional)
- Light sensitivity sensors (optional)
- AA batteries 4

You should be able to build a working one of these for approx £30-£50 each depending on bulk buy and how much you are willing to solder. This robot is very similar to the WheelBot robot, but with one key difference - which is the robotic hat. This hat is more expensive than using a motor driver but much more compact for the chassis. Additionally, it has an inbuilt oltage regulator so both the pico and hat can be powererd from one battery holder. 

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/wheelBot2.jpg" width="50%" >


## Building the chassis
Coming soon

## Programming
Pre-written examples can be found:
- Example.py

The EduBot.py found in [library](https://github.com/shepai/OpenEduBot/Library) must be uploaded in the same directory as your main code on the Raspberry Pi Pico.

We have used the [Thonny IDE](https://thonny.org/). Once downloaded this software allows you to connect to the Raspberry Pi Pico. Simply go to the bottom right corner of the window, and select an interpreter. We are using the Raspberry Pi Pico. Raspberry Pi have a [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) on getting set up with the Pico.

Once all connected you can load one of our examples in and click run. The robot will run this code while the USB is attached. To make it mobile, save the example as main.py on the Pico device, and it will run on boot.
