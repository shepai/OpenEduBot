

#Section 1

from EduBot_CP import wheelBot_2
from machine import Pin,ADC
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction, Pull

bot = wheelBot_2(board_type="pico")

digital_pin=Pin(27,Pin.IN)
analog_pin=ADC(26)

s1 = AnalogIn(board.GP26)

def get_voltage(pin):
    return (pin.value * 3.3)

s2 = DigitalInOut(board.GP27)
s2.direction = Direction.INPUT

print(s2.value)
print(digital_pin.value())
print(analog_pin.read_u16())
print(get_intensity(s1))
