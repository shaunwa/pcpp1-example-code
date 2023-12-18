import functools
import math

def math_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

@functools.total_ordering
class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __float__(self):
        return self.top / self.bottom

    def __str__(self):
        return f'{self.top}/{self.bottom}'

    def __bool__(self):
        return self.top != 0

    def __int__(self):
        if self.top % self.bottom == 0:
            return int(self.top / self.bottom)
        else:
            raise Exception(f'The fraction {self} does not have an integer representation')
        
    def __repr__(self):
        return f'Fraction({self.top}, {self.bottom})'

    def __format__(self, format_spec):
        if format_spec == 'regular':
            return self.__str__()
        elif format_spec == 'long':
            return f'{self.top} over {self.bottom}'
        elif format_spec == 'reduced':
            gcd = math.gcd(self.top, self.bottom)
            return f'{int(self.top / gcd)}/{int(self.bottom / gcd)}'
        else:
            return self.__str__()

    def __add__(self, other):
        lcm = math_lcm(self.bottom, other.bottom)
        left_multiplier = lcm / self.bottom
        right_multiplier = lcm / other.bottom

        return Fraction(
            int(self.top * left_multiplier + other.top * right_multiplier),
            lcm
        )

    def __sub__(self, other):
        lcm = math_lcm(self.bottom, other.bottom)
        left_multiplier = lcm / self.bottom
        right_multiplier = lcm / other.bottom

        return Fraction(
            int(self.top * left_multiplier - other.top * right_multiplier),
            lcm
        )

    def __mul__(self, other):
        new_top = self.top * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def __truediv__(self, other):
        new_top = self.top * other.bottom
        new_bottom = self.bottom * other.top
        return Fraction(new_top, new_bottom)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self_value = self.top / self.bottom
            other_value = other.top / other.bottom
            return self_value == other_value
        elif isinstance(other, int) or isinstance(other, float):
            self_value = self.top / self.bottom
            return self_value == other
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Fraction):
            self_value = self.top / self.bottom
            other_value = other.top / other.bottom
            return self_value > other_value
        elif isinstance(other, int) or isinstance(other, float):
            self_value = self.top / self.bottom
            return self_value > other
        else:
            return NotImplemented
    
f1 = Fraction(15, 20)
f2 = Fraction(24, 12)
f3 = Fraction(3, 4)
f4 = Fraction(12, 16)

print(f'f2 as a float: {float(f2)}')
print(f'f2 as a bool: {bool(f2)}')
print(f'f2 as a str: {f2}')
print(f'f2 as an int: {int(f2)}')

print(f'repr(f1) is {f1!r}')
print(f'format(f1, "regular") is {format(f1, "regular")}')
print(f'format(f1, "long") is {format(f1, "long")}')
print(f'format(f1, "reduced") is {format(f1, "reduced")}')