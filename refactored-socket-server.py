import socket
import threading

class MultiClientServer:
    def __init__(self, host=socket.gethostname(), port=8000):
        self.clients = []
        self.clients_lock = threading.Lock()
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(3)
        self.message_handlers = []
        print(f'Waiting for connections on {self.host}, port {self.port}')

    def add_handler(self, message_handler):
        self.message_handlers.append(message_handler)

    def client_thread(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(f'Received data: {data}')

            if not data:
                break

            with self.clients_lock:
                for handle_message in self.message_handlers:
                    handle_message(client_socket, self.clients, data)

    def start_server(self):
        while True:
            client_socket, _ = self.server_socket.accept()

            with self.clients_lock:
                self.clients.append(client_socket)

            new_thread = threading.Thread(target=self.client_thread, args=(client_socket,))
            new_thread.start()

    def stop_server(self):
        self.server_socket.close()
        for client in self.clients:
            client.close()

def custom_message_handler(client_socket, all_sockets, data):
    print('Inside custom_message_handler')

    other_sockets = [client for client in all_sockets if client is not client_socket]

    for other_socket in other_sockets:
        other_socket.sendall(data.encode('utf-8'))

    if data == 'done':
        client_socket.close()
        all_sockets.remove(client_socket)

if __name__ == "__main__":
    server = MultiClientServer()
    server.add_handler(custom_message_handler)

    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()