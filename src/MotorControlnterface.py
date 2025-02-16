import gpiozero as gpio
from gpiozero.pins.rpigpio import RPiGPIOPin as RPin
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


VCCPin = RPin(2)
VCCPin.function = "output"
GNDPin = RPin(6)
VCCPin.function = "output"
BIN2Pin = RPin(17)
VCCPin.function = "output"
BIN1Pin = RPin(27)
VCCPin.function = "output"
AIN1Pin = RPin(23)
VCCPin.function = "output"
AIN2Pin = RPin(24)
VCCPin.function = "output"
STBYPin = RPin(25)
VCCPin.function = "output"
PWMBPin = RPin(12)
VCCPin.function = "output"
PWMAPin = RPin(13)
VCCPin.function = "output"

freq = 200
PWMAPin.frequency = freq
PWMBPin.frequency = freq

def turnOnMotors():
    STBYPin.state = 1
def turnOffMoters():
    STBYPin.state = 0
if __name__ == "__main__":
    print("running test")


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