"""
Light braightenberg robot
The light sensors allow close quarter sensing incase of collision.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""

from EduBot import wheelBot_2
import utime
from machine import Pin,ADC
from random import choice

#setup the robot
robot = wheelBot_2()
robot.stop()

sensor1=Pin(26,Pin.IN)
sensor2=Pin(27,Pin.IN)

sensor1=ADC(26)
sensor2=ADC(27)

while True:
    #gather sensor data
    s1=int(sensor1.read_u16()/10)
    s2=int(sensor2.read_u16()/10)

    print(s1,s2)
    
    if abs(s2-s1)<150: #noise 
        robot.forward(20)
        utime.sleep(0.8)
        robot.stop()
    elif s1>s2: #just one obstacle
        robot.left(delay=0.25)
        robot.stop()
    elif s2>s1: #just one obstacle
        robot.right(delay=0.25)
        robot.stop()

    utime.sleep(0.5)
robot.stop()


