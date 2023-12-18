def divide(x, y):
    return x / y

def divide_then_add(x, y, z):
    return x + divide(y, z)

def divide_verbose(x, y):
    print(f'{x} divided by {y} is {divide(x, y)}')

def get_number_from_user():
    input_valid = False

    while not input_valid:
        try:
            number_raw = input('Please enter a number:')
            number = float(number_raw)
            input_valid = True
        except ValueError:
            print('Nope that is not a number!')
            input_valid = False
        else:
            return number

def run_divide_program():
    try:
        x = get_number_from_user()
        y = get_number_from_user()
        if y == 0:
            print('No! y cannot be zero! Let me give you one more chance...')
            y = get_number_from_user()
        divide_verbose(x, y)
    except ZeroDivisionError:
        print('NO! Don\'t you dare try dividing by zero!')
    finally:
        print('Thank you for using the divide program!')

run_divide_program()