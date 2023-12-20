import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def create_table():
    connection = sqlite3.connect('expenses.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      date TEXT,
                      category TEXT,
                      amount REAL)
    ''')
    connection.commit()
    connection.close()

class ExpensesRequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, body):
            response_data = json.dumps(body).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', len(response_data))
            self.end_headers()
            self.wfile.write(response_data)

    def do_GET(self):
        if self.path == '/expenses':
            connection = sqlite3.connect('expenses.db')
            cursor = connection.cursor() 
            cursor.execute('SELECT * FROM expenses')
            expenses = cursor.fetchall()
            self._send_response(200, expenses)

    def do_POST(self):
        if self.path == '/expenses':
            content_length = int(self.headers['Content-Length'])
            request_body = json.loads(self.rfile.read(content_length))

            connection = sqlite3.connect('expenses.db')
            cursor = connection.cursor()

            cursor.execute('INSERT INTO expenses (name, date, category, amount) VALUES (?, ?, ?, ?)',
                           (request_body['name'], request_body['date'], request_body['category'], request_body['amount']))
            connection.commit()

            request_body['id'] = cursor.lastrowid
            self._send_response(201, request_body)

    def do_DELETE(self):
        if self.path.startswith('/expenses/'):
            id_to_delete = int(self.path.split('/')[-1])

            connection = sqlite3.connect('expenses.db')
            cursor = connection.cursor()
            cursor.execute('DELETE FROM expenses WHERE id = ?', (id_to_delete,))
            connection.commit()
            connection.close()

            self._send_response(204, {})

if __name__ == '__main__':
    create_table()
    server = HTTPServer(('localhost', 8000), ExpensesRequestHandler)
    print('Starting expenses REST API...')
    server.serve_forever()