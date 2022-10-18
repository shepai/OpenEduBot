"""
Light braightenberg robot

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd


DEBUGGIN TIPS:

If your robot is running away from light, then you should switch the sensor cables around (or switch the pins in the code)

"""

from EduBot import wheelBot
import utime
from machine import Pin,ADC
from random import choice

#setup the robot
robot = wheelBot() #board_type="pico_1"
robot.stop()

#switch pins if te robot is moving away from light
sensor1=ADC(27)
sensor2=ADC(26)

voltage=4.8
def getRawPin(sensor):
    #this is if you have made your own sensor
    return 1-(sensor.read_u16() / 65535 * voltage)/voltage

while True:
    #gather sensor data
    s1=getRawPin(sensor1)/2
    s2=getRawPin(sensor2)/2

    print(s1,s2)
    #still keep slow or moving forward
    speed_1=max(100*s1,20)
    speed_2=max(100*s2,20)
    #print(speed_1,speed_2)
    #utime.sleep(0.5)
    #switch r to f if the robot is moving backwards
    robot.motorOn(4, "r", speed_1)
    robot.motorOn(3, "r", speed_2)
