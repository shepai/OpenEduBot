# Introduction

There are different chassis that the library currently supports. Of course, you can build and make your own, but these are the chassis we have built support for.


## MicroPython
MicroPython is the default on the Raspberry Pi Pico.

### [WheelBot](https://github.com/shepai/OpenEduBot/tree/main/Instructions%20and%20code/WheelBot)
Wheelbot is a robot that uses... wheels and a ball caster. It is  great for line following, obstacle avoiding, and light following tasks. This small cheap chassis can allow cheap robotics teaching in schools. This makes use of motor drivers and breadboards, allowing you to build your own circuits. This robot is better for teaching electronic tasks, and good for audience who require longer.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/wheelBot.jpg" width="25%" >

### [WheelBot2](https://github.com/shepai/OpenEduBot/tree/main/Instructions%20and%20code/WheelBot_2)
Wheelbot 2 is an updated version of wheelbot, to use a better, more compact circuit. This robot can also be cheaper than the wheelbot. This method requires little circuit building compared to wheelbot, making it quicker to build and deploy for any audience.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/291091183_407439234666715_8003499927750599944_n.jpg" width="25%" >

### ServoBot
Servo bot is in development, and will allow you to control two wheels via continuous rotation servos.



## CircuitPython

CircuitPython is an alternative to MicroPython that some devices use. Using EduBot_CP.py you can have access to CircuitPython variants of the chassis. These will have separate instructions.

### [WheelBot](https://github.com/shepai/OpenEduBot/tree/main/Instructions%20and%20code/CircuitPython%20WheelBot)
This is a CircuitPython variant for the wheelbot. This has a braitenberg example for light following behaviours.
<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/Robot.jpeg" width="50%" >

## Controlling sensors
The different example codes come with their own sensor control. This section explains how you can use different sensors an interface with them.

### Photoresistor light sensors
The Photoresistor light sensor typically has 3 or 4 pins. The 3 pin variant is designed for digital reading. This will mean that the light detects on or off based on the light level crossing a threshold. The light threshold activation can be determined by rotating the screw in the blue box. With the 4 pin variant you have the choice between digital and analogue. Analogue is better at reading the intensity of light on a scale. This is ideal for light following robots.

<img src="https://raw.githubusercontent.com/shepai/OpenEduBot/main/Assets/sensor.jpg" width="20%" >

Within MicroPython we can call pins in using the machine library. We can then set a pin number using one of the GP#. Here we have pin 27 set to digital read and pin 26 set to analogue.

```
from machine import Pin,ADC

digital_pin=Pin(27,Pin.IN)
analog_pin=ADC(26)

print(digital_pin.value())
print(analog_pin.read_u16())
```

The above code will execute and print a digital reading of 1 or 0, depending on whether the sensor threshold is met. It will then output an analogue reading from the sensor connected to 26. This can be a very large and noisy value. You may want to see what the maximum and minimum values it can reach and divide down to a percentage scale of what it was. This is especially good when you are controlling motor speeds based off of light intensity.

Within CircuitPython the digital and analogue pins are separate libraries. We also must import board in order to get easy access to each pin. The following codes both use the same pins as the micropython code above.

```
import board
from analogio import AnalogIn

s1 = AnalogIn(board.GP26)

def get_voltage(pin):
    return (pin.value * 3.3)

print(get_intensity(s1))
```

For digital reading we use the digital library.

```
import board
from digitalio import DigitalInOut, Direction, Pull

s2 = DigitalInOut(board.GP27)
s2.direction = Direction.INPUT

print(s2.value)

```
