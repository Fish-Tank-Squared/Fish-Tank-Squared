from PositionToSpeed import RectangleBoxCircleDeadZonePosToSpeed, test
from limiter import iterative_rate_limit
import random
import time

if __name__ == "__main__":
    controler = RectangleBoxCircleDeadZonePosToSpeed()
    controler.setSettings(1, 1, 500, 500, 50, 50, 400, 400, 100)

    #pos_obj.setSettings
    current_speed = 0
    target = controler.getCurrentSpeed(250, 250)
    target = (target[0] + target[1])/2.0
    while True:
        current_speed = iterative_rate_limit(current_speed, 0.1, target)
        if target == current_speed:
            target = controler.getCurrentSpeed(random.randint(51, 449), random.randint(51, 449))
            target = (target[0] + target[1])/2.0
        print(f"Current: {current_speed},  Target: {target}")
        # send speed to motors