"""
Braightenberg robot for crossing the reality gap
The light sensors allow light following behaviours.

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd

DEBUGGIN TIPS:

If your robot is running away from light, then you should switch the sensor cables around (or switch the pins in the code)
"""

from EduBot import wheelBot
import utime
from machine import ADC

GENOTYPE=[ 8.08404537,  9.64568124,  2.99583673,  9.69069223,  0.60330581, -0.10944596] #add genotype

robot=wheelBot() #the robot from the library

#setup the pins for analog read
sensor1=ADC(26)
sensor2=ADC(27)

#read background noise
ST1=sensor1.read_u16()//100
ST2=sensor2.read_u16()//100

def getReading(sen,ST=200):
    #read the sensor pin and convert to percentage of light
    return max((ST-sen.read_u16()//100)/ST,0.01)

#change the sensor gain to preference
sensor_gain=0.5

def calc(genotype):
    w_ll,w_lr,w_rl,w_rr,bl,br = genotype
    #  Calculate local intensity
    il=getReading(sensor1,ST=ST1)
    ir =getReading(sensor2,ST=ST2)
    #weights times inputs plus bias
    lm = il*w_ll + ir*w_rl + bl;
    rm = il*w_lr + ir*w_rr + br;
    print(">",dl,dr)

    print(lm,rm)
    #change divider as you please
    return lm/50,rm/50

while True:
    speed1,speed2=calc(GENOTYPE) #place your genotype in here
    #do not change this code
    #pin directions speed

    #still keep slow or moving forward
    speed_1=max(speed1//2,20)
    speed_2=max(speed2//2,20)

    robot.motorOn(4, "f", speed_1)
    robot.motorOn(3, "f", speed_2)
