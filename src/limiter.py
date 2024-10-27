from math import fabs


def iterative_rate_limit(current_voltage, limit, target):
    if target <= 0:
        new_voltage = current_voltage - limit
    else:
        new_voltage = current_voltage + limit
    return min(new_voltage, target) if target > 0 else max(new_voltage, target)

if __name__ == "__main__":
    voltage = 0
    target = 12
    while voltage != target:
        voltage = iterative_rate_limit(voltage, 0.5, target)
        print(voltage)