class Logger:
    def __init__(self, func):
        print(f'Decorating function {func.__name__}...')
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(f'{self.func.__name__} has been called!')
        return self.func(*args, **kwargs)

def log_calls(func):
    print('Setup code!')

    def wrapper(*args, **kwargs):
        print(f'{func.__name__} has been called!')
        return func(*args, **kwargs)
    
    return wrapper

@Logger
def add(a, b):
    return a + b

add(1, 2)
add(2, 3)
add(2, 3)