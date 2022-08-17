class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    # metodo es lo mismo a una function
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(10, 20)

print(r1.area())
print(r1.height)
print(r1.perimeter())
