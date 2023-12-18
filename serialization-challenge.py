import json

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    @classmethod
    def from_dict(cls, dictionary):
        person = Person(dictionary['first_name'], dictionary['last_name'])
        return person

my_dictionary = {'a': 1, 'b': 2}
p = Person('Shaun', 'Wassell')
# print(json.dumps(p))

with open('serialization-challenge-output.json', 'w') as file:
    json.dump(p.to_dict(), file)

with open('serialization-challenge-output.json', 'r') as file:
    p_copy = Person.from_dict(json.load(file))
    print(p_copy)