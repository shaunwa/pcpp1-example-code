import pickle

def my_function():
    return 5

print(my_function.__name__)

class MyClass:
    @classmethod
    def my_class_method(cls):
        my_instance = cls()

    def say_hello(self):
        print('Hello!')

class MyOtherClass:
    pass

i = MyClass()

print(i.say_hello.__name__)

print(pickle.__name__)

if __name__ == '__main__':
    print('I am the special-attrs file! Thank you for running me')

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + self.last_name
    
    def with_different_first_name(self, new_first_name):
        new_instance = self.__class__(new_first_name, self.last_name)
        return new_instance

p = Person('Shaun', 'Wassell')
p_modified = p.with_different_first_name('John')

print(p is p_modified)

print(Person.__bases__)

print(Person.__dict__)
print(p.__dict__)