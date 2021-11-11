# This will have -> method chaining:
# Calling multiple methods sequentially each call performs an action on the same obj and returns self

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
