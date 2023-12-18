class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_details(self):
        print(f'{self.name} - {self.email} - {self.get_user_type()}')

    def get_user_type(self):
        return 'Basic User'

    def can_edit(self):
        return False

    def can_view(self):
        return True

    def can_delete(self):
        return False

    def can_delete_users(self):
        return False

    def can_reset_passwords(self):
        return False

class Editor(User):
    def get_user_type(self):
        return 'Editor'

    def can_edit(self):
        return True

class Admin(User):
    def get_user_type(self):
        return 'Admin'

    def can_edit(self):
        return True

    def can_delete(self):
        return True

    def brag_about_admin_privileges(self):
        print('I am the greatest! Behold my admin powers!')

class SuperAdmin(Admin):
    def get_user_type(self):
        return 'Super Admin'

    def can_delete_users(self):
        return True

    def can_reset_passwords(self):
        return True

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_species(self):
        return 'This animal doesn\'t have a defined species'

    def print_details(self):
        print(f'{self.name} is a {self.get_species()} and is {self.age} years old')
    
class Cat(Animal):
    def get_species(self):
        return 'Felis catus'

class Dog(Animal):
    def get_species(self):
        return 'Canis lupus familiaris'

class Elephant(Animal):
    def get_species(self):
        return 'Loxodonta africana'

basic = User('b', 'b@gmail.com')
editor = Editor('e', 'e@gmail.com')
admin = Admin('a', 'a@gmail.com')
super_admin = SuperAdmin('s', 's@gmail.com')

if basic.can_edit:
    print('Deleting a user now...')
else:
    print('This user isn\'t allowed to delete other users!')

users = [
    basic,
    editor,
    admin,
    super_admin
]

cat = Cat('Whiskerton', 4)
dog = Dog('Sherlock', 5)
elephant = Elephant('Dumbo II', 50)

users_and_animals = [*users, cat, dog, elephant]

for x in users_and_animals:
    x.print_details()