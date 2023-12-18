import random

def get_int_from_user():
    try:
        user_input_raw = input('Give me an integer: ')
        user_input = int(user_input_raw)
        print('About to return the user input...')
        return user_input
    except ValueError:
        print('Something went wrong with the program!')

def execute_squaring_program():
    while True:
        user_input = get_int_from_user()
        print(f'You entered {user_input}, that number squared is {user_input * user_input}')

execute_squaring_program()

# try:
#     user_input_raw = input('Give me an integer: ')
#     user_input = int(user_input_raw)
# except ValueError:
#     random_int = random.randint(0, 10)
#     print('Ah, I see you don\'t know what an integer is. Let me pick one for you')
#     print(f'I picked {random_int}, that number squared is {random_int * random_int}')
# else:
#     print(f'You entered {user_input}, that number squared is {user_input * user_input}')
# finally:
#     print('Thank you for using the program, have a nice day!')
