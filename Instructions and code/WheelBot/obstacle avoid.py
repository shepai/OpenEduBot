"""
This code makes use of two ultrasound sensors for long distance planning, but also two MH light sensors
The light sensors allow close quarter sensing incase of collision.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""


import utime
from machine import Pin
from random import choice

robot = WheelBot(trigPin=[12,5],echoPin=[15,4],in1=11,in2=10,in3=9,in4=8)
robot.stop()

sensor1=Pin(26,Pin.IN)
sensor2=Pin(27,Pin.IN)


while True:
    s1=sensor1.value() #get whether or not theres an obstacle on one side
    s2=sensor2.value() #get whether or not theres an obstacle on the other side
    dist=robot.distance() #get sensor value from both ultrasound sensors
    #print(dist)
    if s1==0 and s2==0: #big obstacle infront of both robots
        robot.backward()
        utime.sleep(0.8)
        robot.right(delay=choice([0.15,0.25])) #use random choice so that the robot doesn't get stuck turning left and right
        robot.stop()
    elif s1==0: #just one obstacle
        print("r")
        robot.right(delay=choice([0.15,0.25]))
        robot.stop()
    elif s2==0: #just one obstacle
        print("r")
        robot.left(delay=choice([0.15,0.25]))
        robot.stop()
    elif (dist[0]>40 and dist[1]>40): #insignificant distance
        print("f")
        robot.forward()
        utime.sleep(0.8) #only jump forward slightly to give time for snesing
        robot.stop()
    elif dist[0]==dist[1]: #the istances are the same but there is an obstacle
        robot.backward()
        utime.sleep(0.8)
        robot.right(delay=choice([0.15,0.25]))
        robot.stop()

    elif dist[0]<dist[1]: #pne sensor clsoer than othre
        print("r")
        robot.right(delay=choice([0.15,0.25]))
        robot.stop()
    else: #other sensor closer than sensor
        print("l")
        robot.left(delay=choice([0.15,0.25]))
        robot.stop()
    utime.sleep(0.5)
robot.stop()
