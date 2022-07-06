"""
Light braightenberg robot
The light sensors allow light following behaviours.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""

from EduBot import WheelBot
import utime
from machine import Pin,ADC
from random import choice

robot = WheelBot() #wheel bot chassis pins
robot.stop()

#take pins as analog as to get a varied reading
sensor1=ADC(26)
sensor2=ADC(27)

while True:
    s1=int(sensor1.read_u16()/10)
    s2=int(sensor2.read_u16()/10)
    print(s1,s2)
    if abs(s2-s1)<150: #filter noise and go forward if no light is found
        #more elegant solutions would rotate around and find the lightest angle
        print("f")
        robot.forward()
        utime.sleep(0.8)
        robot.stop() #implement stops
    elif s1>s2: #move towards the lightest sensor
        print("r")
        robot.right(delay=0.05)
        robot.stop()
    elif s2>s1: #move towards the lightest sensor
        print("l")
        robot.left(delay=0.05)
        robot.stop()


    utime.sleep(0.5)
robot.stop()
