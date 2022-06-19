"""
Braitenbergs are simple agents that exhibit seeking behaviour.
This code uses the ultrasound sensor to run away from obstacles.

Code by Dexter R Shepherd

"""

from EduBot import WheelBot
import utime

robot = WheelBot(trigPin=[12,5],echoPin=[15,4],in1=11,in2=10,in3=9,in4=8)
robot.stop()



while True:

    dist=robot.distance()
    #print(dist)
    if abs(dist[0]-dist[1])<10 or (dist[0]>40 and dist[1]>40): #insignificant distance
        print("f")
        robot.forward()
    elif dist[0]>dist[1]: #ione sensor clsoer than othre
        print("r")
        robot.right(delay=0.5)

    else: #other sensor closer than sensor
        print("l")
        robot.left(delay=0.5)


    utime.sleep(1)
robot.stop()
