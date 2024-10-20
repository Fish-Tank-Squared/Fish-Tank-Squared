
def iterative_rate_limit(current_voltage, limit, target):
    new_voltage = current_voltage + limit if current_voltage + limit < target else target
    return new_voltage

if __name__ == "__main__":
    starting_voltage = 0
    
    print("This works!")