import json

starting_data = {
    'a': 1,
    'b': 2,
    'c': 3
}

try:
    with open('json-serialization-output.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print('Looks like this is the first time running this program!')
    data = starting_data

print('Here is the current state of the data:')
print(data)

new_value = input('Enter a new value for the key a: ')
data['a'] = new_value

with open('json-serialization-output.json', 'w') as file:
    json.dump(data, file)