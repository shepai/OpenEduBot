"""
Braitenbergs are simple agents that exhibit seeking behaviour.
This code uses the ultrasound sensor to run towards from obstacles.

If the robot is not moving towards the target, consider changing the ">" and "<"
symbols in lines 31 and 28 to be the opposite way round to go left and right.

Code by Dexter R Shepherd

"""


from EduBot import Old_WheelBot
import utime

robot = Old_WheelBot(trigPin=[12,5],echoPin=[15,4],in1=11,in2=10,in3=9,in4=8)
robot.stop()



while True:

    dist=robot.distance()

    #print(dist)
    if dist[0]<10 and dist[1]<10: #insignificant distance
        robot.stop()
    elif dist[0]>dist[1]: #ione sensor clsoer than othre
        print("r")
        robot.right(delay=0.5)
    elif dist[0]<dist[1]: #other sensor closer than sensor
        print("l")
        robot.left(delay=0.5)
    else:
        robot.forward()


    utime.sleep(1)
robot.stop()
