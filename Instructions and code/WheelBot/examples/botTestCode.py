"""
This code is used as an all in one test code to check the bot is built correctly by the user

The sensor pins are read at 26 and 27, if the robot is not turning away from the collision,
consider switching the pins around (26 & 27).

Code by Dexter R Shepherd


DEBUGGIN TIPS:

If your robot is running away from light, then you should switch the sensor cables around (or switch the pins in the code)

"""
sensor1=ADC(27)
sensor2=ADC(26)


import utime
from machine import Pin,ADC
import machine
from random import choice

class wheelBot:
    """
    Requires:
    2 DC motors
    Pico Robotics board
    Raspberry Pi Pico
    Battery packs
        4xAA
    Light sensitivity sensors (optional)

    The I2C communication part of the code was taken from the KitronikPicoRobotics library
    which was used within our own library function to make the control easier for all ages
    """

    #Class variables - these should be the same for all instances of the class.
    # If you wanted to write some code that stepped through
    # the servos or motors then this is the Base and size to do that
    SRV_REG_BASE = 0x08
    MOT_REG_BASE = 0x28
    REG_OFFSET = 4
    def __init__(self, I2CAddress=108,sda=8,scl=9,board_type="pico"):
        self.board_type=board_type
        if self.board_type=="pico":
            self.CHIP_ADDRESS = 108
            sda=machine.Pin(sda)
            scl=machine.Pin(scl)
            self.i2c=machine.I2C(0,sda=sda, scl=scl, freq=100000)
            self.initPCA()
        elif self.board_type=="pico_1":
            Motor1ForwardPin = machine.Pin(3)
            Motor1ReversePin = machine.Pin(2)
            Motor2ForwardPin = machine.Pin(6)
            Motor2ReversePin = machine.Pin(7)
            PWMFreq = 10000
            self.motor1Forward=machine.PWM(Motor1ForwardPin)
            self.motor1Reverse=machine.PWM(Motor1ReversePin)
            self.motor2Forward=machine.PWM(Motor2ForwardPin)
            self.motor2Reverse=machine.PWM(Motor2ReversePin)
            self.motor1Forward.freq(PWMFreq)
            self.motor1Reverse.freq(PWMFreq)
            self.motor2Forward.freq(PWMFreq)
            self.motor2Reverse.freq(PWMFreq)
    #to perform a software reset on the PCA chip.
    #Separate from the init function so we can reset at any point if required - useful for development...
    def swReset(self):
        self.i2c.writeto(0,"\x06")

    #setup the PCA chip for 50Hz and zero out registers.
    def initPCA(self):
        self.swReset() #make sure we are in a known position
        #setup the prescale to have 20mS pulse repetition - this is dictated by the servos.
        self.i2c.writeto_mem(108,0xfe,"\x78")
        #block write outputs to off
        self.i2c.writeto_mem(108,0xfa,"\x00")
        self.i2c.writeto_mem(108,0xfb,"\x00")
        self.i2c.writeto_mem(108,0xfc,"\x00")
        self.i2c.writeto_mem(108,0xfd,"\x00")
        #come out of sleep
        self.i2c.writeto_mem(108,0x00,"\x01")

    def setPrescaleReg(self):
        i2c.writeto_mem(108,0xfe,"\x78")
    #Driving the motor is simpler than the servo - just convert 0-100% to 0-4095 and push it to the correct registers.
    #each motor has 4 writes - low and high bytes for a pair of registers.
    def motorOn(self,motor, direction, speed):
        #cap speed to 0-100%
        if (speed<0):
            speed = 0
        elif (speed>100):
            speed=100
        if self.board_type=="pico":
            motorReg = self.MOT_REG_BASE + (2 * (motor - 1) * self.REG_OFFSET)
            PWMVal = int(speed * 40.95)
            lowByte = PWMVal & 0xFF
            highByte = (PWMVal>>8) & 0xFF #motors can use all 0-4096
            #print (motor, direction, "LB ",lowByte," HB ",highByte)
            if direction == "f":
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg,bytes([lowByte]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+1,bytes([highByte]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+4,bytes([0]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+5,bytes([0]))
            elif direction == "r":
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+4,bytes([lowByte]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+5,bytes([highByte]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg,bytes([0]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+1,bytes([0]))
            else:
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+4,bytes([0]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+5,bytes([0]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg,bytes([0]))
                self.i2c.writeto_mem(self.CHIP_ADDRESS, motorReg+1,bytes([0]))
                raise Exception("INVALID DIRECTION")
        elif self.board_type=="pico_1":
            PWM = int(speed*655.35)
            motor-=2
            if motor == 1:
                if direction == "f":
                    self.motor1Forward.duty_u16(PWM)
                    self.motor1Reverse.duty_u16(0)
                elif direction == "r":
                    self.motor1Forward.duty_u16(0)
                    self.motor1Reverse.duty_u16(PWM)
                else:
                    raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
            elif motor == 2:
                if direction == "f":
                    self.motor2Forward.duty_u16(PWM)
                    self.motor2Reverse.duty_u16(0)
                elif direction == "r":
                    self.motor2Forward.duty_u16(0)
                    self.motor2Reverse.duty_u16(PWM)
                else:
                    raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
            else:
                raise Exception("INVALID MOTOR") #harsh, but at least you'll know
    #To turn off set the speed to 0...
    def motorOff(self,motor):
        self.motorOn(motor,"f",0)
    def forward(self,speed):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is the speed that the robot will move at
        """
        self.motorOn(4, "f", speed)
        self.motorOn(3, "f", speed)
    def backward(self,speed):
        """
        Move the robot backward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        """
        self.motorOn(4, "r", speed)
        self.motorOn(3, "r", speed)
    def left(self,speed=30,delay=1):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn left for
        """
        self.motorOff(4)
        self.motorOff(3)
        self.motorOn(4, "f", speed)
        self.motorOn(3, "r", speed)
        utime.sleep(delay)
        #self.stop()
    def right(self,speed=30,delay=1):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn right for
        """
        self.motorOff(4)
        self.motorOff(3)
        self.motorOn(4, "r", speed)
        self.motorOn(3, "f", speed)
        utime.sleep(delay)
        #self.stop()

    def stop(self):
        """
        Stop the robot by setting all signals to 0
        """
        self.motorOff(4)
        self.motorOff(3)

#setup the robot
robot = wheelBot() #board_type="pico_1"
robot.stop()

#switch pins if te robot is moving away from light


voltage=4.8
def getRawPin(sensor):
    #this is if you have made your own sensor
    return 1-(sensor.read_u16() / 65535 * voltage)/voltage

while True:
    #gather sensor data
    s1=getRawPin(sensor1)/2
    s2=getRawPin(sensor2)/2

    print(s1,s2)
    #still keep slow or moving forward
    speed_1=max(100*s1,20)
    speed_2=max(100*s2,20)
    #print(speed_1,speed_2)
    #utime.sleep(0.5)
    #switch r to f if the robot is moving backwards
    robot.motorOn(4, "r", speed_1)
    robot.motorOn(3, "r", speed_2)
