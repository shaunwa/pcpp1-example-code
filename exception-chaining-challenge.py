class InvalidPersonDataException(Exception):
    pass

class Person:
    def __init__(self, first_name, last_name, age):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.age = int(age)
        except ValueError as e:
            raise InvalidPersonDataException('The age must be convertible into an integer') from e

    @classmethod
    def create_from_string(cls, string): # Shaun Wassell 123
        try:
            first_name, last_name, age_raw = string.split()
            new_person = Person(first_name, last_name, age_raw)
            return new_person
        except InvalidPersonDataException as e:
            raise ValueError('The third data point must be convertible into an integer')

user_data_raw = input('Enter in the data for a new person, separated by spaces: ')
person = Person.create_from_string(user_data_raw)
print(f'The person is named: {person.first_name}')