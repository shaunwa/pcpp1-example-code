print(type(5)) # int
x = 'Hello'
print(type(x)) # str

class MyClass:
    def __init__(self, a):
        self.a = a

i = MyClass(100)

print(hasattr(i, 'a'))
print(hasattr(i, 'b'))

if hasattr(i, 'some_attribute'):
    print(i.some_attribute)

try:
    i.some_attribute
except AttributeError:
    print('The instance does not have that attribute!')

attr_name = 'age'
setattr(i, attr_name, 123)
print(getattr(i, attr_name, 'N/A'))

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + self.last_name

p = Person('Shaun', 'Wassell')

unique_attrs = []

o = object()
print(dir(p))

for attr in dir(p):
    if attr not in dir(o):
        unique_attrs.append(attr)

print(unique_attrs)

callable_attrs = []
non_callable_attrs = []

for attr in dir(p):
    if callable(getattr(p, attr)):
        callable_attrs.append(attr)
    else:
        non_callable_attrs.append(attr)

print(callable_attrs)
print(non_callable_attrs)
