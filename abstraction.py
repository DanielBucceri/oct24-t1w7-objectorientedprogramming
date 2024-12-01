# shape base class with an area() method
# subclass such as square, circle, triangle etc
import math
from abc import ABC, abstractmethod #Abstract base Class = "ABC"

class Shape(ABC):
    @abstractmethod # @ declerator ?
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius): # init must be used to set up attributes to then be used later
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

c1 = Circle(7)
print(c1.area())
r1 = Rectangle(5, 10)
print(r1.area())

