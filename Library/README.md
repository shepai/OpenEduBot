There are two main variations of Python for circuit boards. We have developed circuitpython and micropython variants. The circuitPython one has been designed for the [MakerPi](https://thepihut.com/products/maker-pi-rp2040) whereas the micropython libary is designed for the Pico.

# Using the library
The library contains different bots for different chassis. For memory efficiency you may want to import only the classes you want. Each class corresponds to one of the designs within [intructions and code](https://github.com/shepai/OpenEduBot/tree/main/Instructions%20and%20code). Of course, you can use your own chassis designs with these libraries. As long as you use the same hardware.

## Dependincies 

### CircuitPython
1. simpleio
2. adafruit_motor


## CircuitPython
CircuitPython is an open-source derivative of the MicroPython programming language targeted toward students and beginners.

```
from EduBot_CP import wheelBot_2

bot = wheelBot_2()
```

## MicroPython
MicroPython is the default variant of python electronics on the Raspberry Pi Pico. The library has been developed for many chassis.

```
from EduBot_CP import wheelBot_2

bot = wheelBot_2()
```
In order for it to work with the Pico and robotics board, you mst add the following parameter.
```
from EduBot_CP import wheelBot_2

bot = wheelBot_2(board_type="pico")
```
