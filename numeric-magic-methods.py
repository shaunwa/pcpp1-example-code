class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            x_prod = self.x * other.x
            y_prod = self.y * other.y
            return x_prod + y_prod
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

v1 = Vector(1, 2)
v2 = Vector(3, 4)

vsum = v1 + v2
vdiff = v1 - v2

print(f'x: {vdiff.x}, y: {vdiff.y}')