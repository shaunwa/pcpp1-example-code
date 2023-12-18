# Positional Arguments
def add(a, b):
    return a + b

print(add(100, 200))

# Keyword Arguments

def create_person(name, age, hair_color, height, weight):
    pass

create_person(
    name='Bob',
    age=35,
    hair_color='Brown',
    height='6ft',
    weight='180'
)

# Arbitrary Positional

def create_grocery_list(*items):
    grocery_list = 'Groceries:\n'
    for item in items:
        grocery_list += f'{item}\n'
    
    return grocery_list

print(create_grocery_list('apples', 'bananas', 'canteloupe'))

# Arbitrary Keyword

def update_person_details(person, **updates):
    for key in updates:
        person[key] = updates[key]
    
person = { 'name': 'Bob', 'age': 35 }
update_person_details(person, name='Robert', favorite_food='Pizza')

print(person)

# Positional Only

def cross_product(a, b, /):
    pass

m1 = []
m2 = []

cross_product(m1, m2)
# cross_product(b=m1, a=m2)

# Keyword-Only

def create_person(*, name, age, hair_color, height, weight):
    pass

create_person(
    name='Bob',
    age=35,
    hair_color='Brown',
    height='6ft',
    weight='180'
)

# Combining  Positional-Only and Keyword-Only Args

def my_func(a, b, c, /, d, e, f, *, g, h, i):
    pass