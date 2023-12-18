import json

person = { 'name': 'Shaun', 'age': 123, 'hair': 'brown' }
numbers = [1, 2, 3, 4, 5]

json_string = '{"a": 1, "b": 2, "c": 3}'

print(json.dumps(person))
print(json.dumps(numbers))

dictionary = json.loads(json_string)
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['c'])

with open('json-basics.json', 'r') as file:
    python_data = json.load(file)

with open('json-basics.json', 'w') as file:
    json.dump(person, file)

print(python_data)