def track_attributes(cls):
    class Wrapper(cls):
        def __setattr__(self, attr_name, new_value):
            print(f'Instance of {cls.__name__} is changing the {attr_name} attribute to {new_value}')
            object.__setattr__(self, attr_name, new_value)
    
    return Wrapper

@track_attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Shaun', 123)

p1.name = 'Sean'
p1.age = 0