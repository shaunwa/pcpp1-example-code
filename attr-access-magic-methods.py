import math

o_set = object.__setattr__
o_get = object.__getattribute__

in_conversions = {
    'in': 1,
    'cm': 2.45,
    'm': 0.0245,
    'mi': 0.000015782,
    'ft': 0.08333,
}

class Person:
    def __init__(self, first_name, last_name, age, height):
        o_set(self, 'first_name', first_name)
        o_set(self, 'last_name', last_name)
        o_set(self, 'age', age)
        o_set(self, 'height', height)

    def __getattribute__(self, name):
        if name == 'full_name':
            return object.__getattribute__(self, 'first_name') + ' ' + object.__getattribute__(self, 'last_name')
        elif name.startswith('age_'):
            units = name.split('_')[1]
            age = object.__getattribute__(self, 'age')
            if units == 'days':
                return age * 365
            elif units == 'hours':
                return age * 365 * 24
            elif units == 'seconds':
                return age * 365 * 24 * 3600
            elif units == 'months':
                return age * 12
            elif units == 'years':
                return age
        elif name.startswith('height_'):
            units = name.split('_')[1]
            height = object.__getattribute__(self, 'height')

            if units in in_conversions:
                return height * in_conversions[units]
            else:
                raise Exception(f'The unit {units} is not supported for this attribute')

        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'full_name':
            first_name, last_name = value.split()
            object.__setattr__(self, 'first_name', first_name)
            object.__setattr__(self, 'last_name', last_name)


        elif name == 'age':
            raise Exception('Age is a read-only value!')
        # elif name.startswith('age_'):
        #     units = name.split('_')[1]

        #     if units == 'days':
        #         new_age = value / 365
        #     if units == 'hours':
        #         new_age = value / 365 / 24
        #     if units == 'seconds':
        #         new_age = value / 365 / 24 / 3600
        #     if units == 'months':
        #         new_age = value / 12
        #     if units == 'years':
        #         new_age = value

        #     o_set(self, 'age', math.floor(new_age))

        elif name.startswith('height_'):
            units = name.split('_')[1]
            height = o_get(self, 'height')

            if units == 'in':
                new_height = value
            elif units == 'cm':
                new_height = value / 2.54
            elif units == 'm':
                new_height = value / 0.0254
            elif units == 'mi':
                new_height = value / 0.000015782
            
            o_set(self, 'height', new_height)

        o_set(self, name, value)

    def __delattr__(self, name):
        object.__delattr__(self, name)

        if name == 'age':
            raise Exception('Age is a read-only value!')
        
    def birthday(self):
        o_set(self, 'age', o_get(self, 'age') + 1)

p1 = Person('Shaun', 'Wassell', 123, 72)

p1.full_name = 'John Smith'

print(p1.first_name)
print(p1.last_name)