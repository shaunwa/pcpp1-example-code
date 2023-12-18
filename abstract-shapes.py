from abc import ABC, abstractmethod
from math import sqrt

class Shape(ABC):
    @abstractmethod
    def get_number_of_sides(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, short_side_length, long_side_length):
        self.short_side_length = short_side_length
        self.long_side_length = long_side_length

    def get_number_of_sides(self):
        return 4

    def get_perimeter(self):
        return 2 * self.short_side_length + 2 * self.long_side_length

    def get_area(self):
        return self.short_side_length * self.long_side_length

r1 = Rectangle(10, 23)
print(r1.get_number_of_sides())
print(r1.get_perimeter())
print(r1.get_area())

class Trapezoid(Shape):
    def __init__(self, short_side_length, long_side_length, height):
        self.short_side_length = short_side_length
        self.long_side_length = long_side_length
        self.height = height

    def get_number_of_sides(self):
        return 4

    def get_area(self):
        return (self.short_side_length + self.long_side_length) / 2 * self.height

    def get_perimeter(self):
        bottom_side_length = (self.long_side_length - self.short_side_length) / 2
        diagonal_side_length = sqrt(bottom_side_length * bottom_side_length + self.height * self.height)
        return diagonal_side_length * 2 + self.long_side_length + self.short_side_length

t1 = Trapezoid(5, 10, 5)
print(t1.get_number_of_sides())
print(t1.get_perimeter())
print(t1.get_area())

class RightTriangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_number_of_sides(self):
        return 3

    def get_area(self):
        return self.height * self.width / 2

    def get_perimeter(self):
        return sqrt(self.height * self.height + self.width * self.width) + self.height + self.width
    
tri1 = RightTriangle(3, 4)
print(tri1.get_number_of_sides())
print(tri1.get_perimeter())
print(tri1.get_area())