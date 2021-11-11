# This will have -> method chaining:
# Calling multiple methods sequentially each call performs an action on the same obj and returns self
from abc import ABC, abstractmethod


class Vehicle(ABC):
    # Prevents a user from creating an object of that class
    # + compels a user to override abstract methods in a child class
    # abstract class = a class which contains one or more abstract methods.
    # abstract method = a method that has a declaration but does not have an implementation.

    @abstractmethod
    def go(self):
        pass


# using an abstract class is a good way to see if you're missing implementations
# you did not inherit shit here btw, try it out if you want to see the error using Car(Vehicle)
class Car:
    # a class variable is created inside of a class but not inside a constructor
    wheels = 4

    # the init method
    def __init__(self, make, model, year, color):
        self.make = make  # instance variables are inside of a constructor,
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        """
        self refers to the object that's refering this method
        :return:
        """
        print("This car is driving")
        return self

    def stop(self):
        print("This car has stoped")
        return self

    def __str__(self):
        txt = f"The maker is {self.make}, the model is {self.model}, from the year {self.year} and color {self.color}"
        return txt


car = Car("don't know", "who cares", 1994, "Red")
car.drive()\
    .stop()
