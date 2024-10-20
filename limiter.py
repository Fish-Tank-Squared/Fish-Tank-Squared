
def iterative_rate_limit(current_voltage, limit, target):
    new_voltage = current_voltage + limit if current_voltage + limit < target else target
    return new_voltage

if __name__ == "__main__":
    voltage = 0
    target = 12
    while voltage != target:
        voltage = iterative_rate_limit(voltage, 0.5, target)
        print(voltage)