
""" This is a program full of learning exercises from the below website: """
# https://pynative.com/python-object-oriented-programming-oop-exercise/

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Create a child class called Bus that will inherit all of the variables and methods
# of the Vehicle class

class Bus(Vehicle):
    pass