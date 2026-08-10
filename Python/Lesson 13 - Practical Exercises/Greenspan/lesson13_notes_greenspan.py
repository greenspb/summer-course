curl http://20.127.202.175:8000 | Format-Table -Wrap -AutoSize # PS
curl http://20.127.202.175:8000 | less #unix
curl 20.127.202.175:8000

curl -H "X-Username: chief.engineer" -H "X-Password: ares-vallis-7" http://20.127.202.175:8000 

import requests
headers = {'X-Username': "chief.engineer", 'X-Password': "ares-vallis-7"}
response = requests.get("http://20.127.202.175:8000", headers=headers)
print(response.reason, response.status_code)
print(response.text)

ssh chief.tech@20.127.202.175
#1000-souls-aboard

#   [1] Telemetry systems      -> Python Problem 1
#   [2] Food resource recalc   -> Python Problem 2
#   [3] Emergency comms rocket -> Python Problem 3
#   [4] Submit solutions       -> pull request
#   [5] Broadcast beacon       -> host a site from your VM

#mkdir filename{1..100} #This command makes 100 directories.

ls
#cd mission
#cat the_answers.txt
#cd Folder1 
grep -r "telemetry" # Find the location of file mentioning telemetry.
grep -R "telemetry"


#either
#cat mission/Folder1/Folder22/Folder26/telemetry_python_problem1.txt
# or
grep -rl "telemetry" | xargs cat

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

#problem 2
grep -r "resource" 
grep -R "resource"
#grep -rl "resource" | xargs cat
cat mission/Folder1/Folder37/Folder86/resource_pythonProblem2.txt

#calculate area of pizza per units of dough
class Automatron():
    def __init__(self, name, area, units):
        self.name = name
        self.area = area
        self.units = units
        self.efficiency = area/units
    def __str__(self):
        return f"{{'name': '{self.name}', 'area': {self.area}, 'units': {self.units}, 'efficiency': {self.efficiency}}}"

def area_cirlce(diameter):
    return 3.14*(diameter/2)**2

def area_triangle(base, height):
    return base * height / 2

def area_square(length):
    return length**2

first = Automatron("first", 2 * area_cirlce(15), 20)
second = Automatron("second", area_triangle(20, 20), 20)
third = Automatron("third", area_square(18), 18)
my_list = [first, second, third]

def compare_automatrons(list_):
    max_eff = 0
    most_eff = None
    for automatron in list_:
        print(automatron)
        if automatron.efficiency > max_eff:
            most_eff = automatron
    print(f"The most efficient automatron is {most_eff}")

compare_automatrons(my_list)

#Problem 3
cd / #Root folder
cd Problem3
cat problem3_statement.txt 

def calculate_fuel(mass):
    return (10 * (mass/3) // 10) - 2

assert calculate_fuel(1969) == 654
assert calculate_fuel(100756) == 33583

#cat input.txt

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