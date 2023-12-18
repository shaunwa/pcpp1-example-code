class Greeter:
    def say_hello(self):
        print('Hello!')

class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if not name.startswith('Awesome'):
            raise TypeError('All classes created by MyMetaclass must start with "Awesome"')
        new_bases = bases + (Greeter,)
        return super().__new__(cls, name, new_bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

class AwesomeCar(metaclass=MyMetaclass):
    pass

c = AwesomeCar()
print(AwesomeCar.__name__)
c.say_hello()