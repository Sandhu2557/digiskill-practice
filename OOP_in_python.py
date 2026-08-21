# OOP (object orentiend programming) in python

# Encapsulation means
# In programming, related data is encapsulated into a single object.
# object is combination of related variables and functions
# in object store data (attributes) : performs action(method functions)

# Data Abstraction means
# its mean we do not show all our data and functions to the outside world.

# class is blueprint for creating object.
# class defines attributs and method function.

class Car:
    def __init__(self,color):
        self.color=color

    def start(self):
        print(f"{self.color} car started")

# first object 

my_car=Car("red")
my_car.start()
#second object
second_car=Car("red")
second_car.start()