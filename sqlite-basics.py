import sqlite3

connection = sqlite3.connect('my-first-database.db')
cursor = connection.cursor()

create_table_statement = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
'''

cursor.execute(create_table_statement)
connection.commit()

# insert_user_statement = '''
# INSERT INTO users (name, email) VALUES ('Simona Millham', 'simona@gmail.com'), ('Shaun Wassell', 'shaun@gmail.com'), ('Bob Salmans', 'bob@gmail.com')
# '''
# cursor.execute(insert_user_statement)
# connection.commit()

select_users_statement = '''
SELECT * FROM users
'''
cursor.execute(select_users_statement)

for user in cursor:
    print(user)

# id_to_delete = input('Please enter the id of the user you would like to delete: ')
# delete_user_statement = f'''
# DELETE FROM users WHERE id = ?
# '''
# cursor.execute(delete_user_statement, (id_to_delete,))
# connection.commit()

id_to_update = input('Which user would you like to update? (Enter the id): ')
new_email = input('Please enter a new email for the user: ')
new_name = input('Please enter a new name for the user: ')

update_statement = '''
UPDATE users SET email = ?, name = ? WHERE id = ?
'''
cursor.execute(update_statement, (new_email, new_name, id_to_update))
connection.commit()

# print('Here are the updated users after the delete operation:')
# cursor.execute(select_users_statement)

# for user in cursor:
#     print(user)

connection.close()