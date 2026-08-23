# classes and objects in python
# object is combination of related variables and functions
# in object store data (attributes) : performs action(method functions)

class car:
    def drive(self):
        print("your car is moving")
# create object
car1=car()
car1.drive()

class Car:
    color="red"
    def drive(self):
        print(f"{self.color} car is moving")

car2=Car()
car2.drive()

class kar:
    color="red"
    def drive(self):
        print(f"{self.color} car is moving")
    def setcolor(self,new_color):
        self.color=new_color

car3=kar()
car3.drive()
car3.setcolor("White")
car3.drive()