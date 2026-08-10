def telemetry():
    preferred_units = input("Enter telemetry data preference: (Miles above Mars, Kilometers above Mars): ").lower()
    if "miles" in preferred_units:
        miles = float(input("Enter number (miles above Mars): "))
        yards = 1760 * miles
        feet = 5280 * miles
        inches = 12 * 5280 * miles
        units = ["miles", "yards", "feet", "inches"]
        widths = [10, 10, 10, 15]              
        measurements = [miles, yards, feet, inches]
    if "kilometers" in preferred_units:
        kilometers = float(input("Enter number (kilometers above Mars): "))
        meters = 1000 * kilometers
        centimeters = 10_000 * kilometers
        millimeters = 100_000 * kilometers
        units = ["kilometers", "meters", "centimeters", "millimeters"]
        widths = [10, 15, 15, 20]              
        measurements = [kilometers, meters, centimeters, millimeters]
    for (unit, width) in zip(units, widths):
        print(unit.ljust(width), end='| ')
    print()
    for (measurement, width) in zip(measurements, widths):
        print(str(measurement).ljust(width), end='| ')
    print()
    return None

telemetry()