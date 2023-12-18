class Person:
    def __init__(self, name, age, hair_color, eye_color):
        print("Creating a new instance of the Person class!")
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
    
    def greet(self, other_name):
        print(f'Hello {other_name}, my name is {self.name}!')
    
class Developer(Person):
    pass

class PythonDeveloper(Developer):
    pass

print(f'Developer is subclass of Person: {issubclass(PythonDeveloper, Person)}')

person_1 = Developer("Shaun", 123, "brown", "brown")
person_2 = Person("Lalo", 102, "brown", "brown")

# person_1.greet('Lalo')
# person_2.greet('Shaun')

def print_person_details(person):
    if isinstance(person, Person):
        print(f'name: {person.name}, age: {person.age}')
    else:
        print('Oh no! It looks like you\'re trying to print details for a non-person variable')
    
print_person_details(person_1)
x = 10
print_person_details(x)

# print(f"{person_1.name} is {person_1.age} years old")
# print(f"{person_2.name} is {person_2.age} years old")

# person_2.name = "Lala"

# print(f"{person_2.name} is {person_2.age} years old")