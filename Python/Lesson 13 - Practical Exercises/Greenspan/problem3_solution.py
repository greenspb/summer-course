def calculate_fuel(mass):
    return (10 * (mass/3) // 10) - 2

assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

#cat input.txt

def calculate_total_fuel():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        total_fuel = 0
        for line in lines:
            try:
                mass = int(line.strip())
                total_fuel += calculate_fuel(mass)
            except:
                continue
    print(f"The total amount of fuel needed is {total_fuel}")
    return total_fuel

calculate_total_fuel()