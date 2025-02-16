import gpiozero as gpio
from gpiozero.pins.rpigpio import RPiGPIOPin as RPin
import math
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
STOP = -1 #set later

VCCPin = RPin(VCC)
VCCPin.function = "output"
GNDPin = RPin(GND)
GNDPin.function = "output"
BIN2Pin = RPin(BIN2)
BIN2Pin.function = "output"
BIN1Pin = RPin(BIN1)
BIN1Pin.function = "output"
AIN1Pin = RPin(AIN1)
AIN1Pin.function = "output"
AIN2Pin = RPin(AIN2)
AIN2Pin.function = "output"
STBYPin = RPin(STBY)
STBYPin.function = "output"
PWMBPin = RPin(PWMB)
PWMBPin.function = "output"
PWMAPin = RPin(PWMA)
PWMAPin.function = "output"
STOPPin = RPin(STOP)
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

