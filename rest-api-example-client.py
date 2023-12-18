import requests
import json

product_name = input('Enter a name for the new product you wish to create: ')
request_data = {'name': product_name}
print(f'Here is the data we are sending: {json.dumps(request_data)}')

response = requests.post(
    'http://localhost:8000/products',
    data=json.dumps(request_data),
    headers={'Content-Type': 'application/json'},
    params={'name': 'p'})

print('Succesfully created a new product!')