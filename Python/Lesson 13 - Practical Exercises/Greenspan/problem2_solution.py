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