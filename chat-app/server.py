import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.clients = []
        self.next_id = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()

    def start_server(self):
        print('Server is now listening for connections...')

        while True:
            client_socket, addr = self.server_socket.accept()
            client_dict = { 'id': self.next_id, 'socket': client_socket } 
            self.clients.append(client_dict)
            self.next_id += 1
            print(f'Client connected from {addr}')
            thread = threading.Thread(target=self.handle_client, args=(client_dict,))
            thread.start()

    def stop_server(self):
        print('Stopping server...')

    def handle_client(self, client_dict):
        client_id = client_dict['id']
        client_socket = client_dict['socket']
        while True:
            try:
                message_raw = client_socket.recv(1024)
                if not message_raw:
                    break
                message = message_raw.decode('utf-8')
                message = f'Client {client_id}: {message}'
                self.broadcast_message(message.encode('utf-8'), client_dict)
            except Exception as e:
                print(f'Exception: {e}')
                break
        
        self.clients.remove(client_dict)
        client_socket.close()

    def broadcast_message(self, message, source_client_dict):
        for client_dict in self.clients:
            if client_dict is not source_client_dict:
                try:
                    client_dict['socket'].send(message)
                except Exception as e:
                    print(f'Exception when broadcasting: {e}')

if __name__ == '__main__':
    server = ChatServer('0.0.0.0', 8000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()