"""
Light braightenberg robot

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

 
DEBUGGIN TIPS:

If your robot is running away from light, then you should switch the sensor cables around (or switch the pins in the code)

"""
from EduBot_CP import wheelBot
import time
import board
from analogio import AnalogIn

s2 = AnalogIn(board.GP26)
s1 = AnalogIn(board.GP27)

bot=wheelBot()

#get background noise
ST1=s1.value * 3.3
ST2=s2.value * 3.3


def get_intensity(pin,M=65536):
    return max(min(1-((pin.value * 3.3) / M),1),0)

while True:
    r1,r2=(int(get_intensity(s1,M=ST1)*100),int(get_intensity(s2,M=ST2)*100))

    print(r1,r2)
    
    #move at full speed
    bot.motor1_move(max(r1,20) *-1) #remove *-1 for alternate direction
    bot.motor2_move(max(r2,20))


