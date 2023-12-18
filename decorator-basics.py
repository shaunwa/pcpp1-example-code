def debug_logger(verbose=True):
    def decorator(func):
        def wrapper_verbose(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'{func.__name__} has been called with args: {args} and kwargs: {kwargs}, and returned {result}')
            return result

        def wrapper_regular(*args, **kwargs):
            print(f'{func.__name__} has been called!')
            return func(*args, **kwargs)

        return wrapper_verbose if verbose else wrapper_regular
    
    return decorator

def args_are_all(data_type):
    def arg_check_decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) != data_type:
                    raise Exception(f'All args must be {data_type}!')
            for value in kwargs.values():
                if type(arg) != data_type:
                    raise Exception(f'All kwargs must be {data_type}!')

            return func(*args, **kwargs)
        
        return wrapper
    
    return arg_check_decorator

@args_are_all(int)
@debug_logger(verbose=False)
def add(a, b):
    return a + b

@args_are_all(str)
@debug_logger(verbose=False)
def append(str1, str2):
    return str1 + str2

print(add(40, 50))
print(append('Hello,', ' Shaun'))

@debug_logger(verbose=True)
def greet():
    print('Hello my friends!')
