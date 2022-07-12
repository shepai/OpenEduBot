"""
Servo robot using continuous rotation motors

Code by Dexter R Shepherd

"""

from EduBot import servoBot
import utime


a=servoBot(1,2)
val=10
a.servoWrite(1,0)
a.servoWrite(2,0)
utime.sleep(1)
for i in range(10): 
    a.servoWrite(1,val+10)
    a.servoWrite(2,val+10)
    utime.sleep(1)
    