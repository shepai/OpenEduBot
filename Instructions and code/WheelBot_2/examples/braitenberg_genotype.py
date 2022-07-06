"""
Braightenberg robot for crossing the reality gap
The light sensors allow light following behaviours.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

"""

from EduBot import wheelBot_2
import utime
from machine import ADC

GENOTYPE=[ 8.08404537,  9.64568124,  2.99583673,  9.69069223,  0.60330581, -0.10944596]
a=wheelBot_2()
sensor1=ADC(26)
sensor2=ADC(27)

#change the sensor gain to preference
sensor_gain=0.5

def calc(genotype):
    w_ll,w_lr,w_rl,w_rr,bl,br = genotype
    # Calculate (square) distance to element
    dl=int(sensor1.read_u16()/1000)
    dr=int(sensor2.read_u16()/1000)

    #  Calculate local intensity
    il = sensor_gain/dl;
    ir = sensor_gain/dr;
    #weights times inputs plus bias
    lm = il*w_ll + ir*w_rl + bl;
    rm = il*w_lr + ir*w_rr + br;
    print(">",dl,dr)

    print(lm,rm)
    #change divider as you please
    return lm/50,rm/50

while True:
    speed1,speed2=calc(GENOTYPE) #place your genotype in here
    utime.sleep(1)
    #do not change this code
    #pin directions speed
    a.motorOn(4,"f",100*speed1)
    a.motorOn(3,"f",100*speed2)
