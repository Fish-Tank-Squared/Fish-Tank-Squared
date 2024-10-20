from PositionToSpeed import RectangleBoxCircleDeadZonePosToSpeed
from limiter import iterative_rate_limit

if __name__ == "__main__":
    pos_obj = RectangleBoxCircleDeadZonePosToSpeed()
    #pos_obj.setSettings
    current_speed = 0
    target = 1
    while current_speed != target:
        target = pos_obj.getCurrentSpeed(0,23)
        current_speed = iterative_rate_limit(current_speed, 0.05, target)
        # send speed to motors