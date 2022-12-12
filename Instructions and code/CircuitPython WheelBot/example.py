"""

"""

from EduBot_CP import wheelBot
import time
import board

bot=wheelBot(board_type="pico_1")

while True:
    bot.forward(50)
    time.sleep(1)
    bot.left(50)
    time.sleep(1)
    bot.forward(50)
    time.sleep(1)
bot.stop()
