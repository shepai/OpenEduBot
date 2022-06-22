"""
Light braightenberg robot
The light sensors allow light following behaviours.
This robot design does not use motor speed like the original design suggests for
simplicity of robot.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""

from EduBot import WheelBot
import utime
from machine import Pin,ADC
from random import choice

robot = WheelBot(trigPin=[12,5],echoPin=[15,4],in1=11,in2=10,in3=9,in4=8) #wheel bot chassis pins
robot.stop()

#take pins as analog as to get a varied reading
sensor1=ADC(26)
sensor2=ADC(27)

while True:
    s1=int(sensor1.read_u16()/10)
    s2=int(sensor2.read_u16()/10)
    #s1=sensor1.value() #get whether or not theres an obstacle on one side
    #s2=sensor2.value() #get whether or not theres an obstacle on the other side
    dist=robot.distance() #get sensor value from both ultrasound sensors
    print(s1,s2)
    if (dist[0]<=10 and dist[1]<=10): #insignificant distance
        robot.stop()
    elif abs(s2-s1)<150: #filter noise and go forward if no light is found
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


