def tell_me_about(thing):
    # print(f'The name is: {getattr(thing, '__name__', 'N/A')}')
    if hasattr(thing, '__name__'):
        print(f'The name of this thing is: {getattr(thing, "__name__")}')

    print(f'Type: {type(thing)}')
    print(f'Class: {thing.__class__}')
    print(f'Is callable?: {callable(thing)}')
    print(f'Attributes and methods: {dir(thing)}')

    if hasattr(thing, '__dict__'):
        print('Attributes:')
        for key, value in thing.__dict__.items():
            print(f'{key}: {value}')

class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def my_class_method(cls):
        my_instance = cls()

    def say_hello(self):
        print('Hello!')

        
my_instance = MyClass(1, 2, 3)

def my_function():
    print('Hello!')

x = 5

tell_me_about(MyClass)
tell_me_about(my_instance)
tell_me_about(my_function)
tell_me_about(x)
