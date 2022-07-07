"""
Robot code for going forward, urning and going backwards. 

Code by Dexter R Shepherd

"""

from EduBot import wheelBot_2
import utime

a=wheelBot_2()

while True:
    a.forward(25) #move the robot forward
    utime.sleep(4) #move robot for 4 seconds
    a.right(speed=25,delay=0.4) #turn slowly
    utime.sleep(1)
    a.left(speed=25,delay=0.4) #turn slowly
    utime.sleep(1)
    a.backward(25) #move robot back
    utime.sleep(4)
