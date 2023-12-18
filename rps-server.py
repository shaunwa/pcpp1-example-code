import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

server_socket.bind((host, port))
server_socket.listen(3)

print('Server is waiting for connections...')

client_1_socket, client_1_address = server_socket.accept()
print('Client 1 has connected!')

client_2_socket, client_2_address = server_socket.accept()
print('Client 2 has connected!')

c1_choice = client_1_socket.recv(1024).decode('utf-8')
c2_choice = client_2_socket.recv(1024).decode('utf-8')

if c1_choice == c2_choice:
    result = 'tie'
elif c1_choice == 'rock':
    if c2_choice == 'paper':
        result = 'c2 wins!'
    elif c2_choice == 'scissors':
        result = 'c1 wins!'
elif c1_choice == 'paper':
    if c2_choice == 'rock':
        result = 'c1 wins!'
    elif c2_choice == 'scissors':
        result = 'c2 wins!'
elif c1_choice == 'scissors':
    if c2_choice == 'paper':
        result = 'c1 wins!'
    elif c2_choice == 'rock':
        result = 'c2 wins!'

client_1_socket.sendall(result.encode('utf-8'))
client_2_socket.sendall(result.encode('utf-8'))

client_1_socket.close()
client_2_socket.close()