from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib.parse

products = [
    { 'name': 'Headphones' },
    { 'name': 'Computer' },
    { 'name': 'Pen' },
]

class RESTAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('Received a get request!')
        path_segments = urllib.parse.urlparse(self.path).path.split('/')
        if path_segments[1] == 'products':
            if len(path_segments) == 2:
                params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                name_filter = params.get('name', [''])[0]

                if len(name_filter) > 0:
                    response_data = json.dumps(
                        [p for p in products if name_filter in p['name']]
                    ).encode()
                else:
                    response_data = json.dumps(products).encode()

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(response_data))
                self.end_headers()
                self.wfile.write(response_data)
            else:
                product = next((product for product in products if product['name'] == path_segments[2]))
                response_data = json.dumps(product).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(response_data))
                self.end_headers()
                self.wfile.write(response_data) 

    def do_POST(self):
        print(f'The length of the content is: {self.headers["Content-Length"]}')
        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length)
        new_product = json.loads(request_data.decode())
        products.append(new_product)
        self.send_response(201)
        self.end_headers()
    
    def do_PUT(self):
        print('Received a put request!')
        path_segments = urllib.parse.urlparse(self.path).path.split('/')
        product = next((product for product in products if product['name'] == path_segments[2]))

        content_length = int(self.headers['Content-Length'])
        request_data = self.rfile.read(content_length)
        product_updates = json.loads(request_data.decode()) 

        for key, value in product_updates.items():
            product[key] = value

        self.send_response(200)
        self.end_headers() 
    
    def do_DELETE(self):
        global products
        path_segments = urllib.parse.urlparse(self.path).path.split('/')
        products = [product for product in products if product['name'] != path_segments[2]]

        self.send_response(200)
        self.end_headers() 

server = HTTPServer(('localhost', 8000), RESTAPIHandler)
print('Server is listening on localhost:8000')
server.serve_forever()