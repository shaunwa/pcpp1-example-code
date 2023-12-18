def create_greeter():
    name = 'Shaun'
    number_of_times = 0

    def greet():
        nonlocal number_of_times
        print(f'Hello, {name}. I have seen you {number_of_times} times today')
        number_of_times += 1

    return greet

f = create_greeter()
f()
f()
f()
f()
f()
f()