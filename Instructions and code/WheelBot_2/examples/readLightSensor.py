from machine import Pin,ADC
import utime

sensor1=ADC(26)
def getReading(sen):
    return max((200-sen.read_u16()//100)/200,0)
while True:
    utime.sleep(0.5)
    print(getReading(sensor1)*100,"% Light intensity")