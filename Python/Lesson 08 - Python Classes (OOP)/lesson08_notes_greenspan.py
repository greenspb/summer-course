#Defines the space explorer game.

class Spacecraft():
    """The spacecraft has a fuel level and a fuel efficiency. When a player visits a planet, fuel 
    efficiency has an impact on how much fuel is consumed to travel the distance between the two planets. 
    """

    def __init__(self, name, fuel_level, fuel_efficiency):
        self._name = name
        self._fuel_level = fuel_level
        self._fuel_efficiency = fuel_efficiency
        #self.max_fuel = 200_000

    def add_fuel(self, amount):
        self._fuel_level += amount
        #self._fuel_level = min(self._fuel_level, self._fuel_level + amount)
        #self._fuel_level = max(self._fuel_level, 0)

    def calc_fuel(self, distance):
        return distance / self._fuel_efficiency

    def has_enough_fuel(self, distance):
#        return self._fuel_level >= self.calc_fuel(distance)  #Does the same as the if statement in alternative one-liner code.
        if self._fuel_level >= self.calc_fuel(distance):
# Prints state for testing purposes.
#            print(f"{self.name} has enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return True
        else:
# Prints state for testing purposes.
#            print(f"{self.name} does not have enough fuel. \t | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self.fuel_level}")
            return False

    def launch(self, distance):
        if self.has_enough_fuel(distance):
            self._fuel_level -= self.calc_fuel(distance)
            print(f"{self._name} launched successfully and completed the journey.")
        else:
            print(f"Fuel Warning for {self._name} | Fuel Needed: {self.calc_fuel(distance)} \t Fuel Level: {self._fuel_level} \t Add fuel before launch.")

# Tests the Spacecraft class.
# if __name__ == '__main__':
#     my_ship = Spacecraft("McQueen's Motorcycle", 100, 5)
#     my_ship.has_enough_fuel(1000)
#     my_ship.launch(1000)
#     my_ship.add_fuel(100)
#     my_ship.launch(1000)


#from typing import Literal  #Implements type hinting with specific string values.
#allow_resources = Literal['crystal', 'gas']  #Implements type hinting with specific string values.
#from enum import Enum       #  #Implements type hinting with dynamic values.
class Planet():
    """There are a variety of planets in this system. Some of the planets are discovered, but many are not. 
    The planets have a number of resources and can be of varying danger levels. 
    Add some descriptive text to the planet to make them feel more alive.
    """

    def __init__(self, name: str, coordinates: tuple[int, int, int], danger: int, resources: int, atmosphere: str):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self):
        return f'{self.name}, located at {self.coordinates}, is a planet with {self.danger} danger, {self.resources} resources, and {self.atmosphere} atmosphere.'

    def __sub__(self, operand: 'Planet'):
        #if type(operand) != Planet:
        if not isinstance(operand, Planet): 
            raise TypeError('Must only subtract planets')
        distance = sum([(c1-c2)**2 for c1,c2 in zip(self.coordinates, operand.coordinates)]) ** (1/2)
        return distance

# Tests the Planet class.
# if __name__ == '__main__':
#     planets = [
#         Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
#         Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
#         Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
#         Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
#         Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
#         Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
#         Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
#         Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
#         Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
#         Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
#     ]
#     print(f'The distance between {planets[0].name} and {planets[1].name} is {planets[0] - planets[1]}.')
#Test TypeError when subtracting planets.
#   planets[0] - 5

class Player():
    """The player should keep track of which planets have been visited, how many credits they have, 
    and have the ability to complete missions on the planet they're currently at. 
    The player can also purchase fuel for their spacecraft when they are on a planet.
    """

    def __init__(self, name, difficulty=3):
        if difficulty == 3:
            fuel_level = 100
            fuel_efficiency = 1
        self.spacecraft = Spacecraft(name, fuel_level, fuel_efficiency)
        self._current_planet = "Earth"
        self._visited_planets = {"Earth"}
        self._score = 0
        self._credits = 500 * (5 - difficulty)
        self._mission_rewards = []

    def planet_update(self, destination):
        self._current_planet += destination
        self._visited_planets.union(destination)
        
    def purchase_fuel(self, cost):
        self._credits -= cost
        self.spacecraft.add_fuel(cost/1)

    def complete_mission(self, planet: Planet):
        self._planet_visited.append(planet.name)
        self._credits += planet.resources
        self._mission_rewards += None  #Update mission rewards.

# planets_available = [
#     Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
#     Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
#     Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
#     Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
#     Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
#     Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
#     Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
#     Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
#     Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
#     Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
# ]

# Implements Dictionary Mapping + Data Class.
# Instead of creating separate variable names like earth = Planet(...),
# store them ina dictionary keyed by their name.
# Using dataclaseses makes defining the Planet structure clean and readable.
# Python 3.7 (via PEP 557) introduced dataclasses as a standard library.
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass(frozen=True)
class Planet:
  name: str
  coordinates: tuple[float, float, float]
  danger: int
  resources: int
  atmosphere: str

# Raw planet data: easy to add, edit, or import.
raw_planet_data = [
    ("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like"),
    ("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin"),
    ("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant"),
    ("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant"),
    ("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy"),
    ("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy"),
    ("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen"),
    ("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen"),
    ("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like"),
    ("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")
]

# Instantiate and map automatically using a dictionary comprehension.
# Type Hinting -- planets: Dict[str, Planet]
planets: Dict[str, Planet] = {
    data[0]: Planet(*data) for data in raw_planet_data
}

#name = input("Enter a name for your spacecraft:")
#difficulty = input("Select difficulty (1-5): ")
player = Player("McQueen")



#while any([])

#distance = 
#self.has_enough_fuel(distance)
#self.has_enough_fuel