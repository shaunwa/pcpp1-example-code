class MyCustomException(Exception):
    pass

def my_dangerous_function():
    raise MyCustomException('Make sure it is plugged in!')

try:
    my_dangerous_function()
except MyCustomException:
    print('Handling MyCustomException')
except ValueError:
    print('Handling ValueError')
except Exception:
    print('Handling Exception')
