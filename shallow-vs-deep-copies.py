from copy import copy, deepcopy

numbers_1 = [1, 2, 3]
numbers_2 = copy(numbers_1)

numbers_1[0] = 99
print(numbers_1)
print(numbers_2)

my_dict_1 = { 'a': 1, 'b': 2, 'c': 3 }
my_dict_2 = copy(my_dict_1)

my_dict_2['a'] = -42
print(my_dict_1)
print(my_dict_2)

config = {
    'dark_mode_enabled': True,
    'sound_enabled': False,
}

class Person:
    def __init__(self, first_name, last_name, favorite_foods, config):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_foods = favorite_foods
        self.config = config

    @classmethod
    def create_from_instance(cls, other_instance):
        return Person(other_instance.first_name, other_instance.last_name)

    def __str__(self):
        return f'{self.first_name} {self.last_name} likes to eat: {self.favorite_foods}'

    def __copy__(self):
        new_instance = Person(self.first_name, self.last_name, deepcopy(self.favorite_foods), self.config)
        return new_instance

p1 = Person('Shaun', 'Wassell', ['Pizza', 'Steak', 'Ice cream'], config)
p2 = copy(p1)
p2.favorite_foods.append('Broccoli')
print(p1.config)
print(p2.config)

config['sound_enabled'] = True

print(p1.config)
print(p2.config)

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = deepcopy(m1)

m1[0][0] = 99

print(m1)
print(m2)

person = {
    'name': {
        'first': 'Shaun',
        'last': 'Wassell'
    }
}
person_2 = deepcopy(person)
person['name']['first'] = 'John'
print(person)
print(person_2) 

class Component:
    def __init__(self, config, title):
        self.config = config
        self.title = title

    def get_background_color(self):
        if self.config['dark_mode_enabled']:
            return 'dark_grey'
        else:
            return 'very_light_grey'

c1 = Component(config, 'friends-list')
c2 = copy(c1)
c2.title = 'favorite-friends-list'

print(c1.get_background_color())
print(c2.get_background_color())

config['dark_mode_enabled'] = False

print(c1.get_background_color())
print(c2.get_background_color())