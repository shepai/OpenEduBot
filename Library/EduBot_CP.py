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
import busio
import time
import pwmio
from adafruit_motor import servo, motor

class wheelBot:
    SRV_REG_BASE = 0x08
    MOT_REG_BASE = 0x28
    REG_OFFSET = 4
    def initPCA(self):
        self.swReset() #make sure we are in a known position
        #setup the prescale to have 20mS pulse repetition - this is dictated by the servos.
        buf = bytearray(2)
        buf[0] = 0xfe
        buf[1] = 0x78
        self.i2c.writeto(self.CHIP_ADDRESS,buf)
        #block write outputs to off
        for blockReg in range(0xFA, 0xFE, 1):
            buf[0] = blockReg
            buf[1] = 0x00
            self.i2c.writeto(self.CHIP_ADDRESS, buf)
        #come out of sleep
        buf[0] = 0x00
        buf[1] = 0x01
        self.i2c.writeto(self.CHIP_ADDRESS, buf)
        
    def __init__(self,m1a=board.GP8,m1b=board.GP9,m2a=board.GP10,m2b=board.GP11,board_type="default"):
        """
        Initialize the wheel bot and the pins going to the motor driver
        @param m1a
        @param m1b
        @param m2a
        @param m2b
        """
        self.board_type=board_type
        # Initialize DC motors
        self.mA=3
        self.mB=4
        if board_type.lower()=="pico": #allow for different board types
            self.CHIP_ADDRESS = 108
            self.i2c = busio.I2C(board.GP9, board.GP8)
            #sda=board.Pin(sda)
            #scl=board.Pin(scl)
            #self.i2c=board.I2C(0,sda=sda, scl=scl, freq=100000)
            self.initPCA()
        elif self.board_type=="pico_1":
            Motor1ForwardPin = board.GP3
            Motor1ReversePin = board.GP2
            Motor2ForwardPin = board.GP6
            Motor2ReversePin = board.GP7
            PWMFreq = 10000
            self.motor1Forward=pwmio.PWMOut(Motor1ForwardPin,frequency=PWMFreq)
            self.motor1Reverse=pwmio.PWMOut(Motor1ReversePin,frequency=PWMFreq)
            self.motor2Forward=pwmio.PWMOut(Motor2ForwardPin,frequency=PWMFreq)
            self.motor2Reverse=pwmio.PWMOut(Motor2ReversePin,frequency=PWMFreq)
            self.mA=1
            self.mB=2
        else:
            m1a = pwmio.PWMOut(m1a, frequency=50)
            m1b = pwmio.PWMOut(m1b, frequency=50)
            self.motor1 = motor.DCMotor(m1a, m1b)
            m2a = pwmio.PWMOut(m2a, frequency=50)
            m2b = pwmio.PWMOut(m2b, frequency=50)
            self.motor2 = motor.DCMotor(m2a, m2b)
    def swReset(self):
        while (self.i2c.try_lock() != True):
            time.sleep(0.001)
        self.i2c.writeto(0,"\x06")
    def stop(self):
        """
        Stop the robot by setting all signals to 0
        """
        if "pico" in self.board_type:
            self.motorOff(self.mB)
            self.motorOff(self.mA)
        else:
            self.motor1.throttle = 0  # motor1.throttle = None to spin freely
            self.motor2.throttle = 0
    def forward(self,speed):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is the speed that the robot will move at
        """
        if "pico" in self.board_type:
            self.motorOn(self.mB, "r", speed)
            self.motorOn(self.mA, "r", speed)
        else:
            self.motor1.throttle = -1*(speed/100)
            self.motor2.throttle = 1*(speed/100)
    def left(self,speed=50,delay=0.5):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn right for
        """
        if "pico" in self.board_type:
            self.motorOff(self.mB)
            self.motorOff(self.mA)
            self.motorOn(self.mB, "r", speed)
            self.motorOn(self.mA, "f", speed)
        else:
            self.stop()
            self.motor1.throttle = 1*(speed/100)
            self.motor2.throttle = 1*(speed/100)
        time.sleep(delay)
    def setMotors(self,a,b):
        assert (a>=1 and a<=4 and b>=1 and b<=4),"Incorrect motor number "
        self.mA=a
        self.mB=b
    def right(self,speed=50,delay=0.5):
        """
        Move the robot forward by rotating both motors the same direction. This relies on the robot motors being wired the same way
        @param speed is how quickly it rotates
        @param delay is how long the robot will turn left for
        """
        if "pico" in self.board_type:
            self.motorOff(self.mB)
            self.motorOff(self.mA)
            self.motorOn(self.mB, "f", speed)
            self.motorOn(self.mA, "r", speed)
        else:
            self.stop()
            self.motor1.throttle = -1*(speed/100)
            self.motor2.throttle = -1*(speed/100)
        time.sleep(delay)
    def backward(self,speed):
        if "pico" in self.board_type:
            self.motorOn(self.mB, "f", speed)
            self.motorOn(self.mA, "f", speed)
        else:
            self.motor1.throttle = 1*(speed/100)
            self.motor2.throttle = -1*(speed/100)
    def motor1_move(self,speed):
        if "pico" in self.board_type:
            self.motorOn(self.mA, "r", 100*(speed/100))
        else:
            self.motor1.throttle = 1*(speed/100)
    def motor2_move(self,speed):
        if "pico" in self.board_type:
            self.motorOn(self.mB, "r", 100*(speed/100))
        else:
            self.motor2.throttle = 1*(speed/100)
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
            buf = bytearray(2)
            #print (motor, direction, "LB ",lowByte," HB ",highByte)
            if direction == "f":
                buf[0] = motorReg
                buf[1] = lowByte
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+1
                buf[1] = highByte
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+4
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+5
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
            elif direction == "r":
                buf[0] = motorReg+4
                buf[1] = lowByte
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+5
                buf[1] = highByte
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+1
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
            else:
                buf[0] = motorReg
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+1
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+4
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                buf[0] = motorReg+5
                buf[1] = 0x00
                self.i2c.writeto(self.CHIP_ADDRESS,buf)
                raise Exception("INVALID DIRECTION")
        elif self.board_type=="pico_1":
            #convert 0-100 to 0-65535
            PWM = int(speed*655.35)
            if motor == 1:
                if direction == "f":
                    self.motor1Forward.duty_cycle = PWM
                    self.motor1Reverse.duty_cycle = 0
                elif direction == "r":
                    self.motor1Forward.duty_cycle = 0
                    self.motor1Reverse.duty_cycle = PWM
                else:
                    raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
            elif motor == 2:
                if direction == "f":
                    self.motor2Forward.duty_cycle = PWM
                    self.motor2Reverse.duty_cycle = 0
                elif direction == "r":
                    self.motor2Forward.duty_cycle = 0
                    self.motor2Reverse.duty_cycle = PWM
                else:
                    raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
            else:
                raise Exception("INVALID MOTOR") #harsh, but at least you'll know
    #To turn off set the speed to 0...
    def motorOff(self,motor):
        self.motorOn(motor,"f",0)
    #each motor has 4 writes - low and high bytes for a pair of registers. 
    




