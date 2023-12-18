# print('Hello' + ' Shaun')

def repeat_string(s, number_of_times):
    if type(s) != str:
        raise TypeError('First arg must be a string!')
    if type(number_of_times) != int:
        raise TypeError('Second arg must be an int!')
    return s * number_of_times

# print(repeat_string('Hello', 10.0))

class TxtFilename(str):
    def __new__(cls, value):
        if not value.endswith('.txt'):
            raise ValueError('The string that was passed in is not a txt file name!')
        return super().__new__(cls, value)

# filename = TxtFilename('my-file')
# print(filename)

class Person:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, key):
        if key != 'name':
            raise KeyError('Person has no value for that key')
        return self.name

p = Person('Shaun')
print(p['name'])
print(p['favorite_color'])
