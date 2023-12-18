import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

try:
    client_socket.connect((host, port))

    user_choice = input('Please enter your choice (rock/paper/scissors): ')
    user_choice_data = user_choice.encode('utf-8')

    bytes_sent = 0

    while bytes_sent < len(user_choice_data):
        additional_bytes = client_socket.send(user_choice_data[bytes_sent:])
        bytes_sent += additional_bytes
        if additional_bytes == 0:
            raise Exception('Something is wrong with the connection!')

    result = client_socket.recv(1024).decode('utf-8')
    print(f'The result of the game is: {result}')
except ConnectionRefusedError:
    print('Could not connect to the server!')

