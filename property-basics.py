from math import sqrt

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def area(self):
        print('Someone is trying to access the area of this rectangle!')
        return self.height * self.width

    @area.setter
    def area(self, value):
        new_height = value / self.__width
        self.__height = new_height

    @property
    def perimeter(self):
        return self.__height * 2 + self.__width * 2

    @perimeter.setter
    def perimeter(self, value):
        new_height_doubled = value - self.__width * 2
        self.__height = new_height_doubled / 2

    @property
    def aspect_ratio(self):
        return self.__width / self.__height

    @aspect_ratio.setter
    def aspect_ratio(self, value):
        new_height = self.__width / value
        self.__height = new_height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self.__height = value
        else:
            self.__height = float(value)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, (int, float)):
            self.__width = value
        else:
            self.__width = float(value)
    
    # @area.setter
    # def area(self, value):
    #     self.height = sqrt(value)
    #     self.width = sqrt(value)

    # @area.deleter
    # def area(self):
    #     self.height = 0
    #     self.width = 0

r = Rectangle(10, 4)
r.aspect_ratio = 16/9
print(f'The rectangle is {r.width} x {r.height}')
print(f'The perimeter of the rectangle is {r.perimeter}')
print(f'The aspect ratio of the rectangle is {r.aspect_ratio}')