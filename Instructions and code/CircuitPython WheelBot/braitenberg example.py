"""

"""

from EduBot_CP import wheelBot
import time
import board
from analogio import AnalogIn

s1 = AnalogIn(board.GP28)
s2 = AnalogIn(board.GP26)

bot=wheelBot(board_type="pico_1")
bot.motorOn(2,"f",40)
bot.forward(50)
print("..")
time.sleep(10)
def get_intensity(pin):
    return max(min(1-((pin.value * 3.3) / 65536),1),0)

while True:
    r1,r2=(get_intensity(s1)*10,get_intensity(s2)*10)

    if int(r1)>int(r2):
        bot.left()
    elif int(r1)<int(r2):
        bot.right()
    else:
        bot.forward(50)
    time.sleep(0.5)
    bot.stop()
