import json

def get_first_time_data():
    name = input('Name: ')
    age = int(input('Age: '))
    favorite_food = input('Favorite food: ')

    person = { 'name': name, 'age': age, 'favorite_food': favorite_food }

    with open('json-user-data.json', 'w') as file:
        json.dump(person, file)
    
def get_updates(existing_data):
    new_name = input(f'Name ({existing_data["name"]}): ')
    new_age = int(input(f'Age ({existing_data["age"]}): '))
    new_favorite_food = input(f'Favorite food ({existing_data["favorite_food"]}): ')

    updated_person = {**existing_data}

    if new_name:
        updated_person['name'] = new_name
    if new_age:
        updated_person['age'] = new_age
    if new_favorite_food:
        updated_person['favorite_food'] = new_favorite_food

    with open('json-user-data.json', 'w') as file:
        json.dump(updated_person, file)

try:
    with open('json-user-data.json', 'r') as file:
        existing_data = json.load(file)
        get_updates(existing_data)
except FileNotFoundError:
    get_first_time_data()