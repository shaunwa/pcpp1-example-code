class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @full_name.setter
    def full_name(self, value):
        first_name, last_name = value.split(' ')
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def details(self):
        return f'{self.__first_name} {self.__last_name}, {self.__age} years old'

    @details.setter
    def details(self, value):
        full_name, age_str = value.split(', ')
        self.full_name = full_name
        self.__age = age_str.split(' ')[0]

p1 = Person('Shaun', 'Wassell', 123)
p1.first_name = 'Sean'
p1.full_name = 'Shawn Wasel'
p1.details = 'Shaun Wassell, 124 years old'
print(p1.full_name)
print(p1.details)
