class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}'

print('Welcome to the person tracker program!')

try:
    while True:
        full_name_valid = False

        while not full_name_valid:
            try:
                full_name_raw = input('Please enter the FULL NAME: ')
                split_names = full_name_raw.split()
                if len(split_names) != 2:
                    raise ValueError('Full name must be first name, followed by a space, followed by last name')

                first_name, last_name = split_names
                full_name_valid = True
            except ValueError:
                print('Sorry! That isn\'t a valid full name, please try again:')
                full_name_valid = False

        age_valid = False

        while not age_valid:
            try:
                age_raw = input('Please enter the AGE: ')
                age = int(age_raw)
                age_valid = True
            except ValueError:
                print('Sorry! That isn\'t a valid age, please try again:')
                age_valid = False

        new_person = Person(first_name, last_name, age) 
        print('Created the person!')
        print(new_person)
finally:
    print('Thank you for using the person tracker program!')
