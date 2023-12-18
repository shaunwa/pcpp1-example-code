class MyMetaclass(type):
    def __init__(cls, name, bases, attrs):
        print('Creating a class...')
        super().__init__(name, bases, attrs)

class Person(metaclass=MyMetaclass):
    pass

p = Person()