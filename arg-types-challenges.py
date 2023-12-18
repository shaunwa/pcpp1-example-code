# 1. Average function

def get_average(*args):
    if len(args) == 0:
        return 0
    total = sum(args)
    return total / len(args)

print(get_average(1, 2, 3))
print(get_average(100))
print(get_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(get_average()) # 0

# 2. Area of Rectangle

def calculate_rect_area(*, length, width):
    return length * width

print(calculate_rect_area(length=10, width=5))
# print(calculate_rect_area(10, 5)) # Should give an error!

# 3. Powers of Numbers

def power(x, y, /):
    return x ** y

print(power(4, 2))
print(power(2, 8))
# power(x=4, y=2) # Should give an error!

# 4. Create a Dictionary

def create_dict(**entries):
    return entries

print(create_dict(
    a=1,
    b='Hello!',
    c=True,
))

# 5. Distance between points

import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(get_distance(1, 1, 5, 5))
print(get_distance(x1=1, y1=1, x2=5, y2=5))

# 6. Greeting - no If statements allowed!

def greet(name, greeting_phrase='Hello'):
    return f'{greeting_phrase}, {name}!'

print(greet('Shaun')) # Hello, Shaun!
print(greet('Shaun', 'Howdy')) # Howdy, Shaun!