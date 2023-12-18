class Person:
    def __init__(self, name, age, hair_color):
        object.__setattr__(self, 'name', name)
        object.__setattr__(self, 'age', age)
        object.__setattr__(self, 'hair_color', hair_color)
    
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if callable(attr):
            return attr

        raise Exception('Do NOT try accessing an attribute on the Person class!')

    def __setattr__(self, name, value):
        raise Exception('All attributes in the Person class are private!')

    def __delattr__(self, name):
        raise Exception('All attributes in the Person class are private, you cannot delete them!')

    def __get_name(self):
        return self.__name
    
    def print_name(self):
        print(f'My name is {object.__getattribute__(self, "name")}')

class Developer(Person):
    def print_name(self):
        print(f'My name is {self.__get_name()}')

p1 = Person('Shaun', 123, 'brown')
del p1.name
