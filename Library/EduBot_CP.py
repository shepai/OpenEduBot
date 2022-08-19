"""
Open Robotics library for educational use. This library gives access to a handful of chassis designs
with the aimed intension to be for cheaper robotics use without the need of expert programming.

This version is for circuit python devices. It was stested using the MakerPi

Code written by:

Dexter R Shepherd, AI student at the University of Sussex
    https://www.linkedin.com/in/dexter-shepherd-1a4a991b8/
    https://shepai.github.io/

This code is open source, therefore free to distribute or modify. We only ask to credit original source.

"""

import board
import digitalio
import simpleio
import time
import pwmio
from adafruit_motor import servo, motor

class wheelBot_2:
    def __init__(self,m1a=board.GP8,m1b=board.GP9,m2a=board.GP10,m2b=board.GP11):
        """
        Initialize the wheel bot and the pins going to the motor driver
        @param m1a
        @param m1b
        @param m2a
        @param m2b
        """
        # Initialize DC motors
        m1a = pwmio.PWMOut(m1a, frequency=50)
        m1b = pwmio.PWMOut(m1b, frequency=50)
        self.motor1 = motor.DCMotor(m1a, m1b)
        m2a = pwmio.PWMOut(m2a, frequency=50)
        m2b = pwmio.PWMOut(m2b, frequency=50)
        self.motor2 = motor.DCMotor(m2a, m2b)
    def stop(self):
        """
        Stop the robot by setting all signals to 0
        """
        self.motor1.throttle = 0  # motor1.throttle = None to spin freely
        self.motor2.throttle = 0
    def forward(self,speed):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is the speed that the robot will move at
        """
        self.motor1.throttle = -1*(speed/100) 
        self.motor2.throttle = 1*(speed/100)
    def left(self,speed=50,delay=0.5):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn right for
        """
        self.stop()
        self.motor1.throttle = 1*(speed/100)  
        self.motor2.throttle = 1*(speed/100)
        time.sleep(delay)
    def right(self,speed=50,delay=0.5):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn left for
        """
        self.stop()
        self.motor1.throttle = -1*(speed/100)  
        self.motor2.throttle = -1*(speed/100)
        time.sleep(delay)
    def backward(self,speed):
        self.motor1.throttle = 1*(speed/100) 
        self.motor2.throttle = -1*(speed/100)
    def motor1_move(self,speed):
        self.motor1.throttle = 1*(speed/100)
    def motor2_move(self,speed):
        self.motor2.throttle = 1*(speed/100) 
        

