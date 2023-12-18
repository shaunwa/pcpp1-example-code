from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'The function {func.__name__} is being called')
        return func(*args, **kwargs)

    return wrapper

@logger
def say_hello():
    print('Hello!')

@logger
def add(x, y):
    return x + y

@logger
def connect_to_db(url):
    print('Connecting to database...')

print(say_hello.__name__)
print(add.__name__)
print(connect_to_db.__name__)

say_hello()
add(1, 2)
connect_to_db('blah')