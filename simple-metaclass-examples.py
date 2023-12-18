class MustHaveSayHelloMethod(type):
    def __init__(cls, name, bases, attrs):
        if 'say_hello' not in attrs:
            raise TypeError('This class must have a say_hello method!')
        super().__init__(name, bases, attrs)

class MustInheritFromVehicle(type):
    def __init__(cls, name, bases, attrs):
        if Vehicle not in bases:
            raise TypeError('This class must inherit from Vehicle!')
        super().__init__(name, bases, attrs)

class Vehicle:
    pass

class Car(Vehicle, metaclass=MustInheritFromVehicle):
    def start_up(self):
        print('Vroom!')
    
    def drive(self):
        print('The car begins to move!')

    def say_hello(self):
        print('Beep beep!')