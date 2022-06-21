"""
Light braightenberg robot
The light sensors allow close quarter sensing incase of collision.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""

from EduBot import WheelBot
import utime
from machine import Pin,ADC
from random import choice

robot = WheelBot(trigPin=[12,5],echoPin=[15,4],in1=11,in2=10,in3=9,in4=8)
robot.stop()

sensor1=Pin(26,Pin.IN)
sensor2=Pin(27,Pin.IN)

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
    elif abs(s2-s1)<150: #noise 
        print("f")
        robot.forward()
        utime.sleep(0.8)
        robot.right(delay=choice([0.15,0.25])) #use random choice so that the robot doesn't get stuck turning left and right
        robot.stop()
    elif s1>s2: #just one obstacle
        print("r")
        #robot.backward()
        #utime.sleep(0.8)
        robot.right(delay=0.05)
        robot.stop()
    elif s2>s1: #just one obstacle
        print("l")
        #robot.backward()
        #utime.sleep(0.8)
        robot.left(delay=0.05)
        robot.stop()
    
    
    utime.sleep(0.5)
robot.stop()


