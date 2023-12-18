import sqlite3

connection = sqlite3.connect('ecommerce-site.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
)
''')

cursor.execute('''
INSERT INTO products (name, description, price) VALUES ('Shoes', 'Available in all sizes', 5099)
''')

connection.commit()

cursor.execute('''
SELECT * FROM products
''')

for product in cursor:
    print(product)

connection.close()