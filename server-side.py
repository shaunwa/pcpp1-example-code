import http.server
import socketserver

class SimpleRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print('Received a request!')

        response_data = 'Hello'.encode()

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(response_data))
        self.end_headers()
        self.wfile.write(response_data)

server = socketserver.TCPServer(('', 8000), SimpleRequestHandler)
print('The server is now listening...')
server.serve_forever()