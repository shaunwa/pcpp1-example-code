def print_on_instance(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            print(f'Creating a new instance of the {cls.__name__} class.')
            super().__init__(*args, **kwargs)
        
    return Wrapper

# @attr_check('name', str)
# @attr_check('age', int)

def attr_check(attr_name, attr_type):
    def decorator(cls):
        class Wrapper(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                if type(getattr(self, attr_name)) != attr_type:
                    raise TypeError(f'The attr {attr_name} must be of type {attr_type}')
        
        return Wrapper

    return decorator

@print_on_instance
class Test:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b 

# t1 = Test(1, 2, 3, 4)
# t1 = Test(1, 2, 3, 4)
# t1 = Test(1, 2, 3, 4)
# t1 = Test(1, 2, 3, 4)

@attr_check('name', str)
@attr_check('age', int)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Shaun', '123')