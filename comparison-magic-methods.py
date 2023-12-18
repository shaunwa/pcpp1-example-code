import functools

@functools.total_ordering
class Person:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __gt__(self, other):
        return self.age > other.age

    def greet(self, other_name):
        print(f'Hello {other_name}, my name is {self.name}!')

p1 = Person('Shaun', 40, 'brown', 'brown')
p2 = Person('Shaun', 40, 'brown', 'brown')

print(p1 != p2)
print(p1 <= p2)
print(p1 == p2)
print(p1 > p2)