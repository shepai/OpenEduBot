"""
Servo robot using continuous rotation motors

Code by Dexter R Shepherd

"""

from EduBot import servoBot
import utime


a=servoBot(1,2)

a.servoWrite(1,40)
a.servoWrite(2,140)
"""
for i in range(10):
    a.servoWrite(1,0)
    a.servoWrite(2,0)
    utime.sleep(1)
    a.servoWrite(1,180)
    a.servoWrite(2,180)
    utime.sleep(1)
    """