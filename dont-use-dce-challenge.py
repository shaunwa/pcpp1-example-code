# x = int(input('Please enter the first number: '))
# y = int(input('Please enter the second number: '))

# exec(f'print(x + y)')

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def drop_database():
    print('Dropping database...')

# attr = input('Please enter the name of the attribute you want to access: ')

# p = Person('Shaun', 'Wassell', 123)

# print(getattr(p, attr))

print('Please complete the code so that the function returns the sum of its arguments:')
code_snippet = """
def my_function(a, b):
"""
print(code_snippet)

user_input = input('')
exec(f"""{code_snippet}
    {user_input}
""")

result = my_function(10, 22)
if result == 32:
    print('Correct!')
else:
    print('Wrong!')