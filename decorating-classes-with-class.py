class Logger:
    def __init__(self, cls):
        print(f'Decorating the class {cls.__name__}')
        self.cls = cls
    
    def greet(self):
        print('Hello')

    def __call__(self, *args, **kwargs):
        print(f'Creating a new instance of the {self.cls.__name__} class')
        new_instance = self.cls(*args, **kwargs)
        new_instance.greet = self.greet
        return new_instance

@Logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Shaun', 123)
print(f'The person\'s name is {p1.name}')
p1.greet()