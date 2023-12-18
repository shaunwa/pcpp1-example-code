with open('serialization-basics-output.txt', 'a+') as file:
    file.seek(0)
    previous_inputs = file.read()
    print('Here are the previous things you\'ve entered:')
    print(previous_inputs)
    new_input = input('Please enter a new word: ')
    file.write(new_input + '\n')