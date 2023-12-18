import time

def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = f'{args} {kwargs}'
        if key in cache_dict:
            print('Found previously computed result!')
            return cache_dict[key]
        else:
            print('Computing new result')
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
    
    return wrapper

print(f'The cache_dict is: {cache_dict}')

@cache
def add_delayed(a, b):
    time.sleep(2)
    return a + b

print(f'The sum of 2 and 3 is {add_delayed(2, 3)}')
print(f'The sum of 2 and 3 is {add_delayed(2, 3)}')
print(f'The sum of 2 and 3 is {add_delayed(2, 3)}')
print(f'The sum of 5 and 3 is {add_delayed(5, 3)}')