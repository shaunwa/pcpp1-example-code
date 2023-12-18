import socket
import threading
import time

connection_established = False

while not connection_established:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 8000
        client_socket.connect((host, port))
        connection_established = True
    except ConnectionRefusedError:
        print('Unable to connect to the socket server. Trying again in 5 seconds...')
        time.sleep(5)

# Send message to server

def start_input_loop():
    while True:
        next_message = input('Please enter the message you want to send to the server: ')
        client_socket.sendall(next_message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f'The server responded with: {data}')
        if next_message == 'done':
            break
    client_socket.close()

input_loop = threading.Thread(target=start_input_loop)
input_loop.start()

def listen_for_messages():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f'\nNew Message!: {data}')

messages_loop = threading.Thread(target=listen_for_messages)
messages_loop.start()