from machine import Pin,ADC
import utime

sensor1=ADC(27)
led=[Pin(2,Pin.OUT),Pin(3,Pin.OUT),Pin(4,Pin.OUT)]

voltage=4.8
def getRawPin(sensor):
    #this is if you have made your own sensor
    return 1-((sensor.read_u16() / 65535 * voltage)/voltage)

print(dir(led[0]))
while True:
    utime.sleep(0.5)
    val=getRawPin(sensor1)*100
    val
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
