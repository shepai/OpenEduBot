"""
Open Robotics library for educational use. This library gives access to a handful of chassis designs
with the aimed intension to be for cheaper robotics use without the need of expert programming.

Code written by:

Dexter R Shepherd, AI student at the University of Sussex
    https://www.linkedin.com/in/dexter-shepherd-1a4a991b8/
    https://shepai.github.io/

Debugged by:

Joshua Kybett, Computer Science Masters student at the University of Sussex

This code is open source, therefore free to distribute or modify. We only ask to credit original source.

"""
#import standard needed libraries
from machine import Pin
import utime
#import servo libraries
try:
    pass
except:
    print("Servo libraries are not in the directory. These will need to be installed before using servo chassis")
    #output more values
print("Loaded OpenEduBot Education library")

ValidGPIO=[i for i in range(28)] #valid pins
class WheelBot:
    """
    Requires:
    2 DC motors
    Motor driver
    Raspberry Pi Pico
    Two separate battery packs
        4xAA
        3XAA
    Ultrasound range sensor
    Breadboard (for ease)
    """
    def __init__(self,trigPin=26,echoPin=22,in1=18,in2=19,in3=20,in4=21):
        """
        Creates a wheel chassis bot for two DC motors using a motor driver and ultrasound sensor
        with given pins that the chassis can use connected to the Pico. Al must be GPIO pins
        @param trigPin is the pin that connects to the ultrasound sensor trigger pin
        @param echoPin is the pin that connects to the ultrasound sensor echo pin
        @param in1 connects to the motor driver in1 (motor1)
        @param in2 connects to the motor driver in2 (motor1)
        @param in3 connects to the motor driver in3 (motor2)
        @param in4 connects to the motor driver in4 (motor2)
        """
        assert in1 in ValidGPIO and in2 in ValidGPIO and in3 in ValidGPIO and in4 in ValidGPIO,"Invalid pin specified. Only use pins within "+str(ValidGPIO)
        if type(trigPin)==type([]) and type(echoPin)==type([]):
            assert len(trigPin)==len(echoPin),"Echo Pin and Trigger Pin list of pins are not equal. Place in format [trig1,trig2] and [echo1,echo2]"
            self.trigger = []
            self.echo = []
            for i in range(len(trigPin)):
                self.trigger.append(Pin(trigPin[i], Pin.OUT))
                assert trigPin.count(trigPin[i])==1 and echoPin.count(echoPin[i])==1 and trigPin[i] not in echoPin and echoPin[i] not in trigd=WheelBot(trigPin=[26,24],echoPin=[24,25],in1=24,in2=23,in3=22,in4=21)Pin, "You cannot have the same pin called multiple times" 
                self.echo.append(Pin(echoPin[i], Pin.IN))
        else: #use as default pins
            assert trigPin in ValidGPIO and echoPin in ValidGPIO, "Invalid pin specified. Only use pins within "+str(ValidGPIO)
            self.trigger = Pin(trigPin, Pin.OUT)
            self.echo = Pin(echoPin, Pin.IN)
        self.IN1 = Pin(in1, Pin.OUT)
        self.IN2 = Pin(in2, Pin.OUT)
        self.IN3 = Pin(in3, Pin.OUT)
        self.IN4 = Pin(in4, Pin.OUT)

    def distance(self):
       """
       Get the distance from the ultrasound sensor wired to the trigger and echo pins
       if multiple sensors are entered then return array of distances
       """
       self.trigger.low()
       utime.sleep_us(2)
       self.trigger.high()
       utime.sleep_us(5)
       self.trigger.low()
       while self.echo.value() == 0:
           signaloff = utime.ticks_us()
       while self.echo.value() == 1:
           signalon = utime.ticks_us()
       timepassed = signalon - signaloff
       distance = (timepassed * 0.0343) / 2
       return distance
    def forward(self):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        """
        self.motor1()
        self.motor2()
    def backward(self):
        """
        Move the robot backward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        """
        self.motor1(fir=True)
        self.motor2(fir=True)
    def left(self,delay=1):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        """
        self.motor1(fir=True)
        self.motor2()
        time.sleep(delay)
        self.stop()
    def right(self,delay=1):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        """
        self.motor1(fir=True)
        self.motor2()
        time.sleep(delay)
        self.stop()
    def motor1(self,fir=True):
        """
        Rotate the motor based on the direction
        @param fir decides which way it should rotate
        """
        if fir:
            self.IN1.value(1)  #spin forward
            self.IN2.value(0)
        else:
            self.IN1.value(0)  #spin forward
            self.IN2.value(1)
    def motor2(self,fir=True):
        """
        Rotate the motor based on the direction
        @param fir decides which way it should rotate
        """
        if fir:
            self.IN3.value(1)  #spin forward
            self.IN4.value(0)
        else:
            self.IN3.value(0)  #spin forward
            self.IN4.value(1)
    def stop(self):
        """
        Stop the robot by setting all signals to 0
        """
        self.IN1.value(0) 
        self.IN2.value(0) 
        self.IN3.value(0)   
        self.IN4.value(0) 


class ServoBot:
    pass


"""
robot = PALbot(trigPin=26,echoPin=22,in1=18,in2=19,in3=20,in4=21)
robot.stop()

robot.stop()
utime.sleep(1)
robot.motor1()
robot.motor2()
utime.sleep(10)
robot.stop()

#while True:
#    print(robot.distance())
#    utime.sleep(1)

while True:
    utime.sleep(0.5)
    dist=robot.distance()
    
    robot.motor1()
    robot.motor2()
    if dist<10:
        robot.motor1()
        robot.motor2(fir=False)
        utime.sleep(1)
"""
