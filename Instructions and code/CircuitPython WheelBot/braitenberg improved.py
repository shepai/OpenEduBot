"""

"""

from EduBot_CP import wheelBot
import time
import board
from analogio import AnalogIn

s1 = AnalogIn(board.GP26)
s2 = AnalogIn(board.GP27)

bot=wheelBot()

def get_intensity(pin):
    return max(min(1-((pin.value * 3.3) / 65536),1),0)

while True:
    r1,r2=(get_intensity(s1)*100,get_intensity(s2)*100)

    print(r1,r2)
    bot.motor1_move(r1/2)
    bot.motor2_move(r2/2)

    time.sleep(0.5)
    bot.stop()
