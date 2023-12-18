import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

server_socket.bind((host, port))
server_socket.listen(3)

print('Server is waiting for connections...')

client_socket, client_address = server_socket.accept()
print(f'A new client has connected!')

data = client_socket.recv(1024)
person = pickle.loads(data)

client_socket.sendall(f'Hello, {person["name"]}'.encode('utf-8'))

# Do something with the data

client_socket.close()