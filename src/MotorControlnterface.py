import gpiozero as gpio
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

motor1 = gpio.Motor(AIN1, AIN2, PWMA, pwm = True)
standBy = gpio.LED(STBY)
def on():
    standBy.on()
def off():
    standBy.off()
if __name__ == "__main__":
    print("running test")