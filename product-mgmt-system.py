import sqlite3

conn = sqlite3.connect('product-mgmt-system.db')
cursor = conn.cursor()

create_products_table_statement = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    price INTEGER NOT NULL
)
'''
cursor.execute(create_products_table_statement)
conn.commit()

def add_product():
    name = input('Please enter the name for the new product: ')
    price = int(input('Please enter the price for the new product (in cents): '))
    cursor.execute('''
    INSERT INTO products (name, price) VALUES (?, ?);
    ''', (name, price))
    print('Product created successfully!')

def edit_product():
    id_to_update = input('Please enter the id of the product you would like to edit: ')
    new_name = input('Please enter a new name: ')
    new_price = input('Please enter a new price: ')

    if new_name:
        if new_price:
            cursor.execute(
                'UPDATE products SET name = ?, price = ? WHERE id = ?',
                (new_name, int(new_price), id_to_update))
        else:
            cursor.execute(
                'UPDATE products SET name = ? WHERE id = ?',
                (new_name, id_to_update))
    else:
        if new_price:
            cursor.execute(
                'UPDATE products SET price = ? WHERE id = ?',
                (int(new_price), id_to_update))

def delete_product():
    id_to_delete = input('Please enter the id of the product you would like to delete: ')
    cursor.execute('DELETE FROM products WHERE id = ?', (id_to_delete,))

def list_products():
    cursor.execute('SELECT * FROM products')
    for product in cursor:
        print(product)

while True:
    command = input('What would you like to do? (add/edit/del/list/exit): ')

    if command == 'add':
        add_product()
    elif command == 'edit':
        edit_product()
    elif command == 'del':
        delete_product()
    elif command == 'list':
        list_products()
    elif command == 'exit':
        break
    else:
        print('That is not a valid command!')
    
    conn.commit()