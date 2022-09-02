import board
import digitalio
from analogio import AnalogIn
import time
import pwmio


LED_PINS = [board.GP0,
            board.GP1,
            board.GP2,
            board.GP3,
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
            board.GP16,
            board.GP17]

LEDS = []
for pin in LED_PINS:
    # Set pins as digital output
    digout = digitalio.DigitalInOut(pin)
    digout.direction = digitalio.Direction.OUTPUT
    LEDS.append(digout)

sensor = AnalogIn(board.A0)

def showPins(val):
    for pin in LEDS:
        pin.value=False
    ind=int(len(LEDS)*val)
    for i in range(ind):
        LEDS[i].value=True

def get_voltage(pin):
    return max(min(1-((pin.value * 3.3) / 65536),1),0)

def getRawPin(pin):
    #this is if you have made your own sensor
    return (sensor.value / 65535 * pin.reference_voltage)/3.7

while True:
    intensity=get_voltage(sensor)
    print((intensity,"% light intensity"))
    showPins(intensity)
    time.sleep(0.1)
