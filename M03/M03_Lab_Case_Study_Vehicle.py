# M03_Lab_Case_Study_Vehicle.py
# Jenn Bowers
# This program uses classes for different vehicles and attributes
import os
os.system("cls")

class Vehicle:
    '''
    Super class "Vehicle"
    '''
    def __init__(self, vehicletype, year, make, model):
        self.vehicletype = vehicletype
        self.year = year
        self.make = make
        self.model = model

    def describe(self):   # Prints the vehicle information in a legible format
        return f"Vehicle type: {self.vehicletype} \nYear: {self.year}\nMake: {self.make}\nModel: {self.model}"

class Automobile(Vehicle):
    '''
    Child class of "Vehicle"
    For the classification of automobiles
    '''
    def __init__(self, year, make, model, doors, roof):
        super().__init__(self, year, make, model)
        self.vehicletype = "Car"
        self.doors = doors
        self.roof = roof
    
    def describe(self):  # Prints the vehicle output plus additional attributes from Automobile
        return super().describe()  + f"\nNumber of doors: {self.doors}\nType of roof: {self.roof}"
    
class Broomstick(Vehicle):
    '''Child class of "Vehicle" 
    For the classification of broomsticks
    '''
    def __init__(self, year, make, model, length ):
        super().__init__(self, year, make, model)
        self.vehicletype = "Broomstick"
        self.length = length
    
    def describe(self):  # Prints the vehicle output plus additional attributes from Broomstick
        return super().describe() + f"\nLength of the broomstick: {self.length}"

class Boat(Vehicle):
    '''Child class of "Vehicle" 
    For the classification of boats
    '''
    def __init__(self, year, make, model, length, motors):
        super().__init__(self, year, make, model)
        self.vehicletype = "Boat"
        self.length = length
        self.motors = motors
    
    def describe(self):  # Prints the vehicle output plus additional attributes from Broomstick
        return super().describe() + f"\nLength of the boat: {self.length}\nNumber of motors: {self.motors}"


# Input for type of vehicle
my_vehicle = input("What type of vehicle is it: ").upper()
year = input("Enter the vehicle's year: ").capitalize()
make = input("Enter the vehicle's make: ").capitalize()
model = input("Enter the vehicle's model: ").capitalize()

if my_vehicle == "CAR" or my_vehicle == "AUTOMOBILE":   # If the vehicle is an automobile
    doors = input("Enter the number of doors, 2 or 4: ").capitalize()
    roof = input("Is it a sun roof or solid roof: ").capitalize()
    my_vehicle = Automobile(year, make, model, doors, roof)
    print()
    print(my_vehicle.describe())   
    # Calls the describe function to output the information neatly

elif my_vehicle == "BROOM" or my_vehicle == "BROOMSTICK":  # If the vehicle is a broomstick
    length = input("Enter the length of the stick: ")
    my_vehicle = Broomstick(year, make, model, length)
    print()
    print(my_vehicle.describe())
    # Calls the describe function to output the information neatly

elif my_vehicle == "BOAT" or my_vehicle == "SHIP":
    length = input("Enter the length of the boat: ")
    motors = input("How many motors: ")
    my_vehicle = Boat(year, make, model, length, motors)
    print()
    print(my_vehicle.describe())
    # Calls the describe function to output the information neatly

else:   # If the vehicle is anything besides a car, boat, or broomstick
    your_vehicle = Vehicle(my_vehicle.capitalize(), year, make, model)
    print(f"Your {my_vehicle.capitalize()} has not been added to the program yet.")
    print(f"Please review your vehicle. \n{your_vehicle.describe()}")