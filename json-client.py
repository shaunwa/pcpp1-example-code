import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

person = { 'name': 'Shaun', 'age': 123, 'hair_color': 'brown' }

try:
    client_socket.connect((host, port))
    person_data = pickle.dumps(person)

    bytes_sent = 0

    while bytes_sent < len(person_data):
        additional_bytes = client_socket.send(person_data[bytes_sent:])
        print(f'Transferred {additional_bytes} bytes')
        bytes_sent += additional_bytes
        if additional_bytes == 0:
            raise Exception('Something is wrong with the connection!')

    response = client_socket.recv(1024).decode('utf-8')
    print(f'The server says: {response}')
except ConnectionRefusedError:
    print('Could not connect to the server!')

