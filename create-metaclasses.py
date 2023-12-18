def create_required_methods_metaclass(required_method_names):
    class NewMetaClass(type):
        def __init__(cls, name, bases, attrs):
            missing_method_names = [method_name for method_name in required_method_names if method_name not in attrs]
            if len(missing_method_names) > 0:
                raise TypeError(f'The class {name} must have methods {missing_method_names}. None was found.')

            super().__init__(name, bases, attrs)

    return NewMetaClass

RequiredABCMethods = create_required_methods_metaclass(['a', 'b', 'c'])

class MyClass(metaclass=RequiredABCMethods):
    def a(self):
        print('This is the a method')

    def b(self):
        print('This is the b method')

    def c(self):
        print('This is the c method')

class AnotherClass(metaclass=create_required_methods_metaclass(['d', 'e', 'f'])):
    pass