from machine import Pin,ADC
import utime

sensor1=ADC(26)
led=[Pin(2,Pin.OUT),Pin(3,Pin.OUT),Pin(4,Pin.OUT)]

def getReading(sen):
    return max((200-sen.read_u16()//100)/200,0)

def getRawPin(sensor):
    #this is if you have made your own sensor
    return (sensor.read_u16() / 65535 * 3.7)/3.7

print(dir(led[0]))
while True:
    utime.sleep(0.5)
    val=getRawPin(sensor1)*100
    print(val,"% Light intensity")
    if val>80:
        led[2].high()
        led[1].high()
        led[0].high()
    elif val>65:
        led[2].low()
        led[1].high()
        led[0].high()
    elif val>50:
        led[2].low()
        led[1].low()
        led[0].high()
    else:
        led[2].low()
        led[1].low()
        led[0].low()
