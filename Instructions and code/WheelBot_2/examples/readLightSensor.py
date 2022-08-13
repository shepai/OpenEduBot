from machine import Pin,ADC
import utime

sensor1=ADC(26)
def getReading(sen):
    return (200-sen.read_u16()//100)/200
while True:
    utime.sleep(0.5)
    print(getReading(sensor1))