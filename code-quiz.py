print('Define a function called "add_numbers" that takes 2 numbers as arguments and returns their sum')

lines = []

while True:
    next_line = input()
    if next_line:
        lines.append(next_line)
    else:
        break

program = '\n'.join(lines)

try:
    exec(program)

    result = add_numbers(10, 20)

    if result == 30:
        print('Congratulations! That worked!')
    else:
        print('No, please try again')
except Exception:
    print('No, please try again')