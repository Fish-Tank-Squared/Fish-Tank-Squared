import gpiozero as gpio
from gpiozero.pins.rpigpio import RPiGPIOFactory as RPin
from gpiozero import LED
import math

factory = RPin()
#pins
VCC = 2
GND = 6
BIN2 = 17
BIN1 = 27
AIN1 = 23
AIN2 = 24
STBY = 25
PWMB = 12
PWMA = 13
STOP = 30 #set later

VCCPin = LED(VCC).pin
VCCPin.function = "output"
GNDPin = LED(GND).pin
GNDPin.function = "output"
BIN2Pin = LED(BIN2).pin
BIN2Pin.function = "output"
BIN1Pin = LED(BIN1).pin
BIN1Pin.function = "output"
AIN1Pin = LED(AIN1).pin
AIN1Pin.function = "output"
AIN2Pin = LED(AIN2).pin
AIN2Pin.function = "output"
STBYPin = LED(STBY).pin
STBYPin.function = "output"
PWMBPin = LED(PWMB).pin
PWMBPin.function = "output"
PWMAPin = LED(PWMA).pin
PWMAPin.function = "output"
STOPPin = LED(STOP).pin
STOPPin.function = "input"

freq = 200
PWMAPin.frequency = freq
PWMBPin.frequency = freq

def turnOnMotors():
    STBYPin.state = 1
def turnOffMoters():
    STBYPin.state = 0

#speed between 1 and -1
def setMotorA(speed):
    if speed < 0:
        AIN1Pin.state = 1
        AIN2Pin.state = 0
    else:
        AIN1Pin.state = 0
        AIN2Pin.state = 1
    PWMAPin.state = math.abs(speed)

def setMotorB(speed):
    if speed < 0:
        BIN1Pin.state = 1
        BIN2Pin.state = 0
    else:
        BIN1Pin.state = 0
        BIN2Pin.state = 1
    PWMBPin.state = math.abs(speed)

def close():
    VCCPin.close()
    GNDPin.close()
    BIN2Pin.close()
    BIN1Pin.close()
    AIN1Pin.close()
    AIN2Pin.close()
    STBYPin.close()
    PWMBPin.close()
    PWMAPin.close()
    STOPPin.close()

if __name__ == "__main__":
    print("running test")
    close()

