from EduBot_CP import wheelBot
import time
import board
from analogio import AnalogIn

s1 = AnalogIn(board.GP28)
s2 = AnalogIn(board.GP26)

#change the sensor gain to preference
sensor_gain=0.5
def get_intensity(pint):
    return (pin.value*3.3) /65536

def calc(genotype):
    w_ll,w_lr,w_rl,w_rr,bl,br = (genotype[0],genotype[1],genotype[2],genotype[3],genotype[4],genotype[5])
    # Calculate (square) distance to element
    #  Calculate local intensity
    il,ir=(get_intensity(s1)*10,get_intensity(s2)*10)

    #weights times inputs plus bias
    lm = il*w_ll + ir*w_rl + bl;
    rm = il*w_lr + ir*w_rr + br;
    print(">",dl,dr)
    print(lm,rm)
    return lm,rm
