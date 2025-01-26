import math

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

rect = Rectangle(5, 3)
circle = Circle(4)
print("Rectangle Area:", rect.calculate_area())
print("Circle Area:", round(circle.calculate_area(), 2))
