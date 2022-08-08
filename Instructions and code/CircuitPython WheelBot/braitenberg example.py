"""

"""

from EduBot_CP import wheelBot_2
import time
import board
from analogio import AnalogIn

s1 = AnalogIn(board.GP28)
s2 = AnalogIn(board.GP26)

bot=wheelBot_2()

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

while True:
    r1,r2=(get_voltage(s1),get_voltage(s2))
    
    if int(r1)>int(r2):
        bot.left()
    elif int(r1)<int(r2):
        bot.right()
    else:
        bot.forward(50)
    time.sleep(0.5)
    bot.stop()


